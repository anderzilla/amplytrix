---
name: cloud-run-readiness
description: Validate an Amplytrix service or job against Google Cloud Run runtime, security, operability, scaling, and cost requirements.
---

# Cloud Run readiness

Verify linux/amd64, statelessness, `0.0.0.0:$PORT` for services or finite exit for jobs, SIGTERM handling, startup/liveness/readiness, timeouts, non-root/minimal image, no embedded secrets, structured telemetry and bounded external connections. Review CPU/memory/concurrency/min/max/cost, service identity, Cloud SQL and rollback. Build/run/smoke locally where possible. Complete with pass/fail evidence and untested cloud assumptions.
