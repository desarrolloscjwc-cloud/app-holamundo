# app-holamundo

Hola mundo para probar el pipeline de punta a punta. App en Python (solo biblioteca estándar) pensada para Cloud Run.

## Endpoints

| Ruta          | Respuesta                         |
|---------------|-----------------------------------|
| `GET /`       | 200 `Hola mundo desde Cloud Run`  |
| `GET /health` | 200 `ok`                          |
| otras         | 404                               |

## Correr localmente

```bash
python -m app.main            # puerto 8080 por defecto
PORT=9000 python -m app.main  # puerto personalizado
curl localhost:8080/
```

Escucha en `0.0.0.0` y en el puerto de la variable `PORT`.

## Pruebas

```bash
python -m unittest discover -s tests
```

## Docker

```bash
docker build -t app-holamundo .
docker run --rm -p 8080:8080 app-holamundo
```
