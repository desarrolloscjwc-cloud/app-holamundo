FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app

RUN useradd --create-home --uid 1001 appuser
USER appuser

EXPOSE 8080
CMD ["python", "-m", "app.main"]
