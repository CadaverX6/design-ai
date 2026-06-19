# PostHog Design System

> Open-source product analytics design with bold hedgehog-orange identity, self-hosted-first surfaces, event-explorer clarity, and developer-native UX.

---

## 1. Visual Theme & Atmosphere

PostHog should feel open, powerful, and irreverently developer-friendly. The design language communicates product analytics, session replay, feature flags, A/B testing, and data pipelines — all self-hostable and open source.

- Mood: bold, open, developer-native, playful yet powerful
- Density: high, with event tables, funnel charts, session replay timelines, and feature-flag lists
- Character: bold orange-red brand, dark charcoal surfaces, off-white canvas, hedgehog mascot moments

## 2. Color Palette & Roles

| Token | Hex | Role |
|-------|-----|------|
| `--ph-orange` | `#F54E00` | Primary brand CTA and hedgehog identity |
| `--ph-orange-dark` | `#C43D00` | Hover and active states |
| `--ph-yellow` | `#F9BD2B` | Secondary accent and highlight |
| `--ph-teal` | `#1DC9B7` | Session replay and heatmap accent |
| `--ph-green` | `#36B37E` | Flag enabled and success state |
| `--ph-red` | `#F3333D` | Error and flag disabled |
| `--surface-card` | `#FFFFFF` | Chart cards and event panels |
| `--surface-bg` | `#F9F4F0` | Warm off-white background |
| `--surface-dark` | `#1D1F27` | Dark mode and query panel |
| `--text-primary` | `#1D1F27` | Primary labels and titles |
| `--text-secondary` | `#747EA3` | Secondary labels and axis text |
| `--border-default` | `#E8E8E8` | Panel and table borders |

Orange is the signature color — used for the primary CTA and any brand-moment. Teal is reserved exclusively for session replay and heatmap features.

## 3. Typography Rules

```css
--font-sans: "Matter", Inter, ui-sans-serif, system-ui, -apple-system, sans-serif;
--font-mono: "Source Code Pro", "JetBrains Mono", Menlo, monospace;
```

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Hero Display | 56px | 800 | 1.0 |
| Page Title | 32px | 700 | 1.1 |
| Section Title | 22px | 600 | 1.2 |
| Card Title | 18px | 600 | 1.3 |
| Body | 15px | 400 | 1.65 |
| Event Name | 14px | 600 | 1.35 |
| Code / Event Key | 13px | 400 | 1.6 |
| Label | 12px | 600 | 1.35 |

## 4. Component Stylings

```css
.button-primary {
  min-height: 40px;
  padding: 0 18px;
  border: none;
  border-radius: 8px;
  background: #F54E00;
  color: #FFFFFF;
  font: 700 14px/1 "Matter", Inter, sans-serif;
}

.insight-card {
  border: 1px solid #E8E8E8;
  border-radius: 12px;
  background: #FFFFFF;
  padding: 20px 24px;
}

.event-chip {
  display: inline-flex;
  padding: 3px 10px;
  border-radius: 6px;
  background: #FFF1EB;
  color: #F54E00;
  font: 600 12px/1.4 "Matter", sans-serif;
}

.flag-toggle {
  width: 40px;
  height: 22px;
  border-radius: 999px;
  background: #F3333D;
  transition: background 0.2s;
}

.flag-toggle.enabled {
  background: #36B37E;
}
```

## 5. Layout Principles

| Token | Value | Usage |
|-------|-------|-------|
| `--space-2` | `8px` | Event table row padding |
| `--space-4` | `16px` | Card content rhythm |
| `--space-6` | `24px` | Section padding |
| `--space-10` | `40px` | Dashboard section gaps |

Product tour-style left navigation by feature category. The insight builder at the top of every analytics view. Session replay timeline should fill at least 60% of the viewport width.

## 6. Depth & Elevation

```css
.shadow-card   { box-shadow: 0 2px 8px rgba(29, 31, 39, 0.07); }
.shadow-panel  { box-shadow: 0 8px 24px rgba(245, 78, 0, 0.10); }
.shadow-modal  { box-shadow: 0 20px 50px rgba(29, 31, 39, 0.16); }
```

The warm off-white background gives cards natural visual lift without heavy shadows.

## 7. Do's and Don'ts

Do make the event capture setup the first experience for every new user. Do use the hedgehog mascot in empty states and onboarding — it's a PostHog signature. Do use mono font for all event names and property keys. Do not repurpose orange for error states. Do not bury the self-hosting documentation — it is a primary value proposition.

## 8. Responsive Behavior

| Breakpoint | Min Width | Behavior |
|------------|-----------|----------|
| Mobile | `0px` | Key metric summary, feature flag toggles |
| Tablet | `768px` | Simplified funnel and trends view |
| Desktop | `1200px` | Full analytics workspace: insights, session replay, flags |

Desktop is the primary surface. Mobile is for quick monitoring checks.

## 9. Agent Prompt Guide

Design like PostHog: bold orange CTAs, warm off-white canvas, hedgehog mascot in empty states, teal session-replay accents, mono event keys, open-source developer tone, and insight-first product analytics hierarchy.
