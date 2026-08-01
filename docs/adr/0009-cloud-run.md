# ADR-0009: Cloud Run compute target

Status: accepted — 2026-08-01

Use separate Cloud Run services for web/API and Jobs for finite work. It provides scale-to-zero and low platform overhead. GKE is unjustified; functions constrain architecture. Containers follow `$PORT`, statelessness, non-root, probes, SIGTERM, minimal multi-stage build, SBOM/scan.
