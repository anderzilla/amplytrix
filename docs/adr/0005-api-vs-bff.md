# ADR-0005: Independent API with thin web BFF

Status: accepted — 2026-08-01

Core use cases live behind an independent REST API; Next.js may compose UI-specific data but owns no business rule. A Next-only BFF is simpler initially but harms non-web clients and independent scaling. Cost is a second Cloud Run service and network hop. Validate authorization/correlation propagation and avoid duplicate endpoints.
