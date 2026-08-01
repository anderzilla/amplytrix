# ADR-0024: FastAPI as an inbound HTTP adapter

Status: accepted — 2026-08-01

FastAPI owns transport validation, context, error mapping and OpenAPI only. Routers call application use cases and never contain business rules or concrete repositories. Flask offers less native typing/OpenAPI; Django adds persistence/framework coupling not needed. Framework imports are forbidden in domain.
