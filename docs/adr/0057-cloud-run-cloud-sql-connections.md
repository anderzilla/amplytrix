# ADR-0057: Cloud Run and Cloud SQL connection budget

Status: accepted — 2026-08-01

## Context and decision

Small per-instance pools, bounded overflow/statement timeout and max instances must satisfy a tested global database connection budget including jobs/admin reserve. Unlimited autoscaling and a large pool per instance were rejected.

## Consequences and validation

Protects SQL but can throttle demand. Load-test pool wait, transactions and failures; change only with database/Cloud Run metrics and restore/SLO evidence.
