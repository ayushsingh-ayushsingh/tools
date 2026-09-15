# CloudflareLogo

Official Cloudflare logo component with glyph and full logo variants.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/cloudflare-logo/cloudflare-logo.tsx)

---

```
import { CloudflareLogo } from "@cloudflare/kumo";

export function CloudflareLogoBasicDemo() {
  return <CloudflareLogo className="w-72" />;
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import {
  CloudflareLogo,
  PoweredByCloudflare,
  generateCloudflareLogoSvg,
} from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import {
  CloudflareLogo,
  PoweredByCloudflare,
  generateCloudflareLogoSvg,
} from "@cloudflare/kumo/components/cloudflare-logo";
```

## [Usage](#usage)

```
import { CloudflareLogo } from "@cloudflare/kumo";

export default function Example() {
  return <CloudflareLogo className="w-36" />;
}
```

## [Examples](#examples)

### [Glyph Only](#glyph-only)

Use `variant=“glyph”` to display just the cloud icon without the wordmark.

```
import { CloudflareLogo } from "@cloudflare/kumo";

export function CloudflareLogoGlyphDemo() {
  return <CloudflareLogo variant="glyph" className="w-24" />;
}
```

### [Color Variants](#color-variants)

The logo supports three color schemes: brand colors, black, and white.

```
import { CloudflareLogo } from "@cloudflare/kumo";

export function CloudflareLogoColorVariantsDemo() {
  return (
    <div className="flex flex-wrap items-center gap-8">
      <CloudflareLogo className="w-28" color="color" />
      <div className="rounded-lg bg-white p-4">
        <CloudflareLogo className="w-28" color="black" />
      </div>
      <div className="rounded-lg bg-black p-4">
        <CloudflareLogo className="w-28" color="white" />
      </div>
    </div>
  );
}
```

### [Glyph Color Variants](#glyph-color-variants)

```
import { CloudflareLogo } from "@cloudflare/kumo";

export function CloudflareLogoGlyphVariantsDemo() {
  return (
    <div className="flex flex-wrap items-center gap-8">
      <CloudflareLogo variant="glyph" className="w-12" color="color" />
      <div className="rounded-lg bg-white p-4">
        <CloudflareLogo variant="glyph" className="w-12" color="black" />
      </div>
      <div className="rounded-lg bg-black p-4">
        <CloudflareLogo variant="glyph" className="w-12" color="white" />
      </div>
    </div>
  );
}
```

### [Sizing](#sizing)

Size the logo using CSS width classes. The height adjusts automatically to maintain aspect ratio.

```
import { CloudflareLogo } from "@cloudflare/kumo";

export function CloudflareLogoSizesDemo() {
  return (
    <div className="flex flex-wrap items-end gap-6">
      <CloudflareLogo className="w-20" />
      <CloudflareLogo className="w-28" />
      <CloudflareLogo className="w-44" />
    </div>
  );
}
```

### [Brand Assets Menu](#brand-assets-menu)

Combine with DropdownMenu to create a brand assets menu. Use `generateCloudflareLogoSvg()` to get copy-paste ready SVG markup.

