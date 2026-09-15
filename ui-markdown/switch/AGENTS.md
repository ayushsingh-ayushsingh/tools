# Switch

A two-state button that can be either on or off.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/switch/switch.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/switch)

---

```
import { useState } from "react";
import { Switch } from "@cloudflare/kumo";

export function SwitchBasicDemo() {
  const [checked, setChecked] = useState(false);
  return (
    <Switch label="Switch" checked={checked} onCheckedChange={setChecked} />
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Switch } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Switch } from "@cloudflare/kumo/components/switch";
```

## [Usage](#usage)

```
import { Switch } from "@cloudflare/kumo";
import { useState } from "react";

export default function Example() {
  const [checked, setChecked] = useState(false);

  return (
    <Switch checked={checked} onCheckedChange={(val) => setChecked(val)} />
  );
}
```

## [Examples](#examples)

### [Off State](#off-state)

```
import { Switch } from "@cloudflare/kumo";

export function SwitchOffDemo() {
  return <Switch label="Switch" checked={false} onCheckedChange={() => {}} />;
}
```

### [On State](#on-state)

```
import { Switch } from "@cloudflare/kumo";

export function SwitchOnDemo() {
  return <Switch label="Switch" checked={true} onCheckedChange={() => {}} />;
}
```

### [Disabled](#disabled)

```
import { Switch } from "@cloudflare/kumo";

export function SwitchDisabledDemo() {
  return <Switch label="Disabled" checked={false} disabled />;
}
```

### [Variants](#variants)

The Switch supports two variants: `default` (blue when on) and `neutral` (monochrome). Both use a squircle shape.

```
import { Switch } from "@cloudflare/kumo";

/** All variants comparison — 2×2 grid showing off/on for default and neutral */
export function SwitchVariantsDemo() {
  return (
    <div className="grid grid-cols-2 gap-x-8 gap-y-4">
      <Switch label="Default off" checked={false} onCheckedChange={() => {}} />
      <Switch label="Default on" checked={true} onCheckedChange={() => {}} />
      <Switch
        label="Neutral off"
        variant="neutral"
        checked={false}
        onCheckedChange={() => {}}
      />
      <Switch
        label="Neutral on"
        variant="neutral"
        checked={true}
        onCheckedChange={() => {}}
      />
    </div>
  );
}
```

### [Neutral Variant](#neutral-variant)

The neutral variant uses monochrome colors and a squircle shape, ideal for subtle, less prominent toggles.

```
import { useState } from "react";
import { Switch } from "@cloudflare/kumo";

/** Neutral variant - monochrome switch for subtle, less prominent toggles */
export function SwitchNeutralDemo() {
  const [checked, setChecked] = useState(false);
  return (
    <Switch
      label="Neutral switch"
      variant="neutral"
      checked={checked}
      onCheckedChange={setChecked}
    />
  );
}
```

### [Neutral States](#neutral-states)

```
import { Switch } from "@cloudflare/kumo";

/** Neutral variant in different states */
export function SwitchNeutralStatesDemo() {
  return (
    <div className="flex flex-col gap-4">
      <Switch
        label="Neutral off"
        variant="neutral"
        checked={false}
        onCheckedChange={() => {}}
      />
      <Switch
        label="Neutral on"
        variant="neutral"
        checked={true}
        onCheckedChange={() => {}}
      />
      <Switch
        label="Neutral disabled"
        variant="neutral"
        checked={false}
        disabled
      />
    </div>
  );
}
```

### [Sizes](#sizes)

Three sizes available: `sm`, `base` (default), and `lg`.

```
import { Switch } from "@cloudflare/kumo";

/** All sizes comparison */
export function SwitchSizesDemo() {
  return (
    <div className="flex flex-col gap-4">
      <Switch
        label="Small"
        size="sm"
        checked={true}
        onCheckedChange={() => {}}
      />
      <Switch
        label="Base (default)"
        size="base"
        checked={true}
        onCheckedChange={() => {}}
      />
      <Switch
        label="Large"
        size="lg"
        checked={true}
        onCheckedChange={() => {}}
      />
    </div>
  );
}
```

### [Custom ID](#custom-id)

When a custom `id` is provided, clicking the label still toggles the switch. The `id` is forwarded to Base UI so the label’s `htmlFor` stays in sync.

```
import { useState } from "react";
import { Switch } from "@cloudflare/kumo";

/** Switch with a custom id prop — clicking the label should still toggle the switch. */
export function SwitchCustomIdDemo() {
  const [checked, setChecked] = useState(false);
  return (
    <Switch
      id="my-custom-switch"
      label="Custom ID"
      checked={checked}
      onCheckedChange={setChecked}
    />
  );
}
```

