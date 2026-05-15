# VMware Design System

> Enterprise-ready consumer-simple design with strong action blue, structured layout logic, and explicit accessibility. VMware’s Clarity design system balances application rigor with approachable component patterns and highly reusable foundations.

---

## 1. Visual Theme & Atmosphere

### Overall Aesthetic
Clarity is designed to make enterprise software feel **coherent, scalable, and people-centered**. It is built for application environments where users need dependable patterns, strong hierarchy, and clear calls to action.

### Mood & Feeling
- **Structured**: complex software should feel organized
- **Approachable**: enterprise does not have to mean harsh or confusing
- **Accessible**: Clarity explicitly integrates WCAG-focused guidance
- **Efficient**: patterns should be obvious across products
- **Utility-first**: styling should support task completion

### Design Density
**Medium to medium-high density**. Clarity is comfortable in data-heavy and form-heavy applications, but it uses hierarchy, layout, and control consistency to keep those views manageable.

### Visual Character
- Action blue as a primary interaction signal
- Compact rectangular components with low-radius geometry
- Dense but controlled application layouts
- Strong support for form and card patterns
- Little ornamental styling

---

## 2. Color Palette & Roles

### Core Colors

| Token | Hex | Role |
|-------|-----|------|
| `--action-blue` | `#0065C4` | Primary interaction color |
| `--action-blue-hover` | `#0050A1` | Hover / active state |
| `--action-blue-soft` | `#EAF4FF` | Light highlighted surface |

### Neutral Foundation

| Token | Hex | Role |
|-------|-----|------|
| `--dark-bg` | `#182026` | Dark theme application background |
| `--dark-surface` | `#202B33` | Dark content surface |
| `--light-page` | `#F5F8FA` | Light application background |
| `--light-surface` | `#FFFFFF` | Light card / container |
| `--border-dark` | `#30404D` | Dark border |
| `--border-light` | `#D8E1E8` | Light border |
| `--text-strong` | `#182026` | Primary text on light |
| `--text-muted` | `#5C7080` | Secondary text |

### Semantic Colors

| Token | Hex | Role |
|-------|-----|------|
| `--success` | `#2D9D78` | Success |
| `--warning` | `#D9822B` | Warning |
| `--danger` | `#DB3737` | Error / destructive |
| `--info` | `#137CBD` | Informational state |

### Color Usage Rules
- Use action blue consistently for primary actions.
- Support both light and dark application surfaces with equivalent clarity.
- Apply intent colors semantically and sparingly.

---

## 3. Typography Rules

### Font Stack

```css
/* Clarity-style application sans */
--font-sans: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI',
             Helvetica, Arial, sans-serif;
--font-mono: 'SF Mono', 'Roboto Mono', Menlo, Consolas, monospace;
```

### Type Scale

| Element | Size | Weight | Line Height | Letter Spacing | Usage |
|---------|------|--------|-------------|----------------|-------|
| Page Title | 32px | 700 | 1.15 | -0.015em | App or view title |
| Section Title | 24px | 600 | 1.2 | -0.01em | Section heading |
| Card Title | 18px | 600 | 1.3 | 0 | Card / module title |
| Body | 14px | 400 | 1.5 | 0 | Standard content |
| Small Body | 12px | 400 | 1.45 | 0 | Dense metadata |
| Label | 12px | 600 | 1.3 | 0.01em | Buttons and control labels |
| Code | 12px | 400 | 1.45 | 0 | Technical values |

### Typography Philosophy
Clarity typography should feel **compact, operational, and predictable**. It supports enterprise tasks where scanning and consistency matter more than brand flourish.

### Practical Rules
- Use clear action language in button labels.
- Keep dense layouts readable with consistent text sizes.
- Use strong hierarchy for page titles and section headings.

---

## 4. Component Stylings

### Buttons

#### Solid Button
```css
.button-primary {
  background: #0065C4;
  color: #FFFFFF;
  min-height: 36px;
  padding: 0 16px;
  border: 1px solid #0065C4;
  border-radius: 3px;
  font: 600 12px/1 system-ui, sans-serif;
  text-transform: uppercase;
}
```

