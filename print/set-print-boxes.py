"""Renseigne TrimBox (format fini A4) et BleedBox (fonds perdus) sur chaque page du PDF imprimeur.

Usage : python3 set-print-boxes.py <fichier.pdf> <fonds_perdus_mm>
"""
import sys

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

path, bleed_mm = sys.argv[1], float(sys.argv[2])
bleed = bleed_mm * 72 / 25.4
A4_W, A4_H = 210 * 72 / 25.4, 297 * 72 / 25.4

reader = PdfReader(path)
writer = PdfWriter()
for page in reader.pages:
    x0, y0, x1, y1 = (float(v) for v in page.mediabox)
    page.bleedbox = RectangleObject([x0, y0, x1, y1])
    # Chromium arrondit la taille de page au point près : on ancre la coupe A4 exacte
    # sur le coin haut-gauche, d'où la mise en page CSS est calculée.
    page.trimbox = RectangleObject([x0 + bleed, y1 - bleed - A4_H, x0 + bleed + A4_W, y1 - bleed])
    writer.add_page(page)
writer.add_metadata({"/Title": "Catalogue produits — ADOM SENIOR", "/Author": "ADOM SENIOR"})
with open(path, "wb") as f:
    writer.write(f)

print(f"TrimBox 210 × 297 mm, fonds perdus {bleed_mm:g} mm — {len(reader.pages)} pages")
