# Étape 3 (à lancer après corriger-visap-original-2.py).
# Volet central intérieur : supprime « 5. Observations » (cadre champ libre) et déplace le bloc
# « VISAP réalisée par » en bas de la fiche produit ; les deux quadrillages de croquis
# sont agrandis (carreaux de 5 mm, trait marqué tous les 25 mm, comme l'original).
# Usage : python3 corriger-visap-original-3.py VISAP-corrige-2.pdf VISAP-corrige-3.pdf
import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, DecodedStreamObject
src, dst = sys.argv[1], sys.argv[2]
r = PdfReader(src); w = PdfWriter(clone_from=r); p = w.pages[1]
L = p['/Contents'].get_object().get_data().decode('latin-1').split('\n')

def idx(s):
    hits = [i for i, l in enumerate(L) if s in l]
    assert len(hits) == 1, (s, hits)
    return hits[0]

X0, WID, CELL = 629.2913, 538.5827, 14.17323   # volet central : x, largeur (38 carreaux), carreau 5 mm
NCOLS, NROWS, GAP = 38, 23, 14.17323
TOP1 = 742.6772
H = NROWS * CELL
grids = [(TOP1 - H, 'IMPLANTATION AVANT TRAVAUX'), (TOP1 - H - GAP - H, 'IMPLANTATION APR\\003S TRAVAUX')]

def grid(y0, label):
    o = ['1 1 1 rg', 'n %.4f %.4f %.4f %.4f re f*' % (X0, y0, WID, H), '.25 w', '.85098 .894118 .894118 RG']
    o += ['n %.4f %.4f m %.4f %.4f l S' % (X0 + i * CELL, y0, X0 + i * CELL, y0 + H) for i in range(1, NCOLS) if i % 5]
    o += ['n %.4f %.4f m %.4f %.4f l S' % (X0, y0 + j * CELL, X0 + WID, y0 + j * CELL) for j in range(1, NROWS) if j % 5]
    o += ['.5 w', '.686275 .776471 .788235 RG']
    o += ['n %.4f %.4f m %.4f %.4f l S' % (X0 + i * CELL, y0, X0 + i * CELL, y0 + H) for i in range(5, NCOLS, 5)]
    o += ['n %.4f %.4f m %.4f %.4f l S' % (X0, y0 + j * CELL, X0 + WID, y0 + j * CELL) for j in range(5, NROWS, 5)]
    o += ['.027451 .243137 .278431 RG', '1.1 w', 'n %.4f %.4f %.4f %.4f re S' % (X0, y0, WID, H)]
    top = y0 + H
    o += ['1 1 1 rg', 'n 632.6929 %.4f 175.748 18.70866 re f*' % (top - 22.677),
          '.027451 .243137 .278431 rg',
          'BT 1 0 0 1 638.9291 %.4f Tm /F2+0 8 Tf 9.6 TL (%s) Tj T* ET' % (top - 17.008, label)]
    return o

# 1) quadrillages : remplacer tout ce qui est entre le titre du volet et « 5. Observations » exclu
t = idx('(4. FICHE TERRAIN - Croquis et observations) Tj')
obs_bar = idx('n 629.2913 184.252 4.535433 15.87402 re f*') - 1      # couleur ambre de la barre « 5. »
new = []
for y0, lab in grids:
    new += grid(y0, lab)
L[t + 1:obs_bar] = new

# 2) supprimer « 5. Observations » + cadre + « CHAMP LIBRE »
a = idx('n 629.2913 184.252 4.535433 15.87402 re f*') - 1
b = idx('(CHAMP LIBRE) Tj')
del L[a:b + 1]

# 3) bloc « VISAP réalisée par » : déplacé du volet central vers la fiche produit (+586,77 pt en x)
a = idx('(VISAP R\\001ALIS\\001E PAR) Tj') - 1
b = idx('BT 1 0 0 1 1040.031 85.2 Tm')
L.insert(b + 1, 'Q'); L.insert(a, 'q 1 0 0 1 %.4f 0 cm' % (1216.063 - 629.2913))

# 4) cadre « Précisions » raccourci par le bas pour laisser la place au bloc
i = idx('n 1216.063 79.65354 538.5827 111.1181 re S')
L[i] = 'n 1216.063 116 538.5827 %.4f re S' % (79.65354 + 111.1181 - 116)

# 5) titre du volet : il n'y a plus d'observations sur ce volet
i = idx('(4. FICHE TERRAIN - Croquis et observations) Tj')
L[i] = L[i].replace('(4. FICHE TERRAIN - Croquis et observations) Tj', '(4. FICHE TERRAIN - Croquis) Tj')

ns = DecodedStreamObject(); ns.set_data('\n'.join(L).encode('latin-1'))
p[NameObject('/Contents')] = w._add_object(ns.flate_encode())
w.write(dst); print('écrit', dst, '— quadrillages %.0f mm de haut chacun' % (H / 72 * 25.4))
