# Catalogue produits — ADOM SENIOR

Ce repo contient le catalogue produits complet d'ADOM SENIOR, décliné en deux formats :

- **`print/`** — la source du catalogue imprimable (PDF), prêt à envoyer à un imprimeur.
- **`web/`** — la version destinée au site adomsenior.fr (repo `Wawa33230/WEB-ADOMSENIOR`), à transmettre telle quelle à ChatGPT pour intégration et déploiement.
- **`dist/catalogue-adomsenior.pdf`** — le PDF déjà généré, prêt à l'emploi.

Structure du catalogue (identique dans les deux versions) :

1. Présentation d'ADOM SENIOR
2. Notre activité & nos secteurs d'intervention
3. Receveurs de douche
4. Revêtement mural
5. Parois de douche
6. Accessoires — barres, siège, robinetterie
7. Travaux annexes — lavabo, WC

## Visuels : source unique, le catalogue fournisseur LT Showertec

Sur demande explicite, **aucune photo du site adomsenior.fr n'est réutilisée** (ni les vraies photos de chantiers, ni les rendus 3D déjà publiés en ligne), pour éviter tout doublon entre le catalogue produits et le reste du site.

Tous les visuels (21 images) proviennent du **catalogue fournisseur LT Showertec** que vous avez transmis (`Catalogue_LT_SHOWERTEC.pdf`) : photos produit détourées (robinetterie, barre en T, siège) et rendus d'ambiance de salle de bain (receveurs Futura/Moderna/Slim, panneaux Relief, dalles murales, parois pliantes, meuble vasque). Chaque image a été extraite proprement du PDF fournisseur (fond blanc restitué, pas de fond noir parasite) puis réutilisée une seule fois dans tout le document — zéro répétition.

Les gammes citées (Slim, Futura, Moderna, Design pour les receveurs ; Relief et dalles clipsables pour les murs ; parois pliantes Intimity ; barres en T ; sièges Design) sont les gammes réellement commercialisées par LT Showertec, telles que documentées dans leur catalogue.

**Netteté des visuels** : certaines photos sources sont plus petites que la zone qu'elles remplissent dans la mise en page (notamment les fonds pleine page des séparateurs de section). `print/prepare-media.py` reprend chaque photo, l'agrandit en Lanczos jusqu'à 3200 px de long côté (~300 dpi sur une page A4 pleine) puis applique un renforcement de netteté (unsharp mask) pour compenser le flou inhérent à l'agrandissement — sans recadrer ni modifier le contenu. Export en `.jpg` qualité 96. Cela reste un agrandissement algorithmique : sur les textures très douces (ex. béton ciré en fond de page de garde), un zoom extrême (>250 %) dans le PDF peut encore laisser deviner un léger flou — c'est la limite physique de la photo source (max ~1300 px de large dans le catalogue LT fourni), pas un réglage à corriger. Pour une netteté parfaite à très fort zoom sur ces images précises, il faudrait un fichier source encore plus défini auprès de LT Showertec.

**Bugs corrigés** :
- Page « Qui sommes-nous » (page 3) : les deux photos débordaient parfois sur le bas de page à cause d'un souci de calcul de hauteur en grille CSS — corrigé.
- Séparateurs de section et page de contact (pages 5, 7, 9, 11, 13, 15, 17) : les images de fond utilisaient une transparence (`opacity`) directement sur la photo, ce que certains lecteurs PDF mobiles ne savent pas restituer et qui les rendait invisibles à l'écran (l'assombrissement se fait maintenant uniquement via le calque de couleur superposé, la photo elle-même reste pleinement opaque — plus fiable sur tous les lecteurs).
- Page Accessoires (page 12) : le set de douche et la barre en T étaient recadrés/tronqués par le format de la vignette ; ils s'affichent maintenant en entier (sur fond blanc, sans recadrage).

## 1. Version PDF (`print/`)

- `catalogue-print.html` : la mise en page complète (17 pages A4), avec les images embarquées dans `print/media/`.
- `build-pdf.mjs` : script Playwright qui reproduit exactement la méthode déjà utilisée par ADOM SENIOR pour ses autres documents (`documents/gen.mjs` dans le repo du site).
- `prepare-media.py` : à relancer depuis `print/media/` après avoir ajouté ou remplacé une photo source (`.png`), avant de régénérer le PDF.

