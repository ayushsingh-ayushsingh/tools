// Exports every marimo notebook in notebooks/src/*.py to
// public/notebooks/<slug>/ as a self-contained WASM bundle.
//
// Usage:
//   pnpm notebooks:export
//   node scripts/export-notebooks.mjs [--check]
//
// With --check, `marimo check --select MW` (WASM compatibility) runs first
// and aborts the export on failure. Without it, the export runs directly.

import { readdirSync, existsSync } from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), '..');
const notebooksDir = path.join(root, 'notebooks');
const srcDir = path.join(notebooksDir, 'src');
const outRoot = path.join(root, 'public', 'notebooks');

const runCheck = process.argv.includes('--check');

function discoverNotebooks() {
	if (!existsSync(srcDir)) return [];
	return readdirSync(srcDir)
		.filter((file) => file.endsWith('.py') && !path.basename(file).startsWith('_'))
		.sort()
		.map((file) => ({ file, slug: path.basename(file, '.py') }));
}

function run(cmd, args, cwd) {
	const result = spawnSync(cmd, args, { cwd, stdio: 'inherit' });
	if (result.error) {
		console.error(`Failed to start ${cmd}: ${result.error.message}`);
		process.exit(1);
	}
	return result.status ?? 1;
}

const notebooks = discoverNotebooks();
if (notebooks.length === 0) {
	console.log(`No notebooks found in ${path.relative(root, srcDir)}. Nothing to export.`);
	process.exit(0);
}

let failed = 0;
for (const { file, slug } of notebooks) {
	const outDir = path.join(outRoot, slug);
	console.log(`\n=== ${file} -> public/notebooks/${slug}/ ===`);

	if (runCheck) {
		const status = run('uv', ['run', 'marimo', 'check', `src/${file}`, '--select', 'MW'], notebooksDir);
		if (status !== 0) {
			console.error(`WASM compatibility check failed for ${file}. Skipping export.`);
			failed += 1;
			continue;
		}
	}

	const status = run(
		'uv',
		[
			'run',
			'marimo',
			'-y',
			'export',
			'html-wasm',
			'--mode',
			'run',
			'--no-show-code',
			'-f',
			`src/${file}`,
			'-o',
			path.relative(notebooksDir, outDir),
		],
		notebooksDir,
	);
	if (status !== 0) {
		console.error(`Export failed for ${file} (exit code ${status}).`);
		failed += 1;
	}
}

if (failed > 0) {
	console.error(`\n${failed} notebook(s) failed.`);
	process.exit(1);
}
console.log(`\nExported ${notebooks.length} notebook(s) to public/notebooks/.`);
