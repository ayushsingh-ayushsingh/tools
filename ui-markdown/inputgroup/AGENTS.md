# InputGroup

Compose inputs with addons, icons, buttons, and text for rich form fields.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/input-group/input-group.tsx)

---

```
import { useRef, useState } from "react";
import { InputGroup, Loader } from "@cloudflare/kumo";
import { CheckCircleIcon } from "@phosphor-icons/react";

export function InputGroupDemo() {
  const [status, setStatus] = useState<"idle" | "loading" | "success">(
    "success",
  );
  const [value, setValue] = useState("kumo");
  const timerRef = useRef<ReturnType<typeof setTimeout>>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const next = e.target.value;

    setValue(next);

    if (timerRef.current) clearTimeout(timerRef.current);

    if (next.length > 0) {
      setStatus("loading");

      timerRef.current = setTimeout(() => setStatus("success"), 1500);
    } else {
      setStatus("idle");
    }
  };

  return (
    <div className="w-full max-w-2xs">
      <InputGroup>
        <InputGroup.Input
          maxLength={20}
          onChange={handleChange}
          value={value}
        />
        <InputGroup.Suffix>.workers.dev</InputGroup.Suffix>
        {status !== "idle" && (
          <InputGroup.Addon align="end">
            {status === "loading" ? (
              <Loader />
            ) : (
              <CheckCircleIcon weight="duotone" className="text-kumo-success" />
            )}
          </InputGroup.Addon>
        )}
      </InputGroup>
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { InputGroup } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { InputGroup } from "@cloudflare/kumo/components/input-group";
```

## [Usage](#usage)

### [With Built-in Field (Recommended)](#with-built-in-field-recommended)

Pass the `label` prop to InputGroup to enable the built-in Field wrapper with label, description, and error support.

```
import { InputGroup } from "@cloudflare/kumo";
import { MagnifyingGlassIcon } from "@phosphor-icons/react";

export default function Example() {
  return (
    <InputGroup label="Search" description="Find pages, components, and more">
      <InputGroup.Addon>
        <MagnifyingGlassIcon />
      </InputGroup.Addon>
      <InputGroup.Input placeholder="Search..." />
    </InputGroup>
  );
}
```

### [Bare InputGroup (Custom Layouts)](#bare-inputgroup-custom-layouts)

For custom form layouts, use InputGroup without `label`. Must provide `aria-label` on `InputGroup.Input` for accessibility.

```
import { InputGroup } from "@cloudflare/kumo";
import { MagnifyingGlassIcon } from "@phosphor-icons/react";

export default function Example() {
  return (
    <InputGroup>
      <InputGroup.Addon>
        <MagnifyingGlassIcon />
      </InputGroup.Addon>
      <InputGroup.Input placeholder="Search..." aria-label="Search" />
    </InputGroup>
  );
}
```

## [Examples](#examples)

### [Icon](#icon)

Use Addon to place an icon at the start of the input as a visual identifier.

```
import { InputGroup } from "@cloudflare/kumo";
import { LinkIcon } from "@phosphor-icons/react";

export function InputGroupIconsDemo() {
  return (
    <InputGroup className="w-full max-w-3xs">
      <InputGroup.Addon>
        <LinkIcon />
      </InputGroup.Addon>
      <InputGroup.Input placeholder="Paste a link..." aria-label="Link" />
    </InputGroup>
  );
}
```

### [Text](#text)

Use Addon to place text prefixes or suffixes alongside the input.

```
import { InputGroup } from "@cloudflare/kumo";

export function InputGroupTextDemo() {
  return (
    <div className="flex flex-col gap-4">
      <InputGroup className="w-full max-w-3xs">
        <InputGroup.Addon>@</InputGroup.Addon>
        <InputGroup.Input placeholder="username" aria-label="Username" />
      </InputGroup>

      <InputGroup className="w-full max-w-3xs">
        <InputGroup.Input placeholder="email" aria-label="Email" />
        <InputGroup.Addon align="end">@example.com</InputGroup.Addon>
      </InputGroup>

      <InputGroup className="w-full max-w-3xs">
        <InputGroup.Addon>/api/</InputGroup.Addon>
        <InputGroup.Input placeholder="endpoint" aria-label="API path" />
        <InputGroup.Addon align="end">.json</InputGroup.Addon>
      </InputGroup>
    </div>
  );
}
```

