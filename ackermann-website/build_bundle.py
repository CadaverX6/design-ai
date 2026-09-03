#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Packt die statische Website in eine einzelne, in sich geschlossene HTML-Datei,
damit sie sich über einen Link ansehen lässt. Inhaltlich identisch zur
Mehrseiten-Fassung in site/ — nur der Transport ist ein anderer.
"""
import base64
import json
import os
import re

SITE = "/home/user/design-ai/ackermann-website/site"
OUT = "/home/user/design-ai/ackermann-website/website-vorschau.html"

# ---- CSS mit eingebetteten Schriften -------------------------------------
fonts_css = open(f"{SITE}/assets/fonts.css").read()
for m in set(re.findall(r"url\('fonts/([^']+)'\)", fonts_css)):
    raw = open(f"{SITE}/assets/fonts/{m}", "rb").read()
    uri = "data:font/woff2;base64," + base64.b64encode(raw).decode()
    fonts_css = fonts_css.replace(f"url('fonts/{m}')", f"url({uri})")

site_css = open(f"{SITE}/assets/site.css").read()
site_js = open(f"{SITE}/assets/site.js").read()

# ---- Seiten einsammeln ---------------------------------------------------
pages = {}
for dirpath, _, files in os.walk(SITE):
    for f in sorted(files):
        if not f.endswith(".html"):
            continue
        full = os.path.join(dirpath, f)
        key = os.path.relpath(full, SITE).replace(os.sep, "/")
        html = open(full).read()
        main = re.search(r'<main id="inhalt">(.*?)</main>', html, re.S).group(1)
        title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)
        # Verweise auf die Wurzel normalisieren, damit ein Router sie auflösen kann
        depth = key.count("/")
        if depth:
            main = main.replace('href="../', 'href="')
        pages[key] = {"title": title, "html": main}

# Kopfzeile und Navigationsblatt einmal aus der Startseite übernehmen
home = open(f"{SITE}/index.html").read()
header = re.search(r"(<header class=\"site-head\">.*?</header>)", home, re.S).group(1)
navsheet = re.search(r"(<div class=\"nav-sheet\".*?</div>\s*</div>)", home, re.S)
navsheet = re.search(r'(<div class="nav-sheet" id="mobile-nav" hidden>.*?</nav>\s*</div>)', home, re.S).group(1)

doc = f"""<title>Ackermann Gebäudetechnik</title>
<style>
{fonts_css}
{site_css}
/* Nur für die Einzeldatei-Vorschau: der Hinweisstreifen über der Website. */
.vorschau{{
  background:#111111; color:#FFFFFF; font:400 12px/1.5 var(--sans);
  padding:10px 24px; text-align:center;
}}
.vorschau b{{font-weight:600}}
.vorschau span{{color:#B9B9B9}}
</style>

<p class="vorschau"><b>Statische Präsentationsfassung.</b>
<span>Alle Bildflächen sind Platzhalter für echte Projektfotos · Rotwert und Webfont
sind Platzhalter aus dem Corporate Design abzuleiten</span></p>

<a class="skip" href="#inhalt">Zum Inhalt springen</a>
<div class="sheet">
{header}
{navsheet}
<main id="inhalt"></main>
</div>

<script>
var PAGES = {json.dumps(pages, ensure_ascii=False)};

(function () {{
  var view = document.getElementById('inhalt');

  function setNav(key) {{
    document.querySelectorAll('.site-nav a, .nav-sheet nav a').forEach(function (a) {{
      var href = a.getAttribute('href');
      if (href === key) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    }});
  }}

  function show(key, hash) {{
    var page = PAGES[key];
    if (!page) return false;
    view.innerHTML = page.html;
    document.title = page.title;
    setNav(key);
    if (hash) {{
      var el = document.getElementById(hash);
      if (el) {{ el.scrollIntoView(); return true; }}
    }}
    window.scrollTo(0, 0);
    return true;
  }}

  // Interne Verweise abfangen; alles andere (tel:, mailto:) bleibt unberührt.
  document.addEventListener('click', function (e) {{
    var a = e.target.closest ? e.target.closest('a') : null;
    if (!a) return;
    var href = a.getAttribute('href');
    if (!href || /^(https?:|mailto:|tel:)/.test(href)) return;

    if (href.charAt(0) === '#') {{
      var el = document.getElementById(href.slice(1));
      if (el) {{ e.preventDefault(); el.scrollIntoView(); }}
      return;
    }}
    var parts = href.split('#');
    var key = parts[0].replace(/^\\.\\//, '');
    if (PAGES[key]) {{
      e.preventDefault();
      var sheet = document.getElementById('mobile-nav');
      if (sheet && !sheet.hidden) {{
        sheet.hidden = true;
        document.body.classList.remove('nav-open');
        var t = document.querySelector('.nav-toggle');
        if (t) t.setAttribute('aria-expanded', 'false');
      }}
      show(key, parts[1]);
      history.pushState({{key: key}}, '', '#' + key + (parts[1] ? '@' + parts[1] : ''));
    }}
  }});

  window.addEventListener('popstate', function () {{ fromHash(); }});

  function fromHash() {{
    var raw = location.hash.slice(1);
    var key = 'index.html', anchor = '';
    if (raw) {{
      var bits = raw.split('@');
      if (PAGES[bits[0]]) {{ key = bits[0]; anchor = bits[1] || ''; }}
    }}
    show(key, anchor);
  }}

  fromHash();
}})();

{site_js}
</script>
"""

open(OUT, "w").write(doc)
print(f"{len(pages)} Seiten · {len(doc)/1024/1024:.2f} MB · {OUT}")
