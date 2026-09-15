# Toolbar

Compose explicit toolbar controls into one clean grouped card.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/toolbar/toolbar.tsx)

---

```
import { InputGroup, Toolbar } from "@cloudflare/kumo";
import { FunnelSimpleIcon, GearSixIcon, MagnifyingGlassIcon } from "@phosphor-icons/react";

/** Basic Toolbar with an InputGroup and adjacent action buttons. */
export function ToolbarDemo() {
  return (
    <Toolbar className="w-full max-w-md">
      <Toolbar.InputGroup aria-label="Search DNS records" className="flex-1">
        <InputGroup.Addon>
          <MagnifyingGlassIcon />
        </InputGroup.Addon>
        <InputGroup.Input placeholder="Search DNS records" />
      </Toolbar.InputGroup>
      <Toolbar.Button icon={FunnelSimpleIcon} aria-label="Filter" />
      <Toolbar.Button icon={GearSixIcon} aria-label="Settings" />
    </Toolbar>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Toolbar } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Toolbar } from "@cloudflare/kumo/components/toolbar";
```

## [Usage](#usage)

Use `Toolbar` when multiple controls should read as one compact toolbar or filter card. Use `Toolbar.Button`, `Toolbar.Link`, `Toolbar.Input`, and `Toolbar.InputGroup` directly. Compose Select and Combobox triggers with those toolbar controls through their `render` props.

```
import { InputGroup, Toolbar } from "@cloudflare/kumo";
import { FunnelSimpleIcon, MagnifyingGlassIcon } from "@phosphor-icons/react";

export default function Example() {
  return (
    <Toolbar>
      <Toolbar.InputGroup aria-label="Search DNS records">
        <InputGroup.Addon>
          <MagnifyingGlassIcon />
        </InputGroup.Addon>
        <InputGroup.Input placeholder="Search DNS records" />
      </Toolbar.InputGroup>
      <Toolbar.Button icon={FunnelSimpleIcon} aria-label="Filter" />
    </Toolbar>
  );
}
```

## [Behavior](#behavior)

Toolbar item components intentionally own grouped control presentation:

-   Every `Toolbar.*` control uses the `base` size by default.
-   The Toolbar `size` prop remains available for compatibility but is deprecated; omit it for the base size.
-   `Toolbar.Button` always renders with quiet toolbar button styling.
-   `Toolbar.Link` renders a `LinkButton` with quiet toolbar styling and participates in arrow-key navigation.
-   `Toolbar.InputGroup` passes props directly to `InputGroup` with the resolved toolbar size.
-   Give Select `render={<Toolbar.Button />}` to compose its trigger into the toolbar.
-   Give `Combobox.TriggerInput` `render={<Toolbar.Input />}` for an editable toolbar combobox.
-   Give `Combobox.TriggerValue` `render={<Toolbar.Button />}` for a button-style toolbar combobox.
-   Select and Combobox retain their value behavior, popup portals, filtering, and form inputs while joining toolbar arrow-key navigation.
-   Adjacent toolbar items share borders and only the Toolbar’s outer corners are rounded.
-   A Select or Combobox without a rendered Toolbar control keeps its standalone presentation and does not join the toolbar’s roving focus order.

## [Examples](#examples)

### [Select](#select)

Select keeps its regular root props, including `items`. Its `render` prop replaces the trigger, so rendering `Toolbar.Button` makes that trigger a toolbar item without replacing the Select root.

```
import { Select, Toolbar } from "@cloudflare/kumo";
import { FunnelSimpleIcon, GearSixIcon } from "@phosphor-icons/react";

/** Select composes its trigger with Toolbar.Button. */
export function ToolbarSelectDemo() {
  return (
    <Toolbar>
      <Toolbar.Button icon={FunnelSimpleIcon}>Filter</Toolbar.Button>
      <Select
        aria-label="Sort records"
        defaultValue="name"
        items={{ name: "Name", created: "Created date", status: "Status" }}
        render={<Toolbar.Button />}
      />
      <Toolbar.Button icon={GearSixIcon} aria-label="View settings" />
    </Toolbar>
  );
}
```

### [Combobox](#combobox)

Compose an editable Combobox trigger with `Toolbar.Input`. For a non-editable value trigger, render `Toolbar.Button` from `Combobox.TriggerValue`. Continue to compose the popup from regular `Combobox.*` components. In a horizontal toolbar, place an editable trigger last so left and right arrows can continue to serve both text-cursor and toolbar navigation predictably.

```
import { Combobox, Toolbar } from "@cloudflare/kumo";
import { FunnelSimpleIcon } from "@phosphor-icons/react";

/** Combobox composes its editable trigger with Toolbar.Input. */
export function ToolbarComboboxDemo() {
  return (
    <Toolbar className="w-full max-w-md">
      <Toolbar.Button icon={FunnelSimpleIcon}>Status</Toolbar.Button>
      <Combobox items={toolbarComboboxItems}>
        <Combobox.TriggerInput
          aria-label="Filter status"
          className="flex-1"
          placeholder="Filter status…"
          render={<Toolbar.Input />}
        />
        <Combobox.Content>
          <Combobox.List>
            {(item: string) => (
              <Combobox.Item key={item} value={item}>
                {item}
              </Combobox.Item>
            )}
          </Combobox.List>
          <Combobox.Empty>No matching statuses.</Combobox.Empty>
        </Combobox.Content>
      </Combobox>
    </Toolbar>
  );
}
```

### [Input Shorthand](#input-shorthand)

Use `Toolbar.Input` for simple text inputs that do not need addons.

