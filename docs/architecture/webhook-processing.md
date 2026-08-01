# Webhook processing

```mermaid
sequenceDiagram
  participant P as Provider
  participant W as Webhook adapter
  participant DB as Inbox
  participant Q as Task dispatcher
  participant B as Billing handler
  P->>W: signed bounded request
  W->>W: rate limit + verify + normalize identity
  W->>DB: insert unique provider/event record
  W-->>P: 2xx quickly
  DB->>Q: outbox dispatch
  Q->>B: idempotent task
  B->>P: fetch authoritative resource if needed
  B->>DB: transaction: payment/subscription/invoice + audit + outbox
```

Reject invalid signature/size; do not log payload secrets. Duplicate events return success after lookup. Handlers tolerate out-of-order delivery through provider occurrence/version data and reconciliation. Transient failures retry with backoff; permanent failures enter a dead-letter record with reason, owner and controlled replay. Replay re-verifies authorization, preserves the original event, creates a new attempt and cannot bypass idempotency.
