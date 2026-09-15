# Layer Card

A card component with a layered visual effect, perfect for navigation or feature highlights.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/layer-card/layer-card.tsx)

---

```
import { LayerCard, Button } from "@cloudflare/kumo";
import { ArrowRightIcon } from "@phosphor-icons/react";

export function LayerCardDemo() {
  return (
    <LayerCard>
      <LayerCard.Secondary className="flex items-center justify-between">
        <div>Next Steps</div>
        <Button
          variant="ghost"
          size="sm"
          shape="square"
          aria-label="Go to next steps"
        >
          <ArrowRightIcon size={16} />
        </Button>
      </LayerCard.Secondary>

      <LayerCard.Primary>Get started with Kumo</LayerCard.Primary>
    </LayerCard>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { LayerCard } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { LayerCard } from "@cloudflare/kumo/components/layer-card";
```

## [Usage](#usage)

```
import { LayerCard } from "@cloudflare/kumo";

export default function Example() {
  return (
    <LayerCard className="w-[250px]">
      <LayerCard.Secondary>Documentation</LayerCard.Secondary>
      <LayerCard.Primary>Learn how to use Kumo components</LayerCard.Primary>
    </LayerCard>
  );
}
```

`LayerCard` also supports a simple surface-style mode for cases where you do not need a secondary header row. In those cases, render content directly inside `LayerCard` instead of wrapping it in `LayerCard.Primary`.

```
import { LayerCard } from "@cloudflare/kumo";

export default function Example() {
  return (
    <LayerCard className="w-[250px] p-4">
      Learn how to use Kumo components
    </LayerCard>
  );
}
```

## [Examples](#examples)

### [Basic Card](#basic-card)

```
import { LayerCard } from "@cloudflare/kumo";

export function LayerCardBasicDemo() {
  return (
    <LayerCard className="w-[250px]">
      <LayerCard.Secondary>Getting Started</LayerCard.Secondary>
      <LayerCard.Primary>
        <p className="text-sm text-kumo-subtle">
          Quick start guide for new users
        </p>
      </LayerCard.Primary>
    </LayerCard>
  );
}
```

### [Surface-style Card](#surface-style-card)

For simple card containers, render content directly inside `LayerCard` without `LayerCard.Primary`.

```
import { LayerCard } from "@cloudflare/kumo";

export function LayerCardSurfaceDemo() {
  return (
    <LayerCard className="w-[250px] p-4">
      <p className="text-sm text-kumo-subtle">
        Quick start guide for new users
      </p>
    </LayerCard>
  );
}
```

### [Multiple Cards](#multiple-cards)

```
import { LayerCard } from "@cloudflare/kumo";

export function LayerCardMultipleDemo() {
  return (
    <div className="flex gap-4">
      <LayerCard className="w-[200px]">
        <LayerCard.Secondary>Components</LayerCard.Secondary>
        <LayerCard.Primary>
          <p className="text-sm">Browse all components</p>
        </LayerCard.Primary>
      </LayerCard>
      <LayerCard className="w-[200px]">
        <LayerCard.Secondary>Examples</LayerCard.Secondary>
        <LayerCard.Primary>
          <p className="text-sm">View code examples</p>
        </LayerCard.Primary>
      </LayerCard>
    </div>
  );
}
```

### [Filter Toolbar with Small Tabs](#filter-toolbar-with-small-tabs)

Combine `Tabs size=“sm”` with `Input size=“sm”` inside a LayerCard for compact filter toolbars. Both share the same `h-6.5` (26px) height.

