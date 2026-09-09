# LGPD readiness

Before collecting personal data: map controller/operator roles and processing inventory; document
purpose/lawful basis; minimize fields; publish notice; support access/correction/export/deletion/objection;
execute processor and international-transfer review; perform impact assessment for high-risk AI
processing; test incident notification workflow. Consent is not the default lawful basis. No
production readiness claim exists yet — the items above remain open beyond what is decided below.

## Interim contacts and retention

Resolves OQ-04 (`docs/decisions/open-questions.md`) at an interim level: enough to name a real,
reachable owner and a real default before any user or client data is collected, not a full
production-readiness claim.

- **Privacy contact / DPO (interim):** Anderson (`anderzilla`), `anderson.hg25@gmail.com`. Acting in
  this role personally until Code Matrix's legal entity is confirmed (OQ-01) and a dedicated
  role/address is formalized.
- **Incident and vulnerability contact:** same address, `anderson.hg25@gmail.com`, reused from
  `SECURITY.md` rather than creating a second channel. `SECURITY.md` is updated to point here instead
  of "pending."
- **Default retention:** in the absence of a stricter legal, contractual, or project-specific
  requirement, project/client data classified Confidential or Restricted
  (`docs/security/data-classification.md`) is retained **90 days after project closure or contract
  termination**, then deleted or irreversibly anonymized per the closure procedure below. This is a
  ceiling, not a target — a shorter client-agreed retention always takes precedence.

This is deliberately interim: it satisfies "before collecting user data" with a real, accountable
contact and a real number, while the fuller readiness checklist above (impact assessment, processor
review, international transfer, tested notification workflow) stays open and tracked.

## Closure, export, retention, and deletion

Resolves OQ-16 at the same interim level. Applies when a project or client relationship ends
(`docs/source-of-truth/domain.md` project/context boundary), and complements the general retention
default above with the specific closure sequence:

1. **Export window.** For the retention period above (90 days unless a shorter client-agreed term
   applies), the client may request export of their Confidential-classified deliverables and
   evidence in a portable format. This window starts at closure, not at the export request.
2. **Deletion.** At the end of the export window, raw client content and any derived artifact that is
   not sanitized evidence is deleted, not merely marked inactive. Deletion evidence (what, when, by
   whom) is recorded the same way as other governance evidence
   (`PROJECT_CONSTITUTION.md` Definition of Done).
3. **Sanitized pattern retention is the exception, not the default.** A sanitized, evidence-backed
   pattern may survive deletion only under the existing known-error-learning governance
   (ADR-0063, `.codex/agents/known-error-librarian.md`), with explicit customer-reuse approval
   recorded on the record itself. Absent that approval, deletion in step 2 is unconditional.
4. **Anonymization is not assumed sufficient.** Where anonymization is chosen instead of deletion, it
   must be irreversible and pass legal and technical validation before any reuse or retention decision
   relies on it — per `PROJECT_CONSTITUTION.md`'s prohibition on reuse or retention of derived
   patterns without that validation. No default anonymization technique is pre-approved by this
   document.

Residual risk: this procedure is written and enforceable operationally (delete raw content, gate
sanitized retention on an existing approval mechanism), but it has not yet been exercised end-to-end
against real client data, and the impact assessment for high-risk AI processing above is still open.
That gap is carried in `docs/decisions/risk-register.md` rather than claimed closed here.
