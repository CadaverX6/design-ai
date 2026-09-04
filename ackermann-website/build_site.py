#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die statische Präsentations-Website aus dem Wireframe."""

import os
import re
import unicodedata

SITE = "/home/user/design-ai/ackermann-website/site"
ASSETS = "/home/user/design-ai/ackermann-website/assets"

_MARK = open(f"{SITE}/assets/logo-mark.svg").read()
_MARK = re.sub(r"<!--.*?-->", "", _MARK, flags=re.S)
MARK = _MARK.replace('<svg ', '<svg class="brand-mark" aria-hidden="true" focusable="false" ', 1) \
            .replace(' role="img" aria-label="Ackermann Gebäudetechnik"', '')

BRAND = (f'{MARK}<span class="brand-word"><b>ACKERMANN</b><i>GEBÄUDETECHNIK</i></span>')
LOCKUP = (f'{MARK}<span class="brand-word"><b>ACKERMANN</b><i>GEBÄUDETECHNIK</i>'
          f'<small>GmbH &amp; Co. KG</small><small>Ingenieur- und Meisterbetrieb</small></span>')


def drawing(key):
    """Inline SVG of a construction drawing; falls back to the station until a drawing lands."""
    path = f"{ASSETS}/drawings/{key}.svg"
    if not os.path.exists(path):
        path = f"{ASSETS}/drawings/station.svg"
    return open(path).read()


STATION_SVG = drawing("station")

import sys
sys.path.insert(0, ASSETS)
from icons_fallback import ICONS as FALLBACK_ICONS   # noqa: E402

ICON_DIR = f"{SITE}/assets/icons"


def _normalize_stock_svg(svg):
    """Bring a downloaded stock icon into the site's colour system."""
    svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    svg = re.sub(r"<!DOCTYPE[^>]*>", "", svg)
    head, rest = svg.split(">", 1)
    head = re.sub(r'\s(width|height)="[^"]*"', "", head)
    svg = head + ">" + rest
    svg = re.sub(r'fill="(?!none)[^"]*"', 'fill="currentColor"', svg)
    svg = re.sub(r"fill:\s*(?!none)[^;\"}]+", "fill:currentColor", svg)
    svg = re.sub(r'stroke="(?!none)[^"]*"', 'stroke="currentColor"', svg)
    svg = re.sub(r"stroke:\s*(?!none)[^;\"}]+", "stroke:currentColor", svg)
    return svg.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1).strip()


def icon(slot, size=""):
    """Stock icon from site/assets/icons/<slot>.svg when present, else the fallback."""
    path = f"{ICON_DIR}/{slot}.svg"
    if os.path.exists(path):
        svg, src = _normalize_stock_svg(open(path).read()), "stock"
    else:
        svg, src = FALLBACK_ICONS[slot], "fallback"
    cls = "ico" + (f" {size}" if size else "")
    return f'<span class="{cls}" data-icon="{slot}" data-src="{src}">{svg}</span>'


TRADE_ICON = {"Heizung": "heizung", "Sanitär": "sanitaer", "Lüftung": "lueftung",
              "Kälte": "kaelte", "Stationsbau": "stationsbau"}

DRAWING_TAG = "Konstruktionsdarstellung · Projektfoto folgt"


def fig(key, caption, ratio=None, tag=DRAWING_TAG):
    r = f' data-ratio="{ratio}"' if ratio else ""
    meta = (f'<div class="fig-meta"><span class="cap">{caption}</span>'
            f'<span class="tag">{tag}</span></div>') if (caption or tag) else ""
    return f'<figure><div class="fig"{r}>{drawing(key)}</div>{meta}</figure>'


def drawing_for(p):
    """Which drawing stands in for a project's photograph."""
    special = {
        "amtsgericht-starnberg": "pellet",
        "wohnanlagen-solothurner-strasse-zuericher-strasse-muenchen": "heizraum",
        "parkhauserweiterung-gartencenter-seebauer-muenchen": "kaelte",
        "st-elisabeth-planegg": "kaelte",
        "grammstrasse-8": "sanitaer",
        "wohnhaus-stollbergstrasse-muenchen": "lueftung",
    }
    if p["slug"] in special:
        return special[p["slug"]]
    first = re.sub(r"<[^>]+>", "", p["gewerke"]).split("·")[0].strip()
    return {"Heizung": "heizzentrale", "Sanitär": "sanitaer", "Lüftung": "lueftung",
            "Kälte": "kaelte"}.get(first, "station")

NAV = [
    ("Startseite", "index.html"),
    ("Referenzen", "referenzen.html"),
    ("Stationsbau", "stationsbau.html"),
    ("Arbeiten bei uns", "arbeiten-bei-uns.html"),
    ("Kontakt", "kontakt.html"),
]


def slug(s):
    s = s.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-+", "-", s)[:70]


def doc(title, desc, body, current, depth=0):
    """depth 0 = Wurzel, 1 = Unterordner (referenzen/)."""
    up = "../" * depth
    nav_desktop, nav_mobile = [], []
    for name, href in NAV:
        cur = ' aria-current="page"' if name == current else ""
        nav_desktop.append(f'<a href="{up}{href}"{cur}>{name}</a>')
        nav_mobile.append(f'<a href="{up}{href}"{cur}>{name}</a>')
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" href="{up}assets/fonts.css">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
<div class="sheet">

<header class="site-head">
  <div class="wrap">
    <a class="brand" href="{up}index.html">{BRAND}</a>
    <nav class="site-nav" aria-label="Hauptnavigation">{''.join(nav_desktop)}</nav>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav">Menü</button>
  </div>
</header>

<div class="nav-sheet" id="mobile-nav" hidden>
  <div class="nav-sheet-head">
    <a class="brand" href="{up}index.html">{BRAND}</a>
    <button class="nav-close" type="button">Menü schließen</button>
  </div>
  <nav aria-label="Hauptnavigation, mobil">{''.join(nav_mobile)}</nav>
</div>

<main id="inhalt">
{body}
</main>

</div>
<script src="{up}assets/site.js"></script>
</body>
</html>
"""


def sec(idx, label, h2, body, alt=False, tag="section", anchor=""):
    band = " alt" if alt else ""
    ida = f' id="{anchor}"' if anchor else ""
    return f"""
<{tag} class="sec{band}"{ida}><div class="wrap">
  <div class="sec-head">
    <div class="kicker"><span class="idx">{idx}</span><span class="label">{label}</span></div>
    <h2>{h2}</h2>
  </div>
  <div class="sec-body">{body}</div>