### [Button](#button)

Place `InputGroup.Button` inside an Addon for actions that operate directly on the input value, such as reveal/hide or clear.

```
import { useState } from "react";
import { InputGroup } from "@cloudflare/kumo";
import { MagnifyingGlassIcon, EyeIcon, EyeSlashIcon, XIcon } from "@phosphor-icons/react";

export function InputGroupButtonsDemo() {
  const [show, setShow] = useState(false);
  const [searchValue, setSearchValue] = useState("search");

  return (
    <div className="flex flex-col gap-4">
      <InputGroup className="w-full max-w-3xs">
        <InputGroup.Input
          type={show ? "text" : "password"}
          defaultValue="password"
          aria-label="Password"
        />
        <InputGroup.Addon align="end">
          <InputGroup.Button
            shape="square"
            className="text-kumo-subtle"
            icon={show ? EyeSlashIcon : EyeIcon}
            aria-label={show ? "Hide password" : "Show password"}
            onClick={() => setShow(!show)}
          />
        </InputGroup.Addon>
      </InputGroup>

      <InputGroup className="w-full max-w-3xs">
        <InputGroup.Addon>
          <MagnifyingGlassIcon />
        </InputGroup.Addon>
        <InputGroup.Input
          value={searchValue}
          placeholder="Search"
          aria-label="Search"
          onChange={(e) => setSearchValue(e.target.value)}
        />
        {searchValue && (
          <InputGroup.Addon align="end" className="pr-1">
            <InputGroup.Button
              shape="square"
              icon={XIcon}
              aria-label="Clear search"
              onClick={() => setSearchValue("")}
            />
          </InputGroup.Addon>
        )}
        <InputGroup.Button variant="secondary" onClick={() => {}}>
          Search
        </InputGroup.Button>
      </InputGroup>
    </div>
  );
}
```

### [Button with Tooltip](#button-with-tooltip)

Pass a `tooltip` prop to `InputGroup.Button` to show a tooltip on hover. When no explicit `aria-label` is provided, the button derives it from a string tooltip value.

```
import { InputGroup } from "@cloudflare/kumo";
import { MagnifyingGlassIcon, QuestionIcon } from "@phosphor-icons/react";

export function InputGroupTooltipButtonDemo() {
  return (
    <InputGroup className="w-full max-w-2xs">
      <InputGroup.Addon>
        <MagnifyingGlassIcon />
      </InputGroup.Addon>
      <InputGroup.Input
        placeholder="Search with query language..."
        aria-label="Search"
      />
      <InputGroup.Addon align="end">
        <InputGroup.Button
          shape="square"
          className="text-kumo-subtle"
          icon={QuestionIcon}
          aria-label="Query language help"
          tooltip="Query language help"
          onClick={() => {}}
        />
      </InputGroup.Addon>
    </InputGroup>
  );
}
```

### [Kbd](#kbd)

Place a keyboard shortcut hint inside an end Addon.

```
import { InputGroup } from "@cloudflare/kumo";
import { MagnifyingGlassIcon } from "@phosphor-icons/react";

export function InputGroupKbdDemo() {
  return (
    <InputGroup className="w-full max-w-3xs">
      <InputGroup.Addon>
        <MagnifyingGlassIcon />
      </InputGroup.Addon>
      <InputGroup.Input placeholder="Search..." aria-label="Search" />
      <InputGroup.Addon align="end">
        <kbd className="border-none! bg-none!">⌘K</kbd>
      </InputGroup.Addon>
    </InputGroup>
  );
}
```

### [Loading](#loading)

Place a Loader inside an end Addon as a status indicator while validating the input value.

```
import { InputGroup, Loader } from "@cloudflare/kumo";

export function InputGroupLoadingDemo() {
  return (
    <InputGroup className="w-full max-w-3xs">
      <InputGroup.Input defaultValue="kumo" aria-label="kumo" />
      <InputGroup.Addon align="end">
        <Loader />
      </InputGroup.Addon>
    </InputGroup>
  );
}
```

