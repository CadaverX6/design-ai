#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iso — kleine Bibliothek für isometrische Konstruktionszeichnungen als SVG.

Alle Zeichnungen der Website entstehen hieraus, damit sie eine gemeinsame
Sprache sprechen: gleiche Projektion, gleiche Strichstärken, gleiche
Beschriftung, gleiche Farbkonvention für Leitungen.

Konventionen
------------
* Weltkoordinaten: x nach rechts-unten, y nach links-unten (zum Betrachter),
  z nach oben. Ein Körper mit größerem y steht weiter vorn.
* Malreihenfolge = Aufrufreihenfolge. Hinten zuerst zeichnen, vorn zuletzt.
  Jeder Körper trägt eine mit der Grundfläche gefüllte Silhouette und
  verdeckt damit, was hinter ihm liegt.
* Konturen erben currentColor. Leitungen bekommen per `kind` eine Klasse:
      'n'   neutral (Ink)          'vl'  Heizung Vorlauf   (Rot)
      'rl'  Heizung Rücklauf (Blau) 'kw'  Kaltwasser        (Grün)
      'ww'  Warmwasser (Rot)        'luft' Luft            (Grau)
  Die Farben liegen als CSS-Variablen im SVG-Stylesheet mit Fallback, sodass
  die Seite sie über --pipe-vl usw. steuern kann.
* Beschriftungen: `callout()` setzt Ausleger in eine rechte Spalte, ohne
  dass sich Linien kreuzen. `footnote()` hängt eine Notiz unter das Objekt.
