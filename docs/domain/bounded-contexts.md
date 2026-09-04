# Project-governed bounded contexts

The managed-service MVP begins with these candidate boundaries. They remain hypotheses until Event
Storming demonstrates language, ownership, invariants, and transaction boundaries.

| Context                 | Responsibility                                                                 | MVP posture                        |
| ----------------------- | ------------------------------------------------------------------------------ | ---------------------------------- |
| Project Governance      | project charter, roles, contract boundary, baseline, decisions, change gates   | declarative Phase Zero; core       |
| Discovery & Scenarios   | intake, problem framing, comparable options, estimates and assumptions         | declarative Phase Zero; core       |
| Knowledge & Provenance  | allowed sources, versions, citations, retrieval policy, retention and deletion | declarative Phase Zero; core       |
| Capability Registry     | admitted agents, skills, MCPs, templates, versions and project eligibility     | declarative Phase Zero; supporting |
| Execution Orchestration | jobs, policy evaluation, tool scope, retries, cost bounds and outcomes         | contract only in Phase Zero; core  |
| Evidence & Supervision  | favorable/contrary evidence, independent review, approvals and stop conditions | declarative Phase Zero; core       |
| Audit & Compliance      | append-only accountability trail, correlation, policy and acceptance evidence  | minimum contract in Phase Zero     |
| Identity & Access       | identity authentication and project-scoped authorization adapter               | decision/provider deferred         |

Commercial subscription contexts below remain relevant to later modalities but do not drive the
managed-service MVP.

## Later commercial contexts

| Context                                 | Value      | Dependency/complexity/risk          | Revenue/MVP                         | Externalization |
| --------------------------------------- | ---------- | ----------------------------------- | ----------------------------------- | --------------- |
| Identity & Access                       | Supporting | medium/high security                | required capability, not custom MVP | high            |
| Organizations & Teams                   | Supporting | IAM; medium/high isolation          | Team later                          | medium          |
| Subscription & Billing                  | Supporting | entitlement; high financial         | paid beta later                     | high provider   |
| Product/Agent/Skill/Workflow Catalogs   | Supporting | product model; medium               | catalog slice likely MVP            | low-medium      |
| AI Execution                            | Core       | policies/providers; very high       | central MVP                         | providers only  |
| Technical Memory                        | Core       | ingestion/access; high              | validate early                      | low             |
| Architecture/Documentation Intelligence | Core       | execution/memory; high              | differentiating slice               | low             |
| Repository Analysis                     | Core       | SCM/tools; high security            | likely MVP input                    | connector only  |
| Usage Metering/Cost Management          | Supporting | execution/billing; high correctness | needed before paid AI               | medium          |
| Audit & Compliance                      | Supporting | all sensitive contexts; high        | minimum audit early                 | low             |
| Notifications                           | Generic    | events/preferences; medium          | later                               | high            |
| Marketplace                             | Supporting | catalog/billing/identity; very high | not MVP                             | partial         |

Do not create persistence modules from either table alone. A context becomes accepted only after
language, ownership, transaction, and integration boundaries are demonstrated.

The commercial architecture refines the candidates into Identity & Access, Product Catalog, Entitlements, Billing & Subscriptions, Trials & Promotions, Usage & Metering, AI Execution, Workspaces & Repositories, Technical Memory, Audit & Compliance, Notifications and Experimentation. They remain modules in one deployable modular monolith; each owns its schema and published application contracts.
