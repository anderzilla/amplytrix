import { access, readFile, readdir } from 'node:fs/promises';
import { join, normalize } from 'node:path';

const root = process.cwd();
const failures = [];
const readJson = async (path) => {
  try {
    return JSON.parse(await readFile(join(root, path), 'utf8'));
  } catch (error) {
    failures.push(`${path}: ${error.message}`);
    return null;
  }
};
const exists = async (path) => {
  try {
    await access(join(root, path));
  } catch {
    failures.push(`missing: ${path}`);
  }
};
const expect = (condition, message) => {
  if (!condition) failures.push(message);
};

const schemaDir = 'schemas/v1';
const schemaFiles = (await readdir(join(root, schemaDir))).filter((file) =>
  file.endsWith('.schema.json'),
);
expect(schemaFiles.length >= 12, `expected at least 12 v1 schemas; found ${schemaFiles.length}`);
const schemaIds = new Set();
for (const file of schemaFiles) {
  const path = `${schemaDir}/${file}`;
  const schema = await readJson(path);
  if (!schema) continue;
  expect(schema.$schema === 'https://json-schema.org/draft/2020-12/schema', `${path}: wrong draft`);
  expect(typeof schema.$id === 'string' && schema.$id.includes(':v1:'), `${path}: missing v1 $id`);
  expect(!schemaIds.has(schema.$id), `${path}: duplicate $id ${schema.$id}`);
  schemaIds.add(schema.$id);
}

const projectRoot = 'projects/amplytrix-construction';
const required = [
  'docs/adr/0062-project-governed-managed-service.md',
  'docs/governance/codematrix-collaboration.md',
  'registry/capabilities.json',
  'registry/agents.json',
  'registry/skills.json',
  'registry/mcps.json',
  `${projectRoot}/project.json`,
  `${projectRoot}/intake.json`,
  `${projectRoot}/baseline-decision.json`,
  `${projectRoot}/knowledge/sources.json`,
  `${projectRoot}/governance/task-envelope-primary.json`,
  `${projectRoot}/governance/task-envelope-reviewer.json`,
  `${projectRoot}/governance/primary-evidence-pack.json`,
  `${projectRoot}/governance/change-proposal.json`,
];
await Promise.all(required.map(exists));

const [project, intake, baseline, capabilities, agents, skills, mcps, sources, primary, reviewer] =
  await Promise.all([
    readJson(`${projectRoot}/project.json`),
    readJson(`${projectRoot}/intake.json`),
    readJson(`${projectRoot}/baseline-decision.json`),
    readJson('registry/capabilities.json'),
    readJson('registry/agents.json'),
    readJson('registry/skills.json'),
    readJson('registry/mcps.json'),
    readJson(`${projectRoot}/knowledge/sources.json`),
    readJson(`${projectRoot}/governance/task-envelope-primary.json`),
    readJson(`${projectRoot}/governance/task-envelope-reviewer.json`),
  ]);

if (project && intake && baseline) {
  expect(project.schema_version.startsWith('1.'), 'project: schema version is not v1');
  expect(project.id === baseline.project_id, 'baseline project does not match project');
  expect(
    project.baseline_ref.endsWith('baseline-decision.json'),
    'project baseline ref is invalid',
  );
  expect(project.governance.task_id === primary?.task_id, 'project/primary task IDs differ');
  expect(
    project.governance.governance_commit === primary?.kb_commit,
    'project/primary governance commits differ',
  );
  expect(
    ['agency_briefing', 'client_documents', 'third_party_documents', 'direct_discovery'].includes(
      intake.origin,
    ),
    'intake origin is not admitted',
  );
  expect(intake.readiness_check.status === 'accepted-as-input', 'dogfood intake is not ready');
  expect(
    intake.readiness_check.scope_boundary ===
      'internal-minimum-readiness-check-not-full-agency-diagnostic',
    'readiness/full diagnostic boundary is missing',
  );
  expect(
    intake.readiness_check.effort_estimate?.status &&
      intake.readiness_check.cost_attribution &&
      intake.readiness_check.commercial_disposition,
    'readiness commercial metadata is incomplete',
  );
}

