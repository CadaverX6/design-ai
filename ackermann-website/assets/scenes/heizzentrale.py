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
s.room(200, 84, 52, door=(136, 24, 44))

# hintere Reihe: Schaltschrank, Ausdehnungsgefäß, zwei Wärmeerzeuger
s.box((178, 3, 0), (18, 10, 48), plates=3)                  # Schaltschrank
s.box((34, 8, 0), (28, 26, 42), plates=2)                   # Wärmeerzeuger 1
s.box((72, 8, 0), (28, 26, 42), plates=2)                   # Wärmeerzeuger 2

# Kesselvorlauf: Steigleitungen und Sammelleitung zum Puffer (oben)
s.pipe((82, 22, 42), (82, 22, 56), kind="vl")
s.run([(44, 22, 42), (44, 22, 56), (113, 22, 56)], kind="vl")

# Kesselrücklauf: vom Puffer (unten) zu den Kesseln
s.pipe((92, 30, 42), (92, 30, 48), kind="rl")
s.run([(54, 30, 42), (54, 30, 48), (101, 30, 48), (101, 30, 8), (113, 30, 8)], kind="rl")
s.valve(67, 30, 48)

# Pufferspeicher
s.cyl(126, 26, 0, 14, 64, bands=4)
s.valve(96, 22, 56)

# vordere Reihe: Ausdehnungsgefäß, Rücklaufsammler, Pumpengruppe, Vorlaufverteiler
s.cyl(10, 44, 0, 7, 24, bands=2)                            # Ausdehnungsgefäß
s.run([(10, 51, 10), (10, 70, 10), (40, 70, 10)], kind="rl") # Anschluss MAG an Sammler
s.valve(22, 70, 10)                                         # Kappenventil
s.hcyl((40, 70, 10), 70, 4.5, axis="x")                     # Sammler
for px in (56, 76, 96):
    s.pump(px, 70, 14.5, r=5.5, h=12, motor=10)
    s.pipe((px, 70, 36.5), (px, 70, 41.5), kind="vl")
s.hcyl((40, 70, 46), 70, 4.5, axis="x")                     # Verteiler

# Anbindung Puffer — Verteiler
s.run([(126, 40, 46), (126, 70, 46), (110, 70, 46)], kind="vl")
s.valve(126, 56, 46)
s.run([(126, 40, 10), (126, 70, 10), (110, 70, 10)], kind="rl")
s.valve(126, 58, 10)

s.callout((86, 18, 42), "Wärmeerzeuger")
s.callout((126, 26, 64), "Pufferspeicher")
s.callout((76, 70, 36.5), "Pumpengruppe")
s.callout((104, 70, 50.5), "Verteiler")
s.footnote((200, 84, 0), "Hydraulik als Gesamtsystem")

out = os.path.join(os.path.dirname(__file__), "..", "drawings", "heizzentrale.svg")
svg = s.write(out)
print("heizzentrale.svg", len(svg), "bytes")
