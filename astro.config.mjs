// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import fs from 'node:fs';
import path from 'node:path';

// Dev-only fallback: notebook pages are raw marimo files served from public/
// (public/<slug>/index.html), and dev servers do not resolve directory URLs
// to index.html the way static hosts do. Rewrite/<slug>[/edit] to the matching
// index.html when one exists on disk; never intercepts Astro routes or files.
function notebookIndexFallback() {
	return {
		name: 'notebook-index-fallback',
		apply: 'serve',
		configureServer(server) {
			server.middlewares.use((req, _res, next) => {
				const urlPath = decodeURIComponent((req.url || '').split('?')[0]);
				if (urlPath === '/' || path.extname(urlPath) !== '') {
					next();
					return;
				}
				const trimmed = urlPath.replace(/\/+$/, '');
				const candidate = path.join(server.config.publicDir, `${trimmed}/index.html`);
				if (fs.existsSync(candidate)) {
					req.url = `${trimmed}/index.html`;
				}
				next();
			});
		},
	};
}

// https://astro.build/config
export default defineConfig({
	vite: {
		plugins: [tailwindcss(), notebookIndexFallback()],
	},
});
