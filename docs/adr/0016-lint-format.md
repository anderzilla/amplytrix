# ADR-0016: ESLint and Prettier

Status: accepted — 2026-08-01

Use ESLint 9 type-aware rules for correctness and Prettier for formatting. Biome is faster but the selected framework/plugin ecosystem and type-aware rule coverage favor ESLint. Imports/boundaries are checked by architecture tests as the graph grows.
