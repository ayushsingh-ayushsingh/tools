// Exports every marimo notebook in notebooks/src/*.py as a standalone page.
// Each notebook ships as the raw marimo WASM bundle, served directly:
//
//   public/<slug>/index.html        (run mode, read-only)
//   public/<slug>/edit/index.html   (edit mode, editable, shares ../assets/)
//
// Those are the only notebook pages — there is no wrapper chrome and no
// `/notebooks/*` route. The single deliberate difference from pristine marimo
// output is dark-mode support (see THEME_PAYLOAD): marimo bundles are
// light-only, so the export injects a small pre-paint script + style that
// follows the site theme (`localStorage "kumo-mode"`, else the OS
// preference) by inverting the page, exactly like the old embedded frames
// did. Nothing else is added, removed, or rearranged.
//
// Usage:
//   pnpm notebooks:export
//   node scripts/export-notebooks.mjs [--check] [--show-code|--no-show-code]
//
// `--show-code` / `--no-show-code` (default: `--no-show-code`) applies to the
// view-only bundle; the edit bundle always shows code. With --check,
// `marimo check --select MW` (WASM compatibility) runs first and aborts the
// export on failure.
//
// Optimisation: the two flavours differ only in their HTML — the run bundle
// embeds `"mode": "read"` where the edit bundle embeds `"mode": "edit"`,
// while `assets/` is byte-identical. So marimo runs once per notebook (run
// mode) into a temp dir; the edit page is derived by flipping the mount
// config and rebasing `./` references to `../` (from `/<slug>/edit/`, bare
// `./assets/…` would wrongly resolve under `/<slug>/edit/`).

import {
	readdirSync,
	existsSync,
	readFileSync,
	writeFileSync,
	mkdirSync,
	cpSync,
	rmSync,
} from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), '..');
const notebooksDir = path.join(root, 'notebooks');
const srcDir = path.join(notebooksDir, 'src');
const workDir = path.join(root, 'generated', 'notebooks', '.work');
const publicDir = path.join(root, 'public');

const args = process.argv.slice(2);
const runCheck = args.includes('--check');

if (args.some((arg) => arg === '--mode' || arg.startsWith('--mode='))) {
	console.error('The --mode flag was removed: `pnpm notebooks:export` now always exports both the view-only and editable bundles.');
	process.exit(1);
}

// The ONLY delta from pristine marimo output. Runs synchronously before first
// paint (no theme flash): reads the site theme stored by the catalogue toggle,
// falls back to the OS preference, and inverts the light-only bundle when
// dark. Listens for cross-tab toggle changes and OS changes. Hue-rotate
// restores hues after inversion.
const THEME_PAYLOAD = `<script data-notebook-theme="true">(function(){function wantDark(){try{var stored=localStorage.getItem("kumo-mode");if(stored==="dark")return true;if(stored==="light")return false}catch(e){}return window.matchMedia("(prefers-color-scheme: dark)").matches}function apply(){document.documentElement.classList.toggle("nb-dark",wantDark())}apply();window.addEventListener("storage",function(e){if(e&&e.key==="kumo-mode")apply()});try{window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change",apply)}catch(e){}})();</script><style data-notebook-theme="true">html.nb-dark{color-scheme:dark;background:#fff;filter:invert(1) hue-rotate(180deg)}</style>`;

// Anchored to the WASM mount config so notebook code that happens to mention
// `"mode": "read"` is never touched.
const MOUNT_MODE_READ = /("lspWorkspace":\s*null,\s*"mode":\s*")read(")/;
const REL_REF = /(href|src)="\.\//g;

function parseShowCode(argv) {
	if (argv.includes('--show-code')) return true;
	if (argv.includes('--no-show-code')) return false;
	return false;
}

const showCode = parseShowCode(args);

function discoverNotebooks() {
	if (!existsSync(srcDir)) return [];
	return readdirSync(srcDir)
		.filter((file) => file.endsWith('.py') && !path.basename(file).startsWith('_'))
		.sort()
		.map((file) => ({ file, slug: path.basename(file, '.py') }));
}