```
import { useState } from "react";
import { Badge, Input, LayerCard, Tabs } from "@cloudflare/kumo";

// ─── Mockup: Segmented filter + search ───────────────────────────────

/** Subrequests card with inline filter toolbar inside Primary. */
export function LayerCardFilterSubrequestsDemo() {
  const [filter, setFilter] = useState<StatusFilter>("all");
  const [search, setSearch] = useState("");

  const filtered = ORIGINS.filter((o) => {
    if (filter === "2xx" && o.s2xx === 0) return false;
    if (filter === "4xx" && o.s4xx === 0) return false;
    if (search && !o.origin.toLowerCase().includes(search.toLowerCase()))
      return false;
    return true;
  });

  return (
    <LayerCard className="w-full max-w-[540px]">
      <LayerCard.Secondary>Subrequests</LayerCard.Secondary>

      <LayerCard.Primary>
        {/* Toolbar: tabs + search on one line */}
        <div className="mb-2 flex items-center gap-3">
          <Input
            size="sm"
            placeholder="Filter origins…"
            aria-label="Filter origins"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="min-w-0 flex-1"
          />
          <Tabs
            variant="segmented"
            size="sm"
            className="shrink-0"
            tabs={[
              { value: "all", label: "All" },
              { value: "2xx", label: "2xx" },
              { value: "3xx", label: "3xx" },
              { value: "4xx", label: "4xx" },
              { value: "5xx", label: "5xx" },
            ]}
            value={filter}
            onValueChange={(v) => setFilter(v as StatusFilter)}
          />
        </div>

        {/* Custom lightweight table — no banding, uniform bg */}
        <div className="-mx-1 text-sm">
          {/* Header */}
          <div className="grid grid-cols-[1fr_auto_auto] gap-x-4 border-b border-kumo-fill px-1 pb-2 text-xs font-medium text-kumo-subtle">
            <span>Origin</span>
            <span className="w-28 text-right">Requests</span>
            <span className="w-20 text-right">Duration</span>
          </div>

          {/* Rows */}
          {filtered.map((row, i) => (
            <div
              key={row.origin}
              className={`grid grid-cols-[1fr_auto_auto] items-center gap-x-4 px-1 py-2.5 ${i < filtered.length - 1 ? "border-b border-kumo-hairline" : ""}`}
            >
              <span className="truncate font-medium text-kumo-default">
                {row.origin}
              </span>
              <div className="flex w-28 items-center justify-end gap-1.5">
                {row.s2xx > 0 && (
                  <Badge variant="success">{`2xx ${row.s2xx}`}</Badge>
                )}
                {row.s4xx > 0 && (
                  <Badge variant="error">{`4xx ${row.s4xx}`}</Badge>
                )}
              </div>
              <span className="w-20 text-right text-kumo-subtle">
                {row.duration}
              </span>
            </div>
          ))}
        </div>

        {/* Footer */}
        <div className="-mx-1 border-t border-kumo-fill pt-2 text-xs text-kumo-subtle">
          Showing {filtered.length} of {ORIGINS.length}
        </div>
      </LayerCard.Primary>
    </LayerCard>
  );
}
```

### [Test IDs](#test-ids)

`LayerCard.Primary` and `LayerCard.Secondary` accept all standard HTML attributes, including `data-testid` for testing.

```
import { LayerCard } from "@cloudflare/kumo";

/** Pass HTML attributes like `data-testid` to `Primary` and `Secondary` for testing. */
export function LayerCardTestIdDemo() {
  return (
    <LayerCard className="w-[250px]">
      <LayerCard.Secondary data-testid="card-header">
        Getting Started
      </LayerCard.Secondary>
      <LayerCard.Primary data-testid="card-body">
        <p className="text-sm text-kumo-subtle">
          Quick start guide for new users
        </p>
      </LayerCard.Primary>
    </LayerCard>
  );
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| render | `ReactNode` | \- | Allows you to replace the component's HTML element with a different tag, or compose it with another component. Accepts a \`ReactElement\` or a function that returns the element to render. |
| children | `ReactNode` | \- | \- |
| className | `string` | \- | \- |
| id | `string` | \- | \- |
| lang | `string` | \- | \- |
| title | `string` | \- | \- |