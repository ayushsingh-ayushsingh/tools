# Select

Displays a list of options for the user to pick from—triggered by a button.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/select/select.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/select)

---

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Basic Select with visible label - the recommended pattern. */
export function SelectBasicDemo() {
  const [value, setValue] = useState("apple");

  return (
    <Select
      label="Favorite Fruit"
      className="w-[200px]"
      value={value}
      onValueChange={(v) => setValue(v ?? "apple")}
      items={{ apple: "Apple", banana: "Banana", cherry: "Cherry" }}
    />
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Select } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Select } from "@cloudflare/kumo/components/select";
```

## [Usage](#usage)

```
import { Select } from "@cloudflare/kumo";

export default function Example() {
  const [value, setValue] = useState("apple");

  return (
    <Select
      label="Favorite Fruit"
      value={value}
      onValueChange={(v) => setValue(v ?? "apple")}
      items={{ apple: "Apple", banana: "Banana", cherry: "Cherry" }}
    />
  );
}
```

## [Examples](#examples)

### [Basic](#basic)

A select with a visible label. When you provide the `label` prop, the select automatically renders inside a Field wrapper with the label displayed above it.

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Basic Select with visible label - the recommended pattern. */
export function SelectBasicDemo() {
  const [value, setValue] = useState("apple");

  return (
    <Select
      label="Favorite Fruit"
      className="w-[200px]"
      value={value}
      onValueChange={(v) => setValue(v ?? "apple")}
      items={{ apple: "Apple", banana: "Banana", cherry: "Cherry" }}
    />
  );
}
```

### [Sizes](#sizes)

Use the `size` prop to match Input sizing (xs, sm, base, lg).

```
import { Select } from "@cloudflare/kumo";

/** Select trigger sizes (xs/sm/base/lg) matching Input and Combobox. */
export function SelectSizesDemo() {
  return (
    <div className="grid gap-4">
      <div className="flex items-center gap-3">
        <span className="w-10 text-sm text-kumo-subtle">xs</span>
        <Select
          aria-label="Select size xs"
          size="xs"
          className="w-[200px]"
          placeholder="Choose..."
          items={{ a: "Option A", b: "Option B" }}
        />
      </div>
      <div className="flex items-center gap-3">
        <span className="w-10 text-sm text-kumo-subtle">sm</span>
        <Select
          aria-label="Select size sm"
          size="sm"
          className="w-[200px]"
          placeholder="Choose..."
          items={{ a: "Option A", b: "Option B" }}
        />
      </div>
      <div className="flex items-center gap-3">
        <span className="w-10 text-sm text-kumo-subtle">base</span>
        <Select
          aria-label="Select size base"
          size="base"
          className="w-[200px]"
          placeholder="Choose..."
          items={{ a: "Option A", b: "Option B" }}
        />
      </div>
      <div className="flex items-center gap-3">
        <span className="w-10 text-sm text-kumo-subtle">lg</span>
        <Select
          aria-label="Select size lg"
          size="lg"
          className="w-[200px]"
          placeholder="Choose..."
          items={{ a: "Option A", b: "Option B" }}
        />
      </div>
    </div>
  );
}
```

### [Placement](#placement)

The popup prefers `side="bottom"` and flips automatically when that side runs out of room. Use `side`, `align`, `sideOffset` and `alignOffset` to pin it explicitly — collision handling still applies.

```
import { Select } from "@cloudflare/kumo";

/**
 * Use `side` and `align` to pin the popup. Placement still flips automatically
 * when the chosen side runs out of room.
 */
export function SelectPlacementDemo() {
  return (
    <div className="grid gap-4 sm:grid-cols-2">
      <Select
        label="side=bottom (default)"
        className="w-[200px]"
        defaultValue="earth"
        items={planets}
      />
      <Select
        label="side=top"
        side="top"
        className="w-[200px]"
        defaultValue="earth"
        items={planets}
      />
      <Select
        label="align=end"
        align="end"
        className="w-[200px]"
        defaultValue="earth"
        items={planets}
      />
      <Select
        label="sideOffset=12"
        sideOffset={12}
        className="w-[200px]"
        defaultValue="earth"
        items={planets}
      />
    </div>
  );
}
```

