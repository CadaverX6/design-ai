# Ramp Design System

> Corporate finance design with confident green identity, spend-control surfaces, real-time savings highlights, and finance-team clarity.

---

## 1. Visual Theme & Atmosphere

Ramp should feel smart, efficient, and trustworthy. The design language communicates corporate cards, expense management, bill payments, procurement, and AI-powered savings recommendations.

- Mood: smart, efficient, modern, trustworthy
- Density: medium-to-high, with spend tables, card management, savings dashboards, and approval flows
- Character: confident green brand, crisp white finance surfaces, savings-first messaging, clean data hierarchy

## 2. Color Palette & Roles

| Token | Hex | Role |
|-------|-----|------|
| `--ramp-green` | `#27AE60` | Primary brand CTA and savings highlight |
| `--ramp-green-dark` | `#1E8A4A` | Hover and active states |
| `--ramp-black` | `#0A0A0A` | Premium card surface and dark accents |
| `--ramp-blue` | `#2563EB` | Secondary actions and informational |
| `--ramp-amber` | `#D97706` | Pending approval and review state |
| `--ramp-red` | `#DC2626` | Declined transaction and error |
| `--surface-card` | `#FFFFFF` | Spend and employee cards |
| `--surface-bg` | `#F8FAFC` | Dashboard background |
| `--surface-dark` | `#0A0A0A` | Physical card mockup surface |
| `--text-primary` | `#111827` | Transaction amounts and labels |
| `--text-secondary` | `#6B7280` | Merchant names and timestamps |
| `--border-default` | `#E5E7EB` | Table and panel borders |

Green is the primary action and savings signal. The physical card mockup uses near-black as its surface — this is a signature Ramp visual.

## 3. Typography Rules

```css
--font-sans: Inter, ui-sans-serif, system-ui, -apple-system, sans-serif;
--font-mono: "JetBrains Mono", "SF Mono", Menlo, monospace;
```

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Page Title | 30px | 700 | 1.1 |
| Section Title | 22px | 600 | 1.2 |
| Savings Amount | 40px | 700 | 1.0 |
| Transaction Amount | 16px | 600 | 1.3 |
| Body | 15px | 400 | 1.6 |
| Merchant Name | 14px | 500 | 1.4 |
| Label | 12px | 600 | 1.35 |

## 4. Component Stylings

```css
.button-primary {
  min-height: 40px;
  padding: 0 18px;
  border: none;
  border-radius: 8px;
  background: #27AE60;
  color: #FFFFFF;
  font: 600 14px/1 Inter, sans-serif;
}

.corporate-card {
  border-radius: 16px;
  background: #0A0A0A;
  color: #FFFFFF;
  padding: 24px;
  aspect-ratio: 1.586 / 1;
}

.transaction-row {
  display: flex;
  align-items: center;
  padding: 14px 16px;
  border-bottom: 1px solid #F1F5F9;
}

.savings-badge {
  display: inline-flex;
  padding: 4px 12px;
  border-radius: 999px;
  background: #DCFCE7;
  color: #166534;
  font: 700 13px/1.4 Inter, sans-serif;
}
```

## 5. Layout Principles

| Token | Value | Usage |
|-------|-------|-------|
| `--space-3` | `12px` | Transaction row padding |
| `--space-5` | `20px` | Card content rhythm |
| `--space-8` | `32px` | Section separation |
| `--space-14` | `56px` | Major page sections |

Lead with total savings at the top of the dashboard — it is Ramp's core value proposition. Transaction feed below. Pending approvals should be surfaced immediately with a clear count.

## 6. Depth & Elevation

```css
.shadow-card     { box-shadow: 0 2px 8px rgba(17, 24, 39, 0.06); }
.shadow-savings  { box-shadow: 0 8px 24px rgba(39, 174, 96, 0.12); }
.shadow-modal    { box-shadow: 0 20px 52px rgba(17, 24, 39, 0.16); }
```

The savings summary card gets a green-tinted shadow to reinforce the positive financial impact message.

## 7. Do's and Don'ts

Do lead with total savings on every dashboard view. Do use the 1.586:1 aspect ratio for physical card mockups. Do use mono font for all card numbers and transaction IDs. Do not use red for brand elements — reserve it strictly for declined or error states. Do not bury the pending approvals count.

## 8. Responsive Behavior

| Breakpoint | Min Width | Behavior |
|------------|-----------|----------|
| Mobile | `0px` | Transaction feed, receipt upload, card freeze toggle |
| Tablet | `768px` | Spend overview + transaction list |
| Desktop | `1200px` | Full finance dashboard: cards, spend, approvals, savings |

Mobile is essential — employees submit receipts and check limits on the go.

## 9. Agent Prompt Guide

Design like Ramp: confident green CTAs, near-black corporate card mockup, savings-first dashboard hierarchy, clean transaction feeds, green savings badges, and modern B2B finance clarity.