### [Switch Group](#switch-group)

Group related switches with `Switch.Group`. Provides a shared legend, description, and error message for the group.

```
import { Switch } from "@cloudflare/kumo";

/** Shows a Switch.Group with a legend for grouping related switches */
export function SwitchGroupDemo() {
  return (
    <Switch.Group legend="Notification settings">
      <Switch.Item label="Email notifications" />
      <Switch.Item label="SMS notifications" />
      <Switch.Item label="Push notifications" />
    </Switch.Group>
  );
}
```

### [Visually Hidden Legend](#visually-hidden-legend)

Use `Switch.Legend` with `className="sr-only"` to keep the legend accessible to screen readers while hiding it visually. This is useful when the group is already labeled by a parent `Field` or heading, and showing the legend would create a redundant label.

```
import { Switch } from "@cloudflare/kumo";

/** Shows Switch.Legend with sr-only to visually hide the legend while keeping it accessible, useful when a parent Field already provides a visible label */
export function SwitchLegendSrOnlyDemo() {
  return (
    <Switch.Group>
      <Switch.Legend className="sr-only">Notification settings</Switch.Legend>
      <Switch.Item label="Email notifications" />
      <Switch.Item label="SMS notifications" />
      <Switch.Item label="Push notifications" />
    </Switch.Group>
  );
}
```

### [Custom Legend Styling](#custom-legend-styling)

`Switch.Legend` accepts `className` for full control over legend presentation. Use it instead of the `legend` string prop when you need custom typography, colors, or layout.

```
import { Switch } from "@cloudflare/kumo";

/** Shows Switch.Legend with custom styling for full control over legend presentation */
export function SwitchLegendCustomDemo() {
  return (
    <Switch.Group>
      <Switch.Legend className="text-sm font-normal text-kumo-subtle">
        Notification settings
      </Switch.Legend>
      <Switch.Item label="Email notifications" />
      <Switch.Item label="SMS notifications" />
      <Switch.Item label="Push notifications" />
    </Switch.Group>
  );
}
```

## [API Reference](#api-reference)

### [Switch](#switch)

Individual switch toggle with built-in label.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| variant | `"default" | "neutral"` | `"default"` | Visual variant: "default" (pill, brand color) or "neutral" (squircle, monochrome) |
| label | `ReactNode` | \- | Label content for the switch (Field wrapper is built-in) - can be a string or any React node. Optional when used standalone for visual-only purposes. |
| labelTooltip | `ReactNode` | \- | Tooltip content to display next to the label via an info icon |
| required | `boolean` | \- | Whether the switch is required. When explicitly false, shows "(optional)" text after the label. |
| controlFirst | `boolean` | \- | When true (default), switch appears before label. When false, label appears before switch. |
| size | `"sm" | "base" | "lg"` | `"base"` | \- |
| checked | `boolean` | \- | \- |
| disabled | `boolean` | \- | \- |
| transitioning | `boolean` | \- | \- |
| name | `string` | \- | \- |
| type | `"submit" | "reset" | "button"` | \- | \- |
| value | `string | string[] | number` | \- | \- |
| className | `string` | \- | \- |
| id | `string` | \- | \- |
| lang | `string` | \- | \- |
| title | `string` | \- | \- |
| onClick\* | `(event: React.MouseEvent) => void` | \- | Callback when switch is clicked |

### [Switch.Group](#switchgroup)

Container for multiple switches with legend, description, and error support.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| legend | `string` | \- | Legend text for the group. For more control over legend styling, omit this prop and use \`<Switch.Legend>\` as a child instead. |
| children\* | `ReactNode` | \- | Child Switch.Item components (and optionally a Switch.Legend) |
| error | `string` | \- | Error message for the group (only appears in groups, not single switches) |
| description | `ReactNode` | \- | Helper text for the group |
| disabled | `boolean` | \- | Whether all switches in the group are disabled |
| controlFirst | `boolean` | \- | When true (default), switch appears before label. When false, label appears before switch. |
| className | `string` | \- | Additional CSS classes |

### [Switch.Legend](#switchlegend)

Composable legend sub-component for Switch.Group. Accepts `className` for full styling control (e.g. `className="sr-only"` to visually hide). Use instead of the `legend` string prop when you need custom legend styling.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children\* | `ReactNode` | \- | Legend content |
| className | `string` | \- | Additional CSS classes (e.g. "sr-only" to visually hide the legend) |

### [Switch.Item](#switchitem)

Individual switch within Switch.Group.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.