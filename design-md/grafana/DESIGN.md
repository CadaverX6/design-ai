# Grafana Design System

> Observability-platform design with dark dashboards, strong signal color, and highly structured reusable UI. Grafana’s Saga design system emphasizes accessibility, flexibility, coherence, and predictable patterns for dense monitoring interfaces.

---

## 1. Visual Theme & Atmosphere

### Overall Aesthetic
Grafana feels like **operational signal made usable**. The design has to support dense metrics, dashboards, forms, alerts, and plugin experiences without losing clarity or coherence.

### Mood & Feeling
- **Technical**: the product should feel built for engineers and operators
- **Signal-rich**: visual hierarchy must help users spot what matters quickly
- **Coherent**: reusable patterns are essential across dashboards and plugins
- **Accessible**: Saga explicitly bakes accessibility into the system
- **Flexible**: components need to work across many configurations

### Design Density
**Medium-high density**. Grafana surfaces often carry charts, filters, controls, and lists, but structure and component consistency keep them understandable.

### Visual Character
- Dark theme as a strong product-default mood
- Orange brand energy used as a highlight, not a flood
- Tight, data-friendly typography and spacing
- Strong modular components for lists, forms, grids, and navigation

---

## 2. Color Palette & Roles

### Core Brand Colors

| Token | Hex | Role |
|-------|-----|------|
| `--grafana-orange` | `#F05A28` | Signature brand accent |
| `--grafana-orange-dark` | `#D44A1A` | Hover / stronger emphasis |
| `--grafana-orange-soft` | `#FFE8DE` | Soft highlight surface |

### Dark Theme Foundation

| Token | Hex | Role |
|-------|-----|------|
| `--dark-1` | `#111217` | Primary background |
| `--dark-2` | `#181B1F` | Secondary surface |
| `--dark-3` | `#1F242A` | Panel and card surface |
| `--dark-border` | `#2F3840` | Border and divider |
| `--text-light` | `#F4F5F8` | Primary text on dark |
| `--text-muted` | `#B6BDC6` | Secondary text on dark |

### Signal and Semantic Colors

| Token | Hex | Role |
|-------|-----|------|
| `--blue` | `#5794F2` | Info, link, chart support |
| `--green` | `#73BF69` | Success / healthy state |
| `--yellow` | `#FADE2A` | Warning / degraded state |
| `--red` | `#E24D42` | Error / critical state |

### Color Usage Rules
- Let dark surfaces and chart colors do most of the visual work.
- Use orange mainly for brand emphasis and select actions.
- Keep semantic colors sharp and data-meaningful.

---

## 3. Typography Rules

### Font Stack

```css
/* Grafana-style dashboard sans */
--font-sans: Inter, 'Helvetica Neue', Arial, sans-serif;
--font-mono: 'Roboto Mono', 'SF Mono', Menlo, monospace;
```

### Type Scale

| Element | Size | Weight | Line Height | Letter Spacing | Usage |
|---------|------|--------|-------------|----------------|-------|
| Page Title | 32px | 700 | 1.15 | -0.015em | Dashboard or page title |
| Section Title | 24px | 600 | 1.2 | -0.01em | Section header |
| Card Title | 18px | 600 | 1.3 | 0 | Panel title |
| Body | 14px | 400 | 1.5 | 0 | Standard UI text |
| Small Body | 12px | 400 | 1.45 | 0 | Dense metadata |
| Label | 12px | 500 | 1.3 | 0.01em | Controls and buttons |
| Code | 12px | 400 | 1.45 | 0 | Query and metric values |

### Typography Philosophy
Grafana typography should feel **compact, readable, and operational**. The system must support dashboards, forms, alerts, and plugin UIs without strain.

### Practical Rules
- Keep panel titles short.
- Use typographic contrast to distinguish key metrics from supporting labels.
- Reserve mono styles for queries, IDs, and technical values.

---

## 4. Component Stylings

### Buttons

