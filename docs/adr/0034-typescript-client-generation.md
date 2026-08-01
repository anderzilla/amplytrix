# ADR-0034: Isolated generated TypeScript client

Status: proposed — 2026-08-01

Generate a TypeScript client from the reviewed OpenAPI snapshot into a dedicated generated package. Evaluate openapi-typescript plus a thin fetch client against Orval after real endpoint needs. Generated files are immutable by hand; generator version, snapshot and breaking-change gate are pinned.
