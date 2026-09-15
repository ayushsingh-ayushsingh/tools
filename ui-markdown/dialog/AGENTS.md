# Dialog

A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/dialog/dialog.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/dialog)

---

```
import { Dialog, Button } from "@cloudflare/kumo";
import { X } from "@phosphor-icons/react";

export function DialogWithActionsDemo() {
  return (
    <Dialog.Root>
      <Dialog.Trigger render={(p) => <Button {...p}>Delete</Button>} />
      <Dialog className="p-8">
        <div className="mb-4 flex items-start justify-between gap-4">
          <Dialog.Title className="text-2xl font-semibold">
            Modal Title
          </Dialog.Title>
          <Dialog.Close
            aria-label="Close"
            render={(props) => (
              <Button
                {...props}
                variant="secondary"
                shape="square"
                icon={<X />}
                aria-label="Close"
              />
            )}
          />
        </div>
        <Dialog.Description className="text-kumo-subtle">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </Dialog.Description>
        <div className="mt-8 flex justify-end gap-2">
          <Dialog.Close
            render={(props) => (
              <Button variant="secondary" {...props}>
                Cancel
              </Button>
            )}
          />
          <Dialog.Close
            render={(props) => (
              <Button variant="destructive" {...props}>
                Delete
              </Button>
            )}
          />
        </div>
      </Dialog>
    </Dialog.Root>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Dialog } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Dialog } from "@cloudflare/kumo/components/dialog";
```

## [Usage](#usage)

```
import { Dialog, Button } from "@cloudflare/kumo";

export default function Example() {
  return (
    <Dialog.Root>
      <Dialog.Trigger render={(p) => <Button {...p}>Open</Button>} />
      <Dialog>
        <Dialog.Title>Dialog Title</Dialog.Title>
        <Dialog.Description>Dialog content goes here.</Dialog.Description>
        <div className="flex justify-end gap-2 mt-4">
          <Dialog.Close
            render={(p) => (
              <Button variant="secondary" {...p}>
                Cancel
              </Button>
            )}
          />
        </div>
      </Dialog>
    </Dialog.Root>
  );
}
```

## [Dialog vs Alert Dialog](#dialog-vs-alert-dialog)

The Dialog component supports two ARIA roles to properly convey semantic meaning to assistive technologies:

| Role | Use Case | Behavior |
| --- | --- | --- |
| `role="dialog"` (default) | General-purpose modals, forms, content display | Dismissible by default |
| `role="alertdialog"` | Destructive actions, confirmations, critical warnings | Requires explicit user acknowledgment |

## [Examples](#examples)

### [Basic Dialog](#basic-dialog)

```
import { Dialog, Button } from "@cloudflare/kumo";
import { X } from "@phosphor-icons/react";

export function DialogBasicDemo() {
  return (
    <Dialog.Root>
      <Dialog.Trigger render={(p) => <Button {...p}>Click me</Button>} />
      <Dialog className="p-8">
        <div className="mb-4 flex items-start justify-between gap-4">
          <Dialog.Title className="text-2xl font-semibold">
            Modal Title
          </Dialog.Title>
          <Dialog.Close
            aria-label="Close"
            render={(props) => (
              <Button
                {...props}
                variant="secondary"
                shape="square"
                icon={<X />}
                aria-label="Close"
              />
            )}
          />
        </div>
        <Dialog.Description className="text-kumo-subtle">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </Dialog.Description>
      </Dialog>
    </Dialog.Root>
  );
}
```

### [Sizes](#sizes)

The `size` prop controls the fixed width of the dialog on desktop. Content that overflows the dialog width will scroll horizontally within the dialog rather than stretching it.

