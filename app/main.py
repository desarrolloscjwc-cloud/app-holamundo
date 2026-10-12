"""Servidor HTTP "Hola mundo" usando solo la biblioteca estándar."""
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def get_response(path):
    """Devuelve (status, cuerpo) para una ruta. No depende del servidor."""
    route = path.split("?", 1)[0]
    if route == "/":
        return 200, "Hola mundo desde Cloud Run"
    if route == "/health":
        return 200, "ok"
    return 404, "Not Found"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, body = get_response(self.path)
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main():
    port = int(os.environ.get("PORT", "8080"))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Escuchando en 0.0.0.0:{port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
