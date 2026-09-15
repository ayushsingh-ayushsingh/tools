# Empty

A component to display when there&#39;s no content or data to show, with optional command line and actions.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/empty/empty.tsx)

---

```
import { Empty, Button } from "@cloudflare/kumo";
import { PackageIcon, CodeIcon, GlobeIcon } from "@phosphor-icons/react";

export function EmptyDemo() {
  return (
    <Empty
      icon={<PackageIcon size={48} />}
      title="No packages found"
      description="Get started by installing your first package."
      commandLine="npm install @cloudflare/kumo"
      contents={
        <div className="flex items-center gap-2">
          <Button icon={<CodeIcon />}>See examples</Button>
          <Button icon={<GlobeIcon />} variant="primary">
            View documentation
          </Button>
        </div>
      }
    />
  );
}
```

## [Installation](#installation)

```
import { Empty } from "@cloudflare/kumo";
```

## [Usage](#usage)

```
import { Empty } from "@cloudflare/kumo";
import { PackageIcon } from "@phosphor-icons/react";

export default function Example() {
  return (
    <Empty
      icon={<PackageIcon size={48} />}
      title="No packages found"
      description="Get started by installing your first package."
      commandLine="npm install @kumo/ui"
    />
  );
}
```

## [Examples](#examples)

### [Basic](#basic)

```
import { Empty } from "@cloudflare/kumo";

export function EmptyBasicDemo() {
  return (
    <Empty
      title="No results found"
      description="Try adjusting your search or filter to find what you're looking for."
    />
  );
}
```

## [Sizes](#sizes)

Empty states come in three sizes to fit different container contexts.

```
import { Empty } from "@cloudflare/kumo";
import { Database } from "@phosphor-icons/react";

export function EmptySizesDemo() {
  return (
    <div className="flex flex-col gap-8">
      <div>
        <p className="mb-2 text-sm text-kumo-subtle">Small</p>
        <Empty
          size="sm"
          icon={<Database size={32} className="text-kumo-inactive" />}
          title="No data available"
          description="There is no data to display."
        />
      </div>
      <div>
        <p className="mb-2 text-sm text-kumo-subtle">Base</p>
        <Empty
          size="base"
          icon={<Database size={48} className="text-kumo-inactive" />}
          title="No data available"
          description="There is no data to display."
        />
      </div>
      <div>
        <p className="mb-2 text-sm text-kumo-subtle">Large</p>
        <Empty
          size="lg"
          icon={<Database size={64} className="text-kumo-inactive" />}
          title="No data available"
          description="There is no data to display."
        />
      </div>
    </div>
  );
}
```

## [With Command Line](#with-command-line)

Include a copyable command to help users get started.

```
import { Empty } from "@cloudflare/kumo";
import { FolderOpen } from "@phosphor-icons/react";

export function EmptyWithCommandDemo() {
  return (
    <Empty
      icon={<FolderOpen size={48} className="text-kumo-inactive" />}
      title="No projects found"
      description="Get started by creating your first project using the command below."
      commandLine="npm create kumo-project"
    />
  );
}
```

## [With Actions](#with-actions)

Add custom action buttons using the contents prop.

```
import { Empty, Button } from "@cloudflare/kumo";
import { CloudSlash } from "@phosphor-icons/react";

export function EmptyWithActionsDemo() {
  return (
    <Empty
      icon={<CloudSlash size={48} className="text-kumo-inactive" />}
      title="No connection"
      description="Unable to connect to the server. Please check your connection and try again."
      contents={
        <div className="flex gap-2">
          <Button variant="primary">Retry</Button>
          <Button variant="secondary">Go Back</Button>
        </div>
      }
    />
  );
}
```

## [Minimal](#minimal)

At minimum, only a title is required.

```
import { Empty } from "@cloudflare/kumo";

export function EmptyMinimalDemo() {
  return <Empty title="Nothing here" />;
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| size | `"sm" | "base" | "lg"` | `"base"` | Size of the empty state container. - \`"sm"\` — Compact empty state for smaller containers - \`"base"\` — Default empty state size - \`"lg"\` — Large empty state for prominent placement |
| icon | `ReactNode` | \- | Decorative icon displayed above the title (e.g. from \`@phosphor-icons/react\`). |
| title\* | `string` | \- | Primary heading text for the empty state. |
| description | `string` | \- | Secondary description text displayed below the title. |
| commandLine | `string` | \- | Shell command displayed in a copyable code block. |
| contents | `ReactNode` | \- | Additional content (buttons, links) rendered below the description. |
| className | `string` | \- | Additional CSS classes merged via \`cn()\`. |