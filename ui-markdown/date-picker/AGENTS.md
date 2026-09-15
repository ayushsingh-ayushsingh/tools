# DatePicker

A date selection calendar supporting single, multiple, and range selection modes.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/date-picker/date-picker.tsx)

---

```
import { useState } from "react";
import { DatePicker } from "@cloudflare/kumo";

/**
 * Single date selection.
 */
export function DatePickerSingleDemo() {
  const [date, setDate] = useState<Date | undefined>();

  return (
    <div className="flex flex-col gap-4">
      <DatePicker
        mode="single"
        selected={date}
        onChange={(d) => {
          if (d) {
            setDate(d);
          }
        }}
      />
      <p className="text-sm text-kumo-subtle">
        Selected: {date ? date.toLocaleDateString() : "None"}
      </p>
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { DatePicker, type DateRange } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import {
  DatePicker,
  type DateRange,
} from "@cloudflare/kumo/components/date-picker";
```

## [Usage](#usage)

DatePicker supports three selection modes: `single`, `multiple`, and `range`.

```
import { useState } from "react";
import { DatePicker } from "@cloudflare/kumo";

export default function Example() {
  const [date, setDate] = useState<Date>();

  return <DatePicker mode="single" selected={date} onChange={setDate} />;
}
```

## [Examples](#examples)

### [Single Date Selection](#single-date-selection)

Select a single date. The most common use case for date pickers.

```
import { useState } from "react";
import { DatePicker } from "@cloudflare/kumo";

/**
 * Single date selection.
 */
export function DatePickerSingleDemo() {
  const [date, setDate] = useState<Date | undefined>();

  return (
    <div className="flex flex-col gap-4">
      <DatePicker
        mode="single"
        selected={date}
        onChange={(d) => {
          if (d) {
            setDate(d);
          }
        }}
      />
      <p className="text-sm text-kumo-subtle">
        Selected: {date ? date.toLocaleDateString() : "None"}
      </p>
    </div>
  );
}
```

### [Multiple Date Selection](#multiple-date-selection)

Select multiple individual dates. Use `max` to limit the number of selections.

```
import { useState } from "react";
import { DatePicker } from "@cloudflare/kumo";

/**
 * Multiple date selection with a maximum of 5 dates.
 */
export function DatePickerMultipleDemo() {
  const [dates, setDates] = useState<Date[] | undefined>();

  return (
    <div className="flex flex-col gap-4">
      <DatePicker
        mode="multiple"
        selected={dates}
        onChange={setDates}
        max={5}
      />
      <p className="text-sm text-kumo-subtle">
        Selected: {dates?.length ?? 0} date(s)
      </p>
    </div>
  );
}
```

### [Date Range Selection](#date-range-selection)

Select a continuous range of dates. Works well with `numberOfMonths={2}` for a side-by-side view.

```
import { useState } from "react";
import { DatePicker, DateRange } from "@cloudflare/kumo";

/**
 * Date range selection with two months displayed.
 */
export function DatePickerRangeDemo() {
  const [range, setRange] = useState<DateRange | undefined>();

  return (
    <div className="flex flex-col gap-4">
      <DatePicker
        mode="range"
        selected={range}
        onChange={setRange}
        numberOfMonths={2}
      />
      <p className="text-sm text-kumo-subtle">
        Range:{" "}
        {range?.from
          ? `${range.from.toLocaleDateString()} - ${range.to?.toLocaleDateString() ?? "..."}`
          : "None"}
      </p>
    </div>
  );
}
```

### [Range with Min/Max Constraints](#range-with-minmax-constraints)

Constrain the range length using `min` and `max` props (in days/nights).

```
import { useState } from "react";
import { DatePicker, DateRange } from "@cloudflare/kumo";

/**
 * Date range with minimum 3 nights and maximum 7 nights.
 */
export function DatePickerRangeMinMaxDemo() {
  const [range, setRange] = useState<DateRange | undefined>();

  return (
    <div className="flex flex-col gap-4">
      <DatePicker
        mode="range"
        selected={range}
        onChange={setRange}
        min={3}
        max={7}
        footer={
          <span className="text-xs text-kumo-subtle">Select 3-7 nights</span>
        }
      />
    </div>
  );
}
```

### [With Popover](#with-popover)

