# Commercial context map

```mermaid
flowchart LR
  IAM["Identity & Access"] --> WS["Workspaces & Repositories"]
  CAT["Product Catalog"] --> ENT["Entitlements"]
  TRIAL["Trials & Promotions"] --> ENT
  BILL["Billing & Subscriptions"] --> ENT
  USAGE["Usage & Metering"] --> ENT
  ENT --> EXEC["AI Execution"]
  WS --> EXEC
  EXEC --> USAGE
  EXEC --> MEM["Technical Memory"]
  IAM --> AUDIT["Audit & Compliance"]
  BILL --> AUDIT
  EXEC --> AUDIT
  BILL --> NOTIFY["Notifications"]
  TRIAL --> NOTIFY
  EXP["Experimentation"] --> CAT
  EXP --> TRIAL
```

Arrows mean downstream consumption through an owned application contract, not table access. External identity, payment, model and source-control systems use Anti-Corruption Layers. In-process calls/events are default; durable outbox plus task/event delivery is introduced only where delivery semantics require it. Every consumer is idempotent.
