# ADR-0053: Organization-scoped multi-tenancy

Status: accepted — 2026-08-01

## Context and decision

Organization is the tenant, including personal organizations; tenant rows are non-null scoped and repositories derive scope from auth context. RLS is deferred to benchmark. User tenancy and database-per-tenant were rejected.

## Consequences and validation

Uniform model supports teams; shared-database leakage is critical risk. Compound constraints and adversarial tenant tests gate implementation.
