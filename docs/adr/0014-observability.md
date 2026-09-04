# ADR-0014: OpenTelemetry observability

Status: accepted — 2026-08-01

Emit structured JSON logs, W3C trace context, correlation/tenant-safe identifiers, metrics, and traces through OpenTelemetry; Google Cloud is the initial backend. Redact secrets/personal data at source. Avoid high-cardinality labels and sample traces by environment/risk.