### [Aligned to the selected option](#aligned-to-the-selected-option)

Set `alignItemWithTrigger` to overlay the popup on the trigger so the selected option sits directly on top of it, the way a native `select` behaves. Options before the selection render above the trigger and the rest below, so the popup can extend in both directions. Both selects below have `Mars` selected mid-list — open them to compare. This mode disables itself and falls back to normal anchored placement when there is not enough room.

```
import { Select } from "@cloudflare/kumo";

/**
 * `alignItemWithTrigger` overlays the popup on the trigger so the selected
 * option sits directly on top of it, like a native `<select>`. Options before
 * the selection render above the trigger and the rest below. Open the second
 * select — "Mars" is selected mid-list, so the popup extends in both
 * directions. Falls back to normal anchored placement when space runs out.
 */
export function SelectDynamicPlacementDemo() {
  return (
    <div className="flex flex-wrap items-start gap-8">
      <Select
        label="Anchored (default)"
        description="Opens below the trigger"
        className="w-[200px]"
        defaultValue="mars"
        items={planets}
      />
      <Select
        label="Aligned to selection"
        description="Selected option lands on the trigger"
        alignItemWithTrigger
        className="w-[200px]"
        defaultValue="mars"
        items={planets}
      />
    </div>
  );
}
```

### [Without Visible Label](#without-visible-label)

When a visible label isn’t needed (e.g., in compact UIs or when context is clear), use `aria-label` for accessibility.

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Select without visible label - use aria-label for accessibility. */
export function SelectWithoutLabelDemo() {
  const [value, setValue] = useState("apple");

  return (
    <Select
      aria-label="Select a fruit"
      className="w-[200px]"
      value={value}
      onValueChange={(v) => setValue(v ?? "apple")}
      items={{ apple: "Apple", banana: "Banana", cherry: "Cherry" }}
    />
  );
}
```

### [With Description](#with-description)

Select integrates with the Field wrapper to show description text below the input.

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Select with label and description text. */
export function SelectWithDescriptionDemo() {
  const [value, setValue] = useState<string | null>(null);

  return (
    <Select
      label="Issue Type"
      description="Choose the category that best describes your issue"
      className="w-[280px]"
      value={value}
      onValueChange={(v) => setValue(v as string | null)}
      items={{
        bug: "Bug",
        documentation: "Documentation",
        feature: "Feature",
      }}
    />
  );
}
```

### [With Error](#with-error)

Pass the `error` prop to display a validation error. When an error is present, it replaces the description in the UI.

```
import { Select } from "@cloudflare/kumo";

/** Select with label and validation error. */
export function SelectWithErrorDemo() {
  return (
    <Select
      label="Issue Type"
      error="Please select an issue type"
      className="w-[280px]"
      value={null}
      items={{
        bug: "Bug",
        documentation: "Documentation",
        feature: "Feature",
      }}
    />
  );
}
```

### [Placeholder](#placeholder)

Use the `placeholder` prop to show text when no value is selected. When using `renderValue` to customize the display of selected values, the placeholder is shown instead of calling `renderValue` when the value is `null`.

```
<Select
  placeholder="Select a user..."
  value={user}
  renderValue={(user) => user.name} // Only called when user is not null
/>
```

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Select with placeholder text when no value is selected. */
export function SelectPlaceholderDemo() {
  const [value, setValue] = useState<string | null>(null);

  return (
    <Select
      label="Category"
      placeholder="Choose a category..."
      className="w-[200px]"
      value={value}
      onValueChange={(v) => setValue(v as string | null)}
      items={{
        bug: "Bug",
        documentation: "Documentation",
        feature: "Feature",
      }}
    />
  );
}
```

### [Label with Tooltip](#label-with-tooltip)

Add a tooltip icon next to the label for additional context using `labelTooltip`.

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Select with label tooltip for additional context. */
export function SelectWithTooltipDemo() {
  const [value, setValue] = useState<string | null>(null);

  return (
    <Select
      label="Priority"
      labelTooltip="Higher priority issues are addressed first"
      placeholder="Select priority"
      className="w-[200px]"
      value={value}
      onValueChange={(v) => setValue(v as string | null)}
      items={{
        low: "Low",
        medium: "Medium",
        high: "High",
        critical: "Critical",
      }}
    />
  );
}
```

