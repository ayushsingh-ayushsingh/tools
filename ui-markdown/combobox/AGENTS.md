# Combobox

A searchable select component that allows users to filter and select from a list of options.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/combobox/combobox.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/combobox)

---

```
import { useState } from "react";
import { Combobox } from "@cloudflare/kumo";

// Basic demo with TriggerInput
export function ComboboxDemo() {
  const [value, setValue] = useState<string | null>("Apple");

  return (
    <Combobox
      value={value}
      onValueChange={(v) => setValue(v as string | null)}
      items={fruits}
    >
      <Combobox.TriggerInput placeholder="Please select" />
      <Combobox.Content>
        <Combobox.Empty />
        <Combobox.List>
          {(item: string) => (
            <Combobox.Item key={item} value={item}>
              {item}
            </Combobox.Item>
          )}
        </Combobox.List>
      </Combobox.Content>
    </Combobox>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Combobox } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Combobox } from "@cloudflare/kumo/components/combobox";
```

## [Usage](#usage)

```
import { useState } from "react";
import { Combobox } from "@cloudflare/kumo";

const fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"];

export default function Example() {
  const [value, setValue] = useState<string | null>(null);

  return (
    <Combobox value={value} onValueChange={setValue} items={fruits}>
      <Combobox.TriggerInput placeholder="Select a fruit" />
      <Combobox.Content>
        <Combobox.Empty />
        <Combobox.List>
          {(item) => (
            <Combobox.Item key={item} value={item}>
              {item}
            </Combobox.Item>
          )}
        </Combobox.List>
      </Combobox.Content>
    </Combobox>
  );
}
```

## [Examples](#examples)

### [Sizes](#sizes)

The Combobox supports four size variants that match the Input component: `xs`, `sm`, `base` (default), and `lg`.

```
import { useState } from "react";
import { Combobox } from "@cloudflare/kumo";

/** Demonstrates the different size variants: xs, sm, base, and lg. */
export function ComboboxSizesDemo() {
  const [smValue, setSmValue] = useState<string | null>(null);
  const [baseValue, setBaseValue] = useState<string | null>(null);

  return (
    <div className="flex flex-wrap items-center gap-4">
      <Combobox
        size="sm"
        value={smValue}
        onValueChange={(v) => setSmValue(v as string | null)}
        items={fruits.slice(0, 8)}
      >
        <Combobox.TriggerInput placeholder="Small (sm)" />
        <Combobox.Content>
          <Combobox.Empty />
          <Combobox.List>
            {(item: string) => (
              <Combobox.Item key={item} value={item}>
                {item}
              </Combobox.Item>
            )}
          </Combobox.List>
        </Combobox.Content>
      </Combobox>
      <Combobox
        size="base"
        value={baseValue}
        onValueChange={(v) => setBaseValue(v as string | null)}
        items={fruits.slice(0, 8)}
      >
        <Combobox.TriggerInput placeholder="Base (default)" />
        <Combobox.Content>
          <Combobox.Empty />
          <Combobox.List>
            {(item: string) => (
              <Combobox.Item key={item} value={item}>
                {item}
              </Combobox.Item>
            )}
          </Combobox.List>
        </Combobox.Content>
      </Combobox>
    </div>
  );
}
```

Size also applies to `TriggerValue` (searchable inside variant):

