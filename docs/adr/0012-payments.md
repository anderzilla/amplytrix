# ADR-0012: Provider-neutral payments

Status: proposed — 2026-08-01

Application ports own customers, checkout intents, subscriptions, invoices, and webhook idempotency; adapters map Stripe and a Brazilian provider such as Mercado Pago. Decide provider(s) after legal entity, tax, Pix/boleto/card, recurring billing, chargeback, payout, pricing, and data-processing review. Provider IDs never become domain identities.
