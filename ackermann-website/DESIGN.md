# Ackermann Gebäudetechnik — „Werkplan" Design System

> Technische Gebäudeausrüstung als Werkplan gelesen. Weißes Blatt (#FFFFFF), schwarze Typografie (#111111), Haarlinien mit drei bedeutungstragenden Grauwerten, ein DIN-Schriftfeld als wiederkehrender Container und genau ein roter Akzent pro Ansicht. IBM Plex Sans für Text, IBM Plex Mono für jede Zahl, die eine Messung ist. Sachlich, nummeriert, im Raster — „langweilig gut" im Sinn einer korrekt gezeichneten Werkstattzeichnung.

---

## 1. Visual Theme & Atmosphere

### Overall Aesthetic
Die Seite übernimmt die visuelle Grammatik, in der die Zielgruppe ohnehin arbeitet: Werkpläne, Anlagenschemata, Leistungsverzeichnisse mit Positionsnummern, Schriftfelder. Diese Dokumentkultur ist bereits ruhig, bereits nummeriert, bereits im Raster — und signalisiert Kompetenz ohne ein einziges Adjektiv. Statt einen „Corporate Look" zu erfinden und zu hoffen, dass er technisch wirkt, wird die Sprache übernommen, die das Publikum bereits als neutral liest.

### Mood & Feeling
- **Nachweis statt Behauptung** — Referenzen tragen das Argument, nicht Qualitätsversprechen
- **Ausführend, nicht planend** — die Zeichnung der ausführenden Seite, nie der Entwurf des Planungsbüros
- **Wiederholbar** — derselbe Block erscheint auf jeder Projektseite identisch
- **Beschriftet** — jede Zahl trägt ein Label, jedes Foto eine Bildunterschrift
- **Unaufgeregt** — nichts wird über Stimmung entschieden

### Design Density
Mittlere Dichte mit hartem Deckel. Abschnittsabstand maximal 96 px — nichts auf dieser Seite ist je weiter getrennt. Diese eine Disziplin hält den Auftritt im Register „langweilig gut" statt im Register „Premium-Galerie". Weiß belegt ≥ 75 % jeder Ansicht.

### Visual Character
- Weißes Blatt als Grundfläche, ein einziges Alternativband (#FAFAFA)
- Vier ambiente 1-px-Rasterlinien laufen hinter dem Inhalt
- Radius 0 ausnahmslos — keine Karte, kein Bild, kein Bedienelement
- Keine Schatten, keine Verläufe, keine Füllflächen
- Kanten- statt Mittenausrichtung; nichts ist zentriert
- Fortlaufende Abschnittsnummern wie LV-Positionen

---

## 2. Color Palette & Roles

### Core Foundation

| Token | Hex | Role |
|-------|-----|------|
| `--paper` | `#FFFFFF` | Grundfläche. ≥ 75 % jeder Ansicht |
| `--paper-alt` | `#FAFAFA` | Einziges Alternativband. Max. 2 pro Seite, nie benachbart, nie im Hero, nie im Footer |
| `--ink-900` | `#111111` | Überschriften, Abschnittslinien, Schriftfeldrahmen, Positionslinie |
| `--ink-800` | `#262626` | Fließtext und Lead. 14,5:1 auf Weiß |
| `--ink-500` | `#6F6F6F` | Labels, Gewerke, Bildunterschriften, Indizes, Prozesspfeile |

### Hairlines — drei Grauwerte, drei Bedeutungen

| Token | Hex | Role |
|-------|-----|------|
| `--ink-300` | `#C6C6C6` | Strukturelle Kappe: Prozessbasislinie, Tabellenabschluss |
| `--ink-200` | `#E0E0E0` | Gewöhnliche Trennung: Tabellenzeilen, Bildkante, Header-Unterkante |
| `--raster` | `#EDEDED` | Ausschließlich die vier Rasterlinien. Nie Rahmen, nie Fläche |

Diese drei dürfen nicht getauscht werden — der Grauwert *ist* die Aussage.

### Brand Accent — sämtlich Platzhalter

| Token | Hex | Role |
|-------|-----|------|
| `--ack-red` | `#CC0605` | **PLATZHALTER** (RAL 3020 Verkehrsrot). Aus dem Logo ableiten |
| `--ack-red-deep` | `#A30504` | **PLATZHALTER**. Hover/Aktiv des Pfeils |

Der Stellvertreter ist so gewählt, dass Kontrast und Gewicht bereits realistisch sind. Beim Ableiten des echten Wertes: Kontrast auf Weiß prüfen (Pfeilglyphe ≥ 4,5:1), `--ack-red-deep` bei etwa −20 % Helligkeit neu bilden.

---

## 3. Typography Rules

### Font Stack

```css
--sans: 'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif;
--mono: 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
```

Mono gilt für **jede Zahl, die eine Messung ist**: kW, Liter, WE, DN, m², Telefonnummern, Datumsangaben, Abschnitts- und Positionsnummern. Immer mit `font-variant-numeric: tabular-nums`, damit 650 kW, 370 kW und 8.100 Liter über Projektseiten hinweg exakt untereinander stehen.

**Produktion:** Fonts selbst hosten (woff2, Subsets latin + latin-ext). Ein Aufruf des Google-CDN ist ein vermeidbarer Datenschutz-Befund.

### Type Scale

| Stil | Desktop | Mobil | Verwendung |
|------|---------|-------|------------|
| H1 | 48 / 1.10 / −0.02em / 500 | 32 / 1.15 | Seitentitel, einmal je Seite |
| H2 | 32 / 1.15 / −0.015em / 500 | 26 / 1.20 | Abschnittsüberschrift |
| H3 | 22 / 1.25 / −0.01em / 600 | 20 | Referenzkarte, Aussageblock |
| H4 | 18 / 1.35 / 600 | 18 | Blocküberschrift |
| Lead | 18 / 1.60 / 400 | 18 | Genau ein Absatz je Seite, max. 640 px |
| Body | 16 / 1.65 / 400 | 16 | Satzbreite 752 px |
| Body S | 14 / 1.55 / 400 | 14 | Teaser, Gewerke, Links, Navigation |
| Label | 12 / 1.30 / +0.06em / 600 | 12 | Der **einzige** Versalstil, max. vier Wörter |
| Mono Daten | 13 / 1.45 / 500 | 13 | Alle Messwerte |
| Mono Index | 12 / 1.30 / 500 | 12 | Abschnitts- und Positionsnummern |
| Caption | 12 / 1.50 / 400 | 12 | Jedes Foto trägt genau eine |

### Rules
- **Maximal fünf Stile pro Seite** — bei der Abnahme zählen.
- Tracking nie enger als −0.02em. Deutsche Komposita (`Fernwärmeübergabestation`, `Trinkwasserinstallationen`) fallen darunter zu Farbe zusammen.
- Kein Letter-Spacing im Fließtext.
- `lang="de"` und `hyphens: auto` auf jedem Textcontainer ≥ 16 px; `text-wrap: balance` auf H1/H2, `text-wrap: pretty` im Fließtext.
- Auszeichnung über Gewicht (400 → 600) oder Position im Raster — nie über Farbe, nie über Größensprünge außerhalb der Skala, nie kursiv.
- Links im Fließtext: `#111111`, 1 px Unterstreichung bei 4 px Offset, kein Farbwechsel.

---

## 4. Component Stylings

### Referenzkarte — ein Positionsblatt, keine Marketingkachel
Kein Rahmen, kein Hintergrund, kein Radius, kein Schatten. Die Rasterzelle *ist* die Karte; das einzige gezeichnete Element neben dem Foto ist eine schwarze Linie.

```css
.refcard{display:flex; flex-direction:column; height:100%; text-decoration:none}
.refcard .ph{aspect-ratio:4/3; box-shadow:inset 0 0 0 1px rgba(17,17,17,.10)}
.refcard .rule{display:block; height:1px; background:#111; margin-top:16px; transition:height 120ms}
.refcard .link{margin-top:auto; padding-top:16px}      /* Links fluchten über die Zeile */
.refcard:hover .rule{height:2px}
.refcard:hover h3{text-decoration:underline; text-underline-offset:4px}
```

Reihenfolge: Foto → 16 px → Positionslinie → 12 px → `01 — WOHNEN` → 8 px → Titel → 8 px → Gewerke → 12 px → Teaser (max. 180 Zeichen, **kein** `line-clamp`, das zerlegt deutsche Wörter) → `Projekt ansehen →` mit **schwarzem** Pfeil.

Gewerke sind Klartext mit Mittelpunkt — nie Pills, nie Badges, nie farbige Chips. Ein Gewerk ist eine Tatsache, kein Tag.

### Schriftfeld — der Signature-Container
Rechteck mit 1 px `#111111` Außenrahmen, innen durch 1 px `#E0E0E0` in beschriftete Zellen geteilt. Zelle: 16 px Padding, Label, dann Wert. **Undurchsichtig** (`background:var(--paper)`), damit die Rasterlinien nicht hindurchlaufen.

Erscheint an genau drei Stellen: **Footer/Kontakt**, **Projektdaten** jeder Referenzseite, **Fertigungsnachweis** im Stationsbau. Nie dekorativ.

### Prozesskette — ein Maßstab
Eine 1-px-Basislinie über die Containerbreite; der gesamte Inhalt steht darüber, an jeder Schrittkante fällt ein 8-px-Strich darunter — die Zeile liest sich als Skala mit Graduierungen. Zwischen den Schritten ein dünnes `→` in `#6F6F6F` **auf** der Linie, mit Papierhintergrund, der die Linie unterbricht.

Mobil kippt der Maßstab: senkrechte Linie links, Striche zeigen nach links, Inhalt 24 px eingerückt, **keine Pfeile** — die durchgehende Linie verbindet.

Keine Kreise, keine Icons, keine Fortschrittsbalken, keine Farbe, keine Animation.

### Abschnittskopf — der Taktgeber
Immer vier Teile in dieser Reihenfolge: (1) 1 px `#111111` über die volle Breite, (2) 20 px darunter Mono-Index + Label auf einer Zeile (`01 — AUSGEWÄHLTE REFERENZEN`), (3) 40 px darunter die H2, (4) 32 px darunter der Inhalt. Abschnitte sind fortlaufend nummeriert wie LV-Positionen. Dieser eine wiederkehrende Kopf macht eine lange Seite ohne jedes dekorative Mittel scanbar.

### Bedienelemente
Es gibt keine Buttons. Mobil erscheinen zwei funktionale Elemente „Anrufen" und „E-Mail": 48 px hoch, 1 px `#111111` Rahmen, Radius 0, transparent, schwarzes Label, kein Icon. Nie gefüllt, nie rot.

---

## 5. Layout Principles

### Spacing Scale
8-px-Basis: `4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96`. Feste Zuweisungen: 16 = Innenabstand überall; 24 = Blockeinzug und linker Balken; 32 = Bundsteg und Hero-Abstände; 96 = Abschnittspolster (harte Obergrenze).

### Grid — 80 / 32
12 Spalten, Container 1312 px: `(1312 − 11 × 32) / 12 = 80 px` Spalte bei 32 px Bundsteg. Zwölf statt sechzehn, weil es sauber in die dreispaltige Referenzzeile (je 4) und die sechsgliedrige Prozesskette (je 2) teilt.

**Das sichtbare Raster:** vier 1-px-Linien in `#EDEDED` laufen hinter dem Inhalt an den vier Bandgrenzen. Vier, nicht dreizehn — genug, damit das Blatt lesbar wird, zu wenig, um als Debug-Overlay zu wirken. Als eine `linear-gradient`-Ebene auf einem Pseudo-Element, kein zusätzliches DOM.

```css
.sheet::before{
  content:""; position:absolute; inset:0; pointer-events:none; z-index:0;
  max-width:1312px; margin:0 auto; left:0; right:0;
  background:
    linear-gradient(var(--raster),var(--raster)) 0 0/1px 100% no-repeat,
    linear-gradient(var(--raster),var(--raster)) 448px 0/1px 100% no-repeat,
    linear-gradient(var(--raster),var(--raster)) 896px 0/1px 100% no-repeat,
    linear-gradient(var(--raster),var(--raster)) calc(100% - 1px) 0/1px 100% no-repeat;
}
```

Fotos und Schriftfelder sind undurchsichtig und liegen darüber.

### Measures
Container 1312 · Fließtext 752 (≈ 72–78 deutsche Zeichen) · Lead 640 · Referenzkarte 416 · Prozessschritt 192 (min. 140) · Schriftfeldzelle 304 · Spec-Label-Spalte 220.

Der Fließtext füllt das Blatt nie — die leeren rechten Spalten machen die Rasterlinien sichtbar und lassen die Seite wie eine Zeichnung wirken statt wie eine Textwüste.

---

## 6. Depth & Elevation

Es gibt keine Elevation. Kein `box-shadow` außer einer einzigen Ausnahme: `inset 0 0 0 1px rgba(17,17,17,.10)` auf Fotos, damit eine helle Technikraum-Aufnahme nicht in der weißen Seite zerfließt.

Hierarchie entsteht ausschließlich über **Linienstärke und Grauwert**:

| Ebene | Mittel |
|-------|--------|
| Erklärung | 1 px `#111111` — Abschnittslinie, Schriftfeldrahmen, Positionslinie |
| Struktur | 1 px `#C6C6C6` — Prozessbasis, Tabellenabschluss |
| Trennung | 1 px `#E0E0E0` — Tabellenzeilen, Bildkante |
| Ambiente | 1 px `#EDEDED` — nur die Rasterlinien |

Es existieren genau zwei Strichstärken: 1 px und — für den einen roten Aussagebalken — 3 px.

---

## 7. Do's and Don'ts

### Do
- Referenzen zeigen statt Qualität behaupten
- Jede Zahl beschriften und in Mono setzen
- Jedes Foto mit einer sachlichen Bildunterschrift versehen
- Firmennamen bei erster Nennung vollständig, danach „wir"
- Kanten ausrichten; alles beginnt an der linken Kante von Spalte 1
- Lieber sechzehn starke Referenzen als sechsundzwanzig gemischte

### Don't
- Keine Stockbilder von Monteuren, Werkzeug, Handschlag oder lächelnden Teams
- Keine Werbesprüche („Qualität aus Leidenschaft", „Ihr starker Partner")
- Keine gefüllten Buttons, keine großen CTA-Flächen, kein Kontaktformular
- Keine typischen Sanitär-/Heizungs-Icons als Gestaltungsmittel
- Keine Unternehmenshistorie oder Mitarbeiterzahl als Argument
- Keine eigene Unterseite je Gewerk
- Keine Auftragswerte
- Nichts zentrieren, nichts abrunden, nichts anheben
- Rot nie in Überschriften, Fließtext, Prozesskette, Tabellen oder Schriftfeld

### Rot-Budget
Maximal **ein rotes Element pro Ansicht** im scrollenden Inhalt (gemessen bei 1440 × 900 und 390 × 844). Der Kopfbereich — Logo und aktive Navigationsmarkierung — ist ausgenommen, weil er dauerhaft sichtbar ist. Erlaubt sind: aktive Navigationsmarkierung (2 px), Pfeilglyphe auf einzeln vorkommenden Navigationslinks, **ein** 3-px-Balken je Seite vor der tragenden Aussage, Fokusring. Der Pfeil in Referenzkarten bleibt schwarz — drei Karten pro Zeile ergäben sonst drei rote Pfeile.

Braucht ein neues Element Rot, nimmt es das Budget einer bestehenden Verwendung. Das Budget wird nie erweitert.

---

## 8. Responsive Behavior

### Breakpoints

| Bereich | Spalten | Bundsteg | Rand | Abschnittspolster |
|---------|---------|----------|------|-------------------|
| ≥ 1312 | 12 | 32 | Container 1312 zentriert | 96 |
| 1056–1311 | 12 | 32 | 32, fluid | 96 |
| 672–1055 | 8 | 24 | 24 | 64 |
| 320–671 | 4 | 16 | 16 | 48 |

Rasterlinien: vier ab 1056, drei ab 672, darunter aus.

### Umwandlungen unter 672 px
1. **Spec-Tabellen** werden gestapelte Definitionslisten — Label über Wert, 4 px Abstand, Zeilenlinien bleiben. Sie scrollen **niemals** horizontal.
2. **Prozesskette** kippt in die Senkrechte, Striche zeigen nach links, keine Pfeile.
3. **Referenzkarten** einspaltig, 48 px Zeilenabstand, Bild bleibt 4:3.
4. **Schriftfeld** verliert linken und rechten Rahmen, behält oben, unten und die inneren Linien — sonst wirkt es eng.
5. **Navigation** wird ein weißes Vollbild-Blatt, 160 ms Blende, keine Abdunklung, kein Slide.
6. **„Anrufen" / „E-Mail"** erscheinen nebeneinander, 48 px hoch, transparent mit schwarzem Rahmen.

Alle Touch-Ziele ≥ 44 px. `overflow-x: hidden` ist ein Fehlerdetektor, kein Plan — das Layout darf es nicht brauchen.

### Bekannte Druckpunkte
`Werk- und Montageplanung` im 192-px-Prozessschritt und `Fernwärmeübergabestation` in der 220-px-Label-Spalte. Beides bei 320 und 390 px mit den echten Strings prüfen. Erlaubte Mittel: zweizeiliges Label-Feld mit fester Höhe, `hyphens: auto`, mobiles Prozess-Label auf 15 px — **nicht** das Raster verkleinern, **nicht** horizontal scrollen.

---

## 9. Agent Prompt Guide

### Quick Reference
```
Grund       weiß #FFFFFF, ein Alternativband #FAFAFA (max. 2/Seite, nie benachbart)
Text        #111111 Überschriften · #262626 Fließtext · #6F6F6F Labels
Linien      #111111 Erklärung · #C6C6C6 Struktur · #E0E0E0 Trennung · #EDEDED Raster
Akzent      #CC0605 PLATZHALTER — max. 1 pro Ansicht im Inhalt
Schrift     IBM Plex Sans · IBM Plex Mono für jede Messung, tabular-nums
Raster      12 Spalten, 80/32, Container 1312, Fließtext 752
Radius      0 ausnahmslos
Schatten    keine, außer inset 1px rgba(17,17,17,.10) auf Fotos
Abstand     8er-Basis, Abschnittspolster max. 96
Bewegung    nur Pfeil +3px und Positionslinie 1→2px, je 120ms
```

### Prompt Snippet
```
Gestalte im Design-System „Werkplan" (Ackermann Gebäudetechnik):
eine Website, die wie eine korrekt gezeichnete Werkstattzeichnung wirkt.

Weißes Blatt dominiert (≥75% jeder Ansicht). Schwarze Typografie #111111,
Fließtext #262626, Labels #6F6F6F. Vier ambiente 1px-Rasterlinien in #EDEDED
hinter dem Inhalt an den Bandgrenzen des 12-Spalten-Rasters (80px Spalte,
32px Bundsteg, Container 1312px).

Typografie IBM Plex Sans; IBM Plex Mono mit tabular-nums für jede Zahl, die
eine Messung ist. Max. fünf Typo-Stile pro Seite. Tracking nie enger als
-0.02em wegen deutscher Komposita.

Jeder Abschnitt öffnet identisch: 1px schwarze Linie über volle Breite, 20px
darunter Mono-Index + Versal-Label ("01 — AUSGEWÄHLTE REFERENZEN"), 40px
darunter H2, 32px darunter Inhalt. Abschnitte fortlaufend nummeriert.

Radius 0 ausnahmslos. Keine Schatten, keine Verläufe, keine gefüllten Buttons,
kein Formular, keine Icons. Karten haben weder Rahmen noch Hintergrund — die
Rasterzelle ist die Karte, das einzige gezeichnete Element ist eine schwarze
Positionslinie über dem Titel.

Prozessketten werden als Maßstab gezeichnet: eine Basislinie, Inhalt darüber,
8px-Striche darunter an jeder Schrittkante. Mobil kippt der Maßstab senkrecht.

Wiederkehrender Container ist ein DIN-Schriftfeld: 1px schwarzer Rahmen, innen
durch 1px #E0E0E0 in beschriftete Zellen geteilt, undurchsichtig. Es dient als
Footer/Kontakt, als Projektdaten und als Fertigungsnachweis.

Rot #CC0605 höchstens einmal pro Ansicht im Inhalt: aktive Navigation, der
Pfeil eines einzeln vorkommenden Links, oder ein 3px-Balken vor der tragenden
Aussage der Seite. Sonst nirgends.

Ton: sachlich, ruhig, präzise. Keine Werbesprüche, keine Qualitätsversprechen,
kein Verkaufsdruck. Referenzen belegen, Behauptungen nicht.
```

---

## Herkunft

Abgeleitet aus dem Agenturbriefing „Websitekonzept Ackermann Gebäudetechnik GmbH & Co. KG", Stand August 2026 (siehe `briefing/`). Farbwerte für Rot und die finale Webfont-Wahl sind ausdrücklich als Platzhalter markiert und vor Livegang aus dem vorhandenen Corporate Design abzuleiten.