```
import { useState } from "react";
import { Combobox } from "@cloudflare/kumo";
import { languages, Language } from "./data/languages";

/** Demonstrates size variants with TriggerValue (searchable inside). */
export function ComboboxSizesSearchableInsideDemo() {
  const [smValue, setSmValue] = useState<Language>(languages[0]);
  const [baseValue, setBaseValue] = useState<Language>(languages[1]);

  return (
    <div className="flex flex-wrap items-center gap-4">
      <Combobox
        size="sm"
        value={smValue}
        onValueChange={(v) => setSmValue(v as Language)}
        items={languages}
      >
        <Combobox.TriggerValue className="w-[160px]" />
        <Combobox.Content>
          <Combobox.Input placeholder="Search" />
          <Combobox.Empty />
          <Combobox.List>
            {(item: Language) => (
              <Combobox.Item key={item.value} value={item}>
                {item.emoji} {item.label}
              </Combobox.Item>
            )}
          </Combobox.List>
        </Combobox.Content>
      </Combobox>
      <Combobox
        size="base"
        value={baseValue}
        onValueChange={(v) => setBaseValue(v as Language)}
        items={languages}
      >
        <Combobox.TriggerValue className="w-[180px]" />
        <Combobox.Content>
          <Combobox.Input placeholder="Search" />
          <Combobox.Empty />
          <Combobox.List>
            {(item: Language) => (
              <Combobox.Item key={item.value} value={item}>
                {item.emoji} {item.label}
              </Combobox.Item>
            )}
          </Combobox.List>
        </Combobox.Content>
      </Combobox>
    </div>
  );
}
```

### [Searchable Item (Inside)](#searchable-item-inside)

A searchable select component inside popup that allows users to filter and select.

```
import { useState } from "react";
import { Combobox } from "@cloudflare/kumo";
import { languages, Language } from "./data/languages";

// Searchable inside popup with TriggerValue
export function ComboboxSearchableInsideDemo() {
  const [value, setValue] = useState<Language>(languages[0]);

  return (
    <Combobox
      value={value}
      onValueChange={(v) => setValue(v as Language)}
      items={languages}
    >
      <Combobox.TriggerValue className="w-[200px]" />
      <Combobox.Content>
        <Combobox.Input placeholder="Search languages" />
        <Combobox.Empty />
        <Combobox.List>
          {(item: Language) => (
            <Combobox.Item key={item.value} value={item}>
              {item.emoji} {item.label}
            </Combobox.Item>
          )}
        </Combobox.List>
      </Combobox.Content>
    </Combobox>
  );
}
```

### [Searchable Select with Placeholder](#searchable-select-with-placeholder)

Use `TriggerValue` with a `placeholder` prop to create a searchable Select-style field. The placeholder is displayed until a value is selected.

```
import { useState } from "react";
import { Combobox } from "@cloudflare/kumo";
import { languages, Language } from "./data/languages";

/** Demonstrates using TriggerValue with a placeholder, behaving like a
 * searchable Select field. The placeholder is shown until a value is selected. */
export function ComboboxSearchableSelectDemo() {
  const [value, setValue] = useState<Language | null>(null);

  return (
    <Combobox
      value={value}
      onValueChange={(v) => setValue(v as Language | null)}
      items={languages}
    >
      <Combobox.TriggerValue
        className="w-[200px]"
        placeholder="Select a language"
      />
      <Combobox.Content>
        <Combobox.Input placeholder="Search languages" />
        <Combobox.Empty />
        <Combobox.List>
          {(item: Language) => (
            <Combobox.Item key={item.value} value={item}>
              {item.emoji} {item.label}
            </Combobox.Item>
          )}
        </Combobox.List>
      </Combobox.Content>
    </Combobox>
  );
}
```

### [Object Item Collections](#object-item-collections)

Derive stable values and labels from application objects with `Combobox.createItems()`.

```
import { useState } from "react";
import { Combobox } from "@cloudflare/kumo";

/** Demonstrates deriving Combobox values and labels from application objects. */
export function ComboboxCreateItemsDemo() {
  const [value, setValue] = useState<DatabaseItem | null>(null);

  return (
    <Combobox
      value={value}
      onValueChange={(nextValue) => setValue(nextValue as DatabaseItem | null)}
      items={databaseItems}
    >
      <Combobox.TriggerValue
        className="w-[240px]"
        placeholder="Select a database"
      />
      <Combobox.Content>
        <Combobox.Input placeholder="Search databases" />
        <Combobox.Empty>No databases found.</Combobox.Empty>
        <Combobox.List>
          {(database: DatabaseItem) => (
            <Combobox.Item key={database.value} value={database}>
              {database.label}
            </Combobox.Item>
          )}
        </Combobox.List>
      </Combobox.Content>
    </Combobox>
  );
}
```

