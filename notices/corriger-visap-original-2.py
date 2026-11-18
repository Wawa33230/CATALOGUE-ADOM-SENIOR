# Étape 2 (à lancer après corriger-visap-original.py).
# Usage : python3 corriger-visap-original-2.py VISAP-corrige.pdf VISAP-corrige-2.pdf
# Fiche produit (volet 3 intérieur) du VISAP d'origine :
#  - supprime les champs en doublon avec la fiche terrain (bénéficiaire, bailleur, téléphone, adresse, ville)
#    et garde une seule ligne Date / Établie par / Étage ;
#  - remonte la suite de la fiche et agrandit d'autant le cadre « Précisions » ;
#  - éloigne « Coloris : » de « Receveur — L × P : ».
import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, DecodedStreamObject
src, dst = sys.argv[1], sys.argv[2]
r = PdfReader(src); w = PdfWriter(clone_from=r); p = w.pages[1]
L = p['/Contents'].get_object().get_data().decode('latin-1').split('\n')

def idx(s, start=0):
    hits = [i for i, l in enumerate(L) if s in l and i >= start]
    assert hits, s
    return hits[0]

# 1) Ligne d'identification réduite à Date / Établie par / Étage
start = idx('BT 1 0 0 1 1216.063 734.1732 Tm') - 1          # couleur avant BÉNÉFICIAIRE
end = idx('n 1670.216 688.8189 m 1754.646 688.8189 l S')    # ligne d'écriture ÉTAGE
lab = '.058824 .392157 .439216 rg'; ln = '.788235 .847059 .858824 RG\n.5 w'
new = [
    lab, 'BT 1 0 0 1 1216.063 734.1732 Tm /F2+0 7 Tf 8.4 TL (DATE :) Tj T* ET',
    ln, 'n 1245.063 731.9055 m 1400 731.9055 l S',
    lab, 'BT 1 0 0 1 1426 734.1732 Tm /F2+0 7 Tf 8.4 TL (\\001TABLIE PAR :) Tj T* ET',
    ln, 'n 1482.6 731.9055 m 1614.614 731.9055 l S',
    lab, 'BT 1 0 0 1 1636.157 734.1732 Tm /F2+0 7 Tf 8.4 TL (\\001TAGE :) Tj T* ET',
    ln, 'n 1670.216 731.9055 m 1754.646 731.9055 l S',
]
L[start:end + 1] = new

# 2) « Coloris : » éloigné de L × P
i = idx('(Receveur \\012 L \\005 P :          Coloris :) Tj T* ET')
L[i] = L[i].replace('(Receveur \\012 L \\005 P :          Coloris :) Tj T* ET', '(Receveur \\012 L \\005 P :) Tj T* ET')
L.insert(i + 1, 'BT 1 0 0 1 1372 646.2992 Tm /F3+0 7 Tf 8.4 TL (Coloris :) Tj T* ET')

# 3) Remonter Configuration retenue -> titre Précisions de 2 lignes (43,09 pt), agrandir le cadre Précisions
DY = 734.1732 - 691.0866
a = idx('CONFIGURATION RETENUE') - 1
b = idx('CISIONS / PRODUITS SP')
L.insert(b + 1, 'Q'); L.insert(a, 'q 1 0 0 1 0 %.4f cm' % DY)
box = 'n 1216.063 79.65354 538.5827 68.0315 re S'
j = idx(box); L[j] = 'n 1216.063 79.65354 538.5827 %.4f re S' % (68.0315 + DY)

ns = DecodedStreamObject(); ns.set_data('\n'.join(L).encode('latin-1'))
p[NameObject('/Contents')] = w._add_object(ns.flate_encode())
w.write(dst); print('écrit', dst)
