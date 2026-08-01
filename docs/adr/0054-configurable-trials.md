# ADR-0054: Configurable, consent-based trials

Status: accepted — 2026-08-01

## Context and decision

Trial definitions/eligibility are versioned data; default hypothesis is seven days, one per organization/verified identity, clear notices and no auto-charge absent explicit consent. Trial variants use flags, not branches.

## Consequences and validation

Supports experiments but raises abuse/privacy risk. Test eligibility races, expiry, recovery, consent and guardrail metrics; legal/privacy review precedes card trials.
