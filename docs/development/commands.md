# Commands

| Command                                                          | Purpose                                   |
| ---------------------------------------------------------------- | ----------------------------------------- |
| `uv sync --project apps/backend --locked`                        | exact Python environment                  |
| `pnpm lint` / `typecheck` / `test`                               | unified frontend and backend gates        |
| `pnpm build` / `security` / `validate`                           | artifacts, scans and full local gate      |
| `pnpm backend:openapi`                                           | regenerate authoritative OpenAPI snapshot |
| `uv run --project apps/backend ruff format --check apps/backend` | Python format check                       |
| `uv run --project apps/backend ruff check apps/backend`          | Python lint/import rules                  |
| `uv run --project apps/backend pyright`                          | strict Python typing                      |
| `uv run --project apps/backend pytest`                           | Python tests and risk-based coverage      |
| `uv run --project apps/backend lint-imports`                     | Clean Architecture boundaries             |
| `uv run --project apps/backend alembic heads`                    | migration graph check without applying    |
