from datetime import UTC, datetime, timedelta
from uuid import uuid4

from amplytrix.entitlements.domain import (
    EntitlementDecision,
    EntitlementDefinition,
    EntitlementGrant,
    EntitlementOverride,
    EntitlementResolver,
    ResolutionContext,
)

NOW = datetime(2026, 8, 1, tzinfo=UTC)


def context(**changes: object) -> ResolutionContext:
    values: dict[str, object] = {
        "organization_id": uuid4(),
        "feature_code": "ask_project",
        "subscription_active": True,
        "trial_expired": False,
        "seat_present": True,
        "service_available": True,
        "usage": 2,
        "credits": 5,
        "now": NOW,
    }
    values.update(changes)
    return ResolutionContext(**values)  # type: ignore[arg-type]


def test_active_grant_allows_and_reports_remaining_quota() -> None:
    result = EntitlementResolver().resolve(
        EntitlementDefinition("ask_project"), context(), (EntitlementGrant("ask_project", 20),)
    )
    assert result.decision is EntitlementDecision.ALLOWED
    assert result.remaining == 18


def test_expired_grant_denies_by_default() -> None:
    result = EntitlementResolver().resolve(
        EntitlementDefinition("ask_project"),
        context(),
        (EntitlementGrant("ask_project", 20, NOW - timedelta(seconds=1)),),
    )
    assert result.decision is EntitlementDecision.DENIED


def test_deny_override_precedes_grant() -> None:
    result = EntitlementResolver().resolve(
        EntitlementDefinition("ask_project"),
        context(),
        (EntitlementGrant("ask_project", 20),),
        (EntitlementOverride("ask_project", False),),
    )
    assert result.reason == "explicit_override"


def test_quota_and_subscription_failures_are_distinct() -> None:
    resolver = EntitlementResolver()
    grant = (EntitlementGrant("ask_project", 2),)
    assert (
        resolver.resolve(EntitlementDefinition("ask_project"), context(), grant).decision
        is EntitlementDecision.QUOTA_EXCEEDED
    )
    assert (
        resolver.resolve(
            EntitlementDefinition("ask_project"), context(subscription_active=False), grant
        ).decision
        is EntitlementDecision.PAYMENT_REQUIRED
    )
