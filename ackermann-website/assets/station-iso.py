#!/usr/bin/env python3
"""
Isometric construction drawing of a Fernwaermeuebergabestation.

Solids are filled with the page ground and painted back-to-front, so the
assembly occludes itself the way a real CAD view does instead of reading
as an x-ray. Strokes inherit currentColor, so the drawing works in both themes.
"""
import math

C30, S30 = math.cos(math.radians(30)), math.sin(math.radians(30))
RT2 = math.sqrt(2)


def prj(x, y, z):
    return ((x - y) * C30, (x + y) * S30 - z)


def fmt(pts):
    return "M" + " L".join(f"{a:.2f},{b:.2f}" for a, b in pts) + " Z"


class Part:
    """One solid: a silhouette to knock out the background, plus its edges."""

    def __init__(self):
        self.sil = []      # path strings, filled with the ground colour
        self.edge = []     # (class, path)


PARTS = []               # painted in insertion order: back to front


def box(o, s, plates=0, ribs=0, heavy=False):
    x, y, z = o
    w, d, h = s
    x1, y1, z1 = x + w, y + d, z + h
    p = Part()
    p.sil.append(fmt([prj(x, y1, z1), prj(x, y, z1), prj(x1, y, z1),
                      prj(x1, y, z), prj(x1, y1, z), prj(x, y1, z)]))
    cls = "heavy" if heavy else "ln"
    p.edge.append((cls, fmt([prj(x, y, z1), prj(x1, y, z1),
                             prj(x1, y1, z1), prj(x, y1, z1)])))
    p.edge.append((cls, "M" + " L".join(
        f"{a:.2f},{b:.2f}" for a, b in
        [prj(x, y1, z), prj(x1, y1, z), prj(x1, y, z)])))
    for cx, cy in ((x1, y1), (x, y1), (x1, y)):
        p.edge.append((cls, "M{:.2f},{:.2f} L{:.2f},{:.2f}".format(
            *prj(cx, cy, z), *prj(cx, cy, z1))))
    for i in range(1, plates):                       # plate pack, near side
        t = x + w * i / plates
        p.edge.append(("hair", "M{:.2f},{:.2f} L{:.2f},{:.2f}".format(
            *prj(t, y1, z), *prj(t, y1, z1))))
    for i in range(1, ribs):                          # ribs on the right face
        t = y + d * i / ribs
        p.edge.append(("hair", "M{:.2f},{:.2f} L{:.2f},{:.2f}".format(
            *prj(x1, t, z), *prj(x1, t, z1))))
    PARTS.append(p)
    return p


def cyl(cx, cy, z0, r, h, bands=0):
    rx, ry = r * C30 * RT2, r * S30 * RT2
    sx, top = prj(cx, cy, z0 + h)
    _, bot = prj(cx, cy, z0)
    p = Part()
    p.sil.append(
        f"M{sx - rx:.2f},{top:.2f} A{rx:.2f},{ry:.2f} 0 0,1 {sx + rx:.2f},{top:.2f} "
        f"L{sx + rx:.2f},{bot:.2f} A{rx:.2f},{ry:.2f} 0 0,1 {sx - rx:.2f},{bot:.2f} Z")
    p.edge.append(("ln",
                   f"M{sx - rx:.2f},{top:.2f} a{rx:.2f},{ry:.2f} 0 1,0 {2 * rx:.2f},0 "
                   f"a{rx:.2f},{ry:.2f} 0 1,0 {-2 * rx:.2f},0"))
    p.edge.append(("ln", f"M{sx - rx:.2f},{bot:.2f} a{rx:.2f},{ry:.2f} 0 0,0 {2 * rx:.2f},0"))
    p.edge.append(("ln", f"M{sx - rx:.2f},{top:.2f} L{sx - rx:.2f},{bot:.2f}"))
    p.edge.append(("ln", f"M{sx + rx:.2f},{top:.2f} L{sx + rx:.2f},{bot:.2f}"))
    for i in range(1, bands):
        _, by = prj(cx, cy, z0 + h * i / bands)
        p.edge.append(("hair", f"M{sx - rx:.2f},{by:.2f} a{rx:.2f},{ry:.2f} 0 0,0 {2 * rx:.2f},0"))
    PARTS.append(p)
    return p


