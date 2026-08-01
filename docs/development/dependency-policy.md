# Dependency policy

Prefer platform APIs and existing packages. Before adding: state purpose and owner; compare at least one alternative; check maintenance, release cadence, license, advisories, transitive/install-script risk, runtime/bundle/container cost, Cloud Run/Node compatibility, data/network behavior, and removal path. Pin manager/runtime; commit lockfile; use Renovate with seven-day stability delay. Run install scripts only from reviewed allowlist. Remove unused dependencies promptly.