### [Custom Rendering](#custom-rendering)

Use `renderValue` to customize how the selected value appears in the trigger button. This is useful when working with complex object data structures instead of simple string values.

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Select with custom rendering for complex option display. */
export function SelectCustomRenderingDemo() {
  const [value, setValue] = useState(languages[0]);

  return (
    <Select
      label="Language"
      className="w-[200px]"
      renderValue={(v) => (
        <span>
          {v.emoji} {v.label}
        </span>
      )}
      value={value}
      onValueChange={(v) => setValue(v as (typeof languages)[0])}
    >
      {languages.map((language) => (
        <Select.Option key={language.value} value={language}>
          {language.emoji} {language.label}
        </Select.Option>
      ))}
    </Select>
  );
}
```

The `renderValue` function is only called when a value is selected. Use `placeholder` to define what to show when no value is selected.

Select compares value with items to find which one is selected. For object items, it will compare if the object is the same reference not by value by default. If you want to compare object items by value, you can use `isItemEqualToValue` prop.

```
<Select
  className="w-[200px]"
  placeholder="Select a language..."
  renderValue={(v) => (
    <span>
      {v.emoji} {v.label}
    </span>
  )}
  value={value}
  onValueChange={(v) => setValue(v)}
  // Provides custom comparison logic
  isItemEqualToValue={(item, value) => item.value === value.value}
>
  {languages.map((language) => (
    <Select.Option key={language.value} value={language}>
      {language.emoji} {language.label}
    </Select.Option>
  ))}
</Select>
```

### [Loading](#loading)

A select component with loading state. The loading state is passed to the component via the `loading` prop.

Loading State

Loading From Server (simulated 2s delay)

```
import { Select } from "@cloudflare/kumo";

/** Select in loading state. */
export function SelectLoadingDemo() {
  return <Select aria-label="Loading select" className="w-[200px]" loading />;
}
```

### [Multiple Selection](#multiple-selection)

Enable multiple selection with the `multiple` prop. The value becomes an array of selected items. Use `placeholder` for the empty state and `renderValue` to customize how selections are displayed.

```
<Select
  multiple
  placeholder="Select columns..."
  value={selectedColumns}
  renderValue={(columns) => columns.join(", ")}
  onValueChange={setSelectedColumns}
>
  <Select.Option value="name">Name</Select.Option>
  <Select.Option value="email">Email</Select.Option>
</Select>
```

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Multi-select for choosing multiple values. */
export function SelectMultipleDemo() {
  const [value, setValue] = useState<string[]>(["Name", "Location", "Size"]);

  return (
    <Select
      label="Visible Columns"
      className="w-[250px]"
      multiple
      renderValue={(value) => {
        if (value.length > 3) {
          return (
            <span className="line-clamp-1">
              {value.slice(0, 2).join(", ") + ` and ${value.length - 2} more`}
            </span>
          );
        }
        return <span>{value.join(", ")}</span>;
      }}
      value={value}
      onValueChange={(v) => setValue(v as string[])}
    >
      <Select.Option value="Name">Name</Select.Option>
      <Select.Option value="Location">Location</Select.Option>
      <Select.Option value="Size">Size</Select.Option>
      <Select.Option value="Read">Read</Select.Option>
      <Select.Option value="Write">Write</Select.Option>
      <Select.Option value="CreatedAt">Created At</Select.Option>
    </Select>
  );
}
```

### [More Example](#more-example)

