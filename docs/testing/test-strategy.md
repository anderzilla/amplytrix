# Test strategy

Python domain tests are framework/database/network-free. Application tests use typed fakes for commands, queries, authorization and units of work. SQLAlchemy repositories and Alembic migrations use disposable real PostgreSQL, never SQLite substitution. FastAPI tests cover OpenAPI, status/errors/headers/validation/auth/idempotency. AST and Import Linter tests enforce domain/application/context boundaries. Frontend uses Vitest/Testing Library/a11y and Playwright for critical flows. Bandit, Semgrep, pip-audit, Docker/Trivy and Terraform/Checkov complement security. k6 and mutation testing wait for high-risk real behavior.

Promotion from `develop` to `homolog` adds branch/governance checks, representative desktop/mobile and locale journeys, automated plus manual WCAG evidence, visual baselines when UI exists, user communication, injection/prompt/tool, abuse, monetization, ethical persuasion and gamification review. Findings use the shared six-level severity policy. The consolidated report must distinguish automated execution from manual review.

Repository-driven Phase Zero adds deterministic project-contract checks and an exact-commit
independent review described in `docs/testing/phase-zero-test-plan.md`. The review gate is manual
evidence and cannot be replaced by a passing script.
