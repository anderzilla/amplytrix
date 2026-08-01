from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from uuid import UUID


class EntitlementDecision(StrEnum):
    ALLOWED = "allowed"
    DENIED = "denied"
    QUOTA_EXCEEDED = "quota_exceeded"
    PAYMENT_REQUIRED = "payment_required"
    TRIAL_EXPIRED = "trial_expired"
    SEAT_REQUIRED = "seat_required"
    APPROVAL_REQUIRED = "approval_required"
    TEMPORARILY_UNAVAILABLE = "temporarily_unavailable"


@dataclass(frozen=True, slots=True)
class EntitlementDefinition:
    code: str
    approval_required: bool = False


@dataclass(frozen=True, slots=True)
class EntitlementGrant:
    feature_code: str
    limit: int | None
    expires_at: datetime | None = None

    def active_at(self, now: datetime) -> bool:
        return self.expires_at is None or self.expires_at > now


@dataclass(frozen=True, slots=True)
class EntitlementOverride:
    feature_code: str
    allowed: bool
    expires_at: datetime | None = None

    def active_at(self, now: datetime) -> bool:
        return self.expires_at is None or self.expires_at > now


@dataclass(frozen=True, slots=True)
class ResolutionContext:
    organization_id: UUID
    feature_code: str
    subscription_active: bool
    trial_expired: bool
    seat_present: bool
    service_available: bool
    usage: int
    credits: int
    now: datetime


@dataclass(frozen=True, slots=True)
class EntitlementSnapshot:
    decision: EntitlementDecision
    reason: str
    limit: int | None
    remaining: int | None


class EntitlementResolver:
    def resolve(
        self,
        definition: EntitlementDefinition,
        context: ResolutionContext,
        grants: tuple[EntitlementGrant, ...],
        overrides: tuple[EntitlementOverride, ...] = (),
    ) -> EntitlementSnapshot:
        if definition.code != context.feature_code:
            return EntitlementSnapshot(
                EntitlementDecision.DENIED, "definition_mismatch", None, None
            )
        if not context.service_available:
            return EntitlementSnapshot(
                EntitlementDecision.TEMPORARILY_UNAVAILABLE,
                "dependency_unavailable",
                None,
                None,
            )
        active_override = next(
            (
                item
                for item in overrides
                if item.feature_code == context.feature_code and item.active_at(context.now)
            ),
            None,
        )
        if active_override is not None and not active_override.allowed:
            return EntitlementSnapshot(EntitlementDecision.DENIED, "explicit_override", None, None)
        if context.trial_expired:
            return EntitlementSnapshot(
                EntitlementDecision.TRIAL_EXPIRED, "trial_expired", None, None
            )
        if not context.subscription_active:
            return EntitlementSnapshot(
                EntitlementDecision.PAYMENT_REQUIRED, "subscription_inactive", None, None
            )
        if not context.seat_present:
            return EntitlementSnapshot(
                EntitlementDecision.SEAT_REQUIRED, "seat_required", None, None
            )
        if definition.approval_required:
            return EntitlementSnapshot(
                EntitlementDecision.APPROVAL_REQUIRED, "approval_required", None, None
            )
        grant = next(
            (
                item
                for item in grants
                if item.feature_code == context.feature_code and item.active_at(context.now)
            ),
            None,
        )
        if grant is None and (active_override is None or not active_override.allowed):
            return EntitlementSnapshot(EntitlementDecision.DENIED, "no_active_grant", None, None)
        limit = grant.limit if grant is not None else None
        if context.credits <= 0 or (limit is not None and context.usage >= limit):
            return EntitlementSnapshot(
                EntitlementDecision.QUOTA_EXCEEDED, "quota_exceeded", limit, 0
            )
        remaining = None if limit is None else max(limit - context.usage, 0)
        return EntitlementSnapshot(EntitlementDecision.ALLOWED, "active_grant", limit, remaining)
