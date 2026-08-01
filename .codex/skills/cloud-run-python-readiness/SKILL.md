---
name: cloud-run-python-readiness
description: Validate an Amplytrix Python/FastAPI image for Cloud Run runtime, Uvicorn, async, security, telemetry, migrations, scaling, and cost.
---

# Cloud Run Python readiness

Verify Python/uv lock, minimal multi-stage linux/amd64 image, fixed non-root UID, no build tools/secrets, `0.0.0.0:$PORT`, one direct Uvicorn worker initially, SIGTERM/grace timeout, stateless filesystem, liveness/readiness, JSON/correlation and outbound timeouts. Review concurrency/CPU/memory/pools/min/max/cost. Migrations must be separate Jobs. Build, inspect, scan and smoke; disclose cloud-only assumptions.
