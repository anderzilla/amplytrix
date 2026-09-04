---
name: python-performance-review
description: Review Amplytrix Python/FastAPI/SQLAlchemy performance, async behavior, Cloud Run concurrency, memory, startup, queries, and provider I/O.
---

# Python performance review

Define measured workload/SLO and profile before optimizing. Inspect event-loop blocking, unbounded concurrency/collections/payloads, N+1/query plans/pools, serialization, CPU/memory/startup, timeouts/retries and cache need. Model Cloud Run concurrency and one Uvicorn worker per initial instance; benchmark before workers/Gunicorn. Report reproducible measurements, cost and regression test, not speculative micro-optimizations.
