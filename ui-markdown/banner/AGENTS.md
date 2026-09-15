# Banner

Displays contextual inline messages for informational, alert, or error states.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/banner/banner.tsx)

---

```
import { Banner } from "@cloudflare/kumo";
import { Info, WarningCircle, Warning } from "@phosphor-icons/react";

/** Shows all banner variants with structured title and description. */
export function BannerVariantsDemo() {
  return (
    <div className="w-full space-y-3">
      <Banner
        icon={<Info weight="fill" />}
        title="Update available"
        description="A new version is ready to install."
      />
      <Banner
        icon={<Warning weight="fill" />}
        variant="alert"
        title="Session expiring"
        description="Your session will expire in 5 minutes."
      />
      <Banner
        icon={<WarningCircle weight="fill" />}
        variant="error"
        title="Save failed"
        description="We couldn't save your changes. Please try again."
      />
      <Banner
        icon={<Info weight="fill" />}
        variant="secondary"
        title="Maintenance scheduled"
        description="This service will be unavailable for 10 minutes."
      />
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Banner } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Banner } from "@cloudflare/kumo/components/banner";
```

## [Usage](#usage)

```
import { Banner } from "@cloudflare/kumo";
import { Info } from "@phosphor-icons/react";

export default function Example() {
  return (
    <Banner
      icon={<Info weight="fill" />}
      title="Update available"
      description="A new version is ready to install."
    />
  );
}
```

## [Examples](#examples)

### [Variants](#variants)

#### [Default](#default)

```
import { Banner } from "@cloudflare/kumo";
import { Info } from "@phosphor-icons/react";

/** Default informational banner with title and description. */
export function BannerDefaultDemo() {
  return (
    <Banner
      icon={<Info weight="fill" />}
      title="Update available"
      description="A new version is ready to install."
    />
  );
}
```

#### [Alert](#alert)

```
import { Banner } from "@cloudflare/kumo";
import { Warning } from "@phosphor-icons/react";

/** Alert banner for warnings that need attention. */
export function BannerAlertDemo() {
  return (
    <Banner
      icon={<Warning weight="fill" />}
      variant="alert"
      title="Session expiring"
      description="Your session will expire in 5 minutes."
    />
  );
}
```

#### [Error](#error)

```
import { Banner } from "@cloudflare/kumo";
import { WarningCircle } from "@phosphor-icons/react";

/** Error banner for critical issues. */
export function BannerErrorDemo() {
  return (
    <Banner
      icon={<WarningCircle weight="fill" />}
      variant="error"
      title="Save failed"
      description="We couldn't save your changes. Please try again."
    />
  );
}
```

#### [Secondary](#secondary)

```
import { Banner } from "@cloudflare/kumo";
import { Info } from "@phosphor-icons/react";

/** Neutral secondary banner for contextual messages. */
export function BannerSecondaryDemo() {
  return (
    <Banner
      icon={<Info weight="fill" />}
      variant="secondary"
      title="Maintenance scheduled"
      description="This service will be unavailable for 10 minutes."
    />
  );
}
```

### [With icon](#with-icon)

```
import { Banner } from "@cloudflare/kumo";
import { Warning } from "@phosphor-icons/react";

/** Banner with custom icon and structured content. */
export function BannerWithIconDemo() {
  return (
    <Banner
      icon={<Warning weight="fill" />}
      variant="alert"
      title="Review required"
      description="Please review your billing information before proceeding."
    />
  );
}
```

### [With action](#with-action)

```
import { Banner } from "@cloudflare/kumo";
import { Info, WarningCircle, X } from "@phosphor-icons/react";

/** Banner with action buttons: CTA and dismissable. */
export function BannerWithActionDemo() {
  return (
    <div className="w-full space-y-3">
      <Banner
        icon={<Info weight="fill" />}
        title="Update available"
        description="A new version is ready to install."
        action={
          <>
            <Banner.Action>Update</Banner.Action>
            <Banner.Action variant="ghost" icon={<X />} aria-label="Dismiss" />
          </>
        }
      />
      <Banner
        variant="error"
        icon={<WarningCircle weight="fill" />}
        title="Save failed"
        description="We couldn't save your changes. Please try again."
        action={
          <>
            <Banner.Action>Retry</Banner.Action>
            <Banner.Action variant="ghost" icon={<X />} aria-label="Dismiss" />
          </>
        }
      />
      <Banner
        variant="alert"
        icon={<WarningCircle weight="fill" />}
        title="Save failed"
        description="We couldn't save your changes. Please try again."
        action={
          <>
            <Banner.Action>Retry</Banner.Action>
            <Banner.Action variant="ghost" icon={<X />} aria-label="Dismiss" />
          </>
        }
      />
      <Banner
        variant="secondary"
        icon={<WarningCircle weight="fill" />}
        title="Save failed"
        description="We couldn't save your changes. Please try again."
        action={
          <>
            <Banner.Action>Retry</Banner.Action>
            <Banner.Action variant="ghost" icon={<X />} aria-label="Dismiss" />
          </>
        }
      />
    </div>
  );
}
```

