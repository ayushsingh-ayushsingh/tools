# Button

Displays a button or a component that looks like a button.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/button/button.tsx)

---

```
import { Button } from "@cloudflare/kumo";
import { PlusIcon } from "@phosphor-icons/react";

export function ButtonBasicDemo() {
  return (
    <div className="flex flex-wrap items-center gap-2">
      <Button variant="secondary">Button</Button>
      <Button
        variant="secondary"
        shape="square"
        icon={PlusIcon}
        aria-label="Add"
      />
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Button } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Button } from "@cloudflare/kumo/components/button";
```

## [Usage](#usage)

```
import { Button } from "@cloudflare/kumo";

export default function Example() {
  return <Button variant="secondary">Click me</Button>;
}
```

## [Examples](#examples)

### [Variants](#variants)

#### [Primary](#primary)

```
import { Button } from "@cloudflare/kumo";

export function ButtonPrimaryDemo() {
  return <Button variant="primary">Primary</Button>;
}
```

#### [Secondary](#secondary)

```
import { Button } from "@cloudflare/kumo";

export function ButtonSecondaryDemo() {
  return <Button variant="secondary">Secondary</Button>;
}
```

#### [Ghost](#ghost)

```
import { Button } from "@cloudflare/kumo";

export function ButtonGhostDemo() {
  return <Button variant="ghost">Ghost</Button>;
}
```

#### [Destructive](#destructive)

```
import { Button } from "@cloudflare/kumo";

export function ButtonDestructiveDemo() {
  return <Button variant="destructive">Destructive</Button>;
}
```

#### [Outline](#outline)

```
import { Button } from "@cloudflare/kumo";

export function ButtonOutlineDemo() {
  return <Button variant="outline">Outline</Button>;
}
```

#### [Secondary Destructive](#secondary-destructive)

```
import { Button } from "@cloudflare/kumo";

export function ButtonSecondaryDestructiveDemo() {
  return <Button variant="secondary-destructive">Secondary Destructive</Button>;
}
```

### [Sizes](#sizes)

```
import { Button } from "@cloudflare/kumo";

export function ButtonSizesDemo() {
  return (
    <div className="flex flex-wrap items-center gap-3">
      <Button size="xs" variant="secondary">
        Extra Small
      </Button>
      <Button size="sm" variant="secondary">
        Small
      </Button>
      <Button size="base" variant="secondary">
        Base
      </Button>
      <Button size="lg" variant="secondary">
        Large
      </Button>
    </div>
  );
}
```

### [With Icon](#with-icon)

```
import { Button } from "@cloudflare/kumo";
import { PlusIcon } from "@phosphor-icons/react";

export function ButtonWithIconDemo() {
  return (
    <Button variant="secondary" icon={PlusIcon}>
      Create Worker
    </Button>
  );
}
```

### [Icon Only](#icon-only)

For icon-only buttons, use `shape="square"` or `shape="circle"` with the `icon` prop. **Always include `aria-label`** for accessibility — without visible text, screen readers need the label to convey the button’s purpose.

```
import { Button } from "@cloudflare/kumo";
import { PlusIcon } from "@phosphor-icons/react";

export function ButtonIconOnlyDemo() {
  return (
    <div className="flex flex-wrap items-center gap-3">
      <Button
        variant="secondary"
        shape="square"
        icon={PlusIcon}
        aria-label="Add item"
      />
      <Button
        variant="secondary"
        shape="circle"
        icon={PlusIcon}
        aria-label="Add item"
      />
    </div>
  );
}
```

### [Loading State](#loading-state)

```
import { Button } from "@cloudflare/kumo";

export function ButtonLoadingDemo() {
  return (
    <Button variant="primary" loading>
      Loading...
    </Button>
  );
}
```

### [Disabled State](#disabled-state)

```
import { Button } from "@cloudflare/kumo";

export function ButtonDisabledDemo() {
  return (
    <Button variant="secondary" disabled>
      Disabled
    </Button>
  );
}
```

