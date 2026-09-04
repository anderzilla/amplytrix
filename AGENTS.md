# Operating instructions for Amplytrix agents

## Read first

1. `PROJECT_CONSTITUTION.md`
2. `README.md` and `docs/architecture/system-overview.md`
3. the minimum relevant files in `docs/source-of-truth/`, then relevant ADRs, module README, threat model, and skill
4. `docs/decisions/open-questions.md` and Git status

## Orient before work

Run `git status --short --branch`, `rg --files -uu -g '!.git'`, inspect affected `pyproject.toml`, `uv.lock`, Node manifests, docs and tests, and confirm Python/uv/Node/pnpm versions. Preserve unrelated changes. Do not access files outside the repository, secrets, or production data.

## Official commands

Root: `pnpm install --frozen-lockfile`, `uv sync --project apps/backend --locked`, `pnpm dev`, `pnpm lint`, `pnpm typecheck`, `pnpm test`, `pnpm build`, `pnpm security`, and `pnpm validate`. Backend direct: `uv run --project apps/backend ruff format --check apps/backend`, `ruff check`, `pyright`, `pytest`, `lint-imports`, `alembic heads`, and `pip-audit --skip-editable`. Local PostgreSQL: `docker compose -f infrastructure/docker/compose.yaml up -d postgres`.

## Delivery conventions

Requests beginning exactly with `NOVA TAREFA` require the question "Esta tarefa pertence a qual escopo: frontend, backend, infraestrutura ou transversal?" before planning or edits. After the answer, create `task/<scope>/<short-kebab-name>` from an up-to-date clean `develop`. Requests beginning exactly with `ATUALIZAÇÃO DE ARQUITETURA` require affected-scope confirmation, options/cost/risk analysis, human decision, and `architecture/<short-kebab-name>` from `develop` before changing normative sources.

The only promotion flow is `task/*|architecture/* -> develop -> homolog -> master`, by pull request. Commits follow Conventional Commits and contain one coherent change. Never push, merge, release, deploy, provision, rewrite history, or bypass a gate unless explicitly authorized.

Conserve context: identify scope first; read only relevant source-of-truth sections and module documents; reference paths instead of copying documents; reuse templates/checklists; report incrementally; never regenerate an established pattern.

Commercial features must document value, persuasion technique, monetization, retention, gamification, manipulation/legal/reputation risk, revenue/retention/guardrail metrics, refusal/cancellation/export, required evidence, and stop criteria. Never optimize revenue without complaints, refunds, chargebacks, confusion, accidental conversion, accessibility, consent, privacy, satisfaction, and trust guardrails. Suspected deceptive, abusive, illegal, immoral, autonomy-reducing, or harmful behavior blocks work for human review.

Architecture dependencies are presentation/infrastructure -> application -> domain. Domain imports no FastAPI, Pydantic, SQLAlchemy, Alembic, asyncpg, cloud or provider SDK. Application imports neither presentation nor concrete infrastructure. Bounded contexts cannot import another context's internals or tables. Keep domain, application DTO, HTTP, persistence and provider models separate. Validate all external input; use typed known errors, structured redacted logs, correlation IDs, idempotency and deny-default authorization. Indiscriminate `Any`, silent broad exceptions, mutable global state, sensitive errors, secrets, generated output, `.env*`, MCP local config, state files and production dumps are prohibited.

## Controlled procedures

- Architecture: use the ADR skill, update C4/module boundaries and request architect review.
- Migration: use database-migration skill; additive first, lock/backfill/rollback analysis, disposable integration test; never edit an applied migration.
- Dependency: use dependency-evaluation; record purpose, license, maintenance/security, runtime/bundle/cost and removal path; lockfile must change with manifest.
- Incident: preserve evidence, stop harmful automation, disclose impact/uncertainty, follow `docs/security/incident-response.md`; never conceal or destroy evidence.
- Review: cite exact files/lines, rank correctness/security/data-loss issues first, confirm tests and documentation.

## Completion checklist

Correct branch and confirmed scope; source of truth consulted; user changes preserved; relevant skill followed; commercial objective and guardrail metrics recorded; architecture, accessibility, internationalization, communication, security, abuse, monetization, gamification, observability and privacy considered where applicable; acceptance and negative cases tested; format/lint/typecheck/tests/build and relevant scans executed; docs/contracts/ADRs/diagrams/wiki synchronized; Git diff reviewed; secrets absent; failures and residual risks reported. A task is incomplete if required validation was skipped without a recorded reason.