Pour régénérer le PDF après une modification :

```bash
cd print
node build-pdf.mjs
```

Le fichier est produit dans `dist/catalogue-adomsenior.pdf` (~7 Mo).

**Charte graphique reprise à l'identique** de vos documents existants (`pv-reception-adomsenior.html`, `notice-entretien-adomsenior.html`) : bleu profond `#0e4c5a`, ambre `#d98a3d`/`#e7a551`, titres en serif (Iowan Old Style / Georgia), logo maison.

## 2. Version web (`web/catalogue.html`)

Un **fichier HTML unique et autonome**, à transmettre tel quel à ChatGPT avec l'instruction :

> « Intègre ce fichier comme nouvelle page `/catalogue/index.html` sur le site adomsenior.fr (repo Wawa33230/WEB-ADOMSENIOR), copie le dossier `web/media/catalogue/` dans `public/media/catalogue/`, et ajoute un lien "Catalogue" dans la navigation du header, entre "La solution" et "Réalisations". »

Points importants :

- Le fichier **réutilise à 100 % les classes CSS déjà définies** dans `src/styles.css` du site (header, nav, `section`, `card-grid`, boutons, `.reveal`, etc.) et le script partagé `src/main.js` (thème clair/sombre, menu mobile, animations au scroll, formulaire de contact). **Aucune modification de `main.js` ou `styles.css` n'est nécessaire.**
- Il ajoute son propre `<style>` (styles complémentaires uniquement, aucune redéfinition) et un petit `<script type="module">` en bas de page, autonome, pour :
  - une **galerie « produit animé »** par famille de produits (identique dans l'esprit à celle déjà présente sur la page d'accueil), avec vignettes cliquables et rotation automatique ;
  - une **sous-navigation collante** avec les 5 catégories, dont l'onglet actif se met à jour automatiquement au scroll (scrollspy).
- **16 nouvelles images** sont fournies dans `web/media/catalogue/` — à copier dans `public/media/catalogue/` du repo du site avant déploiement (elles n'existent pas encore sur adomsenior.fr).
- Testé en conditions réelles avec le vrai `styles.css` du site (rendu conforme à la charte).

### Vidéos produit (prêt, mais pas encore alimenté)

Chaque bloc `[data-catalogue-story]` peut accueillir une vidéo à la place d'une photo (le script gère déjà la lecture au clic). Voir le commentaire dans la section « Receveurs de douche » du fichier. **Il manque les fichiers vidéo eux-mêmes** — dès que vous en avez (ex. time-lapse de pose, vidéo produit LT Showertec avec droits d'usage), transmettez-les et j'intègre les emplacements réels.

## 3. Ce qui a servi de base

- Le site `adomsenior.fr` (repo `Wawa33230/WEB-ADOMSENIOR`, cloné en lecture seule pour cette mission) : présentation de l'activité, secteurs d'intervention, charte graphique et méthode déjà en place.
- Le catalogue fournisseur `Catalogue_LT_SHOWERTEC.pdf` que vous avez transmis : contenu produit détaillé (caractéristiques techniques, gammes, finitions) et l'intégralité des visuels du catalogue.
- Accès direct à `ltshowertec.com` et `akw.fr` bloqué par le proxy réseau de cet environnement — sans impact, le PDF fournisseur transmis contenait tout le nécessaire (et davantage) pour construire un catalogue fidèle et visuel.

## 4. Ce qu'il reste à trancher avec vous

- **Tarifs** : volontairement absents (mention « sur devis personnalisé » partout). Dites-moi si vous voulez afficher des tarifs indicatifs par gamme.
- **Fiches produit avec références précises** : le catalogue présente les 5 familles avec leurs caractéristiques et gammes réelles, mais sans tableau de références/dimensions détaillé comme dans le PDF fournisseur d'origine. Dites-moi si vous voulez ce niveau de détail (référence, dimensions, poids) repris dans le catalogue ADOM SENIOR.
- **Mentions légales** : SIRET, adresse, téléphone n'apparaissent nulle part sur le site actuel (seul `contact@adomsenior.fr` est public). Je ne les ai donc pas ajoutés au catalogue — à compléter si vous voulez qu'ils apparaissent en pied du PDF.
