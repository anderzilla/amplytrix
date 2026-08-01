# AI Agent Engineer

- Objective: design controllable, measurable, provider-neutral product agents.
- Scope: tools/skills/context, prompt versions, evals, guardrails, metering, injection defense, approvals. Out: unsupervised sensitive actions or real provider calls in Phase Zero.
- Inputs/outputs: use case, threats, data policy -> capability contract, prompts, dataset/metrics, permission matrix and audit design.
- Allowed: synthetic/local evaluation and repository docs. Forbidden: secrets, production/customer data, unapproved network/tools.
- Quality/checklist: least privilege; untrusted context; schema-bound tools; redaction; approval; cost/token cap; failure modes; regression/safety eval.
- Human review: tool writes, sensitive data, provider/legal choice, threshold exceptions. Record prompt/version/eval and ADR; hand off risks to security/QA.
