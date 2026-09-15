# Pagination

A page navigation component for navigating through paginated content.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/pagination/pagination.tsx)

---

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

export function PaginationBasicDemo() {
  const [page, setPage] = useState(1);

  return (
    <Pagination page={page} setPage={setPage} perPage={10} totalCount={100} />
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Pagination } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Pagination } from "@cloudflare/kumo/components/pagination";
```

## [Usage](#usage)

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

export default function Example() {
  const [page, setPage] = useState(1);

  return (
    <Pagination page={page} setPage={setPage} perPage={10} totalCount={100} />
  );
}
```

## [Examples](#examples)

### [Full Controls (Default)](#full-controls-default)

The default pagination includes first, previous, page input, next, and last buttons.

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

export function PaginationFullDemo() {
  const [page, setPage] = useState(1);

  return (
    <Pagination
      page={page}
      setPage={setPage}
      perPage={10}
      totalCount={100}
      controls="full"
    />
  );
}
```

### [Simple Controls](#simple-controls)

Use `controls="simple"` for a minimal pagination with only previous and next buttons.

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

export function PaginationSimpleDemo() {
  const [page, setPage] = useState(1);

  return (
    <Pagination
      page={page}
      setPage={setPage}
      perPage={10}
      totalCount={100}
      controls="simple"
    />
  );
}
```

### [Unknown Totals](#unknown-totals)

Use `hasNextPage` when the data source does not return a total count. This is common for cursor-based APIs, where calculating the total can be expensive or unavailable. Set it from the response’s next-page signal to keep Next enabled only while another result set exists.

Without a total, users can only move sequentially, so Pagination hides the first, last, and page-selector controls. The `page` value remains useful for the UI, but your application is responsible for storing and sending the cursor or continuation token for each request.

```
const [page, setPage] = useState(1);
const { data } = useQuery({
  queryKey: ["events", page],
  queryFn: () => getEvents({ cursor: cursors[page - 1] }),
});

return (
  <Pagination
    page={page}
    setPage={setPage}
    hasNextPage={data.hasMore}
    text={() => `Page ${page}`}
  />
);
```

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

/** Pagination for an API that reports whether another page exists, but not a total. */
export function PaginationUnknownTotalDemo() {
  const [page, setPage] = useState(1);
  const hasNextPage = page < 3;

  return (
    <Pagination
      text={() => `Page ${page}`}
      page={page}
      setPage={setPage}
      hasNextPage={hasNextPage}
    />
  );
}
```

### [Mid-Page State](#mid-page-state)

Pagination in the middle of a dataset with all navigation enabled.

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

export function PaginationMidPageDemo() {
  const [page, setPage] = useState(5);

  return (
    <Pagination page={page} setPage={setPage} perPage={10} totalCount={100} />
  );
}
```

### [Large Dataset](#large-dataset)

Pagination handles large datasets with many pages.

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

export function PaginationLargeDatasetDemo() {
  const [page, setPage] = useState(1);

  return (
    <Pagination page={page} setPage={setPage} perPage={25} totalCount={1250} />
  );
}
```

### [Custom Text](#custom-text)

You can set custom pagination text.

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

export function PaginationCustomTextDemo() {
  const [page, setPage] = useState(1);
  return (
    <Pagination
      text={({ perPage }: { perPage?: number }) =>
        `Page ${page} - showing ${perPage} per page`
      }
      page={page}
      setPage={setPage}
      perPage={25}
      totalCount={100}
    />
  );
}
```

## [Compound Components](#compound-components)

For more control over layout and features, use the compound component API. This allows you to compose `Pagination.Info`, `Pagination.PageSize`, `Pagination.Controls`, and `Pagination.Separator` in any order.

### [Page Size Selector](#page-size-selector)

Add a dropdown to let users select the number of items per page.

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

/** Pagination with a page size selector using compound components. */
export function PaginationPageSizeSelectorDemo() {
  const [page, setPage] = useState(1);
  const [perPage, setPerPage] = useState(25);

  return (
    <Pagination
      page={page}
      setPage={setPage}
      perPage={perPage}
      totalCount={500}
    >
      <Pagination.Info />
      <Pagination.Separator />
      <Pagination.PageSize
        value={perPage}
        onChange={(size) => {
          setPerPage(size);
          setPage(1);
        }}
      />
      <Pagination.Controls />
    </Pagination>
  );
}
```

### [Custom Page Size Options](#custom-page-size-options)

Customize the available page size options with the `options` prop. Defaults to `[25, 50, 100, 250]`.

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

/** Pagination with custom page size options using compound components. */
export function PaginationCustomPageSizeOptionsDemo() {
  const [page, setPage] = useState(1);
  const [perPage, setPerPage] = useState(10);

  return (
    <Pagination
      page={page}
      setPage={setPage}
      perPage={perPage}
      totalCount={200}
    >
      <Pagination.Info />
      <Pagination.Separator />
      <Pagination.PageSize
        value={perPage}
        onChange={(size) => {
          setPerPage(size);
          setPage(1);
        }}
        options={[10, 20, 50]}
      />
      <Pagination.Controls />
    </Pagination>
  );
}
```

