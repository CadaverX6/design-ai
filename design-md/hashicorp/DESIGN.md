# HashiCorp Design System

> Infrastructure-cloud branding with elegant black-and-white fundamentals, custom typography, and portfolio gradients derived from product colors. HashiCorp’s current brand feels refined, technical, and visually confident without losing enterprise clarity.

---

## 1. Visual Theme & Atmosphere

### Overall Aesthetic
HashiCorp expresses **infrastructure sophistication**. The brand is minimal at its core, using black and white as the foundation, then layering product-derived gradients and precise typography to create high-end technical storytelling.

### Mood & Feeling
- **Elegant**: the brand should feel premium and composed
- **Technical**: infrastructure and security remain central
- **Confident**: the visuals should feel decisive, not busy
- **Modern**: gradients and typography give it current energy
- **Systematic**: product colors are used with restraint and intention

### Design Density
**Medium density**. HashiCorp pages often explain portfolio-level ideas, but the system gives those ideas strong visual framing and breathing room.

### Visual Character
- Black and white as the fundamental palette
- Brand gradients used for headlines, strokes, glows, and patterns
- Bespoke type for titles paired with simpler body text
- Clean product storytelling modules
- High contrast and strong spacing

---

## 2. Color Palette & Roles

### Spot Colors

| Token | Hex | Role |
|-------|-----|------|
| `--hashi-black` | `#000000` | Primary contrast and text |
| `--hashi-white` | `#FFFFFF` | Layout foundation |

### Brand Gradient Support

| Token | Hex | Role |
|-------|-----|------|
| `--terraform-purple` | `#844FBA` | Product-derived portfolio reference |
| `--vault-red` | `#E4572E` | Security accent reference |
| `--consul-blue` | `#1F6FEB` | Network/infrastructure accent reference |
| `--nomad-green` | `#6CBF84` | Workload / orchestration accent reference |
| `--brand-gradient` | `linear-gradient(90deg, #844FBA 0%, #1F6FEB 50%, #6CBF84 100%)` | Brand-agnostic headline / glow treatment |

### Neutral Support

| Token | Hex | Role |
|-------|-----|------|
| `--gray-100` | `#F5F5F5` | Light section fill |
| `--gray-400` | `#7A7A7A` | Secondary text |
| `--gray-700` | `#333333` | Dense secondary text |

### Color Usage Rules
- White is generally the foundation.
- Black is used for intentional contrast.
- Product colors and gradients highlight featured content and actions, not every surface.
- Keep the palette refined and simplified even when using multi-color gradients.

---

## 3. Typography Rules

### Font Stack

```css
/* HashiCorp brand typography */
--font-display: 'HashiCorp Sans', Inter, 'Helvetica Neue', Arial, sans-serif;
--font-sans: 'Metro Sans', Inter, 'Helvetica Neue', Arial, sans-serif;
--font-mono: 'SF Mono', 'Roboto Mono', Menlo, monospace;
```

### Type Scale

| Element | Size | Weight | Line Height | Letter Spacing | Usage |
|---------|------|--------|-------------|----------------|-------|
| Hero Display | 56px | 600 | 1.04 | -0.02em | Brand and portfolio hero |
| Page Title | 40px | 600 | 1.1 | -0.015em | Major title |
| Section Title | 28px | 600 | 1.15 | -0.01em | Section heading |
| Card Title | 20px | 600 | 1.25 | 0 | Product or feature card |
| Body | 16px | 400 | 1.6 | 0 | Main content |
| Small Body | 14px | 400 | 1.5 | 0 | Secondary content |
| Label | 14px | 600 | 1.3 | 0.01em | Buttons and controls |

### Typography Philosophy
HashiCorp Sans adds **warmth, sparkle, and movement** to titles, while Metro Sans keeps body content straightforward and durable.

### Practical Rules
- Use sentence case for headlines and body copy.
- Reserve HashiCorp Sans for headlines, subheads, and titles.
- Use Metro Sans for body copy and long descriptions.

---

## 4. Component Stylings

### Buttons

#### Primary Button
```css
.button-primary {
  background: #000000;
  color: #FFFFFF;
  min-height: 44px;
  padding: 0 18px;
  border: 1px solid #000000;
  border-radius: 999px;
  font: 600 14px/1 'Metro Sans', sans-serif;
}
```

