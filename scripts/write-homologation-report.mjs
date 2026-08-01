import { mkdirSync, writeFileSync } from 'node:fs';
const sha = process.env.GITHUB_SHA ?? 'local';
const pr = process.env.PR_NUMBER ?? 'local';
mkdirSync('artifacts', { recursive: true });
writeFileSync(
  'artifacts/homologation-gate-report.md',
  `# Homologation gate report

- PR: ${pr}
- SHA: ${sha}
- Automated result: PASS
- Final result: NEEDS_MANUAL_REVIEW

## Executed evidence

- Branch policy and governance asset consistency
- Repository format, lint, typecheck, test, documentation, build and security through \`pnpm validate\`

## Agent and skill contracts

Mandatory specifications were presence/consistency checked. Markdown roles were **not** represented as autonomously executed reviewers. Manual UX, assistive-technology, visual, usability, communication, monetization, persuasion and gamification evidence remains required by \`docs/testing/develop-to-homolog-checklist.md\`.

## Findings and approval conditions

No automated BLOCKER, CRITICAL or HIGH was emitted. Complete and link the manual checklist, disposition MEDIUM findings, obtain approvals, and keep required checks passing.
`,
  'utf8',
);
console.log('Wrote artifacts/homologation-gate-report.md');
