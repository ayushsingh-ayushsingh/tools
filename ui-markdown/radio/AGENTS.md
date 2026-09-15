# Radio

A control that allows the user to select one option from a set. Always used within a Radio.Group.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/radio/radio.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/radio-group)

---

```
import { useState } from "react";
import { Radio } from "@cloudflare/kumo";

/** Shows a basic controlled radio group */
export function RadioBasicDemo() {
  const [value, setValue] = useState("email");
  return (
    <Radio.Group
      legend="Notification preference"
      value={value}
      onValueChange={setValue}
    >
      <Radio.Item label="Email" value="email" />
      <Radio.Item label="SMS" value="sms" />
      <Radio.Item label="Push notification" value="push" />
    </Radio.Group>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Radio } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Radio } from "@cloudflare/kumo/components/radio";
```

## [Usage](#usage)

```
import { Radio } from "@cloudflare/kumo";

export default function Example() {
  return (
    <Radio.Group legend="Choose an option" defaultValue="a">
      <Radio.Item label="Option A" value="a" />
      <Radio.Item label="Option B" value="b" />
    </Radio.Group>
  );
}
```

## [Examples](#examples)

### [Default (Vertical)](#default-vertical)

Radio groups display vertically by default. Each radio has a label displayed to its right.

```
import { useState } from "react";
import { Radio } from "@cloudflare/kumo";

/** Shows the default vertical radio group layout */
export function RadioDefaultDemo() {
  const [value, setValue] = useState("personal");
  return (
    <Radio.Group legend="Account type" value={value} onValueChange={setValue}>
      <Radio.Item label="Personal" value="personal" />
      <Radio.Item label="Business" value="business" />
      <Radio.Item label="Enterprise" value="enterprise" />
    </Radio.Group>
  );
}
```

### [Horizontal](#horizontal)

Use `orientation="horizontal"` for inline layouts. Items wrap when there isn’t enough space.

```
import { useState } from "react";
import { Radio } from "@cloudflare/kumo";

/** Shows a horizontal radio group layout */
export function RadioHorizontalDemo() {
  const [value, setValue] = useState("md");
  return (
    <Radio.Group
      legend="Size"
      orientation="horizontal"
      value={value}
      onValueChange={setValue}
    >
      <Radio.Item label="Small" value="sm" />
      <Radio.Item label="Medium" value="md" />
      <Radio.Item label="Large" value="lg" />
    </Radio.Group>
  );
}
```

### [With Description](#with-description)

Add helper text below the radio items using the `description` prop.

```
import { useState } from "react";
import { Radio } from "@cloudflare/kumo";

/** Shows a radio group with helper description text */
export function RadioDescriptionDemo() {
  const [value, setValue] = useState("standard");
  return (
    <Radio.Group
      legend="Shipping method"
      description="Choose how you'd like to receive your order"
      value={value}
      onValueChange={setValue}
    >
      <Radio.Item label="Standard (5-7 days)" value="standard" />
      <Radio.Item label="Express (2-3 days)" value="express" />
      <Radio.Item label="Overnight" value="overnight" />
    </Radio.Group>
  );
}
```

### [Control Position](#control-position)

Use `controlPosition="end"` to place labels before radio buttons.

```
import { Radio } from "@cloudflare/kumo";

/** Shows radio group with labels positioned before the radio control */
export function RadioControlPositionDemo() {
  return (
    <Radio.Group legend="Preferences" controlPosition="end" defaultValue="a">
      <Radio.Item label="Label before radio" value="a" />
      <Radio.Item label="Another option" value="b" />
    </Radio.Group>
  );
}
```

### [Radio Card](#radio-card)

Use `appearance="card"` on the group to display each option as a selectable card. Combine with the `description` prop on each item for richer content.

```
import { useState } from "react";
import { Radio } from "@cloudflare/kumo";

/** Shows radio card appearance with Cloudflare plan options */
export function RadioCardDemo() {
  const [value, setValue] = useState("free");
  return (
    <Radio.Group
      legend="Choose a plan"
      appearance="card"
      value={value}
      onValueChange={setValue}
    >
      <Radio.Item
        label="Free"
        description="For personal or hobby projects that aren't business-critical."
        value="free"
      />
      <Radio.Item
        label="Pro"
        description="For professional websites that aren't business-critical."
        value="pro"
      />
      <Radio.Item
        label="Business"
        description="For small businesses operating online."
        value="business"
      />
      <Radio.Item
        label="Contract"
        description="For mission-critical applications that are core to your business."
        value="contract"
      />
    </Radio.Group>
  );
}
```

### [Radio Card (Control on the Left)](#radio-card-control-on-the-left)

Use `controlPosition="start"` on a card radio group to place the radio control on the left of the label and description.

```
import { useState } from "react";
import { Radio } from "@cloudflare/kumo";

/** Shows radio card appearance with the control positioned on the left via controlPosition="start" */
export function RadioCardControlStartDemo() {
  const [value, setValue] = useState("free");
  return (
    <Radio.Group
      legend="Choose a plan"
      appearance="card"
      controlPosition="start"
      value={value}
      onValueChange={setValue}
    >
      <Radio.Item
        label="Free"
        description="For personal or hobby projects that aren't business-critical."
        value="free"
      />
      <Radio.Item
        label="Pro"
        description="For professional websites that aren't business-critical."
        value="pro"
      />
    </Radio.Group>
  );
}
```

