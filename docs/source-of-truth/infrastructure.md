# Infrastructure

Cloud Run, Cloud SQL, Cloud Storage and Terraform are approved targets, but provisioning requires explicit owner, cost/budget and approval. Services are stateless, least-privileged, non-root, observable and rollback-capable. CI produces evidence; production deployment is not automatic. See ADR-0008–0010 and ADR-0017–0018.
