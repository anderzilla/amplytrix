# Branch protection

GitHub rulesets for `develop`, `homolog`, and `master` must block deletion and force-push, require pull requests, required status checks, resolved conversations, and non-stale approvals. `master` is default. Administrators do not bypass silently; emergency recovery records actor, reason, evidence and follow-up ADR/incident where appropriate.

Required checks are `Branch policy / validate`, normal Validate jobs, Documentation, CodeQL and, for `develop -> homolog`, `Develop to homolog gate / homologation-gate`. GitHub plan/API limitations must be recorded rather than simulated. Inspect rulesets after any workflow job rename because required checks are string identities.

CodeQL runs and uploads SARIF as a workflow artifact because GitHub Code Scanning is not enabled for this private repository. If the licensed feature becomes available, change `upload` only through reviewed security configuration and add the native result check to required statuses.

Legacy branches are retained read-only until all clones, links and automation use lowercase names; then deletion needs explicit confirmation and a recorded migration check. No deploy is enabled by these rules.
