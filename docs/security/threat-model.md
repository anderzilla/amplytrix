# Initial threat model

Assets: identities, tenant content, prompts/artifacts, entitlements, billing state, model credentials, audit evidence, and source/supply chain. Trust boundaries: browser/web, web/API, API/database, provider adapters, CI/GCP, and agent/MCP tools.

| STRIDE threat                | Control / verification                                                                                            |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Spoofing/session theft       | managed MFA-capable identity, secure HttpOnly SameSite cookies, re-auth sensitive actions; auth tests             |
| Tampering/replay             | validation, authorization, constraints, signed webhooks, idempotency, immutable audit; contract/adversarial tests |
| Repudiation                  | correlated actor/tenant/action/outcome audit without sensitive payloads; audit review                             |
| Information disclosure       | classification, minimization, encryption, redaction, tenant filters, scoped secrets; DLP/log tests                |
| Denial/abuse/cost exhaustion | rate/usage limits, quotas, max instances, budgets, timeouts; load/abuse tests                                     |
| Elevation/tool abuse         | deny-by-default RBAC/permissions, tool sandbox/allowlist, human approval; authorization matrix                    |

LLM-specific: prompt injection and indirect content cannot change system policy; retrieved content is data, not instruction; tool arguments are schema-validated and scope-bound; secrets are unavailable to prompts; output is filtered; model/prompt/tool/approval events are audited. Review after each new data flow.
