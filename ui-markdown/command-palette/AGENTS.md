# CommandPalette

A composable command palette component for search and command dialogs.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/command-palette/command-palette.tsx)

---

```
import { useState } from "react";
import { CommandPalette, Button } from "@cloudflare/kumo";

export function CommandPaletteBasicDemo() {
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");
  const [selectedItem, setSelectedItem] = useState<string | null>(null);

  const handleSelect = (item: CommandItem) => {
    setSelectedItem(item.title);
    setOpen(false);
    setSearch("");
  };

  // Filter groups based on search
  const filteredGroups = filterGroupsWithItems(sampleGroups, search);

  return (
    <div className="flex flex-col items-start gap-4">
      <Button onClick={() => setOpen(true)}>Open Command Palette</Button>
      {selectedItem && (
        <p className="text-sm text-kumo-subtle">
          Last selected:{" "}
          <span className="text-kumo-default">{selectedItem}</span>
        </p>
      )}

      <CommandPalette.Root
        open={open}
        onOpenChange={setOpen}
        items={filteredGroups}
        value={search}
        onValueChange={setSearch}
        itemToStringValue={(group) => group.label}
        onSelect={(item, { newTab }) => {
          console.log("Selected:", item.title, newTab ? "(new tab)" : "");
          handleSelect(item);
        }}
        getSelectableItems={getSelectableItems}
      >
        <CommandPalette.Input placeholder="Type a command or search..." />
        <CommandPalette.List>
          <CommandPalette.Results>
            {(group: CommandGroup) => (
              <CommandPalette.Group key={group.id} items={group.items}>
                <CommandPalette.GroupLabel>
                  {group.label}
                </CommandPalette.GroupLabel>
                <CommandPalette.Items>
                  {(item: CommandItem) => (
                    <CommandPalette.Item
                      key={item.id}
                      value={item}
                      onClick={() => handleSelect(item)}
                    >
                      <span className="flex items-center gap-3">
                        {item.icon && (
                          <span className="text-kumo-subtle">{item.icon}</span>
                        )}
                        <span>{item.title}</span>
                      </span>
                    </CommandPalette.Item>
                  )}
                </CommandPalette.Items>
              </CommandPalette.Group>
            )}
          </CommandPalette.Results>
          <CommandPalette.Empty>No commands found</CommandPalette.Empty>
        </CommandPalette.List>
        <CommandPalette.Footer>
          <span className="flex items-center gap-2">
            <kbd className="rounded border border-kumo-hairline bg-kumo-base px-1.5 py-0.5 text-[10px]">
              ↑↓
            </kbd>
            <span>Navigate</span>
          </span>
          <span className="flex items-center gap-2">
            <kbd className="rounded border border-kumo-hairline bg-kumo-base px-1.5 py-0.5 text-[10px]">
              ↵
            </kbd>
            <span>Select</span>
          </span>
        </CommandPalette.Footer>
      </CommandPalette.Root>
    </div>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { CommandPalette } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { CommandPalette } from "@cloudflare/kumo/components/command-palette";
```

## [Usage](#usage)

CommandPalette is a compound component built on Base UI’s Autocomplete primitive. It provides accessible keyboard navigation and customizable styling for command palette interfaces.

```
import { useState } from "react";
import { CommandPalette } from "@cloudflare/kumo";

interface Item {
  id: string;
  title: string;
}

const items: Item[] = [
  { id: "1", title: "Create Project" },
  { id: "2", title: "Open Settings" },
];

export default function Example() {
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");

  return (
    <>
      <button onClick={() => setOpen(true)}>Open</button>
      <CommandPalette.Root
        open={open}
        onOpenChange={setOpen}
        items={items}
        value={search}
        onValueChange={setSearch}
        itemToStringValue={(item) => item.title}
        getSelectableItems={(items) => items}
      >
        <CommandPalette.Input placeholder="Search..." />
        <CommandPalette.List>
          <CommandPalette.Results>
            {(item) => (
              <CommandPalette.Item
                key={item.id}
                value={item}
                onClick={() => setOpen(false)}
              >
                {item.title}
              </CommandPalette.Item>
            )}
          </CommandPalette.Results>
          <CommandPalette.Empty>No results</CommandPalette.Empty>
        </CommandPalette.List>
      </CommandPalette.Root>
    </>
  );
}
```

## [Keyboard Navigation](#keyboard-navigation)

Built-in keyboard navigation is provided automatically:

↑+↓Move highlight between items

EnterSelect highlighted item

⌘/Ctrl+EnterSelect with newTab: true

