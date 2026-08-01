"""Create the versioned commercial catalog foundation.

Revision ID: 20260801_0001
Revises:
Create Date: 2026-08-01
"""

# ruff: noqa: E501

from collections.abc import Sequence

from alembic import op

from amplytrix.catalog.infrastructure.database import CatalogBase

revision: str = "20260801_0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA catalog")
    CatalogBase.metadata.create_all(bind=op.get_bind(), checkfirst=False)
    statements = (
        """
        INSERT INTO catalog.products (id, code, name)
        VALUES ('00000000-0000-4000-8000-000000000001', 'amplytrix', 'Amplytrix')
        """,
        """
        INSERT INTO catalog.plans (id, product_id, code, slug, name) VALUES
        ('00000000-0000-4000-8000-000000000101', '00000000-0000-4000-8000-000000000001', 'free', 'free', 'Free'),
        ('00000000-0000-4000-8000-000000000102', '00000000-0000-4000-8000-000000000001', 'pro_trial', 'pro-trial', 'Pro Trial'),
        ('00000000-0000-4000-8000-000000000103', '00000000-0000-4000-8000-000000000001', 'pro', 'pro', 'Pro'),
        ('00000000-0000-4000-8000-000000000104', '00000000-0000-4000-8000-000000000001', 'team', 'team', 'Team'),
        ('00000000-0000-4000-8000-000000000105', '00000000-0000-4000-8000-000000000001', 'premium_architecture', 'premium-architecture', 'Premium Architecture')
        """,
        """
        INSERT INTO catalog.plan_versions (id, plan_id, version, status) VALUES
        ('00000000-0000-4000-8000-000000000201', '00000000-0000-4000-8000-000000000101', '1.0.0', 'published'),
        ('00000000-0000-4000-8000-000000000202', '00000000-0000-4000-8000-000000000102', '1.0.0', 'published'),
        ('00000000-0000-4000-8000-000000000203', '00000000-0000-4000-8000-000000000103', '1.0.0', 'published'),
        ('00000000-0000-4000-8000-000000000204', '00000000-0000-4000-8000-000000000104', '1.0.0', 'published'),
        ('00000000-0000-4000-8000-000000000205', '00000000-0000-4000-8000-000000000105', '1.0.0', 'published')
        """,
        """
        INSERT INTO catalog.prices
          (id, plan_version_id, amount_minor, currency, billing_period, hypothesis, status)
        VALUES
        ('00000000-0000-4000-8000-000000000301', '00000000-0000-4000-8000-000000000201', 0, 'BRL', 'month', true, 'published'),
        ('00000000-0000-4000-8000-000000000303', '00000000-0000-4000-8000-000000000203', 9900, 'BRL', 'month', true, 'draft'),
        ('00000000-0000-4000-8000-000000000304', '00000000-0000-4000-8000-000000000204', 29900, 'BRL', 'month', true, 'draft'),
        ('00000000-0000-4000-8000-000000000305', '00000000-0000-4000-8000-000000000205', 99900, 'BRL', 'month', true, 'draft')
        """,
    )
    for statement in statements:
        op.execute(statement)


def downgrade() -> None:
    CatalogBase.metadata.drop_all(bind=op.get_bind(), checkfirst=False)
    op.execute("DROP SCHEMA catalog")