</div></{tag}>"""


def ph(ratio, tag, what):
    return (f'<div class="ph" data-ratio="{ratio}"><div class="ph-in">'
            f'<span class="ph-tag">{tag} · {ratio}</span>'
            f'<span class="ph-txt">{what}</span></div></div>')


def figure(ratio, tag, what, caption):
    return f'<figure>{ph(ratio, tag, what)}<span class="cap">{caption}</span></figure>'


def refcard(idx, kat, titel, gewerke, teaser, motiv, href, key="station"):
    return f"""<a class="refcard" href="{href}">
  <div class="fig" data-ratio="4:3">{drawing(key)}</div>
  <span class="rule"></span>
  <span class="idx">{idx} — {kat}</span>
  <h3>{titel}</h3>
  <p class="gew">{gewerke}</p>
  <p class="teaser">{teaser}</p>
  <span class="link link-plain">Projekt ansehen <span class="arw" aria-hidden="true">&rarr;</span></span>
</a>"""


def process(steps):
    li = "".join(f'<li><span class="p-label">{s}</span><span class="p-idx">{i:02d}</span></li>'
                 for i, s in enumerate(steps, 1))
    return f'<ol class="process">{li}</ol>'


def spec(rows):
    out = "".join(f'<div><dt class="label">{k}</dt><dd>{v}</dd></div>' for k, v in rows)
    return f'<dl class="spec">{out}</dl>'


def kontakt_sf(up=""):
    return f"""
<div class="lockup" style="margin-bottom:32px">{LOCKUP}</div>
<div class="schriftfeld">
  <div class="sf"><span class="label">{icon("standort", "ico-sm")}Unternehmen</span>
    <p class="val">Ackermann Gebäudetechnik<br>GmbH &amp; Co. KG<br>Lechnerstraße 2<br>82067 Ebenhausen</p></div>
  <div class="sf"><span class="label">{icon("telefon", "ico-sm")}Telefon</span>
    <p class="val data"><a href="tel:+4981789982600">08178 9982 600</a></p></div>
  <div class="sf"><span class="label">{icon("email", "ico-sm")}E-Mail</span>
    <p class="val"><a href="mailto:info@ackermann-gebaeudetechnik.de">info@ackermann-<wbr>gebaeudetechnik.de</a></p></div>
  <div class="sf"><span class="label">{icon("service24", "ico-sm")}Service</span>
    <p class="val">24-Stunden-Notdienst für Vertragspartner</p></div>
  <div class="sf sf-full"><span class="label">{icon("unterlagen", "ico-sm")}Unterlagen</span>
    <p class="val">Leistungsverzeichnisse, Pläne und Projektunterlagen können direkt per E-Mail zugesendet werden.</p></div>
</div>
<div class="mobile-actions">
  <a href="tel:+4981789982600">{icon("telefon")}Anrufen</a>
  <a href="mailto:info@ackermann-gebaeudetechnik.de">{icon("email")}E-Mail</a>
