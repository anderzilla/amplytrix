---
name: branch-policy-validation
description: Validate Amplytrix branch names, bases and allowed PR promotion flow.
---

# Branch policy validation

Read `docs/source-of-truth/branching.md`. Accept only `task/<frontend|backend|infrastructure|transversal>/<kebab> -> develop`, `architecture/<kebab> -> develop`, `develop -> homolog`, and `homolog -> master`. Reject other targets/sources, malformed names and unverifiable bases. Run `pnpm validate:governance`; report source, target, rule and verdict. Do not create exceptions.
