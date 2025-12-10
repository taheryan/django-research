# Simple Dockerfile for the Django my_tennis_club
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install build deps for some wheels (if needed) and pipenv packages
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY . /code/

# Run migrations at container start may be handled by entrypoint or orchestrator;
# keep a migrate step to ensure DB is ready for quick local testing in containers.
RUN python manage.py migrate --no-input || true

EXPOSE 8000

CMD ["gunicorn", "my_tennis_club.wsgi:application", "--bind", "0.0.0.0:8000"]