# Entitlements domain

The resolver combines plan version, add-ons, trial/promotion, overrides, administrative grants, canonical subscription state, grace period, limits, usage/credits, organization/seat, flags and validity. Results are `allowed`, `denied`, `quota_exceeded`, `payment_required`, `trial_expired`, `seat_required`, `approval_required` or `temporarily_unavailable`, with reason code and snapshot version.

EntitlementDefinition, Grant, Override and Snapshot are separate aggregates. Deny is the safe fallback for missing/expired/conflicting inputs. No `if plan == ...` authorization and no direct billing-table read is allowed.
