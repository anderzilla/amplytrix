# ADR-0060: Evidence-driven scalability evolution

Status: accepted — 2026-08-01

## Context and decision

Use workload formulas and benchmarks for 100/1k/10k/100k subscriber bands; tune/aggregate/cache/partition/separate analytics before services/shards/regions. Invented capacity and speculative distribution were rejected.

## Consequences and validation

Defers complexity but requires instrumentation and load/restore practice. Triggers are measured SLO, saturation, isolation, cost or ownership bottlenecks.
