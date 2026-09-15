# Popover

An accessible popup anchored to a trigger element, used for displaying rich content like menus, forms, or additional information.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/popover/popover.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/popover)

---

```
import { Popover, Button } from "@cloudflare/kumo";
import { BellIcon } from "@phosphor-icons/react";

export function PopoverHeroDemo() {
  return (
    <Popover>
      <Popover.Trigger
        render={
          <Button shape="square" icon={BellIcon} aria-label="Notifications" />
        }
      />
      <Popover.Content>
        <Popover.Title>Notifications</Popover.Title>
        <Popover.Description>
          You are all caught up. Good job!
        </Popover.Description>
      </Popover.Content>
    </Popover>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Popover } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Popover } from "@cloudflare/kumo/components/popover";
```

## [Usage](#usage)

```
import { Popover, Button } from "@cloudflare/kumo";

export default function Example() {
  return (
    <Popover>
      <Popover.Trigger render={<Button />}>Open</Popover.Trigger>
      <Popover.Content>
        <Popover.Title>Popover Title</Popover.Title>
        <Popover.Description>Popover content goes here.</Popover.Description>
      </Popover.Content>
    </Popover>
  );
}
```

## [Popover vs Tooltip](#popover-vs-tooltip)

While popovers can be triggered on hover (using `openOnHover`), they serve a different purpose than tooltips. Understanding when to use each is important for accessibility and user experience.

|  | Tooltip | Popover |
| --- | --- | --- |
| Purpose | Short, non-interactive text labels for identification | Rich, interactive content containers |
| Content | Plain text only | Any content: links, buttons, forms, images |
| Trigger | Hover or focus | Click (default) or hover |
| ARIA Role | `role="tooltip"` | `aria-haspopup` |
| Keyboard | Not focusable | Focus moves inside, traps when open |

**Use a Tooltip** when you need to label an icon button or provide a brief explanation. **Use a Popover** when users need to interact with the content inside, such as clicking links, filling out forms, or dismissing with a button.

## [Examples](#examples)

### [Basic Popover](#basic-popover)

```
import { Popover, Button } from "@cloudflare/kumo";

export function PopoverBasicDemo() {
  return (
    <Popover>
      <Popover.Trigger render={<Button />}>Open Popover</Popover.Trigger>
      <Popover.Content>
        <Popover.Title>Popover Title</Popover.Title>
        <Popover.Description>
          This is a basic popover with a title and description.
        </Popover.Description>
      </Popover.Content>
    </Popover>
  );
}
```

### [With Close Button](#with-close-button)

```
import { Popover, Button } from "@cloudflare/kumo";

export function PopoverWithCloseDemo() {
  return (
    <Popover>
      <Popover.Trigger render={<Button />}>Open Settings</Popover.Trigger>
      <Popover.Content>
        <Popover.Title>Settings</Popover.Title>
        <Popover.Description>
          Configure your preferences below.
        </Popover.Description>
        <div className="mt-3">
          <Popover.Close render={<Button variant="secondary" size="sm" />}>
            Close
          </Popover.Close>
        </div>
      </Popover.Content>
    </Popover>
  );
}
```

### [Positioning](#positioning)

Use the `side` prop to control where the popover appears relative to the trigger.

```
import { Popover, Button } from "@cloudflare/kumo";

export function PopoverPositionDemo() {
  return (
    <div className="flex flex-wrap gap-4">
      <Popover>
        <Popover.Trigger render={<Button variant="secondary" />}>
          Bottom
        </Popover.Trigger>
        <Popover.Content side="bottom">
          <Popover.Title>Bottom</Popover.Title>
          <Popover.Description>
            Popover on bottom (default).
          </Popover.Description>
        </Popover.Content>
      </Popover>

      <Popover>
        <Popover.Trigger render={<Button variant="secondary" />}>
          Top
        </Popover.Trigger>
        <Popover.Content side="top">
          <Popover.Title>Top</Popover.Title>
          <Popover.Description>Popover on top.</Popover.Description>
        </Popover.Content>
      </Popover>

      <Popover>
        <Popover.Trigger render={<Button variant="secondary" />}>
          Left
        </Popover.Trigger>
        <Popover.Content side="left">
          <Popover.Title>Left</Popover.Title>
          <Popover.Description>Popover on left.</Popover.Description>
        </Popover.Content>
      </Popover>

      <Popover>
        <Popover.Trigger render={<Button variant="secondary" />}>
          Right
        </Popover.Trigger>
        <Popover.Content side="right">
          <Popover.Title>Right</Popover.Title>
          <Popover.Description>Popover on right.</Popover.Description>
        </Popover.Content>
      </Popover>
    </div>
  );
}
```

### [Custom Content](#custom-content)

Popovers can contain any content, including custom layouts with avatars, buttons, and more.

```
import { Popover, Button } from "@cloudflare/kumo";

export function PopoverCustomContentDemo() {
  return (
    <Popover>
      <Popover.Trigger render={<Button />}>User Profile</Popover.Trigger>
      <Popover.Content className="w-64">
        <div className="flex items-center gap-3">
          <div className="size-10 rounded-full bg-kumo-recessed" />
          <div>
            <Popover.Title>Jane Doe</Popover.Title>
            <p className="text-sm text-kumo-subtle">jane@example.com</p>
          </div>
        </div>
        <div className="mt-3 flex gap-2 border-t border-kumo-hairline pt-3">
          <Button variant="secondary" size="sm" className="flex-1">
            Profile
          </Button>
          <Popover.Close
            render={<Button variant="ghost" size="sm" className="flex-1" />}
          >
            Sign Out
          </Popover.Close>
        </div>
      </Popover.Content>
    </Popover>
  );
}
```

