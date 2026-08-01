# Assumptions

- Code Matrix owns the initial product and Google Cloud organization; legal confirmation is pending.
- Brazil and `pt-BR` are launch defaults; architecture reserves `en-US` without translating Phase Zero artifacts.
- Low initial traffic favors scale-to-zero Cloud Run and a modular monolith.
- Node 24 is the 2026 LTS line; exact patches are automated and reviewed.
- No existing code, production data, cloud project, or committed secrets existed at bootstrap.
- GitHub Actions will be the initial CI orchestrator; deploy remains manual and disabled.
