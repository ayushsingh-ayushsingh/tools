# Table

A table component for displaying tabular data with support for selection, row variants, and column sizing.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/table/table.tsx)

---

```
import { LayerCard, Table } from "@cloudflare/kumo";

export function TableBasicDemo() {
  return (
    <LayerCard className="p-0">
      <Table>
        <Table.Header>
          <Table.Row>
            <Table.Head>Subject</Table.Head>
            <Table.Head>From</Table.Head>
            <Table.Head>Date</Table.Head>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {emailData.slice(0, 3).map((row) => (
            <Table.Row key={row.id}>
              <Table.Cell>{row.subject}</Table.Cell>
              <Table.Cell>{row.from}</Table.Cell>
              <Table.Cell>{row.date}</Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table>
    </LayerCard>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Table } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Table } from "@cloudflare/kumo/components/table";
```

## [Usage](#usage)

```
import { Table, LayerCard } from "@cloudflare/kumo";

export default function Example() {
  return (
    <LayerCard className="p-0">
      <Table>
        <Table.Header>
          <Table.Row>
            <Table.Head>Name</Table.Head>
            <Table.Head>Email</Table.Head>
            <Table.Head>Role</Table.Head>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          <Table.Row>
            <Table.Cell>John Doe</Table.Cell>
            <Table.Cell>john@example.com</Table.Cell>
            <Table.Cell>Admin</Table.Cell>
          </Table.Row>
        </Table.Body>
      </Table>
    </LayerCard>
  );
}
```

## [Examples](#examples)

### [With Checkboxes](#with-checkboxes)

Add row selection with `Table.CheckHead` and `Table.CheckCell`. Both accept `onCheckedChange`, which matches the underlying `Checkbox` component’s signature and exposes optional event details as a second argument.

The older `onValueChange` prop still works but is deprecated — the lint rule will flag it and it will be removed in a future major version. Migrate by renaming the prop:

```
// Before (deprecated)
<Table.CheckCell onValueChange={(checked) => toggleRow(id)} />

// After
<Table.CheckCell onCheckedChange={(checked) => toggleRow(id)} />

// With event details
<Table.CheckCell
  onCheckedChange={(checked, eventDetails) => {
    toggleRow(id);
    eventDetails?.event.stopPropagation();
  }}
/>
```

```
import { useState } from "react";
import { LayerCard, Table } from "@cloudflare/kumo";

export function TableWithCheckboxDemo() {
  const rows = emailData.slice(0, 3);
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());

  const toggleRow = (id: string) => {
    setSelectedIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) {
        next.delete(id);
      } else {
        next.add(id);
      }
      return next;
    });
  };

  const toggleAll = () => {
    if (selectedIds.size === rows.length) {
      setSelectedIds(new Set());
    } else {
      setSelectedIds(new Set(rows.map((r) => r.id)));
    }
  };

  return (
    <LayerCard className="p-0">
      <Table>
        <Table.Header>
          <Table.Row>
            <Table.CheckHead
              checked={selectedIds.size === rows.length}
              indeterminate={
                selectedIds.size > 0 && selectedIds.size < rows.length
              }
              onCheckedChange={toggleAll}
              aria-label="Select all rows"
            />
            <Table.Head>Subject</Table.Head>
            <Table.Head>From</Table.Head>
            <Table.Head>Date</Table.Head>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {rows.map((row) => (
            <Table.Row key={row.id}>
              <Table.CheckCell
                checked={selectedIds.has(row.id)}
                onCheckedChange={() => toggleRow(row.id)}
                aria-label={`Select ${row.subject}`}
              />
              <Table.Cell>{row.subject}</Table.Cell>
              <Table.Cell>{row.from}</Table.Cell>
              <Table.Cell>{row.date}</Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table>
    </LayerCard>
  );
}
```

### [Compact Header](#compact-header)

Use `variant="compact"` on `Table.Header` for a more condensed header style.

