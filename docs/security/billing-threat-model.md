# Billing threat model

Assets: payment facts, subscription/entitlement/credit integrity, invoices, identity/tenant mapping, consent, secrets and audit evidence. Boundaries: browser/API, provider/webhook, API/PostgreSQL, async dispatcher/handler and admin tools.

| Threat                                     | Controls and verification                                                                                             | Residual owner   |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Spoofed/tampered/replayed webhook          | bounded body, mode-correct signature verification, unique provider event, authoritative fetch, inbox and replay tests | Security/Billing |
| Cross-tenant invoice or entitlement access | server tenant context, compound constraints, deny-default repositories, matrix/leak tests                             | Security         |
| Duplicate/out-of-order payment             | idempotency, canonical transition guards, reconciliation and concurrency tests                                        | Billing          |
| Trial/coupon/bot abuse                     | verified eligibility, rate/velocity controls, minimal-data signals, appeal and false-positive monitoring              | Product/Security |
| Admin privilege/mass assignment            | explicit command DTOs, scoped RBAC, re-auth, immutable audit and negative tests                                       | Security         |
| Secret/card disclosure                     | provider-hosted tokenization, Secret Manager, redaction/DLP; no card storage                                          | Platform         |
| Cost exhaustion                            | reservations, quotas, max instances, queue throttles, budgets and anomaly alerts                                      | FinOps           |
| Repudiation/consent dispute                | versioned consent, price/terms snapshot, correlated audit and retention policy                                        | Legal/Product    |
| Injection/supply chain                     | schema validation, parameterized SQL, destination allowlist, pinned/scanned dependencies                              | Engineering      |

Chargeback/refund fraud, provider outage, compromised provider account and malicious insider remain material; recovery uses credential revocation, reconciliation, controlled grants and incident response. Legal acceptance is required for retention, tax/fiscal documents, renewal, refunds, chargebacks and credit accounting.
