# Corrige le VISAP d'origine (TEC-VISAP-TRIPTYQUE-01 Rév. E, ReportLab) sans le refaire :
# ajoute « 4. » devant « FICHE TERRAIN - Croquis et observations » et remonte le bloc
# « VISAP réalisée par » au-dessus du pied de page (volet central intérieur).
# Usage : python3 corriger-visap-original.py VISAP.pdf VISAP-corrige.pdf
import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, DecodedStreamObject
src, dst = sys.argv[1], sys.argv[2]
r = PdfReader(src)
w = PdfWriter(clone_from=r)
p = w.pages[1]
data = p['/Contents'].get_object().get_data().decode('latin-1')
rep = [
    # 1) section 4 : « 4. » devant FICHE TERRAIN - Croquis et observations
    ("(FICHE TERRAIN - Croquis et observations) Tj", "(4. FICHE TERRAIN - Croquis et observations) Tj"),
    # 2) zone Observations raccourcie de 6 mm par le bas (le haut ne bouge pas)
    ("n 629.2913 99.2126 538.5827 73.70079 re S", "n 629.2913 116 538.5827 56.91 re S"),
    # 3) bloc « VISAP réalisée par » remonté de ~7,5 mm, au-dessus du pied de page
    ("BT 1 0 0 1 629.2913 76.53543 Tm /F2+0 7.4 Tf", "BT 1 0 0 1 629.2913 102.7 Tm /F2+0 7.4 Tf"),
    ("n 629.2913 36.85039 242.3622 39.68504 re S", "n 629.2913 58 242.3622 39.68504 re S"),
    ("n 871.6535 36.85039 161.5748 39.68504 re S", "n 871.6535 58 161.5748 39.68504 re S"),
    ("n 1033.228 36.85039 134.6457 39.68504 re S", "n 1033.228 58 134.6457 39.68504 re S"),
    ("BT 1 0 0 1 636.0945 64.06299 Tm", "BT 1 0 0 1 636.0945 85.2 Tm"),
    ("BT 1 0 0 1 878.4567 64.06299 Tm", "BT 1 0 0 1 878.4567 85.2 Tm"),
    ("BT 1 0 0 1 1040.031 64.06299 Tm", "BT 1 0 0 1 1040.031 85.2 Tm"),
]
for a, b in rep:
    assert data.count(a) == 1, a
    data = data.replace(a, b)
ns = DecodedStreamObject()
ns.set_data(data.encode('latin-1'))
p[NameObject('/Contents')] = w._add_object(ns.flate_encode())
w.write(dst)
print('écrit', dst)