EscapeClose the dialog

## [Examples](#examples)

### [With Grouped Items](#with-grouped-items)

Group related commands together with labels.

```
import { useState } from "react";
import { CommandPalette, Button } from "@cloudflare/kumo";

export function CommandPaletteBasicDemo() {
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");
  const [selectedItem, setSelectedItem] = useState<string | null>(null);

  const handleSelect = (item: CommandItem) => {
    setSelectedItem(item.title);
    setOpen(false);
    setSearch("");
  };

  // Filter groups based on search
  const filteredGroups = filterGroupsWithItems(sampleGroups, search);

  return (
    <div className="flex flex-col items-start gap-4">
      <Button onClick={() => setOpen(true)}>Open Command Palette</Button>
      {selectedItem && (
        <p className="text-sm text-kumo-subtle">
          Last selected:{" "}
          <span className="text-kumo-default">{selectedItem}</span>
        </p>
      )}

      <CommandPalette.Root
        open={open}
        onOpenChange={setOpen}
        items={filteredGroups}
        value={search}
        onValueChange={setSearch}
        itemToStringValue={(group) => group.label}
        onSelect={(item, { newTab }) => {
          console.log("Selected:", item.title, newTab ? "(new tab)" : "");
          handleSelect(item);
        }}
        getSelectableItems={getSelectableItems}
      >
        <CommandPalette.Input placeholder="Type a command or search..." />
        <CommandPalette.List>
          <CommandPalette.Results>
            {(group: CommandGroup) => (
              <CommandPalette.Group key={group.id} items={group.items}>
                <CommandPalette.GroupLabel>
                  {group.label}
                </CommandPalette.GroupLabel>
                <CommandPalette.Items>
                  {(item: CommandItem) => (
                    <CommandPalette.Item
                      key={item.id}
                      value={item}
                      onClick={() => handleSelect(item)}
                    >
                      <span className="flex items-center gap-3">
                        {item.icon && (
                          <span className="text-kumo-subtle">{item.icon}</span>
                        )}
                        <span>{item.title}</span>
                      </span>
                    </CommandPalette.Item>
                  )}
                </CommandPalette.Items>
              </CommandPalette.Group>
            )}
          </CommandPalette.Results>
          <CommandPalette.Empty>No commands found</CommandPalette.Empty>
        </CommandPalette.List>
        <CommandPalette.Footer>
          <span className="flex items-center gap-2">
            <kbd className="rounded border border-kumo-hairline bg-kumo-base px-1.5 py-0.5 text-[10px]">
              ↑↓
            </kbd>
            <span>Navigate</span>
          </span>
          <span className="flex items-center gap-2">
            <kbd className="rounded border border-kumo-hairline bg-kumo-base px-1.5 py-0.5 text-[10px]">
              ↵
            </kbd>
            <span>Select</span>
          </span>
        </CommandPalette.Footer>
      </CommandPalette.Root>
    </div>
  );
}
```

### [Simple Flat List](#simple-flat-list)

For simpler use cases, use a flat array of items without grouping.

```
import { useState } from "react";
import { CommandPalette, Button } from "@cloudflare/kumo";

export function CommandPaletteSimpleDemo() {
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");

  return (
    <div>
      <Button onClick={() => setOpen(true)}>Open Simple Palette</Button>

      <CommandPalette.Root
        open={open}
        onOpenChange={setOpen}
        items={simpleItems}
        value={search}
        onValueChange={setSearch}
        itemToStringValue={(item) => item.title}
        onSelect={(item) => {
          console.log("Selected:", item.title);
          setOpen(false);
        }}
        getSelectableItems={(items) => items}
      >
        <CommandPalette.Input placeholder="Search actions..." />
        <CommandPalette.List>
          <CommandPalette.Results>
            {(item: SimpleItem) => (
              <CommandPalette.Item
                key={item.id}
                value={item}
                onClick={() => {
                  console.log("Clicked:", item.title);
                  setOpen(false);
                }}
              >
                {item.title}
              </CommandPalette.Item>
            )}
          </CommandPalette.Results>
          <CommandPalette.Empty>No actions found</CommandPalette.Empty>
        </CommandPalette.List>
      </CommandPalette.Root>
    </div>
  );
}
```

### [Loading State](#loading-state)

Show a loading spinner while fetching results.

