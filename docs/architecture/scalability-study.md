# Scalability study

No capacity number is asserted without a benchmark. For subscriber bands 100, 1,000, 10,000 and 100,000, measure the same model and change architecture only at observed thresholds.

| Band    | Expected focus                                                    | Required evidence before next evolution                                 |
| ------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------- |
| 100     | correctness, restore, cost attribution, small pools/max instances | journey baseline, webhook burst and AI execution benchmark              |
| 1,000   | queue backlog, hot queries, connection budget, noisy tenants      | p95/p99 latency, saturation, retry/duplicate and tenant-isolation load  |
| 10,000  | partition candidates, aggregates/cache, read/analytics separation | EXPLAIN plans, event retention volume, restore time, replica/lag tests  |
| 100,000 | regional/shard/context extraction assessment                      | sustained benchmark proving a specific bottleneck and ownership benefit |

Inputs: active ratio `a`, peak request rate per active user `r`, AI executions `e`, usage events per execution `u`, webhook rate `w`, average stored bytes `b`, retention `d`. Derive `peak_rps=N*a*r`, `usage_events=N*a*e*u`, `retained_bytes=daily_events*b*d`; benchmark distributions and bursts rather than averages.

Connection safety invariant: `max_instances * (pool_size + pool_overflow) + jobs/workers/admin_reserve <= tested_database_connection_budget`. Configure small pools, statement timeout and max instances from a measured budget. API is stateless; start co-located and split `api`, `worker`, `webhooks`, `jobs` only for independent scaling/security/SLO evidence.

Cloud Tasks fits explicit scheduled/retried destination work; Pub/Sub fits fan-out events with idempotent consumers; Cloud Run Jobs fit finite batch/admin/migration work; a long-lived worker is justified only for pull/always-on semantics. Outbox is the reliable publication boundary. Track latency/error/saturation, connection use, queue age, dead letters, payment reconciliation, AI cost, log volume, backups and restore drills. RPO/RTO, minimum instances, HA and budgets remain owner-approved targets.

FinOps model (BRL reporting; provider source currency retained): requests/CPU-memory, instances, SQL compute/storage/backups, object storage/egress, queue operations, logs/traces, AI tokens/tools and support. Low/base/high scenarios are formulas driven by measured workload; budget alerts, quotas, max instances, sampling/retention and per-tenant credit ceilings bound runaway cost. No resource is provisioned by this decision.

Official sources reviewed 2026-08-01: [Cloud Tasks](https://docs.cloud.google.com/tasks/docs/dual-overview), [Pub/Sub subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview), [Cloud Run jobs](https://docs.cloud.google.com/run/docs/create-jobs), [Cloud Run execution models](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run), and [Cloud SQL from Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-run).
