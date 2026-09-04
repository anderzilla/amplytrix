import { readFile } from 'node:fs/promises';

const document = JSON.parse(await readFile(new URL('../openapi.json', import.meta.url), 'utf8'));
if (document.openapi !== '3.1.0') throw new Error('Expected OpenAPI 3.1.0');
if (!document.paths?.['/health/live'] || !document.paths?.['/health/ready']) {
  throw new Error('Required health contracts are missing');
}