```
import { useState } from "react";
import { CommandPalette, Button } from "@cloudflare/kumo";

// With loading state
export function CommandPaletteLoadingDemo() {
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [search, setSearch] = useState("");

  const handleOpen = () => {
    setOpen(true);
    setLoading(true);
    // Simulate loading
    setTimeout(() => setLoading(false), 1500);
  };

  // Filter groups based on search
  const filteredGroups = filterGroupsWithItems(sampleGroups, search);

  return (
    <div>
      <Button onClick={handleOpen}>Open with Loading</Button>

      <CommandPalette.Root
        open={open}
        onOpenChange={setOpen}
        items={loading ? [] : filteredGroups}
        value={search}
        onValueChange={setSearch}
        itemToStringValue={(group) => group.label}
        getSelectableItems={getSelectableItems}
      >
        <CommandPalette.Input placeholder="Search..." />
        <CommandPalette.List>
          {loading ? (
            <CommandPalette.Loading />
          ) : (
            <>
              <CommandPalette.Results>
                {(group: CommandGroup) => (
                  <CommandPalette.Group key={group.id} items={group.items}>
                    <CommandPalette.GroupLabel>
                      {group.label}
                    </CommandPalette.GroupLabel>
                    <CommandPalette.Items>
                      {(item: CommandItem) => (
                        <CommandPalette.Item
                          key={item.id}
                          value={item}
                          onClick={() => setOpen(false)}
                        >
                          <span className="flex items-center gap-3">
                            {item.icon && (
                              <span className="text-kumo-subtle">
                                {item.icon}
                              </span>
                            )}
                            <span>{item.title}</span>
                          </span>
                        </CommandPalette.Item>
                      )}
                    </CommandPalette.Items>
                  </CommandPalette.Group>
                )}
              </CommandPalette.Results>
              <CommandPalette.Empty>No results found</CommandPalette.Empty>
            </>
          )}
        </CommandPalette.List>
      </CommandPalette.Root>
    </div>
  );
}
```

### [Disabling Browser Autocomplete](#disabling-browser-autocomplete)

Pass standard HTML input attributes like `autoComplete`, `autoCorrect`, `spellCheck`, and `data-*` to suppress browser and password manager autocomplete overlays.

```
import { useState } from "react";
import { CommandPalette, Button } from "@cloudflare/kumo";

/** Demonstrates disabling browser autocomplete and spellcheck on the command palette input. */
export function CommandPaletteNoAutocompleteDemo() {
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");

  const filteredGroups = filterGroupsWithItems(sampleGroups, search);

  return (
    <div className="flex flex-col items-start gap-4">
      <Button onClick={() => setOpen(true)}>
        Open Palette (No Autocomplete)
      </Button>

      <CommandPalette.Root
        open={open}
        onOpenChange={setOpen}
        items={filteredGroups}
        value={search}
        onValueChange={setSearch}
        itemToStringValue={(group) => group.label}
        onSelect={(item) => {
          console.log("Selected:", item.title);
          setOpen(false);
          setSearch("");
        }}
        getSelectableItems={getSelectableItems}
      >
        <CommandPalette.Input
          placeholder="Search commands..."
          autoComplete="off"
          autoCorrect="off"
          autoCapitalize="none"
          spellCheck={false}
          data-1p-ignore="true"
          data-lpignore="true"
        />
        <CommandPalette.List>
          <CommandPalette.Results>
            {(group: CommandGroup) => (
              <CommandPalette.Group key={group.id} items={group.items}>
                <CommandPalette.GroupLabel>
                  {group.label}
                </CommandPalette.GroupLabel>
                <CommandPalette.Items>
                  {(item: CommandItem) => (
                    <CommandPalette.Item
                      key={item.id}
                      value={item}
                      onClick={() => {
                        setOpen(false);
                        setSearch("");
                      }}
                    >
                      <span className="flex items-center gap-3">
                        {item.icon && (
                          <span className="text-kumo-subtle">{item.icon}</span>
                        )}
                        <span>{item.title}</span>
                      </span>
                    </CommandPalette.Item>
                  )}
                </CommandPalette.Items>
              </CommandPalette.Group>
            )}
          </CommandPalette.Results>
          <CommandPalette.Empty>No commands found</CommandPalette.Empty>
        </CommandPalette.List>
      </CommandPalette.Root>
    </div>
  );
}
```

### [ResultItem with Breadcrumbs](#resultitem-with-breadcrumbs)

Use `ResultItem` for rich items with breadcrumbs, icons, and optional text highlighting.

