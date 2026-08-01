# ADR-0052: PostgreSQL schemas by bounded context

Status: accepted — 2026-08-01

## Context and decision

Use one PostgreSQL database and owned logical schemas with SQLAlchemy/Alembic; no cross-context table access. Database-per-context and public-schema sharing were rejected for MVP.

## Consequences and validation

Clear ownership with low operational cost; migrations and transaction boundaries need discipline. Validate disposable PostgreSQL migrations, FKs/constraints and ownership tests.
