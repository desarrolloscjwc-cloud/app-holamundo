import threading
import unittest
import urllib.error
import urllib.request
from http.server import HTTPServer

from app.main import Handler, get_response


class GetResponseTest(unittest.TestCase):
    def test_root(self):
        self.assertEqual(get_response("/"), (200, "Hola mundo desde Cloud Run"))

    def test_health(self):
        self.assertEqual(get_response("/health"), (200, "ok"))

    def test_unknown(self):
        self.assertEqual(get_response("/otra")[0], 404)

    def test_query_string_ignored(self):
        self.assertEqual(get_response("/health?x=1"), (200, "ok"))


class ServerTest(unittest.TestCase):
    def test_http(self):
        srv = HTTPServer(("127.0.0.1", 0), Handler)
        t = threading.Thread(target=srv.serve_forever, daemon=True)
        t.start()
        base = f"http://127.0.0.1:{srv.server_address[1]}"
        try:
            with urllib.request.urlopen(base + "/") as r:
                self.assertEqual(r.status, 200)
                self.assertEqual(r.read().decode(), "Hola mundo desde Cloud Run")
            with self.assertRaises(urllib.error.HTTPError) as c:
                urllib.request.urlopen(base + "/nada")
            self.assertEqual(c.exception.code, 404)
        finally:
            srv.shutdown()
            srv.server_close()


if __name__ == "__main__":
    unittest.main()
