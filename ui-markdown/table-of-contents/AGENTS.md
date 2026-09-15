# Table of Contents

Presentational compound component for section navigation with an active indicator bar.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/table-of-contents/table-of-contents.tsx)

---

```
import { TableOfContents } from "@cloudflare/kumo";

function DemoWrapper({ children }: { children: React.ReactNode }) {
  return <div className="min-w-48">{children}</div>;
}

export function TableOfContentsBasicDemo() {
  return (
    <DemoWrapper>
      <TableOfContents>
        <TableOfContents.Title>On this page</TableOfContents.Title>
        <TableOfContents.List>
          {headings.map((heading) => (
            <TableOfContents.Item
              key={heading.text}
              active={heading.text === "Usage"}
              className="cursor-pointer"
            >
              {heading.text}
            </TableOfContents.Item>
          ))}
        </TableOfContents.List>
      </TableOfContents>
    </DemoWrapper>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { TableOfContents } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { TableOfContents } from "@cloudflare/kumo/components/table-of-contents";
```

## [Usage](#usage)

```
import { TableOfContents } from "@cloudflare/kumo";

export default function Example() {
  return (
    <TableOfContents>
      <TableOfContents.Title>On this page</TableOfContents.Title>
      <TableOfContents.List>
        <TableOfContents.Item href="#intro" active>
          Introduction
        </TableOfContents.Item>
        <TableOfContents.Item href="#api">API Reference</TableOfContents.Item>
      </TableOfContents.List>
    </TableOfContents>
  );
}
```

This component is purely presentational — you control `active` on each item. For automatic scroll tracking, pair it with the `useTableOfContentsActiveId` hook below.

## [Scroll tracking](#scroll-tracking)

`useTableOfContentsActiveId` derives the active section from scroll position: pass the section ids in document order and it returns the id of the topmost section in view, plus a `selectSection` action that pins a clicked section until the smooth scroll settles (so short sections stay highlighted after a jump). Hash deep-links (`#usage`) are handled automatically. The hook is SSR-safe — all DOM access happens in effects.

```
import { TableOfContents, useTableOfContentsActiveId } from "@cloudflare/kumo";

export default function Example({ headings }) {
  const { activeId, selectSection } = useTableOfContentsActiveId({
    ids: headings.map((h) => h.slug),
    offset: 64, // fixed header height in px
  });

  return (
    <TableOfContents>
      <TableOfContents.Title>On this page</TableOfContents.Title>
      <TableOfContents.List>
        {headings.map((h) => (
          <TableOfContents.Item
            key={h.slug}
            href={`#${h.slug}`}
            active={activeId === h.slug}
            onClick={() => selectSection(h.slug)}
          >
            {h.text}
          </TableOfContents.Item>
        ))}
      </TableOfContents.List>
    </TableOfContents>
  );
}
```

Pass a `root` element to track a custom scroll container instead of the viewport (and `trackHash: false` when hash navigation doesn’t apply):

```
import { useState } from "react";
import { TableOfContents, useTableOfContentsActiveId } from "@cloudflare/kumo";

/**
 * Live scroll tracking via `useTableOfContentsActiveId`, scoped to a custom
 * scroll container through the `root` option. Scroll the content — the active
 * item follows; click an item to jump.
 */
