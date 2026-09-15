# Tag Input

A creatable multi-value input for values that do not come from a predefined option list.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/tag-input/tag-input.tsx)

---

```
import { useState } from "react";
import { TagInput } from "@cloudflare/kumo";

export function TagInputDemo() {
  const [recipients, setRecipients] = useState(["ava@cloudflare.com"]);
  return (
    <TagInput
      label="Recipients"
      description="Paste comma- or newline-separated email addresses."
      placeholder="name@example.com"
      autoComplete="off"
      value={recipients}
      onValueChange={setRecipients}
      validateValue={(value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)}
    />
  );
}
```

## [Installation](#installation)

```
import { TagInput } from "@cloudflare/kumo";
```

## [Usage](#usage)

Use `value` with `onValueChange` to control the tags. Use `defaultValue` for uncontrolled usage.

```
const [tags, setTags] = useState<string[]>([]);

<TagInput
  label="Labels"
  value={tags}
  onValueChange={setTags}
  placeholder="Add a label"
/>
```

## [Examples](#examples)

### [Unrestricted values](#unrestricted-values)

```
import { TagInput } from "@cloudflare/kumo";

export function TagInputUnrestrictedDemo() {
  return (
    <TagInput
      defaultValue={["frontend", "priority"]}
      label="Labels"
      description="Accepts any non-empty value."
      placeholder="Add a label"
    />
  );
}
```

### [Maximum values](#maximum-values)

```
import { TagInput } from "@cloudflare/kumo";

export function TagInputLimitedDemo() {
  return (
    <TagInput
      defaultValue={["alpha"]}
      label="Access groups"
      maxValues={3}
      description="A maximum of three groups."
      placeholder="Type a group name"
    />
  );
}
```

### [Localization](#localization)

```
import { TagInput } from "@cloudflare/kumo";

export function TagInputLocalizationDemo() {
  return (
    <TagInput
      defaultValue={["uno"]}
      label="Etiquetas"
      labels={{
        input: "Agregar etiqueta",
        removeValue: (value) => `Eliminar ${value}`,
        invalidValue: (value) => `${value} no es valido.`,
        maxValuesReached: (maxValues) => `Maximo de ${maxValues} etiquetas.`,
      }}
      maxValues={3}
      placeholder="Agregar una etiqueta"
    />
  );
}
```

## [Behavior](#behavior)

Press Enter, comma, or Tab to create a tag. Blur also commits the current value. Pasting comma- or newline-separated text creates each value synchronously. Duplicate values are ignored.

## [Localization](#localization-1)

Use `labels` to translate all TagInput-generated text: the fallback input name, tag removal action, invalid-value feedback, and maximum-value feedback.

```
<TagInput
  label="Etiquetas"
  labels={{
    input: "Agregar etiqueta",
    removeValue: (value) => `Eliminar ${value}`,
    invalidValue: (value) => `${value} no es valido.`,
    maxValuesReached: (maxValues) => `Maximo de ${maxValues} etiquetas.`,
  }}
/>
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| alt | `string` | \- | \- |
| autoComplete | `React.HTMLInputAutoCompleteAttribute` | \- | \- |
| checked | `boolean` | \- | \- |
| height | `number | string` | \- | \- |
| list | `string` | \- | \- |
| name | `string` | \- | \- |
| placeholder | `string` | \- | \- |
| readOnly | `boolean` | \- | \- |
| required | `boolean` | \- | \- |
| type | `React.HTMLInputTypeAttribute` | \- | \- |
| width | `number | string` | \- | \- |
| className | `string` | \- | \- |
| id | `string` | \- | \- |
| lang | `string` | \- | \- |
| title | `string` | \- | \- |
| children | `ReactNode` | \- | \- |
| value | `string[]` | \- | \- |
| validateValue | `object` | \- | \- |
| maxValues | `number` | \- | \- |
| labels | `TagInputLabels` | \- | Translated labels for generated input, action, and validation text. |
| label | `ReactNode` | \- | \- |
| labelTooltip | `ReactNode` | \- | \- |
| description | `ReactNode` | \- | \- |
| error | `string | object` | \- | \- |
| variant | `"default" | "error"` | `"default"` | \- |
| disabled | `boolean` | \- | \- |