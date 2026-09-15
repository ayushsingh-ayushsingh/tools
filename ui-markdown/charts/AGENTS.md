# Charts

Charts built on ECharts.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/chart/chart.tsx)

---

Chart components are built on ECharts. Install it as a dependency:

```
npm install echarts
```

For optimal bundle size, import only the ECharts components you need. The examples below show the minimum required imports for our use cases.

```
import * as echarts from "echarts/core";
import { BarChart, LineChart, PieChart } from "echarts/charts";
import { useEffect, useMemo, useState } from "react";
import {
  AriaComponent,
  AxisPointerComponent,
  BrushComponent,
  GridComponent,
  MarkLineComponent,
  TooltipComponent,
} from "echarts/components";
import { CanvasRenderer } from "echarts/renderers";

echarts.use([
  BarChart,
  LineChart,
  PieChart,
  AxisPointerComponent,
  BrushComponent,
  GridComponent,
  MarkLineComponent,
  TooltipComponent,
  CanvasRenderer,
  AriaComponent,
]);
```

## [Available Charts](#available-charts)

Timeseries Chart

A specialized chart for displaying time-based data.

[Learn more](/charts/timeseries)

Custom Chart

Examples like pie charts.

[Learn more](/charts/custom)

## [Color System](#color-system)

Color Palette

Information about our color system.

[Learn more](/charts/colors)

## [Legend](#legend)

Use `LegendItem` to display chart series information with color indicators.

### [LargeItem](#largeitem)

```
import { ChartPalette, ChartLegend } from "@cloudflare/kumo";
import { useIsDarkMode } from "~/lib/use-is-dark-mode";

/**
 * Legend items with default variant showing semantic colors.
 */
export function LegendDefaultDemo() {
  const isDarkMode = useIsDarkMode();

  return (
    <div className="space-y-4">
      <h3 className="text-sm font-medium">Active State</h3>

      <div className="flex flex-wrap gap-4 divide-x divide-kumo-hairline">
        <ChartLegend.LargeItem
          name="Requests"
          color={ChartPalette.semantic("Neutral", isDarkMode)}
          value="1,234"
          unit="req/s"
        />
        <ChartLegend.LargeItem
          name="Storage"
          color={ChartPalette.semantic("Attention", isDarkMode)}
          value="56"
          unit="GB"
        />
        <ChartLegend.LargeItem
          name="Warnings"
          color={ChartPalette.semantic("Warning", isDarkMode)}
          value="128"
        />
      </div>

      <h3 className="mt-12 text-sm font-medium">Inactive State</h3>

      <div className="flex flex-wrap gap-4 divide-x divide-kumo-hairline">
        <ChartLegend.LargeItem
          name="Requests"
          color={ChartPalette.semantic("Neutral", isDarkMode)}
          value="1,234"
          unit="req/s"
          inactive
        />
        <ChartLegend.LargeItem
          name="Storage"
          color={ChartPalette.semantic("Attention", isDarkMode)}
          value="56"
          unit="GB"
          inactive
        />
        <ChartLegend.LargeItem
          name="Warnings"
          color={ChartPalette.semantic("Warning", isDarkMode)}
          value="128"
          inactive
        />
      </div>

      <h3 className="mt-12 text-sm font-medium">Loading state</h3>

      <div className="flex flex-wrap gap-4 divide-x divide-kumo-hairline">
        <ChartLegend.LargeItem loading />
      </div>
    </div>
  );
}
```

### [SmallItem](#smallitem)

```
import { ChartPalette, ChartLegend } from "@cloudflare/kumo";
import { useIsDarkMode } from "~/lib/use-is-dark-mode";

/**
 * Legend items with compact variant using categorical colors.
 */
export function LegendCompactDemo() {
  const isDarkMode = useIsDarkMode();

  return (
    <div className="space-y-4">
      <h3 className="text-sm font-medium">Active State</h3>
      <div className="flex flex-wrap gap-4">
        <ChartLegend.SmallItem
          name="Requests"
          color={ChartPalette.semantic("Neutral", isDarkMode)}
          value="1,234"
          unit="req/s"
        />
        <ChartLegend.SmallItem
          name="Storage"
          color={ChartPalette.semantic("Attention", isDarkMode)}
          value="56"
          unit="GB"
        />
        <ChartLegend.SmallItem
          name="Warnings"
          color={ChartPalette.semantic("Warning", isDarkMode)}
          value="128"
        />
      </div>

      <h3 className="mt-12 text-sm font-medium">Inactive State</h3>
      <div className="flex flex-wrap gap-4">
        <ChartLegend.SmallItem
          name="Requests"
          color={ChartPalette.semantic("Neutral", isDarkMode)}
          value="1,234"
          unit="req/s"
          inactive
        />
        <ChartLegend.SmallItem
          name="Storage"
          color={ChartPalette.semantic("Attention", isDarkMode)}
          value="56"
          unit="GB"
          inactive
        />
        <ChartLegend.SmallItem
          name="Warnings"
          color={ChartPalette.semantic("Warning", isDarkMode)}
          value="128"
          inactive
        />
      </div>

      <h3 className="mt-12 text-sm font-medium">Loading state</h3>

      <div className="flex flex-wrap gap-4">
        <ChartLegend.SmallItem loading />
      </div>
    </div>
  );
}
```

# Chart Colors

Semantic and categorical color tokens for Cloudflare dashboard charts.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/chart/Color.ts)

---

Chart colors in Kumo are split into three systems — **semantic** tokens for data with inherent polarity, a **categorical** palette for nominal series and a **sequential** scale for density encoding. Using the right system for the data type is the most important color decision in a chart.

