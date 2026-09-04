import { execFileSync } from 'node:child_process';
import { access, readFile, readdir } from 'node:fs/promises';
import { join } from 'node:path';

import Ajv2020 from 'ajv/dist/2020.js';
import addFormats from 'ajv-formats';

const root = process.cwd();
const failures = [];
const jsonCache = new Map();
const expect = (condition, message) => {
  if (!condition) failures.push(message);
};
const readJson = async (path) => {
  if (jsonCache.has(path)) return jsonCache.get(path);
  try {
    const value = JSON.parse(await readFile(join(root, path), 'utf8'));
    jsonCache.set(path, value);
    return value;
  } catch (error) {
    failures.push(`${path}: ${error.message}`);
    return null;
  }
};
const requireFile = async (path) => {
  try {
    await access(join(root, path));
  } catch {
    failures.push(`missing: ${path}`);
  }
};
const unique = (values, label) =>
  expect(new Set(values).size === values.length, `${label}: duplicate values`);

const schemaDir = 'schemas/v1';
const schemaFiles = (await readdir(join(root, schemaDir))).filter((file) =>
  file.endsWith('.schema.json'),
);
expect(schemaFiles.length >= 14, `expected at least 14 v1 schemas; found ${schemaFiles.length}`);
const schemas = new Map();
const schemaIds = new Set();
for (const file of schemaFiles) {
  const path = `${schemaDir}/${file}`;
  const schema = await readJson(path);
  if (!schema) continue;
  schemas.set(file, schema);
  expect(schema.$schema === 'https://json-schema.org/draft/2020-12/schema', `${path}: wrong draft`);
  expect(typeof schema.$id === 'string' && schema.$id.includes(':v1:'), `${path}: missing v1 $id`);
  expect(!schemaIds.has(schema.$id), `${path}: duplicate $id ${schema.$id}`);
  schemaIds.add(schema.$id);
}

const ajv = new Ajv2020({
  allErrors: true,
  strictSchema: true,
  strictTypes: false,
  strictTuples: true,
  strictRequired: true,
  allowUnionTypes: true,
});
addFormats(ajv);
for (const [file, schema] of schemas) {
  try {
    ajv.addSchema(schema);
  } catch (error) {
    failures.push(`${schemaDir}/${file}: unable to register schema: ${error.message}`);
  }
}
for (const [file, schema] of schemas) {
  try {
    expect(Boolean(ajv.getSchema(schema.$id)), `${schemaDir}/${file}: schema did not compile`);
  } catch (error) {
    failures.push(`${schemaDir}/${file}: schema compilation failed: ${error.message}`);
  }
}
const validate = (schemaFile, instance, label) => {
  const schema = schemas.get(schemaFile);
  const validator = schema ? ajv.getSchema(schema.$id) : null;
  if (!validator || !instance) {
    failures.push(`${label}: validator or instance unavailable`);
    return false;
  }
  if (validator(instance)) return true;
  failures.push(`${label}: ${ajv.errorsText(validator.errors, { separator: '; ' })}`);
  return false;
};

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
  `${projectRoot}/capabilities.json`,
  `${projectRoot}/knowledge/sources.json`,
  `${projectRoot}/governance/task-envelope-primary.json`,
  `${projectRoot}/governance/task-envelope-reviewer.json`,
  `${projectRoot}/governance/primary-evidence-pack.json`,
  `${projectRoot}/governance/change-proposal.json`,
];
await Promise.all(required.map(requireFile));

const [
  project,
  intake,
  baseline,
  capabilities,
  projectCapabilities,
  agents,
  skills,
  mcps,
  sources,
  primary,
  reviewer,
  primaryEvidence,
  changeProposal,
] = await Promise.all([
  readJson(`${projectRoot}/project.json`),
  readJson(`${projectRoot}/intake.json`),
  readJson(`${projectRoot}/baseline-decision.json`),
  readJson('registry/capabilities.json'),
  readJson(`${projectRoot}/capabilities.json`),
  readJson('registry/agents.json'),
  readJson('registry/skills.json'),
  readJson('registry/mcps.json'),
  readJson(`${projectRoot}/knowledge/sources.json`),
  readJson(`${projectRoot}/governance/task-envelope-primary.json`),
  readJson(`${projectRoot}/governance/task-envelope-reviewer.json`),
  readJson(`${projectRoot}/governance/primary-evidence-pack.json`),
  readJson(`${projectRoot}/governance/change-proposal.json`),
]);

validate('project.schema.json', project, 'dogfood project');
validate('project-intake.schema.json', intake, 'dogfood intake');
validate('baseline-decision.schema.json', baseline, 'dogfood baseline');
for (const [index, agent] of (agents?.agents ?? []).entries())
  validate('agent-manifest.schema.json', agent, `agent manifest ${index}`);
