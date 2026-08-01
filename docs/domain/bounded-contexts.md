# Commercial bounded contexts

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

Do not create modules from this table alone. A context becomes accepted only after language, ownership, transaction and integration boundaries are demonstrated.

The commercial architecture refines the candidates into Identity & Access, Product Catalog, Entitlements, Billing & Subscriptions, Trials & Promotions, Usage & Metering, AI Execution, Workspaces & Repositories, Technical Memory, Audit & Compliance, Notifications and Experimentation. They remain modules in one deployable modular monolith; each owns its schema and published application contracts.
