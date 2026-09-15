# CodeHighlighted

Shiki-powered syntax highlighting with VS Code-quality highlighting, theming, and lazy loading.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/code/code.tsx)

---

**New in v1.10:** Shiki-powered syntax highlighting with lazy loading. Import from `@cloudflare/kumo/code` to use.

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
import { ReactNode } from "react";

/**
 * Wrapper component that provides Shiki context for all demos.
 * This loads Shiki once and shares it across all CodeHighlighted instances.
 */
function DemoProvider({ children }: { children: ReactNode }) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={[
        "tsx",
        "typescript",
        "javascript",
        "bash",
        "json",
        "css",
        "html",
      ]}
    >
      {children}
    </ShikiProvider>
  );
}

/** Basic syntax highlighting demo */
export function CodeHighlightedBasicDemo() {
  return (
    <DemoProvider>
      <CodeHighlighted
        code={`const greeting = "Hello, World!";
console.log(greeting);`}
        lang="typescript"
      />
    </DemoProvider>
  );
}
```

## [Overview](#overview)

A Shiki-powered syntax highlighter. Supports 200+ languages with TextMate grammars, dual light/dark themes, and lazy loading. Exported from a separate entry point ( `@cloudflare/kumo/code` ) to avoid bundling Shiki for apps that don’t need it.

## [Installation](#installation)

CodeHighlighted is exported from a separate entry point to avoid bundling Shiki for apps that don’t need it.

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
```

**Important:** Do NOT import from the main `@cloudflare/kumo` entry. That would pull Shiki into your bundle even if you don’t use it.

## [Basic Usage](#basic-usage)

Wrap your app with `ShikiProvider` to configure Shiki once. All `CodeHighlighted` components inside share the same Shiki instance.

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";

export function App() {
  return (
    <ShikiProvider
      engine="javascript"
      languages={["tsx", "typescript", "bash", "json"]}
    >
      {/* All CodeHighlighted components share the same Shiki instance */}
      <CodeHighlighted code="const x = 1;" lang="typescript" />
    </ShikiProvider>
  );
}
```

## [Examples](#examples)

### [Languages](#languages)

CodeHighlighted supports 200+ languages through Shiki. Only load the languages you need.

#### [TypeScript](#typescript)

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
import { ReactNode } from "react";

/**
 * Wrapper component that provides Shiki context for all demos.
 * This loads Shiki once and shares it across all CodeHighlighted instances.
 */
function DemoProvider({ children }: { children: ReactNode }) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={[
        "tsx",
        "typescript",
        "javascript",
        "bash",
        "json",
        "css",
        "html",
      ]}
    >
      {children}
    </ShikiProvider>
  );
}

/** TypeScript with interface */
export function CodeHighlightedTypeScriptDemo() {
  return (
    <DemoProvider>
      <CodeHighlighted
        code={`interface User {
  id: string;
  name: string;
  email: string;
}

async function fetchUser(id: string): Promise<User> {
  const response = await fetch(\`/api/users/\${id}\`);
  return response.json();
}`}
        lang="typescript"
      />
    </DemoProvider>
  );
}
```

#### [React / TSX](#react--tsx)

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
import { ReactNode } from "react";

/**
 * Wrapper component that provides Shiki context for all demos.
 * This loads Shiki once and shares it across all CodeHighlighted instances.
 */
function DemoProvider({ children }: { children: ReactNode }) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={[
        "tsx",
        "typescript",
        "javascript",
        "bash",
        "json",
        "css",
        "html",
      ]}
    >
      {children}
    </ShikiProvider>
  );
}

/** React/TSX code example */
export function CodeHighlightedReactDemo() {
  return (
    <DemoProvider>
      <CodeHighlighted
        code={`import { useState } from "react";

export function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <button onClick={() => setCount(c => c + 1)}>
      Count: {count}
    </button>
  );
}`}
        lang="tsx"
      />
    </DemoProvider>
  );
}
```

#### [Bash / Shell](#bash--shell)

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
import { ReactNode } from "react";

/**
 * Wrapper component that provides Shiki context for all demos.
 * This loads Shiki once and shares it across all CodeHighlighted instances.
 */
function DemoProvider({ children }: { children: ReactNode }) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={[
        "tsx",
        "typescript",
        "javascript",
        "bash",
        "json",
        "css",
        "html",
      ]}
    >
      {children}
    </ShikiProvider>
  );
}

