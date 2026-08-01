---
name: docker-hardening
description: Harden and review Amplytrix Dockerfiles and container images for Cloud Run and CI supply-chain safety.
---

# Docker hardening

Use pinned trusted minimal base, multi-stage build, deterministic install, narrow copy and `.dockerignore`; remove build tools/secrets; run fixed non-root UID; use exec entrypoint; expose only required port; keep writable paths ephemeral. Build image, inspect user/history/size, smoke health/shutdown, generate SBOM and scan vulnerabilities. Critical known findings or secret evidence block completion.
