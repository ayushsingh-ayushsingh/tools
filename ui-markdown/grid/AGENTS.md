# Grid

A responsive grid layout component for organizing content into columns.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/grid/grid.tsx)

---

```
import { Grid, GridItem, Surface, Text } from "@cloudflare/kumo";

export function GridDemo() {
  return (
    <Grid variant="2up" gap="base">
      <GridItem>
        <Surface className="rounded-lg p-4">
          <Text bold>Item 1</Text>
          <div className="mt-1">
            <Text variant="secondary">First grid item</Text>
          </div>
        </Surface>
      </GridItem>
      <GridItem>
        <Surface className="rounded-lg p-4">
          <Text bold>Item 2</Text>
          <div className="mt-1">
            <Text variant="secondary">Second grid item</Text>
          </div>
        </Surface>
      </GridItem>
    </Grid>
  );
}
```

## [Installation](#installation)

```
import { Grid, GridItem } from "@cloudflare/kumo";
```

## [Grid Variants](#grid-variants)

The Grid component supports multiple column layouts that adapt responsively across breakpoints.

```
import { Grid, GridItem, Surface, Text } from "@cloudflare/kumo";

export function GridVariantsDemo() {
  return (
    <div className="flex flex-col gap-8">
      <div>
        <p className="mb-2 text-kumo-subtle">variant="2up"</p>
        <Grid variant="2up" gap="sm">
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>1</Text>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>2</Text>
            </Surface>
          </GridItem>
        </Grid>
      </div>

      <div>
        <p className="mb-2 text-kumo-subtle">variant="3up"</p>
        <Grid variant="3up" gap="sm">
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>1</Text>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>2</Text>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>3</Text>
            </Surface>
          </GridItem>
        </Grid>
      </div>

      <div>
        <p className="mb-2 text-kumo-subtle">variant="4up"</p>
        <Grid variant="4up" gap="sm">
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>1</Text>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>2</Text>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>3</Text>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>4</Text>
            </Surface>
          </GridItem>
        </Grid>
      </div>
    </div>
  );
}
```

## [Asymmetric Layouts](#asymmetric-layouts)

Use asymmetric variants for sidebar/main content layouts.

```
import { Grid, GridItem, Surface, Text } from "@cloudflare/kumo";

export function GridAsymmetricDemo() {
  return (
    <div className="flex flex-col gap-8">
      <div>
        <p className="mb-2 text-kumo-subtle">variant="2-1" (66% / 33%)</p>
        <Grid variant="2-1" gap="sm">
          <GridItem>
            <Surface className="rounded-lg p-4">
              <Text bold>Main Content</Text>
              <div className="mt-1">
                <Text variant="secondary">Two-thirds width</Text>
              </div>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4">
              <Text bold>Sidebar</Text>
              <div className="mt-1">
                <Text variant="secondary">One-third width</Text>
              </div>
            </Surface>
          </GridItem>
        </Grid>
      </div>

      <div>
        <p className="mb-2 text-kumo-subtle">variant="1-2" (33% / 66%)</p>
        <Grid variant="1-2" gap="sm">
          <GridItem>
            <Surface className="rounded-lg p-4">
              <Text bold>Sidebar</Text>
              <div className="mt-1">
                <Text variant="secondary">One-third width</Text>
              </div>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4">
              <Text bold>Main Content</Text>
              <div className="mt-1">
                <Text variant="secondary">Two-thirds width</Text>
              </div>
            </Surface>
          </GridItem>
        </Grid>
      </div>
    </div>
  );
}
```

## [Gap Sizes](#gap-sizes)

Control the spacing between grid items with the gap prop.

