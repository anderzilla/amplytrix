---
name: python-security-review
description: Review Amplytrix Python/FastAPI/SQLAlchemy code for ecosystem, web, tenant, AI, dependency, and unsafe-language security risks.
---

# Python security review

Map trust/data/tool boundaries. Check deserialization/pickle, eval/exec/subprocess, traversal/temp/uploads/XML/regex, SSRF redirects/timeouts/destination limits, SQL parameterization/mass assignment, debug/tracebacks/CORS/cookies/JWT, tenant authorization, prompt/tool exfiltration and token/resource abuse. Run Ruff security rules, Bandit, Semgrep, pip-audit and container scan. Report exact evidence/severity/fix/test; never reproduce secrets.
