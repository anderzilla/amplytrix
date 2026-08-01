# System overview

Amplytrix begins with a Next.js web service and a Python 3.13/FastAPI modular-monolith API; finite administrative work will use Cloud Run Jobs. PostgreSQL is the system of record and object artifacts use Cloud Storage. External identity, payment, source-control and model providers sit behind Python application ports/Anti-Corruption Layers. No provider integration is implemented in Phase Zero.

Dependency rule: FastAPI presentation and SQLAlchemy/provider infrastructure depend on application; application depends on domain/ports; domain depends only on Python's standard library. FastAPI-generated OpenAPI is the frontend contract, never the domain model.
