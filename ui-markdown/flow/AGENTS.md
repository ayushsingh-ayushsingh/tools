# Flow

A group of components for building directed flow diagrams with nodes and connectors.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/flow/flow.tsx)

---

```
import { Flow } from "@cloudflare/kumo";

/** Flow diagram with parallel branching */
export function FlowParallelDemo() {
  return (
    <Flow>
      <Flow.Node>Start</Flow.Node>
      <Flow.Parallel>
        <Flow.List>
          <Flow.Node>Branch A1</Flow.Node>
          <Flow.Node>Branch A2</Flow.Node>
        </Flow.List>
        <Flow.Node>Branch B</Flow.Node>
        <Flow.Node>Branch C</Flow.Node>
      </Flow.Parallel>
      <Flow.Node>End</Flow.Node>
    </Flow>
  );
}
```

## [Installation](#installation)

### [Barrel](#barrel)

```
import { Flow } from "@cloudflare/kumo";
```

### [Granular](#granular)

```
import { Flow } from "@cloudflare/kumo/components/flow";
```

## [Usage](#usage)

The Flow components work together to create directed flow diagrams. Use `Flow` as the container, `Flow.Node` for individual steps, and `Flow.Parallel` to create branching paths.

```
import { Flow } from "@cloudflare/kumo";

export default function Example() {
  return (
    <Flow>
      <Flow.Node>Step 1</Flow.Node>
      <Flow.Node>Step 2</Flow.Node>
      <Flow.Node>Step 3</Flow.Node>
    </Flow>
  );
}
```

## [Examples](#examples)

### [Sequential Flow](#sequential-flow)

A simple linear flow with nodes connected in sequence.

```
import { Flow } from "@cloudflare/kumo";

/** Basic flow diagram with sequential nodes */
export function FlowBasicDemo() {
  return (
    <Flow>
      <Flow.Node>Step 1</Flow.Node>
      <Flow.Node>Step 2</Flow.Node>
      <Flow.Node>Step 3</Flow.Node>
    </Flow>
  );
}
```

### [Parallel Branches](#parallel-branches)

Use `Flow.Parallel` to create branching paths that run in parallel.

```
import { Flow } from "@cloudflare/kumo";

/** Flow diagram with parallel branching */
export function FlowParallelDemo() {
  return (
    <Flow>
      <Flow.Node>Start</Flow.Node>
      <Flow.Parallel>
        <Flow.List>
          <Flow.Node>Branch A1</Flow.Node>
          <Flow.Node>Branch A2</Flow.Node>
        </Flow.List>
        <Flow.Node>Branch B</Flow.Node>
        <Flow.Node>Branch C</Flow.Node>
      </Flow.Parallel>
      <Flow.Node>End</Flow.Node>
    </Flow>
  );
}
```

### [Vertical Orientation](#vertical-orientation)

Set `orientation="vertical"` to lay nodes out top-to-bottom instead of the default left-to-right. Connectors, parallel branches, and `align` all adapt to the vertical axis.

```
import { Flow } from "@cloudflare/kumo";

/** Vertical flow diagram with sequential nodes */
export function FlowVerticalDemo() {
  return (
    <Flow orientation="vertical">
      <Flow.Node>Step 1</Flow.Node>
      <Flow.Node>Step 2</Flow.Node>
      <Flow.Node>Step 3</Flow.Node>
    </Flow>
  );
}
```

Parallel branches work the same way in vertical flows. In this orientation `align` controls horizontal alignment of nodes.

```
import { Flow } from "@cloudflare/kumo";

/** Vertical flow diagram with parallel branching */
export function FlowVerticalParallelDemo() {
  return (
    <Flow orientation="vertical" align="center">
      <Flow.Node>Start</Flow.Node>
      <Flow.Parallel>
        <Flow.Node>Branch A</Flow.Node>
        <Flow.Node>Branch B</Flow.Node>
        <Flow.Node>Branch C</Flow.Node>
      </Flow.Parallel>
      <Flow.Node>End</Flow.Node>
    </Flow>
  );
}
```

### [Custom Node Styling](#custom-node-styling)

Use the `render` prop to completely customize node appearance. The render prop accepts a React element that will be used instead of the default styled node.

```
import { Flow } from "@cloudflare/kumo";

/** Flow diagram with custom node styling using render prop */
export function FlowCustomContentDemo() {
  return (
    <Flow>
      <Flow.Node
        render={<li className="size-4 rounded-full bg-kumo-hairline" />}
      />
      <Flow.Node
        render={
          <li className="rounded-lg bg-kumo-contrast px-3 py-2 font-medium text-kumo-inverse">
            my-worker
          </li>
        }
      />
    </Flow>
  );
}
```