const scenarioFiles = ['conservative', 'realistic', 'aggressive'];
const scenarios = await Promise.all(
  scenarioFiles.map((name) => readJson(`${projectRoot}/scenarios/${name}.json`)),
);
expect(
  scenarios.every((scenario) => scenario?.project_id === project?.id),
  'one or more scenarios belong to another project',
);
expect(
  scenarios.filter((scenario) => scenario?.status === 'selected').length === 1,
  'exactly one scenario must be selected',
);
expect(
  scenarios.some(
    (scenario) => scenario?.id === baseline?.scenario_id && scenario.status === 'selected',
  ),
  'baseline does not point to the selected scenario',
);

const evidenceFiles = (await readdir(join(root, projectRoot, 'evidence'))).filter((file) =>
  file.endsWith('.json'),
);
const evidence = await Promise.all(
  evidenceFiles.map((file) => readJson(`${projectRoot}/evidence/${file}`)),
);
expect(
  evidence.some((item) => item?.polarity === 'favorable'),
  'missing favorable evidence',
);
expect(
  evidence.some((item) => item?.polarity === 'contrary'),
  'missing contrary evidence',
);
expect(
  evidence.every((item) => item?.project_id === project?.id && item?.task_id === primary?.task_id),
  'evidence project/task linkage failed',
);

const capabilityIds = new Set(capabilities?.entries?.map((entry) => entry.id));
const manifestIds = new Set([
  ...(agents?.agents?.map((entry) => entry.id) ?? []),
  ...(skills?.skills?.map((entry) => entry.id) ?? []),
]);
expect(
  [...capabilityIds].every((id) => manifestIds.has(id)),
  'capability index references a missing agent/skill manifest',
);
expect(mcps?.default === 'deny', 'MCP registry is not deny-default');
expect(Array.isArray(mcps?.entries) && mcps.entries.length === 0, 'Phase Zero activates an MCP');

expect(sources?.default === 'blocked', 'knowledge source admission is not default-blocked');
expect(
  sources?.records?.every(
    (source) =>
      source.project_id === project?.id &&
      source.content_policy === 'untrusted-data-not-instruction',
  ),
  'source segregation/content policy failed',
);

if (primary && reviewer) {
  expect(
    primary.envelope_id !== reviewer.envelope_id,
    'primary and reviewer envelope IDs are equal',
  );
  expect(primary.task_id === reviewer.task_id, 'primary/reviewer task IDs differ');
  expect(primary.kb_commit === reviewer.kb_commit, 'primary/reviewer governance commits differ');
  expect(primary.role !== reviewer.role, 'primary/reviewer roles are not distinct');
  expect(
    primary.collaboration.review_required && reviewer.collaboration.review_required,
    'review is not required',
  );
}

for (const [base, file] of [
  [projectRoot, project?.$schema],
  [projectRoot, intake?.$schema],
  [projectRoot, baseline?.$schema],
]) {
  if (!file) continue;
  const resolved = normalize(join(root, base, file));
  try {
    await access(resolved);
  } catch {
    failures.push(`unresolvable project schema ref: ${file}`);
  }
}

if (process.argv.includes('--require-independent-review')) {
  const pack = await readJson(`${projectRoot}/governance/reviewer-evidence-pack.json`);
  expect(pack?.role === 'reviewer', 'review evidence role is not reviewer');
  expect(
    typeof pack?.review_of === 'string' && pack.review_of.length === 40,
    'review target is not a commit',
  );
  expect(pack?.recommendation === 'pass', 'independent review did not pass');
  expect(typeof pack?.independence_attestation === 'string', 'independence attestation is missing');
}

if (failures.length) {
  console.error(`Phase Zero validation failed (${failures.length})`);
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}
console.log(
  `phase-zero-ok: ${schemaFiles.length} schemas, ${capabilityIds.size} capabilities, ${evidence.length} evidence records`,
);
