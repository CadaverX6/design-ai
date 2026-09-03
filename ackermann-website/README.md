# Ackermann Gebäudetechnik GmbH & Co. KG — Websitekonzept

Wireframe für die Unternehmenswebsite der Ackermann Gebäudetechnik GmbH & Co. KG,
ausführender Fachbetrieb für Sanitär-, Heizungs-, Lüftungs- und Klimatechnik
(Lechnerstraße 2, 82067 Ebenhausen).

Grundlage ist das Agenturbriefing „Websitekonzept", Stand August 2026, in `briefing/`.
Dies ist ein **Wireframe zur Abstimmung** — noch keine Produktivumsetzung.

## Inhalt

| Pfad | Inhalt |
|---|---|
| `wireframe.html` | Der Wireframe. Sechs Seiten, Desktop-/Mobil-Umschalter, Konzept- und Token-Anhang |
| `DESIGN.md` | Das Design-System „Werkplan" im Repo-Format (9 Abschnitte) |
| `assets/station-iso.svg` | Isometrische Konstruktionszeichnung der Fernwärmeübergabestation (Hero) |
| `assets/station-iso.py` | Generator für die Zeichnung — Geometrie ist parametrisch, nicht handgezeichnet |
| `briefing/` | Original-Agenturbriefing als PDF und extrahierter Volltext |

## Konzept — „Werkplan"

Die Website übernimmt die visuelle Grammatik, in der die Zielgruppe ohnehin arbeitet:
Werkpläne, Anlagenschemata, Leistungsverzeichnisse mit Positionsnummern, Schriftfelder.
Weiß dominiert, Schwarz trägt Typografie und Linien, Rot ist der eine farbige Stift —
maximal ein rotes Element pro Ansicht im Inhalt.

Wiederkehrendes Element ist das **Schriftfeld** nach DIN-Vorbild: es dient als Footer und
Kontaktblock, als Projektdaten-Block jeder Referenzseite und als Fertigungsnachweis im
Stationsbau. Es fügt weder Farbe noch Form hinzu — nur Haarlinien und Beschriftungen.

## Seiten

Startseite · Referenzen · Referenz-Detailseite (Muster: Amtsgericht Starnberg) ·
Stationsbau · Arbeiten bei uns · Kontakt

Die Navigation bleibt bewusst schlank. Sanitär, Heizung, Lüftung und Kälte werden auf der
Startseite erklärt; nur der Stationsbau erhält wegen seiner technischen Tiefe eine eigene Seite.

## Ansehen

`wireframe.html` ist eigenständig und lässt sich direkt im Browser öffnen. Die Webfonts
werden zur Vorschau vom Google-CDN geladen — **für die Produktion sind sie selbst zu hosten**
(Datenschutz).

## Platzhalter

Bewusst offen gelassen und im Wireframe als `PLATZHALTER` markiert:

- **Rotwert** — aus dem vorhandenen Logo ableiten. Stellvertreter ist RAL 3020 Verkehrsrot
- **Webfont** — IBM Plex ist gesetzt, aber 1:1 austauschbar
- **Alle Bildflächen** — stehen für echte Projekt-, Anlagen-, Werkstatt- und Baustellenfotos.
  Es werden ausdrücklich keine Stockbilder verwendet
- **Grammstraße 8** — endgültige Projektdaten vor Veröffentlichung ergänzen
- **Nennung der Auftraggeber** je Referenzseite prüfen. Keine Auftragswerte
- **Bewerbungs-E-Mail** mit Umlaut-Domain technisch auf Zustellbarkeit prüfen
- **Impressum und Datenschutz** juristisch finalisieren

Die vollständige Liste steht im Wireframe unter „Konzept & Tokens".