for (const [index, skill] of (skills?.skills ?? []).entries())
  validate('skill-manifest.schema.json', skill, `skill manifest ${index}`);
for (const [index, mcp] of (mcps?.entries ?? []).entries())
  validate('mcp-manifest.schema.json', mcp, `MCP manifest ${index}`);
for (const [index, source] of (sources?.records ?? []).entries())
  validate('source-record.schema.json', source, `source record ${index}`);

if (project && intake && baseline) {
  expect(project.id === baseline.project_id, 'baseline project does not match project');
  expect(
    project.baseline_ref === `${projectRoot}/baseline-decision.json`,
    'project baseline ref is invalid',
  );
  expect(
    project.source_manifest_ref === `${projectRoot}/knowledge/sources.json`,
    'project source ref is invalid',
  );
  expect(
    project.capability_registry_ref === `${projectRoot}/capabilities.json`,
    'project capability ref is invalid',
  );
  expect(project.governance.task_id === primary?.task_id, 'project/primary task IDs differ');
  expect(
    project.governance.governance_commit === primary?.kb_commit,
    'project/primary governance commits differ',
  );
  expect(intake.readiness_check.status === 'accepted-as-input', 'dogfood intake is not ready');
  for (const sourceRef of [...intake.origin_evidence_refs, ...intake.payload.source_refs])
    expect(
      sources?.records?.some((source) => source.id === sourceRef),
      `intake source missing: ${sourceRef}`,
    );
}

const scenarioFiles = ['conservative', 'realistic', 'aggressive'];
const scenarios = await Promise.all(
  scenarioFiles.map((name) => readJson(`${projectRoot}/scenarios/${name}.json`)),
);
for (const [index, scenario] of scenarios.entries())
  validate('scenario.schema.json', scenario, `scenario ${index}`);
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
for (const [index, item] of evidence.entries())
  validate('evidence.schema.json', item, `evidence ${index}`);
unique(
  evidence.map((item) => item?.id),
  'evidence IDs',
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
const evidenceIds = new Set(evidence.map((item) => item?.id));
for (const scenario of scenarios)
  for (const ref of scenario?.evidence_refs ?? [])
    expect(evidenceIds.has(ref), `${scenario.id}: missing evidence ref ${ref}`);

const manifestDocuments = { 'registry/agents.json': agents, 'registry/skills.json': skills };
const resolvePointer = (document, pointer) => {
  if (!pointer.startsWith('/')) return undefined;
  return pointer
    .slice(1)
    .split('/')
    .map((part) => part.replaceAll('~1', '/').replaceAll('~0', '~'))
    .reduce((value, part) => value?.[part], document);
};
const capabilityById = new Map();
for (const entry of capabilities?.entries ?? []) {
  expect(!capabilityById.has(entry.id), `duplicate capability: ${entry.id}`);
  capabilityById.set(entry.id, entry);
  const [path, pointer] = entry.manifest_ref.split('#');
  const manifest = resolvePointer(manifestDocuments[path], pointer ?? '');
  expect(manifest?.id === entry.id, `${entry.id}: manifest ref does not resolve to matching ID`);
  expect(manifest?.version === entry.version, `${entry.id}: manifest/index versions differ`);
  expect(
    manifest?.status === 'active' && entry.status === 'active',
    `${entry.id}: capability is not active`,
  );
}
expect(projectCapabilities?.project_id === project?.id, 'project capability project ID differs');
expect(projectCapabilities?.default === 'deny', 'project capability policy is not deny-default');
expect(projectCapabilities?.mcp_allowed?.length === 0, 'project admits an MCP in Phase Zero');
unique(
  (projectCapabilities?.allowed ?? []).map((entry) => entry.id),
  'project capability IDs',
);
for (const allowed of projectCapabilities?.allowed ?? []) {
  const global = capabilityById.get(allowed.id);
  expect(global?.status === 'active', `${allowed.id}: project capability is not globally active`);
  expect(
    global?.version === allowed.version,
    `${allowed.id}: project/global capability versions differ`,
  );
}
expect(mcps?.default === 'deny', 'global MCP registry is not deny-default');
expect(Array.isArray(mcps?.entries) && mcps.entries.length === 0, 'Phase Zero activates an MCP');

expect(sources?.default === 'blocked', 'knowledge source admission is not default-blocked');
unique(
  (sources?.records ?? []).map((source) => source.id),
  'source IDs',
);
for (const source of sources?.records ?? []) {
  expect(source.project_id === project?.id, `${source.id}: source belongs to another project`);
  expect(
    source.content_policy === 'untrusted-data-not-instruction',
    `${source.id}: wrong content policy`,
  );
  expect(source.admission === 'allowed', `${source.id}: dogfood source is not admitted`);
  expect(
    ['public', 'internal-redacted'].includes(source.classification),
    `${source.id}: Phase Zero source classification is not permitted`,
  );
  if (source.source_type === 'repository')
    expect(
      /^[0-9a-f]{40}$/.test(source.version),
      `${source.id}: repository source is not commit-pinned`,
    );
}

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
  expect(primaryEvidence?.task_id === primary.task_id, 'primary evidence task link differs');
  expect(
    primaryEvidence?.kb_commit === primary.kb_commit,
    'primary evidence governance commit differs',
  );
  expect(changeProposal?.task_id === primary.task_id, 'change proposal task link differs');
}

