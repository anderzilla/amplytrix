# ADR-0028: Pyright strict over mypy

Status: accepted — 2026-08-01

Use Pyright strict for fast, consistent inference and Protocol/unknown-type enforcement across Windows and CI. Mypy is credible but would duplicate policy and needs more plugin decisions. Suppressions must be local, diagnostic-specific and justified.
