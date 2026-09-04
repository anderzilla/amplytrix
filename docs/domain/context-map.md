# Project-governed context map

```mermaid
flowchart LR
  IAM["Identity & Access"] --> PG["Project Governance"]
  PG --> DS["Discovery & Scenarios"]
  DS --> PG
  PG --> KP["Knowledge & Provenance"]
  PG --> CR["Capability Registry"]
  PG --> EO["Execution Orchestration"]
  KP --> EO
  CR --> EO
  EO --> ES["Evidence & Supervision"]
  ES --> PG
  PG --> AU["Audit & Compliance"]
  KP --> AU
  EO --> AU
  ES --> AU
  CM["CodeMatrix Agency"] -. "versioned API/events" .-> PG
```

Arrows mean downstream consumption through an owned application contract, never table access.
CodeMatrix Agency cannot read Amplytrix storage directly. External identity, model, source-control, and
future payment systems use Anti-Corruption Layers. In-process calls/events are default; durable
outbox plus task/event delivery is introduced only where delivery semantics require it. Every
external consumer is authenticated, authorized, correlated, and idempotent.
