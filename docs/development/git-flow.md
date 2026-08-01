# Git flow

`master`, `homolog`, and `develop` are permanent. Work begins at current `develop` as `task/<scope>/<name>` or `architecture/<name>`. PR flow is exclusively:

```text
task/* or architecture/* -> develop -> homolog -> master
```

Never reverse-promote or skip homologation. A hotfix path requires a new architecture update. Legacy `main`, `Develop`, `Homolog`, and `Master` are frozen during migration; do not target them. Validate locally with `pnpm validate:governance` and in `.github/workflows/branch-policy.yml`.
