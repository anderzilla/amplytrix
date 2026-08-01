# ADR-0039: Isolate domain, application, HTTP, persistence and provider models

Status: accepted — 2026-08-01

Each boundary owns its representation and explicit mapping. Domain objects protect invariants; application DTOs express use cases; Pydantic schemas express HTTP; SQLAlchemy models express storage; provider models remain adapter-local. Duplication that prevents semantic coupling is intentional and tested at mappings.
