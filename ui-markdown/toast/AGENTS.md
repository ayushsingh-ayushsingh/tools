# Toast

A notification system for displaying brief, non-intrusive messages to users.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/toast/toast.tsx)

---

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

function ToastTriggerButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() =>
        toastManager.add({
          title: "Toast created",
          description: "This is a toast notification.",
        })
      }
    >
      Show toast
    </Button>
  );
}

export function ToastBasicDemo() {
  return (
    <Toasty>
      <ToastTriggerButton />
    </Toasty>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Toasty, useKumoToastManager } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Toasty, useKumoToastManager } from "@cloudflare/kumo/components/toast";
```

## [Usage](#usage)

The toast system consists of two parts: the `Toasty` provider component and the `useKumoToastManager()` hook for triggering toasts.

```
import { Toasty, useKumoToastManager, Button } from "@cloudflare/kumo";

function ToastTrigger() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() =>
        toastManager.add({
          title: "Success!",
          description: "Your changes have been saved.",
        })
      }
    >
      Save changes
    </Button>
  );
}

export default function App() {
  return (
    <Toasty>
      <ToastTrigger />
      {/* Rest of your app */}
    </Toasty>
  );
}
```

## [Setup](#setup)

Wrap your application (or a section of it) with the `Toasty` provider. This sets up the toast context and renders the toast viewport.

```
// In your app root or layout
import { Toasty } from "@cloudflare/kumo";

export function Layout({ children }) {
  return <Toasty>{children}</Toasty>;
}
```

## [Examples](#examples)

### [Title and Description](#title-and-description)

A complete toast with both title and description.

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

function ToastTriggerButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() =>
        toastManager.add({
          title: "Toast created",
          description: "This is a toast notification.",
        })
      }
    >
      Show toast
    </Button>
  );
}

export function ToastBasicDemo() {
  return (
    <Toasty>
      <ToastTriggerButton />
    </Toasty>
  );
}
```

### [Title Only](#title-only)

A simple toast with just a title for brief messages.

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

function ToastTitleOnlyButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() =>
        toastManager.add({
          title: "Settings saved",
        })
      }
    >
      Title only
    </Button>
  );
}

export function ToastTitleOnlyDemo() {
  return (
    <Toasty>
      <ToastTitleOnlyButton />
    </Toasty>
  );
}
```

### [Description Only](#description-only)

A toast with only a description for more detailed messages.

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

function ToastDescriptionOnlyButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() =>
        toastManager.add({
          description: "Your changes have been saved successfully.",
        })
      }
    >
      Description only
    </Button>
  );
}

export function ToastDescriptionOnlyDemo() {
  return (
    <Toasty>
      <ToastDescriptionOnlyButton />
    </Toasty>
  );
}
```

### [Success Variant](#success-variant)

Use the success variant for confirmations and positive outcomes.

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

/** Success toast with green accent border and check icon. */
function ToastSuccessButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      variant="primary"
      onClick={() =>
        toastManager.add({
          title: "Deployed successfully",
          description: "Your Worker is now live.",
          variant: "success",
        })
      }
    >
      Deploy Worker
    </Button>
  );
}

export function ToastSuccessDemo() {
  return (
    <Toasty>
      <ToastSuccessButton />
    </Toasty>
  );
}
```

### [Multiple Toasts](#multiple-toasts)

Multiple toasts stack and animate smoothly. Hover over the stack to expand them.

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

function ToastMultipleButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() => {
        toastManager.add({
          title: "First toast",
          description: "This is the first notification.",
        });
        setTimeout(() => {
          toastManager.add({
            title: "Second toast",
            description: "This is the second notification.",
          });
        }, 500);
        setTimeout(() => {
          toastManager.add({
            title: "Third toast",
            description: "This is the third notification.",
          });
        }, 1000);
      }}
    >
      Show multiple toasts
    </Button>
  );
}

export function ToastMultipleDemo() {
  return (
    <Toasty>
      <ToastMultipleButton />
    </Toasty>
  );
}
```

### [Functional Updates](#functional-updates)

Update a toast in place from its current state. This example changes the deployment toast to success after it is created.

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

function ToastFunctionalUpdateButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() => {
        const id = toastManager.add({
          id: "functional-update",
          title: "Deploying Worker",
          description: "Uploading your changes.",
          variant: "info",
          data: { deployment: "in progress" },
        });

        setTimeout(() => {
          toastManager.update(id, (toast) => ({
            title: "Worker deployed",
            description: `Deployment was ${toast.data.deployment}.`,
            variant: "success",
          }));
        }, 1200);
      }}
    >
      Deploy Worker
    </Button>
  );
}

/** Demonstrates updating a toast from its current state. */
export function ToastFunctionalUpdateDemo() {
  return (
    <Toasty>
      <ToastFunctionalUpdateButton />
    </Toasty>
  );
}
```

### [Error Variant](#error-variant)

Use the error variant for critical issues that need attention.

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

function ToastErrorButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() =>
        toastManager.add({
          title: "Deployment failed",
          description: "Unable to connect to the server.",
          variant: "error",
        })
      }
    >
      Show error toast
    </Button>
  );
}

export function ToastErrorDemo() {
  return (
    <Toasty>
      <ToastErrorButton />
    </Toasty>
  );
}
```

### [Warning Variant](#warning-variant)

Use the warning variant for cautionary messages.

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

function ToastWarningButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() =>
        toastManager.add({
          title: "Rate limit warning",
          description: "You're approaching your API quota.",
          variant: "warning",
        })
      }
    >
      Show warning toast
    </Button>
  );
}

export function ToastWarningDemo() {
  return (
    <Toasty>
      <ToastWarningButton />
    </Toasty>
  );
}
```

### [Info Variant](#info-variant)

Use the info variant for neutral informational messages.

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

/** Info toast with blue accent border and info icon. */
function ToastInfoButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() =>
        toastManager.add({
          title: "New version available",
          description: "Kumo v4.2 includes performance improvements.",
          variant: "info",
        })
      }
    >
      Show info toast
    </Button>
  );
}

export function ToastInfoDemo() {
  return (
    <Toasty>
      <ToastInfoButton />
    </Toasty>
  );
}
```

### [Custom Content](#custom-content)

Use the content prop to render completely custom toast content.

```
import { Button, Toasty, useKumoToastManager, Link } from "@cloudflare/kumo";
import { CheckCircleIcon } from "@phosphor-icons/react/dist/ssr";

function ToastCustomContentButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() =>
        toastManager.add({
          content: (
            <div>
              <div className="flex items-center gap-2">
                <CheckCircleIcon />
                <Link href="/">my-first-worker</Link> created!
              </div>
            </div>
          ),
        })
      }
    >
      Show custom content
    </Button>
  );
}

export function ToastCustomContentDemo() {
  return (
    <Toasty>
      <ToastCustomContentButton />
    </Toasty>
  );
}
```

### [Action Buttons](#action-buttons)

Add action buttons to toasts for user interaction.

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

function ToastActionsButton() {
  const toastManager = useKumoToastManager();

  return (
    <Button
      onClick={() =>
        toastManager.add({
          title: "Need help?",
          description: "Get assistance with your deployment.",
          actions: [
            {
              children: "Support",
              variant: "secondary",
              onClick: () => console.log("Support clicked"),
            },
            {
              children: "Ask AI",
              variant: "primary",
              onClick: () => console.log("Ask AI clicked"),
            },
          ],
        })
      }
    >
      Show with actions
    </Button>
  );
}

export function ToastActionsDemo() {
  return (
    <Toasty>
      <ToastActionsButton />
    </Toasty>
  );
}
```

### [Promise](#promise)

Use the promise method to show loading, success, and error states automatically.

```
import { Button, Toasty, useKumoToastManager } from "@cloudflare/kumo";

function ToastPromiseButton() {
  const toastManager = useKumoToastManager();

  const simulateDeployment = () => {
    return new Promise<{ name: string }>((resolve, reject) => {
      setTimeout(() => {
        if (Math.random() > 0.3) {
          resolve({ name: "my-worker" });
        } else {
          reject(new Error("Network error"));
        }
      }, 2000);
    });
  };

  return (
    <Button
      onClick={() =>
        toastManager.promise(simulateDeployment(), {
          loading: {
            title: "Deploying...",
            description: "Please wait while we deploy your Worker.",
          },
          success: (data) => ({
            title: "Deployed!",
            description: `Worker "${data.name}" is now live.`,
          }),
          error: (err) => ({
            title: "Deployment failed",
            description: err.message,
            variant: "error",
          }),
        })
      }
    >
      Deploy with promise
    </Button>
  );
}

export function ToastPromiseDemo() {
  return (
    <Toasty>
      <ToastPromiseButton />
    </Toasty>
  );
}
```

## [API Reference](#api-reference)

### [Toasty](#toasty)

The provider component that wraps your app and manages the toast system.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| variant | `"default" | "success" | "error" | "warning" | "info"` | `"default"` | \- |
| children\* | `React.ReactNode` | \- | Application content. Toasts render via a portal above this. |
| container | `PortalContainer` | \- | Container element for the portal. Use this to render toasts inside a Shadow DOM or custom container. Overrides \`KumoPortalProvider\` context. |
| toastManager | `ReturnType<typeof createKumoToastManager>` | \- | Optional toast manager created by \`createKumoToastManager()\`. When provided, allows code outside the React tree (timers, module-load callbacks, query-cache listeners) to dispatch toasts via the same dedupe-aware manager that \`useKumoToastManager()\` returns inside the tree. Forwarded to the underlying \`@base-ui/react/toast\` \`Toast.Provider\` \`toastManager\` prop — see https://base-ui.com/react/components/toast for the upstream primitive. |

### [useKumoToastManager()](#usekumotoastmanager)

A hook that returns the toast manager for creating toasts.

```
const toastManager = useKumoToastManager();

// Add a toast
toastManager.add(options);

// Update from the current toast state
toastManager.update(toastId, (toast) => ({
  description: `Updated after ${toast.timeout ?? 5000}ms`,
}));

// Promise-based toast
toastManager.promise(asyncFn(), {
  loading: options,
  success: (data) => options,
  error: (err) => options,
});
```

### [Toast Options](#toast-options)

Options passed to `toastManager.add()` and promise handlers.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| title | string | — | The toast title displayed prominently. |
| description | string | — | Secondary text displayed below the title. |
| variant | “default” | “success” | “error” | “warning” | “info" | "default” | Visual style of the toast. |
| content | ReactNode | — | Custom content to render inside the toast. Overrides title and description. |
| actions | ButtonProps\[\] | — | Array of button props to render as action buttons. |
| timeout | number | 5000 | Time in milliseconds before the toast auto-dismisses. |