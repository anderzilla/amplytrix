# Execution roadmap 2026-2027

Living reference for program sprints and their exit gates. A gate opens only when the required
evidence is attached to the delivering commit; the sprint's calendar end date alone never opens a
gate. This roadmap complements, and never overrides, `PROJECT_CONSTITUTION.md`'s Definition of
Ready/Done, `docs/decisions/open-questions.md`, and `docs/decisions/risk-register.md`.

## Sprint 2026-09-14 -> 2026-09-18 — Program and gates

### Objective

Advance four standing open questions (`docs/decisions/open-questions.md`) to a decided or evidenced
state, producing one concrete artifact per question: a budget, a data classification, a risk
baseline, and a groomed backlog. The gate depends on evidence linked to the delivering commit, not on
reaching 2026-09-18.

### Deliverables, source open question, and owners

| Deliverable         | Source OQ                                                                         | OQ role owner (`open-questions.md`) | Primary human owner   | Independent reviewer                                               |
| ------------------- | --------------------------------------------------------------------------------- | ----------------------------------- | --------------------- | ------------------------------------------------------------------ |
| Budget              | OQ-14 — readiness effort estimation, Agency cost attribution, discovery packaging | Product/finance/legal               | Anderson (anderzilla) | Evidence Supervisor agent (`.codex/agents/evidence-supervisor.md`) |
| Data classification | OQ-04 — data retention, DPO/contact, incident and vulnerability addresses         | Privacy/security                    | Anderson (anderzilla) | Evidence Supervisor agent                                          |
| Risk baseline       | OQ-16 — closure export, retention, deletion, and anonymization evidence           | Privacy/legal/security              | Anderson (anderzilla) | Evidence Supervisor agent                                          |
| Backlog             | OQ-01 — legal entity, copyright owner, license                                    | Code Matrix/legal                   | Anderson (anderzilla) | Evidence Supervisor agent                                          |

Notes:

- Anderson (`anderzilla`) is the sole accountable human for this program; every deliverable above
  names them as primary owner. That does not waive the constitution's independent-reviewer
  requirement — it is satisfied by an AI reviewer role instead of a second human, per the sponsor's
  direction that project tests and actions run through the AI agents defined for this project
  (`docs/agents/agent-catalog.md`, `.codex/agents/`). The QA and Test Engineer agent executes the
  applicable tests; the Evidence Supervisor agent performs the independent review and cannot approve
  its own or the Project Conductor's work (`.codex/agents/evidence-supervisor.md`,
  `.codex/agents/project-conductor.md`).
- The OQ-to-deliverable mapping favors topical fit over list order: OQ-14's cost/effort estimation is
  the budget input; OQ-04's retention/DPO scope is the data classification input; OQ-16's
  closure/anonymization evidence is the highest-risk item folded into the risk baseline alongside
  `docs/decisions/risk-register.md`; OQ-01's entity/license question gates what can be worked publicly
  and therefore seeds the backlog. If a different mapping was intended, correct this table before the
  gate closes — the mapping itself is not evidence and does not need to be right on the first pass.

### Exit gate

A deliverable above is done only when every item below is true and the evidence is linked to the
delivering commit, per `PROJECT_CONSTITUTION.md`'s Definition of Done and
`docs/development/pull-request-policy.md`:

- Positive and negative acceptance criteria are recorded before implementation starts
  (`docs/templates/task-plan.md`).
- Applicable tests run and their results are recorded, not asserted (QA and Test Engineer agent
  output; manual items follow `docs/testing/develop-to-homolog-checklist.md`).
- Documentation, contracts, risks, and rollback are synchronized with what shipped — no stale
  artifact survives the same commit.
- A primary owner and an independent reviewer are both linked to the same delivering commit
  (Evidence Supervisor agent output for the reviewer half, per above).
- No open BLOCKER/CRITICAL/HIGH finding; any accepted residual risk is recorded in
  `docs/decisions/risk-register.md` with owner and mitigation.
- Demo and retrospective are completed and logged.

If 2026-09-18 arrives with any item unmet: record the gap as a risk in
`docs/decisions/risk-register.md` with owner and new target date, state the blocker once, and do not
start work that depends on the unmet deliverable. The gate stays closed until the evidence exists —
extending the date does not substitute for it.

## Future sprints

To be detailed as the program advances. Each new sprint follows this format: Objective ->
Deliverables/Owners -> Exit gate.
