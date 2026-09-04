"""Wärmepumpen in Kaskade für Heizen und Kühlen."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from iso import Scene
s = Scene("Zwei Wärmepumpen in Kaskade mit Pufferspeicher und Hydraulik")

s.box((0, 0, 0), (158, 66, 5), heavy=True)
s.run([(6, 12, 60), (140, 12, 60)], kind="vl")                   # Vorlauf-Sammler
s.valve(96, 12, 60)
s.box((140, 6, 5), (14, 11, 44), plates=3)                       # Regelung
# Wärmepumpen in Kaskade
for i, x in enumerate((14, 60)):
    s.box((x, 26, 5), (36, 26, 44), plates=4, ribs=9)
    s.cyl(x + 18, 39, 49, 12, 8, bands=1)
    s.run([(x + 18, 39, 57), (x + 18, 12, 57), (x + 18, 12, 60)], kind="vl")
    s.run([(x + 8, 52, 5), (x + 8, 60, 5), (x + 8, 60, 16)], kind="rl")
s.cyl(120, 36, 5, 17, 56, bands=4)                               # Pufferspeicher
s.box((114, 30, 61), (12, 12, 4))
# vordere Reihe: Rücklauf, Pumpen, Kaltwasserabgang
s.run([(6, 60, 16), (146, 60, 16)], kind="rl")
for px in (44, 82):
    s.cyl(px, 60, 16, 6.2, 13)
    s.box((px - 5, 55, 29), (10, 10, 12))
    s.run([(px, 60, 41), (px, 60, 48)], kind="vl")
s.run([(6, 60, 48), (146, 60, 48)], kind="vl")
s.run([(146, 60, 48), (146, 60, 30)], kind="kw")                 # Kühlkreis
s.valve(30, 60, 16)
s.valve(108, 60, 48)

s.callout((32, 39, 57), "Wärmepumpe")
s.callout((78, 39, 57), "Kaskade")
s.callout((120, 36, 65), "Pufferspeicher")
s.callout((63, 60, 41), "Hydraulik")
s.footnote((158, 66, 0), "Heizen und Kühlen")
s.write(os.path.join(os.path.dirname(__file__), "..", "drawings", "kaelte.svg"))
print("kaelte")
