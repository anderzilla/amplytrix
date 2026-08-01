# ADR-0047: Billing provider port and ACL

Status: accepted — 2026-08-01

## Context and decision

Application owns a `BillingProvider` port; Mercado Pago, Stripe and fake adapters translate requests, statuses, errors and webhooks. SDK/provider types cannot enter domain/application.

## Consequences and validation

Mapping effort buys testability and replacement. Contract suites verify timeouts, retry/idempotency, redaction and capability gaps. Supersedes the general choice in ADR-0012 with this concrete boundary.
