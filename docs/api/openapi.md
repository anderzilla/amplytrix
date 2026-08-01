# OpenAPI lifecycle

FastAPI's generated OpenAPI 3.1 document is authoritative and committed at `packages/api-contracts/openapi.json`. `pnpm backend:openapi` regenerates it; CI fails on an uncommitted difference and validates required operations. Breaking-change detection and a generated TypeScript client are proposed in ADR-0034 before the first business endpoint. Operation IDs are stable, generated output is never hand-edited, and domain/persistence/provider models are explicitly mapped to transport schemas.