```
import { useState } from "react";
import { CloudflareLogo, DropdownMenu, generateCloudflareLogoSvg } from "@cloudflare/kumo";
import { CloudIcon, CodeIcon, DownloadSimpleIcon, ArrowSquareOutIcon } from "@phosphor-icons/react";

export function CloudflareLogoCopyDemo() {
  const [copied, setCopied] = useState<string | null>(null);

  const copyToClipboard = async (text: string, label: string) => {
    await navigator.clipboard.writeText(text);
    setCopied(label);
    setTimeout(() => setCopied(null), 2000);
  };

  return (
    <div className="flex items-center gap-4">
      <DropdownMenu>
        <DropdownMenu.Trigger>
          <button
            type="button"
            className="flex items-center gap-2 rounded-lg bg-black px-4 py-3 text-white transition-opacity hover:opacity-80"
          >
            <CloudflareLogo variant="glyph" color="white" className="w-8" />
            <span className="font-medium">Logo</span>
          </button>
        </DropdownMenu.Trigger>
        <DropdownMenu.Content>
          <DropdownMenu.Item
            icon={CloudIcon}
            onClick={() =>
              copyToClipboard(
                generateCloudflareLogoSvg({ variant: "glyph" }),
                "glyph",
              )
            }
          >
            {copied === "glyph" ? "Copied!" : "Copy logo as SVG"}
          </DropdownMenu.Item>
          <DropdownMenu.Item
            icon={CodeIcon}
            onClick={() =>
              copyToClipboard(
                generateCloudflareLogoSvg({ variant: "full" }),
                "full",
              )
            }
          >
            {copied === "full" ? "Copied!" : "Copy full logo as SVG"}
          </DropdownMenu.Item>
          <DropdownMenu.Item
            icon={DownloadSimpleIcon}
            onClick={() =>
              window.open(
                "https://www.cloudflare.com/press-kit/",
                "_blank",
                "noopener",
              )
            }
          >
            Download brand assets
          </DropdownMenu.Item>
          <DropdownMenu.Separator />
          <DropdownMenu.Item
            icon={ArrowSquareOutIcon}
            onClick={() =>
              window.open(
                "https://www.cloudflare.com/brand-assets/",
                "_blank",
                "noopener",
              )
            }
          >
            Visit brand guidelines
          </DropdownMenu.Item>
        </DropdownMenu.Content>
      </DropdownMenu>

      <span className="text-sm text-kumo-subtle">
        Click to open the brand assets menu
      </span>
    </div>
  );
}
```

## [PoweredByCloudflare](#poweredbycloudflare)

A pre-built “Powered by Cloudflare” badge component for footers and attribution.

### [Basic Usage](#basic-usage)

```
import { PoweredByCloudflare } from "@cloudflare/kumo";

// =============================================================================
// PoweredByCloudflare Demos
// =============================================================================

export function PoweredByCloudflareBasicDemo() {
  return <PoweredByCloudflare />;
}
```

### [Color Variants](#color-variants-1)

```
import { PoweredByCloudflare } from "@cloudflare/kumo";

export function PoweredByCloudflareVariantsDemo() {
  return (
    <div className="flex flex-wrap items-center gap-4">
      <PoweredByCloudflare />
      <PoweredByCloudflare color="black" />
      <div className="rounded-lg bg-black p-3">
        <PoweredByCloudflare color="white" />
      </div>
    </div>
  );
}
```

### [Footer Example](#footer-example)

```
import { PoweredByCloudflare } from "@cloudflare/kumo";

export function PoweredByCloudflareFooterDemo() {
  return (
    <footer className="flex w-full items-center justify-between rounded-lg border border-kumo-hairline bg-kumo-elevated px-6 py-4">
      <span className="text-sm text-kumo-subtle">
        &copy; 2026 Your Company. All rights reserved.
      </span>
      <PoweredByCloudflare />
    </footer>
  );
}
```

## [SVG Generation](#svg-generation)

Use `generateCloudflareLogoSvg()` to get copy-paste ready SVG markup for non-React contexts.

```
import { generateCloudflareLogoSvg } from "@cloudflare/kumo";

// Generate glyph SVG (cloud only)
const glyphSvg = generateCloudflareLogoSvg({ variant: "glyph" });

// Generate full logo SVG
const fullSvg = generateCloudflareLogoSvg({ variant: "full" });

// Generate black logo
const blackSvg = generateCloudflareLogoSvg({ color: "black" });

// Copy to clipboard
await navigator.clipboard.writeText(
  generateCloudflareLogoSvg({ variant: "glyph", color: "color" }),
);
```

## [API Reference](#api-reference)

CloudflareLogo extends `SVGSVGElement` and accepts all standard SVG attributes.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| variant | ”glyph” | “full" | "full” | Logo variant. `glyph` shows just the cloud icon, `full` includes the wordmark. |
| color | ”color” | “black” | “white" | "color” | Color scheme. `color` uses brand colors, `black` and `white` are solid. |
| className | string | \- | CSS classes for sizing (e.g., `w-36`). Height adjusts automatically. |

### [PoweredByCloudflare](#poweredbycloudflare-1)

Extends `HTMLAnchorElement` and accepts all standard anchor attributes.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| color | ”color” | “black” | “white" | "color” | Color scheme for the logo and text. |
| href | string | ”[https://www.cloudflare.com](https://www.cloudflare.com)” | Link destination. Opens in a new tab by default. |