### [Rich Label Content](#rich-label-content)

The `label` prop on `Radio.Item` accepts React nodes, so you can embed icons, badges, or other markup alongside the text.

```
import { useState } from "react";
import { Badge, Radio } from "@cloudflare/kumo";

/** Shows Radio.Item labels with rich ReactNode content (icons, badges, or additional markup) */
export function RadioRichLabelDemo() {
  const [value, setValue] = useState("pro");
  return (
    <Radio.Group
      legend="Choose a plan"
      appearance="card"
      value={value}
      onValueChange={setValue}
    >
      <Radio.Item
        label={
          <span className="flex items-center gap-2">
            Free
            <Badge variant="neutral">$0</Badge>
          </span>
        }
        description="For personal or hobby projects."
        value="free"
      />
      <Radio.Item
        label={
          <span className="flex items-center gap-2">
            Pro
            <Badge variant="primary">Popular</Badge>
          </span>
        }
        description="For professional websites."
        value="pro"
      />
    </Radio.Group>
  );
}
```

### [Radio Card (Horizontal)](#radio-card-horizontal)

Combine `appearance="card"` with `orientation="horizontal"` for a side-by-side card layout.

```
import { useState } from "react";
import { Radio } from "@cloudflare/kumo";

/** Shows radio card appearance in horizontal layout */
export function RadioCardHorizontalDemo() {
  const [value, setValue] = useState("free");
  return (
    <Radio.Group
      legend="Choose a plan"
      appearance="card"
      orientation="horizontal"
      value={value}
      onValueChange={setValue}
    >
      <Radio.Item
        label="Free"
        description="For personal or hobby projects that aren't business-critical."
        value="free"
      />
      <Radio.Item
        label="Pro"
        description="For professional websites that aren't business-critical."
        value="pro"
      />
      <Radio.Item
        label="Business"
        description="For small businesses operating online."
        value="business"
      />
      <Radio.Item
        label="Contract"
        description="For mission-critical applications that are core to your business."
        value="contract"
      />
    </Radio.Group>
  );
}
```

### [With Error](#with-error)

Show validation errors at the group level using the `error` prop.

```
import { Radio } from "@cloudflare/kumo";

/** Shows error state for both default and card radio groups */
export function RadioErrorDemo() {
  return (
    <div className="grid grid-cols-2 gap-6">
      <Radio.Group
        legend="Payment method"
        error="Please select a payment method to continue"
      >
        <Radio.Item label="Credit Card" value="card" variant="error" />
        <Radio.Item label="PayPal" value="paypal" variant="error" />
      </Radio.Group>
      <Radio.Group
        legend="Payment method"
        appearance="card"
        error="Please select a payment method to continue"
      >
        <Radio.Item
          label="Credit Card"
          description="Pay with Visa, Mastercard, American Express, or Elo."
          value="card"
          variant="error"
        />
        <Radio.Item
          label="PayPal"
          description="Pay with your PayPal account."
          value="paypal"
          variant="error"
        />
      </Radio.Group>
    </div>
  );
}
```

### [Disabled](#disabled)

Disable the entire group or individual items.

```
import { Radio } from "@cloudflare/kumo";

/** Shows disabled state for both default and card radio groups */
export function RadioDisabledDemo() {
  return (
    <div className="grid grid-cols-2 gap-6">
      <Radio.Group legend="Disabled group" disabled defaultValue="a">
        <Radio.Item label="Option A" value="a" />
        <Radio.Item label="Option B" value="b" />
      </Radio.Group>
      <Radio.Group legend="Individual disabled" defaultValue="available">
        <Radio.Item label="Available" value="available" />
        <Radio.Item label="Unavailable" value="unavailable" disabled />
      </Radio.Group>
      <Radio.Group
        legend="Disabled card group"
        appearance="card"
        disabled
        defaultValue="a"
      >
        <Radio.Item
          label="Option A"
          description="This option is disabled."
          value="a"
        />
        <Radio.Item
          label="Option B"
          description="This option is disabled."
          value="b"
        />
      </Radio.Group>
      <Radio.Group
        legend="Individual disabled card"
        appearance="card"
        defaultValue="available"
      >
        <Radio.Item
          label="Available"
          description="This option can be selected."
          value="available"
        />
        <Radio.Item
          label="Unavailable"
          description="This option is not available."
          value="unavailable"
          disabled
        />
      </Radio.Group>
    </div>
  );
}
```

### [Visually Hidden Legend](#visually-hidden-legend)

Use `Radio.Legend` with `className="sr-only"` to keep the legend accessible to screen readers while hiding it visually. This is useful when the radio group is already labeled by a parent `Field` or heading, and showing the legend would create a redundant label.