```
import { useState } from "react";
import { CommandPalette, Button } from "@cloudflare/kumo";

export function CommandPaletteResultItemDemo() {
  const [open, setOpen] = useState(false);
  const [search, setSearch] = useState("");

  return (
    <div>
      <Button onClick={() => setOpen(true)}>Open with ResultItem</Button>

      <CommandPalette.Root
        open={open}
        onOpenChange={setOpen}
        items={searchResults}
        value={search}
        onValueChange={setSearch}
        itemToStringValue={(item) => item.title}
        getSelectableItems={(items) => items}
      >
        <CommandPalette.Input placeholder="Search documentation..." />
        <CommandPalette.List>
          <CommandPalette.Results>
            {(item: SearchResult) => (
              <CommandPalette.ResultItem
                key={item.id}
                value={item}
                title={item.title}
                breadcrumbs={item.breadcrumbs}
                icon={item.icon}
                onClick={() => {
                  console.log("Navigate to:", item.title);
                  setOpen(false);
                }}
              />
            )}
          </CommandPalette.Results>
          <CommandPalette.Empty>No pages found</CommandPalette.Empty>
        </CommandPalette.List>
        <CommandPalette.Footer>
          <span className="flex items-center gap-2">
            <kbd className="rounded border border-kumo-hairline bg-kumo-base px-1.5 py-0.5 text-[10px]">
              ↑↓
            </kbd>
            <span>Navigate</span>
          </span>
          <span className="flex items-center gap-2">
            <kbd className="rounded border border-kumo-hairline bg-kumo-base px-1.5 py-0.5 text-[10px]">
              ⌘↵
            </kbd>
            <span>Open in new tab</span>
          </span>
        </CommandPalette.Footer>
      </CommandPalette.Root>
    </div>
  );
}
```

## [Component Parts](#component-parts)

### [CommandPalette.Root](#commandpaletteroot)

The main wrapper that combines Dialog + Panel. Manages open state and Autocomplete functionality.

### [CommandPalette.Dialog](#commandpalettedialog)

Modal dialog wrapper. Use with Panel for swappable content (e.g., drill-down navigation).

### [CommandPalette.Panel](#commandpalettepanel)

Autocomplete panel without dialog. Use inside Dialog for content that can swap without re-mounting.

### [CommandPalette.Input](#commandpaletteinput)

Search input field with auto-focus and keyboard handling.

### [CommandPalette.List](#commandpalettelist)

Scrollable container for results.

### [CommandPalette.Results](#commandpaletteresults)

Render prop iterator for items/groups.

### [CommandPalette.Group](#commandpalettegroup)

Category grouping container.

### [CommandPalette.GroupLabel](#commandpalettegrouplabel)

Section header text within a group.

### [CommandPalette.Items](#commandpaletteitems)

Render prop iterator for items within a group.

### [CommandPalette.Item](#commandpaletteitem)

Basic selectable item.

### [CommandPalette.ResultItem](#commandpaletteresultitem)

Rich item with breadcrumbs, icons, and text highlighting.

### [CommandPalette.HighlightedText](#commandpalettehighlightedtext)

Renders text with highlighted portions based on match indices.

### [CommandPalette.Empty](#commandpaletteempty)

Empty state when no results match.

### [CommandPalette.Loading](#commandpaletteloading)

Loading spinner state.

### [CommandPalette.Footer](#commandpalettefooter)

Footer for keyboard hints or other content.

## [API Reference](#api-reference)

### [CommandPalette.Root Props](#commandpaletteroot-props)

```
interface CommandPaletteRootProps<TGroup, TItem> {
  // Dialog state
  open: boolean;
  onOpenChange: (open: boolean) => void;
  onBackdropClick?: (e: React.MouseEvent) => void;

  // Autocomplete
  items: TGroup[];
  value?: string;
  onValueChange?: (value: string) => void;
  itemToStringValue?: (item: TGroup) => string;
  filter?: (item: TGroup, query: string) => boolean;
  onItemHighlighted?: (item: TGroup | undefined, details: {...}) => void;

  // Selection
  onSelect?: (item: TItem, options: { newTab: boolean }) => void;
  getSelectableItems?: (items: TGroup[]) => TItem[];

  children: React.ReactNode;
}
```

### [CommandPalette.ResultItem Props](#commandpaletteresultitem-props)

```
interface CommandPaletteResultItemProps<T> {
  value: T;
  title: string;
  breadcrumbs?: string[];
  titleHighlights?: [number, number][];
  breadcrumbHighlights?: [number, number][][];
  description?: string;
  icon?: React.ReactNode;
  onClick: (e: React.MouseEvent) => void;
  showArrow?: boolean; // default: true
  external?: boolean; // shows external link icon
  nonInteractive?: boolean;
}
```