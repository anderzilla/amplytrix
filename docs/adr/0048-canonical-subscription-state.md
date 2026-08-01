# ADR-0048: Canonical subscription state machine

Status: accepted — 2026-08-01

## Context and decision

Use `pending,incomplete,trialing,active,past_due,grace_period,paused,cancel_scheduled,canceled,expired,unpaid`; adapters map provider facts. Unknown/out-of-order input reconciles instead of guessing.

## Consequences and validation

Stable business language requires maintained mappings. Transition/property/concurrency tests and audit history are mandatory.