### [Custom Trigger](#custom-trigger)

Use `Combobox.Trigger` with a `render` prop to replace the default input-like trigger with your own element. Pair with `Combobox.Value` to display the selected value. Useful for account switchers, sidebar navigation, or anywhere the default chrome doesn’t fit.

```
import { useState } from "react";
import { CaretUpDownIcon } from "@phosphor-icons/react";
import { Combobox, Button } from "@cloudflare/kumo";
import { languages, Language } from "./data/languages";

export function ComboboxCustomTriggerDemo() {
  const [value, setValue] = useState<Language>(languages[0]);

  return (
    <Combobox
      value={value}
      onValueChange={(v) => setValue(v as Language)}
      items={languages}
    >
      <Combobox.Trigger render={<Button variant="ghost" size="sm" />}>
        <Combobox.Value>
          <span className="truncate">
            {value.emoji} {value.label}
          </span>
        </Combobox.Value>
        <CaretUpDownIcon size={14} className="shrink-0 text-kumo-subtle" />
      </Combobox.Trigger>
      <Combobox.Content>
        <Combobox.Input placeholder="Search languages" />
        <Combobox.Empty />
        <Combobox.List>
          {(item: Language) => (
            <Combobox.Item key={item.value} value={item}>
              {item.emoji} {item.label}
            </Combobox.Item>
          )}
        </Combobox.List>
      </Combobox.Content>
    </Combobox>
  );
}
```

### [Grouped](#grouped)

Group items into categories using the Group and GroupLabel components.

```
import { useState } from "react";
import { Combobox } from "@cloudflare/kumo";

// Grouped items demo
export function ComboboxGroupedDemo() {
  const [value, setValue] = useState<ServerLocation | null>(null);

  return (
    <Combobox
      value={value}
      onValueChange={(v) => setValue(v as ServerLocation | null)}
      items={servers}
    >
      <Combobox.TriggerInput
        className="w-[200px]"
        placeholder="Select server"
      />
      <Combobox.Content>
        <Combobox.Empty />
        <Combobox.List>
          {(group: ServerLocationGroup) => (
            <Combobox.Group key={group.value} items={group.items}>
              <Combobox.GroupLabel>{group.value}</Combobox.GroupLabel>
              <Combobox.Collection>
                {(item: ServerLocation) => (
                  <Combobox.Item key={item.value} value={item}>
                    {item.label}
                  </Combobox.Item>
                )}
              </Combobox.Collection>
            </Combobox.Group>
          )}
        </Combobox.List>
      </Combobox.Content>
    </Combobox>
  );
}
```

### [Multiple](#multiple)

Allow users to select multiple options from the list.

```
import { useState } from "react";
import { Combobox, Text, Button } from "@cloudflare/kumo";

export function ComboboxMultipleDemo() {
  const [value, setValue] = useState<BotItem[]>([]);

  return (
    <div className="flex gap-2">
      <Combobox
        value={value}
        onValueChange={setValue}
        items={bots}
        isItemEqualToValue={(bot: BotItem, selected: BotItem) =>
          bot.value === selected.value
        }
        multiple
      >
        <Combobox.TriggerMultipleWithInput
          className="w-[400px]"
          placeholder="Select bots"
          renderItem={(selected: BotItem) => (
            <Combobox.Chip key={selected.value}>{selected.label}</Combobox.Chip>
          )}
          inputSide="right"
        />
        <Combobox.Content className="max-h-[200px] min-w-auto overflow-y-auto">
          <Combobox.Empty />
          <Combobox.List>
            {(item: BotItem) => (
              <Combobox.Item key={item.value} value={item}>
                <div className="flex gap-2">
                  <Text>{item.label}</Text>
                  <Text variant="secondary">{item.author}</Text>
                </div>
              </Combobox.Item>
            )}
          </Combobox.List>
        </Combobox.Content>
      </Combobox>
      <Button variant="primary">Submit</Button>
    </div>
  );
}
```

