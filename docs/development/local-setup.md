# Local setup

Use Python 3.13 with uv 0.11 and Node 24/Corepack/pnpm 11. Run `uv sync --project apps/backend --locked`, `corepack enable`, `pnpm install --frozen-lockfile`, copy `.env.example` to ignored `.env`, and start PostgreSQL with the compose file. Backend: `uv run --project apps/backend uvicorn amplytrix.main:app --app-dir apps/backend/src --host 0.0.0.0 --port 8080`; web: `pnpm --filter @amplytrix/web dev`. Never use production credentials/data locally.