/** Bash/shell commands */
export function CodeHighlightedBashDemo() {
  return (
    <DemoProvider>
      <CodeHighlighted
        code={`# Install Kumo
npm install @cloudflare/kumo

# Or with pnpm
pnpm add @cloudflare/kumo

# Start development server
pnpm dev`}
        lang="bash"
      />
    </DemoProvider>
  );
}
```

#### [JSON](#json)

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
import { ReactNode } from "react";

/**
 * Wrapper component that provides Shiki context for all demos.
 * This loads Shiki once and shares it across all CodeHighlighted instances.
 */
function DemoProvider({ children }: { children: ReactNode }) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={[
        "tsx",
        "typescript",
        "javascript",
        "bash",
        "json",
        "css",
        "html",
      ]}
    >
      {children}
    </ShikiProvider>
  );
}

/** JSON configuration */
export function CodeHighlightedJsonDemo() {
  return (
    <DemoProvider>
      <CodeHighlighted
        code={`{
  "name": "@cloudflare/kumo",
  "version": "1.9.0",
  "dependencies": {
    "react": "^19.0.0",
    "shiki": "^4.0.0"
  }
}`}
        lang="json"
      />
    </DemoProvider>
  );
}
```

#### [CSS](#css)

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
import { ReactNode } from "react";

/**
 * Wrapper component that provides Shiki context for all demos.
 * This loads Shiki once and shares it across all CodeHighlighted instances.
 */
function DemoProvider({ children }: { children: ReactNode }) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={[
        "tsx",
        "typescript",
        "javascript",
        "bash",
        "json",
        "css",
        "html",
      ]}
    >
      {children}
    </ShikiProvider>
  );
}

/** CSS code example */
export function CodeHighlightedCssDemo() {
  return (
    <DemoProvider>
      <CodeHighlighted
        code={`.button {
  background: var(--color-brand);
  border-radius: 0.5rem;
  padding: 0.5rem 1rem;
  
  &:hover {
    background: var(--color-brand-hover);
  }
}`}
        lang="css"
      />
    </DemoProvider>
  );
}
```

### [Highlight Lines](#highlight-lines)

Emphasize specific lines with `highlightLines` (1-indexed).

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
import { ReactNode } from "react";

/**
 * Wrapper component that provides Shiki context for all demos.
 * This loads Shiki once and shares it across all CodeHighlighted instances.
 */
function DemoProvider({ children }: { children: ReactNode }) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={[
        "tsx",
        "typescript",
        "javascript",
        "bash",
        "json",
        "css",
        "html",
      ]}
    >
      {children}
    </ShikiProvider>
  );
}

/** With highlighted lines */
export function CodeHighlightedHighlightLinesDemo() {
  return (
    <DemoProvider>
      <CodeHighlighted
        code={`function processData(items: string[]) {
  // Filter out empty items
  const filtered = items.filter(Boolean);
  
  // Transform to uppercase (highlighted)
  const transformed = filtered.map(item => item.toUpperCase());
  
  // Return sorted result
  return transformed.toSorted();
}`}
        lang="typescript"
        highlightLines={[5, 6]}
      />
    </DemoProvider>
  );
}
```

### [Custom Highlight Color](#custom-highlight-color)

Customize the highlight color with the `--kumo-code-highlight-bg` CSS variable.

### [Line Numbers](#line-numbers)

Display line numbers with `showLineNumbers` .

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
import { ReactNode } from "react";

/**
 * Wrapper component that provides Shiki context for all demos.
 * This loads Shiki once and shares it across all CodeHighlighted instances.
 */
function DemoProvider({ children }: { children: ReactNode }) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={[
        "tsx",
        "typescript",
        "javascript",
        "bash",
        "json",
        "css",
        "html",
      ]}
    >
      {children}
    </ShikiProvider>
  );
}

