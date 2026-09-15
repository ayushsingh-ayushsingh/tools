# [tools.ayushthinks.com](https://tools.ayushthinks.com)

A catalogue of interactive [marimo](https://marimo.io) notebooks, hosted as a static [Astro](https://astro.build) site. Each notebook is exported to WebAssembly and runs entirely in the visitor's browser — no Python server required.

## Project structure

```text
/
├── notebooks/            # Python workspace (managed with uv)
│   ├── src/              # Notebook sources — create every new notebook here
│   │   ├── image-compression.py
│   │   └── marimo_nb/    # Launcher package (auto-discovers notebooks in src/)
│   ├── README.md         # Notebook workflow: setup, editing, export
│   └── AGENTS.md         # Contributor guide for agents working on notebooks
├── public/
│   └── <slug>/            # Per-notebook pages (generated, not committed)
│       ├── index.html      # Raw marimo bundle, view-only (+ theme payload)
│       ├── assets/         # WASM framework assets
│       ├── logo.png, favicon.ico, …  # Static files marimo emits
│       └── edit/
│           ├── index.html  # Raw marimo bundle, editable (shares ../assets/)
│           └── logo.png, favicon.ico
├── scripts/
│   └── export-notebooks.mjs  # Exports each notebook to public/<slug>/ (+ edit/)
├── src/
│   ├── lib/
│   │   └── notebooks.ts        # Shared notebook discovery (slugs + titles)
│   └── pages/
│       └── index.astro   # Catalogue listing every notebook
└── package.json
```

How the pieces fit together:

1. Notebook sources live in `notebooks/src/<slug>.py`.
2. `pnpm notebooks:export` exports each one in both flavours — view-only and editable — as raw marimo bundles to `public/<slug>/index.html` and `public/<slug>/edit/index.html`.
3. Those files ARE the notebook pages: `/<slug>` and `/<slug>/edit` serve the marimo HTML directly, full-screen, with no wrapper chrome and no `/notebooks/*` route. The only deliberate difference from pristine marimo output is dark-mode support (a pre-paint script + style follows the site theme, else the OS preference). The catalogue at `/` lists them all.

## Prerequisites

- Node.js 22.12 or later with `pnpm`.
- Python 3.12 or later with [`uv`](https://docs.astral.sh/uv/) for the notebooks workspace.

## Quick start

Install web dependencies and start the dev server:

```sh
pnpm install
pnpm dev
```

The site is then available at `http://localhost:4321`.

To work on the notebooks themselves, see [`notebooks/README.md`](notebooks/README.md). In short:

```sh
cd notebooks
uv sync
uv run marimo edit src/image-compression.py
```

## Adding a new notebook

Create the file in `notebooks/src/` — not in the `notebooks/` root — so it is picked up automatically:

```sh
cd notebooks
uv run marimo new src/my-notebook.py
```

Then check it, export it, and confirm it appears on the site:

```sh
uv run marimo check src/my-notebook.py --select MW
pnpm notebooks:export
pnpm dev
```

Exports contain both flavours by default: view-only (`--mode run --no-show-code`) and editable. To show code by default in the view-only bundle:

```sh
node scripts/export-notebooks.mjs --show-code
```

The notebook will be live at `/my-notebook` (view-only) and `/my-notebook/edit` (editable) — the only two notebook pages. The full workflow, including WebAssembly compatibility notes, is covered in [`notebooks/README.md`](notebooks/README.md).

## Scripts

| Command                        | Action                                                              |
| :----------------------------- | :------------------------------------------------------------------ |
| `pnpm install`                 | Installs web dependencies                                           |
| `pnpm dev`                     | Starts the local dev server at `localhost:4321`                     |
| `pnpm notebooks:export`        | Exports every notebook in `notebooks/src/` to `public/<slug>/` (view-only + editable, raw marimo HTML + theme payload) |
| `pnpm notebooks:export:check`  | As above, with a WASM compatibility check first                     |
| `pnpm build`                   | Exports notebooks, then builds the static site to `./dist/`         |
| `pnpm preview`                 | Previews the production build locally                               |
| `pnpm astro ...`               | Runs Astro CLI commands such as `astro add` or `astro check`        |

`pnpm build` runs the notebook export automatically via `prebuild`, so `./dist/` always contains the latest notebooks. Exported bundles are deliberately git-ignored; the repository stays lean and every build reproduces them from source.

## Deployment

The build output in `./dist/` is a fully static site — any static host will do. Serve it over HTTP(S); exported notebooks cannot run from `file://` URLs.

> Note, AI was **heavily** used in the making of this project

Created with ❤️ by Ayush Singh
