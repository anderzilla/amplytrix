# Project intake contract

`schemas/v1/project-intake.schema.json` is the transport-neutral canonical payload for project
readiness. It accepts `agency_briefing`, `client_documents`, `third_party_documents`, and
`direct_discovery`. Receipt is idempotent by `idempotency_key`; origin artifact ID/version and
evidence remain immutable. Receiving a payload never marks it true or executable: Amplytrix adds a
versioned readiness result and decision reference.

A future Agency integration may expose an authenticated API command and/or event using this payload.
The integration must define compatibility, retry/replay behavior, actor/project authorization,
correlation, signature/authentication, consent/transfer basis, retention/deletion, and failure/DLQ
handling before implementation. No shared table, bucket, credential, or implicit user session is
allowed. This contract does not authorize an endpoint or MCP in Phase Zero.