</div>
<div class="legal"><a href="{up}impressum.html">Impressum</a><a href="{up}datenschutz.html">Datenschutz</a></div>"""


# =====================================================================
#  PROJEKTDATEN
# =====================================================================
# (Titel, Gewerke, Teaser, Bildmotiv, Ort, Projektart, Einstieg, Technik-Zeilen)
KATEGORIEN = [
    ("Bildung & Betreuung", [
        ("KiTa Martinsried", "Heizung · Sanitär",
         "Heizungs- und Sanitärtechnik für eine Kindertagesstätte.",
         "Technikraum einer Kindertagesstätte.", "Martinsried", "Neubau", None, None),
        ("Kurt-Huber-Gymnasium Gräfelfing, Nordtrakt", "Sanitär · Heizung",
         "Sanitär- und Heizungstechnik im Nordtrakt eines Gymnasiums.",
         "Sanitärinstallation im Schulgebäude.", "Gräfelfing", "Bestand", None, None),
        ("Kinderhaus Nonnenwaldstraße, Penzberg", "Sanitär",
         "Sanitärtechnik für ein Kinderhaus.",
         "Sanitärtechnik im Kinderhaus.", "Penzberg", "Neubau", None, None),
        ("Haus für Kinder Farnweg, München", "Sanitär",
         "Sanitärtechnik für eine Kindertageseinrichtung.",
         "Sanitärinstallation, Rohbau oder fertige Anlage.", "München", "Neubau", None, None),
        ("Kindertagesstätte Schondorf am Ammersee", "Heizung",
         "Heizungstechnik für eine Kindertagesstätte.",
         "Heizzentrale einer Kindertagesstätte.", "Schondorf am Ammersee", "Neubau", None, None),
    ]),
    ("Wohnen", [
        ("Wohnanlagen Solothurner Straße / Züricher Straße, München", "Heizung · Sanitär",
         "Neun Heizzentralen innerhalb einer Sommerpause. Heizungs- und Sanitärarbeiten im bewohnten "
         "Bestand, mit eigenen Fernwärmeübergabestationen und Frischwassermodulen.",
         "Fertige Heizzentrale mit vorgefertigter Station und Frischwassermodul.",
         "München", "Sanierung im bewohnten Bestand",
         "Diese Referenz steht vor allem für Organisation im bewohnten Bestand: neun Heizzentralen "
         "innerhalb einer Sommerpause, Heizungs- und Sanitärarbeiten, enge Versorgungsfenster sowie "
         "eigene Fernwärmeübergabestationen und Frischwassermodule. Im Mittelpunkt stehen nicht nur "
         "technische Einzelkomponenten, sondern die koordinierte Abwicklung mehrerer Zentralen in "
         "engem Zeitrahmen.",
         [("Umfang", "Neun Heizzentralen"),
          ("Zeitrahmen", "Innerhalb einer Sommerpause"),
          ("Gewerke", "Heizung und Sanitär"),
          ("Eigenfertigung", "Fernwärmeübergabestationen und Frischwassermodule aus eigener Fertigung"),
          ("Randbedingung", "Bewohnter Bestand, enge Versorgungsfenster")]),
        ("Neubau Mehrfamilienhaus Auenstraße, Hohenschäftlarn", "Sanitär · Heizung · Lüftung",
         "Sanitär, Heizung und Lüftung im Neubau eines Mehrfamilienhauses.",
         "Verteilung und Hydraulik im Neubau.", "Hohenschäftlarn", "Neubau", None, None),
        ("Loftneubau Franz-Joseph-Straße 14, München", "Sanitär · Heizung · Lüftung",
         "Sanitär, Heizung und Lüftung für einen Loftneubau.",
         "Technische Installation im Loftneubau.", "München", "Neubau", None, None),
        ("Wohnhaus Stollbergstraße, München", "Lüftung",
         "Lüftungstechnik für ein Wohnhaus.",
         "Luftleitungsnetz mit fachgerechter Dämmung.", "München", "Wohnbau", None, None),
        ("Wohnanlage Funkerstraße 4–10, München", "Heizung · Sanitär",
         "Heizungs- und Sanitärtechnik für eine Wohnanlage.",
         "Heizzentrale der Wohnanlage.", "München", "Wohnanlage", None, None),
        ("Wohnanlage Staltacher Straße / Waldfriedhofstraße / Etalstraße, München", "Sanitär",
         "Sanitärtechnik über mehrere Standorte einer Wohnanlage.",
         "Trinkwasserinstallation im Bestand.", "München", "Wohnanlage, mehrere Standorte", None, None),
        ("Wohnhaus Kreuzweg 4a, Gauting", "Sanitär · Heizung · Lüftung",
         "Sanitär, Heizung und Lüftung für ein Wohnhaus.",
         "Technikraum im Einfamilienhaus.", "Gauting", "Wohnbau", None, None),
        ("Grammstraße 8", '<mark class="pl">PLATZHALTER: Gewerke</mark>',
         'Premium-/Luxuswohnungsbau. <mark class="pl">PLATZHALTER: technische Detailbeschreibung nach '
         'Vorlage der endgültigen Projektdaten.</mark>',
         "Sehr saubere, zurückhaltende Installation im Premium-Wohnungsbau.",
         '<mark class="pl">PLATZHALTER</mark>', "Premium-/Luxuswohnungsbau", None, None),
    ]),
    ("Öffentliche Gebäude", [
        ("Rathaus Berg", "Sanitär", "Sanitärtechnik im Rathaus.",
         "Sanitärinstallation im öffentlichen Bestand.", "Berg", "Bestand", None, None),
        ("Agentur für Arbeit Weilheim", "Sanitär · Heizung · Lüftung",
         "Sanitär, Heizung und Lüftung in einem Verwaltungsgebäude.",
         "Technikzentrale im Verwaltungsbau.", "Weilheim", "Verwaltungsgebäude", None, None),
        ("Salesianum München", "Sanitär · Trockene Feuerlöschanlage",
         "Sanitärtechnik und trockene Feuerlöschanlage.",
         "Steigleitung der trockenen Feuerlöschanlage.", "München", "Bestand", None, None),
        ("Amtsgericht Starnberg", "Heizung",
         "Modernisierung der Wärmeversorgung im Bestand mit zwei Pellet-Wärmeerzeugern à 135 kW und "
         "einem vor Ort montierten Pufferspeicher.",
         "Pellet-Doppelkesselanlage und Pufferspeicher im Bestandstechnikraum.",
         "Starnberg", "Modernisierung im Bestand",
         "Die Wärmeversorgung des Amtsgerichts Starnberg wurde im Bestand modernisiert. Eingesetzt "
         "wurden zwei Pellet-Wärmeerzeuger mit je 135 kW, zusammen 270 kW. Ein besonderer Schwerpunkt "
         "lag auf dem rund 8.100 Liter großen Pufferspeicher, der am Standort montiert und geschweißt "
         "wurde, sowie auf der Einbringung in die vorhandenen Technikräume.",
         [("Wärmeerzeuger", "2 × Pellet-Wärmeerzeuger à 135 kW"),
          ("Gesamtleistung", '<span class="data">270 kW</span>'),
          ("Pufferspeicher", '<span class="data">ca. 8.100 Liter</span> — am Standort montiert und geschweißt'),
          ("Weitere Anlagenteile", "Rückbau der Altanlage · Brennstoffversorgung und Fördersystem · "
                                   "Abgasanlage · Druckhaltung und Entgasung · Anbindung Rampenheizung"),
          ("Abschluss", "Inbetriebnahme und technische Dokumentation")]),
        ("Finanzamt Starnberg", "Heizung", "Heizungstechnik in einem Finanzamt.",
         "Heizzentrale im Verwaltungsgebäude.", "Starnberg", "Verwaltungsgebäude", None, None),
        ("Feuerwehrhaus Wolfratshausen", "Heizung", "Heizungstechnik für ein Feuerwehrhaus.",
         "Heizzentrale des Feuerwehrhauses.", "Wolfratshausen", "Öffentliches Gebäude", None, None),
        ("Finanzamt Landsberg am Lech", "Sanitär · Heizung · Lüftung",
         "Sanitär, Heizung und Lüftung in einem Finanzamt.",
         "Lüftungs- und Heizungstechnik im Verwaltungsbau.", "Landsberg am Lech",
         "Verwaltungsgebäude", None, None),
        ("Erinnerungsort Ehrenbürgstraße, München-Neuaubing", "Sanitär",
         "Sanitärtechnik an einem Erinnerungsort.",
         "Sanitärinstallation im denkmalgeschützten Bestand.", "München-Neuaubing", "Bestand", None, None),
        ("Hauptbahnhof Garmisch-Partenkirchen", "Sanitär · Entwässerung",
         "Sanitär- und Entwässerungstechnik im Bahnhofsgebäude.",
         "Entwässerungstechnik im Bahnhofsgebäude.", "Garmisch-Partenkirchen", "Bestand", None, None),
        ("Bahnhofsgebäude Grafrath", "Sanitär · Heizung",
         "Sanitär- und Heizungstechnik im Bahnhofsgebäude.",
         "Technikraum im Bahnhofsgebäude.", "Grafrath", "Bestand", None, None),
    ]),
    ("Gewerbe", [
        ("St. Elisabeth, Planegg", "Heizung",
         "Zwei Grundwasser-Wärmepumpen in Kaskade, ergänzende Gas-Brennwerttechnik und Solarthermie.",
         "Wärmepumpenkaskade mit ergänzender Brennwerttechnik.", "Planegg", "Gewerbe",
         "Die Wärmeversorgung wurde als kombiniertes System ausgeführt: zwei Grundwasser-Wärmepumpen "
         "in Kaskade, ergänzt um Gas-Brennwerttechnik und Solarthermie.",
         [("Wärmeerzeuger", "Zwei Grundwasser-Wärmepumpen in Kaskade"),
          ("Ergänzung", "Gas-Brennwerttechnik"),
          ("Solar", "Solarthermie")]),
        ("Ammerseehotel", "Heizung · Sanitär", "Heizungs- und Sanitärtechnik für ein Hotel.",
         "Heizzentrale des Hotels.", "Ammersee", "Hotel", None, None),
        ("Parkhauserweiterung Gartencenter Seebauer, München", "Sanitär · Heizung · Kälte",
         "Wärmepumpentechnik für Heizen und Kühlen, ergänzt um Sanitär- und Entwässerungstechnik im "
         "laufenden Gewerbebetrieb.",
         "Technikzentrale im Gewerbebau: Wärmepumpen, Verteilung, Entwässerungstechnik.",
         "München", "Gewerbebau, Erweiterung",
         "Im Rahmen der Parkhauserweiterung wurden Sanitär, Heizung und Kälte ausgeführt. Eingesetzt "
         "wurde Wärmepumpentechnik für Heizen und Kühlen, ergänzt um Sanitär- und Entwässerungstechnik.",
         [("Gewerke", "Sanitär, Heizung und Kälte"),
          ("Wärme und Kälte", "Wärmepumpentechnik für Heizen und Kühlen"),
          ("Sanitär", "Sanitär- und Entwässerungstechnik")]),
    ]),
]

# Wo eine belastbare Bildunterschrift aus dem Briefing ableitbar ist, steht sie hier.
# Alle übrigen bleiben sichtbar offen.
CAPTIONS = {
    "amtsgericht-starnberg":
        "Pellet-Doppelkesselanlage, 2 × 135 kW, mit vor Ort montiertem Pufferspeicher.",
    "wohnanlagen-solothurner-strasse-zuericher-strasse-muenchen":
        "Fertige Heizzentrale mit Fernwärmeübergabestation und Frischwassermodul aus eigener Fertigung.",
    "parkhauserweiterung-gartencenter-seebauer-muenchen":
        "Wärmepumpentechnik für Heizen und Kühlen im Gewerbebau.",
    "st-elisabeth-planegg":
        "Zwei Grundwasser-Wärmepumpen in Kaskade mit ergänzender Brennwerttechnik.",
}

PROJEKTE = []
n = 0
for kat, items in KATEGORIEN:
    for p in items:
        n += 1
        PROJEKTE.append({
            "idx": f"{n:02d}", "kat": kat, "titel": p[0], "gewerke": p[1], "teaser": p[2],
            "motiv": p[3], "ort": p[4], "art": p[5], "einstieg": p[6], "technik": p[7],
            "slug": slug(p[0]),
            "caption": CAPTIONS.get(slug(p[0]),
                                    '<mark class="pl">PLATZHALTER: Bildunterschrift</mark>'),
        })

BY_SLUG = {p["slug"]: p for p in PROJEKTE}
HOME_SLUGS = ["wohnanlagen-solothurner-strasse-zuericher-strasse-muenchen",
              "parkhauserweiterung-gartencenter-seebauer-muenchen",
              "grammstrasse-8"]


# =====================================================================
#  STARTSEITE
# =====================================================================
def home_cards():
    cards = []
    for i, s in enumerate(HOME_SLUGS, 1):
        p = BY_SLUG[s]
        cards.append(refcard(f"{i:02d}", p["kat"], p["titel"], p["gewerke"], p["teaser"],
                             p["motiv"], f'referenzen/{p["slug"]}.html', drawing_for(p)))
    return ('<p class="lead" style="margin-bottom:40px">Drei Projekte aus unterschiedlichen Bereichen '
            'des Projektgeschäfts.</p>\n<div class="refgrid">' + "".join(cards) + "</div>")


LEIST_DRAWING = {"Sanitär": "sanitaer", "Heizung": "heizzentrale", "Lüftung": "lueftung",
                 "Kälte": "kaelte", "Stationsbau": "frischwassermodul"}
LEIST_CAPTION = {"Sanitär": "Trinkwasserinstallation mit Frischwassermodul und Steigstrang.",
                 "Heizung": "Heizzentrale: Wärmeerzeuger, Pufferspeicher, Verteiler.",
                 "Lüftung": "Lüftungsgerät mit Wärmerückgewinnung und Kanalnetz.",
                 "Kälte": "Wärmepumpen in Kaskade für Heizen und Kühlen.",
                 "Stationsbau": "Frischwassermodul aus eigener Fertigung."}

LEISTUNGEN = [
    ("Sanitär",
     "Ausführung sanitärtechnischer Anlagen für Neubau und Bestand. Das umfasst Trinkwasserinstallationen, "
     "Entwässerungssysteme, Warmwasserbereitung sowie Sanierungen im laufenden Betrieb. Je nach Anforderung "
     "werden Frischwassermodule, Abscheider- und Hebeanlagen, Wasseraufbereitung und weitere Sonderlösungen "
     "integriert.",
     "Trinkwasserinstallationen · Entwässerung · Warmwasserbereitung · Frischwassersysteme · Abscheider- und "
     "Hebeanlagen · Wasseraufbereitung und Kalkschutz · Sanitäreinrichtungen · Trinkwasserhygiene", None),
    ("Heizung",
     "Ausführung von Heizungsanlagen für Wohnungsbau, Gewerbe und öffentliche Gebäude. Dazu gehören neue "
     "Heizzentralen ebenso wie die Modernisierung bestehender Anlagen. Je nach Projekt kommen Wärmepumpen, "
     "Fernwärme, Pelletanlagen oder andere Wärmeerzeuger zum Einsatz; Wärmeverteilung, Hydraulik, "
     "Druckhaltung, Entgasung und fachgerechte Dämmung werden als Gesamtsystem betrachtet.",
     "Wärmepumpenanlagen · Fernwärmeanlagen · Heizungszentralen · Wärmeverteilung einschließlich fachgerechter "
     "Dämmung · Fußbodenheizung und Heizflächen · Anlagenhydraulik und Speichertechnik · Druckhaltung und "
     "Entgasung · hydraulischer Abgleich · Anlagenoptimierung und Regelungstechnik", None),
    ("Lüftung",
     "Errichtung und Modernisierung von Lüftungsanlagen für Wohngebäude, Gewerbe und öffentliche Einrichtungen. "
     "Entscheidend ist eine sauber einregulierte Anlage mit den richtigen Luftmengen, die zum Gebäude und zur "
     "Nutzung passt.",
     "zentrale und dezentrale Lüftungsanlagen · Wohnraumlüftung · Sanitärraumentlüftung · Zu- und Abluftsysteme · "
     "Luftleitungsnetze einschließlich fachgerechter Dämmung · Wärmerückgewinnung · Schall- und "
     "Brandschutzkomponenten · Einregulierung und Inbetriebnahme", None),
    ("Kälte",
     "Ausführung kältetechnischer Anlagen als Bestandteil der Gebäudetechnik. Je nach Projekt werden Systeme "
     "zur Kühlung von Räumen oder technischen Bereichen umgesetzt und mit Heizungs- und Lüftungsanlagen "
     "abgestimmt.",
     "Raumkühlung · Kühlung technischer Bereiche · Abstimmung mit Heizung und Lüftung", None),
    ("Stationsbau",
     "Eigene Konstruktion und Fertigung von Fernwärmeübergabestationen, Frischwassermodulen sowie "
     "projektbezogenen Solar- und Hydraulikstationen. Dieser Bereich erhält als einziger Leistungsbereich eine "
     "eigene technische Unterseite.",
     "Fernwärmeübergabestationen · Frischwassermodule · Solar- und Hydraulikstationen · Heizkreisverteiler · "
     "Pufferspeicher und Ladegruppen", ("Stationsbau entdecken", "stationsbau.html")),
]


def leistungen_html():
    rows = []
    for titel, text, begriffe, link in LEISTUNGEN:
        extra = ""
        if link:
            extra = (f'<p style="margin-top:16px"><a class="link" href="{link[1]}">{link[0]} '
                     f'<span class="arw" aria-hidden="true">&rarr;</span></a></p>')
        rows.append(f"""<div class="leist-row">
  <h4>{icon(TRADE_ICON[titel], "ico-lg")}{titel}</h4>
  <div><p class="small" style="color:var(--ink-800)">{text}</p>
    <p class="begriffe">{begriffe}</p>{extra}</div>
  {fig(LEIST_DRAWING[titel], LEIST_CAPTION[titel], ratio="4:3", tag="")}
