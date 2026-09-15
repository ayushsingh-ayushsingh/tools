# Collapsible

A composable disclosure component for showing and hiding content.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/collapsible/collapsible.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/collapsible)

---

```
import { Collapsible, Text } from "@cloudflare/kumo";
import { useState } from "react";

/**
 * Hero demo using DefaultTrigger and DefaultPanel for classic Kumo styling.
 */
export function CollapsibleHeroDemo() {
  const [isOpen, setIsOpen] = useState(true);
  return (
    <div className="w-full">
      <Collapsible.Root open={isOpen} onOpenChange={setIsOpen}>
        <Collapsible.DefaultTrigger>What is Kumo?</Collapsible.DefaultTrigger>
        <Collapsible.DefaultPanel>
          <Text>Kumo is Cloudflare's new design system.</Text>
        </Collapsible.DefaultPanel>
      </Collapsible.Root>
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Collapsible } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Collapsible } from "@cloudflare/kumo/components/collapsible";
```

## [Usage](#usage)

Collapsible uses a compound component pattern for full composition control.

### [With Default Styling](#with-default-styling)

Use `DefaultTrigger` and `DefaultPanel` for the classic Kumo style:

```
import { Collapsible } from "@cloudflare/kumo";

export default function Example() {
  const [open, setOpen] = useState(false);

  return (
    <Collapsible.Root open={open} onOpenChange={setOpen}>
      <Collapsible.DefaultTrigger>Show details</Collapsible.DefaultTrigger>
      <Collapsible.DefaultPanel>
        Content with border-left accent styling.
      </Collapsible.DefaultPanel>
    </Collapsible.Root>
  );
}
```

### [Custom Trigger](#custom-trigger)

Use the `render` prop on `Trigger` for full control over the trigger element:

```
<Collapsible.Root open={open} onOpenChange={setOpen}>
  <Collapsible.Trigger render={<Button variant="ghost" />}>
    {open ? "Hide" : "Show"} details
  </Collapsible.Trigger>
  <Collapsible.Panel className="mt-2 p-4 bg-kumo-tint rounded-lg">
    Custom styled panel content.
  </Collapsible.Panel>
</Collapsible.Root>
```

## [Examples](#examples)

### [Basic](#basic)

```
import { Collapsible, Text } from "@cloudflare/kumo";
import { useState } from "react";

/**
 * Basic usage with default styling components.
 */
export function CollapsibleBasicDemo() {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div className="w-full">
      <Collapsible.Root open={isOpen} onOpenChange={setIsOpen}>
        <Collapsible.DefaultTrigger>What is Kumo?</Collapsible.DefaultTrigger>
        <Collapsible.DefaultPanel>
          <Text>Kumo is Cloudflare's new design system.</Text>
        </Collapsible.DefaultPanel>
      </Collapsible.Root>
    </div>
  );
}
```

### [Multiple Items](#multiple-items)

```
import { Collapsible, Text } from "@cloudflare/kumo";
import { useState } from "react";

/**
 * Multiple independent collapsibles.
 */
export function CollapsibleMultipleDemo() {
  const [open1, setOpen1] = useState(false);
  const [open2, setOpen2] = useState(false);
  const [open3, setOpen3] = useState(false);

  return (
    <div className="w-full space-y-2">
      <Collapsible.Root open={open1} onOpenChange={setOpen1}>
        <Collapsible.DefaultTrigger>What is Kumo?</Collapsible.DefaultTrigger>
        <Collapsible.DefaultPanel>
          <Text>Kumo is Cloudflare's new design system.</Text>
        </Collapsible.DefaultPanel>
      </Collapsible.Root>
      <Collapsible.Root open={open2} onOpenChange={setOpen2}>
        <Collapsible.DefaultTrigger>
          How do I use it?
        </Collapsible.DefaultTrigger>
        <Collapsible.DefaultPanel>
          <Text>Install the components and import them into your project.</Text>
        </Collapsible.DefaultPanel>
      </Collapsible.Root>
      <Collapsible.Root open={open3} onOpenChange={setOpen3}>
        <Collapsible.DefaultTrigger>
          Is it open source?
        </Collapsible.DefaultTrigger>
        <Collapsible.DefaultPanel>
          <Text>Check the repository for license information.</Text>
        </Collapsible.DefaultPanel>
      </Collapsible.Root>
    </div>
  );
}
```

### [Custom Trigger](#custom-trigger-1)

Use `Collapsible.Trigger` with the `render` prop for full control:

```
import { Button, Collapsible, Text } from "@cloudflare/kumo";
import { useState } from "react";

/**
 * Custom trigger using the render prop for full control.
 */
export function CollapsibleCustomTriggerDemo() {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div className="w-full">
      <Collapsible.Root open={isOpen} onOpenChange={setIsOpen}>
        <Collapsible.Trigger render={<Button variant="secondary" size="sm" />}>
          {isOpen ? "Hide details" : "Show details"}
        </Collapsible.Trigger>
        <Collapsible.Panel className="mt-3 rounded-lg bg-kumo-tint p-4">
          <Text>
            This panel uses custom styling instead of the default border-left
            accent.
          </Text>
        </Collapsible.Panel>
      </Collapsible.Root>
    </div>
  );
}
```

### [Keep Mounted](#keep-mounted)

