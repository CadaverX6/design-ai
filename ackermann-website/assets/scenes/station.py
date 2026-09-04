#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fernwärmeübergabestation auf gefertigtem Rahmen — Hero der Startseite."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from iso import Scene

s = Scene("Isometrische Konstruktionszeichnung einer Fernwärmeübergabestation: "
          "Wärmeübertrager, Umwälzpumpen, Pufferspeicher und Regelung auf einem "
          "im eigenen Betrieb gefertigten Rahmen.")

# Rahmen
s.box((0, 0, 0), (160, 70, 5), heavy=True)

# hintere Reihe: Primärvorlauf, Abgänge, Regelung
s.pipe((4, 10, 62), (152, 10, 62), kind="vl")
s.run([(22, 10, 62), (22, 30, 62), (22, 30, 50)], kind="vl")
s.run([(48, 10, 62), (48, 32, 62), (48, 32, 40)], kind="vl")
s.valve(88, 10, 62)
s.box((132, 4, 5), (16, 10, 42), plates=4)

# mittlere Reihe: Wärmeübertrager, Speicher
s.box((14, 28, 5), (18, 22, 46), plates=9, ribs=5)
s.box((40, 30, 5), (16, 20, 36), plates=8, ribs=4)
s.cyl(120, 37, 5, 17, 60, bands=4)
s.box((114, 31, 65), (12, 12, 4))

# vordere Reihe: Rücklaufsammler, Pumpengruppe, Sekundärverteiler
s.pipe((4, 60, 12), (146, 60, 12), kind="rl")
for px in (66, 88):
    s.cyl(px, 60, 12, 6.6, 15)
    s.box((px - 5.2, 54.8, 27), (10.4, 10.4, 13))
    s.pipe((px, 60, 40), (px, 60, 50), kind="vl")
s.valve(30, 60, 12)
s.valve(112, 60, 12)
s.pipe((4, 60, 50), (146, 60, 50), kind="vl")
s.valve(104, 60, 50)

s.callout((23, 37, 51), "Wärmeübertrager")
s.callout((88, 60, 40), "Umwälzpumpen")
s.callout((120, 37, 69), "Pufferspeicher")
s.callout((140, 9, 47), "Regelung")
s.footnote((160, 70, 0), "Rahmen — eigene Fertigung")

out = os.path.join(os.path.dirname(__file__), "..", "drawings", "station.svg")
svg = s.write(out)
print("station.svg", len(svg), "bytes")