### [Inline Suffix](#inline-suffix)

Suffix renders text that flows seamlessly next to the typed value — useful for domain inputs like `.workers.dev`. Pair with a status icon Addon to show validation state.

```
import { InputGroup } from "@cloudflare/kumo";
import { CheckCircleIcon, XCircleIcon } from "@phosphor-icons/react";

export function InputGroupSuffixDemo() {
  return (
    <div className="flex w-full max-w-2xs flex-col gap-4">
      <InputGroup label="Subdomain">
        <InputGroup.Input
          aria-label="Subdomain"
          defaultValue="kumo"
          maxLength={20}
        />
        <InputGroup.Suffix>.workers.dev</InputGroup.Suffix>
        <InputGroup.Addon align="end">
          <CheckCircleIcon weight="duotone" className="text-kumo-success" />
        </InputGroup.Addon>
      </InputGroup>

      <InputGroup
        label="Subdomain"
        error={{ message: "This subdomain is unavailable", match: true }}
      >
        <InputGroup.Input
          aria-label="Subdomain"
          defaultValue="kumo"
          maxLength={20}
        />
        <InputGroup.Suffix>.workers.dev</InputGroup.Suffix>
        <InputGroup.Addon align="end">
          <XCircleIcon weight="duotone" className="text-kumo-danger" />
        </InputGroup.Addon>
      </InputGroup>
    </div>
  );
}
```

### [Sizes](#sizes)

Four sizes: `xs`, `sm`, `base` (default), and `lg`. The size applies to the entire group.

```
import { InputGroup } from "@cloudflare/kumo";
import { MagnifyingGlassIcon, QuestionIcon } from "@phosphor-icons/react";

export function InputGroupSizesDemo() {
  return (
    <div className="flex w-full max-w-3xs flex-col gap-4">
      <InputGroup size="xs" label="Extra Small">
        <InputGroup.Addon>
          <MagnifyingGlassIcon />
        </InputGroup.Addon>
        <InputGroup.Input placeholder="Extra small input" />
        <InputGroup.Addon align="end">
          <InputGroup.Button
            className="text-kumo-subtle"
            icon={QuestionIcon}
            shape="square"
            aria-label="Help"
          />
        </InputGroup.Addon>
      </InputGroup>

      <InputGroup size="sm" label="Small">
        <InputGroup.Addon>
          <MagnifyingGlassIcon />
        </InputGroup.Addon>
        <InputGroup.Input placeholder="Small input" />
        <InputGroup.Addon align="end">
          <InputGroup.Button
            className="text-kumo-subtle"
            icon={QuestionIcon}
            shape="square"
            aria-label="Help"
          />
        </InputGroup.Addon>
      </InputGroup>

      <InputGroup label="Base (default)">
        <InputGroup.Addon>
          <MagnifyingGlassIcon />
        </InputGroup.Addon>
        <InputGroup.Input placeholder="Base input" />
        <InputGroup.Addon align="end">
          <InputGroup.Button
            className="text-kumo-subtle"
            icon={QuestionIcon}
            shape="square"
            aria-label="Help"
          />
        </InputGroup.Addon>
      </InputGroup>

      <InputGroup size="lg" label="Large">
        <InputGroup.Addon>
          <MagnifyingGlassIcon />
        </InputGroup.Addon>
        <InputGroup.Input placeholder="Large input" />
        <InputGroup.Addon align="end">
          <InputGroup.Button
            className="text-kumo-subtle"
            icon={QuestionIcon}
            shape="square"
            aria-label="Help"
          />
        </InputGroup.Addon>
      </InputGroup>
    </div>
  );
}
```

### [States](#states)

Various input states including error, disabled, and with description. Pass `label`, `error`, and `description` props directly to `InputGroup`.

