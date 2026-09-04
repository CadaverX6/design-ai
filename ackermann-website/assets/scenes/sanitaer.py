"""Trinkwasserinstallation: Frischwassermodul, Speicher, Steigstrang."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from iso import Scene
s = Scene("Trinkwasserinstallation mit Frischwassermodul, Speicher und Steigstrang")

s.box((0, 0, 0), (150, 66, 5), heavy=True)                       # Bodenplatte
# hintere Reihe
s.run([(6, 12, 58), (128, 12, 58)], kind="kw")                   # Kaltwasser-Zulauf
s.run([(30, 12, 58), (30, 30, 58), (30, 30, 46)], kind="kw")
s.valve(70, 12, 58)
s.box((128, 6, 5), (14, 10, 40), plates=3)                       # Schaltschrank
# mittlere Reihe
s.box((18, 26, 5), (20, 24, 42), plates=10, ribs=5)              # Frischwassermodul
s.cyl(108, 34, 5, 18, 62, bands=4)                               # Speicher
s.box((102, 28, 67), (12, 12, 4))
s.cyl(60, 34, 5, 9, 30, bands=2)                                 # Enthärtung / Filter
# vordere Reihe
s.run([(6, 58, 14), (140, 58, 14)], kind="kw")                   # Zirkulation
s.run([(6, 58, 46), (140, 58, 46)], kind="ww")                   # Warmwasser-Verteiler
s.run([(140, 58, 46), (140, 58, 84)], kind="ww")                 # Steigstrang
s.run([(140, 58, 84), (118, 58, 84)], kind="ww")
for px in (44, 78):
    s.cyl(px, 58, 14, 6.0, 13)
    s.box((px - 4.8, 53.2, 27), (9.6, 9.6, 12))
    s.run([(px, 58, 39), (px, 58, 46)], kind="ww")
s.valve(24, 58, 14)
s.valve(100, 58, 46)

s.callout((28, 38, 47), "Frischwassermodul")
s.callout((60, 34, 35), "Wasseraufbereitung")
s.callout((108, 34, 71), "Speicher")
s.callout((140, 58, 84), "Steigstrang")
s.footnote((150, 66, 0), "Trinkwasserhygiene")
s.write(os.path.join(os.path.dirname(__file__), "..", "drawings", "sanitaer.svg"))
print("sanitaer")
