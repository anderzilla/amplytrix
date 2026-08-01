# Technology radar

| Ring   | Technology                                                              | Reason                                                  |
| ------ | ----------------------------------------------------------------------- | ------------------------------------------------------- |
| Adopt  | Python 3.13, uv, FastAPI/Uvicorn                                        | typed backend, universal lock and lean Cloud Run HTTP   |
| Adopt  | Ruff, Pyright strict, Pytest, Import Linter                             | unified Python quality and boundary enforcement         |
| Adopt  | Node 24, TypeScript strict, pnpm 11, Turborepo                          | frontend/build coordination only                        |
| Adopt  | Next.js 16, React 19                                                    | web delivery and server composition                     |
| Adopt  | FastAPI-generated REST/OpenAPI                                          | HTTP adapter and authoritative frontend contract        |
| Adopt  | PostgreSQL/Cloud SQL, SQLAlchemy 2/Alembic/asyncpg                      | relational integrity and Python infrastructure adapters |
| Adopt  | Docker, Cloud Run, Terraform, GitHub Actions                            | portable delivery and IaC                               |
| Trial  | OpenTelemetry, Testcontainers, Playwright                               | validate with first feature                             |
| Assess | Identity Platform, Stripe/Mercado Pago, provider AI SDKs                | pending legal/product decision                          |
| Hold   | NestJS backend, premature services, Celery, Redis/vector DB, Kubernetes | superseded or no validated need                         |