### [With Field](#with-field)

Add label and description using the built-in Field wrapper.

```
import { useState } from "react";
import { Combobox } from "@cloudflare/kumo";

export function ComboboxWithFieldDemo() {
  const [value, setValue] = useState<DatabaseItem | null>(null);

  return (
    <div className="w-80">
      <Combobox
        items={databases}
        value={value}
        onValueChange={setValue}
        label="Database"
        description="Select your preferred database"
      >
        <Combobox.TriggerInput placeholder="Select database" />
        <Combobox.Content>
          <Combobox.Empty />
          <Combobox.List>
            {(item: DatabaseItem) => (
              <Combobox.Item key={item.value} value={item}>
                {item.label}
              </Combobox.Item>
            )}
          </Combobox.List>
        </Combobox.Content>
      </Combobox>
    </div>
  );
}
```

### [Disabled](#disabled)

Pass the `disabled` prop to prevent interaction. Works with both `TriggerInput` and `TriggerValue`.

```
import { Combobox } from "@cloudflare/kumo";
import { languages, Language } from "./data/languages";

export function ComboboxDisabledDemo() {
  return (
    <div className="flex flex-wrap items-start gap-4">
      <Combobox value="Apple" items={fruits} disabled>
        <Combobox.TriggerInput
          className="w-[200px]"
          placeholder="Select fruit"
        />
        <Combobox.Content>
          <Combobox.Empty />
          <Combobox.List>
            {(item: string) => (
              <Combobox.Item key={item} value={item}>
                {item}
              </Combobox.Item>
            )}
          </Combobox.List>
        </Combobox.Content>
      </Combobox>

      <Combobox value={languages[0]} items={languages} disabled>
        <Combobox.TriggerValue className="w-[200px]" />
        <Combobox.Content>
          <Combobox.Input placeholder="Search" />
          <Combobox.Empty />
          <Combobox.List>
            {(item: Language) => (
              <Combobox.Item key={item.value} value={item}>
                {item.emoji} {item.label}
              </Combobox.Item>
            )}
          </Combobox.List>
        </Combobox.Content>
      </Combobox>
    </div>
  );
}
```

### [Disabled Items](#disabled-items)

Pass the `disabled` prop to an individual `Combobox.Item` to make it non-selectable. Disabled rows are rendered with a muted style and skipped during keyboard navigation selection.

```
import { useState } from "react";
import { Combobox, Text } from "@cloudflare/kumo";

/** Demonstrates disabled individual items. The `disabled` prop on
 * `Combobox.Item` blocks click and keyboard selection, and renders the row
 * with muted text + a not-allowed cursor. Useful for surfacing options that
 * exist but the user can't pick (e.g. permission-gated, read-only, or
 * already in use elsewhere). */
export function ComboboxDisabledItemsDemo() {
  type DatabaseItemWithDisabled = DatabaseItem & {
    disabled?: boolean;
    reason?: string;
  };

  const items: DatabaseItemWithDisabled[] = [
    { value: "postgres", label: "PostgreSQL" },
    { value: "mysql", label: "MySQL" },
    { value: "mariadb", label: "MariaDB", disabled: true, reason: "Beta" },
    { value: "mongodb", label: "MongoDB" },
    {
      value: "cassandra",
      label: "Apache Cassandra",
      disabled: true,
      reason: "Coming soon",
    },
    { value: "redis", label: "Redis" },
    { value: "d1", label: "Cloudflare D1" },
  ];

  const [value, setValue] = useState<DatabaseItemWithDisabled | null>(null);

  return (
    <div className="w-80">
      <Combobox value={value} onValueChange={setValue} items={items}>
        <Combobox.TriggerInput placeholder="Select database" />
        <Combobox.Content>
          <Combobox.Empty />
          <Combobox.List>
            {(item: DatabaseItemWithDisabled) => (
              <Combobox.Item
                key={item.value}
                value={item}
                disabled={item.disabled}
              >
                <span>
                  {item.label}
                  {item.reason && (
                    <Text variant="secondary" size="xs" as="span">
                      {" — "}
                      {item.reason}
                    </Text>
                  )}
                </span>
              </Combobox.Item>
            )}
          </Combobox.List>
        </Combobox.Content>
      </Combobox>
    </div>
  );
}
```