export function TableOfContentsScrollspyDemo() {
  const [root, setRoot] = useState<HTMLDivElement | null>(null);

  const { activeId, selectSection } = useTableOfContentsActiveId({
    ids: scrollspySections.map((s) => s.id),
    root,
    trackHash: false,
  });

  return (
    <div className="flex w-full max-w-xl gap-6">
      <div className="min-w-40">
        <TableOfContents>
          <TableOfContents.Title>On this page</TableOfContents.Title>
          <TableOfContents.List>
            {scrollspySections.map((section) => (
              <TableOfContents.Item
                key={section.id}
                render={<button type="button" />}
                active={activeId === section.id}
                onClick={() => {
                  selectSection(section.id);
                  root
                    ?.querySelector(`#${section.id}`)
                    ?.scrollIntoView({ behavior: "smooth", block: "start" });
                }}
              >
                {section.title}
              </TableOfContents.Item>
            ))}
          </TableOfContents.List>
        </TableOfContents>
      </div>
      <div
        ref={setRoot}
        className="h-64 flex-1 overflow-y-auto rounded-lg border border-kumo-hairline p-4"
      >
        {scrollspySections.map((section) => (
          <section key={section.id}>
            <h4
              id={section.id}
              className="mb-2 scroll-mt-2 text-sm font-semibold"
            >
              {section.title}
            </h4>
            <p className="mb-6 text-sm text-kumo-subtle">
              {Array.from(
                { length: 6 },
                () =>
                  `Scrollable placeholder copy for the ${section.title} section. `,
              ).join("")}
            </p>
          </section>
        ))}
        <div className="h-40" />
      </div>
    </div>
  );
}
```

### [Options](#options)

`ids` — section anchor ids, in document order (required). `offset` — px from the top of the viewport/root to the activation line, typically your fixed header height (default `0`). `root` — custom scroll container (default: viewport). `trackHash` — select the section from `location.hash` on load and `hashchange` (default `true`).

## [Examples](#examples)

### [Interactive](#interactive)

Click an item to set it as active. The consumer controls state via `active` and `onClick`.

```
import { useState } from "react";
import { TableOfContents } from "@cloudflare/kumo";

function DemoWrapper({ children }: { children: React.ReactNode }) {
  return <div className="min-w-48">{children}</div>;
}

export function TableOfContentsInteractiveDemo() {
  const [active, setActive] = useState("Introduction");

  return (
    <DemoWrapper>
      <TableOfContents>
        <TableOfContents.Title>On this page</TableOfContents.Title>
        <TableOfContents.List>
          {headings.map((heading) => (
            <TableOfContents.Item
              key={heading.text}
              active={heading.text === active}
              onClick={() => setActive(heading.text)}
              className="cursor-pointer"
            >
              {heading.text}
            </TableOfContents.Item>
          ))}
        </TableOfContents.List>
      </TableOfContents>
    </DemoWrapper>
  );
}
```

### [No active item](#no-active-item)

When no item has `active` set, all items show the default subtle text style with a hover indicator.

```
import { TableOfContents } from "@cloudflare/kumo";

function DemoWrapper({ children }: { children: React.ReactNode }) {
  return <div className="min-w-48">{children}</div>;
}

export function TableOfContentsNoActiveDemo() {
  return (
    <DemoWrapper>
      <TableOfContents>
        <TableOfContents.Title>On this page</TableOfContents.Title>
        <TableOfContents.List>
          {headings.map((heading) => (
            <TableOfContents.Item key={heading.text} className="cursor-pointer">
              {heading.text}
            </TableOfContents.Item>
          ))}
        </TableOfContents.List>
      </TableOfContents>
    </DemoWrapper>
  );
}
```

### [Groups](#groups)

Use `TableOfContents.Group` to organize items into labeled sections with indented children. Groups support two modes: pass an `href` to make the group label a clickable link (like “Examples” and “API” below), or omit it for a plain non-interactive title (like “Getting Started”).

```
import { TableOfContents } from "@cloudflare/kumo";

function DemoWrapper({ children }: { children: React.ReactNode }) {
  return <div className="min-w-48">{children}</div>;
}

/** Shows both group modes: clickable group labels (with `href`) and plain title labels (without `href`). */
export function TableOfContentsGroupDemo() {
  return (
    <DemoWrapper>
      <TableOfContents>
        <TableOfContents.Title>On this page</TableOfContents.Title>
        <TableOfContents.List>
          <TableOfContents.Item active className="cursor-pointer">
            Overview
          </TableOfContents.Item>
          <TableOfContents.Group label="Examples" href="#examples-demo">
            <TableOfContents.Item className="cursor-pointer">
              Basic example
            </TableOfContents.Item>
            <TableOfContents.Item className="cursor-pointer">
              Advanced example
            </TableOfContents.Item>
          </TableOfContents.Group>
          <TableOfContents.Group label="Getting Started">
            <TableOfContents.Item className="cursor-pointer">
              Installation
            </TableOfContents.Item>
            <TableOfContents.Item className="cursor-pointer">
              Configuration
            </TableOfContents.Item>
          </TableOfContents.Group>
          <TableOfContents.Group label="API" href="#api-demo">
            <TableOfContents.Item className="cursor-pointer">
              Props
            </TableOfContents.Item>
            <TableOfContents.Item className="cursor-pointer">
              Events
            </TableOfContents.Item>
          </TableOfContents.Group>
        </TableOfContents.List>
      </TableOfContents>
    </DemoWrapper>
  );
}
```

### [Without title](#without-title)

The title sub-component is optional — use `TableOfContents.List` directly if you don’t need a heading.

```
import { TableOfContents } from "@cloudflare/kumo";

