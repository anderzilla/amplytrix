# Transitive security overrides — 2026-09-04

Owner: DevSecOps. Purpose: unblock the existing HIGH security gate without a broad tooling upgrade.

`pnpm audit` reported patched-version advisories in transitive development/build dependencies:
`fast-uri` through Commitlint/Ajv, `js-yaml` through Commitlint/ESLint, and `nanoid` through
PostCSS/Vite. Direct application imports do not use these packages.

Options evaluated:

1. Leave the lockfile unchanged: zero change, but violates the repository's HIGH-finding gate.
2. Upgrade Commitlint, ESLint, Vitest, TypeScript, and related parents: eventually preferable, but
   current updates include multiple majors and materially expand this architecture task.
3. Pin the minimum patched transitive versions with pnpm overrides: selected as the smallest
   reversible correction.

Verified registry metadata on 2026-09-04: `fast-uri@3.1.6` is BSD-3-Clause,
`js-yaml@4.3.1` is MIT, and `nanoid@3.3.18` is MIT and supports Node 24. No runtime bundle, cloud,
network, data, provider, or financial capability is added. Install/provenance risk remains the normal
npm registry/lockfile risk and is checked by frozen install, integrity hashes, build/tests, and audit.

Removal path: DevSecOps removes each override after parent dependency upgrades resolve to an equal or
newer safe compatible version and the full validation/audit passes. Do not retain overrides as an
unowned substitute for routine dependency upgrades.
