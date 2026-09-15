# Tooltip

A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/tooltip/tooltip.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/tooltip)

---

```
import { Tooltip, TooltipProvider, Button } from "@cloudflare/kumo";
import { PlusIcon } from "@phosphor-icons/react";

export function TooltipHeroDemo() {
  return (
    <TooltipProvider>
      <Tooltip
        content="Add new item"
        render={
          <Button shape="square" icon={PlusIcon} aria-label="Add new item" />
        }
      />
    </TooltipProvider>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Tooltip, TooltipProvider } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Tooltip, TooltipProvider } from "@cloudflare/kumo/components/tooltip";
```

## [Usage](#usage)

```
import { Tooltip, Button } from "@cloudflare/kumo";

export default function Example() {
  return (
    <Tooltip content="Tooltip text" render={<Button />}>
      Hover me
    </Tooltip>
  );
}
```

For delay grouping across multiple tooltips, see [TooltipProvider](#tooltipprovider).

## [Examples](#examples)

### [Basic Tooltip](#basic-tooltip)

```
import { Tooltip, TooltipProvider, Button } from "@cloudflare/kumo";
import { PlusIcon } from "@phosphor-icons/react";

export function TooltipBasicDemo() {
  return (
    <TooltipProvider>
      <Tooltip
        content="Add"
        render={<Button shape="square" icon={PlusIcon} aria-label="Add" />}
      />
    </TooltipProvider>
  );
}
```

### [Multiple Tooltips](#multiple-tooltips)

```
import { Tooltip, TooltipProvider, Button } from "@cloudflare/kumo";
import { PlusIcon, TranslateIcon } from "@phosphor-icons/react";

export function TooltipMultipleDemo() {
  return (
    <TooltipProvider>
      <div className="flex gap-2">
        <Tooltip
          content="Add"
          render={<Button shape="square" icon={PlusIcon} aria-label="Add" />}
        />
        <Tooltip
          content="Change language"
          render={
            <Button
              shape="square"
              icon={TranslateIcon}
              aria-label="Change language"
            />
          }
        />
      </div>
    </TooltipProvider>
  );
}
```

### [Long Content / Overflow](#long-content--overflow)

Tooltips with long content automatically constrain their width to the available viewport space using `--available-width` from Base UI’s Positioner. Hover over the edge buttons to see the tooltip wrap instead of overflowing the viewport.

```
import { Tooltip, TooltipProvider, Button } from "@cloudflare/kumo";

/**
 * Control the delay before opening and closing the tooltip.
 * `delay` controls open delay (default: 600ms), `closeDelay` controls close delay (default: 0ms).
 */
/**
 * Demonstrates that long tooltip content respects available viewport space.
 * Tooltips near the edge of the viewport constrain their width to
 * `--available-width` so they don't overflow.
 */
export function TooltipOverflowDemo() {
  const longContent =
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.";
  return (
    <TooltipProvider>
      <div className="flex w-full justify-between">
        <Tooltip
          content={longContent}
          side="bottom"
          render={<Button variant="secondary" />}
        >
          Near left edge
        </Tooltip>
        <Tooltip
          content={longContent}
          side="bottom"
          render={<Button variant="secondary" />}
        >
          Centered
        </Tooltip>
        <Tooltip
          content={longContent}
          side="bottom"
          render={<Button variant="secondary" />}
        >
          Near right edge
        </Tooltip>
      </div>
    </TooltipProvider>
  );
}
```

### [Delay Control](#delay-control)

Use `delay` to control how long to wait before opening (default: 600ms) and `closeDelay` to control how long to wait before closing (default: 0ms).

```
import { Tooltip, TooltipProvider, Button } from "@cloudflare/kumo";

export function TooltipDelayDemo() {
  return (
    <TooltipProvider>
      <div className="flex gap-4">
        <Tooltip
          content="Opens after 1 second"
          delay={1000}
          render={<Button variant="secondary" />}
        >
          1s open delay
        </Tooltip>
        <Tooltip
          content="Stays open 500ms after leaving"
          closeDelay={500}
          render={<Button variant="secondary" />}
        >
          500ms close delay
        </Tooltip>
        <Tooltip
          content="Instant open, stays 1s"
          delay={0}
          closeDelay={1000}
          render={<Button variant="secondary" />}
        >
          Instant + 1s close
        </Tooltip>
      </div>
    </TooltipProvider>
  );
}
```

## [TooltipProvider](#tooltipprovider)

`TooltipProvider` groups multiple tooltips so that after the first tooltip has been shown, switching to another skips the open delay. Place it once at your app root or layout — not around each individual `Tooltip`.

```
// Wrap your app or layout once
<TooltipProvider>
  <App />
</TooltipProvider>

// Then use Tooltip anywhere inside
<Tooltip content="Add" render={<Button shape="square" icon={PlusIcon} />} />
```

## [API Reference](#api-reference)

### [Tooltip](#tooltip)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| side | `"top" | "bottom" | "left" | "right"` | `"top"` | \- |
| className | `string` | \- | Additional CSS classes |
| children | `ReactNode` | \- | Child elements |
| content\* | `ReactNode` | \- | Content to display in the tooltip |

### [TooltipProvider](#tooltipprovider-1)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| delay | `number` | `600` | How long to wait (ms) before opening a tooltip once the pointer enters the trigger. |
| closeDelay | `number` | `0` | How long to wait (ms) before closing a tooltip. |
| timeout | `number` | `400` | Grace period (ms) during which a just-closed tooltip's delay is skipped when another tooltip opens. |