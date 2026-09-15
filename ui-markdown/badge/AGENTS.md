# Badge

Displays a small label for status, categorization, or metadata.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/badge/badge.tsx)

---

```
import { Badge } from "@cloudflare/kumo";

export function BadgeSemanticVariantsDemo() {
  return (
    <div className="flex flex-wrap items-center gap-2">
      <Badge variant="primary">Primary</Badge>
      <Badge variant="secondary">Secondary</Badge>
      <Badge variant="error">Error</Badge>
      <Badge variant="success">Success</Badge>
      <Badge variant="warning">Warning</Badge>
      <Badge variant="info">Info</Badge>
      <Badge variant="outline">Outline</Badge>
      <Badge variant="beta">Beta</Badge>
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Badge } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Badge } from "@cloudflare/kumo/components/badge";
```

## [Usage](#usage)

```
import { Badge } from "@cloudflare/kumo";

export default function Example() {
  return <Badge variant="secondary">New</Badge>;
}
```

## [Examples](#examples)

### [Primary Badges](#primary-badges)

```
import { Badge } from "@cloudflare/kumo";

export function BadgeSemanticVariantsDemo() {
  return (
    <div className="flex flex-wrap items-center gap-2">
      <Badge variant="primary">Primary</Badge>
      <Badge variant="secondary">Secondary</Badge>
      <Badge variant="error">Error</Badge>
      <Badge variant="success">Success</Badge>
      <Badge variant="warning">Warning</Badge>
      <Badge variant="info">Info</Badge>
      <Badge variant="outline">Outline</Badge>
      <Badge variant="beta">Beta</Badge>
    </div>
  );
}
```

### [Other color variants](#other-color-variants)

Other color variants for specific products/use cases where the semantic badges aren’t enough to convey intended meaning or status.

```
import { Badge } from "@cloudflare/kumo";

export function BadgeColorVariantsDemo() {
  return (
    <div className="flex flex-wrap items-center gap-2">
      <Badge variant="neutral">Neutral</Badge>
      <Badge variant="red">Red</Badge>
      <Badge variant="green">Green</Badge>
      <Badge variant="orange">Orange</Badge>
      <Badge variant="teal">Teal</Badge>
      <Badge variant="blue">Blue</Badge>
      <Badge variant="purple">Purple</Badge>
    </div>
  );
}
```

### [Dot badges](#dot-badges)

Use `appearance="dot"` for a subtle status indicator with a colored dot. Supported with `success`, `warning`, `error`, and `neutral` variants.

```
import { Badge } from "@cloudflare/kumo";

export function BadgeDotDemo() {
  return (
    <div className="flex flex-wrap items-center gap-2">
      <Badge variant="success" appearance="dot">
        Healthy
      </Badge>
      <Badge variant="warning" appearance="dot">
        Warning
      </Badge>
      <Badge variant="error" appearance="dot">
        Error
      </Badge>
      <Badge variant="neutral" appearance="dot">
        Neutral
      </Badge>
    </div>
  );
}
```

### [In a sentence](#in-a-sentence)

```
import { Badge } from "@cloudflare/kumo";

export function BadgeInSentenceDemo() {
  return (
    <p className="flex items-center gap-2">
      Workers
      <Badge variant="secondary">New</Badge>
    </p>
  );
}
```

### [With an icon](#with-an-icon)

Filled badges accept a Phosphor icon component or React element through `icon`. Dot badges use their status dot and do not accept icons.

```
import { Badge } from "@cloudflare/kumo";
import { CheckCircleIcon } from "@phosphor-icons/react";

export function BadgeIconDemo() {
  return (
    <Badge icon={CheckCircleIcon} variant="success">
      Verified
    </Badge>
  );
}
```

### [Linked badge](#linked-badge)

Wrap a badge in [`Link`](/components/link) to make it navigable. The badge adds a ring when its ancestor link is hovered.

```
import { Badge, Link } from "@cloudflare/kumo";

export function BadgeLinkDemo() {
  return (
    <Link href="/changelog" variant="plain">
      <Badge variant="outline">View changelog</Badge>
    </Link>
  );
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| variant | `"primary" | "secondary" | "error" | "warning" | "success" | "destructive" | "info" | "beta" | "outline" | "red" | "green" | "neutral" | "orange" | "purple" | "teal" | "teal-subtle" | "blue"` | `"primary"` | Color variant of the badge. Recommended semantic variants: - \`"primary"\` — Primary badge - \`"secondary"\` — Secondary badge - \`"error"\` — Error badge - \`"warning"\` — Warning badge - \`"success"\` — Success badge - \`"info"\` — Info badge Additional token variants: - \`"red"\`, \`"orange"\`, \`"green"\`, \`"teal"\`, \`"blue"\`, \`"purple"\`, \`"neutral"\` - \`"teal-subtle"\`, \`"neutral-subtle"\` - \`"inverted"\` - \`"outline"\` — Bordered badge with the base background - \`"beta"\` — Dashed-border badge for beta/experimental features |
| className | `string` | \- | Additional CSS classes merged via \`cn()\`. |
| children | `ReactNode` | \- | Content rendered inside the badge. |
| appearance | `"filled" | "dot"` | `"filled"` | Visual appearance of the badge. - \`"filled"\` — Filled background using the variant color (default) - \`"dot"\` — Outlined badge with a colored circle dot. Only \`success\`, \`warning\`, \`error\`, and \`neutral\` variants show a dot. Dot badges do not accept icons. |
| icon | `ReactNode` | \- | Icon from \`@phosphor-icons/react\` or a React element. Rendered before children. |