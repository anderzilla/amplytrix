# ADR-0030: Python modular monolith

Status: accepted — 2026-08-01

Bounded contexts share one FastAPI deployment but own domain/application/infrastructure/presentation internals and data. Cross-context access uses published contracts, not table/internal imports. Extraction requires independent scaling, security, ownership or release evidence. No placeholder context directory is created before discovery.
