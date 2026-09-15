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
marimo edit src/image-compression.py
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

Export the notebook as a self-contained WebAssembly bundle. From this folder:

```bash
marimo export html-wasm --mode run --no-show-code -f src/my-notebook.py -o ../public/notebooks/my-notebook/
```

To export every notebook at once, use the script at the repository root instead:

```bash
cd ..
pnpm notebooks:export
```

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

Then visit `http://localhost:4321/my-notebook` for the wrapped page, or `http://localhost:4321/notebooks/my-notebook/index.html` for the standalone bundle (most static hosts also serve the shorter `/notebooks/my-notebook/` directory URL in production).

A few points worth keeping in mind:

- Use `--mode run` for published output so visitors get the app without the editor chrome. Reserve `--mode edit` for local experiments.
- Exported bundles under `public/notebooks/` are generated files and are not committed. `pnpm build` regenerates them automatically.
- Never export into `src/pages/`. That folder holds Astro routes only; raw bundles belong in `public/notebooks/`, with thin wrapper pages generated from `src/pages/[slug].astro`.
- Keep each notebook's dependencies declared in its PEP 723 metadata block (`# /// script` … `# ///`) so packages install correctly in the browser. Notebook files must stay within the 2 GB WebAssembly memory limit and avoid packages without a WebAssembly-compatible wheel.

## Browser notifications

Marimo sends a browser notification (`Execution completed`) every time a run finishes while its tab is in the background — and when notification permission is still undecided, it requests permission on each such run. If you once clicked "Allow", background runs will keep notifying you. There is currently no marimo setting to switch this off (upstream issue [marimo-team/marimo#3659](https://github.com/marimo-team/marimo/issues/3659)).

To stop it immediately in your own browser, block notifications for the marimo origin:

- **Chrome / Edge:** padlock (or tune) icon in the address bar → Site settings → Notifications → Block. Do this for both `localhost:2718` (local `marimo edit` / `marimo run`) and the hosted site.
- **Firefox:** padlock icon → Connection secure → More information → Permissions → uncheck "Use default" under "Send Notifications" and select Block.

The hosted site itself never prompts visitors: the notebook wrapper page declines notification permission requests inside the embedded frame on their behalf. Anyone who previously granted permission can still revoke it per site as described above.

> Note, AI was **heavily** used in the making of this project

Created with ❤️ by Ayush Singh