### [Title](#title)

Use the `title` prop to wrap the button in a tooltip. This is useful for icon-only buttons, disabled buttons, or whenever additional context helps the user understand the action.

```
import { Button } from "@cloudflare/kumo";
import { PlusIcon } from "@phosphor-icons/react";

/** Demonstrates title tooltips on enabled, icon-only, and disabled buttons. */
export function ButtonTitleDemo() {
  return (
    <div className="flex flex-wrap items-center gap-3">
      <Button variant="secondary" title="Create a new Worker">
        Create Worker
      </Button>
      <Button
        variant="secondary"
        shape="square"
        icon={PlusIcon}
        aria-label="Add item"
        title="Add item"
      />
      <Button
        variant="secondary"
        title="You need edit access to create a Worker"
        disabled
      >
        Create Worker
      </Button>
    </div>
  );
}
```

### [Link as Button](#link-as-button)

Use `LinkButton` when the interaction should navigate somewhere but still look like a button. Use `Button` for in-place actions like submitting, opening, or toggling UI.

```
import { LinkButton } from "@cloudflare/kumo";
import { ArrowSquareOutIcon } from "@phosphor-icons/react";

/** Demonstrates using LinkButton for navigation actions that should look like buttons. */
export function ButtonLinkAsButtonDemo() {
  return (
    <div className="flex flex-wrap items-center gap-3">
      <LinkButton href="/components/link" variant="secondary">
        Read Link docs
      </LinkButton>
      <LinkButton
        href="https://developers.cloudflare.com"
        variant="ghost"
        icon={ArrowSquareOutIcon}
        external
      >
        Cloudflare Docs
      </LinkButton>
    </div>
  );
}
```

### [Link with Tooltip](#link-with-tooltip)

Pass `title` to a `LinkButton` to wrap it in a tooltip, just like `Button`. This surfaces extra context on hover and focus.

```
import { LinkButton } from "@cloudflare/kumo";

/** Demonstrates a title tooltip on an enabled LinkButton. */
export function ButtonLinkTooltipDemo() {
  return (
    <LinkButton
      href="/components/link"
      variant="secondary"
      title="Opens the Link component docs"
    >
      Read Link docs
    </LinkButton>
  );
}
```

### [Disabled Link](#disabled-link)

Set `disabled` on a `LinkButton` to render a non-interactive button styled like the link. Pass `title` to explain why it’s unavailable via a tooltip.

```
import { LinkButton } from "@cloudflare/kumo";

/** Demonstrates the disabled LinkButton, including a title tooltip explaining why. */
export function ButtonDisabledLinkDemo() {
  return (
    <div className="flex flex-wrap items-center gap-3">
      <LinkButton href="/components/link" variant="secondary" disabled>
        Disabled link
      </LinkButton>
      <LinkButton
        href="/components/link"
        variant="secondary"
        disabled
        title="You need edit access to continue"
      >
        Disabled with tooltip
      </LinkButton>
    </div>
  );
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| shape | `"base" | "square" | "circle"` | `"base"` | \- |
| size | `"xs" | "sm" | "base" | "lg"` | `"base"` | \- |
| variant | `"primary" | "secondary" | "ghost" | "destructive" | "secondary-destructive" | "outline"` | `"secondary"` | \- |
| children | `ReactNode` | \- | \- |
| className | `string` | \- | \- |
| icon | `ReactNode` | \- | Icon from \`@phosphor-icons/react\` or a React element. Rendered before children. |
| loading | `boolean` | \- | Shows a loading spinner and disables interaction. |
| title | `string` | \- | \- |
| id | `string` | \- | \- |
| lang | `string` | \- | \- |
| disabled | `boolean` | \- | \- |
| name | `string` | \- | \- |
| type | `"submit" | "reset" | "button"` | \- | \- |
| value | `string | string[] | number` | \- | \- |