# Execution roadmap 2026-2027

Living reference for program sprints and their exit gates. A gate opens only when the required
evidence is attached to the delivering commit; the sprint's calendar end date alone never opens a
gate. This roadmap complements, and never overrides, `PROJECT_CONSTITUTION.md`'s Definition of
Ready/Done, `docs/decisions/open-questions.md`, and `docs/decisions/risk-register.md`.

## Program timeline

All 30 sprints are tracked as GitHub issues (`type:sprint` label, one per row below) on the
[Amplytrix · Roadmap 2026–2027](https://github.com/users/anderzilla/projects/1) board. Each issue's
own checklist (Entregas / Qualidade e documentação) is the source of truth for that sprint's
day-to-day progress — this table is the source of truth for the sequence, dates, and phase, so the
two are not duplicated field-by-field. Sprints run back-to-back in two-week windows unless noted;
`S00` and `S07` are short (5-day) checkpoints, and `S07 -> S08` carries a deliberate ~2.5-week gap
(year-end break).

| Sprint | Phase | Window                   | Objective               | Issue                                                                   |
| ------ | ----- | ------------------------ | ----------------------- | ----------------------------------------------------------------------- |
| S00    | F0    | 2026-09-14 -> 2026-09-18 | Programa e gates        | [#9](https://github.com/anderzilla/amplytrix/issues/9) — detailed below |
| S01    | F1    | 2026-09-21 -> 2026-10-02 | Comprador e problema    | [#10](https://github.com/anderzilla/amplytrix/issues/10)                |
| S02    | F1    | 2026-10-05 -> 2026-10-16 | Oferta e amostra        | [#11](https://github.com/anderzilla/amplytrix/issues/11)                |
| S03    | F2    | 2026-10-19 -> 2026-10-30 | Método operacional      | [#12](https://github.com/anderzilla/amplytrix/issues/12)                |
| S04    | F2    | 2026-11-02 -> 2026-11-13 | UX CodeMatrix           | [#13](https://github.com/anderzilla/amplytrix/issues/13)                |
| S05    | F3    | 2026-11-16 -> 2026-11-27 | Governance slice        | [#14](https://github.com/anderzilla/amplytrix/issues/14)                |
| S06    | F3    | 2026-11-30 -> 2026-12-11 | Cenários e baseline     | [#15](https://github.com/anderzilla/amplytrix/issues/15)                |
| S07    | F3    | 2026-12-14 -> 2026-12-18 | Evidência e exportação  | [#16](https://github.com/anderzilla/amplytrix/issues/16)                |
| S08    | F4    | 2027-01-04 -> 2027-01-15 | Persistência            | [#17](https://github.com/anderzilla/amplytrix/issues/17)                |
| S09    | F4    | 2027-01-18 -> 2027-01-29 | API                     | [#18](https://github.com/anderzilla/amplytrix/issues/18)                |
| S10    | F4    | 2027-02-01 -> 2027-02-12 | Console interno         | [#19](https://github.com/anderzilla/amplytrix/issues/19)                |
| S11    | F4    | 2027-02-15 -> 2027-02-26 | Recuperação operacional | [#20](https://github.com/anderzilla/amplytrix/issues/20)                |
| S12    | F5    | 2027-03-01 -> 2027-03-12 | Abstração de provedores | [#21](https://github.com/anderzilla/amplytrix/issues/21)                |
| S13    | F5    | 2027-03-15 -> 2027-03-26 | Autoridade e custo      | [#22](https://github.com/anderzilla/amplytrix/issues/22)                |
| S14    | F5    | 2027-03-29 -> 2027-04-09 | Red-team técnico        | [#23](https://github.com/anderzilla/amplytrix/issues/23)                |
| S15    | F6    | 2027-04-12 -> 2027-04-23 | Piloto 1                | [#24](https://github.com/anderzilla/amplytrix/issues/24)                |
| S16    | F6    | 2027-04-26 -> 2027-05-07 | Piloto 2                | [#25](https://github.com/anderzilla/amplytrix/issues/25)                |
| S17    | F6    | 2027-05-10 -> 2027-05-21 | Piloto 3 e decisão      | [#26](https://github.com/anderzilla/amplytrix/issues/26)                |
| S18    | F7    | 2027-05-24 -> 2027-06-04 | Pacote avulso 1         | [#27](https://github.com/anderzilla/amplytrix/issues/27)                |
| S19    | F7    | 2027-06-07 -> 2027-06-18 | Pacote avulso 2         | [#28](https://github.com/anderzilla/amplytrix/issues/28)                |
| S20    | F7    | 2027-06-21 -> 2027-07-02 | Repetibilidade          | [#29](https://github.com/anderzilla/amplytrix/issues/29)                |
| S21    | F8    | 2027-07-05 -> 2027-07-16 | Portal somente leitura  | [#30](https://github.com/anderzilla/amplytrix/issues/30)                |
| S22    | F8    | 2027-07-19 -> 2027-07-30 | Aprovações no portal    | [#31](https://github.com/anderzilla/amplytrix/issues/31)                |
| S23    | F8    | 2027-08-02 -> 2027-08-13 | Identidade e isolamento | [#32](https://github.com/anderzilla/amplytrix/issues/32)                |
| S24    | F8    | 2027-08-16 -> 2027-08-27 | Portal beta             | [#33](https://github.com/anderzilla/amplytrix/issues/33)                |
| S25    | F9    | 2027-08-30 -> 2027-09-10 | Catálogo e entitlements | [#34](https://github.com/anderzilla/amplytrix/issues/34)                |
| S26    | F9    | 2027-09-13 -> 2027-09-24 | Billing                 | [#35](https://github.com/anderzilla/amplytrix/issues/35)                |
| S27    | F9    | 2027-09-27 -> 2027-10-08 | Ciclo comercial         | [#36](https://github.com/anderzilla/amplytrix/issues/36)                |
| S28    | F10   | 2027-10-11 -> 2027-10-22 | Staging e operação      | [#37](https://github.com/anderzilla/amplytrix/issues/37)                |
| S29    | F10   | 2027-10-25 -> 2027-11-05 | Lançamento controlado   | [#38](https://github.com/anderzilla/amplytrix/issues/38)                |

Only S00 has a detailed gate section below today. Each sprint gets one — Objective, deliverables and
owners, exit gate, evidence log — added to this file as its window approaches, following the S00
format; "approaches" is a planning convenience, not a gate condition — the gate itself still depends
only on evidence, per the rule above.

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

### Evidence log

Ahead of the sprint window, so the gate above can actually be checked at 2026-09-14 rather than
started from zero:

- **Data classification (OQ-04)** — interim decision recorded 2026-09-09: `docs/decisions/open-questions.md`
  (status column), `docs/security/lgpd-readiness.md#interim-contacts-and-retention`,
  `docs/security/data-classification.md` (retention note), `SECURITY.md` (real interim contact
  replacing the "pending" placeholder). Positive criterion: a real, reachable contact and a real
  retention default exist before any user/client data is collected. Negative criterion: no
  production-readiness or legal-compliance claim beyond that interim scope. Independent-review pass:
  contact and retention wording checked against `docs/decisions/open-questions.md`'s own trigger
  ("before collecting user data") and against `PROJECT_CONSTITUTION.md`'s prohibition on
  overclaiming; no BLOCKER/CRITICAL/HIGH raised, residual gap (full LGPD readiness checklist) carried
  in `docs/decisions/risk-register.md`, not hidden.
- **Risk baseline (OQ-16)** — interim decision recorded 2026-09-09:
  `docs/security/lgpd-readiness.md#closure-export-retention-and-deletion`,
  `docs/decisions/risk-register.md` ("Client data is reused without valid legal basis" row).
  Positive criterion: a written closure sequence (export window, deletion, sanitized-retention
  exception, anonymization non-assumption) exists before client data is collected. Negative
  criterion: anonymization is never treated as sufficient by default, and sanitized retention stays
  gated on the existing ADR-0063 approval mechanism rather than a new, weaker one. Independent-review
  pass: procedure checked against ADR-0063 and `PROJECT_CONSTITUTION.md`'s reuse prohibition; no
  BLOCKER/CRITICAL/HIGH raised, residual gap (end-to-end exercise against real data, impact
  assessment) carried in the risk register, not claimed closed.
- **Budget (OQ-14)** and **Backlog (OQ-01)** — not started; both need a decision only the sponsor can
  make (real cost/effort figures; legal entity and license), not something to draft speculatively.

## Board

The [Amplytrix · Roadmap 2026–2027](https://github.com/users/anderzilla/projects/1) GitHub Project is
the sprint/kanban view of this document: columns Backlog / Ready / In progress / In review / Done
track each sprint issue's status, and an Iteration field (once populated per the Program timeline
table above) drives the Current/Next iteration and Roadmap views. This markdown file stays the
narrative and gate record; the board stays the at-a-glance status. When they disagree, this file and
the linked issue's own checklist are authoritative — the board's column/iteration placement is a
projection of them, not an independent source of truth, and should be corrected to match rather than
the other way around.
