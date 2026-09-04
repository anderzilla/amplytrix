# Phase Zero risk-based test plan

| Risk / acceptance                        | Evidence and gate                                                                | Owner                |
| ---------------------------------------- | -------------------------------------------------------------------------------- | -------------------- |
| malformed/drifting contract              | parse every JSON/schema; v1 IDs unique; required artifact checks                 | primary/CI           |
| wrong project/baseline                   | project/scenario/baseline relationship assertions                                | primary/CI           |
| incomplete readiness or hidden free work | origin and readiness/commercial metadata assertions                              | product/CI           |
| missing contrary evidence                | require favorable and contrary records linked to task/project                    | evidence reviewer/CI |
| unauthorized capability/MCP              | registry/reference checks; MCP default deny and zero active entries              | security/CI          |
| poisoned/cross-project source            | allowed source project/content-policy checks; future adversarial retrieval tests | knowledge/security   |
| fake or self review                      | distinct envelopes, same task/governance commit; exact-commit read-only review   | independent reviewer |
| policy/runtime divergence                | explicit contrary evidence; future walking-slice contract/isolation tests        | architecture/QA      |

Run `pnpm phase0:validate` for deterministic checks. After recording the review evidence pack, run
`pnpm phase0:review-gate`. Full `pnpm verify` remains required; Python-dependent checks require the
repository's Python 3.13 runtime and must be reported blocked rather than run under 3.12. Negative
future tests cover duplicate intake, replay with changed payload, missing consent/transfer basis,
cross-project source/capability IDs, absent contrary evidence, self-review, expired approval,
out-of-baseline execution, and failed/partial Agency handoff. No performance/UI/container test is
justified until corresponding runtime exists.
