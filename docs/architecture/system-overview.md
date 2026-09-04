# System overview

Amplytrix begins as a repository-driven managed-service method, followed by a Next.js web service and
a Python 3.13/FastAPI modular-monolith API. The project is the governance and isolation unit. Finite
administrative/execution work will use Cloud Run Jobs; explicit scheduled/retried delivery uses Cloud
Tasks. PostgreSQL is the future system of record and object artifacts use Cloud Storage. External
identity, payment, source-control, model, and CodeMatrix Agency systems sit behind application ports
and Anti-Corruption Layers. No provider integration is implemented in Phase Zero.

Dependency rule: FastAPI presentation and SQLAlchemy/provider infrastructure depend on application; application depends on domain/ports; domain depends only on Python's standard library. FastAPI-generated OpenAPI is the frontend contract, never the domain model.

The customer portal and Amplytrix operations console are separate security surfaces. Phase Zero has
neither. Their deployment topology is decided only before UI implementation; shared code cannot
grant shared authorization. Corporate management remains in CodeMatrix Agency and the systems share
neither database nor internal service credentials.
