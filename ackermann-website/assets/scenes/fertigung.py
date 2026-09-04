"""Stationsrahmen in der eigenen Fertigung."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from iso import Scene
s = Scene("Rahmen einer Station in der eigenen Fertigung, Rohrlager und Schweißplatz")

s.box((0, 0, 0), (170, 72, 3), heavy=True)                       # Hallenboden
# hinten: Rohrlager
s.box((8, 6, 3), (86, 14, 26))
for i, z in enumerate((31, 39)):
    s.hcyl((12, 13, z), 78, 3.4, axis="x", bands=4)
s.box((112, 6, 3), (44, 16, 34), plates=5)                       # Werkzeugschrank
# Mitte: Rahmen auf Böcken
s.box((22, 34, 3), (12, 12, 16))                                 # Bock links
s.box((116, 34, 3), (12, 12, 16))                                # Bock rechts
s.box((16, 30, 19), (124, 22, 5), heavy=True)                    # Rahmen
s.box((26, 32, 24), (18, 18, 34), plates=9, ribs=4)              # montierter Übertrager
s.cyl(70, 41, 24, 7, 14)                                         # Pumpe, lose gestellt
s.box((64.5, 35.5, 38), (11, 11, 12))
s.run([(34, 41, 58), (86, 41, 58), (86, 41, 44)], kind="vl")     # angeheftete Probeleitung
s.box((98, 32, 24), (16, 16, 6))                                 # Flanschsatz
# vorn: Schweißplatz
s.box((104, 56, 3), (54, 14, 22), heavy=True)
s.box((118, 58, 25), (14, 10, 9))                                # Schraubstock
s.cyl(148, 63, 25, 6, 16, bands=2)                               # Schutzgasflasche

s.callout((78, 41, 24), "Rahmen")
s.callout((50, 13, 43), "Rohrlager")
s.callout((35, 41, 58), "Wärmeübertrager")
s.callout((131, 63, 34), "Schweißplatz")
s.footnote((170, 72, 0), "Fertigung nach Baumuster")
s.write(os.path.join(os.path.dirname(__file__), "..", "drawings", "fertigung.svg"))
print("fertigung")
