# Sidebar

A composable sidebar navigation component with collapsible groups, icon-only mode, peeking, sliding views, and responsive mobile support.

**Source:** [GitHub](https://github.com/cloudflare/kumo/blob/main/packages/kumo/src/components/sidebar/sidebar.tsx)

---

<Sidebar.Provider defaultOpen>
  <Sidebar>
    <Sidebar.Content>
      <Sidebar.Group>
        <Sidebar.GroupLabel>Overview</Sidebar.GroupLabel>
        <Sidebar.Menu>
          <Sidebar.MenuButton icon={HouseIcon} active>Home</Sidebar.MenuButton>
          <Sidebar.MenuButton icon={GlobeIcon}>Domains</Sidebar.MenuButton>
        </Sidebar.Menu>
      </Sidebar.Group>
    </Sidebar.Content>
  </Sidebar>
</Sidebar.Provider>
Installation
Barrel
import { Sidebar } from "@cloudflare/kumo";
Granular
import { Sidebar } from "@cloudflare/kumo/components/sidebar";
Usage
At minimum you need Provider,Sidebar,Content (scrollable area),Menu, andMenuButton. Add Header /Footer to pin content above or below the scroll area. Use Group +GroupLabel to organize sections.

import { Sidebar } from "@cloudflare/kumo";
import { HouseIcon, CodeIcon, GearIcon } from "@phosphor-icons/react";

function AppLayout({ children }) {
  return (
    <Sidebar.Provider defaultOpen>
      <Sidebar>
        <Sidebar.Content>
          <Sidebar.Group>
            <Sidebar.GroupLabel>Navigation</Sidebar.GroupLabel>
            <Sidebar.Menu>
              <Sidebar.MenuButton icon={HouseIcon} active>Home</Sidebar.MenuButton>
              {/* MenuItem only needed to wrap Collapsible */}
              <Sidebar.MenuItem>
                <Sidebar.Collapsible>
                  <Sidebar.CollapsibleTrigger
                    render={
                      <Sidebar.MenuButton icon={CodeIcon}>
                        Compute <Sidebar.MenuChevron />
                      </Sidebar.MenuButton>
                    }
                  />
                  <Sidebar.CollapsibleContent>
                    <Sidebar.MenuSub>
                      <Sidebar.MenuSubButton>Workers</Sidebar.MenuSubButton>
                    </Sidebar.MenuSub>
                  </Sidebar.CollapsibleContent>
                </Sidebar.Collapsible>
              </Sidebar.MenuItem>
            </Sidebar.Menu>
          </Sidebar.Group>
        </Sidebar.Content>
        <Sidebar.Footer>
          <Sidebar.Trigger />
        </Sidebar.Footer>
      </Sidebar>
      <div className="flex-1">{children}</div>
    </Sidebar.Provider>
  );
}
Examples
Basic
The minimum viable sidebar: just groups, menu buttons, and collapsible sub-menus. No header or footer.MenuButton and MenuSubButton auto-wrap in <li> — no MenuItem / MenuSubItem needed.

Overview

Home

Analytics

Domains
Build

Compute

Workers & Pages

Durable Objects

Storage
Main content area
<Sidebar.Provider defaultOpen>
  <Sidebar>
    <Sidebar.Content>
      <Sidebar.Group>
        <Sidebar.GroupLabel>Overview</Sidebar.GroupLabel>
        <Sidebar.Menu>
          <Sidebar.MenuButton icon={HouseIcon} active>Home</Sidebar.MenuButton>
          <Sidebar.MenuButton icon={ChartBarIcon}>Analytics</Sidebar.MenuButton>
        </Sidebar.Menu>
      </Sidebar.Group>
    </Sidebar.Content>
  </Sidebar>
</Sidebar.Provider>
Toggle & Collapsed State
Use Sidebar.Trigger in the footer or useSidebar().toggleSidebar programmatically. Pass tooltip to show labels on hover when collapsed.

Company

Home

Analytics

Compute

Storage

Collapse
Click the button or the sidebar trigger to toggle

<Sidebar.MenuButton icon={HouseIcon} tooltip="Home" active>
  Home
</Sidebar.MenuButton>

<Sidebar.Footer>
  <Sidebar.Trigger />
</Sidebar.Footer>

// Or programmatically:
const { toggleSidebar } = useSidebar();
Loading
Sidebar.Loading shows nav-item-shaped skeleton rows in place of the nav content while routes and permissions resolve. When collapsed only the icon squares remain. Honours reduced-motion.

Company

Show loaded nav
Toggle to compare the loading state with the loaded nav

<Sidebar>
  <Sidebar.Header>…</Sidebar.Header>
  {isLoading ? (
    <Sidebar.Loading />
  ) : (
    <Sidebar.Content>…</Sidebar.Content>
  )}
  <Sidebar.Footer>…</Sidebar.Footer>
</Sidebar>
Resizable
Drag the edge to resize. Dragging below minWidth collapses; dragging outward from collapsed expands. The resize handle is keyboard accessible: use arrow keys, Home, and End.

Company

Home

Analytics

Storage


Drag the sidebar edge to resize

<Sidebar.Provider defaultOpen resizable defaultWidth={240} minWidth={180} maxWidth={400}>
  <Sidebar>
    <Sidebar.Content>...</Sidebar.Content>
    <Sidebar.ResizeHandle />
  </Sidebar>
</Sidebar.Provider>
Right Side
Use side="right" for a sidebar on the right edge. Place <main> before <Sidebar> in the DOM.

Main content area
Details

Properties

Metrics

Alerts
<Sidebar.Provider defaultOpen side="right">
  <main className="flex-1">...</main>
  <Sidebar>
    <Sidebar.Content>
      <Sidebar.Group>
        <Sidebar.GroupLabel>Details</Sidebar.GroupLabel>
        <Sidebar.Menu>
          <Sidebar.MenuButton icon={GearIcon} active>Properties</Sidebar.MenuButton>
          <Sidebar.MenuButton icon={ChartBarIcon}>Metrics</Sidebar.MenuButton>
        </Sidebar.Menu>
      </Sidebar.Group>
    </Sidebar.Content>
  </Sidebar>
</Sidebar.Provider>
Peeking
Set peekable on the Provider. When the sidebar is collapsed, hovering or focusing it temporarily expands it. Moving away collapses it back. The data-state attribute will be "peeking" during the peek.

Company

Home

Analytics

Compute

Storage

State: Expanded
Collapse, then hover the sidebar to peek

<Sidebar.Provider defaultOpen peekable>
  <Sidebar>
    <Sidebar.Content>...</Sidebar.Content>
    <Sidebar.Footer>
      <Sidebar.Trigger />
    </Sidebar.Footer>
  </Sidebar>
</Sidebar.Provider>

// Read peeking state:
const { state, isPeeking } = useSidebar();
// state: "expanded" | "collapsed" | "peeking"
Auto Scroll
Use autoScrollOnOpen on long collapsible sections to keep newly revealed content in view. This is useful when a group near the bottom of a scrollable sidebar expands below the visible area.

Company
Overview

Home

Analytics

Domains
Platform

Storage

Security

Zero Trust

Settings
Build

Workers

Containers

Open Workers near the bottom of the list

<Sidebar.Collapsible autoScrollOnOpen>
  <Sidebar.CollapsibleTrigger
    render={
      <Sidebar.MenuButton icon={CodeIcon}>
        Workers <Sidebar.MenuChevron />
      </Sidebar.MenuButton>
    }
  />
  <Sidebar.CollapsibleContent>
    <Sidebar.MenuSub>...</Sidebar.MenuSub>
  </Sidebar.CollapsibleContent>
</Sidebar.Collapsible>
Scroll to Item
Tag nav items with itemId, then call useSidebar().scrollToItem(id, options) to bring one into view. Use scrollItemIntoView(id, options) to preserve the current position when the item is already fully visible.align is "start", "center", "end", or "auto" (default — no-op if visible). behavior defaults to "auto" (instant) so cross-app landings don't animate on entry; pass "smooth" for in-app "jump to section" flows. Honors prefers-reduced-motion. Works correctly with Sidebar.SlidingViews — items are resolved from a per-provider registry, not a DOM query.

itemId works in both usage patterns: on Sidebar.MenuButton directly (the common case, which auto-wraps in a <li>), or on Sidebar.MenuItem when you wrap a Collapsible. If you put itemId on a MenuButton nested inside a MenuItem, it still works — the button itself becomes the scroll target.

Company

Home

Analytics

Domains

SSL/TLS

Firewall

Caching

Workers

Pages

R2

KV

D1

AI Gateway

Queues

Zaraz

Turnstile

Load Balancing

Zero Trust

Access

Gateway

Tunnels

Logs

Notifications

Members

API tokens

Billing

Settings

Jump to any tagged item.

Scroll to home
Scroll to workers
Scroll to zero-trust
Scroll to settings
<Sidebar.MenuButton itemId="zero-trust" href="/zt">
  Zero Trust
</Sidebar.MenuButton>

// elsewhere:
const { scrollToItem } = useSidebar();
scrollToItem("zero-trust", { align: "center", behavior: "smooth" });
Sliding Views
Use Sidebar.SlidingViews and Sidebar.SlidingViewfor animated horizontal transitions between navigation surfaces (e.g., account ↔ zone). Inactive views are automatically marked with aria-hidden and inert. Animation respects prefers-reduced-motion.


Account Nav
Account

Home

Members

Analytics

Settings
Active: Account surface

Click the header button to slide between views

const [surface, setSurface] = useState("account");

<Sidebar.SlidingViews activeKey={surface} direction="left">
  <Sidebar.SlidingView value="account">
    <Sidebar.Content>...account nav...</Sidebar.Content>
  </Sidebar.SlidingView>
  <Sidebar.SlidingView value="zone">
    <Sidebar.Content>...zone nav...</Sidebar.Content>
  </Sidebar.SlidingView>
</Sidebar.SlidingViews>
Full Example
Kitchen sink showcasing every subcomponent: header with account switcher, groups with labels, collapsible sections with nested expandable, badges, sliding views, and a footer trigger.


Company

Quick search…

Home

Analytics & Logs

Domains
Build

Compute

Workers & Pages

Durable Objects

Containers

Storage
Protect & Connect

Security

Zero Trust

Main content area
<Sidebar>
  <Sidebar.Header>
    <AccountSwitcher />
  </Sidebar.Header>
  <Sidebar.Content>
    <Sidebar.Group>
      <Sidebar.Menu>
        <Sidebar.MenuButton icon={HouseIcon} active>Home</Sidebar.MenuButton>
      </Sidebar.Menu>
    </Sidebar.Group>
    <Sidebar.Group>
      <Sidebar.GroupLabel>Build</Sidebar.GroupLabel>
      <Sidebar.Menu>
        <Sidebar.MenuItem>
          <Sidebar.Collapsible defaultOpen>
            <Sidebar.CollapsibleTrigger
              render={
                <Sidebar.MenuButton icon={CodeIcon}>
                  Compute <Sidebar.MenuChevron />
                </Sidebar.MenuButton>
              }
            />
            <Sidebar.CollapsibleContent>
              <Sidebar.MenuSub>
                <Sidebar.MenuSubButton>
                  Containers <Sidebar.MenuBadge>Beta</Sidebar.MenuBadge>
                </Sidebar.MenuSubButton>
              </Sidebar.MenuSub>
            </Sidebar.CollapsibleContent>
          </Sidebar.Collapsible>
        </Sidebar.MenuItem>
      </Sidebar.Menu>
    </Sidebar.Group>
  </Sidebar.Content>
  <Sidebar.Footer>
    <Sidebar.Trigger />
  </Sidebar.Footer>
</Sidebar>
Mobile
On narrow viewports the sidebar renders as a navigation drawer. Use mobileBreakpoint to control the threshold. The drawer uses inert and aria-hidden while closed, moves focus in on open, and supports Escape-to-close. This demo forces mobile mode via a high breakpoint.

Open sidebar
Click the button to open the mobile sidebar

Press Escape or click the backdrop to close

<Sidebar.Provider mobileBreakpoint={9999}>
  <Sidebar>
    <Sidebar.Content>...</Sidebar.Content>
  </Sidebar>
</Sidebar.Provider>
Full-screen mobile
Pass fullScreenOnMobile to have the drawer cover the whole viewport instead of leaving a sliver of the page visible. Nav items get comfortable touch targets, and the backdrop is suppressed since nothing shows behind the sheet. Add Sidebar.Close inside the header so the sheet can be dismissed from within the nav. Pair it with breadcrumbs in the page header so the current route stays visible once the nav is closed.

Viewport

390px

Analytics
Account analytics
Account analytics

Drill into the nav — the trail is derived from the tree, so it always matches where you are.

<Sidebar.Provider mobileBreakpoint={9999}>
  <Sidebar fullScreenOnMobile>
    <Sidebar.Header>
      <Sidebar.Close />
    </Sidebar.Header>
    <Sidebar.Content>...</Sidebar.Content>
  </Sidebar>

  <header>
    <Sidebar.Trigger />
    <Breadcrumbs size="sm">
      <Breadcrumbs.Link href="/">Company</Breadcrumbs.Link>
      <Breadcrumbs.Separator />
      <Breadcrumbs.Current>Analytics</Breadcrumbs.Current>
    </Breadcrumbs>
  </header>
</Sidebar.Provider>
API Reference
Sidebar
The main sidebar container. Renders as <aside> on desktop and a navigation drawer on mobile.

Prop	Type	Default	Description
defaultOpen	boolean	-	Initial open state when uncontrolled.
open	boolean	-	Controlled open state.
variant	"sidebar" | "floating" | "inset"	"sidebar"	Sidebar layout variant.
side	"left" | "right"	"left"	Which side the sidebar is on.
collapsible	"icon" | "offcanvas" | "none"	"icon"	-
resizable	boolean	-	Enable drag-to-resize on the sidebar edge.
defaultWidth	number	-	Initial width in pixels when resizable.
minWidth	number	-	Minimum width in pixels when resizing.
maxWidth	number	-	Maximum width in pixels when resizing.
contained	boolean	-	When true, the collapsed sidebar uses absolute positioning instead of fixed, keeping it scoped inside a bounded parent. Useful for demos and embedded sidebars.
peekable	boolean	-	When true, hovering or focusing the collapsed sidebar temporarily expands it. The `state` will be `"peeking"` during the peek. Moving away collapses it back.
animationDuration	number	-	Duration of sidebar expand/collapse animation in milliseconds.
mobileBreakpoint	number	-	Viewport width (in px) below which the sidebar renders as a mobile dialog sheet instead of the desktop aside rail.
children	ReactNode	-	Content — typically `<Sidebar>` + main content.
className	string	-	Additional CSS classes for the wrapper div.
Sidebar.Provider
Context provider managing expand/collapse state and mobile detection.

Prop	Type	Default	Description
defaultOpen	boolean	-	Initial open state when uncontrolled.
open	boolean	-	Controlled open state.
variant	SidebarVariant	-	Sidebar layout variant.
side	SidebarSide	-	Which side the sidebar is on.
collapsible	"icon" | "offcanvas" | "none"	-	-
resizable	boolean	-	Enable drag-to-resize on the sidebar edge.
defaultWidth	number	-	Initial width in pixels when resizable.
minWidth	number	-	Minimum width in pixels when resizing.
maxWidth	number	-	Maximum width in pixels when resizing.
contained	boolean	-	When true, the collapsed sidebar uses absolute positioning instead of fixed, keeping it scoped inside a bounded parent. Useful for demos and embedded sidebars.
peekable	boolean	-	When true, hovering or focusing the collapsed sidebar temporarily expands it. The `state` will be `"peeking"` during the peek. Moving away collapses it back.
animationDuration	number	-	Duration of sidebar expand/collapse animation in milliseconds.
mobileBreakpoint	number	-	Viewport width (in px) below which the sidebar renders as a mobile dialog sheet instead of the desktop aside rail.
children*	ReactNode	-	Content — typically `<Sidebar>` + main content.
className	string	-	Additional CSS classes for the wrapper div.
Sidebar.Content
Scrollable middle section (flex-1 overflow-y-auto). Use Header / Footer to pin content above or below this scroll area.

Sidebar.MenuButton
Primary interactive element. Supports icons, active state, links, and auto-tooltip when collapsed. Auto-wraps in <li> — no MenuItem wrapper needed unless wrapping a Collapsible.

Prop	Type	Default	Description
icon	React.ComponentType<{ className?: string }> | React.ReactNode	-	-
active	boolean	-	-
size	SidebarMenuButtonSize	-	Button size. - `"base"` — Standard nav item - `"sm"` — Compact nav item
href	string	-	-
target	React.HTMLAttributeAnchorTarget	-	Link target — only meaningful when `href` is provided.
tooltip	string	-	-
itemId	string	-	Anchor id for `useSidebar().scrollToItem(id)`.
className	string	-	-
children	ReactNode	-	-
Sidebar.MenuSubButton
Button inside a sub-menu for nested navigation. Auto-wraps in <li> — no MenuSubItem wrapper needed.

Prop	Type	Default	Description
active	boolean	-	Marks this sub-item as currently active/selected.
href	string	-	Navigation URL. When set, renders as a link via LinkProvider.
target	React.HTMLAttributeAnchorTarget	-	Link target — only meaningful when `href` is provided.