```
import { LayerCard, Table } from "@cloudflare/kumo";

export function TableWithCompactHeaderDemo() {
  return (
    <LayerCard className="p-0">
      <Table>
        <Table.Header variant="compact">
          <Table.Row>
            <Table.Head>Subject</Table.Head>
            <Table.Head>From</Table.Head>
            <Table.Head>Date</Table.Head>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {emailData.slice(0, 3).map((row) => (
            <Table.Row key={row.id}>
              <Table.Cell>{row.subject}</Table.Cell>
              <Table.Cell>{row.from}</Table.Cell>
              <Table.Cell>{row.date}</Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table>
    </LayerCard>
  );
}
```

### [Selected Row](#selected-row)

Use `variant="selected"` on `Table.Row` to highlight selected rows.

```
import { useState } from "react";
import { LayerCard, Table } from "@cloudflare/kumo";

export function TableSelectedRowDemo() {
  const rows = emailData.slice(0, 3);
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set(["2"]));

  const toggleRow = (id: string) => {
    setSelectedIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) {
        next.delete(id);
      } else {
        next.add(id);
      }
      return next;
    });
  };

  const toggleAll = () => {
    if (selectedIds.size === rows.length) {
      setSelectedIds(new Set());
    } else {
      setSelectedIds(new Set(rows.map((r) => r.id)));
    }
  };

  return (
    <LayerCard className="p-0">
      <Table>
        <Table.Header>
          <Table.Row>
            <Table.CheckHead
              checked={selectedIds.size === rows.length}
              indeterminate={
                selectedIds.size > 0 && selectedIds.size < rows.length
              }
              onCheckedChange={toggleAll}
              aria-label="Select all rows"
            />
            <Table.Head>Subject</Table.Head>
            <Table.Head>From</Table.Head>
            <Table.Head>Date</Table.Head>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {rows.map((row) => (
            <Table.Row
              key={row.id}
              variant={selectedIds.has(row.id) ? "selected" : "default"}
            >
              <Table.CheckCell
                checked={selectedIds.has(row.id)}
                onCheckedChange={() => toggleRow(row.id)}
                aria-label={`Select ${row.subject}`}
              />
              <Table.Cell>{row.subject}</Table.Cell>
              <Table.Cell>{row.from}</Table.Cell>
              <Table.Cell>{row.date}</Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table>
    </LayerCard>
  );
}
```

### [Fixed Layout with Column Sizes](#fixed-layout-with-column-sizes)

For precise control over column widths, set `layout="fixed"` and use `colgroup` with `col` elements.

```
import { LayerCard, Table } from "@cloudflare/kumo";

export function TableFixedLayoutDemo() {
  return (
    <LayerCard className="p-0">
      <Table layout="fixed">
        <colgroup>
          <col />
          <col className="w-[150px]" />
          <col className="w-[150px]" />
        </colgroup>
        <Table.Header>
          <Table.Row>
            <Table.Head>Subject</Table.Head>
            <Table.Head>From</Table.Head>
            <Table.Head>Date</Table.Head>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {emailData.map((row) => (
            <Table.Row key={row.id}>
              <Table.Cell>{row.subject}</Table.Cell>
              <Table.Cell>{row.from}</Table.Cell>
              <Table.Cell>{row.date}</Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table>
    </LayerCard>
  );
}
```

### [Sticky Column](#sticky-column)

Pin a column to the left or right edge of the scroll container with `sticky="left"` or `sticky="right"` on `Table.Head` and `Table.Cell`. The component automatically adds an opaque background and gradient fade. Wrap the table in an `overflow-x-auto` container.