</div>""")
    return f'<div class="leist">{"".join(rows)}</div>'


HOME = f"""
<section class="hero"><div class="wrap">
  <div class="hero-l">
    <span class="label">Ebenhausen · Technische Gebäudeausrüstung</span>
    <h1>Ackermann Gebäudetechnik GmbH &amp; Co. KG</h1>
    <p class="lead">Ausführender Fachbetrieb für Sanitär-, Heizungs-, Lüftungs- und Klimatechnik.
      Technische Gebäudeausrüstung für Wohnungsbau, Gewerbe und öffentliche Auftraggeber.</p>
    <a class="link" href="referenzen.html">Referenzen ansehen <span class="arw" aria-hidden="true">&rarr;</span></a>
  </div>
  <div class="hero-r">
    {STATION_SVG}
    <span class="cap">Fernwärmeübergabestation · Eigene Konstruktion und Fertigung, Ebenhausen.</span>
  </div>
</div></section>
""" + sec("01", "Ausgewählte Referenzen", "Ausgewählte Projekte", home_cards()) \
    + sec("02", "Leistungen", "Was wir ausführen", leistungen_html(), alt=True) \
    + sec("03", "Arbeits- und Projektverständnis", "Wie wir Projekte abwickeln", """
<p class="statement">Technik funktioniert dann am besten, wenn Planung, Organisation und Ausführung von
Anfang an zusammengedacht werden.</p>
<div class="prose" style="margin-top:32px">
  <p>Technische Projekte funktionieren aus unserer Sicht dann am besten, wenn Informationen, Entscheidungen
  und Verantwortlichkeiten früh zusammengeführt werden. Deshalb betrachten wir nicht nur die einzelne
  Montageleistung, sondern den gesamten Ablauf eines Projekts.</p>
  <p>Von der technischen Ausarbeitung über Werk- und Montageplanung, Bauleitung und Ausführung bis zur
  Inbetriebnahme und anschließenden Wartung bleiben die technischen Zusammenhänge in einer Hand.</p>
  <p>Gerade bei Sanierungen im Bestand ist eine saubere Vorbereitung entscheidend. Laufender Gebäudebetrieb,
  kurze Versorgungsunterbrechungen, beengte Einbausituationen und Schnittstellen zu anderen Gewerken müssen
  frühzeitig erkannt und organisiert werden.</p>
  <p>Auch nach Abschluss des Projekts bleiben wir für unsere Vertragspartner Ansprechpartner — mit
  regelmäßiger Wartung und bei Bedarf mit unserem 24-Stunden-Notdienst.</p>