```
import { Dialog, Button } from "@cloudflare/kumo";
import { DialogProps } from "@cloudflare/kumo";
import { X } from "@phosphor-icons/react";

/**
 * Demonstrates that each dialog size holds its fixed width regardless of
 * content. Each dialog contains a wide table that would previously cause the
 * dialog to stretch beyond its intended size.
 */
export function DialogSizesDemo() {
  const sizes: {
    size: NonNullable<DialogProps["size"]>;
    label: string;
    width: string;
  }[] = [
    { size: "sm", label: "Small", width: "288px" },
    { size: "base", label: "Base", width: "384px" },
    { size: "lg", label: "Large", width: "512px" },
    { size: "xl", label: "Extra Large", width: "768px" },
  ];

  return (
    <div className="flex flex-wrap gap-2">
      {sizes.map(({ size, label, width }) => (
        <Dialog.Root key={size}>
          <Dialog.Trigger
            render={(p) => (
              <Button variant="secondary" {...p}>
                {label} ({width})
              </Button>
            )}
          />
          <Dialog size={size} className="p-8">
            <div className="mb-4 flex items-start justify-between gap-4">
              <Dialog.Title className="text-2xl font-semibold">
                {label} Dialog
              </Dialog.Title>
              <Dialog.Close
                aria-label="Close"
                render={(props) => (
                  <Button
                    {...props}
                    variant="secondary"
                    shape="square"
                    icon={<X />}
                    aria-label="Close"
                  />
                )}
              />
            </div>
            <Dialog.Description className="text-kumo-subtle">
              This <code>size="{size}"</code> dialog should stay at {width} wide
              regardless of the content below.
            </Dialog.Description>
            <div className="mt-4 overflow-auto rounded-md border border-kumo-line">
              <table className="w-max text-sm">
                <thead className="bg-kumo-elevated text-left">
                  <tr>
                    <th className="px-3 py-2">Resource</th>
                    <th className="px-3 py-2">Region</th>
                    <th className="px-3 py-2">Status</th>
                    <th className="px-3 py-2">Latency</th>
                    <th className="px-3 py-2">Requests</th>
                    <th className="px-3 py-2">Last Deployed</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-kumo-hairline">
                  <tr>
                    <td className="px-3 py-2">api-gateway-prod</td>
                    <td className="px-3 py-2">us-east-1</td>
                    <td className="px-3 py-2 text-kumo-success">Healthy</td>
                    <td className="px-3 py-2">12ms</td>
                    <td className="px-3 py-2">1,234,567</td>
                    <td className="px-3 py-2">2026-06-23</td>
                  </tr>
                  <tr>
                    <td className="px-3 py-2">worker-analytics</td>
                    <td className="px-3 py-2">eu-west-1</td>
                    <td className="px-3 py-2 text-kumo-warning">Degraded</td>
                    <td className="px-3 py-2">89ms</td>
                    <td className="px-3 py-2">456,789</td>
                    <td className="px-3 py-2">2026-06-22</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div className="mt-6 flex justify-end gap-2">
              <Dialog.Close
                render={(props) => (
                  <Button variant="secondary" {...props}>
                    Close
                  </Button>
                )}
              />
            </div>
          </Dialog>
        </Dialog.Root>
      ))}
    </div>
  );
}
```

### [Alert Dialog (`role="alertdialog"`)](#alert-dialog-rolealertdialog)

For destructive or confirmation dialogs, use `role="alertdialog"` on `Dialog.Root`. This provides proper accessibility semantics by rendering the dialog with `role="alertdialog"` instead of `role="dialog"`.

When to use `role="alertdialog"`:

-   Destructive actions (delete, discard, remove)
-   Confirmation flows requiring explicit user acknowledgment
-   Actions that cannot be undone
-   Critical warnings or errors

