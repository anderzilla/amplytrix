# ADR-0025: uv over Poetry

Status: accepted — 2026-08-01

Choose uv for its universal lockfile, speed, standalone Windows/Linux binaries, Docker guidance, workspaces and exact syncing. Poetry has a mature workflow and plugin ecosystem but adds slower resolution and another installation/runtime surface. Commit `uv.lock`, use `--locked` in CI/Docker and restrict dependency release dates for reproducibility.
