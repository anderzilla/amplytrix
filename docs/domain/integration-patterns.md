# Integration patterns

- Published language/OpenAPI for frontend-backend transport.
- Application ports plus adapter-local provider models for AI, identity, payment and SCM.
- Anti-Corruption Layers translate external vocabulary and failures.
- In-process calls/events initially; outbox plus Cloud Tasks/Pub/Sub only after delivery semantics are required.
- No context reads another context's tables or imports its internals.
- Every external HTTP call has timeout, bounded retry, size/destination validation, correlation, redaction and circuit-breaker assessment.
