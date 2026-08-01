# Cloud Run target

Web and Python API are separate stateless Cloud Run services; migration/batch commands become controlled Cloud Run Jobs. Backend runs direct Uvicorn with one worker initially, listens on `0.0.0.0:$PORT`, runs non-root, handles SIGTERM, exposes liveness/readiness, emits JSON/correlation and contains no secrets. Start request billing, min 0, bounded max, concurrency 40, 1 vCPU/512 MiB and 30s timeout; measure async I/O, CPU and memory before changing workers. Add Tasks/PubSub/Redis/Armor only from validated need.
