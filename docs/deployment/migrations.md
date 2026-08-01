# Database migration deployment

Alembic never runs during FastAPI startup. Use expand/migrate/contract: create backward-compatible structure, deploy compatible code, run resumable backfill, verify, then remove only after old revisions are retired. CI validates revision graph and PostgreSQL upgrade tests. Staging executes an immutable migration image; production requires backup/PITR confirmation, lock/time estimate, dedicated least-privilege Cloud Run Job identity, human approval and post-check. Prefer roll-forward; downgrade is tested where safe.