#### Outline Button
```css
.button-secondary {
  background: transparent;
  color: #0065C4;
  min-height: 36px;
  padding: 0 16px;
  border: 1px solid #0065C4;
  border-radius: 3px;
  text-transform: uppercase;
}
```

#### Compact Button
```css
.button-compact {
  min-height: 24px;
  padding: 0 10px;
  border-radius: 3px;
  font-size: 12px;
}
```

### Inputs

#### Text Input
```css
.input {
  width: 100%;
  min-height: 36px;
  padding: 0 10px;
  background: #FFFFFF;
  color: #182026;
  border: 1px solid #D8E1E8;
  border-radius: 3px;
  font: 400 12px/1.2 system-ui, sans-serif;
}

.input:focus {
  outline: none;
  border-color: #0065C4;
  box-shadow: 0 0 0 2px rgba(0, 101, 196, 0.14);
}
```

### Cards and Application Containers

#### Card
```css
.card {
  background: #FFFFFF;
  border: 1px solid #D8E1E8;
  border-radius: 6px;
  padding: 16px;
}
```

#### Dark Container
```css
.container-dark {
  background: #202B33;
  color: #F5F8FA;
  border: 1px solid #30404D;
  border-radius: 6px;
  padding: 16px;
}
```

---

## 5. Layout Principles

### Layout Patterns
Clarity explicitly supports both **Z-pattern** and **F-pattern** action placement depending on constrained or unconstrained layouts.

| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | `4px` | Fine alignment |
| `--space-2` | `8px` | Tight spacing |
| `--space-4` | `16px` | Core application spacing |
| `--space-5` | `24px` | Section and card spacing |
| `button-default-height` | `36px` | Primary control size |
| `button-compact-height` | `24px` | Dense contexts |

### Layout Rules
- Use F-pattern for forms and cards.
- Use Z-pattern in modals and wizard-like constrained surfaces.
- Keep application structure obvious through repeated spacing and grouping.
- Align action hierarchy with task risk and importance.

---

## 6. Depth & Elevation

### Surface Hierarchy

| Level | Treatment | Use |
|-------|-----------|-----|
| App background | light or dark base | Overall application shell |
| Container | bordered surface | Section or card |
| Overlay | elevated container | Modal or popover |
| Intent surface | intent-tinted region | Alert / validation state |

### Shadow System

```css
.shadow-container {
  box-shadow: 0 4px 10px rgba(24, 32, 38, 0.08);
}

.shadow-overlay {
  box-shadow: 0 16px 28px rgba(24, 32, 38, 0.18);
}
```

### Depth Rules
- Use bounded containers before dramatic shadow.
- Keep overlays clearly elevated.
- Preserve contrast and border clarity in both light and dark themes.

---

## 7. Do's and Don'ts

### Do
- Use action blue consistently.
- Respect Clarity’s button hierarchy and sizes.
- Keep enterprise screens compact but readable.
- Support accessibility in every state.
- Use predictable layout patterns.

### Don't
- Add decorative softness or oversized radii.
- Overuse accent color outside primary actions.
- Ignore dark-theme clarity requirements.
- Mix action placement logic randomly.

---

## 8. Responsive Behavior

### Responsive Rules
- Keep dense controls readable by stacking earlier on smaller screens.
- Preserve button hierarchy even when actions wrap.
- Avoid compact button size in touch-heavy contexts.
- Keep dialogs and forms simple and scroll-friendly on mobile.

### Mobile Character
Clarity-based mobile interfaces should still feel structured and enterprise-ready. Simplify layout, but keep the same strong action and form logic.

---

## 9. Agent Prompt Guide

### Quick Reference
- **Mood**: structured, accessible, enterprise-ready
- **Primary accent**: action blue `#0065C4`
- **Layout**: Z-pattern and F-pattern logic
- **Components**: low-radius buttons, compact inputs, bounded containers

### Prompt Snippet

```text
Design this interface in the style of VMware’s Clarity design system. Use action blue (#0065C4) for primary interaction, compact enterprise controls with low-radius geometry, strong application containers, and highly predictable layout patterns. The result should feel structured, accessible, and consumer-simple inside enterprise complexity.
```
