# Billing test strategy

Domain tests cover catalog immutability, price/version windows, canonical transitions, resolver precedence/deny fallback and balanced credit ledger. Application tests use fake providers for retry, duplicate, out-of-order, compensation and concurrency. PostgreSQL integration tests verify schemas, constraints, tenant isolation, outbox/inbox, locking and migrations; SQLite is prohibited.

Contract/adversarial tests verify both provider webhook modes, signatures, limits, replay, timeouts and status mapping. HTTP tests cover authz, CSRF, idempotency, enumeration, mass assignment and stable errors. E2E covers Free, trial expiry/conversion, paid activation, failure/grace/recovery, previewed upgrade/downgrade, cancel/resume/refund and export.

Load tests use the formulas in the scalability study for journey mix, webhook bursts, usage ingestion and queue backlog; assert latency/error/saturation/connection budgets without inventing capacity. Restore/reconciliation/dead-letter drills and commercial-integrity review gate release.
