# Link

A styled anchor component for inline text links with multiple variants and composition support.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/link/link.tsx)

---

```
import { Link } from "@cloudflare/kumo";

export function LinkBasicDemo() {
  return (
    <div className="grid gap-x-6 gap-y-4 text-base md:grid-cols-3">
      <Link href="#">Default inline link</Link>
      <Link href="#" variant="current">
        Current color link
      </Link>
      <Link href="#" variant="plain">
        Plain inline link
      </Link>
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Link } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Link } from "@cloudflare/kumo/components/link";
```

## [Usage](#usage)

### [Basic Link](#basic-link)

The default Link component renders an underlined anchor with primary color styling.

```
import { Link } from "@cloudflare/kumo";

export default function Example() {
  return (
    <p>
      Read our <Link href="/docs">documentation</Link> for more details.
    </p>
  );
}
```

### [External Links](#external-links)

Use the `Link.ExternalIcon` subcomponent to indicate links that open in a new tab.

```
import { Link } from "@cloudflare/kumo";

export default function Example() {
  return (
    <Link
      href="https://cloudflare.com"
      target="_blank"
      rel="noopener noreferrer"
    >
      Visit Cloudflare <Link.ExternalIcon />
    </Link>
  );
}
```

### [Framework Integration (LinkProvider)](#framework-integration-linkprovider)

For app-wide router integration, configure a `LinkProvider` at your app root. Your wrapper component receives `href` and is responsible for bridging to your router’s API. This lets engineers use `<Link href="...">` everywhere without thinking about routing internals.

```
import { forwardRef } from "react";
import { LinkProvider } from "@cloudflare/kumo";
import { Link as RouterLink } from "react-router-dom";

// Your app's wrapper maps href to the router's navigation prop
// and handles external URLs with a plain <a>
const AppLink = forwardRef(({ href, to, ...rest }, ref) => {
  const destination = href ?? to;
  const isExternal =
    destination?.startsWith("http") &&
    new URL(destination).origin !== window.location.origin;

  if (isExternal) {
    return <a ref={ref} href={destination} {...rest} />;
  }
  return <RouterLink ref={ref} to={destination} {...rest} />;
});

// Wrap your app once
export function App() {
  return (
    <LinkProvider component={AppLink}>
      {/* All <Link href="..."> calls go through AppLink */}
      <YourApp />
    </LinkProvider>
  );
}
```

### [Composition with render prop](#composition-with-render-prop)

For exceptional cases where you need direct control over the rendered element, use the `render` prop. This bypasses the `LinkProvider` entirely — all other props (`href`, `target`, `className`, etc.) are merged onto the provided element automatically.

```
import { Link } from "@cloudflare/kumo";
import { Link as RouterLink } from "react-router-dom";

export default function Example() {
  return (
    <>
      {/* Force a specific router link (bypasses LinkProvider) */}
      <Link render={<RouterLink to="/dashboard" />} variant="inline">
        Dashboard
      </Link>

      {/* Force a plain anchor (bypasses LinkProvider) */}
      <Link render={<a />} href="https://example.com" target="_blank" rel="noopener noreferrer">
        External Site <Link.ExternalIcon />
      </Link>
    </>
  );
}
```

## [Examples](#examples)

### [Inline in Paragraph](#inline-in-paragraph)

Links flow naturally within paragraph text with proper underline offset.

```
import { Link } from "@cloudflare/kumo";

export function LinkInParagraphDemo() {
  return (
    <p className="mx-auto max-w-md text-base leading-relaxed text-kumo-default">
      This is a paragraph with an <Link href="#">inline link</Link> that flows
      naturally with the surrounding text. Links maintain proper underline
      offset for readability.
    </p>
  );
}
```

### [External Link with Icon](#external-link-with-icon)

Use `Link.ExternalIcon` to visually indicate links that navigate away from your site.

