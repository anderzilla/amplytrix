# ADR-0018: Secret Manager and workload identity

Status: accepted — 2026-08-01

Local values stay in ignored `.env`; CI/GCP use OIDC/workload identity and Secret Manager with per-service identities. No long-lived service account keys, secret in image, repository, Terraform state, logs, artifacts, or MCP config. Rotation and revocation need named owners before production.
