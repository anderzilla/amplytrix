# syntax=docker/dockerfile:1.7
FROM ghcr.io/astral-sh/uv:0.11.17 AS uv
FROM python:3.13-alpine AS build
COPY --from=uv /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app
COPY pyproject.toml uv.lock README.md ./
COPY src ./src
RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked --no-dev --no-editable

FROM python:3.13-alpine AS runtime
ENV PATH=/app/.venv/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080
RUN apk upgrade --no-cache \
    && addgroup --system --gid 10001 app \
    && adduser --system --uid 10001 --ingroup app --home /nonexistent --shell /sbin/nologin app
WORKDIR /app
COPY --from=build --chown=app:app /app/.venv .venv
USER 10001:10001
EXPOSE 8080
CMD ["sh", "-c", "exec uvicorn amplytrix.main:app --host 0.0.0.0 --port ${PORT:-8080} --workers 1 --timeout-graceful-shutdown 10"]
