# Colors

Kumo uses semantic color tokens that automatically adapt to light and dark mode. Use these classes in your Tailwind CSS instead of raw color values.

---

## [Usage](#usage)

Always use semantic tokens instead of raw Tailwind colors. This ensures your UI automatically adapts to light and dark mode, and that your components remain consistent across themes.

#### [Correct](#correct)

```
<div className="bg-kumo-base text-kumo-default border-kumo-hairline">
  <button className="bg-kumo-brand text-white">Primary</button>
  <button className="bg-kumo-control text-kumo-default">Secondary</button>
</div>
```

#### [Incorrect](#incorrect)

```
{
  /* Never use raw Tailwind colors */
}
<div className="bg-white dark:bg-gray-900 text-black dark:text-white">
  <button className="bg-blue-500">Primary</button>
</div>;
```

> Lint rules enforce this: The `no-primitive-colors` rule will flag any raw Tailwind colors like `bg-blue-500`.

## [Mode](#mode)

Set `data-mode` on a parent element to control light/dark mode. Never use Tailwind’s `dark:` variant — semantic tokens handle dark mode automatically via CSS `light-dark()`.

```
// Set mode on html or body
<html data-mode="light">  // Light mode
<html data-mode="dark">   // Dark mode

// Components automatically adapt - no dark: variants needed
<div className="bg-kumo-base text-kumo-default" />
```

## [Themes](#themes)

Themes override semantic token values while preserving the same token names. Set `data-theme` on a parent element to apply a theme.

### [Available Themes](#available-themes)

- `kumo` — Default theme (no attribute needed)
- `fedramp` — Government compliance styling

```
// Apply a theme to a section or the whole app
<div data-theme="fedramp">
  {/* All Kumo components inside use fedramp token overrides */}
  <Button>FedRAMP Styled</Button>
</div>

// Themes work with both light and dark mode
<html data-mode="dark" data-theme="fedramp">
```

### [Theme Generator](#theme-generator)

Themes are defined in a centralized config and generated as CSS files. The theme generator ensures consistency across all themes.

```

# List all tokens and their theme overrides

pnpm --filter @cloudflare/kumo codegen:themes --list

# Generate theme CSS files

pnpm --filter @cloudflare/kumo codegen:themes

# Preview changes without writing files

pnpm --filter @cloudflare/kumo codegen:themes --dry-run
```

Theme config: `packages/kumo/scripts/theme-generator/config.ts`

### [Creating a New Theme](#creating-a-new-theme)

Add theme overrides in the config file. Only override tokens that need to change — all other tokens inherit from the base kumo theme.

```
// In scripts/theme-generator/config.ts
export const THEME_CONFIG: ThemeConfig = {
  color: {
    "kumo-base": {
      newName: "",
      theme: {
        kumo: {
          light: "var(--color-white, #fff)",
          dark: "var(--color-black, #000)",
        },
        // Add your theme override
        myTheme: {
          light: "#f0f4f8",
          dark: "#1a1f2e",
        },
      },
    },
    // ... other tokens
  },
};

// Add to available themes
export const AVAILABLE_THEMES = ["kumo", "fedramp", "myTheme"] as const;
```

Then run `pnpm codegen:themes` to generate the CSS.

## [Semantic Tokens](#semantic-tokens)

We use semantic tokens to group colors by purpose. Use the token that matches the role of the element, not the color you want to achieve.

Semantic tokens are named by **role**, not by hue. A token like `bg-kumo-danger` communicates intent — it doesn’t imply a specific shade of red, and its exact value can change per theme or color mode without touching your component code.

### [Surface Hierarchy](#surface-hierarchy)

Surfaces establish depth and layering in the UI. Use them in order from the outermost background inward.

