# Icon-Set — Magnific Stock (Freepik/Flaticon)

Die Website nutzt zehn Icons als **sekundäre Marker** — vor Leistungstiteln, in den
Schriftfeld-Zellen, an den mobilen Bedienelementen und in der Projektkopfzeile. Nie als
Hauptgestaltungselement (Briefing §9).

Der Build nimmt für jeden Slot automatisch die Datei `site/assets/icons/<slot>.svg`, sobald
sie hier liegt, und normalisiert sie (Füllungen → `currentColor`, feste Maße entfernt). Fehlt
die Datei, steht ein Rückfall-Icon in der Strichsprache der Zeichnungen an ihrer Stelle
(`assets/icons_fallback.py`). Nach dem Ablegen genügt `python3 build_site.py`.

## Ausgewählte Icons

Die Auswahl hält je Gruppe **einen Autor**, damit die Strichstärke und Ecken zusammenpassen.
Zwei Slots konnten nicht aus demselben Set besetzt werden und sind markiert — dort beim
Download prüfen, ob der Stil zum Set passt, sonst eine Alternative aus dem Set des Autors wählen.

| Slot (Dateiname) | Verwendung | Stock-ID | Titel | Autor | Hinweis |
|---|---|---|---|---|---|
| `heizung.svg` | Leistung Heizung, Projektkopf | 18950669 | Electric furnace | Malik Grafix | Set A |
| `sanitaer.svg` | Leistung Sanitär, Projektkopf | 18950595 | Tankless water heater | Malik Grafix | Set A |
| `kaelte.svg` | Leistung Kälte, Projektkopf | 18950738 | Ac outside unit | Malik Grafix | Set A |
| `lueftung.svg` | Leistung Lüftung, Projektkopf | 17372390 | Ventilation | HAJICON | **anderes Set — Stil prüfen** |
| `stationsbau.svg` | Leistung Stationsbau | 13833597 | Station | pikepicture | **anderes Set — Stil prüfen** |
| `telefon.svg` | Schriftfeld Telefon, „Anrufen“ | 15810489 | Phone | Minh Do | Set B |
| `email.svg` | Schriftfeld E-Mail, „E-Mail“ | 15810566 | Email | Minh Do | Set B |
| `service24.svg` | Schriftfeld Service (Notdienst) | 15810412 | Customer service | Minh Do | Set B |
| `unterlagen.svg` | Schriftfeld Unterlagen | 15810484 | Sheet | Minh Do | Set B |
| `standort.svg` | Schriftfeld Unternehmen, Projektkopf Ort | 15810499 | Location | Minh Do | Set B |

Set A = Malik Grafix (HVAC-Set), Set B = Minh Do (Interface-Set).
Alle Einträge sind Premium-Icons; sie sind über das bestehende Magnific/Freepik-Konto lizenziert.

## Warum die Dateien hier noch fehlen

Die Icons wurden über die Magnific-Stock-Suche ausgewählt, aber aus der Build-Umgebung dieses
Projekts lässt sich der Download-Host (`cdn-icons.flaticon.com`) nicht erreichen — die
Netzwerkrichtlinie lässt nur wenige Hosts zu. Deshalb ist der Download der letzte Handgriff,
der lokal passiert:

1. In Magnific (oder direkt auf Flaticon) das Icon über die Stock-ID öffnen —
   z. B. `https://www.flaticon.com/search?word=<Titel>` und die ID vergleichen, oder in
   Magnific die Stock-Suche mit demselben Titel.
2. Als **SVG** herunterladen.
3. Unter dem Slot-Dateinamen aus der Tabelle in diesen Ordner legen.
4. `python3 build_site.py` ausführen — der Build meldet je Slot `stock` oder `fallback`
   (im HTML als `data-src` am Icon sichtbar).

Icons ohne passende Datei bleiben auf dem Rückfall; die Seite ist in jedem Zustand vollständig.

## Gestaltungsregel

Icons sind 20 px (Titel 28 px, Schriftfeld 16 px), einfarbig in `--ink-900` bzw. `--ink-500`,
nie rot, nie gefüllt hinterlegt, nie in der Prozesskette und nie in der Navigation.
