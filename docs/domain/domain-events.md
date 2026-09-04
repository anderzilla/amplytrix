# Domain events

Events name completed domain facts in ubiquitous language, carry stable minimal data, tenant/aggregate identity and occurrence time, and are immutable/versioned. They are not commands or logging. Record inside the aggregate; dispatch after successful commit. For future external delivery, use an outbox and idempotent consumers. Retention, personal data and schema compatibility must be explicit.