Use `keepMounted` on `DefaultPanel` (or `Panel`) to preserve internal state — such as form inputs — when the panel is collapsed:

```
import { Collapsible, Input, Text } from "@cloudflare/kumo";
import { useState } from "react";

/**
 * Keep the panel mounted in the DOM when closed to preserve internal state like form inputs.
 */
export function CollapsibleKeepMountedDemo() {
  const [isOpen, setIsOpen] = useState(true);
  return (
    <div className="w-full space-y-4">
      <Collapsible.Root open={isOpen} onOpenChange={setIsOpen}>
        <Collapsible.DefaultTrigger>Edit details</Collapsible.DefaultTrigger>
        <Collapsible.DefaultPanel keepMounted>
          <Text>
            Type something below, then collapse and re-open — your input is
            preserved because the panel stays mounted.
          </Text>
          <Input label="Name" placeholder="Type here…" />
        </Collapsible.DefaultPanel>
      </Collapsible.Root>
    </div>
  );
}
```

### [Form Content](#form-content)

Use `DefaultPanel` with form controls to verify focus rings have enough room inside the animated panel:

```
import { Button, Collapsible, Input } from "@cloudflare/kumo";
import { useState } from "react";

/**
 * Form controls inside DefaultPanel for testing focus ring clipping.
 */
export function CollapsibleFormDemo() {
  const [isOpen, setIsOpen] = useState(true);
  return (
    <div className="w-full">
      <Collapsible.Root open={isOpen} onOpenChange={setIsOpen}>
        <Collapsible.DefaultTrigger>
          Contact settings
        </Collapsible.DefaultTrigger>
        <Collapsible.DefaultPanel>
          <form
            className="flex max-w-sm flex-col gap-4"
            onSubmit={(event) => event.preventDefault()}
          >
            <Input label="Email" placeholder="user@example.com" type="email" />
            <Input label="Team name" placeholder="Design engineering" />
            <Button type="submit">Save settings</Button>
          </form>
        </Collapsible.DefaultPanel>
      </Collapsible.Root>
    </div>
  );
}
```

### [Accordion Pattern](#accordion-pattern)

Control which item is open to create an accordion where only one item can be expanded at a time:

```
import { Collapsible, Text } from "@cloudflare/kumo";
import { useState } from "react";

/**
 * Accordion pattern where only one item can be open at a time.
 */
export function CollapsibleAccordionDemo() {
  const [activeIndex, setActiveIndex] = useState<number | null>(0);

  const items = [
    {
      title: "What is Kumo?",
      content:
        "Kumo is Cloudflare's new design system built on Base UI and Tailwind CSS v4.",
    },
    {
      title: "How do I install it?",
      content:
        "Run `npm install @cloudflare/kumo` and import the components you need.",
    },
    {
      title: "Is it accessible?",
      content:
        "Yes! Kumo is built on Base UI which provides excellent accessibility out of the box.",
    },
  ];

  return (
    <div className="w-full space-y-2">
      {items.map((item, i) => (
        <Collapsible.Root
          key={i}
          open={activeIndex === i}
          onOpenChange={(open) => setActiveIndex(open ? i : null)}
        >
          <Collapsible.DefaultTrigger>{item.title}</Collapsible.DefaultTrigger>
          <Collapsible.DefaultPanel>
            <Text>{item.content}</Text>
          </Collapsible.DefaultPanel>
        </Collapsible.Root>
      ))}
    </div>
  );
}
```

## [Sub-components](#sub-components)

| Component | Description |
| --- | --- |
| `Collapsible.Root` | Manages open state. Pass `open` and `onOpenChange` for controlled mode. |
| `Collapsible.Trigger` | Button that toggles visibility. Use `render` prop for custom elements. |
| `Collapsible.Panel` | Container for collapsible content. |
| `Collapsible.DefaultTrigger` | Pre-styled trigger with text label and animated caret icon. |
| `Collapsible.DefaultPanel` | Pre-styled panel with border-left accent and standard spacing. |

## [API Reference](#api-reference)

### [Collapsible.Root](#collapsibleroot)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `open` | `boolean` | — | Whether the panel is visible (controlled). |
| `defaultOpen` | `boolean` | `false` | Initial open state (uncontrolled). |
| `onOpenChange` | `(open: boolean) => void` | — | Callback when open state changes. |
| `disabled` | `boolean` | `false` | Whether the collapsible is disabled. |

### [Collapsible.Trigger](#collapsibletrigger)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `render` | `ReactElement` | — | Custom element to render as trigger. |
| `className` | `string` | — | Additional CSS classes. |

### [Collapsible.Panel](#collapsiblepanel)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `className` | `string` | — | Additional CSS classes. |
| `keepMounted` | `boolean` | `false` | Whether to keep the panel in the DOM when closed. |

### [Collapsible.DefaultTrigger](#collapsibledefaulttrigger)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `children` | `ReactNode` | — | Label text displayed in the trigger. |
| `className` | `string` | — | Additional CSS classes. |

### [Collapsible.DefaultPanel](#collapsibledefaultpanel)

Accepts all `Collapsible.Panel` props in addition to the ones listed below.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `children` | `ReactNode` | — | Panel content. |
| `className` | `string` | — | Additional CSS classes. |
| `keepMounted` | `boolean` | `false` | Whether to keep the panel in the DOM when closed. |