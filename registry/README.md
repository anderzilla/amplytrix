# Capability registry

This registry is declarative and deny-default. A project may use only a pinned entry explicitly
listed in its package. Registration documents a capability; it does not grant credentials,
production access, provider terms, budget, or authority beyond the project baseline.

An MCP is admitted only for a named external system with a versioned contract, authentication,
least-privilege scope, data classes, owner, revocation path, security tests, and human approval where
required. Phase Zero has no admitted MCP because dogfooding needs no concrete external runtime
integration. Native repository access is not represented as an MCP.
