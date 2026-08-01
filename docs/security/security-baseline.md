# Security baseline

- OWASP ASVS L2 and API Security Top 10 guide web/API controls; OWASP LLM guidance covers agent surfaces.
- TLS at edge, HSTS when domain is controlled, CSP, frame denial, nosniff, strict referrer and minimal permissions headers.
- Deny-default authorization on server; CSRF protection for cookie writes; parameterized SQL; SSRF egress/URL allowlists; body/time limits; schema validation; safe error envelopes.
- CI: Gitleaks, CodeQL, dependency review, Trivy filesystem/image, Checkov Terraform, SBOM. Critical known findings block; lower severity follows risk acceptance with owner/date.
- Workload identity and per-service accounts; Secret Manager; rotation/revocation drills before production.
