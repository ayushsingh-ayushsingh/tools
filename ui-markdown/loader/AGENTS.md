# Loader

A loading spinner to indicate loading state.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/loader/loader.tsx)

---

```
import { Loader } from "@cloudflare/kumo";

export function LoaderBasicDemo() {
  return <Loader />;
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Loader } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Loader } from "@cloudflare/kumo/components/loader";
```

## [Usage](#usage)

```
import { Loader } from "@cloudflare/kumo";

export default function Example() {
  return <Loader />;
}
```

## [Examples](#examples)

### [Default Size](#default-size)

```
import { Loader } from "@cloudflare/kumo";

export function LoaderBasicDemo() {
  return <Loader />;
}
```

### [Custom Size](#custom-size)

```
import { Loader } from "@cloudflare/kumo";

export function LoaderCustomSizeDemo() {
  return <Loader size={24} />;
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| className | `string` | \- | Additional CSS classes merged via \`cn()\`. |
| size | `"sm" | "base" | "lg"` | `"base"` | Size of the spinner. Use a preset name or a custom pixel number. - \`"sm"\` — 16px, for inline use - \`"base"\` — 24px, default size - \`"lg"\` — 32px, for prominent loading states |