### [Centered Alignment](#centered-alignment)

Use the `align` prop to vertically center nodes. This is useful when nodes have different heights.

```
import { Flow } from "@cloudflare/kumo";

/** Flow diagram with vertically centered nodes */
export function FlowCenteredDemo() {
  return (
    <Flow align="center">
      <Flow.Node
        render={<li className="size-4 rounded-full bg-kumo-hairline" />}
      />
      <Flow.Node>my-worker</Flow.Node>
      <Flow.Node
        render={
          <li className="rounded-md bg-kumo-base px-3 py-6 shadow ring ring-kumo-hairline">
            Taller node
          </li>
        }
      />
    </Flow>
  );
}
```

### [Complex Flow](#complex-flow)

Combine sequential and parallel nodes to build complex workflows.

```
import { Flow } from "@cloudflare/kumo";

/** Complex flow diagram example */
export function FlowComplexDemo() {
  return (
    <Flow>
      <Flow.Parallel>
        <Flow.Node>HTTP Trigger</Flow.Node>
        <Flow.Node>Cron Trigger</Flow.Node>
      </Flow.Parallel>
      <Flow.Node>Process Request</Flow.Node>
      <Flow.Parallel>
        <Flow.Node>Log Analytics</Flow.Node>
        <Flow.Node>Update Cache</Flow.Node>
        <Flow.Node>Send Notification</Flow.Node>
      </Flow.Parallel>
      <Flow.Node>Complete</Flow.Node>
    </Flow>
  );
}
```

### [Custom Anchor Points](#custom-anchor-points)

By default, connectors attach to the center of each node. Use `Flow.Anchor` with its `render` prop to specify custom attachment points. The `type` prop controls whether the anchor serves as a `"start"` point (where connectors leave) or `"end"` point (where connectors arrive).

```
import { Flow } from "@cloudflare/kumo";

/** Flow diagram with custom anchor points */
export function FlowAnchorDemo() {
  return (
    <Flow>
      <Flow.Node>Load balancer</Flow.Node>
      <Flow.Node
        render={
          <li className="rounded-lg bg-kumo-overlay shadow-none ring ring-kumo-hairline">
            <Flow.Anchor
              type="end"
              render={
                <div className="flex h-10 items-center px-2.5 text-kumo-subtle">
                  my-worker
                </div>
              }
            />
            <Flow.Anchor
              type="start"
              render={
                <div className="m-1.5 mt-0 rounded bg-kumo-base px-2 py-1.5 shadow ring ring-kumo-hairline">
                  Bindings
                  <span className="ml-3 w-5 text-kumo-subtle">2</span>
                </div>
              }
            />
          </li>
        }
      />
      <Flow.Parallel>
        <Flow.Node>DATABASE</Flow.Node>
        <Flow.Node>OTHER_SERVICE</Flow.Node>
      </Flow.Parallel>
    </Flow>
  );
}
```

### [Panning Large Diagrams](#panning-large-diagrams)

When a diagram exceeds its container, Flow automatically enables panning. Drag to pan the viewport, or use the scroll wheel. Scrollbars appear on hover to indicate available scroll area.

```
import { Flow } from "@cloudflare/kumo";

/** Large flow diagram demonstrating panning */
export function FlowPanningDemo() {
  return (
    <Flow className="rounded-lg border border-kumo-hairline">
      <Flow.Node>Start</Flow.Node>
      <Flow.Node>Authenticate</Flow.Node>
      <Flow.Node>Validate</Flow.Node>
      <Flow.Node>Transform</Flow.Node>
      <Flow.Node>Process</Flow.Node>
      <Flow.Node>Store</Flow.Node>
      <Flow.Node>Notify</Flow.Node>
      <Flow.Node>Log</Flow.Node>
      <Flow.Node>Complete</Flow.Node>
      <Flow.Node>End</Flow.Node>
    </Flow>
  );
}
```

### [Disabled Nodes](#disabled-nodes)

Use the `disabled` prop on a node to visually indicate it’s inactive. Connectors linking to disabled nodes are rendered with reduced opacity.

