---
name: known-error-learning
description: Capture a failed check, incident, review finding, or corrected defect as a sanitized Amplytrix known-error record with evidence and validated remediation options.
---

# Known-error learning

Use this skill after a material failure is observed or a prior failure is revisited. Search the
project's `knowledge/known-errors` directory first and update an existing record when the symptom and
cause match; do not create duplicates for different manifestations of the same cause.

Resolve every record and solution evidence reference through
`knowledge/validation-evidence.json`. Add an indexed repository, review, or immutable CI run/job and
commit reference before citing new evidence; never use a free-text claim as an evidence reference.

Record only facts supported by repository, CI, test, or review evidence. Mark the root cause as a
hypothesis until reproduced or otherwise confirmed. Preserve failed and rejected approaches with
their tradeoffs, compare at least two viable solution options, and identify exactly one selected
solution. A solution is validated only after a reproducible check passes in an environment relevant
to the failure; local success does not stand in for a container or CI result.

Sanitize before writing: exclude secrets, personal data, customer identifiers, raw confidential
logs, prompts, tokens, and proprietary payloads. Keep the record project-local and
`internal-redacted`. Cross-project matching may use sanitized patterns only. Client-facing reuse is
blocked until an authorized human approves security, privacy, ownership, contractual scope, and the
absence of identifying data.

Do not remediate automatically unless the active task already authorizes that change. Do not
publish, notify a customer, deploy, spend, accept risk, or infer commercial permission from the
existence of a known solution. If evidence is incomplete, preserve the entry as observed or
diagnosed and state the next validation needed.