### [Error State](#error-state)

Display validation errors with the error prop.

```
import { useState } from "react";
import { Combobox } from "@cloudflare/kumo";

export function ComboboxErrorDemo() {
  const [value, setValue] = useState<DatabaseItem | null>(null);

  return (
    <div className="w-80">
      <Combobox
        items={databases}
        value={value}
        onValueChange={setValue}
        label="Database"
        error={{ message: "Please select a database", match: true }}
      >
        <Combobox.TriggerInput placeholder="Select database" />
        <Combobox.Content>
          <Combobox.Empty />
          <Combobox.List>
            {(item: DatabaseItem) => (
              <Combobox.Item key={item.value} value={item}>
                {item.label}
              </Combobox.Item>
            )}
          </Combobox.List>
        </Combobox.Content>
      </Combobox>
    </div>
  );
}
```

## [Filtering](#filtering)

Filtering is case- and accent-insensitive by default, powered by `Intl.Collator` under the hood. For string items, no custom `filter` is needed.

When filtering on a property of object items, use `Combobox.useFilter()` to preserve the built-in accent-insensitive matching:

```
function LanguagePicker() {
  const { contains } = Combobox.useFilter();

  const filter = useCallback(
    (item: Language, query: string) => contains(item.label, query),
    [contains],
  );

  return (
    <Combobox items={languages} filter={filter}>
      {/* ... */}
    </Combobox>
  );
}
```

To disable filtering entirely (e.g. when results come from a server), pass `filter={null}`:

```
<Combobox items={results} filter={null}>
  ...
</Combobox>
```

## [Object Item Collections](#object-item-collections-1)

Use `Combobox.createItems()` when items are application objects rather than primitive values. It derives stable selection values and labels while keeping the source object available to the list renderer.

```
import { useState } from "react";
import { Combobox } from "@cloudflare/kumo";

type Fruit = { id: string; label: string };

const fruits = Combobox.createItems<Fruit>(
  [
    { id: "apple", label: "Apple" },
    { id: "banana", label: "Banana" },
  ],
  {
    getValue: (fruit) => fruit.id,
    getLabel: (fruit) => fruit.label,
  },
);

function FruitPicker() {
  const [value, setValue] = useState<Fruit | null>(null);

  return (
    <Combobox items={fruits} value={value} onValueChange={setValue}>
      <Combobox.TriggerInput placeholder="Select a fruit" />
      <Combobox.Content>
        <Combobox.List>
          {(fruit) => (
            <Combobox.Item key={fruit.id} value={fruit}>
              {fruit.label}
            </Combobox.Item>
          )}
        </Combobox.List>
      </Combobox.Content>
    </Combobox>
  );
}
```

Create static collections at module scope. For data that changes at runtime, memoize `Combobox.createItems()` with the source data as its dependency.

## [Customizing Dropdown Height](#customizing-dropdown-height)

By default, `Combobox.Content` has a max height of `24rem` (384px) or the available viewport space, whichever is smaller. The dropdown scrolls automatically when content exceeds this height.

To customize the max height, pass a className to `Combobox.Content`:

