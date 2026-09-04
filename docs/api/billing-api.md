# Billing API (`/api/v1`)

Customer contracts: `POST /billing/checkout-sessions`, `GET /billing/customer|subscription|invoices|payments`, `POST /billing/subscription/change|cancel|resume`, `POST /billing/customer-portal`. Mutations require tenant membership, recent authentication where sensitive, CSRF protection for cookie sessions and `Idempotency-Key`. Change responses include preview, effective date and financial/entitlement effects before confirmation.

Provider webhooks are `/billing/webhooks/mercado-pago` and `/billing/webhooks/stripe`; they use provider authentication, not user sessions. Admin event list/replay is least-privileged and audited. Registration/onboarding/trial routes follow the planned list and the eventual managed identity contract.
