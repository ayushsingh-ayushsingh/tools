# Text

A typography component for various heading and copy styles.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/text/text.tsx)

---

```
import { Text } from "@cloudflare/kumo";

export function TextVariantsDemo() {
  return (
    <div className="grid w-full grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text variant="heading">Heading</Text>
        <Text variant="mono-secondary">text-lg (16px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text variant="heading" size="lg" as="h2">
          Heading large
        </Text>
        <Text variant="mono-secondary">text-xl (20px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text>Body</Text>
        <Text variant="mono-secondary">text-base (14px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text bold>Body bold</Text>
        <Text variant="mono-secondary">text-base (14px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text size="lg">Body lg</Text>
        <Text variant="mono-secondary">text-lg (16px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text size="sm">Body sm</Text>
        <Text variant="mono-secondary">text-sm (13px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text size="xs">Body xs</Text>
        <Text variant="mono-secondary">text-xs (12px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text variant="secondary">Body secondary</Text>
        <Text variant="mono-secondary">text-base (14px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text variant="mono">Monospace</Text>
        <Text variant="mono-secondary">text-sm (13px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text variant="mono" size="lg">
          Monospace lg
        </Text>
        <Text variant="mono-secondary">text-base (14px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text variant="mono-secondary">Monospace secondary</Text>
        <Text variant="mono-secondary">text-sm (13px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text variant="success">Success</Text>
        <Text variant="mono-secondary">text-base (14px)</Text>
      </div>
      <div className="flex flex-col justify-end gap-1 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
        <Text variant="error">Error</Text>
        <Text variant="mono-secondary">text-base (14px)</Text>
      </div>
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Text } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Text } from "@cloudflare/kumo/components/text";
```

## [Usage](#usage)

```
import { Text } from "@cloudflare/kumo";

export default function Example() {
  return <Text>Your content here</Text>;
}
```

### Semantic HTML

The `variant` prop controls visual styling only—it does not determine the HTML element rendered. Heading variants **require** the `as` prop to avoid silently excluding real section headings from the document outline. Body and monospace variants have sensible defaults (`<p>` and `<span>` respectively) and accept `as` optionally.

```
// Heading variants REQUIRE `as` — TypeScript will flag usages missing it
<Text variant="heading1">Page Title</Text> // Doesn't compile

// Real section headings (contribute to the document outline)
<Text variant="heading1" as="h1">Page Title</Text>
<Text variant="heading2" as="h2">Section Title</Text>

// Decorative heading-styled text that is NOT a section heading
<Text variant="heading1" as="span">Big bold card label</Text>

// Visually one size, semantically another
<Text variant="heading1" as="h3">Visually large, but semantically h3</Text>
```

The `as` prop accepts: `"h1"` through `"h6"`, `"p"`, and `"span"`. Body variants default to `"p"`, monospace variants default to `"span"`, and heading variants have no default — you must choose explicitly.

### Restrictions

The `bold` and `size` props are intentionally restricted to the `base`, `secondary`, `success`, and `error` text variants.

```
<Text size="sm" bold>Body</Text>
<Text variant="secondary" bold>Body secondary</Text>
<Text variant="success" size="lg">Success</Text>
<Text variant="error">Error</Text>
```

Monospace variants (`mono` and `mono-secondary`) can only set `size` to `lg` and cannot use the `bold` prop:

```
<Text variant="mono">Monospace</Text>
<Text variant="mono" size="lg">Monospace</Text>
<Text variant="mono" bold>Monospace</Text> // Doesn't compile
```

Headings (i.e. `heading1`, `heading2` and `heading3` variants) cannot use these props at all:

```
<Text variant="heading1" bold>
  Heading 1
</Text> // Doesn't compile
```

## [Truncate](#truncate)

Use the `truncate` prop to clip overflowing text with an ellipsis. This adds `truncate min-w-0` classes, which is useful when `Text` is inside a flex or grid container.

```
import { Text } from "@cloudflare/kumo";

export function TextTruncateDemo() {
  return (
    <div className="w-64 rounded-lg border border-kumo-hairline bg-kumo-base p-4">
      <Text truncate>
        This is a long piece of text that will be truncated with an ellipsis
        when it overflows its container.
      </Text>
    </div>
  );
}
```

```
<Text truncate>This is a long piece of text that will be truncated...</Text>
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| variant | `"heading" | "heading1" | "heading2" | "heading3" | "body" | "secondary" | "success" | "error" | "mono" | "mono-secondary"` | `"body"` | Text style variant. Determines color, font, and weight. - \`"heading"\` — Heading text (16px by default, 20px with \`size="lg"\`; semibold) - \`"heading1"\` — Deprecated; use \`"heading"\` (30px, semibold) - \`"heading2"\` — Deprecated; use \`"heading"\` (24px, semibold) - \`"heading3"\` — Deprecated; use \`"heading"\` (16px, semibold) - \`"body"\` — Default body text - \`"secondary"\` — Muted text for secondary information - \`"success"\` — Success state text - \`"error"\` — Error state text - \`"mono"\` — Monospace text for code - \`"mono-secondary"\` — Muted monospace text |
| size | `"xs" | "sm" | "base" | "lg"` | `"base"` | Text size. Supported values depend on the variant: - \`"heading"\` — 16px when omitted, or 20px with \`"lg"\` - Body variants — \`"xs"\` (12px), \`"sm"\` (13px), \`"base"\` (14px), or \`"lg"\` (16px) - Monospace variants — 13px when omitted, or 14px with \`"lg"\` |
| bold | `boolean` | \- | Whether to use bold font weight (only applies to body variants). |
| truncate | `boolean` | \- | Whether to truncate overflowing text with an ellipsis. Adds \`truncate min-w-0\` classes. |
| as | `"h1" | "h2" | "h3" | "h4" | "h5" | "h6" | "p" | "span" | "label" | "dt" | "dd" | "li" | "figcaption" | "legend" | "pre" | "code" | "em" | "strong" | "small" | "abbr" | "time"` | \- | The HTML element to render. Accepts headings (\`"h1"\`–\`"h6"\`), block text (\`"p"\`, \`"pre"\`), inline text (\`"span"\`, \`"code"\`, \`"em"\`, \`"strong"\`, \`"small"\`, \`"abbr"\`, \`"time"\`), form-related (\`"label"\`, \`"legend"\`), list/definition (\`"dt"\`, \`"dd"\`, \`"li"\`), and \`"figcaption"\`. - \*\*Optional\*\* for \`"heading"\` (defaults to \`"span"\`). Pass the heading element that reflects this text's place in the document outline. - \*\*Required\*\* for deprecated heading variants (\`"heading1"\`, \`"heading2"\`, \`"heading3"\`). - \*\*Optional\*\* for body variants (defaults to \`"p"\`) and monospace variants (defaults to \`"span"\`). |
| children | `ReactNode` | \- | Text content. |