Compose with the [Popover](/components/popover) component to create a dropdown date picker.

```
import { useState } from "react";
import { DatePicker, Popover, Button } from "@cloudflare/kumo";
import { CalendarDotsIcon } from "@phosphor-icons/react";

/**
 * Date picker composed with a Popover for dropdown behavior.
 */
export function DatePickerPopoverDemo() {
  const [date, setDate] = useState<Date | undefined>();

  return (
    <Popover>
      <Popover.Trigger
        render={<Button variant="outline" icon={CalendarDotsIcon} />}
      >
        {date ? date.toLocaleDateString() : "Pick a date"}
      </Popover.Trigger>
      <Popover.Content className="p-3">
        <DatePicker mode="single" selected={date} onChange={setDate} />
      </Popover.Content>
    </Popover>
  );
}
```

### [Date Range with Popover](#date-range-with-popover)

A date range picker in a popover with two months displayed.

```
import { useState } from "react";
import { DatePicker, Popover, Button, DateRange } from "@cloudflare/kumo";
import { CalendarDotsIcon } from "@phosphor-icons/react";

/**
 * Date range picker composed with a Popover for dropdown behavior.
 */
export function DatePickerRangePopoverDemo() {
  const [range, setRange] = useState<DateRange | undefined>();

  const formatRange = () => {
    if (!range?.from) return "Select dates";
    if (!range.to) return range.from.toLocaleDateString();
    return `${range.from.toLocaleDateString()} – ${range.to.toLocaleDateString()}`;
  };

  return (
    <Popover>
      <Popover.Trigger
        render={<Button variant="outline" icon={CalendarDotsIcon} />}
      >
        {formatRange()}
      </Popover.Trigger>
      <Popover.Content className="p-3">
        <DatePicker
          mode="range"
          selected={range}
          onChange={setRange}
          numberOfMonths={2}
        />
      </Popover.Content>
    </Popover>
  );
}
```

### [Date Range with Presets](#date-range-with-presets)

Combine the date picker with preset options for quick selection.

```
import { useState } from "react";
import { DatePicker, Popover, Button, DateRange } from "@cloudflare/kumo";
import { CalendarDotsIcon } from "@phosphor-icons/react";

/**
 * Date range picker with preset options in a popover.
 */
export function DatePickerRangeWithPresetsDemo() {
  const [range, setRange] = useState<DateRange | undefined>();
  const [month, setMonth] = useState<Date>(new Date());

  const today = new Date();

  const presets = [
    {
      label: "Today",
      range: { from: today, to: today },
    },
    {
      label: "Last 7 days",
      range: {
        from: new Date(today.getTime() - 6 * 24 * 60 * 60 * 1000),
        to: today,
      },
    },
    {
      label: "Last 30 days",
      range: {
        from: new Date(today.getTime() - 29 * 24 * 60 * 60 * 1000),
        to: today,
      },
    },
    {
      label: "Last 90 days",
      range: {
        from: new Date(today.getTime() - 89 * 24 * 60 * 60 * 1000),
        to: today,
      },
    },
    {
      label: "This month",
      range: {
        from: new Date(today.getFullYear(), today.getMonth(), 1),
        to: new Date(today.getFullYear(), today.getMonth() + 1, 0),
      },
    },
    {
      label: "Last month",
      range: {
        from: new Date(today.getFullYear(), today.getMonth() - 1, 1),
        to: new Date(today.getFullYear(), today.getMonth(), 0),
      },
    },
  ];

  const handlePresetClick = (preset: { range: DateRange }) => {
    setRange(preset.range);
    // Navigate calendar to show the start of the range
    if (preset.range.from) {
      setMonth(preset.range.from);
    }
  };

  const isPresetActive = (preset: { range: DateRange }) => {
    if (!range?.from || !range?.to || !preset.range.from || !preset.range.to)
      return false;
    // Compare dates only (ignore time)
    const sameFrom =
      range.from.toDateString() === preset.range.from.toDateString();
    const sameTo = range.to.toDateString() === preset.range.to.toDateString();
    return sameFrom && sameTo;
  };

  const formatRange = () => {
    if (!range?.from) return "Select dates";
    if (!range.to) return range.from.toLocaleDateString();
    return `${range.from.toLocaleDateString()} – ${range.to.toLocaleDateString()}`;
  };

  return (
    <Popover>
      <Popover.Trigger
        render={<Button variant="outline" icon={CalendarDotsIcon} />}
      >
        {formatRange()}
      </Popover.Trigger>
      <Popover.Content className="p-0">
        <div className="flex">
          <div className="flex flex-col gap-1 border-r border-kumo-hairline p-2 text-sm">
            {presets.map((preset) => {
              const isActive = isPresetActive(preset);
              return (
                <button
                  key={preset.label}
                  type="button"
                  onClick={() => handlePresetClick(preset)}
                  className={`rounded-md px-3 py-1.5 text-left whitespace-nowrap ${
                    isActive
                      ? "bg-kumo-bg-inverse text-kumo-text-inverse"
                      : "text-kumo-subtle hover:bg-kumo-control"
                  }`}
                >
                  {preset.label}
                </button>
              );
            })}
          </div>
          <div className="p-3">
            <DatePicker
              mode="range"
              selected={range}
              onChange={setRange}
              month={month}
              onMonthChange={setMonth}
              numberOfMonths={2}
            />
          </div>
        </div>
      </Popover.Content>
    </Popover>
  );
}
```