</div>
""" + process(["Technische Ausarbeitung", "Werk- und Montageplanung", "Bauleitung", "Ausführung",
               "Inbetriebnahme", "Wartung / Notdienst"])) \
    + sec("04", "Unternehmensverständnis", "Projektgeschäft ist Teamarbeit", """
<div class="prose">
  <p>Projektgeschäft ist Teamarbeit. Technische Gebäudeausrüstung entsteht dort, wo Erfahrung, Planung,
  Organisation, Bauleitung, Montage und unterschiedliche Fachkompetenzen zuverlässig zusammenspielen.</p>
  <p>Wir verstehen uns als technischer Umsetzungspartner und bringen unsere Erfahrung konstruktiv in die
  Zusammenarbeit mit Planung und Bauherrschaft ein. Wenn wir Verbesserungspotenzial erkennen, sprechen wir
  es offen an und suchen gemeinsam nach einer sinnvollen Lösung.</p>
  <p>Auch mit Fehlern gehen wir transparent um. Entscheidend ist nicht, dass in komplexen Projekten niemals
  etwas schiefläuft, sondern dass Probleme erkannt, Verantwortung übernommen und Lösungen konsequent
  umgesetzt werden. Erkenntnisse sollen in die eigenen Abläufe zurückfließen.</p>
  <p>Unsere Prozesse entwickeln wir kontinuierlich weiter. Ziel ist keine Selbstdarstellung als „perfekt“,
  sondern ein Betrieb, der technisch, organisatorisch und wirtschaftlich jeden Tag ein Stück besser wird.</p>
</div>""", alt=True) \
    + sec("05", "Kontakt", "Kontakt und Unterlagen", kontakt_sf(), tag="footer")


# =====================================================================
#  REFERENZÜBERSICHT
# =====================================================================
def referenzen_page():
    katnav = " ".join(f'<a href="#{slug(k)}">{k}</a>' for k, _ in KATEGORIEN)
    parts = [f"""
<section class="sec" style="padding-bottom:0"><div class="wrap">
  <span class="label">Referenzen</span>
  <h1 style="margin-top:24px">Projekte nach Projektumfeld</h1>
  <p class="lead" style="margin-top:32px">Die Referenzen sind nach Projektumfeld sortiert, nicht nach
  Gewerk — so ist schneller erkennbar, in welchen Gebäudetypen und Projektstrukturen Erfahrung vorhanden
  ist.</p>
  <nav class="katnav" aria-label="Projektumfeld">{katnav}</nav>
</div></section>"""]
    i = 0
    for kat, items in KATEGORIEN:
        i += 1
        cards = []
        for p_ in items:
            p = next(x for x in PROJEKTE if x["titel"] == p_[0])
            cards.append(refcard(p["idx"], p["kat"], p["titel"], p["gewerke"], p["teaser"],
                                 p["motiv"], f'referenzen/{p["slug"]}.html', drawing_for(p)))
        parts.append(sec(f"{i:02d}", kat, kat, f'<div class="refgrid">{"".join(cards)}</div>',
                         alt=(i % 2 == 0), anchor=slug(kat)))
    parts.append(sec("05", "Kontakt", "Kontakt und Unterlagen", kontakt_sf(), tag="footer"))
    return "".join(parts)


# =====================================================================
#  PROJEKTSEITE — ein Muster für alle
# =====================================================================
def projekt_page(p):
    einstieg = p["einstieg"] or (
        f'{p["titel"]} — {p["teaser"]} '
        f'<mark class="pl">PLATZHALTER: Aufgabe, Neubau oder Bestand und die technisch oder '
        f'organisatorisch relevante Besonderheit ergänzen.</mark>')
    if p["technik"]:
        technik = spec(p["technik"])
    else:
        technik = ('<p class="prose"><mark class="pl">PLATZHALTER: Anlagen, Systeme, Leistungsdaten und '
                   'Besonderheiten — nur das, was für dieses Projekt wirklich relevant ist.</mark></p>')

    body = f"""