```
import { Badge, Button, DropdownMenu, LayerCard, Table } from "@cloudflare/kumo";
import { DotsThree, Eye, PencilSimple, Trash } from "@phosphor-icons/react";

/**
 * Demonstrates a sticky right-hand actions column that stays pinned while the
 * table scrolls horizontally. Uses `sticky="right"` on `Table.Head` and
 * `Table.Cell` — the gradient fade and opaque background are applied
 * automatically.
 */
export function TableStickyColumnDemo() {
  return (
    <LayerCard className="w-full max-w-md overflow-x-auto p-0">
      <Table>
        <Table.Header>
          <Table.Row>
            <Table.Head>Subject</Table.Head>
            <Table.Head>From</Table.Head>
            <Table.Head>Date</Table.Head>
            <Table.Head>Tags</Table.Head>
            <Table.Head sticky="right">
              <span className="sr-only">Actions</span>
            </Table.Head>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {emailData.map((row) => (
            <Table.Row key={row.id}>
              <Table.Cell className="whitespace-nowrap">
                {row.subject}
              </Table.Cell>
              <Table.Cell className="whitespace-nowrap">{row.from}</Table.Cell>
              <Table.Cell className="whitespace-nowrap">{row.date}</Table.Cell>
              <Table.Cell className="whitespace-nowrap">
                {row.tags ? (
                  <div className="inline-flex gap-1">
                    {row.tags.map((tag) => (
                      <Badge key={tag}>{tag}</Badge>
                    ))}
                  </div>
                ) : (
                  "—"
                )}
              </Table.Cell>
              <Table.Cell sticky="right" className="text-right">
                <DropdownMenu>
                  <DropdownMenu.Trigger
                    render={
                      <Button
                        variant="ghost"
                        size="sm"
                        shape="square"
                        aria-label="More options"
                      >
                        <DotsThree weight="bold" size={16} />
                      </Button>
                    }
                  />
                  <DropdownMenu.Content>
                    <DropdownMenu.Item icon={Eye}>View</DropdownMenu.Item>
                    <DropdownMenu.Item icon={PencilSimple}>
                      Edit
                    </DropdownMenu.Item>
                    <DropdownMenu.Separator />
                    <DropdownMenu.Item icon={Trash} variant="danger">
                      Delete
                    </DropdownMenu.Item>
                  </DropdownMenu.Content>
                </DropdownMenu>
              </Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table>
    </LayerCard>
  );
}
```

### [Compact Header with Sticky Column](#compact-header-with-sticky-column)

Combining `variant="compact"` on `Table.Header` with `sticky` columns.

```
import { Badge, Button, DropdownMenu, LayerCard, Table } from "@cloudflare/kumo";
import { DotsThree, Eye, PencilSimple, Trash } from "@phosphor-icons/react";

/**
 * Demonstrates a compact header combined with sticky columns. This combination
 * may exhibit visual inconsistencies between the compact header background
 * (`bg-kumo-elevated`) and the sticky cell background (`bg-kumo-base`).
 */
export function TableCompactStickyDemo() {
  return (
    <LayerCard className="w-full max-w-md overflow-x-auto p-0">
      <Table>
        <Table.Header variant="compact">
          <Table.Row>
            <Table.Head>Subject</Table.Head>
            <Table.Head>From</Table.Head>
            <Table.Head>Date</Table.Head>
            <Table.Head>Tags</Table.Head>
            <Table.Head sticky="right">
              <span className="sr-only">Actions</span>
            </Table.Head>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {emailData.map((row) => (
            <Table.Row key={row.id}>
              <Table.Cell className="whitespace-nowrap">
                {row.subject}
              </Table.Cell>
              <Table.Cell className="whitespace-nowrap">{row.from}</Table.Cell>
              <Table.Cell className="whitespace-nowrap">{row.date}</Table.Cell>
              <Table.Cell className="whitespace-nowrap">
                {row.tags ? (
                  <div className="inline-flex gap-1">
                    {row.tags.map((tag) => (
                      <Badge key={tag}>{tag}</Badge>
                    ))}
                  </div>
                ) : (
                  "—"
                )}
              </Table.Cell>
              <Table.Cell sticky="right" className="text-right">
                <DropdownMenu>
                  <DropdownMenu.Trigger
                    render={
                      <Button
                        variant="ghost"
                        size="sm"
                        shape="square"
                        aria-label="More options"
                      >
                        <DotsThree weight="bold" size={16} />
                      </Button>
                    }
                  />
                  <DropdownMenu.Content>
                    <DropdownMenu.Item icon={Eye}>View</DropdownMenu.Item>
                    <DropdownMenu.Item icon={PencilSimple}>
                      Edit
                    </DropdownMenu.Item>
                    <DropdownMenu.Separator />
                    <DropdownMenu.Item icon={Trash} variant="danger">
                      Delete
                    </DropdownMenu.Item>
                  </DropdownMenu.Content>
                </DropdownMenu>
              </Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table>
    </LayerCard>
  );
}
```

