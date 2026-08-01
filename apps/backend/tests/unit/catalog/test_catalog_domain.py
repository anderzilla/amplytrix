from uuid import uuid4

import pytest

from amplytrix.catalog.domain import (
    AddOn,
    CatalogItem,
    CatalogItemVersion,
    CatalogStatus,
    CommercialVisibility,
    Money,
    Plan,
    PlanLimit,
    PlanVersion,
    Price,
    Product,
    SemanticVersion,
)


def item_version(version: SemanticVersion, *, internal: bool = False) -> CatalogItemVersion:
    return CatalogItemVersion(
        id=uuid4(),
        version=version,
        name="Code Review",
        short_description="Review with evidence",
        commercial_description="Finds actionable risks with evidence.",
        visibility=CommercialVisibility.INTERNAL if internal else CommercialVisibility.PAID,
    )


def test_catalog_item_requires_monotonically_increasing_versions() -> None:
    item = CatalogItem(id=uuid4(), code="code_review", slug="code-review")
    item.add_version(item_version(SemanticVersion(1, 0, 0)))
    with pytest.raises(ValueError, match="increase"):
        item.add_version(item_version(SemanticVersion(0, 9, 0)))


def test_public_catalog_excludes_drafts_and_internal_items() -> None:
    item = CatalogItem(id=uuid4(), code="code_review", slug="code-review")
    item.add_version(item_version(SemanticVersion(1, 0, 0), internal=True).publish())
    item.add_version(item_version(SemanticVersion(1, 1, 0)))
    assert item.public_version() is None


def test_published_version_is_immutable_and_public() -> None:
    draft = item_version(SemanticVersion(1, 0, 0))
    published = draft.publish()
    item = CatalogItem(id=uuid4(), code="code_review", slug="code-review")
    item.add_version(published)
    assert draft.status is CatalogStatus.DRAFT
    assert item.public_version() == published


def test_plan_version_cannot_be_replaced_in_place() -> None:
    plan = Plan(id=uuid4(), code="pro", slug="pro")
    version = PlanVersion(
        id=uuid4(),
        version=SemanticVersion(1, 0, 0),
        status=CatalogStatus.PUBLISHED,
        feature_codes=frozenset({"ask_project"}),
        limits=(),
    )
    plan.add_version(version)
    with pytest.raises(ValueError, match="already exists"):
        plan.add_version(version)


def test_price_uses_minor_units_and_requires_hypothesis() -> None:
    amount = Money(minor_units=9900, currency="brl")
    assert amount.currency == "BRL"
    price = Price(
        id=uuid4(),
        plan_version_id=uuid4(),
        amount=amount,
        billing_period="month",
        hypothesis=False,
    )
    with pytest.raises(ValueError, match="hypothesis"):
        price.publish()


def test_value_validation_and_successful_price_publication() -> None:
    with pytest.raises(ValueError, match="negative"):
        SemanticVersion(-1, 0, 0)
    with pytest.raises(ValueError, match="negative"):
        Money(-1, "BRL")
    with pytest.raises(ValueError, match="ISO"):
        Money(1, "REAL")
    with pytest.raises(ValueError, match="negative"):
        PlanLimit("credits", -1, "credit")

    price = Price(
        id=uuid4(),
        plan_version_id=uuid4(),
        amount=Money(100, "BRL"),
        billing_period="month",
        hypothesis=True,
    )
    assert price.publish().status is CatalogStatus.PUBLISHED
    with pytest.raises(ValueError, match="draft"):
        price.publish().publish()


def test_simple_catalog_entities_and_semantic_version_text() -> None:
    assert str(SemanticVersion(1, 2, 3)) == "1.2.3"
    assert Product(uuid4(), "amplytrix", "Amplytrix").code == "amplytrix"
    assert AddOn(uuid4(), "credits", "Credits").code == "credits"


def test_only_draft_catalog_version_can_be_published() -> None:
    with pytest.raises(ValueError, match="draft"):
        item_version(SemanticVersion(1, 0, 0)).publish().publish()
