# Terraform foundation

The initial module expresses Cloud Run safety defaults but is not instantiated and provisions nothing. Terraform was not installed in the bootstrap environment, so CI performs format/validate later. Provider authentication must use workload identity, never service-account key files.
