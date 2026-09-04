# -*- coding: utf-8 -*-
"""
Rückfall-Icons in der Strichsprache der Zeichnungen (24er-Raster, 1,5 px, currentColor).

Sie stehen an jeder Icon-Stelle, bis die ausgewählten Magnific-Stock-Icons in
site/assets/icons/ liegen — dann übernimmt der Build automatisch die Stock-Datei
und diese hier bleiben ungenutzt. Die Auswahl steht in site/assets/icons/MANIFEST.md.
"""

_ATTR = ('xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" '
         'stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" '
         'aria-hidden="true" focusable="false"')

ICONS = {
    # Gewerke -----------------------------------------------------------
    "heizung":     f'<svg {_ATTR}><rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 9h6M9 12h6M9 15h6M8 21v1M16 21v1"/></svg>',
    "sanitaer":    f'<svg {_ATTR}><path d="M4 10h9a4 4 0 0 1 4 4v1"/><path d="M13 10V7h2M11 7h4"/><path d="M4 10v3M17 15v2M15.5 21l1.5-4 1.5 4"/></svg>',
    "lueftung":    f'<svg {_ATTR}><circle cx="12" cy="12" r="2"/><path d="M12 10c0-4 2-6 4-6 1 3-1 5-4 6M14 12c4 0 6 2 6 4-3 1-5-1-6-4M12 14c0 4-2 6-4 6-1-3 1-5 4-6M10 12c-4 0-6-2-6-4 3-1 5 1 6 4"/></svg>',
    "kaelte":      f'<svg {_ATTR}><path d="M12 3v18M3 12h18M6 6l12 12M18 6L6 18"/><path d="M12 3l-2 2M12 3l2 2M12 21l-2-2M12 21l2-2M3 12l2-2M3 12l2 2M21 12l-2-2M21 12l-2 2"/></svg>',
    "stationsbau": f'<svg {_ATTR}><rect x="3" y="9" width="18" height="12" rx="1"/><path d="M7 9V5h4v4M14 13h3M7 13h3M7 17h10"/></svg>',
    # Kontakt -----------------------------------------------------------
    "telefon":     f'<svg {_ATTR}><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>',
    "email":       f'<svg {_ATTR}><rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 6 9-6"/></svg>',
    "service24":   f'<svg {_ATTR}><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "unterlagen":  f'<svg {_ATTR}><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/></svg>',
    "standort":    f'<svg {_ATTR}><path d="M12 21s-6-5.5-6-11a6 6 0 0 1 12 0c0 5.5-6 11-6 11z"/><circle cx="12" cy="10" r="2"/></svg>',
}