### [Open on Hover](#open-on-hover)

Use `openOnHover` on the trigger to open the popover when the user hovers over it. You can also specify a `delay` in milliseconds before the popover appears.

```
import { Popover, Button } from "@cloudflare/kumo";

export function PopoverOpenOnHoverDemo() {
  return (
    <Popover>
      <Popover.Trigger
        openOnHover
        delay={200}
        render={<Button variant="secondary" />}
      >
        Hover Me
      </Popover.Trigger>
      <Popover.Content>
        <Popover.Title>Hover Triggered</Popover.Title>
        <Popover.Description>
          This popover opens on hover with a 200ms delay. It can still contain
          interactive content like buttons and links.
        </Popover.Description>
        <div className="mt-3">
          <Popover.Close render={<Button variant="secondary" size="sm" />}>
            Got it
          </Popover.Close>
        </div>
      </Popover.Content>
    </Popover>
  );
}
```

### [Virtual Anchor](#virtual-anchor)

Use the `anchor` prop on `Popover.Content` to position the popover against an element other than the trigger, or against a virtual point (e.g., a `DOMRect` from `getBoundingClientRect()`). This is useful when the trigger and the desired anchor are in different component trees.

```
import { useState, useRef } from "react";
import { Popover, Button } from "@cloudflare/kumo";
import { DotsThree } from "@phosphor-icons/react";

/** Popover anchored to a virtual element instead of a trigger. */
export function PopoverVirtualAnchorDemo() {
  const [selectedRow, setSelectedRow] = useState<string | null>(null);
  const [anchorRect, setAnchorRect] = useState<DOMRect | null>(null);
  const rowRefs = useRef<Map<string, HTMLTableRowElement>>(new Map());

  const rows = [
    { id: "1", name: "api-gateway", status: "Active" },
    { id: "2", name: "auth-service", status: "Active" },
    { id: "3", name: "worker-prod", status: "Paused" },
  ];

  const handleEdit = (id: string) => {
    const row = rowRefs.current.get(id);
    if (row) {
      setAnchorRect(row.getBoundingClientRect());
      setSelectedRow(id);
    }
  };

  return (
    <div className="w-full">
      <div className="overflow-hidden rounded-lg border border-kumo-hairline">
        <table className="w-full text-sm">
          <thead className="bg-kumo-elevated">
            <tr>
              <th className="px-4 py-2 text-left font-medium">Name</th>
              <th className="px-4 py-2 text-left font-medium">Status</th>
              <th className="w-12 px-4 py-2"></th>
            </tr>
          </thead>
          <tbody className="divide-y divide-kumo-hairline">
            {rows.map((row) => (
              <tr
                key={row.id}
                ref={(el) => {
                  if (el) rowRefs.current.set(row.id, el);
                }}
                className={
                  selectedRow === row.id ? "bg-kumo-recessed" : "bg-kumo-base"
                }
              >
                <td className="px-4 py-2 font-mono">{row.name}</td>
                <td className="px-4 py-2 text-kumo-subtle">{row.status}</td>
                <td className="px-4 py-2">
                  <Button
                    size="xs"
                    variant="ghost"
                    shape="square"
                    icon={DotsThree}
                    aria-label={`Actions for ${row.name}`}
                    onClick={() => handleEdit(row.id)}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <Popover
        open={!!selectedRow}
        onOpenChange={(open) => !open && setSelectedRow(null)}
      >
        <Popover.Content
          side="left"
          anchor={
            anchorRect ? { getBoundingClientRect: () => anchorRect } : undefined
          }
        >
          <Popover.Title>
            Edit {rows.find((r) => r.id === selectedRow)?.name}
          </Popover.Title>
          <Popover.Description>
            The popover anchors to the selected row, not the icon button.
          </Popover.Description>
          <div className="mt-3">
            <Popover.Close render={<Button size="sm" variant="secondary" />}>
              Close
            </Popover.Close>
          </div>
        </Popover.Content>
      </Popover>
    </div>
  );
}
```

## [API Reference](#api-reference)

### [Popover](#popover)

The root component that manages the popover’s open state.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| side | `"top" | "bottom" | "left" | "right"` | `"bottom"` | Which side of the trigger the popover appears on. - \`"top"\` — Above the trigger - \`"bottom"\` — Below the trigger - \`"left"\` — Left of the trigger - \`"right"\` — Right of the trigger |

### [Popover.Trigger](#popovertrigger)

A button that opens the popover when clicked. Use `render` to render your own element.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Popover.Content](#popovercontent)

The container for popover content. Controls positioning via `side`, `align`, `sideOffset`, and `alignOffset` props. Use the `anchor` prop to position against a custom element or virtual point instead of the trigger. Use `positionMethod="fixed"` when the popover needs to escape stacking contexts, such as when inside sticky headers.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Popover.Title](#popovertitle)

A heading that labels the popover for accessibility.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Popover.Description](#popoverdescription)

A paragraph providing additional context about the popover content.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Popover.Close](#popoverclose)

A button that closes the popover when clicked. Use `render` to render your own element.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.