# ADR-0063: Sanitized project-local known-error learning

Status: accepted — 2026-09-04

## Context and drivers

Phase Zero exposed repeatable failure patterns in schema compilation, dependency auditing, review
gates, secret scanning, and container composition. Keeping those lessons only in chat or CI logs
makes recurrence likely and cannot support a future managed-service knowledge product. The Founder
requested an agent-maintained library of known errors, validated solution options, and reusable
learning.

## Options considered

1. **Keep failures only in task history.** No new structure, but weak retrieval, comparison, and
   prevention.
2. **Build a shared customer knowledge service now.** Powerful, but prematurely introduces
   persistence, tenancy, confidential-data, legal, and product-scope risks.
3. **Add a versioned, project-local, sanitized repository library. Selected.** A dedicated agent and
   skill maintain schema-validated records. Cross-project and client use remains a later gated
   projection.

## Decision

Each material failure is recorded under its project with symptom, impact, evidence, cause
confidence, at least two solution options, one selected solution, validation state, prevention, and
reuse restrictions. A cause is not confirmed by repetition alone, and a solution is not validated
until a relevant reproducible check passes. Evidence resolves through a project index to a versioned
repository artifact, exact review, or immutable CI run/job and commit. Failed approaches remain
visible.

The Known Error Librarian may read project evidence and propose repository updates. It cannot grant
authority, perform unapproved remediation, access production/customer data, or publish externally.
Records are `internal-redacted`, project-local, and contain no credentials, personal data, customer
identity, raw confidential logs, prompts, or proprietary payloads.

Client-facing reuse is a future read-only projection of approved sanitized patterns, never direct
access to another project's library. Security, privacy, ownership, contractual, and human review are
required before export. No runtime, database, vector store, MCP, notification channel, or commercial
offering is created by this decision.

## Consequences and validation

The repository gains durable operational memory and comparable remediation evidence at low cost.
Maintenance and review overhead increase, and repository records cannot prove that a future runtime
retrieves or isolates knowledge correctly. Validate schema compilation, record uniqueness,
project/task linkage, selected-solution integrity, evidence-backed resolved status, capability
registration, and independent review of material changes.

Revisit when multiple projects need cross-project retrieval, a client-facing library is proposed,
retention or licensing terms are known, or measured volume justifies persistence and search.
