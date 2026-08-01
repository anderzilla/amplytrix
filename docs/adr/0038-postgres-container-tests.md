# ADR-0038: Real PostgreSQL integration tests

Status: accepted — 2026-08-01

Repository and migration tests use disposable PostgreSQL/Testcontainers or an isolated CI service, never SQLite substitution or shared/production databases. Phase Zero has no persistence adapter, so the integration suite is intentionally documented but empty. First repository must add clean-schema, migration and concurrency tests.
