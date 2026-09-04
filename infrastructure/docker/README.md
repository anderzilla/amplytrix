# Local containers

The compose file runs a disposable development PostgreSQL bound to localhost. Its credential is intentionally local-only. Do not reuse the password or volume outside local development. App images are defined beside their apps to keep build context explicit.
