#!/usr/bin/env python3
"""render.py <in.svg> <out.png> [width]  — Vorschau einer Zeichnung auf weißem Blatt."""
import asyncio
import sys

from playwright.async_api import async_playwright

HTML = """<!doctype html><meta charset="utf-8">
<style>
:root{--iso-ground:#fff;--pipe-vl:#E2001A;--pipe-rl:#5B7A94;--pipe-kw:#3F8F6B;--pipe-ww:#E2001A;--pipe-luft:#8A8A8A;--pipe-gas:#C9A400}
body{margin:0;background:#fff;color:#111}.w{padding:28px 36px}svg{width:100%%;height:auto;display:block}
</style><div class="w">%s</div>"""


async def main(src, dst, width):
    svg = open(src).read()
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pg = await b.new_page(viewport={"width": width, "height": 600}, device_scale_factor=2)
        await pg.set_content(HTML % svg)
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=dst, full_page=True)
        await b.close()


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1000))
