"""Pellet-Doppelkesselanlage mit vor Ort geschweißtem Pufferspeicher."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from iso import Scene
s = Scene("Zwei Pelletkessel mit Fördersystem, Abgasanlage und großem Pufferspeicher")

s.box((0, 0, 0), (176, 70, 5), heavy=True)
# Fördersystem und Abgas hinten
s.duct((6, 12, 66), (96, 12, 66), w=11, h=9)
s.duct((40, 12, 66), (40, 26, 66), w=11, h=9)
s.duct((86, 12, 66), (86, 26, 66), w=11, h=9)
s.cyl(150, 14, 5, 7, 96, bands=6)                                # Abgasanlage
s.box((150, 6, 5), (0.1, 0.1, 0.1))
# Kessel
for x in (16, 62):
    s.box((x, 26, 5), (34, 32, 46), plates=4, ribs=3)
    s.cyl(x + 17, 42, 51, 10, 8, bands=1)
    s.run([(x + 17, 42, 59), (x + 17, 14, 59), (x + 17, 14, 66)], kind="n")
    s.run([(x + 26, 58, 40), (x + 26, 64, 40)], kind="vl")
# Pufferspeicher — das größte Bauteil, vor Ort geschweißt
s.cyl(126, 40, 5, 22, 84, bands=5)
s.box((118, 32, 89), (16, 16, 5))
s.run([(126, 40, 94), (126, 64, 94), (126, 64, 74)], kind="vl")
# Verteiler vorn
s.run([(6, 64, 40), (166, 64, 40)], kind="vl")
s.run([(6, 64, 14), (166, 64, 14)], kind="rl")
s.run([(126, 64, 74), (126, 64, 40)], kind="vl")
for px in (46, 90):
    s.cyl(px, 64, 14, 6.4, 14)
    s.box((px - 5.2, 58.8, 28), (10.4, 10.4, 12))
    s.run([(px, 64, 40), (px, 64, 34)], kind="vl")
s.valve(24, 64, 14)
s.valve(150, 64, 40)

s.callout((33, 42, 59), "Pelletkessel 2 × 135 kW")
s.callout((126, 40, 92), "Pufferspeicher 8.100 l")
s.callout((50, 12, 71), "Fördersystem")
s.callout((150, 14, 99), "Abgasanlage")
s.footnote((176, 70, 0), "Einbringung im Bestand")
s.write(os.path.join(os.path.dirname(__file__), "..", "drawings", "pellet.svg"))
print("pellet")
