#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Heizzentrale eines Wohn- oder Verwaltungsgebäudes — Wärmeerzeuger, Puffer,
Verteiler und Pumpengruppe im Bestandsraum."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from iso import Scene

s = Scene("Isometrische Konstruktionszeichnung einer Heizzentrale: zwei "
          "Wärmeerzeuger, Pufferspeicher, Ausdehnungsgefäß, Verteiler mit "
          "Pumpengruppe und Schaltschrank im Heizraum.")

# Bestandsraum: Boden und zwei Rückwände
s.room(180, 88, 52)

# hintere Reihe: Schaltschrank, Ausdehnungsgefäß, zwei Wärmeerzeuger
s.box((152, 3, 0), (18, 10, 48), plates=3)                  # Schaltschrank
s.cyl(16, 30, 0, 8, 26, bands=2)                            # Ausdehnungsgefäß
s.box((34, 8, 0), (28, 26, 42), plates=2)                   # Wärmeerzeuger 1
s.box((72, 8, 0), (28, 26, 42), plates=2)                   # Wärmeerzeuger 2

# Kesselvorlauf: Steigleitungen und Sammelleitung zum Puffer (oben)
s.pipe((82, 22, 42), (82, 22, 56), kind="vl")
s.run([(44, 22, 42), (44, 22, 56), (111, 22, 56)], kind="vl")

# Kesselrücklauf: vom Puffer (unten) zu den Kesseln, Ausdehnungsgefäß am Rücklauf
s.pipe((54, 30, 42), (54, 30, 48), kind="rl")
s.pipe((92, 30, 42), (92, 30, 48), kind="rl")
s.run([(16, 30, 26), (16, 30, 48), (105, 30, 48), (105, 30, 8), (111, 30, 8)], kind="rl")
s.valve(67, 30, 48)

# Pufferspeicher
s.cyl(124, 26, 0, 14, 64, bands=4)
s.valve(96, 22, 56)

# vordere Reihe: Rücklaufsammler, Pumpengruppe, Vorlaufverteiler
s.pipe((0, 70, 10), (14, 70, 10), kind="rl")                # Heizkreise ins Gebäude
s.pipe((0, 70, 46), (14, 70, 46), kind="vl")
s.hcyl((14, 70, 10), 96, 4.5, axis="x")                     # Sammler
for px in (36, 58, 80):
    s.pump(px, 70, 14.5, r=5.5, h=12, motor=10)
    s.pipe((px, 70, 36.5), (px, 70, 41.5), kind="vl")
s.hcyl((14, 70, 46), 96, 4.5, axis="x")                     # Verteiler

# Anbindung Puffer — Verteiler
s.run([(124, 40, 46), (124, 70, 46), (110, 70, 46)], kind="vl")
s.valve(124, 56, 46)
s.run([(124, 40, 10), (124, 70, 10), (110, 70, 10)], kind="rl")
s.valve(124, 58, 10)

s.callout((48, 21, 42), "Wärmeerzeuger")
s.callout((124, 26, 64), "Pufferspeicher")
s.callout((58, 70, 36.5), "Pumpengruppe")
s.callout((100, 70, 50.5), "Verteiler")
s.footnote((180, 88, 0), "Hydraulik als Gesamtsystem")

out = os.path.join(os.path.dirname(__file__), "..", "drawings", "heizzentrale.svg")
svg = s.write(out)
print("heizzentrale.svg", len(svg), "bytes")