```
import { Dialog, Button } from "@cloudflare/kumo";
import { Warning } from "@phosphor-icons/react";

/**
 * Alert dialog for destructive actions that uses role="alertdialog".
 * This provides proper accessibility semantics for confirmation flows.
 */
export function DialogAlertDemo() {
  return (
    <Dialog.Root role="alertdialog">
      <Dialog.Trigger
        render={(p) => (
          <Button {...p} variant="destructive">
            Delete Account
          </Button>
        )}
      />
      <Dialog className="p-8">
        <div className="mb-4 flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-full bg-kumo-danger/20">
            <Warning size={20} className="text-kumo-danger" weight="fill" />
          </div>
          <Dialog.Title className="text-xl font-semibold">
            Delete Account?
          </Dialog.Title>
        </div>
        <Dialog.Description className="text-kumo-subtle">
          This action cannot be undone. All your data will be permanently
          removed from our servers. Are you sure you want to proceed?
        </Dialog.Description>
        <div className="mt-8 flex justify-end gap-2">
          <Dialog.Close
            render={(props) => (
              <Button variant="secondary" {...props}>
                Cancel
              </Button>
            )}
          />
          <Dialog.Close
            render={(props) => (
              <Button variant="destructive" {...props}>
                Delete Account
              </Button>
            )}
          />
        </div>
      </Dialog>
    </Dialog.Root>
  );
}
```

### [Confirmation Dialog (with `disablePointerDismissal`)](#confirmation-dialog-with-disablepointerdismissal)

For confirmation dialogs that should not be dismissed by clicking outside, use `disablePointerDismissal` on `Dialog.Root`. This can be combined with `role="alertdialog"` for proper accessibility.

```
import { Dialog, Button } from "@cloudflare/kumo";
import { Warning } from "@phosphor-icons/react";

export function DialogConfirmationDemo() {
  return (
    <Dialog.Root disablePointerDismissal>
      <Dialog.Trigger
        render={(p) => (
          <Button {...p} variant="destructive">
            Delete Project
          </Button>
        )}
      />
      <Dialog className="p-8">
        <div className="mb-4 flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-full bg-kumo-danger/20">
            <Warning size={20} className="text-kumo-danger" />
          </div>
          <Dialog.Title className="text-xl font-semibold">
            Delete Project?
          </Dialog.Title>
        </div>
        <Dialog.Description className="text-kumo-subtle">
          This action cannot be undone. This will permanently delete the project
          and all associated data.
        </Dialog.Description>
        <div className="mt-8 flex justify-end gap-2">
          <Dialog.Close
            render={(props) => (
              <Button variant="secondary" {...props}>
                Cancel
              </Button>
            )}
          />
          <Dialog.Close
            render={(props) => (
              <Button variant="destructive" {...props}>
                Delete
              </Button>
            )}
          />
        </div>
      </Dialog>
    </Dialog.Root>
  );
}
```

### [With Actions](#with-actions)

```
import { Dialog, Button } from "@cloudflare/kumo";
import { X } from "@phosphor-icons/react";

export function DialogWithActionsDemo() {
  return (
    <Dialog.Root>
      <Dialog.Trigger render={(p) => <Button {...p}>Delete</Button>} />
      <Dialog className="p-8">
        <div className="mb-4 flex items-start justify-between gap-4">
          <Dialog.Title className="text-2xl font-semibold">
            Modal Title
          </Dialog.Title>
          <Dialog.Close
            aria-label="Close"
            render={(props) => (
              <Button
                {...props}
                variant="secondary"
                shape="square"
                icon={<X />}
                aria-label="Close"
              />
            )}
          />
        </div>
        <Dialog.Description className="text-kumo-subtle">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </Dialog.Description>
        <div className="mt-8 flex justify-end gap-2">
          <Dialog.Close
            render={(props) => (
              <Button variant="secondary" {...props}>
                Cancel
              </Button>
            )}
          />
          <Dialog.Close
            render={(props) => (
              <Button variant="destructive" {...props}>
                Delete
              </Button>
            )}
          />
        </div>
      </Dialog>
    </Dialog.Root>
  );
}
```

### [Custom Max Width](#custom-max-width)

Consumer max-width utilities such as `max-w-lg` should cap the dialog on desktop, even when the dialog contains wide intrinsic content.