<section class="pagehead"><div class="wrap">
  <span class="label">{p["kat"]} · {p["art"]}</span>
  <h1>{p["titel"]}</h1>
  <div class="meta">
    <span class="data">{icon(TRADE_ICON.get(re.sub(r"<[^>]+>", "", p["gewerke"]).split("·")[0].strip(), "stationsbau"), "ico-sm")}{p["gewerke"]}</span>
    <span class="data">{icon("standort", "ico-sm")}{p["ort"]}</span>
    <span class="data">{p["art"]}</span>
  </div>
  <div style="margin-top:40px">{fig(drawing_for(p), p["caption"], ratio="16:9")}</div>
</div></section>
""" + sec("01", "Aufgabe", "Aufgabe und Rahmenbedingungen",
          f'<div class="prose"><p>{einstieg}</p></div>') \
        + sec("02", "Technische Umsetzung", "Anlagen und Systeme", technik)

    if p["slug"] == "amtsgericht-starnberg":
        body += sec("03", "Besondere Anforderungen", "Einbringung und laufender Betrieb", """
<p class="statement">Der Pufferspeicher konnte nicht als Ganzes eingebracht werden — er wurde in den
vorhandenen Technikräumen montiert und geschweißt.</p>
<div class="prose" style="margin-top:32px">
  <p>Die vorhandenen Technikräume gaben die Rahmenbedingungen vor: begrenzte Einbringwege, beengte
  Einbausituation und ein Gebäude im laufenden Betrieb. Rückbau, Einbringung und Montage mussten
  entsprechend abschnittsweise organisiert werden.</p>
</div>""")
    elif p["slug"] == "wohnanlagen-solothurner-strasse-zuericher-strasse-muenchen":
        body += sec("03", "Besondere Anforderungen", "Bewohnter Bestand", """
<p class="statement">Neun Heizzentralen innerhalb einer Sommerpause — bei laufendem Gebäudebetrieb und
engen Versorgungsfenstern.</p>
<div class="prose" style="margin-top:32px">
  <p>Die Anlage blieb während der gesamten Maßnahme bewohnt. Kurze Versorgungsunterbrechungen, die
  Reihenfolge der Zentralen und die Einbringung der vorgefertigten Stationen mussten vorab abgestimmt und
  über den gesamten Zeitraum nachgehalten werden.</p>
</div>""")

    projektdaten = f"""
<div class="schriftfeld">
  <div class="sf"><span class="label">Projektart</span><p class="val">{p["art"]}</p></div>
  <div class="sf"><span class="label">Gewerke</span><p class="val">{p["gewerke"]}</p></div>
  <div class="sf"><span class="label">Ort</span><p class="val">{p["ort"]}</p></div>
  <div class="sf"><span class="label">Status</span><p class="val">Abgeschlossen</p></div>
  <div class="sf sf-full"><span class="label">Auftraggeber</span>
    <p class="val"><mark class="pl">PLATZHALTER</mark> — Nennung nur bei belastbarer Freigabe.
    Keine Auftragswerte.</p></div>
</div>"""

    bilder = f"""
{fig(drawing_for(p), p["motiv"], tag="Anlagenschema · Projektfotos folgen nach Freigabe")}
<p class="cap" style="margin-top:24px; max-width:640px">Projektfotos werden nach Auswahl und Freigabe
ergänzt — drei bis sechs starke Bilder, lieber wenige gute als viele durchschnittliche.</p>
<p style="margin-top:40px"><a class="link" href="../referenzen.html">Weitere Referenzen ansehen
<span class="arw" aria-hidden="true">&rarr;</span></a></p>"""

    nxt = "04" if p["slug"] not in ("amtsgericht-starnberg",
                                    "wohnanlagen-solothurner-strasse-zuericher-strasse-muenchen") else "04"
    body += sec(nxt, "Projektdaten", "Projektdaten", projektdaten)
    body += sec(f"{int(nxt)+1:02d}", "Anlage", "Anlage und Bilder", bilder)
    body += sec(f"{int(nxt)+2:02d}", "Kontakt", "Kontakt und Unterlagen", kontakt_sf("../"), tag="footer")
    return body


# =====================================================================
#  STATIONSBAU
# =====================================================================
STATIONSBAU = """
<section class="pagehead"><div class="wrap">
  <span class="label">Stationsbau</span>
  <h1>Eigene Konstruktion und Fertigung</h1>
  <p class="lead">Die Ackermann Gebäudetechnik GmbH &amp; Co. KG entwickelt und fertigt eigene
  Fernwärmeübergabestationen, Frischwassermodule sowie Solar- und Hydraulikstationen. Die Station wird als
  Teil des gesamten Gebäudesystems betrachtet — von den technischen Grundlagen über Auslegung und
  Konstruktion bis zur Fertigung, Montage, Einregulierung und späteren Wartung.</p>
</div></section>
""" + sec("01", "Grundlagen", "Die richtige Auslegung beginnt mit den richtigen Grundlagen", """
<div class="prose">
  <p>Ob eine Anlage später zuverlässig und energieeffizient funktioniert, entscheidet sich bereits bei der
  technischen Auslegung. Grundlage sind belastbare Informationen über die tatsächlichen Anforderungen des
  Gebäudes. Im Bestand können dazu Verbrauchswerte, vorhandene Anlagendaten, Betriebszustände und die
  tatsächliche Nutzung gehören. Im Neubau bilden die ermittelten Leistungs- und Nutzungsanforderungen die
  Grundlage.</p>
  <p>Auch eine hochwertig gefertigte Anlage kann ihre Aufgabe nicht optimal erfüllen, wenn einzelne
  Komponenten aufgrund unzutreffender oder unvollständiger Grundlagen falsch dimensioniert wurden.</p>
