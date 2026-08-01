# ADR-0040: Development governance, protected branch flow and homologation gate

Status: accepted — 2026-08-01

## Context and drivers

Amplytrix needs traceable promotion, compact operational guidance, repeatable quality evidence, and commercially strong behavior that preserves user autonomy and trust. Drivers are auditability, defect containment, LGPD readiness, predictable cost, documentation economy, and healthy recurring revenue.

## Alternatives

1. Keep informal branches and reviewer judgment: cheapest initially, but inconsistent and unauditable.
2. Use only `develop` and `master`: simpler, but removes a distinct homologation decision.
3. Adopt protected `develop -> homolog -> master` with task/architecture entry branches, automated and manual gates: more CI and administration, but explicit promotion evidence. **Selected.**

## Decision

Use permanent lowercase `develop`, `homolog`, and `master`; `master` is default and production-approved. Allow only `task/*|architecture/* -> develop`, `develop -> homolog`, and `homolog -> master`, through PRs. Required governance and quality checks block invalid flow and blocker/critical/high findings. Rulesets enforce deletion/force-push/direct-update restrictions and approvals where the GitHub plan supports them.

`PROJECT_CONSTITUTION.md` is supreme; `docs/source-of-truth/` holds current operational decisions; ADRs hold history; implementation follows both. The repository is authoritative and the Wiki is a synchronized reader-friendly projection.

Monetization must be assertive, measurable, transparent, consent-based, reversible, and value-producing. Dark patterns, harmful dependency, fabricated evidence, hidden renewal/cost, obstructed exit, data captivity, and coercive gamification are prohibited.

## Consequences

Positive: traceable releases, earlier defects, explicit ownership, reusable guidance, safer monetization. Negative: additional PRs, CI minutes, review latency, administrative maintenance, and possible gate deadlock. Financial cost is limited initially to Actions usage and review time; later visual/E2E infrastructure requires budget approval. Legal controls reduce but do not replace LGPD, consumer-law, pricing, and automated-decision counsel. Security improves through deny-default flow, though compromised administrators and third-party Actions remain risks.

The decision is reversible only through a superseding ADR and architecture update. Legacy `main`, `Develop`, `Homolog`, and `Master` remain temporarily without new work until safe archival/deletion is separately approved after consumers and links migrate.

## Validation and operations

Run `pnpm validate:governance`, normal CI, the develop-to-homolog gate, manual checklist, link checks, and ruleset inspection. Revisit when hotfix time objectives, team size, GitHub plan constraints, CI cost, regulatory advice, or measured promotion latency make the flow unsafe or disproportionate.