```
import { Dialog, Button } from "@cloudflare/kumo";
import { X } from "@phosphor-icons/react";

/**
 * Dialog with a consumer-provided max width and wide intrinsic content.
 * The panel should stay capped at max-w-lg on desktop.
 */
export function DialogMaxWidthDemo() {
  return (
    <Dialog.Root>
      <Dialog.Trigger
        render={(p) => <Button {...p}>Open capped dialog</Button>}
      />
      <Dialog className="max-w-lg p-8">
        <div className="mb-4 flex items-start justify-between gap-4">
          <Dialog.Title className="text-2xl font-semibold">
            Max width override
          </Dialog.Title>
          <Dialog.Close
            aria-label="Close"
            render={(props) => (
              <Button
                {...props}
                variant="secondary"
                shape="square"
                icon={<X />}
                aria-label="Close"
              />
            )}
          />
        </div>
        <Dialog.Description className="text-kumo-subtle">
          This dialog uses <code>className="max-w-lg"</code> and should stay
          capped around 512px on desktop.
        </Dialog.Description>
        <div className="mt-4 truncate rounded-md border border-kumo-line bg-kumo-recessed p-3 font-mono text-sm">
          abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
        </div>
      </Dialog>
    </Dialog.Root>
  );
}
```

### [With Select](#with-select)

Dialog containing a Select dropdown.

```
import { Dialog, Button, Select } from "@cloudflare/kumo";
import { X } from "@phosphor-icons/react";

export function DialogWithSelectDemo() {
  return (
    <Dialog.Root>
      <Dialog.Trigger render={(p) => <Button {...p}>Open Form</Button>} />
      <Dialog className="p-8">
        <div className="mb-4 flex items-start justify-between gap-4">
          <Dialog.Title className="text-2xl font-semibold">
            Create Resource
          </Dialog.Title>
          <Dialog.Close
            aria-label="Close"
            render={(props) => (
              <Button
                {...props}
                variant="secondary"
                shape="square"
                icon={<X />}
                aria-label="Close"
              />
            )}
          />
        </div>
        <Dialog.Description className="mb-4 text-kumo-subtle">
          Select a region for your new resource.
        </Dialog.Description>
        <Select
          className="w-full"
          placeholder="Select region..."
          renderValue={(v) => regions.find((r) => r.value === v)?.label}
        >
          {regions.map((region) => (
            <Select.Option key={region.value} value={region.value}>
              {region.label}
            </Select.Option>
          ))}
        </Select>
        <div className="mt-8 flex justify-end gap-2">
          <Dialog.Close
            render={(props) => (
              <Button variant="secondary" {...props}>
                Cancel
              </Button>
            )}
          />
          <Button variant="primary">Create</Button>
        </div>
      </Dialog>
    </Dialog.Root>
  );
}
```

### [With Combobox](#with-combobox)

Dialog containing a Combobox for searchable selection.

```
import { useState } from "react";
import { Dialog, Button, Combobox } from "@cloudflare/kumo";
import { X } from "@phosphor-icons/react";

export function DialogWithComboboxDemo() {
  const [value, setValue] = useState<{ value: string; label: string } | null>(
    null,
  );

  return (
    <Dialog.Root>
      <Dialog.Trigger render={(p) => <Button {...p}>Open Form</Button>} />
      <Dialog className="p-8">
        <div className="mb-4 flex items-start justify-between gap-4">
          <Dialog.Title className="text-2xl font-semibold">
            Create Resource
          </Dialog.Title>
          <Dialog.Close
            aria-label="Close"
            render={(props) => (
              <Button
                {...props}
                variant="secondary"
                shape="square"
                icon={<X />}
                aria-label="Close"
              />
            )}
          />
        </div>
        <Dialog.Description className="mb-4 text-kumo-subtle">
          Search and select a region for your new resource.
        </Dialog.Description>
        <Combobox value={value} onValueChange={setValue} items={regions}>
          <Combobox.TriggerInput
            className="w-full"
            placeholder="Search regions..."
          />
          <Combobox.Content>
            <Combobox.Empty>No regions found</Combobox.Empty>
            <Combobox.List>
              {(item: { value: string; label: string }) => (
                <Combobox.Item key={item.value} value={item}>
                  {item.label}
                </Combobox.Item>
              )}
            </Combobox.List>
          </Combobox.Content>
        </Combobox>
        <div className="mt-8 flex justify-end gap-2">
          <Dialog.Close
            render={(props) => (
              <Button variant="secondary" {...props}>
                Cancel
              </Button>
            )}
          />
          <Button variant="primary">Create</Button>
        </div>
      </Dialog>
    </Dialog.Root>
  );
}
```

