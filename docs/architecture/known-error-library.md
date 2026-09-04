# Known-error library

The library is operational memory for a single governed project. It captures a failure only after
there is observable evidence and keeps symptom, cause confidence, remediation choices, validation,
and prevention separate. Search existing records before adding one; update a matching cause rather
than cloning it under a new symptom.

Lifecycle: `observed` -> `diagnosed` -> `resolved` -> `superseded`. `Resolved` requires a confirmed
cause, one selected solution, and a passing check in the relevant environment. Alternatives and
failed attempts remain visible with tradeoffs.

Storage is repository-only in Phase Zero. Records are `internal-redacted` and project-local. Never
store credentials, personal data, customer names, raw confidential logs, prompts, or proprietary
payloads. A future customer library may expose only separately approved sanitized patterns through
an isolated read-only projection after security, privacy, ownership, contractual, retention, and
commercial review.

The Known Error Librarian records and compares evidence; it does not silently fix systems or grant
permission. Runtime search, embeddings, persistence, notifications, and customer publication remain
out of scope.
