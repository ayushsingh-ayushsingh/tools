# InputArea

A multi-line text input for longer content with built-in label, description, and error support.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/input/input.tsx)

---

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaBasicDemo() {
  return (
    <InputArea
      label="Description"
      placeholder="Enter a description..."
      description="Provide details about your project"
    />
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { InputArea } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { InputArea } from "@cloudflare/kumo/components/input";
```

`Textarea` is also exported as an alias for `InputArea` for discoverability when migrating from other libraries.

## [Usage](#usage)

### [With Built-in Field (Recommended)](#with-built-in-field-recommended)

Use the `label` prop to enable the built-in Field wrapper with label, description, and error support.

```
import { InputArea } from "@cloudflare/kumo";

export default function Example() {
  return (
    <InputArea
      label="Description"
      placeholder="Enter a description..."
      description="Provide details about your project"
    />
  );
}
```

### [Bare InputArea (Custom Layouts)](#bare-inputarea-custom-layouts)

For custom form layouts, use InputArea without `label`. Must provide `aria-label` or `aria-labelledby` for accessibility.

```
import { InputArea } from "@cloudflare/kumo";

export default function Example() {
  return <InputArea placeholder="Add notes..." aria-label="Notes" rows={3} />;
}
```

## [Examples](#examples)

### [With Label](#with-label)

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaWithLabelDemo() {
  return (
    <InputArea
      label="Bio"
      placeholder="Tell us about yourself"
      description="Max 500 characters"
    />
  );
}
```

### [Custom Row Count](#custom-row-count)

Use the `rows` prop to control the initial height.

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaRowsDemo() {
  return (
    <div className="flex flex-col gap-4">
      <InputArea label="2 rows" placeholder="Small area" rows={2} />
      <InputArea label="4 rows (default)" placeholder="Medium area" rows={4} />
      <InputArea label="8 rows" placeholder="Large area" rows={8} />
    </div>
  );
}
```

### [Error State (String)](#error-state-string)

Error styling is automatically applied when the `error` prop is truthy.

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaErrorStringDemo() {
  return (
    <InputArea
      label="Message"
      placeholder="Enter your message"
      value="Hi"
      error="Message must be at least 10 characters"
    />
  );
}
```

### [Error State (Object)](#error-state-object)

Use an error object with `match` for constraint validation.

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaErrorObjectDemo() {
  return (
    <InputArea
      label="Feedback"
      value="Bad"
      error={{
        message: "Feedback must be at least 20 characters",
        match: "tooShort",
      }}
      minLength={20}
    />
  );
}
```

### [Sizes](#sizes)

Four sizes available: `xs`, `sm`, `base` (default), `lg`.

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaSizesDemo() {
  return (
    <div className="flex flex-col gap-4">
      <InputArea
        size="xs"
        label="Extra Small"
        placeholder="Extra small textarea"
      />
      <InputArea size="sm" label="Small" placeholder="Small textarea" />
      <InputArea label="Base" placeholder="Base textarea (default)" />
      <InputArea size="lg" label="Large" placeholder="Large textarea" />
    </div>
  );
}
```

### [Disabled](#disabled)

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaDisabledDemo() {
  return (
    <InputArea label="Disabled field" placeholder="Cannot edit" disabled />
  );
}
```

### [Auto Resize](#auto-resize)

Use `autoResize` to let the textarea grow vertically as users type or paste multi-line content. `minRows` sets the minimum height, and the optional `maxRows` caps growth — content beyond the cap scrolls.

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaAutoResizeDemo() {
  return (
    <InputArea
      label="Configuration value"
      defaultValue={
        "Review the configuration changes.\n\nAdd follow-up notes here.\n\n"
      }
      autoResize
      minRows={2}
      maxRows={8}
      description="Resizes vertically with content size, up to 8 rows"
    />
  );
}
```

### [Bare InputArea](#bare-inputarea)

InputArea without `label` renders as a bare textarea. Must provide `aria-label` for accessibility.

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaBareDemo() {
  return <InputArea placeholder="Add notes..." aria-label="Notes" rows={3} />;
}
```

### [Optional Field](#optional-field)

Set `required={false}` to show “(optional)” text after the label.

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaOptionalFieldDemo() {
  return (
    <InputArea
      label="Additional Notes"
      required={false}
      placeholder="Any additional information..."
    />
  );
}
```

### [Label with Tooltip](#label-with-tooltip)

Use `labelTooltip` to add an info icon with additional context on hover.

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaLabelTooltipDemo() {
  return (
    <InputArea
      label="Worker Script"
      labelTooltip="Enter your Cloudflare Worker script code here"
      placeholder="export default { async fetch(request) { ... } }"
      rows={4}
    />
  );
}
```

### [React Node Label](#react-node-label)

The `label` prop accepts ReactNode for rich formatting.

```
import { InputArea } from "@cloudflare/kumo";

export function InputAreaReactNodeLabelDemo() {
  return (
    <InputArea
      label={
        <span>
          Notes for <strong>review</strong>
        </span>
      }
      required
      placeholder="Add notes for the reviewer..."
      rows={3}
    />
  );
}
```

## [API Reference](#api-reference)

InputArea accepts all standard HTML textarea attributes plus the following:

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| size | `"xs" | "sm" | "base" | "lg"` | `"base"` | Input size. - \`"xs"\` — Extra small for compact UIs - \`"sm"\` — Small for secondary fields - \`"base"\` — Default size - \`"lg"\` — Large for prominent fields |
| variant | `"default" | "error"` | `"default"` | Visual variant of the textarea. |
| label | `ReactNode` | \- | Label content for the textarea (enables Field wrapper) — can be a string or any React node. |
| labelTooltip | `ReactNode` | \- | Tooltip content to display next to the label via an info icon. |
| description | `ReactNode` | \- | Helper text displayed below the textarea. |
| error | `string | { message: ReactNode; match: FieldErrorMatch }` | \- | Error message or validation error object. |
| autoResize | `boolean` | `false` | Automatically resize the textarea based on its content. |
| minRows | `number` | `1` | Minimum number of rows to display when \`autoResize\` is enabled. |
| maxRows | `number` | \- | Maximum number of rows to grow to when \`autoResize\` is enabled; content beyond this scrolls. |
| onValueChange | `(value: string) => void` | \- | Callback fired with the new string value on every change. |

## [Accessibility](#accessibility)

### [Label Requirement](#label-requirement)

InputArea requires an accessible name via one of:

-   `label` prop (recommended)
-   `placeholder` + `aria-label` for bare textareas
-   `aria-labelledby` for custom label association

Missing accessible names trigger console warnings in development.

### [Error Association](#error-association)

Error messages are automatically associated with the textarea via ARIA attributes for screen reader announcement.