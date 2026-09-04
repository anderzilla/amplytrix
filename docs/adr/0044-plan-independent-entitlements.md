# ADR-0044: Plan-independent entitlements

Status: accepted — 2026-08-01

## Context and decision

One resolver combines versioned grants, add-ons, trials, promotions, overrides, state, quota and seats. Plan-name branching is prohibited. Direct plan checks and provider authorization were rejected.

## Consequences and validation

Adds resolver/snapshot complexity but enables change without deployment. Precedence, expiry, concurrency and deny fallback require exhaustive tests.
