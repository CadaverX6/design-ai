# Okta Design System

> Identity-platform design with clear blue emphasis, accessible structure, and enterprise focus. Okta’s Odyssey system is built to create consistent, efficient, and accessible interfaces across products and sites.

---

## 1. Visual Theme & Atmosphere

### Overall Aesthetic
Okta expresses **trust through clarity**. The interface is straightforward, methodical, and accessibility-first. It should feel secure and efficient without becoming cold or bureaucratic.

### Mood & Feeling
- **Trusted**: identity software must feel dependable and mature
- **Clear**: hierarchy and actions should be unmistakable
- **Accessible**: design decisions prioritize usability across contexts
- **Systematic**: components and patterns should repeat predictably
- **Modern**: the experience should feel current but restrained

### Design Density
**Medium density**. Okta surfaces often include settings, forms, and identity workflows, but Odyssey keeps them readable through strong structure and clear components.

### Visual Character
- Signature Okta blue as the primary action color
- Light neutral surfaces with dark readable text
- Rounded but not playful controls
- Strong emphasis on accessibility and consistency
- Minimal ornamental treatment

---

## 2. Color Palette & Roles

### Core Colors

| Token | Hex | Role |
|-------|-----|------|
| `--okta-blue` | `#1662DD` | Primary action and interactive emphasis |
| `--okta-blue-hover` | `#0F4FBF` | Hover / active state |
| `--okta-blue-soft` | `#EAF2FF` | Light highlighted surface |

### Neutral Foundation

| Token | Hex | Role |
|-------|-----|------|
| `--ink-strong` | `#0F172A` | Primary text |
| `--ink-default` | `#334155` | Body text |
| `--ink-muted` | `#64748B` | Secondary text |
| `--surface-page` | `#F8FAFC` | Main page background |
| `--surface-card` | `#FFFFFF` | Card and panel surface |
| `--border-default` | `#DCE3EA` | Standard border |

### Semantic Colors

| Token | Hex | Role |
|-------|-----|------|
| `--success` | `#15803D` | Success / verified |
| `--warning` | `#D97706` | Warning / caution |
| `--danger` | `#DC2626` | Error / destructive |
| `--info` | `#1662DD` | Informational state |

### Color Usage Rules
- Use blue for primary interaction and selected states.
- Keep the base UI mostly neutral and high-contrast.
- Use semantic colors only for actual state meaning.

---

## 3. Typography Rules

### Font Stack

```css
/* Odyssey-style product sans */
--font-sans: Inter, 'Helvetica Neue', Arial, sans-serif;
--font-mono: 'SF Mono', 'Roboto Mono', Menlo, monospace;
```

### Type Scale

| Element | Size | Weight | Line Height | Letter Spacing | Usage |
|---------|------|--------|-------------|----------------|-------|
| Page Title | 32px | 700 | 1.15 | -0.015em | App-level heading |
| Section Title | 24px | 600 | 1.2 | -0.01em | Section heading |
| Card Title | 18px | 600 | 1.3 | 0 | Card / form title |
| Body | 16px | 400 | 1.55 | 0 | Standard content |
| Small Body | 14px | 400 | 1.5 | 0 | Dense UI copy |
| Label | 14px | 600 | 1.3 | 0.01em | Buttons and form labels |
| Caption | 12px | 500 | 1.4 | 0.01em | Helper and metadata |

### Typography Philosophy
Okta typography should feel **practical, confident, and readable**. It exists to support identity workflows, not to dominate them.

### Practical Rules
- Keep headings short and functional.
- Use labels that clearly describe the user action.
- Preserve strong contrast and spacing in forms.

---

## 4. Component Stylings

### Buttons

#### Primary Button
```css
.button-primary {
  background: #1662DD;
  color: #FFFFFF;
  min-height: 40px;
  padding: 0 16px;
  border: 1px solid #1662DD;
  border-radius: 8px;
  font: 600 14px/1 Inter, sans-serif;
}

.button-primary:hover {
  background: #0F4FBF;
  border-color: #0F4FBF;
}
```

