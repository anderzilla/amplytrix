# Usage and metering domain

UsageEvent is immutable and deduplicated by producer/idempotency key. Reservation prevents overspend; settlement posts consumption or release. CreditLedger is append-only: grant, reserve, consume, release, expire, refund and adjustment entries balance to the materialized quota balance. Corrections are compensating entries, never mutation.

Every AI execution attributes tenant, actor, workspace, agent/skill/model/provider, input/output tokens, duration, estimated cost, credits, result, retries, cache hit and error class. Aggregates are rebuildable from the ledger/events.
