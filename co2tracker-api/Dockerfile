FROM python:3.13-slim as base
FROM base as builder

# Allows docker to cache installed dependencies between builds
RUN apt-get update && apt-get -y install libpq-dev gcc
COPY ./requirements.txt requirements.txt

COPY --from=ghcr.io/astral-sh/uv:0.6.17 /uv /uvx /bin/
COPY pyproject.toml uv.lock /_lock/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    UV_PROJECT_ENVIRONMENT=/app/.venv \
    PYTONPATH=/app/.venv/lib/python3.13/site-packages

RUN --mount=type=cache,target=/root/.cache \
    cd /_lock && \
    uv sync \
    --frozen \
    --no-install-project

FROM base as runtime
# Copy uv binary to runtime stage
COPY --from=ghcr.io/astral-sh/uv:0.6.17 /uv /uvx /bin/

# Create nonroot user first
RUN useradd -m nonroot

# Copy the virtual environment from builder stage and set ownership
COPY --from=builder --chown=nonroot:nonroot /app/.venv /app/.venv

ENV PYTHONPATH=/app/.venv/lib/python3.13/site-packages

# Switch to nonroot user
USER nonroot

# Set working directory and copy project files
WORKDIR /app
COPY --chown=nonroot:nonroot . /app/

EXPOSE 8000
# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - co2tracker.wsgi:application
