# Payment provider abstraction

Application port `BillingProvider` exposes customer, checkout, subscription create/change/cancel/resume/fetch, portal, webhook verification and parsing. Mercado Pago is the first Brazilian adapter, Stripe is the international secondary adapter, and a deterministic fake supports tests. No SDK model/status/error crosses the adapter boundary.

Mercado Pago selection is conditional on merchant/legal/tax review and certification. Its official Subscriptions API supports recurring charges and its webhook topics include subscription and payment events; signature capability differs by integration mode, so adapters must verify the configured mode and reconcile by fetching the authoritative resource. Stripe remains inactive until market need and legal/account approval.

Provider account, external IDs and canonical mapping are stored; card data is never stored. Timeouts, bounded safe retries, idempotency keys, redaction, correlation and circuit-breaker assessment apply.

Official sources reviewed 2026-08-01: [Mercado Pago Subscriptions](https://www.mercadopago.com.br/developers/pt/docs/subscriptions/overview), [Mercado Pago Webhooks](https://www.mercadopago.com.br/developers/pt/docs/your-integrations/notifications/webhooks), and [Stripe webhooks](https://docs.stripe.com/webhooks).
