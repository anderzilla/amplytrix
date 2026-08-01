## Purpose and scope

Describe problem, outcome, exclusions, linked issue/spec/ADR, and rollback.

- Scope: frontend / backend / infrastructure / transversal
- Commercial objective and metric:
- Source-of-truth/ADR impact:
- UX, accessibility, i18n and communication impact:
- Security, privacy and abuse impact:
- Monetization, retention and gamification impact:

## Evidence

- [ ] Format, lint, typecheck, tests, architecture tests and build passed
- [ ] Relevant docs/contracts/diagrams/migrations are synchronized
- [ ] No secret, personal data, production credential, or unrelated change
- [ ] Dependency/license and cost impact reviewed when applicable

## Security checklist

- [ ] Inputs validated; server authorization and tenant scope deny by default
- [ ] Logs/errors redact secrets and personal data; correlation remains useful
- [ ] Injection, CSRF/SSRF/XSS, replay/idempotency, abuse/rate/cost considered
- [ ] Threat model and security tests updated for changed trust boundaries
- [ ] External, irreversible, production, or paid actions have human approval