"""
import math

C30, S30 = math.cos(math.radians(30)), math.sin(math.radians(30))
RT2 = math.sqrt(2)

PIPE_COLORS = {
    "n": None,
    "vl": ("--pipe-vl", "#E2001A"),
    "rl": ("--pipe-rl", "#5B7A94"),
    "kw": ("--pipe-kw", "#3F8F6B"),
    "ww": ("--pipe-ww", "#E2001A"),
    "luft": ("--pipe-luft", "#8A8A8A"),
    "gas": ("--pipe-gas", "#C9A400"),
}

LEGEND_NAMES = {"vl": "Vorlauf", "rl": "Rücklauf", "kw": "Kaltwasser",
                "ww": "Warmwasser", "luft": "Luft", "gas": "Gas"}

# Flächentöne je Orientierung: oben hell, links mittel, rechts dunkel.
# Damit lesen die Körper als Volumen statt als Drahtgitter.
TONES = {
    "n":    ("--iso-top",    "#F2F2EF", "--iso-left",    "#E2E2DE", "--iso-right",    "#D0D0CB"),
    "vl":   ("--iso-vl-t",   "#FBDDE0", "--iso-vl-l",    "#F4BFC4", "--iso-vl-r",     "#EBA3AA"),
    "ww":   ("--iso-vl-t",   "#FBDDE0", "--iso-vl-l",    "#F4BFC4", "--iso-vl-r",     "#EBA3AA"),
    "rl":   ("--iso-rl-t",   "#E7EEF4", "--iso-rl-l",    "#D1DFEA", "--iso-rl-r",     "#B9CDDD"),
    "kw":   ("--iso-kw-t",   "#E3F1EA", "--iso-kw-l",    "#CBE4D7", "--iso-kw-r",     "#B0D3C1"),
    "luft": ("--iso-luft-t", "#EFEFEF", "--iso-luft-l",  "#E0E0E0", "--iso-luft-r",   "#CFCFCF"),
    "gas":  ("--iso-gas-t",  "#F7EFD2", "--iso-gas-l",   "#EDE0B4", "--iso-gas-r",    "#E0CE92"),
    # Akzentkörper: die Hauptkomponente einer Zeichnung darf dunkler stehen
    "dark": ("--iso-dk-t",   "#C9C9C3", "--iso-dk-l",    "#B4B4AE", "--iso-dk-r",     "#9E9E98"),
}


def prj(x, y, z):
    return ((x - y) * C30, (x + y) * S30 - z)


def _pts(seq):
    return " L".join(f"{a:.2f},{b:.2f}" for a, b in seq)


def _closed(seq):
    return "M" + _pts(seq) + " Z"


def _open(seq):
    return "M" + _pts(seq)


def _hull(points):
    """Monotone-chain convex hull; used for the silhouette of round bodies."""
    pts = sorted(set(points))
    if len(pts) < 3:
        return pts

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


class _Part:
    __slots__ = ("sil", "edge", "faces")

    def __init__(self):
        self.sil = []
        self.edge = []       # (cls, kind, path)
        self.faces = []      # (tone, orientation, path)


class Scene:
    def __init__(self, title=""):
        self.title = title
        self.parts = []
        self.callouts = []   # (anchor_xyz, text)
        self.footnotes = []  # (anchor_xyz, text)
        self.kinds_used = set()
        self._xs, self._ys = [], []

    # ------------------------------------------------------------ helpers
    def _track(self, seq):
        for a, b in seq:
            self._xs.append(a)
            self._ys.append(b)

    def _new(self):
        p = _Part()
        self.parts.append(p)
        return p

    # ------------------------------------------------------------ solids
    def box(self, o, s, plates=0, ribs=0, heavy=False, kind="n", hidden_edges=False):
        """Quader. `plates` schraffiert die Vorderseite, `ribs` die rechte Seite."""
        x, y, z = o
        w, d, h = s
        x1, y1, z1 = x + w, y + d, z + h
        P = prj
        p = self._new()
        sil = [P(x, y1, z1), P(x, y, z1), P(x1, y, z1), P(x1, y, z), P(x1, y1, z), P(x, y1, z)]
        self._track(sil)
        tone = kind if kind in TONES else "n"
        p.faces.append((tone, "top",   _closed([P(x, y, z1), P(x1, y, z1), P(x1, y1, z1), P(x, y1, z1)])))
        p.faces.append((tone, "left",  _closed([P(x, y1, z), P(x1, y1, z), P(x1, y1, z1), P(x, y1, z1)])))
        p.faces.append((tone, "right", _closed([P(x1, y, z), P(x1, y1, z), P(x1, y1, z1), P(x1, y, z1)])))
        cls = "heavy" if heavy else "ln"
        p.edge.append((cls, kind, _closed([P(x, y, z1), P(x1, y, z1), P(x1, y1, z1), P(x, y1, z1)])))
        p.edge.append((cls, kind, _open([P(x, y1, z), P(x1, y1, z), P(x1, y, z)])))
        for cx, cy in ((x1, y1), (x, y1), (x1, y)):
            p.edge.append((cls, kind, _open([P(cx, cy, z), P(cx, cy, z1)])))
        for i in range(1, plates):
            t = x + w * i / plates
            p.edge.append(("hair", "n", _open([P(t, y1, z), P(t, y1, z1)])))
        for i in range(1, ribs):
            t = y + d * i / ribs
            p.edge.append(("hair", "n", _open([P(x1, t, z), P(x1, t, z1)])))
        if kind != "n":
            self.kinds_used.add(kind)
        return p

    def cyl(self, cx, cy, z0, r, h, bands=0, kind="n"):
        """Stehender Zylinder (Speicher, Pumpe, Kessel)."""
        rx, ry = r * C30 * RT2, r * S30 * RT2
        sx, top = prj(cx, cy, z0 + h)
        _, bot = prj(cx, cy, z0)
        p = self._new()
        tone = kind if kind in TONES else "n"
        p.faces.append((tone, "left",
            f"M{sx - rx:.2f},{top:.2f} A{rx:.2f},{ry:.2f} 0 0,1 {sx + rx:.2f},{top:.2f} "
            f"L{sx + rx:.2f},{bot:.2f} A{rx:.2f},{ry:.2f} 0 0,1 {sx - rx:.2f},{bot:.2f} Z"))
        p.faces.append((tone, "right",
            f"M{sx:.2f},{top + ry:.2f} A{rx:.2f},{ry:.2f} 0 0,0 {sx + rx:.2f},{top:.2f} "
            f"L{sx + rx:.2f},{bot:.2f} A{rx:.2f},{ry:.2f} 0 0,1 {sx:.2f},{bot + ry:.2f} Z"))
        p.faces.append((tone, "top",
            f"M{sx - rx:.2f},{top:.2f} a{rx:.2f},{ry:.2f} 0 1,0 {2 * rx:.2f},0 "
            f"a{rx:.2f},{ry:.2f} 0 1,0 {-2 * rx:.2f},0 Z"))
        p.edge.append(("ln", kind,
                       f"M{sx - rx:.2f},{top:.2f} a{rx:.2f},{ry:.2f} 0 1,0 {2 * rx:.2f},0 "
                       f"a{rx:.2f},{ry:.2f} 0 1,0 {-2 * rx:.2f},0"))
        p.edge.append(("ln", kind, f"M{sx - rx:.2f},{bot:.2f} a{rx:.2f},{ry:.2f} 0 0,0 {2 * rx:.2f},0"))
        p.edge.append(("ln", kind, f"M{sx - rx:.2f},{top:.2f} L{sx - rx:.2f},{bot:.2f}"))
        p.edge.append(("ln", kind, f"M{sx + rx:.2f},{top:.2f} L{sx + rx:.2f},{bot:.2f}"))
        for i in range(1, bands):
            _, by = prj(cx, cy, z0 + h * i / bands)
            p.edge.append(("hair", "n", f"M{sx - rx:.2f},{by:.2f} a{rx:.2f},{ry:.2f} 0 0,0 {2 * rx:.2f},0"))
        self._track([(sx - rx, top - ry), (sx + rx, bot + ry)])
        if kind != "n":
            self.kinds_used.add(kind)
        return p

    def hcyl(self, a, length, r, axis="x", bands=0, kind="n"):
        """Liegender Zylinder entlang x oder y (Kessel, Puffer, Rohrleitung DN groß)."""
        x0, y0, z0 = a
        n = 36

        def ring(t):
            out = []
            for i in range(n):
                th = 2 * math.pi * i / n
                if axis == "x":
                    out.append(prj(t, y0 + r * math.cos(th), z0 + r * math.sin(th)))
                else:
                    out.append(prj(x0 + r * math.cos(th), t, z0 + r * math.sin(th)))
            return out

        start = x0 if axis == "x" else y0
        far, near = ring(start), ring(start + length)
        p = self._new()
        hull = _hull(far + near)
        tone = kind if kind in TONES else "n"
        p.faces.append((tone, "left", _closed(hull)))
        p.faces.append((tone, "top", _closed(near)))
        self._track(hull)
        # near cap complete, far cap only its visible upper half (−45° … 135°)
        p.edge.append(("ln", kind, _closed(near)))
        vis = [pt for i, pt in enumerate(far) if -45 <= ((360 * i / n + 45) % 360) - 45 <= 135]
        # keep angular order for the open arc
        idx = [i for i in range(n) if -45 <= ((360 * i / n + 45) % 360) - 45 <= 135]
        idx.sort(key=lambda i: ((360 * i / n) + 45) % 360)
        p.edge.append(("ln", kind, _open([far[i] for i in idx])))
        # silhouette generators at 135° and 315°
        for th in (math.radians(135), math.radians(315)):
            if axis == "x":
                A = prj(start, y0 + r * math.cos(th), z0 + r * math.sin(th))
                B = prj(start + length, y0 + r * math.cos(th), z0 + r * math.sin(th))
            else:
                A = prj(x0 + r * math.cos(th), start, z0 + r * math.sin(th))
                B = prj(x0 + r * math.cos(th), start + length, z0 + r * math.sin(th))
            p.edge.append(("ln", kind, _open([A, B])))
        for i in range(1, bands):
            t = start + length * i / bands
            rg = ring(t)
            idx2 = [k for k in range(n) if -45 <= ((360 * k / n + 45) % 360) - 45 <= 135]
            idx2.sort(key=lambda k: ((360 * k / n) + 45) % 360)
            p.edge.append(("hair", "n", _open([rg[k] for k in idx2])))
        if kind != "n":
            self.kinds_used.add(kind)
        return p

    def pipe(self, a, b, r=1.8, kind="n"):
        """Leitungsstück zwischen zwei Punkten, achsparallel."""
        ax, ay, az = a
        bx, by, bz = b
        if ax != bx:
            return self.box((min(ax, bx), ay - r, az - r), (abs(bx - ax), 2 * r, 2 * r), kind=kind)
        if ay != by:
            return self.box((ax - r, min(ay, by), az - r), (2 * r, abs(by - ay), 2 * r), kind=kind)
        return self.box((ax - r, ay - r, min(az, bz)), (2 * r, 2 * r, abs(bz - az)), kind=kind)

    def run(self, points, r=1.8, kind="n"):
        """Leitungszug über mehrere Eckpunkte, hinten nach vorn angegeben."""
        for a, b in zip(points, points[1:]):
            self.pipe(a, b, r=r, kind=kind)

    def duct(self, a, b, w=8, h=6, kind="luft"):
        """Rechteckiger Luftkanal, achsparallel; w = Breite quer, h = Höhe."""
        ax, ay, az = a
        bx, by, bz = b
        if ax != bx:
            return self.box((min(ax, bx), ay - w / 2, az - h / 2), (abs(bx - ax), w, h), kind=kind)
        if ay != by:
            return self.box((ax - w / 2, min(ay, by), az - h / 2), (w, abs(by - ay), h), kind=kind)
        return self.box((ax - w / 2, ay - h / 2, min(az, bz)), (w, h, abs(bz - az)), kind=kind)

    def valve(self, x, y, z, kind="n"):
        """Armatur: Gehäuse, Spindel, Handrad."""
        self.box((x - 2.7, y - 2.7, z - 2.7), (5.4, 5.4, 5.4), kind=kind)
        p = self._new()
        p.edge.append(("ln", "n", _open([prj(x, y, z + 2.7), prj(x, y, z + 7.4)])))
        rx, ry = 3.6 * C30 * RT2, 3.6 * S30 * RT2
        hx, hy = prj(x, y, z + 7.4)
        ell = (f"M{hx - rx:.2f},{hy:.2f} a{rx:.2f},{ry:.2f} 0 1,0 {2 * rx:.2f},0 "
               f"a{rx:.2f},{ry:.2f} 0 1,0 {-2 * rx:.2f},0")
        p.faces.append(("n", "top", ell + " Z"))
        p.edge.append(("ln", "n", ell))
        self._track([(hx - rx, hy - ry), (hx + rx, hy + ry)])

    def pump(self, x, y, z, r=6.0, h=14, motor=12):
        """Inline-Pumpe: Gehäuse als Zylinder, Motor als Block darüber."""
        self.cyl(x, y, z, r, h)
        self.box((x - r * 0.8, y - r * 0.8, z + h), (r * 1.6, r * 1.6, motor))

    def flange(self, at, axis, r=3.0, kind="n"):
        x, y, z = at
        t = 0.9
        if axis == "x":
            self.box((x - t, y - r, z - r), (2 * t, 2 * r, 2 * r), kind=kind)
        elif axis == "y":
            self.box((x - r, y - t, z - r), (2 * r, 2 * t, 2 * r), kind=kind)
        else:
            self.box((x - r, y - r, z - t), (2 * r, 2 * r, 2 * t), kind=kind)

    def room(self, w, d, h, wall=3, door=None):
        """Bestandsraum: Boden und zwei Rückwände. Zuerst aufrufen (liegt hinten)."""
        self.box((-wall, -wall, -3), (w + wall, d + wall, 3), heavy=True)          # Boden
        self.box((-wall, -wall, 0), (w + wall, wall, h))                            # Rückwand (y=0)
        self.box((-wall, -wall, 0), (wall, d + wall, h))                            # Seitenwand (x=0)
        if door:                                                                    # Türöffnung in der Rückwand
            dx, dw, dh = door
            p = self._new()
            p.edge.append(("hair", "n", _closed([prj(dx, 0, 0), prj(dx + dw, 0, 0),
                                                 prj(dx + dw, 0, dh), prj(dx, 0, dh)])))

    def line(self, a, b, cls="hair"):
        p = self._new()
        p.edge.append((cls, "n", _open([prj(*a), prj(*b)])))

    # ------------------------------------------------------------ text
    def callout(self, anchor, text):
        self.callouts.append((anchor, text))

    def footnote(self, anchor, text):
        self.footnotes.append((anchor, text))

    # ------------------------------------------------------------ output
    def render(self, fs=7.4, gap=9.0, legend=True, klass="iso"):
        xs, ys = list(self._xs), list(self._ys)
        mx0, mx1, my0, my1 = min(xs), max(xs), min(ys), max(ys)
        pad = 5.0

        leaders, labels = [], []
        anchors = sorted(((prj(*a), t) for a, t in self.callouts), key=lambda k: k[0][0])
        n = len(anchors)
        label_x = mx1 + 13
        top = my0 - 9
        for i, ((ax, ay), text) in enumerate(anchors):
            chan = top - (n - 1 - i) * gap
            leaders.append(f"M{ax:.2f},{ay:.2f} L{ax:.2f},{chan:.2f} L{label_x:.2f},{chan:.2f}")
            labels.append((label_x + pad, chan + fs * 0.36, text, "start"))
            ys.append(chan)

        foot_y = my1
        for (a, text) in self.footnotes:
            fx, fy = prj(*a)
            drop = fy + 15
            leaders.append(f"M{fx:.2f},{fy:.2f} L{fx:.2f},{drop:.2f}")
            labels.append((fx - pad, drop + fs * 0.9, text, "end"))
            foot_y = max(foot_y, drop + fs * 1.6)
        ys.append(foot_y)

        longest = max([len(t) for _, _, t, _ in labels] + [0])
        minx = mx0 - 10
        maxx = (label_x + pad + longest * fs * 0.62) if anchors else (mx1 + 10)
        legend_h = fs * 2.2 if (legend and self.kinds_used) else 0
        miny, maxy = min(ys) - 8, max(ys) + 6 + legend_h
        W, H = maxx - minx, maxy - miny

        CLS = {"heavy": 'stroke-width="1.45"', "ln": 'stroke-width="1.0"',
               "hair": 'stroke-width="0.45" opacity="0.45"'}

        style = [f".{klass} .k-n{{stroke:currentColor}}"]
        for k, v in PIPE_COLORS.items():
            if v:
                style.append(f".{klass} .k-{k}{{stroke:var({v[0]},{v[1]})}}")
        for k, t in TONES.items():
            style.append(f".{klass} .f-{k}-top{{fill:var({t[0]},{t[1]})}}")
            style.append(f".{klass} .f-{k}-left{{fill:var({t[2]},{t[3]})}}")
            style.append(f".{klass} .f-{k}-right{{fill:var({t[4]},{t[5]})}}")

        out = [
            f'<svg xmlns="http://www.w3.org/2000/svg" class="{klass}" '
            f'viewBox="{minx:.1f} {miny:.1f} {W:.1f} {H:.1f}" '
            f'fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" '
            f'role="img" aria-label="{self.title}">',
            "<style>" + "".join(style) + "</style>",
        ]
        for p in self.parts:
            out.append("<g>")
            for s in p.sil:
                out.append(f'<path d="{s}" fill="var(--iso-ground,#fff)" stroke="none"/>')
            for tone, orient, d in p.faces:
                out.append(f'<path d="{d}" class="f-{tone}-{orient}" stroke="none"/>')
            groups = {}
            for cls, kind, d in p.edge:
                groups.setdefault((cls, kind), []).append(d)
            for (cls, kind), ds in groups.items():
                out.append(f'<g {CLS[cls]} class="k-{kind}">' +
                           "".join(f'<path d="{d}"/>' for d in ds) + "</g>")
            out.append("</g>")

        if leaders:
            out.append('<g class="iso-callouts" stroke-width="0.45" opacity="0.75">' +
                       "".join(f'<path d="{d}"/>' for d in leaders) + "</g>")
            out.append(f'<g class="iso-callouts" fill="currentColor" stroke="none" font-size="{fs}" '
                       f'font-family="ui-monospace,SFMono-Regular,Menlo,monospace" '
                       f'letter-spacing="0.35" opacity="0.75">' +
                       "".join(f'<text x="{tx:.2f}" y="{ty:.2f}" text-anchor="{an}">{t}</text>'
                               for tx, ty, t, an in labels) + "</g>")

        if legend and self.kinds_used:
            lx, ly = minx + 10, maxy - fs * 0.9
            items = []
            for k in ("vl", "rl", "kw", "ww", "luft", "gas"):
                if k in self.kinds_used:
                    items.append(f'<path class="k-{k}" stroke="currentColor" stroke-width="1.6" d="M{lx:.1f},{ly - fs * 0.32:.1f} h{fs * 2:.1f}"/>'
                                 f'<text x="{lx + fs * 2.6:.1f}" y="{ly:.1f}">{LEGEND_NAMES[k]}</text>')
                    lx += fs * 2.6 + len(LEGEND_NAMES[k]) * fs * 0.62 + fs * 1.6
            out.append(f'<g class="iso-legend" fill="currentColor" stroke="none" font-size="{fs * 0.92:.1f}" '
                       f'font-family="ui-monospace,SFMono-Regular,Menlo,monospace" opacity="0.75">'
                       + "".join(items) + "</g>")
        out.append("</svg>")
        return "\n".join(out)

    def write(self, path, **kw):
        svg = self.render(**kw)
        open(path, "w").write(svg)
        return svg
