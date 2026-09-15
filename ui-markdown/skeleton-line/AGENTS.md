# Skeleton Line

A skeleton loading placeholder for text content.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/primitives/skeleton-line/skeleton-line.tsx)

---

```
import { SkeletonLine } from "@cloudflare/kumo";

export function SkeletonLineDemo() {
  return (
    <div className="flex w-64 flex-col gap-3">
      <SkeletonLine />
      <SkeletonLine />
      <SkeletonLine />
    </div>
  );
}
```

## [Installation](#installation)

```
import { SkeletonLine } from "@cloudflare/kumo";
```

## [Custom Widths](#custom-widths)

Control the randomized width range for more natural-looking skeletons.

```
import { SkeletonLine } from "@cloudflare/kumo";

export function SkeletonLineWidthDemo() {
  return (
    <div className="flex w-64 flex-col gap-3">
      <SkeletonLine minWidth={80} maxWidth={100} />
      <SkeletonLine minWidth={60} maxWidth={80} />
      <SkeletonLine minWidth={40} maxWidth={60} />
    </div>
  );
}
```

## [Custom Height](#custom-height)

Override the default height using Tailwind utility classes via `className`. The default height is `0.5rem`.

```
import { SkeletonLine } from "@cloudflare/kumo";

export function SkeletonLineHeightDemo() {
  return (
    <div className="flex w-64 flex-col gap-3">
      <SkeletonLine className="h-2" />
      <SkeletonLine className="h-4" />
      <SkeletonLine className="h-6" />
      <SkeletonLine className="h-8" />
    </div>
  );
}
```

## [Block Height](#block-height)

Use `blockHeight` to set the height of a container that vertically centers the skeleton line. Useful when replacing text of a known line height. Accepts a number (treated as `px`) or any CSS string value.

```
import { SkeletonLine } from "@cloudflare/kumo";
import { ReactNode } from "react";

function DemoWrapper({
  label,
  children,
}: {
  label: string;
  children: ReactNode;
}) {
  return (
    <div className="relative">
      <div className="absolute top-0 right-full bottom-0 mr-2 flex items-center border-r-2 border-kumo-fill pr-2 text-sm">
        {label}
      </div>
      {children}
    </div>
  );
}

export function SkeletonLineBlockHeightDemo() {
  return (
    <div className="flex w-64 flex-col gap-1">
      <DemoWrapper label="32px">
        <SkeletonLine blockHeight={32} />
      </DemoWrapper>
      <DemoWrapper label="48px">
        <SkeletonLine blockHeight={48} />
      </DemoWrapper>
      <DemoWrapper label="64px">
        <SkeletonLine blockHeight={64} />
      </DemoWrapper>
    </div>
  );
}
```

## [Card Loading State](#card-loading-state)

Use skeleton lines to create loading states for cards and content areas.

```
import { SkeletonLine } from "@cloudflare/kumo";

export function SkeletonLineCardDemo() {
  return (
    <div className="w-64 rounded-lg p-4 ring ring-kumo-hairline">
      <div className="mb-4 h-4">
        <SkeletonLine minWidth={40} maxWidth={60} />
      </div>
      <div className="flex flex-col gap-2">
        <SkeletonLine />
        <SkeletonLine />
        <SkeletonLine minWidth={50} maxWidth={70} />
      </div>
    </div>
  );
}
```

## [API Reference](#api-reference)

| Prop | Type | Default |
| --- | --- | --- |
| minWidth | number | 30 |
| maxWidth | number | 100 |
| minDuration | number | 1.3 |
| maxDuration | number | 1.7 |
| minDelay | number | 0 |
| maxDelay | number | 0.5 |
| blockHeight | string | number | \- |
| className | string | \- |