```
import { Link } from "@cloudflare/kumo";

export function LinkExternalDemo() {
  return (
    <Link
      href="https://cloudflare.com"
      target="_blank"
      rel="noopener noreferrer"
      className="text-base"
    >
      Visit Cloudflare <Link.ExternalIcon />
    </Link>
  );
}
```

### [Current Variant (Color Inheritance)](#current-variant-color-inheritance)

The `current` variant inherits color from its parent, useful for links within colored contexts like alerts.

```
import { Link } from "@cloudflare/kumo";

export function LinkCurrentVariantDemo() {
  return (
    <p className="text-base text-kumo-danger">
      This error message contains a{" "}
      <Link href="#" variant="current">
        link
      </Link>{" "}
      that inherits the red color from its parent.
    </p>
  );
}
```

### [Composition with render prop](#composition-with-render-prop-1)

The `render` prop lets you compose Link styling onto any element, enabling integration with framework routing components.

```
import { Link } from "@cloudflare/kumo";

export function LinkRenderDemo() {
  return (
    <div className="flex flex-col gap-x-6 gap-y-4 text-base md:flex-row">
      <Link render={<CustomRouterLink href="/dashboard" />} variant="inline">
        Dashboard (via render)
      </Link>
      <Link
        render={
          <CustomRouterLink
            href="https://developers.cloudflare.com"
            target="_blank"
            rel="noopener noreferrer"
          />
        }
        variant="inline"
      >
        Cloudflare Docs <Link.ExternalIcon />
      </Link>
    </div>
  );
}
```

## [API Reference](#api-reference)

### [Link Props](#link-props)

Extends all native anchor element attributes.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| variant | “inline” | “current” | “plain" | "inline” | Visual style variant |
| render | ReactElement | \- | Element to render with Link props merged onto it |
| href | string | \- | Link destination URL. Use this for all links — both internal and external. Configure a `LinkProvider` to bridge `href` to your router. |
| to | string | \- | **Deprecated.** Use `href` instead. This prop will be removed in a future major version. |
| className | string | \- | Additional CSS classes |
| children | ReactNode | \- | Link content |

### [Variants](#variants)

| Variant | Description | Use Case |
| --- | --- | --- |
| inline | Primary color with underline | Default for inline text links |
| current | Inherits parent text color with underline | Links within colored contexts (alerts, errors) |
| plain | Primary color without underline | Navigation links, menus, footers |

### [Link.ExternalIcon](#linkexternalicon)

SVG icon component to indicate external links. Accepts all SVG element attributes.

```
<Link href="https://example.com" target="_blank" rel="noopener noreferrer">
  External Site <Link.ExternalIcon />
</Link>
```

## [Design Guidelines](#design-guidelines)

### [When to Use Each Variant](#when-to-use-each-variant)

-   **inline**: Default choice for links within body text
    
-   **current**: Links inside alerts, banners, or other colored containers
    
-   **plain**: Navigation menus, footers, or where underlines are distracting
    

### [External Link Indicators](#external-link-indicators)

-   Always use `Link.ExternalIcon` for links that open in new tabs
-   Set `target="_blank"` and `rel="noopener noreferrer"` for security
    
-   The icon provides a visual cue that users will leave the current site
    

### [Framework Integration](#framework-integration)

-   Configure a `LinkProvider` at your app root to integrate with your client-side router
    
-   Your wrapper receives `href` and maps it to your router’s navigation prop (e.g. React Router’s `to`)
    
-   The wrapper should handle external URLs by rendering a plain `&lt;a&gt;` instead of routing them
    
-   Use the `render` prop as an escape hatch for exceptional cases that need direct control over the rendered element
    
-   The `to` prop is deprecated — use `href` for all link destinations
    

### [Accessibility](#accessibility)

-   Links are keyboard focusable by default
-   The external icon has `aria-hidden="true"` - add descriptive text for screen readers
    
-   Ensure sufficient color contrast for all variants
-   Use descriptive link text (avoid “click here”)