def pipe(a, b, r=1.8):
    ax, ay, az = a
    bx, by, bz = b
    if ax != bx:
        return box((min(ax, bx), ay - r, az - r), (abs(bx - ax), 2 * r, 2 * r))
    if ay != by:
        return box((ax - r, min(ay, by), az - r), (2 * r, abs(by - ay), 2 * r))
    return box((ax - r, ay - r, min(az, bz)), (2 * r, 2 * r, abs(bz - az)))


def valve(x, y, z):
    box((x - 2.7, y - 2.7, z - 2.7), (5.4, 5.4, 5.4))
    p = Part()
    p.edge.append(("ln", "M{:.2f},{:.2f} L{:.2f},{:.2f}".format(
        *prj(x, y, z + 2.7), *prj(x, y, z + 7.4))))
    rx, ry = 3.6 * C30 * RT2, 3.6 * S30 * RT2
    hx, hy = prj(x, y, z + 7.4)
    p.sil.append(f"M{hx - rx:.2f},{hy:.2f} a{rx:.2f},{ry:.2f} 0 1,0 {2 * rx:.2f},0 "
                 f"a{rx:.2f},{ry:.2f} 0 1,0 {-2 * rx:.2f},0 Z")
    p.edge.append(("ln", f"M{hx - rx:.2f},{hy:.2f} a{rx:.2f},{ry:.2f} 0 1,0 {2 * rx:.2f},0 "
                        f"a{rx:.2f},{ry:.2f} 0 1,0 {-2 * rx:.2f},0"))
    PARTS.append(p)


# =====================================================================
#  Scene, built strictly back to front so the painter's order is honest.
#  y grows toward the viewer: y=10 is the back rank, y=60 the front rank.
# =====================================================================

# --- skid frame ------------------------------------------------------
box((0, 0, 0), (160, 70, 5), heavy=True)

# --- back rank: primary header, its drops, and the control cabinet ----
pipe((4, 10, 62), (152, 10, 62))
pipe((22, 10, 62), (22, 30, 62))
pipe((22, 30, 62), (22, 30, 50))
pipe((48, 10, 62), (48, 32, 62))
pipe((48, 32, 62), (48, 32, 40))
valve(88, 10, 62)
box((132, 4, 5), (16, 10, 42), plates=4)

# --- middle rank: heat exchangers and the storage vessel --------------
box((14, 28, 5), (18, 22, 46), plates=9, ribs=5)
box((40, 30, 5), (16, 20, 36), plates=8, ribs=4)
cyl(120, 37, 5, 17, 60, bands=4)
box((114, 31, 65), (12, 12, 4))

# --- front rank: return header, pump set, secondary header ------------
pipe((4, 60, 12), (146, 60, 12))
for px in (66, 88):
    cyl(px, 60, 12, 6.6, 15)
    box((px - 5.2, 54.8, 27), (10.4, 10.4, 13))
    pipe((px, 60, 40), (px, 60, 50))
valve(30, 60, 12)
valve(112, 60, 12)
pipe((4, 60, 50), (146, 60, 50))
valve(104, 60, 50)

# =====================================================================
#  Bounds
# =====================================================================
xs, ys = [], []
for p in PARTS:
    for d in p.sil + [e for _, e in p.edge]:
        for tok in d.replace("M", " ").replace("L", " ").replace("A", " ") \
                    .replace("a", " ").replace("Z", " ").split():
            if tok.count(",") == 1:
                try:
                    a, b = tok.split(",")
                    xs.append(float(a)); ys.append(float(b))
                except ValueError:
                    pass