### [With multiple actions](#with-multiple-actions)

```
import { Banner } from "@cloudflare/kumo";
import { Warning } from "@phosphor-icons/react";

/** Banner with multiple action buttons. */
export function BannerWithActionsDemo() {
  return (
    <div className="w-full space-y-3">
      <Banner
        icon={<Warning weight="fill" />}
        variant="error"
        title="Your account is 90 days past due."
        description="Pay now to avoid interruption."
        action={
          <>
            <Banner.Action>Pay now</Banner.Action>
            <Banner.Action variant="secondary">Go to billing</Banner.Action>
          </>
        }
      />
    </div>
  );
}
```

### [Compact size](#compact-size)

Use `size="sm"` in dialogs and other space-constrained contexts. Here, a banner should support the surrounding experience without competing with its primary action, so prefer a Kumo `Link` that renders inline with the description. When greater emphasis is warranted, use `Banner.Action`, which renders at the trailing end.

#### [With inline link](#with-inline-link)

```
import { Banner, Link } from "@cloudflare/kumo";

/**
 * Compact `size="sm"` banner for dialogs and other tight spaces.
 */
export function BannerCompactDemo() {
  return (
    <Banner
      size="sm"
      description="A DNS record for puppies.cloudflare.dev already exists in this zone."
      action={<Link href="#">Manage DNS for puppies.cloudflare.dev</Link>}
    />
  );
}
```

#### [With CTA](#with-cta)

```
import { Banner } from "@cloudflare/kumo";
import { X } from "@phosphor-icons/react";

/** Compact banner with a trailing CTA. */
export function BannerCompactWithCtaDemo() {
  return (
    <Banner
      size="sm"
      description="A DNS record for puppies.cloudflare.dev already exists in this zone."
      action={
        <>
          <Banner.Action>Manage DNS</Banner.Action>
          <Banner.Action variant="ghost">
            <X />
          </Banner.Action>
        </>
      }
    />
  );
}
```

#### [Without action](#without-action)

```
import { Banner } from "@cloudflare/kumo";

/** Compact banner without an action. */
export function BannerCompactWithoutActionDemo() {
  return (
    <Banner
      size="sm"
      description="A DNS record for puppies.cloudflare.dev already exists in this zone."
    />
  );
}
```

### [Custom content](#custom-content)

```
import { Banner, Text } from "@cloudflare/kumo";
import { Info } from "@phosphor-icons/react";

/** Banner with custom React content in description. */
export function BannerCustomContentDemo() {
  return (
    <Banner
      icon={<Info weight="fill" />}
      title="Custom content supported"
      description={
        <Text DANGEROUS_className="text-inherit">
          This banner supports <strong>custom content</strong> with Text.
        </Text>
      }
    />
  );
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| className | `string` | \- | Additional CSS classes merged via \`cn()\`. |
| id | `string` | \- | \- |
| lang | `string` | \- | \- |
| icon | `ReactNode` | \- | Icon element rendered before the banner content (e.g. from \`@phosphor-icons/react\`). |
| title | `string` | \- | Primary heading text for the banner. Use for i18n string injection. |
| description | `ReactNode` | \- | Secondary description text displayed below the title. Use for i18n string injection. |
| action | `ReactNode` | \- | Action slot for a CTA button or link. Compact banners render a Kumo \`Link\` inline with the description; CTAs render at the trailing end. Use \`Banner.Action\` for accent-aware CTAs that self-style to the banner variant; other nodes are rendered as-is. Multiple actions can be passed in a Fragment. Only used in structured mode (with \`title\` or \`description\`). |
| text | `string` | \- | \- |
| children | `ReactNode` | \- | \- |
| variant | `"default" | "alert" | "error" | "secondary"` | `"default"` | Visual style of the banner. - \`"default"\` — Informational blue banner for general messages - \`"alert"\` — Warning yellow banner for cautionary messages - \`"error"\` — Error red banner for critical issues - \`"secondary"\` — Neutral banner for secondary messages |
| size | `"base" | "sm"` | `"base"` | Size of the banner. A \`"sm"\` banner uses tighter spacing and \`text-sm\`, renders a Kumo \`Link\` action inline with the description, and sets its \`Banner.Action\` children to the \`"xs"\` size — suited to dialogs and other tight spaces. |