---
name: openapi-client-generation
description: Generate, validate, or update the Amplytrix TypeScript API client from the authoritative FastAPI OpenAPI snapshot.
---

# OpenAPI client generation

Regenerate deterministic FastAPI OpenAPI and fail on unexpected diff/breaking change. Use pinned reviewed generator into a dedicated generated package; never hand-edit output. Preserve operation IDs, error/nullability/pagination semantics and server compatibility. Run format/typecheck/contract tests and document migration/deprecation. Domain and provider models never become client types implicitly.