### [Disabled Dates with Usage Limits](#disabled-dates-with-usage-limits)

Use the `disabled` prop to make certain dates unselectable, and `footer` to display usage information.

```
import { useState } from "react";
import { DatePicker } from "@cloudflare/kumo";

/**
 * Date picker with disabled dates and a footer showing usage limits.
 */
export function DatePickerDisabledWithFooterDemo() {
  const [dates, setDates] = useState<Date[] | undefined>();
  const today = new Date();

  // Example: some dates are already used/unavailable
  const unavailableDates = [
    new Date(today.getFullYear(), today.getMonth(), 5),
    new Date(today.getFullYear(), today.getMonth(), 12),
    new Date(today.getFullYear(), today.getMonth(), 18),
    new Date(today.getFullYear(), today.getMonth(), 25),
  ];

  const selectedCount = dates?.length ?? 0;
  const maxDays = 5;

  return (
    <DatePicker
      mode="multiple"
      selected={dates}
      onChange={setDates}
      max={maxDays}
      disabled={unavailableDates}
      fixedWeeks
      footer={
        <p className="w-full pt-2 text-xs text-kumo-subtle">
          {selectedCount}/{maxDays} days selected. Grayed dates are unavailable.
        </p>
      }
    />
  );
}
```

## [Full Popover Example](#full-popover-example)

Here’s a complete example showing how to compose DatePicker with Popover:

```
import { useState } from "react";
import { DatePicker, Popover, Button } from "@cloudflare/kumo";
import { CalendarDotsIcon } from "@phosphor-icons/react";

export function DatePickerDropdown() {
  const [date, setDate] = useState<Date>();

  return (
    <Popover>
      <Popover.Trigger
        render={<Button variant="outline" icon={CalendarDotsIcon} />}
      >
        {date ? date.toLocaleDateString() : "Pick a date"}
      </Popover.Trigger>
      <Popover.Content className="p-3">
        <DatePicker
          mode="single"
          selected={date}
          onChange={(d) => setDate(d)}
        />
      </Popover.Content>
    </Popover>
  );
}
```

## [API Reference](#api-reference)

DatePicker forwards all props to

[

react-day-picker

](https://daypicker.dev/api/interfaces/PropsBase)

. Key props include:

-   `mode` — `"single" | "multiple" | "range"` — Selection mode (required)
    
-   `selected` — Currently selected date(s)
-   `onChange` — Callback when selection changes
-   `numberOfMonths` — Number of months to display
-   `disabled` — Dates that cannot be selected
-   `min` / `max` — Min/max selection constraints
-   `footer` — Content rendered below the calendar
-   `locale` — date-fns locale for internationalization
-   `className` — Additional CSS classes

See the

[

react-day-picker documentation

](https://daypicker.dev/docs)

for the full API.

### [Differences from react-day-picker](#differences-from-react-day-picker)

For consistency with other Kumo form components, DatePicker uses `onChange` instead of react-day-picker’s `onSelect`. Full type inference is preserved — TypeScript will correctly narrow the callback signature based on the `mode` prop.