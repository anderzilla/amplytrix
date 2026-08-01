---
name: fastapi-endpoint
description: Create or review a thin Amplytrix FastAPI endpoint and OpenAPI contract without leaking business, persistence, or provider logic.
---

# FastAPI endpoint

Define consumer, authorization and OpenAPI behavior. Use dedicated Pydantic request/response schemas; validate transport/context, call one application use case, map typed result/known errors and emit redacted correlation telemetry. Never inject concrete repository into router or return ORM/domain/provider objects. Test status, schema, headers, errors, validation, auth and idempotency; regenerate contract and check compatibility.
