# ADR-0037: Direct Uvicorn with one worker initially

Status: accepted — 2026-08-01

Run one Uvicorn worker per Cloud Run instance. Cloud Run already scales instances; multiple Gunicorn workers duplicate memory and complicate concurrency on initial 1-vCPU sizing. Measure CPU, memory, latency, external I/O and concurrency before changing. Gunicorn remains an option only with benchmarked need.
