---
name: alembic-migration
description: Create or review safe Amplytrix Alembic migrations and controlled Cloud Run migration-job rollout.
---

# Alembic migration

Use the database-migration skill principles plus SQLAlchemy metadata review. Generate then inspect migration; never trust autogenerate blindly or edit applied revisions. Analyze locks, data volume, tenant constraints, defaults/indexes, downgrade/roll-forward and old/new app compatibility. Test upgrade from previous and clean database using PostgreSQL. Never run at API startup; production Job needs backup, saved artifact and approval.
