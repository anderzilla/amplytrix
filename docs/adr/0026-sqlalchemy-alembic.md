# ADR-0026: SQLAlchemy 2 and Alembic

Status: accepted — 2026-08-01

Use SQLAlchemy 2 only in infrastructure and Alembic for immutable migrations. Aggregate-specific repository ports face inward; ORM models, sessions and tables never become domain or HTTP models. A universal generic repository is prohibited. PostgreSQL remains the production/local integration target.