## [Color systems](#color-systems)

Charts in the dashboard serve different jobs, so color is not “one-size-fits-all.” To avoid misreading data, we use different color systems based on the data task.

## [Semantic tokens](#semantic-tokens)

Semantic chart colors should be used when the data has inherent polarity, i.e. status, severity and health data. Semantic colors communicate to the user that this data needs their attention and an action might be required.

Semantic chart colors are derived from our existing badge/status semantic tokens so meaning stays consistent across components and contexts. We intentionally adjust hue/chroma for charts to be less visually aggressive than badges to reduce visual fatigue and false urgency.

## [Categorical palette](#categorical-palette)

Use the categorical palette when the data has no inherent polarity. The palette is ordered for maximum perceptual distance between adjacent slots to ensure it’s CVD friendly and the data is easily distinguishable.

We reduced categorical tokens from 16 (8 hues × 2 lightness variants) to 5 because most charts intentionally surface only top categories at once (commonly 5). When a chart needs more than 5 series it should cycle those tokens with modulo (color = tokens\[i % 5\]) for consistent, predictable styling.

Categorical colors are tested using a CVD simulator to ensure they remain distinguishable for users with color vision deficiency. Here’s an example of what the categorical colors might look like to someone with deuteranopia.

Color alone should not be used to convey information. When implementing line charts, ensure that you’re using patterns (e.g. dashes/dots) on top of the color palette to differentiate between data points. Since dots and dashes appear lighter, we avoid pairing them with light colors since those lines can fade out.

## [Sequential scale](#sequential-scale)

A 5-step single-hue scale for encoding **density** — use when a single metric varies in magnitude across a set of values and color intensity should reinforce that magnitude. Common uses: choropleth maps (traffic volume by country), heatmaps, and histogram fills. The sequential scale is not appropriate for categorical series differentiation — use the categorical palette for that.

Darker steps encode higher values in light mode; lighter steps encode higher values in dark mode so the most prominent color always corresponds to the highest magnitude.

# Custom Chart

Example charts using the Chart component.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/chart/chart.tsx)

---

## [Custom Chart](#custom-chart)

```
import { Chart } from "@cloudflare/kumo";
import * as echarts from "echarts/core";
import { EChartsOption } from "echarts";
import { useMemo } from "react";
import { useIsDarkMode } from "~/lib/use-is-dark-mode";

export function PieChartDemo() {
  const isDarkMode = useIsDarkMode();

  const options = useMemo<EChartsOption>(
    () => ({
      animation: true,
      animationDuration: 2000,
      tooltip: {
        show: true,
      },
      series: [
        {
          type: "pie",
          data: [
            { value: 101, name: "Series A" },
            { value: 202, name: "Series B" },
            { value: 303, name: "Series C" },
            { value: 404, name: "Series D" },
            { value: 505, name: "Series E" },
          ],
        },
      ],
    }),
    [],
  );

  return (
    <Chart
      echarts={echarts}
      options={options}
      height={400}
      isDarkMode={isDarkMode}
    />
  );
}
```

## [Custom Tooltip with HTML](#custom-tooltip-with-html)

For tooltips that require custom HTML formatting, use the `dangerousHtmlFormatter` property instead of the standard `formatter`. This makes the security implications more explicit.

When using `dangerousHtmlFormatter`, it is **strongly recommended** to sanitize any user-provided content using `echarts.format.encodeHTML` to prevent XSS vulnerabilities.

```
import { Chart } from "@cloudflare/kumo";
import * as echarts from "echarts/core";
import { EChartsOption } from "echarts";
import { useMemo } from "react";
import { useIsDarkMode } from "~/lib/use-is-dark-mode";

/**
 * Custom chart with HTML tooltip using dangerousHtmlFormatter.
 * USE WITH CAUTION: Only use dangerousHtmlFormatter for trusted HTML content.
 * Always sanitize any user-provided data using echarts.format.encodeHTML
 * or similar utilities to prevent XSS vulnerabilities.
 */
export function CustomTooltipChartDemo() {
  const isDarkMode = useIsDarkMode();

  const options = useMemo<EChartsOption>(
    () => ({
      tooltip: {
        trigger: "item",
        formatter: (params: any) => {
          // IMPORTANT: Always escape ALL dynamic values using encodeHTML
          // from echarts/format before including in HTML. This prevents
          // XSS attacks from malicious data like:
          // { name: "<img src=x onerror=alert('xss')>", value: "..." }
          const safeName = echarts.format.encodeHTML(params.name);
          const safeValue = echarts.format.encodeHTML(String(params.value));
          const safePercent = echarts.format.encodeHTML(
            String(Math.round(params.percent)),
          );

          return `
            <div style="padding: 8px;">
              <div style="font-weight: 600; margin-bottom: 4px;">${safeName}</div>
              <div>Value: <strong>${safeValue}</strong></div>
              <div style="font-size: 12px; opacity: 0.7; margin-top: 4px;">
                ${safePercent}% of total
              </div>
            </div>
          `;
        },
      },
      series: [
        {
          type: "pie",
          data: [
            { value: 101, name: "Series A" },
            { value: 202, name: "Series B" },
            // Malicious series name to demonstrate XSS protection via encodeHTML.
            // Without encoding, this would render an alert popup. With encodeHTML,
            // it safely displays as plain text.
            { value: 150, name: "<img src=x onerror=alert('XSS')>" },
            { value: 303, name: "Series C" },
            { value: 404, name: "Series D" },
          ],
        },
      ],
    }),
    [],
  );

  return (
    <Chart
      echarts={echarts}
      options={options}
      height={400}
      isDarkMode={isDarkMode}
    />
  );
}
```
