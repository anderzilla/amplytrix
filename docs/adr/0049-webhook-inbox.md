# ADR-0049: Webhook inbox and asynchronous processing

Status: accepted — 2026-08-01

## Context and decision

After bounded verification, persist each unique provider event and respond quickly; process idempotently, fetch authoritative resources, transact changes/outbox/audit, retry and dead-letter. Heavy synchronous handling and trust in payload alone were rejected.

## Consequences and validation

Eventual consistency and operations increase; resilience/replay improve. Test duplicate, reorder, forgery, outage, poison event and controlled replay.
