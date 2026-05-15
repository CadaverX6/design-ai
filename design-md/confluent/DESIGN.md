# Confluent Design System

> Data-streaming platform design with bright coral energy, cloud-native confidence, and modular enterprise storytelling. Confluent’s current site uses strong accent color, dark product surfaces, and concise technical narratives to make real-time data infrastructure feel approachable and urgent.

---

## 1. Visual Theme & Atmosphere

### Overall Aesthetic
Confluent expresses **real-time data momentum**. The site should feel fast, modern, and technically capable while keeping cloud and AI narratives understandable for both practitioners and buyers.

### Mood & Feeling
- **Innovative**: streaming, AI, and cloud-native ideas should feel current
- **Credible**: the platform must still read as enterprise-grade
- **Energetic**: bright accent color and punchy layouts create motion
- **Modular**: platform capabilities are grouped into clear use-case bands
- **Technical**: screenshots and diagrams should feel real, not abstract fluff

### Design Density
**Medium density**. Confluent pages often cover multiple use cases and outcomes, but they maintain readability through strong sectioning, concise copy, and repeated CTA patterns.

### Visual Character
- Bright coral-red accent over white and dark frames
- Product screenshots and capability modules
- Strong call-to-action rhythm
- Clean enterprise typography with short headlines
- Balanced technical and business storytelling

---

## 2. Color Palette & Roles

### Core Brand Colors

| Token | Hex | Role |
|-------|-----|------|
| `--confluent-coral` | `#FF5F46` | Primary accent and CTA emphasis |
| `--confluent-coral-dark` | `#E84A32` | Hover / active state |
| `--confluent-coral-soft` | `#FFE7E1` | Light brand surface |

### Neutral and Dark Surfaces

| Token | Hex | Role |
|-------|-----|------|
| `--ink-strong` | `#132238` | Primary text |
| `--ink-default` | `#334155` | Body text |
| `--ink-muted` | `#64748B` | Secondary text |
| `--surface-page` | `#F8FAFC` | Page background |
| `--surface-card` | `#FFFFFF` | Card surface |
| `--surface-dark` | `#0F172A` | Product / technical showcase frame |
| `--border-default` | `#E2E8F0` | Border and divider |

### Supportive Colors

| Token | Hex | Role |
|-------|-----|------|
| `--blue` | `#3B82F6` | Informational highlight |
| `--green` | `#16A34A` | Success / positive outcome |
| `--yellow` | `#EAB308` | Caution / attention |

### Color Usage Rules
- Use coral as the clearest brand and action signal.
- Keep most page structure neutral and readable.
- Use dark product frames to reinforce technical depth.

---

## 3. Typography Rules

### Font Stack

```css
/* Modern data-platform sans */
--font-sans: Inter, 'Helvetica Neue', Arial, sans-serif;
--font-mono: 'SF Mono', 'Roboto Mono', Menlo, monospace;
```

### Type Scale

| Element | Size | Weight | Line Height | Letter Spacing | Usage |
|---------|------|--------|-------------|----------------|-------|
| Hero Display | 56px | 700 | 1.04 | -0.02em | Main hero headline |
| Page Title | 40px | 700 | 1.1 | -0.015em | Major section title |
| Section Title | 28px | 600 | 1.15 | -0.01em | Use-case heading |
| Card Title | 20px | 600 | 1.25 | 0 | Card or feature title |
| Body | 16px | 400 | 1.6 | 0 | Standard content |
| Small Body | 14px | 400 | 1.5 | 0 | Secondary content |
| Label | 14px | 600 | 1.3 | 0.01em | Buttons and utility labels |
| Code | 13px | 400 | 1.5 | 0 | Technical values |

### Typography Philosophy
Confluent typography should feel **current, technical, and concise**. The hierarchy needs to support both platform breadth and fast-scanning product decisions.

### Practical Rules
- Keep headlines short and momentum-driven.
- Use modular body copy chunks instead of long explanations.
- Use mono styles for technical examples and code-adjacent content.

---

## 4. Component Stylings

### Buttons

#### Primary Button
```css
.button-primary {
  background: #FF5F46;
  color: #FFFFFF;
  min-height: 44px;
  padding: 0 18px;
  border: 1px solid #FF5F46;
  border-radius: 999px;
  font: 600 14px/1 Inter, sans-serif;
}

.button-primary:hover {
  background: #E84A32;
  border-color: #E84A32;
}
```

#### Secondary Button
```css
.button-secondary {
  background: #FFFFFF;
  color: #132238;
  min-height: 44px;
  padding: 0 18px;
  border: 1px solid #E2E8F0;
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
  color: #132238;
  border: 1px solid #E2E8F0;
  border-radius: 14px;
  font: 400 16px/1.2 Inter, sans-serif;
}
```

### Cards and Product Frames

#### Feature Card
```css
.card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 20px;
  padding: 24px;
}
```

#### Dark Product Frame
```css
.product-frame {
  background: #0F172A;
  color: #FFFFFF;
  border-radius: 24px;
  padding: 24px;
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
| `--space-10` | `64px` | Large rhythm |

### Layout Rules
- Structure the platform story into clear use-case modules.
- Repeat CTA patterns for product, demo, and free-start actions.
- Use screenshots and proof blocks to support technical credibility.
- Keep the page scannable despite breadth.

---

## 6. Depth & Elevation

### Surface Hierarchy

| Level | Treatment | Use |
|-------|-----------|-----|
| Light base | light neutral page field | Overview and narrative |
| Feature card | white bounded module | Capability grouping |
| Dark frame | dark product surface | Technical / demo focus |
| Overlay | elevated light surface | Form or modal |

### Shadow System

```css
.shadow-card {
  box-shadow: 0 8px 18px rgba(19, 34, 56, 0.08);
}

.shadow-dark {
  box-shadow: 0 18px 30px rgba(15, 23, 42, 0.18);
}
```

### Depth Rules
- Use white cards and dark frames deliberately.
- Let screenshots and product UI add technical richness.
- Keep the main layout airy, even when the product story is broad.

---

## 7. Do's and Don'ts

### Do
- Use coral as the clear action and brand cue.
- Keep platform storytelling modular.
- Use dark frames to anchor technical credibility.
- Preserve clear CTA hierarchy.
- Make technical breadth feel manageable.

### Don't
- Flood the page with too many bright accents.
- Turn technical sections into vague AI glow art.
- Overload individual cards with too much copy.
- Let screenshots feel disconnected from the surrounding design.

---

## 8. Responsive Behavior

### Responsive Rules
- Stack feature cards and dark product frames cleanly on mobile.
- Keep core demo and free-start CTAs visible early.
- Simplify dense proof sections before shrinking type too far.
- Preserve strong card and section boundaries at every width.

### Mobile Character
Confluent mobile layouts should still feel energetic and technical. The coral accent and modular product narrative need to remain clear even when the page becomes more vertical.

---

## 9. Agent Prompt Guide

### Quick Reference
- **Mood**: innovative, technical, modular
- **Primary accent**: coral `#FF5F46`
- **Base structure**: light neutral field with dark product frames
- **Typography**: modern concise enterprise sans
- **Components**: pill CTAs, capability cards, dark showcase panels

### Prompt Snippet

```text
Design this interface in the style of Confluent’s current data streaming platform website. Use coral-red (#FF5F46) for primary emphasis, clean neutral page structure, dark technical product frames, and concise modern typography. The result should feel energetic, cloud-native, and credible without becoming noisy or overdecorated.
```