</div>""") + sec("02", "Konstruktion", "Konstruktion in 3D", f"""
<div class="prose">
  <p>Die Stationen werden mit branchenspezifischer 3D-CAD-Software konstruiert. Gerade im Bestand gibt der
  vorhandene Heizraum die Rahmenbedingungen vor. Bereits in der Konstruktion werden Einbringwege,
  vorhandene Rohrleitungen, Wand-, Decken- und Bodensituationen, unterschiedliche Aufstellhöhen,
  Platzverhältnisse sowie die notwendige Zugänglichkeit zu allen Komponenten berücksichtigt.</p>
  <p>Ebenso wichtig sind Wartungsfreundlichkeit und die Möglichkeit, die erforderlichen Dämmstandards
  fachgerecht umzusetzen. Konflikte sollen konstruktiv gelöst werden, bevor sie erst auf der Baustelle
  sichtbar werden.</p>
</div>
<div style="margin-top:40px">{fig("heizraum",
  "Konstruktion einer Fernwärmeübergabestation im vorhandenen Heizraum — Einbringweg und Zugänglichkeit sind Teil der Konstruktion.",
  tag="Konstruktionsdarstellung · CAD-Export folgt")}</div>
""", alt=True) + sec("03", "Fertigung", "Eigene Fertigung", f"""
<p class="statement">Die Station wird nicht extern gefertigt und anschließend lediglich angeliefert: Wir
konstruieren sie selbst, fertigen sie bei uns und bauen sie anschließend mit dem eigenen Team vor Ort auf.</p>
<div class="prose" style="margin-top:32px">
  <p>Nach der Konstruktion werden die Stationen im eigenen Betrieb gefertigt. Konstruktion, Fertigung und
  spätere Montage bleiben eng miteinander verbunden. Die Fertigung erfolgt nach definiertem Baumuster mit
  CE-Kennzeichnung, durch entsprechend geprüfte Schweißer und mit der dazugehörigen technischen
  Dokumentation.</p>
</div>
<div style="margin-top:40px">
  <div class="schriftfeld">
    <div class="sf"><span class="label">Baumuster</span><p class="val">Fertigung nach definiertem Baumuster</p></div>
    <div class="sf"><span class="label">Kennzeichnung</span><p class="val">CE-Kennzeichnung</p></div>
    <div class="sf"><span class="label">Ausführung</span><p class="val">Geprüfte Schweißer</p></div>
    <div class="sf"><span class="label">Nachweis</span><p class="val">Technische Dokumentation</p></div>
  </div>
</div>
""" + process(["Konstruktion", "Fertigung", "Qualitätskontrolle", "Dokumentation", "Montage",
               "Einregulierung", "Inbetriebnahme"]) + f"""
<div style="margin-top:56px" class="gallery">
  {fig("fertigung", "Rahmen einer Station in der eigenen Fertigung.", ratio="4:3", tag="Werkstattfoto folgt")}
  {fig("frischwassermodul", "Frischwassermodul aus eigener Fertigung.", ratio="4:3", tag="Produktfoto folgt")}
  {fig("station", "Fernwärmeübergabestation, montagefertig.", ratio="4:3", tag="Baustellenfoto folgt")}
</div>
""") + sec("04", "Sonderlösungen", "Sonderlösungen und hydraulische Baugruppen", """
<div class="prose">
  <p>Neben Fernwärmeübergabestationen und Frischwassermodulen werden projektbezogene Solar- und
  Hydraulikstationen, Heizkreisverteiler, Pufferspeicher und Ladegruppen gefertigt. Entscheidend ist nicht
  das einzelne Bauteil, sondern die Funktion, die die Anlage später im Gebäude zuverlässig erfüllen muss.</p>
</div>""") + sec("05", "Betrieb", "Einregulierung, Inbetriebnahme und Wartung", """
<div class="prose">
  <p>Eine Anlage ist erst dann fertig, wenn sie im Betrieb funktioniert. Bei Einregulierung und
  Inbetriebnahme wird das Zusammenspiel von Hydraulik, Regelung und Komponenten geprüft und auf den
  vorgesehenen Betrieb abgestimmt. Der Anspruch ist eine Anlage, die zuverlässig, energieeffizient und
  wirtschaftlich funktioniert.</p>
  <p>Auch nach der Inbetriebnahme bleibt die technische Betreuung möglich. Regelmäßige Wartung, Fehlersuche
  und Optimierung werden durch die vorhandene Konstruktion und Dokumentation unterstützt. Für
  Vertragspartner steht zusätzlich der 24-Stunden-Notdienst zur Verfügung.</p>
</div>""", alt=True) + sec("06", "Stationsbau in der Praxis", "Gefertigt und geliefert", """
<div class="prose" style="margin-bottom:40px">
  <p>Die Ackermann Gebäudetechnik GmbH &amp; Co. KG fertigt und liefert projektbezogene
  Fernwärmeübergabestationen, Frischwassersysteme und hydraulische Baugruppen für unterschiedliche
  Auftraggeber und Einbausituationen.</p>
</div>
""" + spec([
    ("Neubau Wohnanlage München · ca. 200 WE",
     'Fernwärmeübergabestation <span class="data">650 kW</span>, zwei Frischwassermodule und '
     'Heizkreisverteiler.'),
    ("Wohnanlage München · 155 WE",
     'Fernwärmeübergabestation <span class="data">370 kW</span> und Frischwassersystem.'),
    ("Wohnanlage München · 152 WE",
     'Fernwärmeübergabestation <span class="data">550 kW</span>, Trinkwassererwärmung '
     '<span class="data">350 kW</span>.'),
]) + """
<p class="cap" style="margin-top:24px; max-width:640px">Auf dieser Seite werden ausschließlich reine
Fertigungs- und Lieferreferenzen gezeigt — keine Projekte, bei denen wir gleichzeitig als ausführender
Installateur tätig waren.</p>
""") + sec("07", "Kontakt", "Kontakt und Unterlagen", kontakt_sf(), tag="footer")


# =====================================================================
#  ARBEITEN BEI UNS
# =====================================================================
ROLLEN = ["Anlagenmechaniker SHK (m/w/d)", "Bauleiter (m/w/d)", "Projektleiter (m/w/d)",
          "Konstrukteur (m/w/d)", "Buchhaltung / kaufmännischer Bereich (m/w/d)"]

ARBEITEN = """
<section class="pagehead"><div class="wrap">
  <span class="label">Arbeiten bei uns</span>
  <h1>Projektgeschäft ist Teamarbeit.</h1>
