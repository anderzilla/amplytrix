# Security policy

Do not open public issues for vulnerabilities. Report privately to the security contact designated by Code Matrix (pending in `docs/decisions/open-questions.md`) with affected version, reproduction, impact, and safe evidence. Do not include personal data or active secrets. The team will acknowledge, triage severity, coordinate remediation and disclosure, and retain incident evidence under the approved policy. Supported versions will be listed after the first release.

Repository policy: no secrets; least privilege; production writes require human approval; critical known vulnerabilities block release; suspected credential exposure triggers immediate revocation and the incident runbook.

High or critical injection, prompt/tool injection, cross-tenant leakage, abusive automation, or missing protection on sensitive flows blocks promotion to `homolog`. Abuse controls minimize personal data, provide legitimate-user recovery, and avoid invasive fingerprinting or opaque sensitive automated decisions without legal review.
