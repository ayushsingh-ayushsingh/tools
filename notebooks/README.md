# [tools.ayushthinks.com](https://tools.ayushthinks.com)

Interactive notebooks for this site, built with [marimo](https://marimo.io) and exported to WebAssembly so they run entirely in the browser.

All notebook sources live in [`src/`](src/). The Astro site embeds each one at `/<slug>` (for example, `/image-compression`), with a catalogue on the home page.

## Setup

You will need Python 3.12 or later with [`uv`](https://docs.astral.sh/uv/) installed.

Move into this folder and install the workspace:

```bash
cd notebooks
uv sync
```

Then activate the virtual environment.

Linux and macOS:

```bash
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Windows (Git Bash):

```bash
source .venv/Scripts/activate
```

## Editing notebooks

Always create and edit notebooks inside [`src/`](src/). Files created in the `notebooks/` root are not discovered by the site tooling and will not be published.

Open an existing notebook:

```bash
marimo edit src/{my-notebook}.py
```

Start a new one directly in the right place:

```bash
marimo new src/my-notebook.py
```

Or launch through the bundled helper, which finds notebooks automatically:

```bash
uv run marimo-nb --edit
uv run marimo-nb --list
```

Before publishing, run marimo's checks on the file:

```bash
marimo check src/my-notebook.py
```

## Publishing a notebook to the site

`pnpm notebooks:export` (from the repository root) exports every notebook in both flavours at once. The site has no wrapper pages and no `/notebooks/*` route: each export lands directly as the page it becomes:

- `../public/{my-notebook}/index.html` — view-only (`--mode run`)
- `../public/{my-notebook}/edit/index.html` — editable (`--mode edit`), sharing `../assets/`
- `../public/{my-notebook}/assets/` and marimo's static files — runtime files the bundle loads

```bash
cd ..
pnpm notebooks:export
```

To show code by default in the view-only bundle:

```bash
node scripts/export-notebooks.mjs --show-code
```

The export script runs a single run-mode export per notebook, then derives the editable HTML from it: the two flavours differ solely in their HTML (the WASM mount config embeds `"mode": "read"` versus `"mode": "edit"`), while `assets/` is byte-identical — so exporting twice would only waste time and disk. Never export `--mode edit` separately.

The only deliberate difference from pristine marimo output is dark-mode support: marimo bundles are light-only, so the export injects one pre-paint `<script>` + `<style>` (marked `data-notebook-theme`) right after `<head>`. It reads the site theme stored by the catalogue toggle (`localStorage "kumo-mode"`), falls back to the OS preference, follows both live (cross-tab `storage` events, `matchMedia` changes), and inverts the page (`invert(1) hue-rotate(180deg)`) when dark. Everything else is byte-identical marimo output, full-screen.

To include a WebAssembly compatibility check before each export:

```bash
pnpm notebooks:export:check
```

That is equivalent to running, per notebook:

```bash
marimo check src/my-notebook.py --select MW
```

After exporting, start the site and confirm the notebook loads:

```bash
pnpm dev
```

Then visit `http://localhost:4321/my-notebook` for the view-only page and `http://localhost:4321/my-notebook/edit` for the editable page — the only two notebook pages.

A few points worth keeping in mind:

- The view-only page (`/<slug>`) gives visitors the app without the editor chrome; the editable page (`/<slug>/edit`) lets them edit the notebook code in the browser. Changes stay on their device and are never saved.
- `--show-code` / `--no-show-code` only applies to the view-only bundle.
- Staged pages under `public/<slug>/` are generated files and are not committed. `pnpm build` regenerates them automatically.
- Never add per-notebook routes under `src/pages/`. Notebook pages are the raw marimo bundles in `public/<slug>/`; `src/pages/` holds only the catalogue.
- Keep each notebook's dependencies declared in its PEP 723 metadata block (`# /// script` … `# ///`) so packages install correctly in the browser. Notebook files must stay within the 2 GB WebAssembly memory limit and avoid packages without a WebAssembly-compatible wheel.

## Browser notifications

Marimo sends a browser notification (`Execution completed`) every time a run finishes while its tab is in the background — and when notification permission is still undecided, it requests permission on each such run. If you once clicked "Allow", background runs will keep notifying you. There is currently no marimo setting to switch this off (upstream issue [marimo-team/marimo#3659](https://github.com/marimo-team/marimo/issues/3659)).

To stop it immediately in your own browser, block notifications for the marimo origin:

- **Chrome / Edge:** padlock (or tune) icon in the address bar → Site settings → Notifications → Block. Do this for both `localhost:2718` (local `marimo edit` / `marimo run`) and the hosted site.
- **Firefox:** padlock icon → Connection secure → More information → Permissions → uncheck "Use default" under "Send Notifications" and select Block.

The hosted site itself never prompts visitors: the notebook wrapper page declines notification permission requests inside the embedded frame on their behalf. Anyone who previously granted permission can still revoke it per site as described above.

> Note, AI was **heavily** used in the making of this project

Created with ❤️ by Ayush Singh
