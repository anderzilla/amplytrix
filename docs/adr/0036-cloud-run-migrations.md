# ADR-0036: Controlled Cloud Run migration job

Status: accepted — 2026-08-01

Never migrate at API startup. CI builds an immutable migration image; staging runs expand-compatible migrations, verifies, then production requires human approval and a dedicated Cloud Run Job identity. Contract/removal migrations follow only after old revisions are gone. Backups, lock/time estimates and roll-forward/rollback are mandatory.