| Token              | Purpose                                                                      |
| ------------------ | ---------------------------------------------------------------------------- |
| `bg-kumo-canvas`   | The outermost page background — sits behind everything                       |
| `bg-kumo-base`     | Default component background                                                 |
| `bg-kumo-elevated` | Slightly elevated surface, e.g. `LayerCard.Secondary`                        |
| `bg-kumo-recessed` | Recessed surface with a subtly darker fill, e.g. segmented `Tabs` background |
| `bg-kumo-tint`     | Subtle tinted background for tables or hover states                          |
| `bg-kumo-contrast` | High-contrast, inverted background                                           |

### [Brand](#brand)

| Token                 | Purpose                           |
| --------------------- | --------------------------------- |
| `bg-kumo-brand`       | Primary brand background          |
| `bg-kumo-brand-hover` | Hover state for brand backgrounds |

### [Semantic Status Colors](#semantic-status-colors)

Each status color comes in two variants: a solid color for icons and indicators, and a `-tint` variant for background fills behind content (i.e. `Badge` or `Banner`).

| Token             | Purpose                     |
| ----------------- | --------------------------- |
| `bg-kumo-info`    | Info indicator              |
| `bg-kumo-success` | Success indicator           |
| `bg-kumo-warning` | Warning indicator           |
| `bg-kumo-danger`  | Error/destructive indicator |

Use the solid token `bg-kumo-*` for status dots, `fill-kumo-*` for icons, and `border-kumo-*`, `ring-kumo-*` for borders and rings. Banners and badges use the `-tint` variant with varying opacity values.

```
import { WarningIcon } from "@phosphor-icons/react";

export function StatusBannerDemo() {
  return (
    <div className="flex items-center gap-2 rounded-lg bg-kumo-danger-tint/70 p-4">
      <WarningIcon weight="fill" className="fill-kumo-danger" />
      <span className="text-sm text-kumo-danger">Something went wrong.</span>
    </div>
  );
}
```

### [Text Colors](#text-colors)

| Token                   | Purpose                                                              |
| ----------------------- | -------------------------------------------------------------------- |
| `text-kumo-default`     | Primary body text                                                    |
| `text-kumo-strong`      | Stronger text contrast than default for headers and important labels |
| `text-kumo-subtle`      | Muted text for descriptions, captions, or secondary labels           |
| `text-kumo-inactive`    | Disabled or inactive text                                            |
| `text-kumo-placeholder` | Placeholder text in inputs                                           |
| `text-kumo-inverse`     | Text intended for use on high-contrast or inverted backgrounds       |
| `text-kumo-link`        | Link text                                                            |
| `text-kumo-info`        | Info-colored text                                                    |
| `text-kumo-success`     | Success-colored text                                                 |
| `text-kumo-warning`     | Warning-colored text                                                 |
| `text-kumo-danger`      | Error/destructive text                                               |

> Semantic text colors (i.e. `text-kumo-success`) are darker by default to provide better contrast and readability against `tint-*` backgrounds.

### [Borders & Rings](#borders--rings)

| Token           | Purpose                                                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| `kumo-hairline` | A border/ring color to distinguish between flat surfaces where no shadow is present (i.e. `LayerCard`). |
| `kumo-line`     | A thicker border/ring color that defines the edge of an elevated surface alongside a shadow.            |

## [Token Reference](#token-reference)

Toggle the theme in the header to see how tokens adapt. Tokens marked as “global” are explicit opt-in classes available regardless of theme.

# Accessibility

Learn how to make the most of Kumo&#39;s accessibility features and guidelines.

---

