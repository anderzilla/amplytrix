# Commercial architecture

Free, Pro Trial, Pro, Team and Premium Architecture are the initial plan families; Enterprise is future scope. Catalog items, plans, prices, limits and entitlements are immutable versioned data, never hardcoded authorization. Prices remain hypotheses until finance/legal/product approval.

Product Catalog owns offerings; Entitlements alone resolves access; Billing maps verified provider payment facts to canonical subscription state; Trials owns eligibility; Usage owns immutable metering and credit ledger. Mercado Pago is the proposed first Brazilian adapter and Stripe the proposed international adapter, both behind a provider ACL. No card data is stored.

One PostgreSQL database uses bounded-context schemas in the modular monolith. Cross-context table access is prohibited. Required asynchronous propagation uses outbox/inbox and idempotent handlers. Cloud Tasks is for directed work, Pub/Sub for justified fan-out and Cloud Run Jobs for finite batch/administrative work. Scaling and service extraction require measured evidence. See ADR-0042 through ADR-0061.
