---
name: injection-security-review
description: Test traditional and agentic injection risks across Amplytrix trust boundaries.
---

# Injection security review

Read `docs/source-of-truth/security.md` and relevant threat model. Map sources/sinks/trust boundaries; run safe static/dynamic negative tests for injection, traversal, XSS, SSRF, deserialization, mass assignment, prompt/tool/retrieval poisoning, exfiltration and tenant leakage. Redact evidence; report reproduction/CWE/file/flow/remedy. BLOCKER/CRITICAL/HIGH block. Never test production.