### [With Dropdown](#with-dropdown)

Dialog containing a Dropdown menu.

```
import { Dialog, Button, DropdownMenu } from "@cloudflare/kumo";
import { X } from "@phosphor-icons/react";

export function DialogWithDropdownDemo() {
  return (
    <Dialog.Root>
      <Dialog.Trigger render={(p) => <Button {...p}>Open Form</Button>} />
      <Dialog className="p-8">
        <div className="mb-4 flex items-start justify-between gap-4">
          <Dialog.Title className="text-2xl font-semibold">
            Resource Actions
          </Dialog.Title>
          <Dialog.Close
            aria-label="Close"
            render={(props) => (
              <Button
                {...props}
                variant="secondary"
                shape="square"
                icon={<X />}
                aria-label="Close"
              />
            )}
          />
        </div>
        <Dialog.Description className="mb-4 text-kumo-subtle">
          Choose an action for the selected resource.
        </Dialog.Description>
        <DropdownMenu>
          <DropdownMenu.Trigger render={<Button>Actions</Button>} />
          <DropdownMenu.Content>
            <DropdownMenu.Item>Edit</DropdownMenu.Item>
            <DropdownMenu.Item>Duplicate</DropdownMenu.Item>
            <DropdownMenu.Separator />
            <DropdownMenu.Item variant="danger">Delete</DropdownMenu.Item>
          </DropdownMenu.Content>
        </DropdownMenu>
        <div className="mt-8 flex justify-end">
          <Dialog.Close
            render={(props) => (
              <Button variant="secondary" {...props}>
                Close
              </Button>
            )}
          />
        </div>
      </Dialog>
    </Dialog.Root>
  );
}
```

## [API Reference](#api-reference)

### [Dialog](#dialog)

The main dialog container that renders the modal overlay and popup.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| className | `string` | \- | Additional CSS classes merged via \`cn()\`. |
| children | `ReactNode` | \- | Dialog content (typically Title, Description, Close, and action buttons). |
| container | `PortalContainer` | \- | Container element for the portal. Use this to render the dialog inside a Shadow DOM or custom container. Overrides \`KumoPortalProvider\` context. |
| size | `"base" | "sm" | "lg" | "xl"` | `"base"` | Dialog width. - \`"sm"\` — Small (288px) for simple confirmations - \`"base"\` — Default (384px) - \`"lg"\` — Large (512px) for complex content - \`"xl"\` — Extra large (768px) for detailed views |

### [Dialog.Root](#dialogroot)

Controls the open state of the dialog. Doesn’t render its own HTML element.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| role | ”dialog” | “alertdialog" | "dialog” | The ARIA role for the dialog. Use `"alertdialog"` for destructive or confirmation flows. |
| disablePointerDismissal | boolean | false | When true, prevents the dialog from being dismissed by clicking outside. |

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Dialog.Trigger](#dialogtrigger)

A button that opens the dialog when clicked.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Dialog.Title](#dialogtitle)

A heading that labels the dialog for accessibility.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Dialog.Description](#dialogdescription)

A paragraph providing additional context about the dialog.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Dialog.Close](#dialogclose)

A button that closes the dialog when clicked.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.