```
import { useState } from "react";
import { Radio } from "@cloudflare/kumo";

/** Shows Radio.Legend with sr-only to visually hide the legend while keeping it accessible, useful when a parent Field already provides a visible label */
export function RadioLegendSrOnlyDemo() {
  const [value, setValue] = useState("all");
  return (
    <Radio.Group defaultValue="all" value={value} onValueChange={setValue}>
      <Radio.Legend className="sr-only">Paths</Radio.Legend>
      <Radio.Item label="Allow all paths" value="all" />
      <Radio.Item label="Restrict to specific paths" value="specific" />
    </Radio.Group>
  );
}
```

### [Custom Legend Styling](#custom-legend-styling)

`Radio.Legend` accepts `className` for full control over legend presentation. Use it instead of the `legend` string prop when you need custom typography, colors, or layout.

```
import { useState } from "react";
import { Radio } from "@cloudflare/kumo";

/** Shows Radio.Legend with custom styling for full control over legend presentation */
export function RadioLegendCustomDemo() {
  const [value, setValue] = useState("email");
  return (
    <Radio.Group value={value} onValueChange={setValue}>
      <Radio.Legend className="text-sm font-normal text-kumo-subtle">
        Notification preference
      </Radio.Legend>
      <Radio.Item label="Email" value="email" />
      <Radio.Item label="SMS" value="sms" />
      <Radio.Item label="Push notification" value="push" />
    </Radio.Group>
  );
}
```

### [Typed Values](#typed-values)

`Radio.Group` and `Radio.Item` support generic types. Pass a type parameter (e.g. `<number>` or an enum) to constrain the type of `value` on both sub-components, and `defaultValue` and `onValueChange` on `Radio.Group`. Defaults to `string` when omitted.

```
enum ThemeType {
  dark = "dark",
  light = "light",
  system = "system",
}

export function RadioTypedValueDemo() {
  const [pageSize, setPageSize] = useState<number>(10);
  const [theme, setTheme] = useState<ThemeType>(ThemeType.system);
  return (
    <div className="grid grid-cols-2 gap-6">
      <Radio.Group<number>
        legend="Items per page"
        value={pageSize}
        onValueChange={setPageSize}
      >
        <Radio.Item<number> label="10" value={10} />
        <Radio.Item<number> label="25" value={25} />
        <Radio.Item<number> label="50" value={50} />
      </Radio.Group>
      <Radio.Group<ThemeType>
        legend="Theme"
        value={theme}
        onValueChange={setTheme}
      >
        <Radio.Item<ThemeType> label="Light" value={ThemeType.light} />
        <Radio.Item<ThemeType> label="Dark" value={ThemeType.dark} />
        <Radio.Item<ThemeType> label="System" value={ThemeType.system} />
      </Radio.Group>
    </div>
  );
}
```

## [API Reference](#api-reference)

### [Radio.Group](#radiogroup)

Container for radio buttons with legend, description, and error support.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| legend | `string` | \- | Legend text for the group (required for accessibility). For more control over legend styling, omit this prop and use \`<Radio.Legend>\` as a child instead. |
| children\* | `ReactNode` | \- | Child Radio.Item components (and optionally a Radio.Legend) |
| orientation | `"vertical" | "horizontal"` | \- | Layout direction of the radio items |
| appearance | `KumoRadioAppearance` | \- | Visual appearance applied to all Radio.Item children. - \`"default"\` — Standard inline radio items - \`"card"\` — Choice card with border, padding, and highlighted selection state Individual items can override this with their own \`appearance\` prop. |
| error | `string` | \- | Error message for the group |
| description | `ReactNode` | \- | Helper text for the group |
| value | `T` | \- | The controlled value of the selected radio item. |
| disabled | `boolean` | \- | Whether all radios in the group are disabled |
| controlPosition | `RadioControlPosition` | \- | Position of radio control relative to label: "start" puts radio before label, "end" puts label before radio. Defaults to "start" for default appearance and "end" for card appearance. |
| name | `string` | \- | Form submission name for the radio group |
| className | `string` | \- | Additional CSS classes |
| defaultValue | `T` | \- | The uncontrolled initial value of the selected radio item. |
| onValueChange | `(value: T, eventDetails: RadioGroupChangeEventDetails) => void` | \- | Callback fired when the selected value changes. The second argument carries native event details about the interaction. |

### [Radio.Legend](#radiolegend)

Composable legend sub-component for Radio.Group. Accepts `className` for full styling control (e.g. `className="sr-only"` to visually hide). Use instead of the `legend` string prop when you need custom legend styling.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children\* | `ReactNode` | \- | Legend content |
| className | `string` | \- | Additional CSS classes (e.g. "sr-only" to visually hide the legend) |

### [Radio.Item](#radioitem)

Individual radio button within Radio.Group.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

## [Accessibility](#accessibility)

### [Semantic HTML](#semantic-html)

Radio.Group uses semantic `<fieldset>` and `<legend>` elements for proper grouping and screen reader announcement.

### [Keyboard Navigation](#keyboard-navigation)

Arrow Up/Down or Arrow Left/Right moves between options. Space selects the focused option. Tab moves focus to and from the radio group.

### [Screen Readers](#screen-readers)

Each radio is announced with its label and selection state. The group legend provides context for all options.