# ADR-0056: Cloud Tasks, Pub/Sub and Cloud Run Jobs roles

Status: accepted — 2026-08-01

## Context and decision

Cloud Tasks handles explicit scheduled/retried destination work; Pub/Sub handles justified fan-out; Cloud Run Jobs handle finite administrative/batch/migration work; outbox publishes reliably. A custom always-on worker is deferred.

## Consequences and validation

Uses different delivery semantics and all consumers remain idempotent. Queue age, duplicate/retry/dead-letter and load tests decide adoption/extraction. Official Google documentation reviewed 2026-08-01 supports these roles.