```
import { Grid, GridItem, Surface, Text } from "@cloudflare/kumo";

export function GridGapDemo() {
  return (
    <div className="flex flex-col gap-8">
      <div>
        <p className="mb-2 text-kumo-subtle">gap="none"</p>
        <Grid variant="side-by-side" gap="none">
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>1</Text>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>2</Text>
            </Surface>
          </GridItem>
        </Grid>
      </div>

      <div>
        <p className="mb-2 text-kumo-subtle">gap="sm"</p>
        <Grid variant="side-by-side" gap="sm">
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>1</Text>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>2</Text>
            </Surface>
          </GridItem>
        </Grid>
      </div>

      <div>
        <p className="mb-2 text-kumo-subtle">
          gap="base" (default, responsive)
        </p>
        <Grid variant="side-by-side" gap="base">
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>1</Text>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>2</Text>
            </Surface>
          </GridItem>
        </Grid>
      </div>

      <div>
        <p className="mb-2 text-kumo-subtle">gap="lg"</p>
        <Grid variant="side-by-side" gap="lg">
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>1</Text>
            </Surface>
          </GridItem>
          <GridItem>
            <Surface className="rounded-lg p-4 text-center">
              <Text>2</Text>
            </Surface>
          </GridItem>
        </Grid>
      </div>
    </div>
  );
}
```

## [Mobile Dividers](#mobile-dividers)

Add dividers between items on mobile with the mobileDivider prop (only works with the 4up variant).

```
import { Grid, GridItem, Surface, Text } from "@cloudflare/kumo";

export function GridMobileDividerDemo() {
  return (
    <Grid variant="4up" gap="base" mobileDivider>
      <GridItem>
        <Surface className="rounded-lg p-4">
          <Text bold>Item 1</Text>
          <div className="mt-1">
            <Text variant="secondary">Has divider on mobile</Text>
          </div>
        </Surface>
      </GridItem>
      <GridItem>
        <Surface className="rounded-lg p-4">
          <Text bold>Item 2</Text>
          <div className="mt-1">
            <Text variant="secondary">Has divider on mobile</Text>
          </div>
        </Surface>
      </GridItem>
      <GridItem>
        <Surface className="rounded-lg p-4">
          <Text bold>Item 3</Text>
          <div className="mt-1">
            <Text variant="secondary">Has divider on mobile</Text>
          </div>
        </Surface>
      </GridItem>
      <GridItem>
        <Surface className="rounded-lg p-4">
          <Text bold>Item 4</Text>
          <div className="mt-1">
            <Text variant="secondary">Has divider on mobile</Text>
          </div>
        </Surface>
      </GridItem>
    </Grid>
  );
}
```

## [All Variants](#all-variants)

Reference for all available grid variants:

| Variant | Description |
| --- | --- |
| `2up` | 1 column mobile, 2 columns medium+ |
| `side-by-side` | Always 2 columns |
| `2-1` | 66%/33% split on medium+ |
| `1-2` | 33%/66% split on medium+ |
| `1-3up` | 1 column mobile, 3 columns large+ |
| `3up` | 1 mobile, 2 medium, 3 large |
| `4up` | Progressive: 1 → 2 → 3 → 4 columns |
| `6up` | 2 mobile, up to 6 on XL |
| `1-2-4up` | 1 mobile, 2 medium, 4 large |

## [API Reference](#api-reference)

### [Grid](#grid)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | `ReactNode` | \- | Grid items to render. |
| className | `string` | \- | Additional CSS classes merged via \`cn()\`. |
| id | `string` | \- | \- |
| lang | `string` | \- | \- |
| title | `string` | \- | \- |
| mobileDivider | `boolean` | \- | Show dividers between grid items on mobile (only works with \`"4up"\` variant). |
| gap | `"none" | "sm" | "base" | "lg"` | `"base"` | Gap size between grid items. - \`"none"\` — No gap - \`"sm"\` — 12px gap - \`"base"\` — Responsive gap (8px → 24px → 32px) - \`"lg"\` — 32px gap |
| variant | `"2up" | "side-by-side" | "2-1" | "1-2" | "1-3up" | "3up" | "4up" | "6up" | "1-2-4up"` | \- | Responsive column layout variant. - \`"2up"\` — 1 col → 2 cols at md - \`"side-by-side"\` — Always 2 cols - \`"2-1"\` — 66%/33% split at md - \`"1-2"\` — 33%/66% split at md - \`"3up"\` — 1 → 2 → 3 cols - \`"4up"\` — 1 → 2 → 3 → 4 cols - \`"6up"\` — 2 → 3 → 4 → 6 cols - \`"1-2-4up"\` — 1 → 2 → 4 cols |

### [GridItem](#griditem)

GridItem is a wrapper component for grid children. It accepts standard div props including `className` and `children`.