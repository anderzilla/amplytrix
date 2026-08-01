# ADR-0050: Usage metering and credit ledger

Status: accepted — 2026-08-01

## Context and decision

Usage events are immutable/idempotent; credits use an append-only reservation/consumption/compensation ledger with rebuildable balances. Mutable counters alone were rejected.

## Consequences and validation

Higher storage/aggregation cost yields financial traceability. Verify balance invariants, races, corrections, retention and cost attribution.
