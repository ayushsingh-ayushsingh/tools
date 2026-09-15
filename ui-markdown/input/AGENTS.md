# Input

A text input field for user input with built-in label, description, and error support.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/input/input.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/input)

---

```
import { Input } from "@cloudflare/kumo";

export function InputBasicDemo() {
  return (
    <Input
      label="Email"
      placeholder="you@example.com"
      description="We'll never share your email"
    />
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Input } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Input } from "@cloudflare/kumo/components/input";
```

## [Usage](#usage)

### [With Built-in Field (Recommended)](#with-built-in-field-recommended)

Use the `label` prop to enable the built-in Field wrapper with label, description, and error support.

```
import { Input } from "@cloudflare/kumo";

export default function Example() {
  return (
    <Input
      label="Email"
      placeholder="you@example.com"
      description="We'll never share your email"
    />
  );
}
```

### [Bare Input (Custom Layouts)](#bare-input-custom-layouts)

For custom form layouts, use Input without `label`. Must provide `aria-label` or `aria-labelledby` for accessibility.

```
import { Input } from "@cloudflare/kumo";

export default function Example() {
  return <Input placeholder="Search..." aria-label="Search products" />;
}
```

## [Examples](#examples)

### [With Label and Description](#with-label-and-description)

The `label` prop enables the built-in Field wrapper with automatic vertical layout (label above input).

```
import { Input } from "@cloudflare/kumo";

export function InputWithLabelDemo() {
  return (
    <Input
      label="Username"
      placeholder="Choose a username"
      description="3-20 characters, alphanumeric only"
    />
  );
}
```

### [With Error (String)](#with-error-string)

Pass `error` as a string for simple error messages. Error styling is automatically applied when the `error` prop is truthy.

```
import { Input } from "@cloudflare/kumo";

export function InputErrorStringDemo() {
  return (
    <Input
      label="Email"
      placeholder="you@example.com"
      value="invalid-email"
      error="Please enter a valid email address"
    />
  );
}
```

### [With Error (Validation Object)](#with-error-validation-object)

Pass `error` as an object with `message` and `match` for HTML5 validation. Error shows when field validity matches.

```
import { Input } from "@cloudflare/kumo";

export function InputErrorObjectDemo() {
  return (
    <Input
      label="Password"
      type="password"
      value="short"
      error={{
        message: "Password must be at least 8 characters",
        match: "tooShort",
      }}
      minLength={8}
    />
  );
}
```

### [Input Sizes](#input-sizes)

Four sizes available: `xs`, `sm`, `base` (default), `lg`.

```
import { Input } from "@cloudflare/kumo";

export function InputSizesDemo() {
  return (
    <div className="flex flex-col gap-4">
      <Input size="xs" label="Extra Small" placeholder="Extra small input" />
      <Input size="sm" label="Small" placeholder="Small input" />
      <Input label="Base" placeholder="Base input (default)" />
      <Input size="lg" label="Large" placeholder="Large input" />
    </div>
  );
}
```

### [Disabled](#disabled)

```
import { Input } from "@cloudflare/kumo";

export function InputDisabledDemo() {
  return <Input label="Disabled field" placeholder="Cannot edit" disabled />;
}
```

### [Optional Field](#optional-field)

Set `required={false}` to show “(optional)” text after the label.

```
import { Input } from "@cloudflare/kumo";

export function InputOptionalFieldDemo() {
  return (
    <Input
      label="Phone Number"
      required={false}
      placeholder="+1 (555) 000-0000"
    />
  );
}
```

### [With Label Tooltip](#with-label-tooltip)

Use `labelTooltip` to add an info icon with additional context on hover.

```
import { Input } from "@cloudflare/kumo";

export function InputLabelTooltipDemo() {
  return (
    <Input
      label="API Key"
      labelTooltip="Find this in your dashboard under Settings > API Keys"
      placeholder="sk_live_..."
    />
  );
}
```

### [ReactNode Label](#reactnode-label)

The `label` prop accepts ReactNode for rich formatting.

```
import { Input } from "@cloudflare/kumo";

export function InputReactNodeLabelDemo() {
  return (
    <Input
      label={
        <span>
          Email for <strong>billing</strong>
        </span>
      }
      required
      placeholder="billing@company.com"
      type="email"
    />
  );
}
```

### [Controlled with onChange](#controlled-with-onchange)

The standard React `onChange` handler receives the full event object. Use `e.target.value` to get the value.

```
import { useState } from "react";
import { Input } from "@cloudflare/kumo";

/** Controlled input using `onChange` (native React event). */
export function InputControlledOnChangeDemo() {
  const [value, setValue] = useState("");
  return (
    <Input
      label="With onChange"
      placeholder="Type something..."
      description={value ? `Value: ${value}` : "Uses e.target.value"}
      value={value}
      onChange={(e) => setValue(e.target.value)}
    />
  );
}
```

