# ADR-0023: Python 3.13 as the backend language

Status: accepted — 2026-08-01

Use Python 3.13 for the primary API, jobs and AI orchestration. It has mature FastAPI/data/AI tooling while remaining broadly supported; 3.14 is newer but carries greater ecosystem compatibility uncertainty. Node/TypeScript remain frontend/build concerns. Consequences: a polyglot monorepo and two lockfiles; unified root commands hide neither toolchain.
