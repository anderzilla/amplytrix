# Project-governed threat model

Scope: managed-service Phase Zero and its future control/knowledge/execution/evidence planes. Assets:
project authority and baseline, client/source content, provenance, prompts/artifacts, capability
versions, execution credentials, approvals, audit evidence, and source/supply chain. Data is public,
internal, confidential-client, personal, credential, or prohibited. Phase Zero admits only public or
internal-redacted material and no secrets or personal data.

Actors are client decision owners, CodeMatrix operators, independent reviewers, attackers,
compromised providers/tools, and malicious or mistaken source authors. Trust boundaries are
repository/project package, future browsers/API, project/database/object storage, CodeMatrix Agency
integration, provider adapters, CI/GCP, and agent/MCP/sandbox tools.

| STRIDE threat                | Control / verification                                                                                            |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Spoofing/session theft       | managed MFA-capable identity, secure HttpOnly SameSite cookies, re-auth sensitive actions; auth tests             |
| Tampering/replay             | validation, authorization, constraints, signed webhooks, idempotency, immutable audit; contract/adversarial tests |
| Repudiation                  | correlated actor/tenant/action/outcome audit without sensitive payloads; audit review                             |
| Information disclosure       | classification, minimization, encryption, redaction, tenant filters, scoped secrets; DLP/log tests                |
| Denial/abuse/cost exhaustion | rate/usage limits, quotas, max instances, budgets, timeouts; load/abuse tests                                     |
| Elevation/tool abuse         | deny-by-default RBAC/permissions, tool sandbox/allowlist, human approval; authorization matrix                    |
| Baseline/scope tampering     | immutable decision reference, change capsules, reviewer gate; relationship tests                                  |
| Cross-project disclosure     | mandatory project scope, owned schemas/objects, deny-default authorization; adversarial isolation tests           |
| Evidence suppression         | require favorable and contrary evidence, explicit inconclusive state, independent review; project validation      |
| Provenance/retrieval poison  | source allowlist, checksum/version, content-as-data policy, citations, quarantine; retrieval/evaluation tests     |
| Reviewer collusion/spoofing  | distinct envelopes/roles, same task/governance commit, independence attestation, auditable adjudication           |
| Agency boundary bypass       | versioned APIs/events only, separate credentials/data, idempotency and correlation; contract/security tests       |
| Unauthorized MCP admission   | empty deny-default registry, named system/contract/auth/scope/owner/revocation requirements; registry tests       |

LLM-specific: prompt injection and indirect content cannot change system policy; retrieved content is
data, not instruction; tool arguments are schema-validated and project/contract-bound; secrets are
unavailable to prompts; output is filtered; model/prompt/tool/approval events are audited. Agents
cannot broaden authority, perform financial decisions, or turn missing evidence into approval.

Preventive controls include classification/minimization, allowlisted sources, checksums, capability
pinning, sandboxing, project-scoped tokens, and human gates. Detective controls include correlation,
append-only logical audit, contrary-evidence checks, usage/cost ceilings, and independent review.
Recovery controls include stopping jobs, revoking a capability/token, restoring a baseline/source
version, quarantining poisoned content, and rollback through a reviewed change capsule.

Residual-risk owners: Product/Architecture for method drift; Security/Privacy for isolation,
retrieval, credentials, and retention; Project Decision Owner for baseline/acceptance; independent
reviewer for review evidence. Each new persistence, provider, MCP, personal-data, or external-action
flow requires an updated model and explicit acceptance of unresolved high risk.
