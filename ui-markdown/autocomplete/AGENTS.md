# Autocomplete

A free-form text input with an optional filtered suggestion list. Unlike Combobox, the value is not constrained to the items list.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/autocomplete/autocomplete.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/autocomplete)

---

```
import { Autocomplete } from "@cloudflare/kumo";

/** Basic autocomplete with a flat list of strings. */
export function AutocompleteDemo() {
  return (
    <Autocomplete items={fruits}>
      <Autocomplete.InputGroup placeholder="Search fruits…" />
      <Autocomplete.Content>
        <Autocomplete.List>
          {(item: string) => (
            <Autocomplete.Item key={item} value={item}>
              {item}
            </Autocomplete.Item>
          )}
        </Autocomplete.List>
      </Autocomplete.Content>
    </Autocomplete>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Autocomplete } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Autocomplete } from "@cloudflare/kumo/components/autocomplete";
```

## [When to use](#when-to-use)

Use `Autocomplete` when the input value can be free-form text and suggestions are optional hints. Use `Combobox` instead when the selected value must come from the predefined list.

## [Controlled](#controlled)

Pass `value` and `onValueChange` for controlled usage.

```
import { useState } from "react";
import { Autocomplete } from "@cloudflare/kumo";

/** Controlled autocomplete with value and onValueChange. */
export function AutocompleteControlledDemo() {
  const [value, setValue] = useState("");

  return (
    <div className="flex w-80 flex-col gap-3">
      <Autocomplete
        items={fruits}
        value={value}
        onValueChange={(v) => setValue(v)}
      >
        <Autocomplete.InputGroup placeholder="Type a fruit…" />
        <Autocomplete.Content>
          <Autocomplete.List>
            {(item: string) => (
              <Autocomplete.Item key={item} value={item}>
                {item}
              </Autocomplete.Item>
            )}
          </Autocomplete.List>
        </Autocomplete.Content>
      </Autocomplete>
      {value && (
        <p className="text-sm text-kumo-subtle">
          Value: <span className="font-medium text-kumo-default">{value}</span>
        </p>
      )}
    </div>
  );
}
```

## [With Field](#with-field)

Add `label`, `description`, and `required` to enable the built-in Field wrapper.

```
import { useCallback } from "react";
import { Autocomplete } from "@cloudflare/kumo";
import { languages, Language } from "./data/languages";

/** Autocomplete with label, description, and Field wrapper. */
export function AutocompleteWithFieldDemo() {
  const { contains } = Autocomplete.useFilter();

  const filter = useCallback(
    (item: Language, query: string) => contains(item.label, query),
    [contains],
  );

  return (
    <div className="w-80">
      <Autocomplete
        items={languages}
        label="Language"
        description="Start typing to filter languages"
        filter={filter}
      >
        <Autocomplete.InputGroup placeholder="Search a language…" />
        <Autocomplete.Content>
          <Autocomplete.List>
            {(item: Language) => (
              <Autocomplete.Item key={item.value} value={item}>
                {item.emoji} {item.label}
              </Autocomplete.Item>
            )}
          </Autocomplete.List>
        </Autocomplete.Content>
      </Autocomplete>
    </div>
  );
}
```

## [Error State](#error-state)

Display validation errors with the `error` prop.

```
import { useCallback } from "react";
import { Autocomplete } from "@cloudflare/kumo";

/** Autocomplete with error state via the Field wrapper. */
export function AutocompleteErrorDemo() {
  const { contains } = Autocomplete.useFilter();

  const filter = useCallback(
    (item: Country, query: string) => contains(item.label, query),
    [contains],
  );

  return (
    <div className="w-80">
      <Autocomplete
        items={countries}
        label="Country"
        error={{ message: "Please enter a valid country", match: true }}
        filter={filter}
      >
        <Autocomplete.InputGroup placeholder="Search countries…" />
        <Autocomplete.Content>
          <Autocomplete.List>
            {(item: Country) => (
              <Autocomplete.Item key={item.code} value={item}>
                {item.label}
              </Autocomplete.Item>
            )}
          </Autocomplete.List>
        </Autocomplete.Content>
      </Autocomplete>
    </div>
  );
}
```

## [Grouped](#grouped)

Group items into categories using `Autocomplete.Group` and `Autocomplete.GroupLabel`.

```
import { Autocomplete } from "@cloudflare/kumo";

/** Autocomplete with grouped items using Group and GroupLabel. */
export function AutocompleteGroupedDemo() {
  return (
    <Autocomplete items={servers}>
      <Autocomplete.InputGroup placeholder="Select region…" />
      <Autocomplete.Content>
        <Autocomplete.List>
          {(group: ServerGroup) => (
            <Autocomplete.Group key={group.value} items={group.items}>
              <Autocomplete.GroupLabel>{group.value}</Autocomplete.GroupLabel>
              <Autocomplete.Collection>
                {(item: ServerLocation) => (
                  <Autocomplete.Item key={item.value} value={item}>
                    {item.label}
                  </Autocomplete.Item>
                )}
              </Autocomplete.Collection>
            </Autocomplete.Group>
          )}
        </Autocomplete.List>
      </Autocomplete.Content>
    </Autocomplete>
  );
}
```