```
import { Toolbar } from "@cloudflare/kumo";
import { FunnelSimpleIcon, GearSixIcon } from "@phosphor-icons/react";

/** Toolbar can use the simpler Input shorthand. */
export function ToolbarMixedControlsDemo() {
  return (
    <Toolbar className="w-full max-w-md">
      <Toolbar.Input
        aria-label="Search DNS records"
        placeholder="Search DNS records"
        className="flex-1"
      />
      <Toolbar.Button icon={FunnelSimpleIcon} aria-label="Filter" />
      <Toolbar.Button icon={GearSixIcon} aria-label="Settings" />
    </Toolbar>
  );
}
```

### [Input Group](#input-group)

Use `Toolbar.InputGroup` when one toolbar item needs its own inline addon or suffix.

```
import { InputGroup, Toolbar } from "@cloudflare/kumo";

/** Toolbar can compose an InputGroup with adjacent actions. */
export function ToolbarInputGroupDemo() {
  return (
    <Toolbar className="w-full max-w-lg">
      <Toolbar.InputGroup aria-label="Worker subdomain" className="flex-1">
        <InputGroup.Input placeholder="my-worker" />
        <InputGroup.Suffix>.workers.dev</InputGroup.Suffix>
      </Toolbar.InputGroup>
      <Toolbar.Button>Visit</Toolbar.Button>
    </Toolbar>
  );
}
```

### [Deprecated sizing](#deprecated-sizing)

The `size` prop still supports `xs`, `sm`, `base`, and `lg` for compatibility, but it is deprecated and will be removed in a future major release. Omit it to use the default `base` size.

```
import { Toolbar } from "@cloudflare/kumo";

/** @deprecated Toolbar size customization remains for compatibility. */
export function ToolbarSizesDemo() {
  return (
    <div className="grid gap-3">
      {(["xs", "sm", "base", "lg"] as const).map((size) => (
        <div key={size} className="flex items-center gap-3">
          <span className="w-10 text-sm text-kumo-subtle">{size}</span>
          <Toolbar size={size} className="w-fit">
            <Toolbar.Input
              aria-label={`${size} search`}
              placeholder="Search..."
            />
            <Toolbar.Button>Apply</Toolbar.Button>
          </Toolbar>
        </div>
      ))}
    </div>
  );
}
```

### [Button Actions](#button-actions)

Toolbar buttons use quiet styling so grouped actions remain visually quiet and consistent.

```
import { Toolbar } from "@cloudflare/kumo";
import { DownloadSimpleIcon, UploadSimpleIcon } from "@phosphor-icons/react";

/** Toolbar buttons always use quiet toolbar styling. */
export function ToolbarActionsDemo() {
  return (
    <Toolbar>
      <Toolbar.Button icon={UploadSimpleIcon}>Upload</Toolbar.Button>
      <Toolbar.Button icon={DownloadSimpleIcon}>Download</Toolbar.Button>
    </Toolbar>
  );
}
```

### [Links](#links)

Use `Toolbar.Link` for navigation actions. It accepts `LinkButton` props except for `size` and `variant`, which are controlled by the Toolbar.

```
import { Toolbar } from "@cloudflare/kumo";
import { BookOpenIcon, DownloadSimpleIcon } from "@phosphor-icons/react";

/** Toolbar links use LinkButton for navigation with toolbar styling. */
export function ToolbarLinksDemo() {
  return (
    <Toolbar>
      <Toolbar.Link href="/components/button" icon={BookOpenIcon}>
        Button documentation
      </Toolbar.Link>
      <Toolbar.Button icon={DownloadSimpleIcon}>Download</Toolbar.Button>
    </Toolbar>
  );
}
```

### [Accessible Labels](#accessible-labels)

Use `aria-label` or `aria-labelledby` for compact controls without visible labels. A Select trigger and each Combobox trigger still need an accessible name. For editable inputs, toolbar focus moves only when the caret is already at the relevant text boundary; while a popup is open, arrow keys navigate its options instead.

```
import { Toolbar } from "@cloudflare/kumo";
import { MagnifyingGlassIcon } from "@phosphor-icons/react";

/** Toolbar items use aria-label for compact accessible names. */
export function ToolbarLabelsDemo() {
  return (
    <Toolbar className="w-full max-w-lg">
      <Toolbar.Input
        aria-label="Search records"
        className="flex-1"
        placeholder="Search"
      />
      <Toolbar.Button icon={MagnifyingGlassIcon} aria-label="Search" />
    </Toolbar>
  );
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| `children` | `ReactNode` | \- | Toolbar controls rendered as one grouped card. |
| `size` **Deprecated** | `”xs” | “sm” | “base” | “lg"` | `"base”` | Sets every supported item size. Omit this deprecated prop to use the default base size. |
| `className` | `string` | \- | Additional CSS classes merged onto the toolbar root. |

### [Select composition](#select-composition)

Pass `render={<Toolbar.Button />}` to Select. Configure disabled-focus behavior on the rendered toolbar control:

```
<Select
  aria-label="Sort records"
  disabled
  items={{ name: "Name" }}
  render={<Toolbar.Button focusableWhenDisabled={false} />}
/>
```

### [Combobox composition](#combobox-composition)

Pass `render={<Toolbar.Input />}` to `Combobox.TriggerInput`, or render `Toolbar.Button` from `Combobox.TriggerValue`:

```
<Combobox items={items}>
  <Combobox.TriggerInput
    aria-label="Filter records"
    render={<Toolbar.Input />}
  />
  <Combobox.Content>...</Combobox.Content>
</Combobox>
```

Set `focusableWhenDisabled` on the rendered `Toolbar.Button` or `Toolbar.Input` to control whether a disabled trigger remains in the toolbar’s roving focus order.