```
import { useState } from "react";
import { Select, Text } from "@cloudflare/kumo";

/** Select with complex object values and custom option rendering. */
export function SelectComplexDemo() {
  const [value, setValue] = useState<(typeof authors)[0] | null>(null);

  return (
    <Select
      label="Author"
      description="Select the primary author for this document"
      placeholder="Select an author"
      className="w-[200px]"
      onValueChange={(v) => setValue(v as (typeof authors)[0] | null)}
      value={value}
      isItemEqualToValue={(item, value) => item?.id === value?.id}
      renderValue={(author) => author.name}
    >
      {authors.map((author) => (
        <Select.Option key={author.id} value={author}>
          <div className="flex w-[300px] items-center justify-between gap-2">
            <Text>{author.name}</Text>
            <Text variant="secondary">{author.title}</Text>
          </div>
        </Select.Option>
      ))}
    </Select>
  );
}
```

### [Disabled Options](#disabled-options)

Options can be disabled with the `disabled` prop. Disabled options are greyed out and cannot be selected.

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Select with disabled options that cannot be selected. */
export function SelectDisabledOptionsDemo() {
  const [value, setValue] = useState<Region | null>(null);

  return (
    <Select
      label="Deployment Region"
      placeholder="Choose a region..."
      className="w-[250px]"
      value={value}
      onValueChange={(v) => setValue(v as Region | null)}
      isItemEqualToValue={(item, val) => item.value === val.value}
    >
      {regions.map((region) => (
        <Select.Option
          key={region.value}
          value={region}
          disabled={region.disabled}
        >
          {region.label}
        </Select.Option>
      ))}
    </Select>
  );
}
```

### [Disabled Items (via items prop)](#disabled-items-via-items-prop)

The `items` object-map prop accepts descriptor objects with `disabled` alongside plain string values.

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Select using the items prop with disabled descriptors. */
export function SelectDisabledItemsDemo() {
  const [value, setValue] = useState<string | null>("free");

  return (
    <Select
      label="Plan"
      className="w-[200px]"
      value={value}
      onValueChange={(v) => setValue(v as string | null)}
      items={{
        free: "Free",
        pro: "Pro",
        business: { label: "Business", disabled: true },
        enterprise: { label: "Enterprise", disabled: true },
      }}
    />
  );
}
```

### [Grouped Options](#grouped-options)

Use `Select.Group`, `Select.GroupLabel`, and `Select.Separator` to organize options under labeled headers with visual dividers.

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Select with grouped options organized under labeled headers. */
export function SelectGroupedDemo() {
  const [value, setValue] = useState<Food | null>(null);

  return (
    <Select
      label="Food"
      placeholder="Pick a food..."
      className="w-[220px]"
      value={value}
      onValueChange={(v) => setValue(v as Food | null)}
      isItemEqualToValue={(item, val) => item.value === val.value}
    >
      <Select.Group>
        <Select.GroupLabel>Fruits</Select.GroupLabel>
        {foods.fruits.map((food) => (
          <Select.Option key={food.value} value={food}>
            {food.label}
          </Select.Option>
        ))}
      </Select.Group>
      <Select.Separator />
      <Select.Group>
        <Select.GroupLabel>Vegetables</Select.GroupLabel>
        {foods.vegetables.map((food) => (
          <Select.Option key={food.value} value={food}>
            {food.label}
          </Select.Option>
        ))}
      </Select.Group>
    </Select>
  );
}
```

### [Groups with Disabled Options](#groups-with-disabled-options)

Combine groups, separators, and disabled options with info tooltips to clearly separate available and unavailable choices.

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Grouped select with disabled options and info tooltips. */
export function SelectGroupedWithDisabledDemo() {
  const [value, setValue] = useState<ServerRegion | null>(null);

  return (
    <Select
      label="Server Region"
      placeholder="Select a region..."
      className="w-[260px]"
      value={value}
      onValueChange={(v) => setValue(v as ServerRegion | null)}
      isItemEqualToValue={(item, val) => item.value === val.value}
    >
      <Select.Group>
        <Select.GroupLabel>Available</Select.GroupLabel>
        {serverRegions.available.map((region) => (
          <Select.Option key={region.value} value={region}>
            {region.label}
          </Select.Option>
        ))}
      </Select.Group>
      <Select.Separator />
      <Select.Group>
        <Select.GroupLabel>Unavailable</Select.GroupLabel>
        {serverRegions.unavailable.map((region) => (
          <Select.Option key={region.value} value={region} disabled>
            {region.label}
          </Select.Option>
        ))}
      </Select.Group>
    </Select>
  );
}
```

