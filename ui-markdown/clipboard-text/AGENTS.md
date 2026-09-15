# Clipboard Text

A text component with a copy-to-clipboard button.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/clipboard-text/clipboard-text.tsx)

---

```
import { ClipboardText } from "@cloudflare/kumo";

export function ClipboardTextBasicDemo() {
  return <ClipboardText text="0c239dd2" />;
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { ClipboardText } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { ClipboardText } from "@cloudflare/kumo/components/clipboard-text";
```

## [Usage](#usage)

```
import { ClipboardText } from "@cloudflare/kumo";

export default function Example() {
  return <ClipboardText text="Copy this text" />;
}
```

## [Examples](#examples)

### [Short Text](#short-text)

```
import { ClipboardText } from "@cloudflare/kumo";

export function ClipboardTextShortDemo() {
  return <ClipboardText text="abc123" />;
}
```

### [API Key](#api-key)

```
import { ClipboardText } from "@cloudflare/kumo";

export function ClipboardTextApiKeyDemo() {
  return <ClipboardText text="sk_live_51H8..." />;
}
```

### [Copy Alternate Text](#copy-alternate-text)

```
import { ClipboardText } from "@cloudflare/kumo";

export function ClipboardTextAlternateTextToCopyDemo() {
  return (
    <ClipboardText
      text="sk_live_***********"
      textToCopy="sk_live_51H8_abc123"
    />
  );
}
```

### [Long Text](#long-text)

```
import { ClipboardText } from "@cloudflare/kumo";

export function ClipboardTextLongDemo() {
  return <ClipboardText text="https://example.com/very/long/url/path" />;
}
```

### [With Tooltip](#with-tooltip)

Shows “Copy” tooltip on hover, “Copied!” toast on click.

```
import { ClipboardText } from "@cloudflare/kumo";

/** With tooltip on hover showing "Copy", and anchored toast on click showing "Copied" */
export function ClipboardTextWithTooltipDemo() {
  return (
    <ClipboardText
      text="npx kumo add button"
      tooltip={{ text: "Copy", copiedText: "Copied!", side: "top" }}
    />
  );
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| size | `"sm" | "base" | "lg"` | `"lg"` | Size of the clipboard text field. - \`"sm"\` — Small clipboard text for compact UIs - \`"base"\` — Default clipboard text size - \`"lg"\` — Large clipboard text for prominent display |
| text\* | `string` | \- | The text to display and copy to clipboard. |
| textToCopy | `string` | \- | If provided, this text will be copied to clipboard instead of the \`text\` prop. |
| className | `string` | \- | Additional CSS classes merged via \`cn()\`. |
| tooltip | `object` | \- | Tooltip config. Shows tooltip on hover, anchored toast on click. |
| labels | `object` | \- | Accessible labels for i18n. |