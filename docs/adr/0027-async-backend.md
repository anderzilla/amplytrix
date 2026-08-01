# ADR-0027: Selective async I/O

Status: accepted — 2026-08-01

Use async FastAPI handlers and SQLAlchemy/asyncpg/provider adapters for concurrent I/O. Keep pure domain logic synchronous and do not introduce async merely for consistency. CPU-heavy work moves to jobs. Every external call needs timeout, bounded retry, destination validation and telemetry.
