# Ackermann Gebäudetechnik GmbH & Co. KG — Websitekonzept

Wireframe für die Unternehmenswebsite der Ackermann Gebäudetechnik GmbH & Co. KG,
ausführender Fachbetrieb für Sanitär-, Heizungs-, Lüftungs- und Klimatechnik
(Lechnerstraße 2, 82067 Ebenhausen).

Grundlage ist das Agenturbriefing „Websitekonzept", Stand August 2026, in `briefing/`.
Dies ist ein **Wireframe zur Abstimmung** — noch keine Produktivumsetzung.

## Inhalt

| Pfad | Inhalt |
|---|---|
| `site/` | **Die statische Website.** 33 Seiten, kein Build-Schritt, keine Abhängigkeiten |
| `website-vorschau.html` | Dieselbe Website als eine einzige Datei — zum Weitergeben per Link oder Mail |
| `wireframe.html` | Der vorausgegangene Wireframe samt Konzept- und Token-Anhang |
| `DESIGN.md` | Das Design-System „Werkplan" im Repo-Format (9 Abschnitte) |
| `build_site.py` | Generator für `site/` — Projektdaten stehen als Liste im Kopf der Datei |
| `build_bundle.py` | Packt `site/` in die Einzeldatei-Vorschau |
| `assets/iso.py`, `assets/scenes/`, `assets/drawings/` | Zeichenbibliothek, Szenen und die daraus erzeugten Konstruktionszeichnungen |
| `site/assets/icons/MANIFEST.md` | Ausgewähltes Magnific-Stock-Icon-Set mit Slot-Dateinamen und Download-Weg |
| `assets/icons_fallback.py` | Rückfall-Icons, bis die Stock-Dateien liegen |
| `assets/station-iso.svg` | Isometrische Konstruktionszeichnung der Fernwärmeübergabestation (Hero) |
| `assets/station-iso.py` | Generator für die Zeichnung — Geometrie ist parametrisch, nicht handgezeichnet |
| `briefing/` | Original-Agenturbriefing als PDF und extrahierter Volltext |

## Die Website ansehen

`site/index.html` lässt sich direkt im Browser öffnen — es gibt keinen Build-Schritt und
keine Abhängigkeiten. Zum Hochladen genügt es, den Ordner `site/` auf einen beliebigen
Webspace zu kopieren.

Lokal mit Server (empfohlen, verhält sich wie auf einem echten Host):

```bash
cd site && python3 -m http.server 8000
```

Die Einzeldatei `website-vorschau.html` enthält dieselbe Website inklusive Schriften und
lässt sich ohne Server weitergeben.

### Seitenbestand

| Seite | Datei |
|---|---|
| Startseite | `site/index.html` |
| Referenzübersicht | `site/referenzen.html` |
| 26 Projektseiten | `site/referenzen/*.html` |
| Stationsbau | `site/stationsbau.html` |
| Arbeiten bei uns | `site/arbeiten-bei-uns.html` |
| Kontakt | `site/kontakt.html` |
| Impressum, Datenschutz | `site/impressum.html`, `site/datenschutz.html` |

Alle 26 Projekte haben eine eigene Seite, damit in der Präsentation kein Verweis ins Leere
läuft. Ausformuliert sind die beiden Musterreferenzen aus dem Briefing — Amtsgericht
Starnberg und Solothurner / Züricher Straße. Die übrigen tragen dieselbe Struktur mit
sichtbar markierten Lücken; diese Markierungen sind zugleich die Inhalts-Checkliste.

### Technische Hinweise

- Schriften sind **selbst gehostet** (IBM Plex, Subsets latin + latin-ext, 280 KB).
  Es wird kein Drittanbieter-CDN aufgerufen.
- Kein Kontaktformular, kein Tracking, keine externen Einbindungen.
- Die Seiten tragen `noindex` — sie sollen vor der Freigabe nicht indexiert werden.
  Vor dem Livegang entfernen.
- Geprüft: alle internen Verweise auflösbar, kein Querscroll bei 1440, 390 und 320 px,
  Tastaturbedienung und Fokusringe vorhanden.

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

- **Rotwert** — `#E2001A`, aus der gelieferten Bildmarke abgelesen; gegen die Vektordatei abgleichen
- **Webfont** — IBM Plex ist gesetzt, aber 1:1 austauschbar
- **Alle Bildflächen** — tragen Konstruktionszeichnungen aus `assets/iso.py`, bis echte Projekt-,
  Anlagen-, Werkstatt- und Baustellenfotos vorliegen. Es werden ausdrücklich keine Stockbilder verwendet
- **Grammstraße 8** — endgültige Projektdaten vor Veröffentlichung ergänzen
- **Nennung der Auftraggeber** je Referenzseite prüfen. Keine Auftragswerte
- **Bewerbungs-E-Mail** mit Umlaut-Domain technisch auf Zustellbarkeit prüfen
- **Impressum und Datenschutz** juristisch finalisieren

Die vollständige Liste steht im Wireframe unter „Konzept & Tokens".
