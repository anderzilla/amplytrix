# Amplytrix

Polyglot foundation repository for Code Matrix's AI-assisted engineering SaaS. Phase Zero contains architecture, pragmatic DDD, governance, agent/skill specifications, and deployable health-only scaffolding; it intentionally contains no commercial features.

## Quick start

Requirements: Python 3.13, uv 0.11, Node.js 24 LTS, Corepack, pnpm 11, and Docker.

```bash
corepack enable
pnpm install --frozen-lockfile
uv sync --project apps/backend --locked
pnpm validate
docker compose -f infrastructure/docker/compose.yaml up -d postgres
pnpm dev
```

Read in order: [project constitution](PROJECT_CONSTITUTION.md), [agent instructions](AGENTS.md), [system overview](docs/architecture/system-overview.md), and [local setup](docs/development/local-setup.md).

Operational decisions are indexed in the [source of truth](docs/source-of-truth/README.md); historical rationale remains in [ADRs](docs/adr/README.md). Development follows `task/*|architecture/* -> develop -> homolog -> master`. The GitHub Wiki is a navigational publication synchronized from reviewed repository documentation, never an independent authority.

## Workspace

- `apps/web`: Next.js UI and UI-specific BFF composition.
- `apps/backend`: Python/FastAPI modular monolith with DDD/Clean Architecture boundaries and health endpoints only.
- `packages/api-contracts`: FastAPI-generated OpenAPI snapshot; future generated TypeScript client remains isolated.
- `infrastructure`: local Docker and non-provisioning Terraform foundation.
- `.codex`: portable project agents, skills, prompts, policies, and MCP example.

Architecture status and open decisions are indexed in [ADRs](docs/adr/README.md). No deployment is automatic.

## License

Copyright Code Matrix. Source-available for evaluation only; see [LICENSE](LICENSE). Licensing is a proposed decision in ADR-0022.
