# Clean Architecture

Domain owns ubiquitous language and invariants using framework-free Python entities, value objects, aggregates, policies and events. Application orchestrates typed commands/queries and defines ports. Infrastructure implements ports with SQLAlchemy/provider SDKs. FastAPI presentation validates Pydantic HTTP schemas and maps results/errors. Mapping is explicit; HTTP, application, domain, persistence and provider models are not reused automatically. Abstract only an observed or explicitly planned boundary variation.
