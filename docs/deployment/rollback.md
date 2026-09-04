# Rollback

Keep previous Cloud Run revisions and immutable image digests. On regression: stop rollout/traffic, shift traffic to last verified revision, verify health and key smoke flow, and monitor. Database changes use expand/migrate/contract so the previous app remains compatible; restore is last resort and requires incident approval. Record revision, schema compatibility, operator, time, evidence, and follow-up.