#### Secondary Button
```css
.button-secondary {
  background: #FFFFFF;
  color: #0F172A;
  min-height: 40px;
  padding: 0 16px;
  border: 1px solid #DCE3EA;
  border-radius: 8px;
}
```

### Inputs

#### Text Input
```css
.input {
  width: 100%;
  min-height: 40px;
  padding: 0 12px;
  background: #FFFFFF;
  color: #0F172A;
  border: 1px solid #DCE3EA;
  border-radius: 8px;
  font: 400 14px/1.2 Inter, sans-serif;
}

.input:focus {
  outline: none;
  border-color: #1662DD;
  box-shadow: 0 0 0 3px rgba(22, 98, 221, 0.14);
}
```

### Cards and Identity Panels

#### Card
```css
.card {
  background: #FFFFFF;
  border: 1px solid #DCE3EA;
  border-radius: 16px;
  padding: 20px;
}
```

#### Auth Panel
```css
.auth-panel {
  background: #FFFFFF;
  border-radius: 18px;
  padding: 24px;
  box-shadow: 0 8px 18px rgba(15, 23, 42, 0.08);
}
```

---

## 5. Layout Principles

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--space-2` | `8px` | Tight spacing |
| `--space-4` | `16px` | Core spacing |
| `--space-5` | `24px` | Panel spacing |
| `--space-6` | `32px` | Section spacing |
| `--space-8` | `48px` | Major grouping |

### Layout Rules
- Keep authentication and settings flows direct and low-friction.
- Group account, org, and security content into clear panels.
- Preserve a visible primary action without crowding the interface.
- Favor repeatable form and card layouts over bespoke compositions.

---

## 6. Depth & Elevation

### Surface Hierarchy

| Level | Treatment | Use |
|-------|-----------|-----|
| Base | light neutral page background | Main canvas |
| Card | white bounded panel | Default grouping |
| Auth panel | elevated white surface | Focused sign-in or setup flow |
| Overlay | stronger elevated surface | Dialog or drawer |

### Shadow System

```css
.shadow-card {
  box-shadow: 0 6px 14px rgba(15, 23, 42, 0.06);
}

.shadow-overlay {
  box-shadow: 0 18px 30px rgba(15, 23, 42, 0.14);
}
```

### Depth Rules
- Use subtle depth to reinforce workflow focus.
- Keep cards restrained and clean.
- Let dialogs and auth flows stand out without becoming glossy.

---

## 7. Do's and Don'ts

### Do
- Use blue consistently for primary interaction.
- Keep identity flows clear and accessible.
- Reuse Odyssey patterns wherever possible.
- Favor clarity and trust over branding theatrics.
- Make form validation states obvious.

### Don't
- Overuse accent colors.
- Hide important actions in dense settings layouts.
- Let auth UI feel playful or experimental.
- Break consistency between similar workflow screens.

---

## 8. Responsive Behavior

### Responsive Rules
- Stack account and security panels early on smaller screens.
- Keep buttons and form controls touch-friendly.
- Preserve a simple single-column auth flow on mobile.
- Keep validation and helper text visible without crowding.

### Mobile Character
Okta mobile interfaces should still feel safe and direct. The experience should simplify without losing its strong action hierarchy or accessibility.

---

## 9. Agent Prompt Guide

### Quick Reference
- **Mood**: trusted, clear, accessible
- **Primary accent**: Okta blue `#1662DD`
- **Layout**: panel-driven identity workflows
- **Components**: rounded enterprise controls, clear auth panels, restrained cards

### Prompt Snippet

```text
Design this interface in the style of Okta’s Odyssey design system. Use a bright blue primary action color (#1662DD), highly readable neutral surfaces, accessible form patterns, and panel-based identity workflows. The result should feel secure, consistent, and efficient rather than flashy or overly decorative.
```
