# Checkbox

A control that allows the user to toggle between checked and not checked. Features built-in label support with automatic horizontal layout.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/checkbox/checkbox.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/checkbox)

---

```
import { useState } from "react";
import { Checkbox } from "@cloudflare/kumo";

export function CheckboxBasicDemo() {
  const [checked, setChecked] = useState(false);
  return (
    <Checkbox
      label="Accept terms and conditions"
      checked={checked}
      onCheckedChange={setChecked}
    />
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Checkbox } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Checkbox } from "@cloudflare/kumo/components/checkbox";
```

## [Usage](#usage)

```
import { Checkbox } from "@cloudflare/kumo";

export default function Example() {
  return <Checkbox label="Accept terms" />;
}
```

## [Examples](#examples)

### [Default](#default)

Checkbox with built-in label. The label automatically displays in a horizontal layout (checkbox before label).

```
import { useState } from "react";
import { Checkbox } from "@cloudflare/kumo";

export function CheckboxDefaultDemo() {
  const [checked, setChecked] = useState(false);
  return (
    <Checkbox
      label="Enable notifications"
      checked={checked}
      onCheckedChange={setChecked}
    />
  );
}
```

### [Checked](#checked)

```
import { useState } from "react";
import { Checkbox } from "@cloudflare/kumo";

export function CheckboxCheckedDemo() {
  const [checked, setChecked] = useState(true);
  return (
    <Checkbox label="I agree" checked={checked} onCheckedChange={setChecked} />
  );
}
```

### [Indeterminate](#indeterminate)

Used for “select all” patterns when some but not all items are selected.

```
import { useState } from "react";
import { Checkbox } from "@cloudflare/kumo";

export function CheckboxIndeterminateDemo() {
  const [indeterminate, setIndeterminate] = useState(true);
  return (
    <Checkbox
      label="Select all"
      indeterminate={indeterminate}
      onCheckedChange={setIndeterminate}
    />
  );
}
```

### [Label First Layout](#label-first-layout)

Use `controlFirst={false}` to place the label before the checkbox.

```
import { useState } from "react";
import { Checkbox } from "@cloudflare/kumo";

export function CheckboxLabelFirstDemo() {
  const [checked, setChecked] = useState(false);
  return (
    <Checkbox
      label="Remember me"
      controlFirst={false}
      checked={checked}
      onCheckedChange={setChecked}
    />
  );
}
```

### [Disabled](#disabled)

```
import { Checkbox } from "@cloudflare/kumo";

export function CheckboxDisabledDemo() {
  return <Checkbox label="Disabled option" disabled />;
}
```

### [Error](#error)

Error variant provides visual styling (red ring). For error messages, use Checkbox.Group.

```
import { Checkbox } from "@cloudflare/kumo";

export function CheckboxErrorDemo() {
  return <Checkbox label="Invalid option" variant="error" />;
}
```

### [Checkbox Group](#checkbox-group)

Group multiple checkboxes with a legend, description, and shared error messages. Uses Checkbox.Group and Checkbox.Item.

```
import { useState } from "react";
import { Checkbox } from "@cloudflare/kumo";

export function CheckboxGroupDemo() {
  const [preferences, setPreferences] = useState<string[]>(["email"]);

  return (
    <Checkbox.Group
      legend="Email preferences"
      description="Choose how you'd like to receive updates"
      value={preferences}
      onValueChange={setPreferences}
    >
      <Checkbox.Item value="email" label="Email notifications" />
      <Checkbox.Item value="sms" label="SMS notifications" />
      <Checkbox.Item value="push" label="Push notifications" />
    </Checkbox.Group>
  );
}
```

### [Checkbox Group with Error](#checkbox-group-with-error)

Show validation errors at the group level. Error replaces description when present.

```
import { Checkbox } from "@cloudflare/kumo";

export function CheckboxGroupErrorDemo() {
  return (
    <Checkbox.Group
      legend="Required preferences"
      error="Please select at least one notification method"
      value={[]}
      onValueChange={() => {}}
    >
      <Checkbox.Item value="email" label="Email" variant="error" />
      <Checkbox.Item value="sms" label="SMS" variant="error" />
    </Checkbox.Group>
  );
}
```

### [Visually Hidden Legend](#visually-hidden-legend)

Use `Checkbox.Legend` with `className="sr-only"` to keep the legend accessible to screen readers while hiding it visually. This is useful when the group is already labeled by a parent `Field` or heading, and showing the legend would create a redundant label.

