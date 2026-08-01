# Environments

`local` uses Docker PostgreSQL and no production credentials. `development`, `staging`, and `production` use separate GCP projects or equivalently hard isolation, service accounts, secrets, databases/buckets, budgets, and telemetry. Production access is least privilege and audited. Terraform state/backends are isolated. Region, project IDs, domains, RTO/RPO and budgets remain open; proposed primary region is São Paulo only after price/service review.
