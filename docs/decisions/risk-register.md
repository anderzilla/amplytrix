# Risk register

| Risk                                                | Likelihood/impact  | Mitigation                                                                                 | Owner/status             |
| --------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------ | ------------------------ |
| Prompt/tool injection causes exfiltration or action | High/critical      | Treat context as untrusted, tool allowlists, scoped tokens, approvals, redaction, audit    | AI/security; open        |
| Cross-tenant access                                 | Medium/critical    | Tenant-aware authorization at every port, DB constraints/RLS evaluation, adversarial tests | Backend/security; open   |
| Vendor lock-in (AI/auth/payments)                   | High/high          | Application ports, normalized usage, provider contract tests, exit plan                    | Architecture; controlled |
| Cloud cost runaway                                  | Medium/high        | scale-to-zero, max instances, budgets/alerts, quotas, per-tenant metering                  | FinOps; before provision |
| Supply-chain compromise                             | Medium/critical    | lockfile, Renovate delay, review, SAST/SCA, SBOM, provenance                               | DevSecOps; CI planned    |
| LGPD non-compliance                                 | Medium/critical    | minimize/classify, lawful basis, retention/deletion, DPO review                            | Privacy; open            |
| Single-region outage/data loss                      | Low/high initially | backups/PITR, restore drills, proportional RTO/RPO                                         | Platform; proposed       |