#### Secondary Button
```css
.button-secondary {
  background: #FFFFFF;
  color: #000000;
  min-height: 44px;
  padding: 0 18px;
  border: 1px solid #000000;
  border-radius: 999px;
}
```

#### Gradient Highlight Button
```css
.button-highlight {
  background: linear-gradient(90deg, #844FBA 0%, #1F6FEB 100%);
  color: #FFFFFF;
  min-height: 44px;
  padding: 0 18px;
  border: none;
  border-radius: 999px;
}
```

### Inputs

#### Text Input
```css
.input {
  width: 100%;
  min-height: 44px;
  padding: 0 14px;
  background: #FFFFFF;
  color: #000000;
  border: 1px solid #D9D9D9;
  border-radius: 12px;
  font: 400 16px/1.2 'Metro Sans', sans-serif;
}
```

### Cards and Portfolio Modules

#### Card
```css
.card {
  background: #FFFFFF;
  border: 1px solid #E5E5E5;
  border-radius: 20px;
  padding: 24px;
}
```

#### Gradient Panel
```css
.gradient-panel {
  background: linear-gradient(135deg, #F5F5F5 0%, #FFFFFF 100%);
  border-radius: 24px;
  padding: 28px;
}
```

---

## 5. Layout Principles

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--space-2` | `8px` | Tight spacing |
| `--space-4` | `16px` | Core spacing |
| `--space-5` | `24px` | Card spacing |
| `--space-6` | `32px` | Section spacing |
| `--space-8` | `48px` | Major grouping |
| `--space-10` | `64px` | Large layout rhythm |

### Layout Rules
- Use white as the base of most layouts.
- Apply gradients as focused brand moments.
- Keep infrastructure and security concepts framed in clean modular sections.
- Let headlines and product stories breathe.

---

## 6. Depth & Elevation

### Surface Hierarchy

| Level | Treatment | Use |
|-------|-----------|-----|
| White base | clean layout foundation | Main content field |
| Light card | white with subtle border | Product or feature grouping |
| Gradient panel | refined branded surface | Hero or spotlight module |
| Overlay | elevated clean surface | Modal or high-focus flow |

### Shadow System

```css
.shadow-card {
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.06);
}

.shadow-overlay {
  box-shadow: 0 18px 32px rgba(0, 0, 0, 0.12);
}
```

### Depth Rules
- Keep depth elegant and understated.
- Let contrast and gradient treatment drive visual interest.
- Avoid over-layering within already strong brand sections.

---

## 7. Do's and Don'ts

### Do
- Start with black and white.
- Use gradients for featured content and actions.
- Use HashiCorp Sans for titles and Metro Sans for body copy.
- Keep enterprise messaging clean and premium.
- Preserve strong white space and contrast.

### Don't
- Use product colors as a general-purpose UI rainbow.
- Crowd a section with too many branded effects.
- Dilute the brand with generic SaaS styling.
- Let gradients replace hierarchy or structure.

---

## 8. Responsive Behavior

### Responsive Rules
- Keep headlines and gradients impactful on smaller screens by simplifying compositions.
- Stack modular product content cleanly.
- Preserve CTA clarity and spacing in portfolio sections.
- Maintain strong reading measures even in technical explainer blocks.

### Mobile Character
HashiCorp mobile should still feel elegant and technically assured. The contrast and gradient moments can simplify, but the refined brand tone should remain obvious.

---

## 9. Agent Prompt Guide

### Quick Reference
- **Mood**: elegant, technical, premium
- **Core palette**: black, white, refined product-derived gradients
- **Typography**: HashiCorp Sans + Metro Sans
- **Layout**: clean white base with modular spotlight sections
- **Components**: pill buttons, clean cards, gradient highlight panels

### Prompt Snippet

```text
Design this interface in the style of HashiCorp’s current brand system. Use black and white as the base, refine the visual hierarchy with product-derived gradients, apply HashiCorp Sans to titles and Metro Sans to body copy, and keep the layout spacious and modular. The result should feel elegant, technical, and infrastructure-grade rather than generic SaaS.
```
