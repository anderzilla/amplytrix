# Architecture

The modular-monolith and inward dependency rules in ADR-0004 and ADR-0023–0039 remain current.
ADR-0062 makes the project the governance and isolation unit and establishes managed-service-first
dogfooding before persistence, API, UI, or self-service automation.

ADR-0063 adds a project-local, schema-validated known-error library and a constrained librarian
agent. Only evidence-backed sanitized patterns may be recorded. Cross-project or client-facing reuse
is a later human-approved projection, never direct access to another project's records.

Project Governance, Discovery & Scenarios, Knowledge & Provenance, Capability Registry, Execution
Orchestration, Evidence & Supervision, and Audit & Compliance are candidate boundaries. They
communicate through application ports and versioned contracts, never internal tables. CodeMatrix
Agency and Amplytrix have separate authentication, data, and runtime ownership; integration is only
through versioned APIs/events with correlation, idempotency, and explicit data classification.

Structural changes require a prompt beginning `ATUALIZAÇÃO DE ARQUITETURA`, affected scope
confirmation, problem/options/pros/cons, and technical, operational, financial, security, legal, and
future-consequence analysis. Wait for human selection; then use `architecture/<name>` from `develop`,
create/supersede an ADR, synchronize diagrams/tests/docs/wiki, and validate. No silent architectural
change.
