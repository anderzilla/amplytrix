# Amplytrix backend

Python 3.13/FastAPI modular-monolith foundation. FastAPI is an inbound adapter; domain and application layers do not import frameworks, ORM, transport schemas, or providers.

```bash
uv sync --locked
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest
uv run lint-imports
uv run alembic heads
uv run uvicorn amplytrix.main:app --host 0.0.0.0 --port 8080
```

Migrations run as a separately approved Cloud Run Job, never at service startup. No business bounded context is implemented in Phase Zero; `shared` contains only proven cross-cutting contracts and health transport.