```
import { useState } from "react";
import { Checkbox } from "@cloudflare/kumo";

/** Shows Checkbox.Legend with sr-only to visually hide the legend while keeping it accessible, useful when a parent Field already provides a visible label */
export function CheckboxLegendSrOnlyDemo() {
  const [preferences, setPreferences] = useState<string[]>(["email"]);
  return (
    <Checkbox.Group value={preferences} onValueChange={setPreferences}>
      <Checkbox.Legend className="sr-only">
        Notification preferences
      </Checkbox.Legend>
      <Checkbox.Item value="email" label="Email notifications" />
      <Checkbox.Item value="sms" label="SMS notifications" />
      <Checkbox.Item value="push" label="Push notifications" />
    </Checkbox.Group>
  );
}
```

### [Custom Legend Styling](#custom-legend-styling)

`Checkbox.Legend` accepts `className` for full control over legend presentation. Use it instead of the `legend` string prop when you need custom typography, colors, or layout.

```
import { useState } from "react";
import { Checkbox } from "@cloudflare/kumo";

/** Shows Checkbox.Legend with custom styling for full control over legend presentation */
export function CheckboxLegendCustomDemo() {
  const [preferences, setPreferences] = useState<string[]>(["email"]);
  return (
    <Checkbox.Group value={preferences} onValueChange={setPreferences}>
      <Checkbox.Legend className="text-sm font-normal text-kumo-subtle">
        Notification preferences
      </Checkbox.Legend>
      <Checkbox.Item value="email" label="Email notifications" />
      <Checkbox.Item value="sms" label="SMS notifications" />
      <Checkbox.Item value="push" label="Push notifications" />
    </Checkbox.Group>
  );
}
```

## [API Reference](#api-reference)

### [Checkbox](#checkbox)

Single checkbox component with built-in label and horizontal layout.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| variant | `"default" | "error"` | `"default"` | Visual variant: "default" or "error" for validation failures (visual only, no error text) |
| label | `ReactNode` | \- | Label content for the checkbox (enables built-in Field wrapper) - can be a string or any React node |
| labelTooltip | `ReactNode` | \- | Tooltip content to display next to the label via an info icon |
| controlFirst | `boolean` | \- | When true (default), checkbox appears before label. When false, label appears before checkbox. |
| checked | `boolean` | \- | Whether the checkbox is checked (controlled) |
| indeterminate | `boolean` | \- | Whether the checkbox is in indeterminate state |
| disabled | `boolean` | \- | Whether the checkbox is disabled |
| name | `string` | \- | Name for form submission |
| required | `boolean` | \- | Whether the field is required |
| className | `string` | \- | Additional class name |

### [Checkbox.Group](#checkboxgroup)

Wrapper for multiple checkboxes with legend, description, and error support.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| legend | `string` | \- | Legend text for the group. For more control over legend styling, omit this prop and use \`<Checkbox.Legend>\` as a child instead. |
| children\* | `ReactNode` | \- | Child Checkbox.Item components (and optionally a Checkbox.Legend) |
| error | `string` | \- | Error message for the group (only appears in groups, not single checkboxes) |
| description | `ReactNode` | \- | Helper text for the group |
| value | `string[]` | \- | Values of checkboxes that should be checked (controlled) |
| allValues | `string[]` | \- | All possible checkbox values (required for parent checkbox pattern) |
| disabled | `boolean` | \- | Whether all checkboxes in the group are disabled |
| controlFirst | `boolean` | \- | When true (default), checkbox appears before label. When false, label appears before checkbox. |
| className | `string` | \- | Additional CSS classes |

### [Checkbox.Legend](#checkboxlegend)

Composable legend sub-component for Checkbox.Group. Accepts `className` for full styling control (e.g. `className="sr-only"` to visually hide). Use instead of the `legend` string prop when you need custom legend styling.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children\* | `ReactNode` | \- | Legend content |
| className | `string` | \- | Additional CSS classes (e.g. "sr-only" to visually hide the legend) |

### [Checkbox.Item](#checkboxitem)

Individual checkbox within Checkbox.Group.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

## [Accessibility](#accessibility)

### [Label Requirement](#label-requirement)

Single checkboxes require a `label` prop or `aria-label` for accessibility. Missing labels trigger console warnings in development.

### [Keyboard Navigation](#keyboard-navigation)

Space toggles the checkbox. Tab moves focus between checkboxes.

### [Screen Readers](#screen-readers)

Checkbox.Group uses semantic `<fieldset>` and `<legend>` elements for proper grouping announcement.