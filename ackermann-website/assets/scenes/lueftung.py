"""Lüftungsgerät mit Wärmerückgewinnung und Kanalnetz."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from iso import Scene
s = Scene("Lüftungsgerät mit Wärmerückgewinnung, Filter, Ventilator und Kanalnetz")

s.box((0, 0, 0), (166, 64, 5), heavy=True)
# Kanäle hinten (Fortluft / Außenluft)
s.duct((10, 14, 62), (150, 14, 62), w=13, h=11, kind="luft")
s.duct((36, 14, 62), (36, 26, 62), w=13, h=11, kind="luft")
s.duct((124, 14, 62), (124, 26, 62), w=13, h=11, kind="luft")
# Gerät: drei gekoppelte Sektionen
s.box((14, 24, 5), (40, 30, 40), plates=6, ribs=4)               # Filtersektion
s.box((54, 24, 5), (46, 30, 40), plates=3, ribs=8)               # Wärmerückgewinnung
s.box((100, 24, 5), (38, 30, 40), plates=5, ribs=4)              # Ventilatorsektion
s.cyl(119, 39, 45, 11, 9, bands=1)                               # Ventilator oben
s.box((142, 26, 5), (14, 26, 30), plates=3)                      # Schalldämpfer
# Kanäle vorn (Zuluft / Abluft)
s.duct((10, 56, 52), (156, 56, 52), w=15, h=12, kind="luft")
s.duct((30, 56, 52), (30, 44, 52), w=15, h=12, kind="luft")
s.duct((119, 56, 52), (119, 44, 52), w=15, h=12, kind="luft")
s.duct((156, 56, 52), (156, 56, 20), w=15, h=12, kind="luft")

s.callout((34, 39, 45), "Filter")
s.callout((77, 39, 45), "Wärmerückgewinnung")
s.callout((119, 39, 54), "Ventilator")
s.callout((149, 39, 35), "Schalldämpfer")
s.footnote((166, 64, 0), "Einregulierung der Luftmengen")
s.write(os.path.join(os.path.dirname(__file__), "..", "drawings", "lueftung.svg"))
print("lueftung")
