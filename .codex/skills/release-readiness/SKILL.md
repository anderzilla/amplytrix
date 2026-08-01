---
name: release-readiness
description: Evaluate an Amplytrix release candidate for go or no-go using gates, compatibility, migrations, security, observability, and rollback evidence.
---

# Release readiness

Identify exact commit/image digest/version and change set. Verify CI/tests/scans/SBOM/licenses, contract compatibility, migrations/backups, config/secrets, staging smoke, monitoring/alerts, capacity/cost, release notes, approvals and rollback rehearsal. Never deploy. Return go/no-go/conditional with blockers, evidence and owners; any failed critical gate is no-go unless a human explicitly accepts risk.