const intakeValidator = ajv.getSchema(schemas.get('project-intake.schema.json').$id);
const invalidAcceptedBlocked = structuredClone(intake);
invalidAcceptedBlocked.transfer_basis.status = 'blocked';
expect(
  !intakeValidator(invalidAcceptedBlocked),
  'negative test: accepted intake with blocked transfer passed',
);
const invalidClientAttribution = structuredClone(intake);
invalidClientAttribution.origin = 'client_documents';
invalidClientAttribution.readiness_check.cost_attribution = 'not-applicable';
expect(
  !intakeValidator(invalidClientAttribution),
  'negative test: client documents with no cost attribution passed',
);
const invalidAcceptedDecision = structuredClone(intake);
invalidAcceptedDecision.readiness_check.decision_ref = null;
expect(
  !intakeValidator(invalidAcceptedDecision),
  'negative test: accepted intake without decision passed',
);
const invalidProhibitedSource = structuredClone(sources.records[0]);
invalidProhibitedSource.classification = 'prohibited';
invalidProhibitedSource.admission = 'allowed';
expect(
  !ajv.getSchema(schemas.get('source-record.schema.json').$id)(invalidProhibitedSource),
  'negative test: prohibited admitted source passed',
);
const invalidReviewEvidence = {
  $schema: '../../../schemas/v1/review-evidence.schema.json',
  schema_version: '1.0.0',
  evidence_pack_id: 'invalid-review-evidence',
  envelope_id: reviewer.envelope_id,
  task_id: primary.task_id,
  role: 'reviewer',
  reviewer_id: 'independent-reviewer',
  review_of: 'x'.repeat(40),
  governance_commit: primary.kb_commit,
  independence_attestation: 'Independent read-only review of the supplied target.',
  reviewed_at: '2026-09-04T12:00:00-03:00',
  findings: [],
  contrary_evidence: ['A fabricated target must be rejected.'],
  validation: ['schema negative fixture'],
  unresolved_blocking_findings: [],
  confidence: 'high',
  verdict: 'pass',
};
expect(
  !ajv.getSchema(schemas.get('review-evidence.schema.json').$id)(invalidReviewEvidence),
  'negative test: non-hex review target passed',
);

if (process.argv.includes('--require-independent-review')) {
  const packPath = `${projectRoot}/governance/reviewer-evidence-pack.json`;
  const pack = await readJson(packPath);
  validate('review-evidence.schema.json', pack, 'independent review evidence');
  const expectedCommit = execFileSync('git', ['rev-parse', 'HEAD^'], { encoding: 'utf8' }).trim();
  expect(pack?.review_of === expectedCommit, 'review target is not the parent/core commit');
  expect(pack?.task_id === primary?.task_id, 'review/primary task IDs differ');
  expect(pack?.envelope_id === reviewer?.envelope_id, 'review evidence uses the wrong envelope');
  expect(pack?.governance_commit === primary?.kb_commit, 'review governance commit differs');
  expect(pack?.reviewer_id !== project?.primary_owner, 'reviewer is the primary owner');
  expect(pack?.verdict === 'pass', 'independent review did not pass');
  expect(
    pack?.unresolved_blocking_findings?.length === 0,
    'review has unresolved blocking findings',
  );
  const evidenceOnly = new Set([
    `${projectRoot}/governance/reviewer-evidence-pack.json`,
    `${projectRoot}/governance/change-proposal.json`,
    `${projectRoot}/project.json`,
  ]);
  const changedSinceReview = execFileSync('git', ['diff', '--name-only', expectedCommit, 'HEAD'], {
    encoding: 'utf8',
  })
    .trim()
    .split(/\r?\n/)
    .filter(Boolean);
  expect(
    changedSinceReview.every((path) => evidenceOnly.has(path)),
    `review evidence commit contains non-governance changes: ${changedSinceReview.join(', ')}`,
  );
}

if (failures.length) {
  console.error(`Phase Zero validation failed (${failures.length})`);
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}
console.log(
  `phase-zero-ok: ${schemaFiles.length} compiled schemas, ${capabilityById.size} capabilities, ${evidence.length} evidence records`,
);