function run(cmd, cmdArgs, cwd) {
	const result = spawnSync(cmd, cmdArgs, { cwd, stdio: 'inherit' });
	if (result.error) {
		console.error(`Failed to start ${cmd}: ${result.error.message}`);
		process.exit(1);
	}
	return result.status ?? 1;
}

// Inject the theme payload right after <head> so it runs before first paint.
function injectTheme(html, slug) {
	if (!/<head>/.test(html)) {
		throw new Error(`no <head> tag found in the marimo export for ${slug}; refusing to ship an un-themed page`);
	}
	return html.replace(/<head>/, `<head>${THEME_PAYLOAD}`);
}

// Build the editable page from a run-mode export: flip the mount config to
// edit mode and rebase relative URLs one level up so they reuse the parent
// bundle's files instead of duplicating them.
function buildEditPage(viewHtml, slug) {
	if (!MOUNT_MODE_READ.test(viewHtml)) {
		throw new Error(`expected exactly one run-mode mount config in the marimo export for ${slug}`);
	}
	return viewHtml.replace(MOUNT_MODE_READ, '$1edit$2').replace(REL_REF, '$1="../');
}

const notebooks = discoverNotebooks();
if (notebooks.length === 0) {
	console.log(`No notebooks found in ${path.relative(root, srcDir)}. Nothing to export.`);
	process.exit(0);
}

let failed = 0;
for (const { file, slug } of notebooks) {
	const stage = path.join(workDir, slug);
	const outDir = path.join(publicDir, slug);
	console.log(`\n=== ${file} -> public/${slug}/index.html (+ edit/index.html) ===`);

	if (runCheck) {
		const status = run('uv', ['run', 'marimo', 'check', `src/${file}`, '--select', 'MW'], notebooksDir);
		if (status !== 0) {
			console.error(`WASM compatibility check failed for ${file}. Skipping export.`);
			failed += 1;
			continue;
		}
	}

	rmSync(stage, { recursive: true, force: true });
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
			showCode ? '--show-code' : '--no-show-code',
			'-f',
			`src/${file}`,
			'-o',
			path.relative(notebooksDir, stage),
		],
		notebooksDir,
	);
	if (status !== 0) {
		console.error(`Export failed for ${file} (exit code ${status}).`);
		rmSync(stage, { recursive: true, force: true });
		failed += 1;
		continue;
	}

	try {
		const viewHtml = readFileSync(path.join(stage, 'index.html'), 'utf8');

		// public/<slug>/ is fully owned by this script: wipe it so stale
		// hashed assets from older marimo versions never linger.
		rmSync(outDir, { recursive: true, force: true });
		mkdirSync(outDir, { recursive: true });
		for (const entry of readdirSync(stage)) {
			if (entry === 'index.html') continue;
			cpSync(path.join(stage, entry), path.join(outDir, entry), { recursive: true });
		}
		writeFileSync(path.join(outDir, 'index.html'), injectTheme(viewHtml, slug));

		// The edit page shares ../assets/; logo.png / favicon.ico are loaded
		// by bundle JS via document-relative URLs, which resolve against
		// /<slug>/edit/ here — serve both paths.
		const editDir = path.join(outDir, 'edit');
		mkdirSync(editDir, { recursive: true });
		writeFileSync(path.join(editDir, 'index.html'), injectTheme(buildEditPage(viewHtml, slug), slug));
		for (const name of ['logo.png', 'favicon.ico']) {
			const src = path.join(stage, name);
			if (existsSync(src)) cpSync(src, path.join(editDir, name));
		}
		console.log(`Wrote public/${slug}/index.html + public/${slug}/edit/index.html (marimo output + theme payload).`);
	} catch (error) {
		console.error(`Failed to stage ${file}: ${error.message}`);
		failed += 1;
	} finally {
		rmSync(stage, { recursive: true, force: true });
	}
}

if (failed > 0) {
	console.error(`\n${failed} notebook(s) failed.`);
	process.exit(1);
}
console.log(`\nExported ${notebooks.length} notebook(s) as standalone pages (view-only + editable).`);
