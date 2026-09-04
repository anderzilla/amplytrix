# ADR-0043: Versioned plans and prices

Status: accepted — 2026-08-01

## Context and decision

Plans, limits and prices are immutable versions; money is integer minor units/currency and subscriptions reference a price version. New prices never silently rewrite contracts. Mutable current price and provider-owned catalog were rejected.

## Consequences and validation

Supports audit/markets at migration complexity. Test windows, currency, grandfathering and explicit migration. Legal/tax publication remains gated.
