# Backend

Python 3.13/FastAPI is the primary API in a modular monolith. Routers are thin; use cases and ports face inward; SQLAlchemy/Alembic/provider models remain infrastructure. External calls require timeout, bounded retry, validation and telemetry. PostgreSQL integration tests use disposable PostgreSQL, never SQLite. See ADR-0023–0039.
