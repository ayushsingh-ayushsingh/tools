# Meter

A progress/percentage meter component for displaying numeric values within a known range.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/meter/meter.tsx)

---

```
import { Meter } from "@cloudflare/kumo";

export function MeterBasicDemo() {
  return <Meter label="Storage used" value={65} />;
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Meter } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Meter } from "@cloudflare/kumo/components/meter";
```

## [Usage](#usage)

```
import { Meter } from "@cloudflare/kumo";

export default function Example() {
  return <Meter label="Storage used" value={65} />;
}
```

## [Examples](#examples)

### [Basic Meter](#basic-meter)

The default meter displays a label and percentage value.

```
import { Meter } from "@cloudflare/kumo";

export function MeterBasicDemo() {
  return <Meter label="Storage used" value={65} />;
}
```

### [Custom Value Display](#custom-value-display)

Use `customValue` to show a custom string instead of the percentage.

```
import { Meter } from "@cloudflare/kumo";

export function MeterCustomValueDemo() {
  return <Meter label="API requests" value={75} customValue="750 / 1,000" />;
}
```

### [Hidden Value](#hidden-value)

Set `showValue={false}` to hide the value display.

```
import { Meter } from "@cloudflare/kumo";

export function MeterHiddenValueDemo() {
  return <Meter label="Progress" value={40} showValue={false} />;
}
```

### [Full Meter](#full-meter)

A meter at 100% capacity.

```
import { Meter } from "@cloudflare/kumo";

export function MeterFullDemo() {
  return <Meter label="Quota reached" value={100} />;
}
```

### [Low Value](#low-value)

A meter with a low value.

```
import { Meter } from "@cloudflare/kumo";

export function MeterLowDemo() {
  return <Meter label="Memory usage" value={15} />;
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| customValue | `string` | \- | Custom formatted value text (e.g. "750 / 1,000") displayed instead of percentage. |
| label\* | `string` | \- | Label text displayed above the meter track. |
| showValue | `boolean` | \- | Whether to display the percentage value next to the label. |
| trackClassName | `string` | \- | Additional CSS classes for the track (background bar). |
| indicatorClassName | `string` | \- | Additional CSS classes for the indicator (filled bar). |
| value | `number` | \- | Current value of the meter |
| max | `number` | \- | Maximum value of the meter (default: 100) |
| min | `number` | \- | Minimum value of the meter (default: 0) |