```
import { useState } from "react";
import { InputGroup } from "@cloudflare/kumo";
import { MagnifyingGlassIcon, EyeIcon, EyeSlashIcon } from "@phosphor-icons/react";

export function InputGroupStatesDemo() {
  const [show, setShow] = useState(false);

  return (
    <div className="flex w-full max-w-3xs flex-col gap-4">
      <InputGroup
        label="Error State"
        error={{ message: "Please enter a valid email address", match: true }}
      >
        <InputGroup.Input type="email" defaultValue="invalid-email" />
        <InputGroup.Addon align="end">@example.com</InputGroup.Addon>
      </InputGroup>

      <InputGroup label="Disabled" disabled>
        <InputGroup.Addon>
          <MagnifyingGlassIcon />
        </InputGroup.Addon>
        <InputGroup.Input placeholder="Search..." />
      </InputGroup>

      <InputGroup label="Optional Field" required={false}>
        <InputGroup.Addon>$</InputGroup.Addon>
        <InputGroup.Input placeholder="0.00" />
      </InputGroup>

      <InputGroup
        label="With Description"
        description="Must be at least 8 characters"
        labelTooltip="Your password is stored securely"
      >
        <InputGroup.Input
          type={show ? "text" : "password"}
          placeholder="Password"
        />
        <InputGroup.Addon align="end">
          <InputGroup.Button
            shape="square"
            className="text-kumo-subtle"
            icon={show ? EyeSlashIcon : EyeIcon}
            aria-label={show ? "Hide password" : "Show password"}
            onClick={() => setShow(!show)}
          />
        </InputGroup.Addon>
      </InputGroup>
    </div>
  );
}
```

## [API Reference](#api-reference)

### [`InputGroup`](#inputgroup)

The root container that provides context to all child components. Accepts Field props (`label`, `description`, `error`) and wraps content in a Field when label is provided.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| label | `ReactNode` | \- | The label content — can be a string or any React node. |
| description | `ReactNode` | \- | Helper text displayed below the control (hidden when \`error\` is present). |
| error | `object` | \- | Validation error with a message and a browser \`ValidityState\` match key. |
| required | `boolean` | \- | When explicitly \`false\`, shows gray "(optional)" text after the label. When \`true\` or \`undefined\`, no indicator is shown. |
| labelTooltip | `ReactNode` | \- | Tooltip content displayed next to the label via an info icon. |
| children | `ReactNode` | \- | \- |
| className | `string` | \- | \- |
| id | `string` | \- | \- |
| lang | `string` | \- | \- |
| title | `string` | \- | \- |
| size | `"xs" | "sm" | "base" | "lg"` | `"base"` | \- |
| disabled | `boolean` | \- | \- |

### [`InputGroup.Input`](#inputgroupinput)

The text input element. Inherits `size`, `disabled`, and `error` from InputGroup context. Accepts all standard input attributes except Field-related props which are handled by the parent.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [`InputGroup.Addon`](#inputgroupaddon)

Container for icons, text, or compact buttons positioned at the start or end of the input.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| align | `"start" | "end"` | `"start"` | Position relative to the input. |
| className | `string` | \- | Additional CSS classes. |

### [`InputGroup.Button`](#inputgroupbutton)

Button for secondary actions like toggle, copy, or help. Renders inside an Addon. Pass a `tooltip` prop to show a tooltip on hover.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| tooltip | `ReactNode` | \- | When provided, wraps the button in a Tooltip. Automatically sets aria-label from a string value. |
| tooltipSide | `"top" | "right" | "bottom" | "left"` | `"bottom"` | Preferred side for the tooltip popup. |
| variant | `"primary" | "secondary" | "ghost" | "destructive" | "secondary-destructive" | "outline"` | `"ghost"` | Button visual style. Defaults to ghost. |
| size | `"xs" | "sm" | "base" | "lg"` | `"sm"` | Button size. |

### [`InputGroup.Suffix`](#inputgroupsuffix)

Inline text that flows seamlessly next to the typed value (e.g., `.workers.dev`). The input width adjusts automatically as the user types.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| className | `string` | \- | Additional CSS classes. |

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

InputGroup requires an accessible name via one of:

-   `label` prop on InputGroup (renders a visible label with built-in Field support)
    
-   `aria-label` on InputGroup.Input for inputs without a visible label
    
-   `aria-labelledby` on InputGroup.Input for custom label association
    

Missing accessible names trigger console warnings in development.

### [Group Role](#group-role)

InputGroup automatically renders with `role="group"`, which semantically associates the input with its addons for assistive technologies.