```
import { Flow } from "@cloudflare/kumo";

/** Flow diagram with disabled nodes */
export function FlowDisabledDemo() {
  return (
    <Flow>
      <Flow.Node>Request</Flow.Node>
      <Flow.Parallel>
        <Flow.Node>Primary Handler</Flow.Node>
        <Flow.Node disabled>Backup Handler (disabled)</Flow.Node>
      </Flow.Parallel>
      <Flow.Node>Response</Flow.Node>
    </Flow>
  );
}
```

### [Parallel Node Alignment](#parallel-node-alignment)

Use the `align` prop on `Flow.Parallel` to control how nodes with different widths are aligned. Use `"start"` (default) to align left, or `"end"` to align right.

```
import { Flow } from "@cloudflare/kumo";

/** Flow diagram with right-aligned parallel nodes */
export function FlowParallelAlignEndDemo() {
  return (
    <Flow>
      <Flow.Node>Start</Flow.Node>
      <Flow.Parallel align="end">
        <Flow.Node>Short</Flow.Node>
        <Flow.Node>Medium Length</Flow.Node>
        <Flow.Node>Very Long Node Name</Flow.Node>
      </Flow.Parallel>
      <Flow.Node>End</Flow.Node>
    </Flow>
  );
}
```

## [Other Examples](#other-examples)

### [Nested Node Lists in Parallel](#nested-node-lists-in-parallel)

Use `Flow.List` inside `Flow.Parallel` to create parallel branches where each branch contains a sequence of connected nodes.

```
import { Flow } from "@cloudflare/kumo";

/** Flow diagram with parallel branches containing nested node sequences */
export function FlowParallelNestedListDemo() {
  return (
    <Flow>
      <Flow.Parallel>
        <Flow.List>
          <Flow.Node>Client Users</Flow.Node>
          <Flow.Node>Engineering Team Access</Flow.Node>
        </Flow.List>
        <Flow.List>
          <Flow.Parallel>
            <Flow.Node>All Authenticated Users</Flow.Node>
            <Flow.Node>Client Users</Flow.Node>
            <Flow.Node>Site Users</Flow.Node>
          </Flow.Parallel>
          <Flow.Node>Contractor Access</Flow.Node>
        </Flow.List>
      </Flow.Parallel>
      <Flow.Node>Destinations</Flow.Node>
    </Flow>
  );
}
```

## [Components](#components)

### [Flow](#flow)

The root container for flow diagrams. Provides panning and scrolling for large diagrams.

| Prop | Type | Description |
| --- | --- | --- |
| orientation | ”horizontal” | “vertical” | Layout direction of the flow. `"horizontal"` (default) lays nodes out left-to-right, `"vertical"` lays them out top-to-bottom. |
| align | ”start” | “center” | Cross-axis alignment of nodes. In horizontal orientation this is vertical alignment; in vertical orientation it is horizontal alignment. `"start"` (default) aligns to the start of the cross axis, `"center"` centers nodes. |
| className | string | Additional CSS classes for the container |
| children | ReactNode | Flow.Node and Flow.Parallel components |

### [Flow.Node](#flownode)

A single node in the flow diagram. Renders as a styled card with automatic connector points. Use the `render` prop to customize the element.

| Prop | Type | Description |
| --- | --- | --- |
| render | ReactElement | Custom element to render instead of the default styled node |
| disabled | boolean | When true, connectors linking to this node are rendered with reduced opacity |
| children | ReactNode | Content to display inside the node |

### [Flow.Anchor](#flowanchor)

A component that marks a custom attachment point for connectors within a Flow.Node. Use this to control exactly where connector lines attach instead of the default node center by providing a custom element via the `render` prop.

| Prop | Type | Description |
| --- | --- | --- |
| type | ”start” | “end” | Whether this anchor serves as a “start” point (outgoing connectors) or “end” point (incoming connectors). When omitted, serves as both. |
| render | ReactElement | Custom element to render for the anchor point |
| children | ReactNode | Content to render at the anchor point |

### [Flow.Parallel](#flowparallel)

A container for parallel branches. Child Flow.Node components are displayed in parallel with junction connectors.

| Prop | Type | Description |
| --- | --- | --- |
| align | ”start” | “end” | Controls horizontal alignment of nodes within the parallel group. `"start"` (default) aligns left, `"end"` aligns right. |
| children | ReactNode | Flow.Node or Flow.List components to display in parallel |

### [Flow.List](#flowlist)

A container for a sequence of Flow.Node components with automatic connectors between them. Use inside Flow.Parallel to create branches with multiple sequential steps.

| Prop | Type | Description |
| --- | --- | --- |
| children | ReactNode | Flow.Node components to display in sequence |