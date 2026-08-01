# ADR-0042: Versioned commercial catalog

Status: accepted — 2026-08-01

## Context and decision

Hardcoded offerings prevent governed change. Store stable catalog identities with immutable published versions and explicit visibility/lifecycle. Executable definitions remain separate. Alternatives were code constants or mutable rows; both lose history.

## Consequences and validation

More joins/administration, but reproducible purchases and retirement. Validate immutability, effective windows and replacement links. Revisit only if measured read cost cannot be solved by snapshots/cache.