/** With line numbers */
export function CodeHighlightedLineNumbersDemo() {
  return (
    <DemoProvider>
      <CodeHighlighted
        code={`import { useState, useEffect } from "react";

export function useWindowSize() {
  const [size, setSize] = useState({ width: 0, height: 0 });
  
  useEffect(() => {
    function handleResize() {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    }
    
    handleResize();
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);
  
  return size;
}`}
        lang="typescript"
        showLineNumbers
      />
    </DemoProvider>
  );
}
```

### [Copy Button](#copy-button)

Add a copy-to-clipboard button with `showCopyButton` .

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
import { ReactNode } from "react";

/**
 * Wrapper component that provides Shiki context for all demos.
 * This loads Shiki once and shares it across all CodeHighlighted instances.
 */
function DemoProvider({ children }: { children: ReactNode }) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={[
        "tsx",
        "typescript",
        "javascript",
        "bash",
        "json",
        "css",
        "html",
      ]}
    >
      {children}
    </ShikiProvider>
  );
}

/** With copy button */
export function CodeHighlightedCopyButtonDemo() {
  return (
    <DemoProvider>
      <CodeHighlighted
        code={`npm install @cloudflare/kumo`}
        lang="bash"
        showCopyButton
      />
    </DemoProvider>
  );
}
```

### [Full Featured](#full-featured)

Combine all features for a complete code display experience.

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
import { ReactNode } from "react";

/**
 * Wrapper component that provides Shiki context for all demos.
 * This loads Shiki once and shares it across all CodeHighlighted instances.
 */
function DemoProvider({ children }: { children: ReactNode }) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={[
        "tsx",
        "typescript",
        "javascript",
        "bash",
        "json",
        "css",
        "html",
      ]}
    >
      {children}
    </ShikiProvider>
  );
}

/** Full featured example */
export function CodeHighlightedFullFeaturedDemo() {
  return (
    <DemoProvider>
      <CodeHighlighted
        code={`import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";

export function CodeExample({ code, language }: Props) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={["tsx", "typescript", "bash", "json"]}
    >
      <CodeHighlighted
        code={code}
        lang={language}
        showCopyButton
      />
    </ShikiProvider>
  );
}`}
        lang="tsx"
        showCopyButton
        highlightLines={[6, 7, 8, 9]}
      />
    </DemoProvider>
  );
}
```

### [Shared Provider](#shared-provider)

Multiple code blocks can share a single `ShikiProvider`. Shiki loads once and is reused for all blocks.

```
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";
import { ReactNode } from "react";

/**
 * Wrapper component that provides Shiki context for all demos.
 * This loads Shiki once and shares it across all CodeHighlighted instances.
 */
function DemoProvider({ children }: { children: ReactNode }) {
  return (
    <ShikiProvider
      engine="javascript"
      languages={[
        "tsx",
        "typescript",
        "javascript",
        "bash",
        "json",
        "css",
        "html",
      ]}
    >
      {children}
    </ShikiProvider>
  );
}

/** Multiple code blocks sharing a provider */
export function CodeHighlightedSharedProviderDemo() {
  return (
    <DemoProvider>
      <div className="space-y-4">
        <CodeHighlighted
          code={`const config = { theme: "dark" };`}
          lang="typescript"
        />
        <CodeHighlighted code={`npm run build`} lang="bash" />
        <CodeHighlighted code={`{ "success": true }`} lang="json" />
      </div>
    </DemoProvider>
  );
}
```

## [Themes](#themes)

CodeHighlighted uses hardcoded themes for consistent styling across all Kumo applications:

-   **Light mode:** `github-light`
    
-   **Dark mode:** `vesper`
    

Theme customization is not supported. This ensures visual consistency across all code blocks in your application.

## [Server-Side Usage](#server-side-usage)

For SSR frameworks (Next.js RSC, Astro, Remix), use the server utilities to highlight at build time.

#### [One-off highlighting](#one-off-highlighting)

```
// Next.js RSC or Astro
import { highlightCode } from "@cloudflare/kumo/code/server";

export default async function Page() {
  const html = await highlightCode(`const x = 1;`, "typescript");

  return <pre dangerouslySetInnerHTML={{ __html: html }} />;
}
```

#### [Reusable highlighter](#reusable-highlighter)

```
// For multiple highlights, reuse the highlighter
import { createServerHighlighter } from "@cloudflare/kumo/code/server";

const highlighter = await createServerHighlighter({
  languages: ["tsx", "bash", "json"],
});

const html1 = highlighter.highlight(code1, "tsx");
const html2 = highlighter.highlight(code2, "bash");

highlighter.dispose(); // Clean up when done
```

## [Custom Hook](#custom-hook)

Use `useShikiHighlighter` for custom implementations.

```
import { useShikiHighlighter } from "@cloudflare/kumo/code";

