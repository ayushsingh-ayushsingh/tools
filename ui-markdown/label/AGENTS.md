# Label

A label component for form fields with support for required/optional indicators and tooltips.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/label/label.tsx)

---

```
import { Label } from "@cloudflare/kumo";

export function LabelBasicDemo() {
  return (
    <div className="flex flex-col gap-4">
      <Label>Default Label</Label>
      <Label showOptional>Optional Label</Label>
      <Label tooltip="More information about this field">
        Label with Tooltip
      </Label>
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Label } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Label } from "@cloudflare/kumo/components/label";
```

## [Usage](#usage)

### [With Form Components (Recommended)](#with-form-components-recommended)

Label features are automatically available through form components like `Input`, `Select`, `Checkbox`, and `Switch` via the `required` and `labelTooltip` props.

```
import { Input } from "@cloudflare/kumo";

export default function Example() {
  return (
    <>
      {/* Optional field with "(optional)" text */}
      <Input label="Phone" required={false} placeholder="+1 555-0000" />

      {/* With tooltip */}
      <Input
        label="API Key"
        labelTooltip="Find this in your dashboard settings"
      />
    </>
  );
}
```

### [Standalone Label](#standalone-label)

For custom form layouts, use the `Label` component directly.

```
import { Label } from "@cloudflare/kumo";

export default function Example() {
  return <Label tooltip="This field is mandatory">Username</Label>;
}
```

## [Examples](#examples)

### [Optional Field](#optional-field)

Shows gray “(optional)” text when `required={false}`.

```
import { Input } from "@cloudflare/kumo";

export function LabelOptionalFieldDemo() {
  return (
    <Input label="Phone Number" required={false} placeholder="+1 555-0000" />
  );
}
```

### [With Tooltip](#with-tooltip)

Shows an info icon with a tooltip for additional context.

```
import { Input } from "@cloudflare/kumo";

export function LabelWithTooltipDemo() {
  return (
    <Input
      label="API Key"
      labelTooltip="Find this in your dashboard settings under API > Keys"
      placeholder="sk_live_..."
    />
  );
}
```

### [ReactNode Label Content](#reactnode-label-content)

Labels support ReactNode content for rich formatting.

```
import { Checkbox } from "@cloudflare/kumo";

export function LabelReactNodeDemo() {
  return (
    <Checkbox
      label={
        <span>
          I agree to the <strong>Terms of Service</strong>
        </span>
      }
    />
  );
}
```

### [Form with Mixed Fields](#form-with-mixed-fields)

Real-world example showing required and optional fields together.

```
import { Input, Select } from "@cloudflare/kumo";

export function LabelFormMixedDemo() {
  return (
    <div className="flex max-w-md flex-col gap-4">
      <Input label="Full Name" placeholder="John Doe" />
      <Input
        label="Email"
        labelTooltip="We'll send your receipt here"
        placeholder="john@example.com"
        type="email"
      />
      <Input label="Company" required={false} placeholder="Acme Inc." />
      <Select label="Country" placeholder="Select a country">
        <Select.Option value="us">United States</Select.Option>
        <Select.Option value="uk">United Kingdom</Select.Option>
        <Select.Option value="ca">Canada</Select.Option>
      </Select>
    </div>
  );
}
```

### [Standalone Label](#standalone-label-1)

Use Label directly for custom layouts or non-form contexts.

```
import { Label } from "@cloudflare/kumo";

export function LabelStandaloneDemo() {
  return (
    <div className="flex flex-col gap-3">
      <Label>Default</Label>
      <Label showOptional>Optional</Label>
      <Label tooltip="Important field">With Tooltip</Label>
    </div>
  );
}
```

## [API Reference](#api-reference)

### [Label Props](#label-props)

Props for the standalone Label component:

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | ReactNode | \- | Label content (required) |
| showOptional | boolean | false | Shows gray “(optional)” text (only when required is false) |
| tooltip | ReactNode | \- | Tooltip content shown via info icon |
| className | string | \- | Additional CSS classes |

### [Form Component Label Props](#form-component-label-props)

These props are available on Input, InputArea, Select, Checkbox, Switch, SensitiveInput, and Combobox:

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| label | ReactNode | \- | Label content (enables Field wrapper) |
| required | boolean | \- | When false: shows “(optional)” text. Also sets HTML required attribute. |
| labelTooltip | ReactNode | \- | Tooltip content shown via info icon next to label |

## [Design Guidelines](#design-guidelines)

### [When to Use Optional Indicators](#when-to-use-optional-indicators)

-   Use “(optional)” for optional fields when most fields are required
    
-   Be consistent within a form
-   Default fields (no indicator) are assumed required by users

### [When to Use Tooltips](#when-to-use-tooltips)

-   Provide additional context that doesn’t fit in the label
-   Explain format requirements or validation rules
-   Link to help documentation for complex fields
-   Keep tooltip content concise - 1-2 sentences max

### [Accessibility](#accessibility)

-   Optional indicators are purely visual - use the `required` attribute for validation
    
-   Tooltips are accessible via keyboard focus on the info icon
-   Screen readers will announce tooltip content when focused