mx0, mx1, my0, my1 = min(xs), max(xs), min(ys), max(ys)

FS = 5.6                     # label size
CH_GAP = 9.0                # vertical gap between leader channels
LABEL_PAD = 5.0

CALLOUTS = [                 # (anchor, text) — anchors are top faces
    ((23, 37, 51), "Wärmeübertrager"),
    ((88, 60, 40), "Umwälzpumpen"),
    ((120, 37, 69), "Pufferspeicher"),
    ((140, 9, 47), "Regelung"),
]
# Sort left to right on screen; leftmost gets the highest channel so no
# vertical segment ever crosses a horizontal one.
anchors = sorted(((prj(*a), t) for a, t in CALLOUTS), key=lambda k: k[0][0])
n = len(anchors)
top_channel = my0 - 9
label_x = mx1 + 13
leaders, labels = [], []
for i, ((ax, ay), text) in enumerate(anchors):
    chan = top_channel - (n - 1 - i) * CH_GAP
    leaders.append(f"M{ax:.2f},{ay:.2f} L{ax:.2f},{chan:.2f} L{label_x:.2f},{chan:.2f}")
    labels.append((label_x + LABEL_PAD, chan + FS * 0.36, text, "start"))
    ys.append(chan)

# the frame gets its own callout, dropped below the skid into empty space
fx, fy = prj(160, 70, 0)
drop = fy + 15
leaders.append(f"M{fx:.2f},{fy:.2f} L{fx:.2f},{drop:.2f}")
labels.append((fx - LABEL_PAD, drop + FS * 0.9, "Rahmen — eigene Fertigung", "end"))
ys.append(drop + FS * 1.6)

longest = max(len(t) for _, _, t, _ in labels)
minx, maxx = mx0 - 10, label_x + LABEL_PAD + longest * FS * 0.62
miny, maxy = min(ys) - 8, max(ys) + 6
W, H = maxx - minx, maxy - miny

CLS = {"heavy": 'stroke-width="1.45"',
       "ln": 'stroke-width="1.0"',
       "hair": 'stroke-width="0.45" opacity="0.45"'}

out = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{minx:.1f} {miny:.1f} {W:.1f} {H:.1f}" '
    f'fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" '
    f'role="img" aria-labelledby="stationTitle">',
    '<title id="stationTitle">Isometrische Konstruktionszeichnung einer '
    'Fernwärmeübergabestation: Wärmeübertrager, Umwälzpumpen, Pufferspeicher und '
    'Regelung auf einem im eigenen Betrieb gefertigten Rahmen.</title>',
]
for p in PARTS:
    out.append('<g>')
    for s in p.sil:
        out.append(f'<path d="{s}" fill="var(--iso-ground, #fff)" stroke="none"/>')
    for cls in ("hair", "ln", "heavy"):
        seg = [d for c, d in p.edge if c == cls]
        if seg:
            out.append(f'<g {CLS[cls]}>' + "".join(f'<path d="{d}"/>' for d in seg) + '</g>')
    out.append('</g>')

out.append('<g stroke-width="0.45" opacity="0.75">')
for d in leaders:
    out.append(f'<path d="{d}"/>')
out.append('</g>')
out.append(f'<g fill="currentColor" stroke="none" font-size="{FS}" '
           f'font-family="ui-monospace, SFMono-Regular, Menlo, monospace" '
           f'letter-spacing="0.35" opacity="0.75">')
for tx, ty, text, anchor in labels:
    out.append(f'<text x="{tx:.2f}" y="{ty:.2f}" text-anchor="{anchor}">{text}</text>')
out.append('</g></svg>')

svg = "\n".join(out)
open("/home/user/design-ai/ackermann-website/assets/station-iso.svg", "w").write(svg)
print(f"viewBox {minx:.1f} {miny:.1f} {W:.1f} {H:.1f}  parts={len(PARTS)}  bytes={len(svg)}")
