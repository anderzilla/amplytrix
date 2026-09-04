# ADR-0051: Commercial modules remain in the modular monolith

Status: accepted — 2026-08-01

## Context and decision

Catalog, entitlement, billing, trials and usage are modules in the existing FastAPI deployment initially. Microservices and a shared undifferentiated module were rejected.

## Consequences and validation

Local operation/transactions are simpler; module boundaries need automated import/table ownership tests. Specializes ADR-0004; extraction needs measured scale, security, ownership or release independence.
