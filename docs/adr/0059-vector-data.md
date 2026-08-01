# ADR-0059: PostgreSQL-first vector data

Status: proposed — 2026-08-01

## Context and decision

Evaluate `pgvector` for the first bounded memory retrieval use case; do not adopt an external vector database without measured need. External-first and unindexed JSON vectors were rejected.

## Consequences and validation

Reduces systems/cost but may contend with OLTP. Benchmark recall, latency, index/build/storage and tenant deletion before acceptance; extract on proven isolation/scale need.
