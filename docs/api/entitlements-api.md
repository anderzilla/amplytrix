# Entitlements API (`/api/v1`)

`GET /entitlements` lists the caller tenant's resolved snapshot; `GET /entitlements/{feature}` returns decision, stable reason code, limit/remaining where disclosable, expiry and snapshot version. It never exposes provider status or another tenant. Stale/missing safety-sensitive state denies; availability failures return `temporarily_unavailable` rather than silently granting.

`POST /admin/entitlements/grants` requires scoped role, reason, expiry, idempotency and immutable audit. Overrides cannot defeat legal/security prohibitions.
