from datetime import datetime
from uuid import UUID

from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    String,
    Text,
    Uuid,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class CatalogBase(DeclarativeBase):
    pass


class ProductRow(CatalogBase):
    __tablename__ = "products"
    __table_args__ = ({"schema": "catalog"},)

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    code: Mapped[str] = mapped_column(String(80), unique=True)
    name: Mapped[str] = mapped_column(String(160))


class CatalogItemRow(CatalogBase):
    __tablename__ = "catalog_items"
    __table_args__ = ({"schema": "catalog"},)

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    product_id: Mapped[UUID] = mapped_column(ForeignKey("catalog.products.id"))
    code: Mapped[str] = mapped_column(String(100), unique=True)
    slug: Mapped[str] = mapped_column(String(120), unique=True)
    item_type: Mapped[str] = mapped_column(String(40))
    category: Mapped[str] = mapped_column(String(80))


class CatalogItemVersionRow(CatalogBase):
    __tablename__ = "catalog_item_versions"
    __table_args__ = (
        CheckConstraint("status in ('draft','published','retired')"),
        CheckConstraint(
            "commercial_visibility in "
            "('internal','free','trial','paid','premium','invite_only','deprecated')"
        ),
        {"schema": "catalog"},
    )

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    catalog_item_id: Mapped[UUID] = mapped_column(ForeignKey("catalog.catalog_items.id"))
    version: Mapped[str] = mapped_column(String(32))
    name: Mapped[str] = mapped_column(String(160))
    short_description: Mapped[str] = mapped_column(String(300))
    commercial_description: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20))
    commercial_visibility: Mapped[str] = mapped_column(String(20))
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    retired_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))


class FeatureRow(CatalogBase):
    __tablename__ = "features"
    __table_args__ = ({"schema": "catalog"},)

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    code: Mapped[str] = mapped_column(String(100), unique=True)
    name: Mapped[str] = mapped_column(String(160))


class PlanRow(CatalogBase):
    __tablename__ = "plans"
    __table_args__ = ({"schema": "catalog"},)

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    product_id: Mapped[UUID] = mapped_column(ForeignKey("catalog.products.id"))
    code: Mapped[str] = mapped_column(String(80), unique=True)
    slug: Mapped[str] = mapped_column(String(100), unique=True)
    name: Mapped[str] = mapped_column(String(160))


class PlanVersionRow(CatalogBase):
    __tablename__ = "plan_versions"
    __table_args__ = (
        CheckConstraint("status in ('draft','published','retired')"),
        {"schema": "catalog"},
    )

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    plan_id: Mapped[UUID] = mapped_column(ForeignKey("catalog.plans.id"))
    version: Mapped[str] = mapped_column(String(32))
    status: Mapped[str] = mapped_column(String(20))


class PriceRow(CatalogBase):
    __tablename__ = "prices"
    __table_args__ = (
        CheckConstraint("amount_minor >= 0"),
        CheckConstraint("char_length(currency) = 3"),
        CheckConstraint("status in ('draft','published','retired')"),
        {"schema": "catalog"},
    )

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    plan_version_id: Mapped[UUID] = mapped_column(ForeignKey("catalog.plan_versions.id"))
    amount_minor: Mapped[int] = mapped_column(BigInteger)
    currency: Mapped[str] = mapped_column(String(3))
    billing_period: Mapped[str] = mapped_column(String(20))
    hypothesis: Mapped[bool] = mapped_column(Boolean, default=True)
    status: Mapped[str] = mapped_column(String(20))


class PlanFeatureRow(CatalogBase):
    __tablename__ = "plan_features"
    __table_args__ = ({"schema": "catalog"},)

    plan_version_id: Mapped[UUID] = mapped_column(
        ForeignKey("catalog.plan_versions.id"), primary_key=True
    )
    feature_id: Mapped[UUID] = mapped_column(ForeignKey("catalog.features.id"), primary_key=True)


class PlanLimitRow(CatalogBase):
    __tablename__ = "plan_limits"
    __table_args__ = (CheckConstraint("limit_value >= 0"), {"schema": "catalog"})

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    plan_version_id: Mapped[UUID] = mapped_column(ForeignKey("catalog.plan_versions.id"))
    feature_id: Mapped[UUID] = mapped_column(ForeignKey("catalog.features.id"))
    limit_value: Mapped[int] = mapped_column(BigInteger)
    unit: Mapped[str] = mapped_column(String(40))


class AddOnRow(CatalogBase):
    __tablename__ = "add_ons"
    __table_args__ = ({"schema": "catalog"},)

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    product_id: Mapped[UUID] = mapped_column(ForeignKey("catalog.products.id"))
    code: Mapped[str] = mapped_column(String(80), unique=True)
    name: Mapped[str] = mapped_column(String(160))