### [Long List (Scrolling Test)](#long-list-scrolling-test)

A select component with many options to test popup scrolling behavior. The popup should scroll smoothly without bounce/overscroll issues.

```
import { useState } from "react";
import { Select } from "@cloudflare/kumo";

/** Select with a long list to test popup scrolling behavior. */
export function SelectLongListDemo() {
  const [value, setValue] = useState<LongListItem | null>(null);

  return (
    <Select
      label="Long List Select"
      description="Tests scrolling behavior with many options"
      placeholder="Choose an option..."
      className="w-[220px]"
      value={value}
      onValueChange={(v) => setValue(v as LongListItem | null)}
      isItemEqualToValue={(item, val) => item.value === val.value}
    >
      {longListItems.map((item) => (
        <Select.Option key={item.value} value={item}>
          {item.label}
        </Select.Option>
      ))}
    </Select>
  );
}
```

## [API Reference](#api-reference)

### [Select](#select)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| align | `"start" | "center" | "end"` | \- | How to align the popup relative to the specified side. |
| alignItemWithTrigger | `boolean` | \- | Whether the positioner overlaps the trigger so the selected item's text is aligned with the trigger's value text. This only applies to mouse input and is automatically disabled if there is not enough space. |
| alignOffset | `number | OffsetFunction` | \- | Additional offset along the alignment axis in pixels. Also accepts a function that returns the offset to read the dimensions of the anchor and positioner elements, along with its side and alignment. The function takes a \`data\` object parameter with the following properties: - \`data.anchor\`: the dimensions of the anchor element with properties \`width\` and \`height\`. - \`data.positioner\`: the dimensions of the positioner element with properties \`width\` and \`height\`. - \`data.side\`: which side of the anchor element the positioner is aligned against. - \`data.align\`: how the positioner is aligned relative to the specified side. |
| anchor | `ReactNode` | \- | An element to position the popup against. By default, the popup will be positioned against the trigger. |
| arrowPadding | `number` | \- | Minimum distance to maintain between the arrow and the edges of the popup. Use it to prevent the arrow element from hanging out of the rounded corners of a popup. |
| collisionAvoidance | `CollisionAvoidance` | \- | Determines how to handle collisions when positioning the popup. \`side\` controls overflow on the preferred placement axis (\`top\`/\`bottom\` or \`left\`/\`right\`): - \`'flip'\`: keep the requested side when it fits; otherwise try the opposite side (\`top\` and \`bottom\`, or \`left\` and \`right\`). - \`'shift'\`: never change side; keep the requested side and move the popup within the clipping boundary so it stays visible. - \`'none'\`: do not correct side-axis overflow. \`align\` controls overflow on the alignment axis (\`start\`/\`center\`/\`end\`): - \`'flip'\`: keep side, but swap \`start\` and \`end\` when the requested alignment overflows. - \`'shift'\`: keep side and requested alignment, then nudge the popup along the alignment axis to fit. - \`'none'\`: do not correct alignment-axis overflow. \`fallbackAxisSide\` controls fallback behavior on the perpendicular axis when the preferred axis cannot fit: - \`'start'\`: allow perpendicular fallback and try the logical start side first (\`top\` before \`bottom\`, or \`left\` before \`right\` in LTR). - \`'end'\`: allow perpendicular fallback and try the logical end side first (\`bottom\` before \`top\`, or \`right\` before \`left\` in LTR). - \`'none'\`: do not fallback to the perpendicular axis. When \`side\` is \`'shift'\`, explicitly setting \`align\` only supports \`'shift'\` or \`'none'\`. If \`align\` is omitted, it defaults to \`'flip'\`. |
| collisionBoundary | `Boundary` | \- | An element or a rectangle that delimits the area that the popup is confined to. |
| collisionPadding | `Padding` | \- | Additional space to maintain from the edge of the collision boundary. |
| disableAnchorTracking | `boolean` | \- | Whether to disable the popup from tracking any layout shift of its positioning anchor. |
| positionMethod | `"absolute" | "fixed"` | \- | Determines which CSS \`position\` property to use. |
| side | `"top" | "bottom" | "left" | "right" | "inline-end" | "inline-start"` | \- | Which side of the anchor element to align the popup against. May automatically change to avoid collisions. |
| sideOffset | `number | OffsetFunction` | \- | Distance between the anchor and the popup in pixels. Also accepts a function that returns the distance to read the dimensions of the anchor and positioner elements, along with its side and alignment. The function takes a \`data\` object parameter with the following properties: - \`data.anchor\`: the dimensions of the anchor element with properties \`width\` and \`height\`. - \`data.positioner\`: the dimensions of the positioner element with properties \`width\` and \`height\`. - \`data.side\`: which side of the anchor element the positioner is aligned against. - \`data.align\`: how the positioner is aligned relative to the specified side. |
| sticky | `boolean` | \- | Whether to maintain the popup in the viewport after the anchor element was scrolled out of view. |
| className | `string` | \- | Additional CSS classes merged via \`cn()\`. |
| render | `ReactNode` | \- | Replaces the trigger element while preserving Select behavior. |
| size | `"xs" | "sm" | "base" | "lg"` | `"base"` | Size of the select trigger. Matches Input component sizes. |
| label | `ReactNode` | \- | Label content for the select. When provided, enables the Field wrapper with a visible label above the select. For accessibility without a visible label, use \`aria-label\` instead. |
| hideLabel | `boolean` | \- | \- |
| placeholder | `string` | \- | Placeholder text shown when no value is selected. |
| loading | `boolean` | \- | When \`true\`, shows a skeleton loader in place of the selected value. |
| disabled | `boolean` | \- | Whether the select is disabled. |
| required | `boolean` | \- | Whether the select is required. When \`false\`, shows "(optional)" text. |
| labelTooltip | `ReactNode` | \- | Tooltip content displayed next to the label via an info icon. |
| value | `T` | \- | Currently selected value (controlled mode). |
| children | `ReactNode` | \- | \`Select.Option\` elements to render in the dropdown. |
| description | `ReactNode` | \- | Helper text displayed below the select. |
| error | `string | object` | \- | Error message string or validation error object with \`match\` key. |
| onValueChange | `(value: T) => void` | \- | Callback when selection changes |
| defaultValue | `T` | \- | Initial value for uncontrolled mode |
| renderValue | `(value: T) => ReactNode` | \- | A function that returns a ReactNode to format the selected value in the trigger. Required when using object values. Use \`placeholder\` for the empty state. |
| items | `Record<string, string> | Array<{ label: ReactNode; value: T }>` | \- | Data structure of items rendered in the popup. Accepts a plain object map (\`{ key: "Label" }\`) or an array of \`{ label, value }\` for object/complex values. |
| isItemEqualToValue | `(item: T, value: T) => boolean` | \- | Custom equality function for comparing items. Required when value is an object, since object identity (\`===\`) won't match across renders. |

### [Select.Option](#selectoption)

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Select.Group](#selectgroup)

Groups related options together with an accessible `role="group"`. Use with `Select.GroupLabel` to provide a visible heading.

### [Select.GroupLabel](#selectgrouplabel)

A visible heading for a `Select.Group`. Automatically associated with its parent group for accessibility.

### [Select.Separator](#selectseparator)

A visual divider line between option groups. Renders with `role="separator"`.