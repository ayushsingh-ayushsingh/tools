import fs from 'node:fs';
import path from 'node:path';

export interface NotebookEntry {
	slug: string;
	title: string;
}

export function titleFromSlug(slug: string): string {
	return slug
		.split(/[-_]+/)
		.map((word) => word.charAt(0).toUpperCase() + word.slice(1))
		.join(' ');
}

// Single source of truth for notebook discovery, shared by the catalogue.
// Notebook pages themselves are the raw marimo bundles exported to
// public/<slug>/ by `pnpm notebooks:export`, not Astro routes.
export function discoverNotebooks(): NotebookEntry[] {
	const notebooksDir = path.join(process.cwd(), 'notebooks', 'src');
	let files: string[] = [];
	try {
		files = fs.readdirSync(notebooksDir);
	} catch {
		return [];
	}
	return files
		.filter((file) => file.endsWith('.py') && !path.basename(file).startsWith('_'))
		.sort()
		.map((file) => {
			const slug = path.basename(file, '.py');
			return { slug, title: titleFromSlug(slug) };
		});
}
