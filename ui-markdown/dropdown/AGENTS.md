# Dropdown Menu

Displays a menu to the user—such as a set of actions or functions—triggered by a button.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/dropdown/dropdown.tsx)

**Base UI:** [Documentation](https://base-ui.com/react/components/menu)

---

```
import { DropdownMenu, Button } from "@cloudflare/kumo";
import { PlusIcon } from "@phosphor-icons/react";

export function DropdownBasicDemo() {
  return (
    <DropdownMenu>
      <DropdownMenu.Trigger render={<Button icon={PlusIcon}>Add</Button>} />
      <DropdownMenu.Content>
        <DropdownMenu.Item>Worker</DropdownMenu.Item>
        <DropdownMenu.Item>Pages</DropdownMenu.Item>
        <DropdownMenu.Item>KV Namespace</DropdownMenu.Item>
      </DropdownMenu.Content>
    </DropdownMenu>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { DropdownMenu } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { DropdownMenu } from "@cloudflare/kumo/components/dropdown";
```

## [Usage](#usage)

```
import { DropdownMenu, Button } from "@cloudflare/kumo";

export default function Example() {
  return (
    <DropdownMenu>
      <DropdownMenu.Trigger render={<Button>Menu</Button>} />
      <DropdownMenu.Content>
        <DropdownMenu.Item onClick={() => console.log("edit")}>
          Edit
        </DropdownMenu.Item>
        <DropdownMenu.Item onClick={() => console.log("duplicate")}>
          Duplicate
        </DropdownMenu.Item>
        <DropdownMenu.Separator />
        <DropdownMenu.Item
          variant="danger"
          onClick={() => console.log("delete")}
        >
          Delete
        </DropdownMenu.Item>
      </DropdownMenu.Content>
    </DropdownMenu>
  );
}
```

## [Examples](#examples)

### [Basic Dropdown](#basic-dropdown)

```
import { DropdownMenu, Button } from "@cloudflare/kumo";
import { PlusIcon } from "@phosphor-icons/react";

export function DropdownBasicDemo() {
  return (
    <DropdownMenu>
      <DropdownMenu.Trigger render={<Button icon={PlusIcon}>Add</Button>} />
      <DropdownMenu.Content>
        <DropdownMenu.Item>Worker</DropdownMenu.Item>
        <DropdownMenu.Item>Pages</DropdownMenu.Item>
        <DropdownMenu.Item>KV Namespace</DropdownMenu.Item>
      </DropdownMenu.Content>
    </DropdownMenu>
  );
}
```

### [Inset Items](#inset-items)

Use `inset` on items without an icon to align their text with items that have one.

```
import { DropdownMenu, Button } from "@cloudflare/kumo";
import { CopyIcon, PencilSimpleIcon, TrashIcon } from "@phosphor-icons/react";

/**
 * Use `inset` on items without an icon to align their text with items that have one.
 */
export function DropdownInsetDemo() {
  return (
    <DropdownMenu>
      <DropdownMenu.Trigger render={<Button>Edit</Button>} />
      <DropdownMenu.Content>
        <DropdownMenu.Item icon={PencilSimpleIcon}>Rename</DropdownMenu.Item>
        <DropdownMenu.Item icon={CopyIcon}>Duplicate</DropdownMenu.Item>
        <DropdownMenu.Separator />
        <DropdownMenu.Item inset>Move to folder</DropdownMenu.Item>
        <DropdownMenu.Item inset>Add to favorites</DropdownMenu.Item>
        <DropdownMenu.Separator />
        <DropdownMenu.Item icon={TrashIcon} variant="danger">
          Delete
        </DropdownMenu.Item>
      </DropdownMenu.Content>
    </DropdownMenu>
  );
}
```

### [Handling Item Clicks](#handling-item-clicks)

Use `onClick` on `DropdownMenu.Item` to handle actions. Each item receives a standard React mouse event handler.

```
import { useState } from "react";
import { DropdownMenu, Button } from "@cloudflare/kumo";
import { CopyIcon, PencilSimpleIcon, TrashIcon } from "@phosphor-icons/react";

/**
 * Use `onClick` on `DropdownMenu.Item` to handle item actions.
 * Each item receives a standard React mouse event handler.
 */
export function DropdownOnClickDemo() {
  const [lastAction, setLastAction] = useState<string | null>(null);

  return (
    <div className="flex flex-col items-start gap-2">
      <DropdownMenu>
        <DropdownMenu.Trigger render={<Button>Actions</Button>} />
        <DropdownMenu.Content>
          <DropdownMenu.Item
            icon={CopyIcon}
            onClick={() => setLastAction("Duplicated")}
          >
            Duplicate
          </DropdownMenu.Item>
          <DropdownMenu.Item
            icon={PencilSimpleIcon}
            onClick={() => setLastAction("Renamed")}
          >
            Rename
          </DropdownMenu.Item>
          <DropdownMenu.Separator />
          <DropdownMenu.Item
            icon={TrashIcon}
            variant="danger"
            onClick={() => setLastAction("Deleted")}
          >
            Delete
          </DropdownMenu.Item>
        </DropdownMenu.Content>
      </DropdownMenu>
      {lastAction && (
        <p className="text-sm text-kumo-subtle">
          Last action: <span className="text-kumo-default">{lastAction}</span>
        </p>
      )}
    </div>
  );
}
```

### [Checkbox Items](#checkbox-items)

Use `DropdownMenu.CheckboxItem` for toggleable options that can be independently checked or unchecked.

```
import { useState } from "react";
import { DropdownMenu, Button } from "@cloudflare/kumo";

export function DropdownCheckboxDemo() {
  const [showSidebar, setShowSidebar] = useState(true);
  const [showLineNumbers, setShowLineNumbers] = useState(false);
  const [wordWrap, setWordWrap] = useState(true);

  return (
    <DropdownMenu>
      <DropdownMenu.Trigger render={<Button>View Options</Button>} />
      <DropdownMenu.Content>
        <DropdownMenu.Group>
          <DropdownMenu.Label>Display</DropdownMenu.Label>
          <DropdownMenu.CheckboxItem
            checked={showSidebar}
            onCheckedChange={setShowSidebar}
          >
            Show sidebar
          </DropdownMenu.CheckboxItem>
          <DropdownMenu.CheckboxItem
            checked={showLineNumbers}
            onCheckedChange={setShowLineNumbers}
          >
            Show line numbers
          </DropdownMenu.CheckboxItem>
          <DropdownMenu.CheckboxItem
            checked={wordWrap}
            onCheckedChange={setWordWrap}
          >
            Word wrap
          </DropdownMenu.CheckboxItem>
        </DropdownMenu.Group>
      </DropdownMenu.Content>
    </DropdownMenu>
  );
}
```

### [Nested Menu with Radio Selection](#nested-menu-with-radio-selection)

Use `DropdownMenu.Sub`, `DropdownMenu.SubTrigger`, and `DropdownMenu.SubContent` to create nested submenus. For single-selection lists like language or timezone, use `DropdownMenu.RadioGroup` and `DropdownMenu.RadioItem`.

```
import { useState } from "react";
import { DropdownMenu, Button } from "@cloudflare/kumo";
import { UserIcon, CreditCardIcon, MoonIcon, SignOutIcon } from "@phosphor-icons/react";

export function DropdownNestedDemo() {
  const [language, setLanguage] = useState("en");
  const [timezone, setTimezone] = useState("America/Los_Angeles");

  return (
    <DropdownMenu>
      <DropdownMenu.Trigger render={<Button icon={UserIcon}>Account</Button>} />
      <DropdownMenu.Content>
        <DropdownMenu.Item icon={UserIcon}>Profile</DropdownMenu.Item>
        <DropdownMenu.Item icon={CreditCardIcon}>Billing</DropdownMenu.Item>
        <DropdownMenu.Item icon={MoonIcon}>Dark mode</DropdownMenu.Item>

        {/* Language submenu with RadioGroup */}
        <DropdownMenu.Sub>
          <DropdownMenu.SubTrigger>Language</DropdownMenu.SubTrigger>
          <DropdownMenu.SubContent>
            <DropdownMenu.Group>
              <DropdownMenu.RadioGroup
                value={language}
                onValueChange={setLanguage}
              >
                {languages.map((lang) => (
                  <DropdownMenu.RadioItem key={lang.code} value={lang.code}>
                    {lang.label}
                    <DropdownMenu.RadioItemIndicator />
                  </DropdownMenu.RadioItem>
                ))}
              </DropdownMenu.RadioGroup>
            </DropdownMenu.Group>
          </DropdownMenu.SubContent>
        </DropdownMenu.Sub>

        {/* Timezone submenu with RadioGroup */}
        <DropdownMenu.Sub>
          <DropdownMenu.SubTrigger>Set Timezone</DropdownMenu.SubTrigger>
          <DropdownMenu.SubContent>
            <DropdownMenu.Group>
              <DropdownMenu.RadioGroup
                value={timezone}
                onValueChange={setTimezone}
              >
                {timezones.map((tz) => (
                  <DropdownMenu.RadioItem key={tz.value} value={tz.value}>
                    {tz.label}
                    <DropdownMenu.RadioItemIndicator />
                  </DropdownMenu.RadioItem>
                ))}
              </DropdownMenu.RadioGroup>
            </DropdownMenu.Group>
          </DropdownMenu.SubContent>
        </DropdownMenu.Sub>

        <DropdownMenu.Separator />
        <DropdownMenu.Item icon={SignOutIcon} variant="danger">
          Log out
        </DropdownMenu.Item>
      </DropdownMenu.Content>
    </DropdownMenu>
  );
}
```

### [Custom Trigger with Avatar](#custom-trigger-with-avatar)

Use the `render` prop to customize the trigger element while passing children to render inside it. This is useful when you need a non-button trigger (like an avatar) wrapped in an accessible button element.

```
import { DropdownMenu } from "@cloudflare/kumo";
import { UserIcon, SignOutIcon, GearIcon } from "@phosphor-icons/react";

/**
 * Demonstrates using the render prop with children to compose a custom trigger
 * that contains other elements. The render prop provides the trigger element,
 * while children are rendered inside it.
 */
export function DropdownAvatarTriggerDemo() {
  return (
    <DropdownMenu>
      <DropdownMenu.Trigger
        render={<button type="button" className="rounded-full" />}
      >
        <span className="flex h-8 w-8 items-center justify-center rounded-full bg-kumo-brand text-sm font-medium text-white">
          MR
        </span>
      </DropdownMenu.Trigger>
      <DropdownMenu.Content>
        <DropdownMenu.Item icon={UserIcon}>Profile</DropdownMenu.Item>
        <DropdownMenu.Item icon={GearIcon}>Settings</DropdownMenu.Item>
        <DropdownMenu.Separator />
        <DropdownMenu.Item icon={SignOutIcon} variant="danger">
          Log out
        </DropdownMenu.Item>
      </DropdownMenu.Content>
    </DropdownMenu>
  );
}
```

### [Navigation Links](#navigation-links)

Use `DropdownMenu.LinkItem` for menu items that navigate to a URL. This renders a semantic `<a>` element with full control over link attributes like `target` and `rel`.

```
import { DropdownMenu, Button } from "@cloudflare/kumo";
import { GearIcon, BookOpenIcon, ArrowSquareOutIcon } from "@phosphor-icons/react";

/**
 * Demonstrates the new LinkItem component for navigation links.
 * Use LinkItem instead of Item with href for cleaner, more semantic links.
 */
export function DropdownLinkItemDemo() {
  return (
    <DropdownMenu>
      <DropdownMenu.Trigger render={<Button>Resources</Button>} />
      <DropdownMenu.Content>
        <DropdownMenu.LinkItem href="/settings" icon={GearIcon}>
          Settings
        </DropdownMenu.LinkItem>
        <DropdownMenu.LinkItem href="/docs" icon={BookOpenIcon}>
          Documentation
        </DropdownMenu.LinkItem>
        <DropdownMenu.Separator />
        <DropdownMenu.LinkItem
          href="https://developers.cloudflare.com"
          target="_blank"
          icon={ArrowSquareOutIcon}
        >
          Developer Docs
        </DropdownMenu.LinkItem>
      </DropdownMenu.Content>
    </DropdownMenu>
  );
}
```

### [Long List](#long-list)

When a dropdown contains many items, the content automatically limits its height to the available viewport space and becomes scrollable.

```
import { DropdownMenu, Button } from "@cloudflare/kumo";

/**
 * A dropdown with a very long list of items to demonstrate the max-height
 * behavior — the content scrolls when it exceeds available viewport space.
 */
export function DropdownLongListDemo() {
  const items = Array.from({ length: 30 }, (_, i) => `Option ${i + 1}`);

  return (
    <DropdownMenu>
      <DropdownMenu.Trigger render={<Button>Open long list</Button>} />
      <DropdownMenu.Content>
        {items.map((item) => (
          <DropdownMenu.Item key={item}>{item}</DropdownMenu.Item>
        ))}
      </DropdownMenu.Content>
    </DropdownMenu>
  );
}
```

## [API Reference](#api-reference)

### [DropdownMenu](#dropdownmenu)

Root component that manages the dropdown state.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| variant | `"default" | "danger"` | `"default"` | Visual style of the dropdown item. - \`"default"\` — Standard item appearance - \`"danger"\` — Destructive action with red text |

### [DropdownMenu.Trigger](#dropdownmenutrigger)

Button that opens the dropdown when clicked.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [DropdownMenu.Item](#dropdownmenuitem)

Individual menu item for actions.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| icon | `Icon | ReactNode` | \- | Icon displayed before the label. |
| variant | `"default" | "danger"` | `"default"` | Visual style of the item. |
| selected | `boolean` | \- | Shows a check mark indicator when true. |
| inset | `boolean` | \- | Adds left padding to align with items that have icons. |
| onClick | `(event: React.MouseEvent) => void` | \- | Callback when the item is clicked. |
| closeOnClick | `boolean` | `true` | Whether the menu closes after clicking this item. |
| disabled | `boolean` | \- | When true, the item cannot be interacted with. |

### [DropdownMenu.LinkItem](#dropdownmenulinkitem)

A menu item that navigates to a URL. Renders a semantic `<a>` element. Use this instead of `Item` for navigation links.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| href | `string` | \- | URL to navigate to when clicked. |
| icon | `Icon | ReactNode` | \- | Icon displayed before the label. |
| variant | `"default" | "danger"` | `"default"` | Visual style of the item. |
| inset | `boolean` | \- | Adds left padding to align with items that have icons. |
| target | `string` | \- | Link target attribute (e.g. "\_blank" for new tab). |
| render | `ReactElement | ((props, state) => ReactElement)` | \- | Custom element to render as the link. Use to integrate with framework routers (e.g. Next.js Link). |

### [DropdownMenu.CheckboxItem](#dropdownmenucheckboxitem)

A menu item that can be toggled on or off. Use for independent boolean options.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| checked | `boolean` | \- | Whether the item is checked. |
| defaultChecked | `boolean` | `false` | Whether the item is initially checked (uncontrolled). |
| onCheckedChange | `(checked: boolean, event: ChangeEventDetails) => void` | \- | Callback when the checked state changes. |
| closeOnClick | `boolean` | `false` | Whether the menu closes after clicking this item. |
| disabled | `boolean` | \- | When true, the item cannot be interacted with. |

### [DropdownMenu.Sub](#dropdownmenusub)

Root component for a nested submenu. Wrap SubTrigger and SubContent inside this.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [DropdownMenu.SubTrigger](#dropdownmenusubtrigger)

Menu item that opens a nested submenu when hovered or clicked. Displays a caret icon automatically.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| icon | `Icon` | \- | Icon displayed before the label. |
| inset | `boolean` | \- | Adds left padding to align with items that have icons. |

### [DropdownMenu.SubContent](#dropdownmenusubcontent)

Container for submenu items. Positioned relative to the SubTrigger.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [DropdownMenu.Separator](#dropdownmenuseparator)

A visual divider between menu items.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [DropdownMenu.RadioGroup](#dropdownmenuradiogroup)

Groups radio items for single-selection behavior. Only one item can be selected at a time.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| value | `any` | \- | The controlled value of the currently selected radio item. |
| defaultValue | `any` | \- | The initially selected value (uncontrolled). |
| onValueChange | `(value: any, event: ChangeEventDetails) => void` | \- | Callback when the selected value changes. |
| disabled | `boolean` | \- | When true, all radio items in the group are disabled. |

### [DropdownMenu.RadioItem](#dropdownmenuradioitem)

A menu item that works like a radio button. Must be used inside a RadioGroup.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| value\* | `any` | \- | The value of this radio item. |
| icon | `Icon | ReactNode` | \- | Icon displayed before the label. |
| inset | `boolean` | \- | Adds left padding to align with items that have icons. |
| closeOnClick | `boolean` | `false` | Whether the menu closes after clicking this item. |
| disabled | `boolean` | \- | When true, the item cannot be interacted with. |

### [DropdownMenu.RadioItemIndicator](#dropdownmenuradioitemindicator)

Shows the selected state for a RadioItem. Displays a checkmark by default.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.