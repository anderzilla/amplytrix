import { access, readFile, readdir } from 'node:fs/promises';

const required = [
  'README.md',
  'PROJECT_CONSTITUTION.md',
  'AGENTS.md',
  'CONTRIBUTING.md',
  'SECURITY.md',
  'docs/architecture/system-overview.md',
  'docs/security/threat-model.md',
  'docs/testing/test-strategy.md',
  'docs/agents/mcp-catalog.md',
  'docs/decisions/open-questions.md',
  'docs/adr/0062-project-governed-managed-service.md',
  'scripts/validate-phase-zero.mjs',
];
await Promise.all(required.map((file) => access(file)));
const adrs = (await readdir('docs/adr')).filter((file) => /^\d{4}-.+\.md$/.test(file));
if (adrs.length < 39) throw new Error(`Expected at least 39 ADRs; found ${adrs.length}`);
const skillDirs = await readdir('.codex/skills');
if (skillDirs.length < 40)
  throw new Error(`Expected at least 40 skills; found ${skillDirs.length}`);
for (const skill of skillDirs) await access(`.codex/skills/${skill}/SKILL.md`);
const constitution = await readFile('PROJECT_CONSTITUTION.md', 'utf8');
if (!constitution.includes('Definition of Done'))
  throw new Error('Constitution lacks Definition of Done');
process.stdout.write(`foundation-ok: ${adrs.length} ADRs, ${skillDirs.length} skills\n`);
