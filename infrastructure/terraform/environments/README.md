# Environment roots

Create isolated `development`, `staging`, and `production` roots only after project IDs, region, remote state buckets, service accounts, budgets and owners are approved. Never commit tfvars or state. A root composes reviewed modules; `apply` requires a saved plan and human approval. Phase Zero deliberately contains no deployable environment values.