</div></section>
""" + sec("01", "Wer wir suchen", "Wir wachsen", """
<p class="statement">Wir wachsen. Wir suchen Menschen, die Verantwortung übernehmen, lernen und gemeinsam
mit dem Unternehmen wachsen wollen.</p>
<div class="prose" style="margin-top:32px">
  <p>Bei der Ackermann Gebäudetechnik GmbH &amp; Co. KG arbeiten unterschiedliche Menschen gemeinsam an
  anspruchsvollen Projekten der technischen Gebäudeausrüstung. Wir wachsen und entwickeln unsere Abläufe
  laufend weiter. Deshalb suchen wir Menschen, die nicht nur fachlich mitarbeiten, sondern Verantwortung
  übernehmen, lernen und gemeinsam mit dem Unternehmen wachsen wollen.</p>
  <p>Dabei zählt nicht nur fachliches Wissen. Genauso wichtig sind Eigenverantwortung, Verlässlichkeit,
  Organisation und die Bereitschaft, gemeinsam Lösungen zu finden.</p>
  <p>Das Unternehmen befindet sich im Wachstum. Zuständigkeiten und Strukturen entwickeln sich mit. Gesucht
  werden Menschen, die mit Veränderungen umgehen können, Verantwortung übernehmen und bereit sind,
  Strukturen aktiv mitzugestalten.</p>
</div>
<div style="margin-top:48px">{fig("fertigung", "Konstruktion, Fertigung und Montage bleiben im Haus — und in einer Hand.", tag="Werkstattfoto folgt")}</div>
""") + sec("02", "Gesuchte Bereiche", "Gesuchte Bereiche",
                 '<ul class="roles">' + "".join(
                     f'<li><span class="idx">{i:02d}</span><span>{r}</span></li>'
                     for i, r in enumerate(ROLLEN, 1)) + "</ul>", alt=True) \
    + sec("03", "Bewerbung", "Der Weg zu uns", f"""
<div class="prose">
  <p>Der Bewerbungsweg ist bewusst einfach: eine kurze E-Mail mit Angaben zur Person und zum gewünschten
  Bereich. Lebenslauf und Unterlagen können direkt beigefügt werden. Es gibt kein Bewerbungsportal und kein
  Formular.</p>
</div>
<div style="margin-top:40px">
  <div class="schriftfeld">
    <div class="sf sf-full" style="border-top:0"><span class="label">Bewerbung</span>
      <p class="val"><a href="mailto:bewerbung@ackermann-gebaeudetechnik.de">bewerbung@ackermann-gebaeudetechnik.de</a></p>
      <p class="cap" style="margin-top:12px">Hinweis Umsetzung: Die Zustellbarkeit der Umlaut-Schreibweise
      ist vor Veröffentlichung technisch zu prüfen. Bis dahin wird die ASCII-Adresse verwendet.
      <mark class="pl">OFFEN</mark></p>
    </div>
  </div>
</div>
<div class="mobile-actions">
  <a href="tel:+4981789982600">{icon("telefon")}Anrufen</a>
  <a href="mailto:bewerbung@ackermann-gebaeudetechnik.de">{icon("email")}E-Mail</a>
</div>""") + sec("04", "Kontakt", "Kontakt und Unterlagen", kontakt_sf(), tag="footer")


KONTAKT = """
<section class="pagehead"><div class="wrap">
  <span class="label">Kontakt</span>
  <h1>Kontakt</h1>
  <p class="lead">Leistungsverzeichnisse, Pläne und Projektunterlagen können direkt per E-Mail zugesendet
  werden.</p>
</div></section>
""" + sec("01", "Kontaktdaten", "Ackermann Gebäudetechnik GmbH &amp; Co. KG", kontakt_sf(), tag="footer")


def rechtsseite(titel, text):
    return f"""
<section class="pagehead"><div class="wrap">
  <span class="label">Rechtliches</span>
  <h1>{titel}</h1>
</div></section>
""" + sec("01", titel, titel, f"""
<div class="prose"><p>{text}</p></div>
""") + sec("02", "Kontakt", "Kontakt und Unterlagen", kontakt_sf(), tag="footer")


# =====================================================================
#  SCHREIBEN
# =====================================================================
def write(path, html):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(html)


BASE = "Ackermann Gebäudetechnik GmbH & Co. KG"

write("index.html", doc(
    f"{BASE} — Ausführender Fachbetrieb für Sanitär, Heizung, Lüftung und Klimatechnik",
    "Ausführender Fachbetrieb für Sanitär-, Heizungs-, Lüftungs- und Klimatechnik. Technische "
    "Gebäudeausrüstung für Wohnungsbau, Gewerbe und öffentliche Auftraggeber in Ebenhausen.",
    HOME, "Startseite"))

write("referenzen.html", doc(
    f"Referenzen — {BASE}",
    "Ausgeführte Projekte der technischen Gebäudeausrüstung, sortiert nach Projektumfeld: Bildung und "
    "Betreuung, Wohnen, öffentliche Gebäude und Gewerbe.",
    referenzen_page(), "Referenzen"))

write("stationsbau.html", doc(
    f"Stationsbau — {BASE}",
    "Eigene Konstruktion und Fertigung von Fernwärmeübergabestationen, Frischwassermodulen sowie Solar- "
    "und Hydraulikstationen.",
    STATIONSBAU, "Stationsbau"))

write("arbeiten-bei-uns.html", doc(
    f"Arbeiten bei uns — {BASE}",
    "Wir wachsen und suchen Menschen, die Verantwortung übernehmen, lernen und gemeinsam mit dem "
    "Unternehmen wachsen wollen.",
    ARBEITEN, "Arbeiten bei uns"))

write("kontakt.html", doc(
    f"Kontakt — {BASE}",
    "Lechnerstraße 2, 82067 Ebenhausen. Telefon 08178 9982 600. 24-Stunden-Notdienst für Vertragspartner.",
    KONTAKT, "Kontakt"))

write("impressum.html", doc(
    f"Impressum — {BASE}",
    "Impressum der Ackermann Gebäudetechnik GmbH & Co. KG.",
    rechtsseite("Impressum",
                'Die Angaben nach § 5 DDG werden vor Veröffentlichung durch den zuständigen Dienstleister '
                'bzw. juristisch finalisiert. <mark class="pl">PLATZHALTER</mark>'), ""))

write("datenschutz.html", doc(
    f"Datenschutz — {BASE}",
    "Datenschutzerklärung der Ackermann Gebäudetechnik GmbH & Co. KG.",
    rechtsseite("Datenschutz",
                'Die Datenschutzerklärung wird vor Veröffentlichung juristisch finalisiert. Die Website '
                'bindet keine Drittanbieter-Dienste ein: Schriften werden selbst gehostet, es gibt kein '
                'Kontaktformular und kein Tracking. <mark class="pl">PLATZHALTER</mark>'), ""))

for p in PROJEKTE:
    write(f'referenzen/{p["slug"]}.html', doc(
        f'{re.sub(r"<[^>]+>", "", p["titel"])} — Referenz — {BASE}',
        re.sub(r"<[^>]+>", "", p["teaser"])[:180],
        projekt_page(p), "Referenzen", depth=1))

count = sum(len(files) for _, _, files in os.walk(SITE) if files)
print(f'{len(PROJEKTE)} Projektseiten · {count} Dateien insgesamt')