function CustomCodeBlock({ code, lang }) {
  const { highlight, isLoading, isReady, error } = useShikiHighlighter();

  if (error) {
    return <div className="text-red-500">Failed to load highlighter</div>;
  }

  if (isLoading) {
    return (
      <pre className="animate-pulse">
        <code>{code}</code>
      </pre>
    );
  }

  const html = highlight(code, lang);

  // null means highlighting failed — render plain text
  if (html === null) {
    return (
      <pre>
        <code>{code}</code>
      </pre>
    );
  }

  return <pre dangerouslySetInnerHTML={{ __html: html }} />;
}
```

## [Internationalization](#internationalization)

Customize button labels at the provider level for all code blocks, or override per-component.

```
// Set labels at the provider level for all code blocks
<ShikiProvider
  engine="javascript"
  languages={["tsx", "bash"]}
  labels={{ copy: "Copier", copied: "Copié!" }}
>
  <App />
</ShikiProvider>

// Or override at the component level
<CodeHighlighted
  code={code}
  lang="tsx"
  showCopyButton
  labels={{ copy: "Copy code", copied: "Done!" }}
/>
```

## [Framework Integration](#framework-integration)

### [Next.js App Router](#nextjs-app-router)

```
// app/providers.tsx
"use client";

import { ShikiProvider } from "@cloudflare/kumo/code";

export function Providers({ children }) {
  return (
    <ShikiProvider engine="javascript" languages={["tsx", "bash", "json"]}>
      {children}
    </ShikiProvider>
  );
}

// app/layout.tsx
import { Providers } from "./providers";

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
```

### [Astro (Static)](#astro-static)

For static sites, use server-side highlighting for zero client-side JavaScript.

```
---
// src/components/CodeBlock.astro
import { highlightCode } from "@cloudflare/kumo/code/server";

const { code, lang } = Astro.props;
const html = await highlightCode(code, lang);
---

<div class="code-block" set:html={html} />
```

## [Bundle Size](#bundle-size)

Shiki is lazy-loaded on first render. The size depends on your configuration:

| Scenario | Languages | Engine | Lazy Load Size |
| --- | --- | --- | --- |
| Minimal | tsx, json | JS | ~75 KB |
| Standard | tsx, ts, bash, json, css, yaml | JS | ~95 KB |
| Full | 15+ languages | WASM | ~250 KB |

Teams that don’t import from `@cloudflare/kumo/code` pay 0 KB.

## [Migration from Code/CodeBlock](#migration-from-codecodeblock)

The legacy `Code` and `CodeBlock` components are deprecated. They will be removed in v2.0.

```
// Before (deprecated)
import { Code, CodeBlock } from "@cloudflare/kumo";
<CodeBlock code="const x = 1;" lang="ts" />

// After
import { ShikiProvider, CodeHighlighted } from "@cloudflare/kumo/code";

// Once at app root
<ShikiProvider engine="javascript" languages={["tsx"]}>
  <App />
</ShikiProvider>

// In components
<CodeHighlighted code="const x = 1;" lang="tsx" />
```

## [API Reference](#api-reference)

### [ShikiProvider Props](#shikiprovider-props)

| Prop | Type | Required | Description |
| --- | --- | --- | --- |
| `engine` | `”javascript” | “wasm”` | Yes | JS is smaller (~50KB), WASM is more accurate (~180KB) |
| `languages` | `string[]` | Yes | Languages to support (e.g., \[“tsx”, “bash”\]) |
| `labels` | `{ copy?: string, copied?: string }` | No | Localized labels for copy button |
| `children` | `ReactNode` | Yes | App content |

### [CodeHighlighted Props](#codehighlighted-props)

| Prop | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Source code to display |
| `lang` | `string` | Yes | Language identifier (must be in provider’s languages) |
| `showLineNumbers` | `boolean` | No | Display line numbers |
| `highlightLines` | `number[]` | No | Lines to emphasize (1-indexed) |
| `showCopyButton` | `boolean` | No | Show copy-to-clipboard button |
| `labels` | `{ copy?: string, copied?: string }` | No | Override provider labels for this instance |
| `className` | `string` | No | Additional CSS classes |

### [useShikiHighlighter Return Value](#useshikihighlighter-return-value)

| Property | Type | Description |
| --- | --- | --- |
| `highlight` | `(code, lang, options?) => string | null` | Returns highlighted HTML, or null if not ready |
| `isLoading` | `boolean` | True while Shiki is loading |
| `isReady` | `boolean` | True when highlight() is safe to call |
| `error` | `Error | null` | Error if Shiki initialization failed |