---
name: database-migration
description: Design, create, validate, or review safe versioned PostgreSQL and Drizzle migrations for Amplytrix.
---

# Database migration

Classify change/volume/lock/tenant risk. Prefer expand-migrate-contract: additive nullable/default-safe schema, compatible app, resumable backfill, verification, later constraint/removal. Never edit applied migrations. Specify transaction, timeout, index strategy, rollback/roll-forward, backup and observability. Test from clean and prior schema with disposable PostgreSQL. Destructive or long-lock changes require human approval.