## [Sizes](#sizes)

The `size` prop on `Autocomplete.InputGroup` supports four variants matching the Input component: `xs`, `sm`, `base` (default), and `lg`.

```
import { Autocomplete } from "@cloudflare/kumo";

/** Demonstrates the four size variants: xs, sm, base, and lg. */
export function AutocompleteSizesDemo() {
  return (
    <div className="flex flex-wrap items-center gap-4">
      <Autocomplete items={fruits.slice(0, 10)}>
        <Autocomplete.InputGroup size="xs" placeholder="xs" />
        <Autocomplete.Content>
          <Autocomplete.List>
            {(item: string) => (
              <Autocomplete.Item key={item} value={item}>
                {item}
              </Autocomplete.Item>
            )}
          </Autocomplete.List>
        </Autocomplete.Content>
      </Autocomplete>
      <Autocomplete items={fruits.slice(0, 10)}>
        <Autocomplete.InputGroup size="sm" placeholder="sm" />
        <Autocomplete.Content>
          <Autocomplete.List>
            {(item: string) => (
              <Autocomplete.Item key={item} value={item}>
                {item}
              </Autocomplete.Item>
            )}
          </Autocomplete.List>
        </Autocomplete.Content>
      </Autocomplete>
      <Autocomplete items={fruits.slice(0, 10)}>
        <Autocomplete.InputGroup size="base" placeholder="base (default)" />
        <Autocomplete.Content>
          <Autocomplete.List>
            {(item: string) => (
              <Autocomplete.Item key={item} value={item}>
                {item}
              </Autocomplete.Item>
            )}
          </Autocomplete.List>
        </Autocomplete.Content>
      </Autocomplete>
      <Autocomplete items={fruits.slice(0, 10)}>
        <Autocomplete.InputGroup size="lg" placeholder="lg" />
        <Autocomplete.Content>
          <Autocomplete.List>
            {(item: string) => (
              <Autocomplete.Item key={item} value={item}>
                {item}
              </Autocomplete.Item>
            )}
          </Autocomplete.List>
        </Autocomplete.Content>
      </Autocomplete>
    </div>
  );
}
```

## [Filtering](#filtering)

Filtering is case- and accent-insensitive by default, powered by `Intl.Collator` under the hood. For string items, no custom `filter` is needed.

When filtering on a property of object items, use `Autocomplete.useFilter()` to preserve the built-in accent-insensitive matching:

```
function LanguagePicker() {
  const { contains } = Autocomplete.useFilter();

  const filter = useCallback(
    (item: Language, query: string) => contains(item.label, query),
    [contains],
  );

  return (
    <Autocomplete items={languages} filter={filter}>
      {/* ... */}
    </Autocomplete>
  );
}
```

To disable filtering entirely (e.g. when results come from a server), pass `filter={null}`:

```
<Autocomplete items={results} filter={null}>
  ...
</Autocomplete>
```

## [API Reference](#api-reference)

### [Autocomplete](#autocomplete)

Root component. Wraps all sub-components and manages state.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| items\* | `unknown[]` | \- | Array of items to display in the dropdown |
| value | `string | number | string[]` | \- | The controlled input value |
| open | `boolean` | \- | Whether the popup is open (controlled) |
| children | `ReactNode` | \- | Autocomplete content (input group, popup content) |
| className | `string` | \- | Additional CSS classes |
| label | `ReactNode` | \- | Label content (enables Field wrapper) |
| required | `boolean` | \- | Whether the field is required |
| labelTooltip | `ReactNode` | \- | Tooltip content to display next to the label |
| description | `ReactNode` | \- | Helper text displayed below the field |
| error | `string | object` | \- | Error message or validation error object |

### [Autocomplete.InputGroup](#autocompleteinputgroup)

Self-contained input wrapper that renders the text input, clear button, and dropdown trigger together.

| Prop | Type | Default |
| --- | --- | --- |
| className | `string` | \- |
| size | `KumoAutocompleteSize` | \- |
| placeholder | `string` | \- |

### [Autocomplete.Content](#autocompletecontent)

Dropdown popup container. Wraps Portal, Positioner, and Popup.

| Prop | Type | Default |
| --- | --- | --- |
| children | `ReactNode` | \- |
| className | `string` | \- |
| align | `AutocompleteBase.Positioner.Props["align"]` | \- |
| alignOffset | `AutocompleteBase.Positioner.Props["alignOffset"]` | \- |
| side | `AutocompleteBase.Positioner.Props["side"]` | \- |
| sideOffset | `AutocompleteBase.Positioner.Props["sideOffset"]` | \- |

### [Autocomplete.Item](#autocompleteitem)

Individual suggestion item in the list.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Additional Sub-components](#additional-sub-components)

-   `Autocomplete.List` — scrollable list container with render prop
-   `Autocomplete.Group` — groups items under a heading
-   `Autocomplete.GroupLabel` — heading label for a group
-   `Autocomplete.Collection` — item container within a group
-   `Autocomplete.Separator` — horizontal divider between items