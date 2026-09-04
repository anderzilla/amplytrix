# Pull request policy

Every PR states scope, commercial objective, risk/data class, source-of-truth and ADR impact, tests, security/privacy, UX/accessibility/i18n/communication, monetization/gamification when applicable, observability, migration/rollback and documentation/wiki impact. Generated evidence must be reproducible.

Task/architecture PRs target `develop`; promotion PRs contain only accumulated reviewed changes. Architecture/security-sensitive changes expect two approvals including the owner when the GitHub plan supports it. Do not merge with pending/failing checks, unresolved BLOCKER/CRITICAL/HIGH, unjustified MEDIUM, stale documentation, incompatible contracts or unsafe migrations.
