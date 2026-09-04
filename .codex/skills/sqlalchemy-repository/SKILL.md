---
name: sqlalchemy-repository
description: Implement or review an aggregate-specific SQLAlchemy 2 repository adapter with explicit domain-persistence mapping and PostgreSQL tests.
---

# SQLAlchemy repository

Start from an inward Protocol needed by a use case. Design infrastructure-only table/mapping, explicit hydrate/dehydrate functions, tenant constraints, transaction/UoW ownership and concurrency. Use SQLAlchemy 2 typed APIs; no universal generic repository, session in domain, lazy-load surprise or ORM object across boundary. Test against disposable PostgreSQL including constraints, round-trip, not-found, rollback and concurrency relevant to the invariant.