### [Controlled with onValueChange](#controlled-with-onvaluechange)

`onValueChange` is a convenience handler from Base UI that gives you the string value directly — no event unwrapping needed. This is the same pattern used by `Select`, `Combobox`, and `Radio.Group`.

```
import { useState } from "react";
import { Input } from "@cloudflare/kumo";

/** Controlled input using `onValueChange` (Base UI convenience — gives you the string directly). */
export function InputControlledOnValueChangeDemo() {
  const [value, setValue] = useState("");
  return (
    <Input
      label="With onValueChange"
      placeholder="Type something..."
      description={value ? `Value: ${value}` : "Receives the value directly"}
      value={value}
      onValueChange={(v) => setValue(v)}
    />
  );
}
```

### [Bare Input (No Label)](#bare-input-no-label)

Input without `label` renders as a bare input. Must provide `aria-label` for accessibility.

```
import { Input } from "@cloudflare/kumo";

export function InputBareDemo() {
  return <Input placeholder="Search..." aria-label="Search products" />;
}
```

### [Error Without Label](#error-without-label)

Error messages and descriptions render even without a visible `label` — use `aria-label` to keep the input accessible.

```
import { Input } from "@cloudflare/kumo";

/** Input without a visible label, showing error and description via `aria-label`. */
export function InputErrorWithoutLabelDemo() {
  return (
    <div className="flex flex-col gap-4">
      <Input
        aria-label="Hostname"
        placeholder="example.com"
        value="not a host"
        error="Please enter a valid hostname"
      />
      <Input
        aria-label="Path"
        placeholder="/api/v1/users"
        value="missing-slash"
        error={{ message: "Path must start with /", match: true }}
      />
    </div>
  );
}
```

### [Input Types](#input-types)

Supports all HTML input types: `text`, `email`, `password`, `number`, `tel`, `url`, etc.

```
import { Input } from "@cloudflare/kumo";

export function InputTypesDemo() {
  return (
    <div className="flex flex-col gap-4">
      <Input type="email" label="Email" placeholder="you@example.com" />
      <Input type="password" label="Password" placeholder="••••••••" />
      <Input type="number" label="Age" placeholder="18" />
      <Input type="tel" label="Phone" placeholder="+1 (555) 000-0000" />
    </div>
  );
}
```

### [Password Manager Overlays](#password-manager-overlays)

Set `passwordManagerIgnore` on non-credential inputs that password managers might incorrectly classify as login fields.

```
import { Input } from "@cloudflare/kumo";

/** Side-by-side comparison: Keeper shows its icon on the default input but not the ignored one. */
export function InputPasswordManagerIgnoreDemo() {
  return (
    <div className="flex flex-col gap-4">
      <Input
        label="API Key (default)"
        type="password"
        placeholder="sk_live_..."
      />
      <Input
        label="API Key (passwordManagerIgnore)"
        type="password"
        placeholder="sk_live_..."
        passwordManagerIgnore
      />
    </div>
  );
}
```

## [API Reference](#api-reference)

Input accepts all standard HTML input attributes plus the following:

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| label | `ReactNode` | \- | Label content for the input (enables Field wrapper) - can be a string or any React node |
| labelTooltip | `ReactNode` | \- | Tooltip content to display next to the label via an info icon |
| description | `ReactNode` | \- | Helper text displayed below the input |
| error | `string | object` | \- | Error message or validation error object |
| passwordManagerIgnore | `boolean` | \- | Suppress browser extension password manager overlays on non-credential inputs. |
| size | `"xs" | "sm" | "base" | "lg"` | `"base"` | Input size. - \`"xs"\` — Extra small for compact UIs - \`"sm"\` — Small for secondary fields - \`"base"\` — Default size - \`"lg"\` — Large for prominent fields |
| variant | `"default" | "error"` | `"default"` | Visual variant. - \`"default"\` — Standard input - \`"error"\` — Error state for validation failures |

### [Validation Error Types](#validation-error-types)

When using `error` as an object, the `match` property corresponds to HTML5 ValidityState values:

| Match | Description |
| --- | --- |
| valueMissing | Required field is empty |
| typeMismatch | Value doesn’t match type (e.g., invalid email) |
| patternMismatch | Value doesn’t match pattern attribute |
| tooShort | Value shorter than minLength |
| tooLong | Value longer than maxLength |
| rangeUnderflow | Value less than min |
| rangeOverflow | Value greater than max |
| true | Always show error (for server-side validation) |

## [Accessibility](#accessibility)

### [Label Requirement](#label-requirement)

Inputs require an accessible name via one of:

-   `label` prop (recommended)
-   `placeholder` + `aria-label` for bare inputs
-   `aria-labelledby` for custom label association

Missing accessible names trigger console warnings in development.

### [Error Association](#error-association)

Error messages are automatically associated with the input via ARIA attributes for screen reader announcement.