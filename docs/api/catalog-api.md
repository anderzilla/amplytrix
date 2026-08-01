# Catalog API (`/api/v1`)

Public read contracts: `GET /catalog`, `/catalog/items`, `/catalog/items/{slug}`, `/plans`, `/plans/{slug}`, `/pricing`. Return only published/effective localized versions, integer minor-unit prices plus currency, limits and truthful availability; use cursor pagination and ETag/cache controls. Admin writes create new item/plan/price versions and require strong authorization, idempotency, audit and optimistic concurrency.

Errors use `{code,message,correlation_id,details?}` without internals. Unknown/unpublished resources return indistinguishable 404 responses.