```
// Shorter dropdown (200px)
<Combobox.Content className="max-h-[200px]">

// Taller dropdown (500px)
<Combobox.Content className="max-h-[500px]">

// Use Tailwind presets
<Combobox.Content className="max-h-64">  // 256px
<Combobox.Content className="max-h-96">  // 384px (same as default)
```

## [API Reference](#api-reference)

### [Combobox](#combobox)

Root component for the searchable select.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| size | `"xs" | "sm" | "base" | "lg"` | `"base"` | Size of the combobox trigger. Matches Input component sizes. - \`"xs"\` — Extra small for compact UIs (h-5 / 20px) - \`"sm"\` — Small for secondary fields (h-6.5 / 26px) - \`"base"\` — Default size (h-9 / 36px) - \`"lg"\` — Large for prominent fields (h-10 / 40px) |
| inputSide | `"right" | "top"` | `"right"` | Position of the text input relative to chips in multi-select mode. - \`"right"\` — Input inline to the right of chips - \`"top"\` — Input above chips |
| items\* | `T[]` | \- | Array of items to display in the dropdown |
| value | `T | T[]` | \- | Currently selected value(s) |
| children | `ReactNode` | \- | Combobox content (trigger, content, items) |
| className | `string` | \- | Additional CSS classes |
| label | `ReactNode` | \- | Label content for the combobox (enables Field wrapper) - can be a string or any React node |
| required | `boolean` | \- | Whether the combobox is required |
| labelTooltip | `ReactNode` | \- | Tooltip content to display next to the label via an info icon |
| description | `ReactNode` | \- | Helper text displayed below the combobox |
| error | `string | object` | \- | Error message or validation error object |
| onValueChange | `(value: T | T[]) => void` | \- | Callback when selection changes |
| multiple | `boolean` | \- | Allow multiple selections |
| isItemEqualToValue | `(item: T, value: T) => boolean` | \- | Custom equality function for comparing items |

### [Combobox.Content](#comboboxcontent)

Dropdown container for the list.

| Prop | Type | Default |
| --- | --- | --- |
| className | `string` | \- |
| align | `ComboboxBase.Positioner.Props["align"]` | \- |
| alignOffset | `ComboboxBase.Positioner.Props["alignOffset"]` | \- |
| side | `ComboboxBase.Positioner.Props["side"]` | \- |
| sideOffset | `ComboboxBase.Positioner.Props["sideOffset"]` | \- |
| anchor | `ComboboxBase.Positioner.Props["anchor"]` | \- |
| positionMethod | `ComboboxBase.Positioner.Props["positionMethod"]` | \- |
| collisionAvoidance | `ComboboxBase.Positioner.Props["collisionAvoidance"]` | \- |
| collisionBoundary | `ComboboxBase.Positioner.Props["collisionBoundary"]` | \- |
| collisionPadding | `ComboboxBase.Positioner.Props["collisionPadding"]` | \- |
| sticky | `ComboboxBase.Positioner.Props["sticky"]` | \- |
| disableAnchorTracking | `ComboboxBase.Positioner.Props["disableAnchorTracking"]` | \- |
| container | `PortalContainer` | \- |

### [Combobox.Item](#comboboxitem)

Individual selectable option.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Additional Sub-components](#additional-sub-components)

-   `Combobox.TriggerInput` - Single-select input trigger
-   `Combobox.TriggerValue` - Button trigger showing selected value
-   `Combobox.TriggerMultipleWithInput` - Multi-select with chips
-   `Combobox.Input` - Search input inside dropdown
-   `Combobox.List` - List container with render prop
-   `Combobox.Group` - Group container for categorized items
-   `Combobox.GroupLabel` - Header label for a group
-   `Combobox.Collection` - Items container within a group
-   `Combobox.Chip` - Selected item chip
-   `Combobox.Empty` - Empty state message
-   `Combobox.createItems` - Collection helper for object items