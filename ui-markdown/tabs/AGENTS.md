# Tabs

A set of layered sections of content, known as tab panels, displayed one at a time.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/tabs/tabs.tsx)

---

```
import { Tabs } from "@cloudflare/kumo";

export function TabsDefaultDemo() {
  return (
    <div className="flex flex-col items-start gap-6">
      <div>
        <p className="mb-2 text-sm text-kumo-subtle">Segmented (default)</p>
        <Tabs
          variant="segmented"
          tabs={[
            { value: "tab1", label: "Tab 1" },
            { value: "tab2", label: "Tab 2" },
            { value: "tab3", label: "Tab 3" },
          ]}
          selectedValue="tab1"
        />
      </div>
      <div>
        <p className="mb-2 text-sm text-kumo-subtle">Underline</p>
        <Tabs
          variant="underline"
          tabs={[
            { value: "tab1", label: "Tab 1" },
            { value: "tab2", label: "Tab 2" },
            { value: "tab3", label: "Tab 3" },
          ]}
          selectedValue="tab1"
        />
      </div>
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Tabs } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Tabs } from "@cloudflare/kumo/components/tabs";
```

## [Usage](#usage)

```
import { Tabs } from "@cloudflare/kumo";

export default function Example() {
  return (
    <Tabs
      tabs={[
        { value: "overview", label: "Overview" },
        { value: "settings", label: "Settings" },
      ]}
      selectedValue="overview"
    />
  );
}
```

## [Examples](#examples)

### [Variants](#variants)

#### [Segmented (Default)](#segmented-default)

A pill-shaped indicator slides between tabs on a subtle background.

```
import { Tabs } from "@cloudflare/kumo";

export function TabsSegmentedDemo() {
  return (
    <Tabs
      variant="segmented"
      tabs={[
        { value: "tab1", label: "Tab 1" },
        { value: "tab2", label: "Tab 2" },
        { value: "tab3", label: "Tab 3" },
      ]}
      selectedValue="tab1"
    />
  );
}
```

#### [Underline](#underline)

A bottom border with a primary-colored indicator. The active tab has bolder text for emphasis.

```
import { Tabs } from "@cloudflare/kumo";

export function TabsUnderlineDemo() {
  return (
    <Tabs
      variant="underline"
      tabs={[
        { value: "tab1", label: "Tab 1" },
        { value: "tab2", label: "Tab 2" },
        { value: "tab3", label: "Tab 3" },
      ]}
      selectedValue="tab1"
    />
  );
}
```

### [Small Size](#small-size)

Use `size="sm"` for a compact tab bar that matches `Input size="sm"` height (h-6.5 / 26px). Useful inside toolbars and filter rows.

```
import { Tabs } from "@cloudflare/kumo";

export function TabsSmDemo() {
  return (
    <div className="flex flex-col items-start gap-6">
      <div>
        <p className="mb-2 text-sm text-kumo-subtle">Segmented sm</p>
        <Tabs
          variant="segmented"
          size="sm"
          tabs={[
            { value: "tab1", label: "Tab 1" },
            { value: "tab2", label: "Tab 2" },
            { value: "tab3", label: "Tab 3" },
          ]}
          selectedValue="tab1"
        />
      </div>
      <div>
        <p className="mb-2 text-sm text-kumo-subtle">Underline sm</p>
        <Tabs
          variant="underline"
          size="sm"
          tabs={[
            { value: "tab1", label: "Tab 1" },
            { value: "tab2", label: "Tab 2" },
            { value: "tab3", label: "Tab 3" },
          ]}
          selectedValue="tab1"
        />
      </div>
    </div>
  );
}
```

### [Controlled](#controlled)

Use the `value` and `onValueChange` props for controlled state.

```
import { useState } from "react";
import { Tabs } from "@cloudflare/kumo";

export function TabsControlledDemo() {
  const [activeTab, setActiveTab] = useState("tab1");

  return (
    <div className="space-y-4">
      <Tabs
        tabs={[
          { value: "tab1", label: "Tab 1" },
          { value: "tab2", label: "Tab 2" },
          { value: "tab3", label: "Tab 3" },
        ]}
        value={activeTab}
        onValueChange={setActiveTab}
      />
      <p className="text-sm text-kumo-subtle">
        Active tab: <code className="text-sm">{activeTab}</code>
      </p>
    </div>
  );
}
```

