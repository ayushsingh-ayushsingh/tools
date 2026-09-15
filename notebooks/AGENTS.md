# Agent guide — notebooks workspace

This folder holds the marimo notebook sources for the site. The Astro application embeds each notebook at `/<slug>`; see the root `README.md` for how the pieces fit together.

## Where things belong

- **Create every new notebook in `src/`.** For example, `src/my-notebook.py`. Files created in the `notebooks/` root are invisible to the site tooling and will never be published.
- **Never write export output by hand.** Bundles are generated into `public/notebooks/<slug>/` via `pnpm notebooks:export`. Never export into `src/pages/` — that folder holds Astro routes only.
- **Shared helpers** go in `src/` with an underscore prefix (for example, `src/_utils.py`) so discovery skips them. The launcher package in `src/marimo_nb/` discovers notebooks automatically; do not hard-code notebook names there.

## Skills to consult

- **`marimo-notebook`** — required reading before creating or restructuring any notebook. Follow its format: PEP 723 dependency block, `import marimo as mo` in the first cell, one idea per cell, no redeclared variables across cells, no `global`, final expression renders.
- **`wasm-compatibility`** — every notebook ships as a WebAssembly bundle. Run `marimo check <notebook> --select MW` and resolve all diagnostics. Declare every dependency in the PEP 723 block, avoid packages without a WebAssembly-compatible wheel, and keep clear of environment variables, hard-coded absolute paths, and datasets near the 2 GB browser memory limit.
- **`uk-business-english`** — any user-facing copy (markdown cells, headings, button labels) uses EN-GB spelling and a measured, professional tone.

## Workflow for a new notebook

1. Create it in place: `uv run marimo new src/<slug>.py` from the `notebooks/` folder.
2. Keep the slug short, lowercase, and hyphenated. It becomes the public URL (`/<slug>`), so changing it later breaks links.
3. Develop with `uv run marimo edit src/<slug>.py`.
4. Validate: `uv run marimo check src/<slug>.py` and `uv run marimo check src/<slug>.py --select MW`.
5. Confirm it runs headlessly: `uv run src/<slug>.py`.
6. Export from the repository root: `pnpm notebooks:export`, then verify at `http://localhost:4321/<slug>` with `pnpm dev`.

## Editing existing notebooks

- Edit only the contents of `@app.cell` functions. Let marimo manage cell parameters and return values.
- Preserve each notebook's reactive graph: no cycles, no mutations shared across cells, UI element values (`.value`) read only in downstream cells.
- Keep all UI elements visible in both interactive and script modes. In script mode, fall back to sensible default data rather than hiding widgets.
- After structural edits, re-run both `marimo check` passes before exporting.

## What good looks like

- One notebook per file, self-contained apart from underscore-prefixed helpers.
- Dependencies pinned sensibly in the PEP 723 block; `marimo` always listed.
- WASM check clean, headless run clean, exported bundle verified in the browser.
- No stray files in `notebooks/` root, no build artefacts in `src/pages/`, no hard-coded notebook lists anywhere.
