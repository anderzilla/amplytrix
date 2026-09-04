# ADR-0062: Project-governed managed service before self-service SaaS

Status: accepted — 2026-09-04

## Context and drivers

Amplytrix must first prove that it can turn incomplete evidence into comparable scenarios, a
human-approved baseline, governed execution, and an auditable delivery. The existing engineering
SaaS foundation did not make the project, its contractual boundary, provenance, contrary evidence,
or human decisions first-class. The Founder authorized a transversal architecture update and the
"Construção da Amplytrix" project as the first complete dogfood case.

Drivers are project-level isolation, traceability, low initial operating cost, reversibility,
managed-service delivery before portal automation, and strict separation from CodeMatrix corporate
management. RULE-034 and DEC-035 in the CodeMatrix Blueprint require a primary owner and an
independent reviewer linked to the same task and governance commit.

## Options considered

1. **Keep the subscription/catalog architecture unchanged.** Lowest implementation cost, but it
   leaves discovery, decisions, evidence, and scope governance outside the product and cannot prove
   the promised method.
2. **Create separate services and portals for every plane now.** Strong deployment isolation, but
   introduces multiple databases, contracts, observability surfaces, cloud cost, and operational
   load before usage evidence exists.
3. **Extend the modular monolith around a project-governed method and begin with declarative
   dogfooding. Selected.** Phase Zero adds versioned contracts, registries, knowledge provenance,
   scenarios, decisions, evidence, and supervision without persistence or provider integration.
   Later runtime slices remain modules until measured isolation, scale, ownership, or release needs
   justify extraction.

## Decision

The project is Amplytrix's unit of governance and data isolation. The initial commercial modality is
a CodeMatrix-managed end-to-end service. Package review and subscription self-service remain later
modalities and cannot weaken project/contract gates.

Candidate contexts are Project Governance, Discovery & Scenarios, Knowledge & Provenance,
Capability Registry, Execution Orchestration, Evidence & Supervision, and Audit & Compliance.
Identity remains an external adapter boundary. These contexts start as declarative contracts and
candidate modules; Event Storming and a walking slice are required before persistence modules are
created.

Project intake accepts an Agency briefing, client documents, third-party documents, or direct
discovery. The Agency path is commercially preferred but not mandatory. Every input remains
untrusted until a CodeMatrix internal readiness check validates minimum completeness, coherence,
risks, and gaps. That minimum gate does not imply delivery of the Agency's full commercial
diagnostic/documentation; packaging and price remain a management decision. Agency-originated input
uses a versioned handoff with origin, transfer basis/consent where applicable, evidence, and
idempotency.

The minimum check records an effort estimate, cost attribution, and commercial disposition subject
to human approval. Client-document validation is attributable Agency process in the Amplytrix
composition, not invisible/free work. Material gaps require a paid Agency diagnostic or a scoped
Amplytrix discovery phase. No fixed price/hours or automatic charge/accounting transfer is decided.

The backend remains a Python/FastAPI modular monolith. PostgreSQL remains the future system of
record with owned schemas and mandatory project scope; Cloud Storage remains the artifact target.
Cloud Tasks and Cloud Run Jobs retain their accepted roles. A separate execution service, sandbox,
or customer/operations frontend is introduced only by a later accepted decision. No database is
shared with CodeMatrix Agency: integration uses versioned APIs/events, correlation and idempotency.

Phase Zero is repository-driven. It provides JSON Schemas, declarative capability/MCP registries,
the Amplytrix construction project package, deterministic validation, and governance evidence. It
does not provision cloud resources, collect personal data, activate MCPs, or implement product
runtime.

## Consequences

Benefits: the method can be exercised immediately at zero external cost; decisions and contrary
evidence become inspectable; runtime choices remain reversible; CodeMatrix and client ownership
boundaries are explicit. Costs: more documentation and validation maintenance, manual orchestration,
and temporary duplication between project artifacts and future persistence models.

Security/privacy improve through deny-default capability admission, source allowlists, project
segregation, and human approvals. Residual risks include declarative policy not matching a future
runtime, malicious retrieved content, reviewer collusion, and accidental inclusion of restricted
data. Automated relationship checks and independent review reduce but do not eliminate them.

Financial cost is repository/CI time only. Any cloud, provider, identity, vector, or MCP activation
requires a separate cost and approval gate. Legal review remains required before client data,
contracts, reuse, retention, or anonymization is operationalized.

## Reversibility, validation, and revisit triggers

Artifacts are versioned files and can be superseded without data migration. Validate JSON parsing,
schema conventions, cross-file references, project/reviewer invariants, source provenance, MCP
deny-default state, repository gates, and independent review. Revisit when the first managed project
requires persistence, a real external integration, concurrent execution, customer access, or when
measured isolation/scale requires separate deployables.
