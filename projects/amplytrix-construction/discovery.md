# Discovery record

## Facts

- A clean, synchronized private Amplytrix checkout already contains a Next.js/FastAPI/PostgreSQL/
  Cloud Run foundation, governance gates, catalog/entitlements scaffolding, agents, and skills.
- The Founder selected a project-centered managed service as the first MVP and authorized this
  transversal architecture update.
- Agency briefing is a preferred prepared input, not a mandatory purchase. Every input origin is
  untrusted until the internal readiness gate.
- RULE-034/DEC-035 require a primary owner and independent exact-target review.

## Assumptions to validate

- Repository artifacts are sufficient to operate the first Phase Zero without a portal.
- A modular monolith remains cheaper and safer than early service extraction.
- Project-level isolation can be implemented in one PostgreSQL database without unacceptable risk;
  persistence work remains blocked until Event Storming and isolation tests.

## Conflicts and gaps

- The older subscription-first vision conflicted with the managed-service-first definition; ADR-0062
  resolves current priority while preserving self-service as a later modality.
- Identity provider, retention details, RLS, RTO/RPO, traffic/cost, and vector strategy remain open.
- The separate wiki contains unrelated local changes and cannot be synchronized safely in this task.
