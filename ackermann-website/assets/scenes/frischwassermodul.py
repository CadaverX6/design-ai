"""Frischwassermodul — Detailansicht der Baugruppe."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from iso import Scene
s = Scene("Frischwassermodul: Plattenwärmeübertrager, Pumpen, Armaturen und Regelung")

# Wandrahmen
s.box((0, 6, 0), (8, 8, 118), heavy=True)
s.box((126, 6, 0), (8, 8, 118), heavy=True)
s.box((0, 6, 0), (134, 8, 8), heavy=True)
s.box((0, 6, 110), (134, 8, 8), heavy=True)
# Heizungsseite hinten
s.run([(10, 10, 92), (124, 10, 92)], kind="vl")
s.run([(10, 10, 26), (124, 10, 26)], kind="rl")
s.valve(100, 10, 92)
s.valve(100, 10, 26)
s.box((96, 8, 40), (30, 10, 40), plates=4)                       # Regelung
# Wärmeübertrager, Mitte
s.box((34, 22, 40), (32, 34, 52), plates=12, ribs=6)
s.run([(50, 22, 96), (50, 10, 96), (50, 10, 92)], kind="vl")
s.run([(50, 56, 34), (50, 56, 26), (50, 10, 26)], kind="rl")
# Trinkwasserseite vorn
s.run([(10, 62, 20), (124, 62, 20)], kind="kw")
s.run([(10, 62, 100), (124, 62, 100)], kind="ww")
for px in (24, 84):
    s.cyl(px, 62, 20, 8, 20)
    s.box((px - 6.5, 55.5, 40), (13, 13, 15))
    s.run([(px, 62, 55), (px, 62, 68)], kind="kw")
s.valve(108, 62, 20)
s.valve(108, 62, 100)
s.box((60, 58, 62), (22, 12, 16), plates=3)                      # Sensorik

s.callout((50, 39, 92), "Plattenwärmeübertrager")
s.callout((24, 62, 55), "Zirkulationspumpe")
s.callout((111, 13, 80), "Regelung")
s.footnote((134, 70, 0), "CE-gekennzeichnetes Baumuster")
s.write(os.path.join(os.path.dirname(__file__), "..", "drawings", "frischwassermodul.svg"))
print("frischwassermodul")
