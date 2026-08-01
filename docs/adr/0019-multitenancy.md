# ADR-0019: Future tenant isolation

Status: proposed — 2026-08-01

Start with tenant identity propagated through every use case and explicit authorization; likely shared schema with mandatory tenant keys and composite constraints. Evaluate PostgreSQL RLS as defense in depth. Enterprise database-per-tenant remains possible. Decide after compliance, scale, noisy-neighbor, analytics, migration, and restore requirements.
