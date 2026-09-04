# Asynchronous processing

Use synchronous request/response while work fits the HTTP timeout. Candidate selection:

| Need                              | Preferred candidate     | Why / risk                                      |
| --------------------------------- | ----------------------- | ----------------------------------------------- |
| Deferred idempotent HTTP command  | Cloud Tasks             | managed retries/rate control; Google lock-in    |
| Fan-out integration event         | Pub/Sub                 | durable consumers/DLQ; eventual consistency     |
| Finite migration/batch/admin work | Cloud Run Jobs          | same container model; startup and job billing   |
| Long-lived queue worker           | Cloud Run worker pool   | continuous cost/operations; only after evidence |
| Local development                 | in-process fake/adapter | no false production guarantee                   |

Celery, Dramatiq and ARQ are deferred: they add broker, worker lifecycle and observability overhead. Every adopted mechanism requires idempotency key, retry/backoff, timeout, poison-message/DLQ behavior, correlation, audit and cost cap.
