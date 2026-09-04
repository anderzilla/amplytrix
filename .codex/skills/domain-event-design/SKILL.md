---
name: domain-event-design
description: Design or review Amplytrix domain events, lifecycle, versioning, dispatch, outbox, idempotency, retention, and consumer semantics.
---

# Domain event design

Name a completed domain fact in owning language. Include stable minimal identifiers/time/schema version, not secrets or mutable object graphs. Define producer point, post-commit dispatch, consumers, ordering/idempotency, retry/DLQ, compatibility and retention. Distinguish domain event from command/integration event/log. Do not add a distributed bus without delivery need.
