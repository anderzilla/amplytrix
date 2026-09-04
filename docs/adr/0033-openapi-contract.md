# ADR-0033: OpenAPI as frontend-backend contract

Status: accepted — 2026-08-01

FastAPI-generated OpenAPI 3.1 is authoritative. Commit a deterministic snapshot, validate it in CI and detect breaking changes. Do not manually duplicate Python/TypeScript transport types. Domain models remain absent from the schema unless explicitly mapped.
