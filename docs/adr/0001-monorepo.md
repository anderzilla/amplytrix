# ADR-0001: pnpm and Turborepo monorepo

Status: accepted — 2026-08-01

## Context and decision

Apps and reusable layers need atomic changes without service sprawl. Use pnpm workspaces with Corepack and Turborepo caching. Alternatives: npm workspaces (less strict/efficient) and Nx (more governance than currently needed).

## Consequences and validation

One lockfile and explicit package boundaries; CI can target affected tasks. Verify deterministic install and architecture tests. Reassess if graph governance exceeds Turborepo.