### [Full Example](#full-example)

Complete table with checkboxes, badges, action buttons, and fixed column widths.

 

```
import { useState } from "react";
import { Badge, Button, DropdownMenu, LayerCard, Table } from "@cloudflare/kumo";
import { DotsThree, EnvelopeSimple, Eye, PencilSimple, Trash } from "@phosphor-icons/react";

export function TableFullDemo() {
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set(["2"]));

  const toggleRow = (id: string) => {
    setSelectedIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) {
        next.delete(id);
      } else {
        next.add(id);
      }
      return next;
    });
  };

  const toggleAll = () => {
    if (selectedIds.size === emailData.length) {
      setSelectedIds(new Set());
    } else {
      setSelectedIds(new Set(emailData.map((r) => r.id)));
    }
  };

  return (
    <LayerCard className="w-full overflow-x-auto p-0">
      <Table layout="fixed">
        <colgroup>
          <col />{" "}
          {/* Checkbox column - width handled by Table.CheckHead/CheckCell */}
          <col />
          <col style={{ width: "150px" }} />
          <col style={{ width: "120px" }} />
          <col style={{ width: "50px" }} />
        </colgroup>
        <Table.Header>
          <Table.Row>
            <Table.CheckHead
              checked={selectedIds.size === emailData.length}
              indeterminate={
                selectedIds.size > 0 && selectedIds.size < emailData.length
              }
              onCheckedChange={toggleAll}
              aria-label="Select all rows"
            />
            <Table.Head>Subject</Table.Head>
            <Table.Head>From</Table.Head>
            <Table.Head>Date</Table.Head>
            <Table.Head></Table.Head>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {emailData.map((row) => (
            <Table.Row
              key={row.id}
              variant={selectedIds.has(row.id) ? "selected" : "default"}
            >
              <Table.CheckCell
                checked={selectedIds.has(row.id)}
                onCheckedChange={() => toggleRow(row.id)}
                aria-label={`Select ${row.subject}`}
              />
              <Table.Cell>
                <div className="flex items-center gap-2">
                  <EnvelopeSimple size={16} />
                  <span className="truncate">{row.subject}</span>
                  {row.tags && (
                    <div className="ml-2 inline-flex gap-1">
                      {row.tags.map((tag) => (
                        <Badge key={tag}>{tag}</Badge>
                      ))}
                    </div>
                  )}
                </div>
              </Table.Cell>
              <Table.Cell>
                <span className="truncate">{row.from}</span>
              </Table.Cell>
              <Table.Cell>
                <span className="truncate">{row.date}</span>
              </Table.Cell>
              <Table.Cell className="text-right">
                <DropdownMenu>
                  <DropdownMenu.Trigger
                    render={
                      <Button
                        variant="ghost"
                        size="sm"
                        shape="square"
                        aria-label="More options"
                      >
                        <DotsThree weight="bold" size={16} />
                      </Button>
                    }
                  />
                  <DropdownMenu.Content>
                    <DropdownMenu.Item icon={Eye}>View</DropdownMenu.Item>
                    <DropdownMenu.Item icon={PencilSimple}>
                      Edit
                    </DropdownMenu.Item>
                    <DropdownMenu.Separator />
                    <DropdownMenu.Item icon={Trash} variant="danger">
                      Delete
                    </DropdownMenu.Item>
                  </DropdownMenu.Content>
                </DropdownMenu>
              </Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table>
    </LayerCard>
  );
}
```

