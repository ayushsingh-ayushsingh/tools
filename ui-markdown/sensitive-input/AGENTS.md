# Sensitive Input

A masked input for sensitive values like API keys and passwords. Click to reveal.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/sensitive-input/sensitive-input.tsx)

---

```
import { SensitiveInput } from "@cloudflare/kumo";

export function SensitiveInputDemo() {
  return (
    <div className="w-80">
      <SensitiveInput label="API Key" defaultValue="sk_live_abc123xyz789" />
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { SensitiveInput } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { SensitiveInput } from "@cloudflare/kumo/components/sensitive-input";
```

## [Usage](#usage)

```
import { SensitiveInput } from "@cloudflare/kumo";

export default function Example() {
  return <SensitiveInput label="Secret" defaultValue="my-secret-key" />;
}
```

## [Sizes](#sizes)

SensitiveInput supports multiple sizes to fit different contexts.

```
import { SensitiveInput } from "@cloudflare/kumo";

export function SensitiveInputSizesDemo() {
  const sizes = ["xs", "sm", "base", "lg"] as const;
  return (
    <div className="flex flex-col gap-4">
      {sizes.map((size) => (
        <div key={size} className="flex items-center gap-2">
          <span className="w-12 text-sm text-kumo-subtle">{size}</span>
          <SensitiveInput
            label={`${size} size`}
            size={size}
            defaultValue="secret-api-key-123"
          />
        </div>
      ))}
    </div>
  );
}
```

## [Controlled](#controlled)

Use controlled mode for full control over the input value.

```
import { useState } from "react";
import { SensitiveInput, Button } from "@cloudflare/kumo";

export function SensitiveInputControlledDemo() {
  const [value, setValue] = useState("my-secret-value");

  return (
    <div className="flex w-80 flex-col gap-4">
      <SensitiveInput
        label="Controlled Secret"
        value={value}
        onValueChange={setValue}
      />
      <div className="text-sm text-kumo-subtle">
        Current value: <code className="text-kumo-default">{value}</code>
      </div>
      <div className="flex gap-2">
        <Button
          onClick={() => setValue("new-secret-" + Date.now())}
          variant="primary"
          size="sm"
        >
          Change value
        </Button>
        <Button onClick={() => setValue("")} variant="secondary" size="sm">
          Clear
        </Button>
      </div>
    </div>
  );
}
```

## [States](#states)

Various input states including error, disabled, read-only, and with description.

```
import { SensitiveInput } from "@cloudflare/kumo";

export function SensitiveInputStatesDemo() {
  return (
    <div className="flex w-80 flex-col gap-4">
      <SensitiveInput
        label="Error State"
        variant="error"
        defaultValue="invalid-key"
        error="This API key is not valid"
      />
      <SensitiveInput label="Disabled" defaultValue="cannot-edit" disabled />
      <SensitiveInput
        label="Read-only"
        defaultValue="view-only-secret-key"
        readOnly
      />
      <SensitiveInput
        label="With Description"
        defaultValue="my-secret-value"
        description="Keep this value secure and don't share it"
      />
    </div>
  );
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| alt | `string` | \- | \- |
| autoComplete | `React.HTMLInputAutoCompleteAttribute` | \- | \- |
| checked | `boolean` | \- | \- |
| disabled | `boolean` | \- | \- |
| height | `number | string` | \- | \- |
| list | `string` | \- | \- |
| name | `string` | \- | \- |
| placeholder | `string` | \- | \- |
| readOnly | `boolean` | \- | \- |
| required | `boolean` | \- | \- |
| width | `number | string` | \- | \- |
| className | `string` | \- | \- |
| id | `string` | \- | \- |
| lang | `string` | \- | \- |
| title | `string` | \- | \- |
| children | `ReactNode` | \- | \- |
| value | `string` | \- | Controlled value |
| size | `"xs" | "sm" | "base" | "lg"` | `"base"` | Size of the input. - \`"xs"\` — Extra small for compact UIs - \`"sm"\` — Small for secondary fields - \`"base"\` — Default input size - \`"lg"\` — Large for prominent fields |
| variant | `"default" | "error"` | `"default"` | Style variant of the input. - \`"default"\` — Default input appearance - \`"error"\` — Error state for validation failures |
| label | `ReactNode` | \- | Label content for the input (enables Field wrapper and sets masked state label) - can be a string or any React node |
| labelTooltip | `ReactNode` | \- | Tooltip content to display next to the label via an info icon |
| description | `ReactNode` | \- | Helper text displayed below the input |
| error | `string | object` | \- | Error message or validation error object |