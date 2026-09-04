# Phase Zero execution plan

1. Align source of truth, ADR, context diagrams, threat model, and risks.
2. Establish versioned schemas for intake, project, scenario, baseline, sources, agents, skills, MCP
   admission, jobs, evidence, approvals, and change capsules.
3. Register only necessary agents/skills; keep MCP admission deny-default and empty.
4. Build this dogfood package with provenance, three scenarios, baseline, plan, evidence, and linked
   RULE-034/DEC-035 envelopes.
5. Run deterministic repository gates and full available validation without using Python 3.12 as a
   substitute for the required Python 3.13.
6. Obtain read-only review of the exact proposed commit; resolve findings and record adjudication.
7. Push a private architecture branch and open a PR to `develop`. Do not merge or deploy.

Stop on secret/personal data, external cost/action, inability to establish provenance, unresolved
high-risk finding, missing reviewer, or a requested change outside the baseline.