### [Many Tabs](#many-tabs)

Tabs automatically scroll horizontally when there are many items.

```
import { Tabs } from "@cloudflare/kumo";

export function TabsManyDemo() {
  return (
    <div className="w-full max-w-md">
      <Tabs
        tabs={[
          { value: "overview", label: "Overview" },
          { value: "analytics", label: "Analytics" },
          { value: "reports", label: "Reports" },
          { value: "notifications", label: "Notifications" },
          { value: "settings", label: "Settings" },
          { value: "billing", label: "Billing" },
          { value: "security", label: "Security" },
          { value: "integrations", label: "Integrations" },
        ]}
        selectedValue="overview"
      />
    </div>
  );
}
```

### [Horizontal Overflow](#horizontal-overflow)

When segmented tabs overflow their container, scroll buttons appear at the clipped edge. Use them, horizontal scrolling, or mouse drag to reveal off-screen tabs.

```
import { Tabs } from "@cloudflare/kumo";

export function TabsOverflowDemo() {
  return (
    <div className="w-full max-w-xs">
      <Tabs
        tabs={[
          { value: "overview", label: "Overview" },
          { value: "analytics", label: "Analytics" },
          { value: "reports", label: "Reports" },
          { value: "notifications", label: "Notifications" },
          { value: "settings", label: "Settings" },
          { value: "billing", label: "Billing" },
          { value: "security", label: "Security" },
          { value: "integrations", label: "Integrations" },
        ]}
        selectedValue="overview"
      />
    </div>
  );
}
```

### [Dynamic Tab Count](#dynamic-tab-count)

This example toggles between an overflowing tab set and the production-like seven-tab set. When the extra tabs disappear, the end overflow control should hide once the remaining tabs fit.

```
import { useState } from "react";
import { Tabs } from "@cloudflare/kumo";

export function TabsDynamicCountDemo() {
  const [showExtraTabs, setShowExtraTabs] = useState(true);
  const tabs = showExtraTabs
    ? [...productionLikeTabs, ...productionLikeExtraTabs]
    : productionLikeTabs;

  return (
    <div className="space-y-3">
      <div className="w-full max-w-[588px]">
        <Tabs tabs={tabs} selectedValue="settings" />
      </div>
      <div className="flex items-center gap-3 text-sm text-kumo-subtle">
        <button
          type="button"
          className="rounded-md border border-kumo-line bg-kumo-base px-2.5 py-1 text-kumo-default hover:bg-kumo-tint focus:ring-2 focus:ring-kumo-brand focus:outline-none"
          onClick={() => setShowExtraTabs((current) => !current)}
        >
          Toggle extra tabs
        </button>
        <span>{showExtraTabs ? "10 tabs" : "7 tabs"}</span>
      </div>
    </div>
  );
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| tabs | `TabsItem[]` | \- | Array of tab items to render. |
| value | `string` | \- | Controlled value. When set, component becomes controlled. |
| selectedValue | `string` | \- | Default selected value for uncontrolled mode. Ignored when \`value\` is set. |
| activateOnFocus | `boolean` | \- | When \`true\`, tabs are activated immediately upon receiving focus via arrow keys. When \`false\` (default), tabs receive focus but require Enter/Space to activate. |
| className | `string` | \- | Additional CSS classes for the root element. |
| listClassName | `string` | \- | Additional CSS classes for the tab list element. |
| indicatorClassName | `string` | \- | Additional CSS classes for the indicator element. |
| labels | `TabsLabels` | \- | Labels for internationalization of aria-labels. All labels have English defaults. |
| variant | `"segmented" | "underline"` | `"segmented"` | Tab style. - \`"segmented"\` — Pill-shaped indicator on a filled track - \`"underline"\` — Underline indicator below tab text |
| size | `"base" | "sm"` | `"base"` | Tab size. - \`"base"\` — Default size (h-9, text-base) - \`"sm"\` — Compact size (h-6.5, text-xs) — matches Input size="sm" |
| onValueChange | `(value: string) => void` | \- | Callback when active tab changes |

### [TabsItem](#tabsitem)

| Property | Type | Required |
| --- | --- | --- |
| value | string | Yes |
| label | ReactNode | Yes |
| className | string | No |
| render | TabsTab.Props\[“render”\] | No |
| nativeButton | boolean | No |