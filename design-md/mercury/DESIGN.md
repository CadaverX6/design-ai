# Mercury Design System

> Startup banking design with clean navy identity, founder-forward surfaces, treasury clarity, and modern financial infrastructure UX.

---

## 1. Visual Theme & Atmosphere

Mercury should feel calm, sophisticated, and founder-friendly. The design language communicates banking, treasury, venture debt, and financial tools built specifically for startups and tech companies.

- Mood: sophisticated, calm, modern, founder-focused
- Density: low-to-medium, with generous whitespace, clean account views, and treasury dashboards
- Character: clean navy brand, crisp white banking surfaces, minimal decoration, elegant typography

## 2. Color Palette & Roles

| Token | Hex | Role |
|-------|-----|------|
| `--merc-navy` | `#1A2744` | Primary brand and CTA |
| `--merc-navy-dark` | `#111B30` | Hover and active states |
| `--merc-teal` | `#0D9488` | IO savings and yield accent |
| `--merc-green` | `#16A34A` | Positive balance and completed transfer |
| `--merc-amber` | `#D97706` | Pending transfer and review |
| `--merc-red` | `#DC2626` | Declined and error states |
| `--surface-card` | `#FFFFFF` | Account and transfer cards |
| `--surface-bg` | `#F9FAFB` | Dashboard background |
| `--surface-dark` | `#1A2744` | Physical card and premium surface |
| `--text-primary` | `#111827` | Balances and transaction labels |
| `--text-secondary` | `#6B7280` | Account details and timestamps |
| `--border-default` | `#E5E7EB` | Card and table borders |

Navy is the dominant brand color. Teal is exclusively for Mercury IO (savings/yield product) — never use it for general UI elements.

## 3. Typography Rules

```css
--font-sans: "Söhne", Inter, ui-sans-serif, system-ui, -apple-system, sans-serif;
--font-mono: "Söhne Mono", "JetBrains Mono", Menlo, monospace;
```

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Hero Balance | 52px | 300 | 1.0 |
| Page Title | 32px | 400 | 1.1 |
| Section Title | 22px | 500 | 1.2 |
| Card Title | 18px | 500 | 1.3 |
| Body | 16px | 400 | 1.65 |
| Transaction Amount | 15px | 600 | 1.3 |
| Label | 13px | 500 | 1.4 |

Use light-to-regular weight for display type — Mercury's sophistication comes from restraint, not weight.

## 4. Component Stylings

```css
.button-primary {
  min-height: 44px;
  padding: 0 22px;
  border: none;
  border-radius: 8px;
  background: #1A2744;
  color: #FFFFFF;
  font: 500 15px/1 "Söhne", Inter, sans-serif;
}

.account-card {
  border: 1px solid #E5E7EB;
  border-radius: 16px;
  background: #FFFFFF;
  padding: 28px;
}

.bank-card-mock {
  border-radius: 16px;
  background: linear-gradient(145deg, #1A2744, #0D1A33);
  color: #FFFFFF;
  padding: 28px;
  aspect-ratio: 1.586 / 1;
}

.transaction-row {
  display: flex;
  align-items: center;
  padding: 16px;
  border-bottom: 1px solid #F3F4F6;
}
```

## 5. Layout Principles

| Token | Value | Usage |
|-------|-------|-------|
| `--space-4` | `16px` | Core content rhythm |
| `--space-6` | `24px` | Card padding |
| `--space-10` | `40px` | Section separation |
| `--space-16` | `64px` | Major page sections |

Show total balance prominently at the top. Account breakdown (checking, savings, IO) directly below. Transaction feed takes the lower half. The layout should feel like a well-designed financial dashboard, not a consumer app.

## 6. Depth & Elevation

```css
.shadow-card   { box-shadow: 0 1px 4px rgba(17, 24, 39, 0.05); }
.shadow-panel  { box-shadow: 0 8px 24px rgba(26, 39, 68, 0.08); }
.shadow-modal  { box-shadow: 0 24px 56px rgba(17, 24, 39, 0.14); }
```

Mercury's elegance depends on restraint — shadows are subtle. Let whitespace and typography do the heavy lifting.

## 7. Do's and Don'ts

Do use light weight typography for balance displays — it reads as confident and sophisticated. Do keep whitespace generous throughout. Do reserve teal exclusively for IO/savings features. Do not use flashy gradients or bold colors on primary banking surfaces. Do not crowd the account overview — clarity is the product.

## 8. Responsive Behavior

| Breakpoint | Min Width | Behavior |
|------------|-----------|----------|
| Mobile | `0px` | Balance view, recent transactions, transfer action |
| Tablet | `768px` | Account summary + transaction list side-by-side |
| Desktop | `1200px` | Full dashboard: all accounts, transactions, treasury, team |

Both mobile and desktop are primary — founders use both contexts heavily.

## 9. Agent Prompt Guide

Design like Mercury: clean navy CTAs, light-weight display typography, navy card mockup, generous whitespace, teal IO savings accent, minimal decoration, and founder-focused startup banking hierarchy.