## [API Reference](#api-reference)

### [Table](#table)

Root table component. Renders a semantic `<table>` element.

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| layout | `"auto" | "fixed"` | `"auto"` | \- |
| variant | `"default" | "selected"` | `"default"` | \- |
| sticky | `"left" | "right"` | \- | \- |
| className | `string` | \- | Additional CSS classes |
| children | `ReactNode` | \- | Child elements |

### [Table.Header](#tableheader)

Table header section. Renders `<thead>`. Set `sticky` to pin the header row to the top of the scroll container.

### [Table.Body](#tablebody)

Table body section. Renders `<tbody>`.

### [Table.Row](#tablerow)

Table row. Supports `variant="selected"` for highlighting.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Table.Head](#tablehead)

Header cell. Renders `<th>`. Accepts `sticky="left"` or `sticky="right"` to pin the column.

### [Table.Cell](#tablecell)

Body cell. Renders `<td>`. Accepts `sticky="left"` or `sticky="right"` to pin the column.

### [Table.CheckHead](#tablecheckhead)

Header cell with checkbox for “select all” functionality.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Table.CheckCell](#tablecheckcell)

Body cell with checkbox for row selection.

| Prop | Type | Default |
| --- | --- | --- |

No component-specific props. Accepts standard HTML attributes.

### [Table.ResizeHandle](#tableresizehandle)

Draggable handle for column resizing. Use with TanStack Table or custom resize logic.

## [TanStack Table Integration](#tanstack-table-integration)

For advanced features like sorting, filtering, and resizable columns, integrate with [TanStack Table](https://tanstack.com/table). The Table component is designed to work seamlessly with TanStack’s headless API.

```
import {
  flexRender,
  getCoreRowModel,
  useReactTable,
} from "@tanstack/react-table";
import { Table } from "@cloudflare/kumo";

function DataTable({ data, columns }) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    columnResizeMode: "onChange",
  });

  return (
    <Table layout="fixed">
      <colgroup>
        {table.getAllColumns().map((column) => (
          <col key={column.id} style={{ width: column.getSize() }} />
        ))}
      </colgroup>
      <Table.Header>
        {table.getHeaderGroups().map((headerGroup) => (
          <Table.Row key={headerGroup.id}>
            {headerGroup.headers.map((header) => (
              <Table.Head key={header.id}>
                {flexRender(
                  header.column.columnDef.header,
                  header.getContext(),
                )}
                <Table.ResizeHandle
                  onMouseDown={header.getResizeHandler()}
                  onTouchStart={header.getResizeHandler()}
                />
              </Table.Head>
            ))}
          </Table.Row>
        ))}
      </Table.Header>
      <Table.Body>
        {table.getRowModel().rows.map((row) => (
          <Table.Row key={row.id}>
            {row.getVisibleCells().map((cell) => (
              <Table.Cell key={cell.id}>
                {flexRender(cell.column.columnDef.cell, cell.getContext())}
              </Table.Cell>
            ))}
          </Table.Row>
        ))}
      </Table.Body>
    </Table>
  );
}
```

## [Accessibility](#accessibility)

### [Semantic HTML](#semantic-html)

Table uses semantic `<table>`, `<thead>`, `<tbody>`, `<th>`, and `<td>` elements for proper screen reader navigation.

### [Checkbox Labels](#checkbox-labels)

Always provide `aria-label` for `Table.CheckHead` and `Table.CheckCell` to describe their purpose.

### [Keyboard Navigation](#keyboard-navigation)

Tab moves focus through interactive elements. Checkboxes respond to Space.