function DemoWrapper({ children }: { children: React.ReactNode }) {
  return <div className="min-w-48">{children}</div>;
}

export function TableOfContentsWithoutTitleDemo() {
  return (
    <DemoWrapper>
      <TableOfContents>
        <TableOfContents.List>
          {headings.slice(0, 3).map((heading) => (
            <TableOfContents.Item
              key={heading.text}
              active={heading.text === "Introduction"}
              className="cursor-pointer"
            >
              {heading.text}
            </TableOfContents.Item>
          ))}
        </TableOfContents.List>
      </TableOfContents>
    </DemoWrapper>
  );
}
```

### [Custom element](#custom-element)

Use the `render` prop to swap the default anchor for a button, router link, or any element.

```
import { useState } from "react";
import { TableOfContents } from "@cloudflare/kumo";

function DemoWrapper({ children }: { children: React.ReactNode }) {
  return <div className="min-w-48">{children}</div>;
}

/** Demonstrates using the `render` prop with a custom link component. */
export function TableOfContentsRenderPropDemo() {
  const [clicked, setClicked] = useState<string | null>(null);

  return (
    <DemoWrapper>
      <div className="space-y-3">
        <TableOfContents>
          <TableOfContents.List>
            {["Introduction", "Installation", "Usage"].map((text) => (
              <TableOfContents.Item
                key={text}
                render={<button type="button" />}
                onClick={() => setClicked(text)}
                active={text === "Introduction"}
              >
                {text}
              </TableOfContents.Item>
            ))}
          </TableOfContents.List>
        </TableOfContents>
        {clicked && (
          <p className="text-xs text-kumo-subtle">Clicked: {clicked}</p>
        )}
      </div>
    </DemoWrapper>
  );
}
```

#### [React Router](#react-router)

```
<TableOfContents.Item render={<Link to="/intro" />} active>
  Introduction
</TableOfContents.Item>
```

#### [Next.js](#nextjs)

```
import Link from "next/link";

<TableOfContents.Item render={<Link href="/intro" />} active>
  Introduction
</TableOfContents.Item>;
```

#### [Button (no navigation)](#button-no-navigation)

```
<TableOfContents.Item render={<button type="button" />} onClick={handleClick}>
  Introduction
</TableOfContents.Item>
```

## [API Reference](#api-reference)

### [`TableOfContents`](#tableofcontents)

Root nav container with a default `aria-label` of “Table of contents”.

| Prop | Type | Default |
| --- | --- | --- |
| children | `ReactNode` | \- |
| className | `string` | \- |
| id | `string` | \- |
| lang | `string` | \- |
| title | `string` | \- |

### [`TableOfContents.Title`](#tableofcontentstitle)

Optional uppercase heading displayed above the list (renders a `<p>`).

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [`TableOfContents.List`](#tableofcontentslist)

List container with a left border rail.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [`TableOfContents.Item`](#tableofcontentsitem)

Individual navigation link. Set `active` for the current section. Use the `render` prop to swap the anchor for a router link or button.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| active | `boolean` | \- | Whether this item represents the currently active section. |
| render | `React.ReactElement` | \- | Custom element to render as the link. Use this to integrate with framework routers (e.g., Next.js \`<Link>\`, React Router \`<NavLink>\`). The element receives all anchor props including \`href\`, \`className\`, and \`children\`. |

### [`TableOfContents.Group`](#tableofcontentsgroup)

Groups items under a labeled section with indented children. Pass `href` to make the label a clickable link, or omit for a plain title.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| label\* | `string` | \- | Label displayed above the group's items. |
| href | `string` | \- | URL the group label links to. When provided, the label renders as a clickable link with item styling. |
| active | `boolean` | \- | Whether this group's label represents the currently active section. Only applies when \`href\` is provided. |