Accessibility is a top priority for Kumo. Built on [Base UI](https://base-ui.com/react/overview/accessibility), Kumo components handle many complex accessibility details including ARIA attributes, role attributes, pointer interactions, keyboard navigation, and focus management. The goal is to provide an accessible user experience out of the box, with intuitive APIs for configuration.

This page highlights some of the key accessibility features of Kumo, as well as some ways you will need to augment the library, in order to ensure that your application is accessible to everyone.

## [Keyboard Navigation](#keyboard-navigation)

Kumo components adhere to the [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) to provide basic keyboard accessibility out of the box. This is critical for users who have difficulty using a pointer device, but it’s also important for users who prefer navigating with a keyboard or other input mode.

Many components provide support for arrow keys, alphanumeric keys, Home, End, Enter, and Esc.

## [Focus Management](#focus-management)

Kumo components manage focus automatically following a user interaction. Additionally, some components provide props like `initialFocus` and `finalFocus`, to configure focus management.

While Kumo components manage focus, it’s the developer’s responsibility to visually indicate focus. This is typically handled by styling the `:focus` or `:focus-visible` CSS pseudo-classes. [WCAG provides guidelines on focus appearance](https://www.w3.org/WAI/WCAG21/Understanding/focus-visible.html).

## [Color Contrast](#color-contrast)

When styling elements, it’s important to meet the minimum requirements for color contrast between each foreground element and its corresponding background element. Unless your application has strict requirements around compliance with current standards, consider adhering to [APCA](https://www.myndex.com/APCA/), which is slated to become the new standard in WCAG 3.

## [Accessible Labels](#accessible-labels)

Kumo provides components like `Field`, `Input`, and `Checkbox` to automatically associate form controls. Additionally, you can use the native HTML `<label>` element to provide context to corresponding inputs.

Most applications will present custom controls that require accessible names provided by markup features such as `alt`, `aria-label` or `aria-labelledby`. [WAI-ARIA provides guidelines on providing accessible names to custom controls](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/).

## [Testing](#testing)

Kumo components, built on Base UI, are tested on a broad spectrum of browsers, devices, platforms, screen readers, and environments to ensure accessibility across different user contexts.

---

For more detailed information about the accessibility features provided by Base UI, visit the [official accessibility documentation](https://base-ui.com/react/overview/accessibility).

---

name: kumo-design
description: Cloudflare product design guidance. Use when designing, implementing, or reviewing Cloudflare dashboard interfaces, Kumo UI, responsive styling, dialogs, or frontend tests.
---

# Cloudflare Design

Apply these rules when designing, implementing, or reviewing Cloudflare product interfaces. Follow recommended examples and avoid patterns marked as examples to avoid.

## Rules

### `content-text-size` Use 14px for content text

All content text—body, buttons, data, other interactables—must be 14px in size. 16px and above are restricted to headings and subheadings.

**Good**

```tsx
<Text>Content text</Text>
```

**Avoid**

```tsx
<Text size="lg">Content text</Text>
```

### `heading-case` Always sentence case headings

Never capitalize or uppercase headings. Product names must be title-cased.

**Good**

```tsx
<Text as="h2">Recent requests</Text>
```

**Avoid**

```tsx
<Text as="h2">Recent Requests</Text>
```

```tsx
<Text as="h2" DANGEROUS_className="uppercase">
  Recent requests
</Text>
```

### `font-tracking` Never change the font's tracking

Do not use the `tracking-*` classes to change the spacing between characters.

**Good**

```tsx
<span className="text-lg">Worker Metrics</span>
```

**Avoid**

```tsx
<span className="text-lg tracking-tight">Worker Metrics</span>
```

### `font-weight` Never use `font-bold`

Use `font-semibold` for headings and `font-medium` for bold inline text.

**Good**

```tsx
<Text as="h3" variant="heading">Account settings</Text>
<Text as="strong" bold>required</Text>
```

**Avoid**

```tsx
<Text as="h3" DANGEROUS_className="font-bold">Account settings</Text>
<Text as="strong" DANGEROUS_className="font-bold">required</Text>
```

### `related-text-spacing` Put related text closer together

Related text should have smaller spacing around it than the content it belongs to.

**Good**

```tsx
<div className="grid gap-6">
  <div className="grid gap-1.5">
    <Text as="h3" variant="heading">
      Web Analytics
    </Text>
    <Text>Measure site traffic without changing your code.</Text>
  </div>
  <Button>Configure</Button>
</div>
```

**Avoid**

```tsx
<div className="grid gap-4">
  <Text as="h3" variant="heading">
    Web Analytics
  </Text>
  <Text>Measure site traffic without changing your code.</Text>
  <Button>Configure</Button>
</div>
```

### `text-spacing` Optically align spacing around text

Spacing around text should take into account its line height. Typically this means vertical spacing should be slightly smaller than horizontal.

**Good**

```tsx
<LayerCard className="px-5 py-4">...</LayerCard>
```

**Avoid**

```tsx
<LayerCard className="p-5">...</LayerCard>
```

### `hover-color-transitions` Never transition colors for hover states

Color changes on hover must be immediate. Transitions on fast interactions make the UI feel sluggish.

**Good**

```tsx
<button className="hover:bg-kumo-tint">...</button>
```

**Avoid**

```tsx
<button className="transition-colors duration-300 hover:bg-kumo-tint">
  ...
</button>
```

### `shadow-borders` Never use borders with drop shadows

Use `ring ring-kumo-line` to create a transparent border that maintains sharp edges.

**Good**

```tsx
<LayerCard className="shadow-md ring ring-kumo-line">...</LayerCard>
```

**Avoid**

```tsx
<LayerCard className="border border-kumo-line shadow-md">...</LayerCard>
```

### `concentric-border-radius` Use concentric border radii

When borders or rings are 8px or less apart, their corner radii must be mathematically concentric: outer radius = inner radius + padding.

**Good**

```tsx
<div className="rounded-xl p-1">
  <div className="rounded-lg">...</div>
</div>
```

**Avoid**

```tsx
<div className="rounded-xl p-1">
  <div className="rounded-xl">...</div>
</div>
```

### `icon-alignment` Align icons with the first line of text

Inline icons must be optically the same size as and be center-aligned with text. Use `h-lh flex items-center` for multi-line alignment.

**Good**

```tsx
<div className="flex items-start gap-2">
  <span className="h-lh flex items-center">
    <Icon />
  </span>
  <Text>Text that may wrap onto multiple lines</Text>
</div>
```

**Avoid**

```tsx
<div className="flex items-start gap-2">
  <span className="flex items-center">
    <Icon />
  </span>
  <Text>Text that may wrap onto multiple lines</Text>
</div>
```

```tsx
<div className="flex items-center gap-2">
  <Icon />
  <Text>Text that may wrap onto multiple lines</Text>
</div>
```

### `inline-monospace-size` Reduce the font size of inline monospaced text

Monospaced text should have a slightly smaller font size (~0.9em) when mixed with regular text.

**Good**

```tsx
<Text size="lg">
  Edit <span className="font-mono text-[0.9em]">wrangler.toml</span> to
  continue.
</Text>
```

**Avoid**

```tsx
<Text size="lg">
  Edit <span className="font-mono">wrangler.toml</span> to continue.
</Text>
```

### `sticky-borders` Use `border` to separate sticky elements from the content

**Good**

```tsx
<div className="sticky top-0 border-b border-kumo-line">...</div>
```

**Avoid**

```tsx
<div className="sticky top-0">...</div>
```

### `collapse-content-size` Maintain content size during collapse animations

Collapsible content must maintain its content size while closing to avoid its content shifting during animations.

**Good**

```tsx
<motion.div animate={{ width: open ? 256 : 0 }}>
  <div className="w-64">...</div>
</motion.div>
```

**Avoid**

```tsx
<motion.div animate={{ width: open ? 256 : 0 }}>
  <div className="w-full min-w-0">...</div>
</motion.div>
```

### `layer-card-nesting` Never stack `LayerCard` on top of one another

**Good**

```tsx
<div>
  <Text as="h3">Recent requests</Text>
  <LayerCard>...</LayerCard>
</div>
```

**Avoid**

```tsx
<LayerCard>
  <Text as="h3">Recent requests</Text>
  <LayerCard>...</LayerCard>
</LayerCard>
```

### `dialog-rendering` Never conditionally render dialogs

Conditionally rendering dialogs disables their open/close animation. Use the `open` prop to determine if a dialog should be visible or not.

**Good**

```tsx
<Dialog.Root open={open} onOpenChange={setOpen}>
  <Dialog>
    <Dialog.Title>Edit Worker</Dialog.Title>
    <Dialog.Description>Update this Worker's settings.</Dialog.Description>
  </Dialog>
</Dialog.Root>
```

**Avoid**

```tsx
{
  open && (
    <Dialog.Root open>
      <Dialog>
        <Dialog.Title>Edit Worker</Dialog.Title>
      </Dialog>
    </Dialog.Root>
  );
}
```

---

### Instructions

This folder contains all the kumo component documentation: ./kumo_ui/kumo

```
./ui-markdown
├── autocomplete
│   └── AGENTS.md
├── badge
│   └── AGENTS.md
├── banner
│   └── AGENTS.md
├── breadcrumbs
│   └── AGENTS.md
├── button
│   └── AGENTS.md
├── charts
│   └── AGENTS.md
├── checkbox
│   └── AGENTS.md
├── clipboard-text
│   └── AGENTS.md
├── cloudflare-logo
│   └── AGENTS.md
├── codehighlighted
│   └── AGENTS.md
├── collapsible
│   └── AGENTS.md
├── combobox
│   └── AGENTS.md
├── command-palette
│   └── AGENTS.md
├── date-picker
│   └── AGENTS.md
├── dialog
│   └── AGENTS.md
├── dropdown
│   └── AGENTS.md
├── empty
│   └── AGENTS.md
├── flow
│   └── AGENTS.md
├── grid
│   └── AGENTS.md
├── input
│   └── AGENTS.md
├── inputarea
│   └── AGENTS.md
├── inputgroup
│   └── AGENTS.md
├── label
│   └── AGENTS.md
├── layer-card
│   └── AGENTS.md
├── link
│   └── AGENTS.md
├── loader
│   └── AGENTS.md
├── meter
│   └── AGENTS.md
├── pagination
│   └── AGENTS.md
├── popover
│   └── AGENTS.md
├── radio
│   └── AGENTS.md
├── select
│   └── AGENTS.md
├── sensitive-input
│   └── AGENTS.md
├── sidebar
│   └── AGENTS.md
├── skeleton-line
│   └── AGENTS.md
├── switch
│   └── AGENTS.md
├── table
│   └── AGENTS.md
├── table-of-contents
│   └── AGENTS.md
├── tabs
│   └── AGENTS.md
├── tag-input
│   └── AGENTS.md
├── text
│   └── AGENTS.md
├── toast
│   └── AGENTS.md
├── toolbar
│   └── AGENTS.md
└── tooltip
    └── AGENTS.md
```

44 directories, 43 files

> This is a pnpm project, use pnpm commands!

## Development

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)

## Instructions

```
linux at arch in ~/Projects/tools (main●●)
$ pnpm notebooks:export
$ node scripts/export-notebooks.mjs

=== image-compression.py -> public/image-compression/index.html (+ edit/index.html) ===
Running in a sandbox: /home/linux/.local/bin/uv run --isolated --no-project --compile-bytecode --with-requirements /tmp/tmppgntf3z2.txt --python >=3.12 marimo -y export html-wasm --mode run --no-show-code -f src/image-compression.py -o ../generated/notebooks/.work/image-compression
⠴ Resolving dependencies...                                                                                                                  error: Request failed after 3 retries
  Caused by: Failed to fetch: `https://pypi.org/simple/pillow/`
  Caused by: error sending request for url (https://pypi.org/simple/pillow/)
  Caused by: client error (Connect)
  Caused by: dns error
  Caused by: failed to lookup address information: Temporary failure in name resolution

Exported 1 notebook(s) as standalone pages (view-only + editable).

linux at arch in ~/Projects/tools (main●●)
$
```