#### Primary Button
```css
.button-primary {
  background: #F05A28;
  color: #FFFFFF;
  min-height: 32px;
  padding: 0 14px;
  border: 1px solid #F05A28;
  border-radius: 6px;
  font: 500 14px/1 Inter, sans-serif;
}
```

#### Secondary Button
```css
.button-secondary {
  background: #1F242A;
  color: #F4F5F8;
  min-height: 32px;
  padding: 0 14px;
  border: 1px solid #2F3840;
  border-radius: 6px;
}
```

### Inputs

#### Text Input
```css
.input {
  width: 100%;
  min-height: 32px;
  padding: 0 10px;
  background: #181B1F;
  color: #F4F5F8;
  border: 1px solid #2F3840;
  border-radius: 6px;
  font: 400 14px/1.2 Inter, sans-serif;
}
```

### Panels and Dashboard Surfaces

#### Dashboard Panel
```css
.panel {
  background: #1F242A;
  color: #F4F5F8;
  border: 1px solid #2F3840;
  border-radius: 12px;
  padding: 16px;
}
```

#### Metric Card
```css
.metric-card {
  background: #181B1F;
  border-radius: 12px;
  padding: 16px;
}
```

---

## 5. Layout Principles

### Layout Rules
Saga encourages **reusable templates and patterns** for common page types like lists, tables, dashboards, and forms.

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | `4px` | Fine alignment |
| `--space-2` | `8px` | Tight spacing |
| `--space-4` | `16px` | Core spacing |
| `--space-5` | `24px` | Section spacing |
| `button-sm` | `24px` | Small button height |
| `button-md` | `32px` | Standard button height |
| `button-lg` | `48px` | Large button height |

### Layout Guidance
- Default to reusable page templates before inventing custom layouts.
- Use clear panel and navigation hierarchy in dashboards.
- Keep forms organized for clarity and ease of use.
- Let grid and stack primitives structure content cleanly.

---

## 6. Depth & Elevation

### Surface Hierarchy

| Level | Treatment | Use |
|-------|-----------|-----|
| Base dark | dark application background | Main shell |
| Panel | bordered dark surface | Dashboard or form unit |
| Metric card | inset dark surface | Highlighted data |
| Overlay | elevated dark surface | Modal or expanded tool |

### Shadow System

```css
.shadow-panel {
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.18);
}

.shadow-overlay {
  box-shadow: 0 18px 30px rgba(0, 0, 0, 0.28);
}
```

### Depth Rules
- Use borders and background separation before dramatic shadow.
- Keep overlays clearly elevated.
- Maintain visual discipline so dashboards don’t turn noisy.

---

## 7. Do's and Don'ts

### Do
- Use orange as a strong but selective brand cue.
- Keep dashboards and forms highly structured.
- Reuse Saga patterns and templates.
- Use color and hierarchy to emphasize task-at-hand.
- Match UI friction to action severity.

### Don't
- Overcrowd dashboards with too many equal-priority highlights.
- Use arbitrary card styles from screen to screen.
- Turn every action into a bright orange button.
- Sacrifice accessibility in dense views.

---

## 8. Responsive Behavior

### Responsive Rules
- Let panel grids collapse cleanly into stacked layouts.
- Preserve readable chart titles, filters, and actions on small screens.
- Use larger buttons only when emphasis or touch contexts demand them.
- Keep lists and objects scannable even when column layouts collapse.

### Mobile Character
Grafana mobile layouts should still feel operational and coherent. Simplification is fine, but the information architecture and signal clarity must remain strong.

---

## 9. Agent Prompt Guide

### Quick Reference
- **Mood**: technical, signal-rich, coherent
- **Primary accent**: Grafana orange `#F05A28`
- **Core surfaces**: dark dashboards with bordered panels
- **Typography**: compact Inter-style UI sans
- **Layout**: reusable templates, grids, stacked panel logic

### Prompt Snippet

```text
Design this interface in the style of Grafana’s Saga design system. Use dark dashboard surfaces, Grafana orange (#F05A28) as a selective brand accent, highly structured panels, compact readable typography, and reusable page templates. The result should feel operational, coherent, and accessible in dense monitoring contexts.
```
