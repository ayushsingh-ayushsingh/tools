# Breadcrumbs

A navigation component that shows the current page&#39;s location within a navigational hierarchy.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/breadcrumbs/breadcrumbs.tsx)

---

```
import { Breadcrumbs } from "@cloudflare/kumo";
import { House } from "@phosphor-icons/react";

export function BreadcrumbsWithIconsDemo() {
  return (
    <Breadcrumbs>
      <Breadcrumbs.Link href="#" icon={<House size={16} />}>
        Home
      </Breadcrumbs.Link>
      <Breadcrumbs.Separator />
      <Breadcrumbs.Link href="#">Projects</Breadcrumbs.Link>
      <Breadcrumbs.Separator />
      <Breadcrumbs.Current>Current Project</Breadcrumbs.Current>
    </Breadcrumbs>
  );
}
```

## [Installation](#installation)

```
import { Breadcrumbs } from "@cloudflare/kumo";
```

## [Usage](#usage)

```
import { Breadcrumbs } from "@cloudflare/kumo";

export function BreadcrumbsDemo() {
  return (
    <Breadcrumbs>
      <Breadcrumbs.Link href="#">Home</Breadcrumbs.Link>
      <Breadcrumbs.Separator />
      <Breadcrumbs.Link href="#">Docs</Breadcrumbs.Link>
      <Breadcrumbs.Separator />
      <Breadcrumbs.Current>Breadcrumbs</Breadcrumbs.Current>
    </Breadcrumbs>
  );
}
```

## [Examples](#examples)

### [Basic](#basic)

```
import { Breadcrumbs } from "@cloudflare/kumo";

export function BreadcrumbsDemo() {
  return (
    <Breadcrumbs>
      <Breadcrumbs.Link href="#">Home</Breadcrumbs.Link>
      <Breadcrumbs.Separator />
      <Breadcrumbs.Link href="#">Docs</Breadcrumbs.Link>
      <Breadcrumbs.Separator />
      <Breadcrumbs.Current>Breadcrumbs</Breadcrumbs.Current>
    </Breadcrumbs>
  );
}
```

### [Loading](#loading)

```
import { Breadcrumbs } from "@cloudflare/kumo";
import { House } from "@phosphor-icons/react";

export function BreadcrumbsLoadingDemo() {
  return (
    <Breadcrumbs>
      <Breadcrumbs.Link href="#" icon={<House size={16} />}>
        Home
      </Breadcrumbs.Link>
      <Breadcrumbs.Separator />
      <Breadcrumbs.Link href="#">Docs</Breadcrumbs.Link>
      <Breadcrumbs.Separator />
      <Breadcrumbs.Current loading></Breadcrumbs.Current>
    </Breadcrumbs>
  );
}
```

### [Root](#root)

```
import { Breadcrumbs } from "@cloudflare/kumo";
import { House } from "@phosphor-icons/react";

export function BreadcrumbsRootDemo() {
  return (
    <Breadcrumbs>
      <Breadcrumbs.Current icon={<House size={16} />}>
        Worker Analytics
      </Breadcrumbs.Current>
    </Breadcrumbs>
  );
}
```

### [Clipboard](#clipboard)

```
import { Breadcrumbs } from "@cloudflare/kumo";

export function BreadcrumbsWithClipboardDemo() {
  return (
    <Breadcrumbs>
      <Breadcrumbs.Link href="#">Home</Breadcrumbs.Link>
      <Breadcrumbs.Separator />
      <Breadcrumbs.Current>Breadcrumbs</Breadcrumbs.Current>
      <Breadcrumbs.Clipboard text="#" />
    </Breadcrumbs>
  );
}
```

## [API Reference](#api-reference)

### [Breadcrumbs](#breadcrumbs)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| size | `"sm" | "base"` | `"base"` | Size of the breadcrumbs. - \`"sm"\` — Compact breadcrumbs for dense UIs - \`"base"\` — Default breadcrumbs size |
| children | `ReactNode` | \- | \- |
| className | `string` | \- | Additional CSS classes merged via \`cn()\`. |

### [Breadcrumbs.Link](#breadcrumbslink)

| Prop | Type | Default |
| --- | --- | --- |
| href\* | `string` | \- |
| icon | `React.ReactNode` | \- |

### [Breadcrumbs.Current](#breadcrumbscurrent)

| Prop | Type | Default |
| --- | --- | --- |
| loading | `boolean` | \- |
| icon | `React.ReactNode` | \- |

### [Breadcrumbs.Separator](#breadcrumbsseparator)

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Breadcrumbs.Clipboard](#breadcrumbsclipboard)

| Prop | Type | Default |
| --- | --- | --- |
| text\* | `string` | \- |