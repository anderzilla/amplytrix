import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { execFileSync } from 'node:child_process';

const root = process.cwd();
const failures = [];
const requiredSource = [
  'README',
  'product',
  'business',
  'architecture',
  'domain',
  'frontend',
  'backend',
  'infrastructure',
  'security',
  'testing',
  'ui-ux',
  'accessibility',
  'internationalization',
  'communication',
  'monetization',
  'ethical-persuasion',
  'commercial-integrity',
  'competitive-conduct',
  'gamification',
  'privacy',
  'branching',
  'glossary',
];
const requiredAgents = [
  'ui-ux-architecture-agent',
  'accessibility-agent',
  'internationalization-agent',
  'visual-quality-agent',
  'usability-flow-agent',
  'user-communication-agent',
  'injection-security-agent',
  'bot-abuse-detection-agent',
  'monetization-strategy-agent',
  'ethical-persuasion-agent',
  'commercial-integrity-agent',
  'gamification-loyalty-agent',
];
const requiredSkills = [
  'ui-ux-review',
  'accessibility-review',
  'internationalization-review',
  'visual-regression-review',
  'usability-flow-review',
  'user-communication-review',
  'injection-security-review',
  'prompt-injection-review',
  'bot-abuse-review',
  'monetization-review',
  'ethical-persuasion-review',
  'commercial-integrity-review',
  'gamification-review',
  'retention-review',
  'develop-to-homolog-gate',
  'branch-policy-validation',
  'source-of-truth-update',
  'task-branch-creation',
  'architecture-update',
];
const required = [
  ...requiredSource.map((name) => `docs/source-of-truth/${name}.md`),
  ...requiredAgents.map((name) => `.codex/agents/${name}.md`),
  ...requiredSkills.map((name) => `.codex/skills/${name}/SKILL.md`),
  '.github/workflows/branch-policy.yml',
  '.github/workflows/develop-to-homolog-gate.yml',
  'docs/development/git-flow.md',
  'docs/development/branch-protection.md',
  'docs/development/pull-request-policy.md',
  'docs/testing/develop-to-homolog-checklist.md',
  'docs/adr/0040-development-governance.md',
  'docs/adr/0041-ethical-commercial-integrity.md',
];
for (const file of required) if (!existsSync(join(root, file))) failures.push(`missing: ${file}`);
for (const file of ['PROJECT_CONSTITUTION.md', 'AGENTS.md', 'docs/source-of-truth/branching.md']) {
  if (!existsSync(join(root, file))) continue;
  const body = readFileSync(join(root, file), 'utf8');
  for (const token of ['develop', 'homolog', 'master'])
    if (!body.includes(token)) failures.push(`${file}: missing ${token}`);
}
for (const [file, tokens] of [
  ['PROJECT_CONSTITUTION.md', ['Dark patterns', 'User trust']],
  ['docs/source-of-truth/commercial-integrity.md', ['BLOCKER', 'artificial dependency']],
  ['.codex/skills/develop-to-homolog-gate/SKILL.md', ['commercial-integrity', 'obscure charge']],
]) {
  if (!existsSync(join(root, file))) continue;
  const body = readFileSync(join(root, file), 'utf8');
  for (const token of tokens) if (!body.includes(token)) failures.push(`${file}: missing ${token}`);
}
const source = process.env.PR_SOURCE;
const target = process.env.PR_TARGET;
const taskPattern =
  /^task\/(frontend|backend|infrastructure|transversal)\/[a-z0-9]+(?:-[a-z0-9]+)*$/;
const architecturePattern = /^architecture\/[a-z0-9]+(?:-[a-z0-9]+)*$/;
const isAllowed = (from, to) =>
  (to === 'develop' && (taskPattern.test(from) || architecturePattern.test(from))) ||
  (from === 'develop' && to === 'homolog') ||
  (from === 'homolog' && to === 'master');
for (const [from, to, expected] of [
  ['task/frontend/example', 'develop', true],
  ['architecture/example', 'develop', true],
  ['develop', 'homolog', true],
  ['homolog', 'master', true],
  ['develop', 'master', false],
  ['task/backend/example', 'homolog', false],
  ['master', 'develop', false],
  ['feature/example', 'develop', false],
]) {
  if (isAllowed(from, to) !== expected)
    failures.push(`internal branch matrix failed: ${from} -> ${to}`);
}
if (source || target) {
  if (!isAllowed(source ?? '', target ?? ''))
    failures.push(`forbidden PR flow: ${source ?? '<missing>'} -> ${target ?? '<missing>'}`);
  if (target === 'develop' && process.env.CI === 'true') {
    try {
      execFileSync('git', ['merge-base', '--is-ancestor', 'origin/develop', 'HEAD'], {
        stdio: 'ignore',
      });
    } catch {
      failures.push(`${source}: branch ancestry does not include origin/develop`);
    }
  }
}
try {
  const tracked = execFileSync('git', ['ls-files'], { encoding: 'utf8' }).split(/\r?\n/);
  const artifact = tracked.find((file) =>
    /(^|\/)(node_modules|\.next|\.turbo|\.terraform|\.venv|dist)(\/|$)|(^|\/)\.coverage$/.test(
      file,
    ),
  );
  if (artifact) failures.push(`tracked local/generated artifact: ${artifact}`);
} catch {
  failures.push('unable to inspect tracked files with git');
}
if (failures.length) {
  console.error(`Governance validation failed (${failures.length})`);
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}
console.log(
  `Governance validation passed: ${required.length} required assets and policy consistency checked.`,
);
