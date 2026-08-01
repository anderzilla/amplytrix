# ADR-0055: Provider-calculated, disclosed proration

Status: proposed — 2026-08-01

## Context and decision

Where supported, fetch a provider preview, translate it, disclose amount/effective date and require confirmation before change. Home-grown proration and undisclosed immediate changes were rejected.

## Consequences and validation

Reduces financial divergence but capabilities vary. Enable per adapter only after rounding, tax, retry and race contract tests plus legal approval.