### [Custom Info Text](#custom-info-text)

Use a render function to customize the info text.

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

/** Pagination with custom info text using compound components. */
export function PaginationCompoundCustomInfoDemo() {
  const [page, setPage] = useState(1);

  return (
    <Pagination page={page} setPage={setPage} perPage={25} totalCount={100}>
      <Pagination.Info>
        {({ page, totalCount }) =>
          `Page ${page} of ${Math.ceil((totalCount ?? 1) / 25)}`
        }
      </Pagination.Info>
      <Pagination.Controls />
    </Pagination>
  );
}
```

### [Custom Layout](#custom-layout)

Arrange components in any order. Here the page size selector is on the right.

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

/** Pagination with page size selector on the right side. */
export function PaginationPageSizeRightDemo() {
  const [page, setPage] = useState(1);
  const [perPage, setPerPage] = useState(25);

  return (
    <Pagination
      page={page}
      setPage={setPage}
      perPage={perPage}
      totalCount={500}
    >
      <Pagination.Info />
      <div className="flex items-center gap-2">
        <Pagination.Controls />
        <Pagination.Separator />
        <Pagination.PageSize
          value={perPage}
          onChange={(size) => {
            setPerPage(size);
            setPage(1);
          }}
        />
      </div>
    </Pagination>
  );
}
```

### [Dropdown Page Selector](#dropdown-page-selector)

Use `pageSelector="dropdown"` on `Pagination.Controls` to render a dropdown select instead of a text input for page navigation. This is useful when you want users to pick from a list of available pages rather than typing a number.

```
<Pagination page={page} setPage={setPage} perPage={perPage} totalCount={500}>

<Pagination.Info />
<Pagination.Separator />
<Pagination.PageSize
  value={perPage}
  onChange={(size) => {
    setPerPage(size);
    setPage(1);
  }}
/>
<Pagination.Controls pageSelector="dropdown" />
</Pagination>
```

## [Internationalization](#internationalization)

Use the `labels` prop to customize all UI strings for different locales. All labels default to English.

```
import { useState } from "react";
import { Pagination } from "@cloudflare/kumo";

/** Pagination with French labels for internationalization. */
export function PaginationI18nDemo() {
  const [page, setPage] = useState(1);

  return (
    <Pagination
      page={page}
      setPage={setPage}
      perPage={10}
      totalCount={100}
      labels={{
        firstPage: "Première page",
        previousPage: "Page précédente",
        nextPage: "Page suivante",
        lastPage: "Dernière page",
        pageNumber: "Numéro de page",
        pageSize: "Taille de page",
      }}
    >
      <Pagination.Info>
        {({ pageShowingRange, totalCount }) => (
          <>
            Affichage de{" "}
            <span className="tabular-nums">{pageShowingRange}</span> sur{" "}
            <span className="tabular-nums">{totalCount}</span>
          </>
        )}
      </Pagination.Info>
      <Pagination.Controls />
    </Pagination>
  );
}
```

## [API Reference](#api-reference)

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| setPage\* | `(page: number) => void` | \- | Callback when page changes |
| page | `number` | \- | Current page number (1-indexed). |
| perPage | `number` | \- | Number of items displayed per page. |
| totalCount | `number` | \- | Total number of items across all pages. |
| hasNextPage | `boolean` | \- | Whether another page exists when the total count is unknown. Ignored when \`totalCount\` is provided. Unknown totals use sequential controls only. |
| className | `string` | \- | Additional CSS classes for the container |
| labels | `PaginationLabels` | \- | Labels for internationalization of aria-labels. All labels have English defaults. For visible text like "Showing X of Y", use render props on sub-components: - \`Pagination.Info\` children for the info text - \`Pagination.PageSize\` label prop for the "Per page:" text |
| children | `ReactNode` | \- | Compound component children for custom layouts. Use Pagination.Info, Pagination.PageSize, Pagination.Controls, and Pagination.Separator. |
| controls | `"full" | "simple"` | `"full"` | \- |
| text | `object` | \- | \- |