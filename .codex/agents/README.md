# Agent specifications

Portable Markdown specifications for human or Codex orchestration. Every agent inherits `.codex/policies/safety.md`, works within repository scope, records structural choices in ADRs and hands off using `.codex/prompts/handoff.md`. Tool names are capability descriptions, not implicit permission grants.

All reports classify findings as `BLOCKER`, `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, or `INFO`. The first three block; `MEDIUM` requires correction or approved justification. Reports list scope, inputs, checks, evidence, finding/location/affected flow, recommendation, residual risk and verdict. Agents never silently change architecture or make external/paid/production writes.
