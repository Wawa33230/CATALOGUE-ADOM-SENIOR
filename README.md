# Catalogue produits — ADOM SENIOR

Ce repo contient le catalogue produits complet d'ADOM SENIOR, décliné en deux formats :

- **`print/`** — la source du catalogue imprimable (PDF), prêt à envoyer à un imprimeur.
- **`web/`** — la version destinée au site adomsenior.fr (repo `Wawa33230/WEB-ADOMSENIOR`), à transmettre telle quelle à ChatGPT pour intégration et déploiement.
- **`dist/catalogue-adomsenior.pdf`** — le PDF A4 (écran, e-mail, impression bureautique).
- **`dist/catalogue-adomsenior-imprimeur.pdf`** — le PDF à envoyer à l'imprimeur : A4 + 3 mm de fonds perdus sur chaque bord (216 × 303 mm), TrimBox/BleedBox renseignées.

La 4e de couverture (page 20) contient un **encart « Votre conseiller ADOM SENIOR »** à remplir à la main par le commercial en rendez-vous (nom, téléphone, e-mail, date du RDV, prochaine étape) avec un emplacement 85 × 55 mm pour agrafer une carte de visite ou apposer un cachet.

Les polices sont embarquées dans `print/fonts/` (Gelasio, équivalent libre de Georgia, et Inter — licence SIL OFL) : le PDF est identique quel que soit l'ordinateur qui le génère.

Structure du catalogue PDF (20 pages — la version web n'a pas encore été synchronisée avec les derniers ajouts, voir section 2) :

1. Couverture
2. Sommaire
3. Présentation d'ADOM SENIOR
4. Notre activité & nos secteurs d'intervention
5. Zones d'intervention — carte des départements (Nord-Ouest, Sud-Ouest, Sud-Est)
6. Receveurs de douche
7. Revêtement mural — avec nuancier détaillé (9 gammes, 36 finitions)
8. Parois de douche
9. Accessoires — barres, siège, robinetterie
10. Travaux complémentaires — lavabo, WC
11. Sols
12. Contact

Un fichier `SITE-WEB-BRIEF.md` à la racine du repo résume l'intégralité du contenu du catalogue (textes, gammes, coordonnées) dans un format pensé pour être transmis directement à ChatGPT afin de reproduire le catalogue sur adomsenior.fr.

## Visuels du catalogue PDF

Sur demande (avec autorisation), les visuels proviennent désormais de deux sources :

- **ltshowertec.com** (fournisseur) : ambiances haute définition (2 000 à 2 500 px) par finition — Slim, Relief, dalles murales, parois, receveurs — et photos produit sur fond blanc (colonne de douche, barre en T).
- **adomsenior.fr** : vraies photos de chantiers ADOM SENIOR (avant/après en page 3, réalisations en page 4, WC suspendu en page 17).

Les images sont utilisées à leur résolution d'origine, sans agrandissement artificiel ; aucune ne porte de filigrane. Les pastilles du nuancier (pages 10–11) ont été découpées une à une dans les planches fournisseur et légendées dans la typographie du catalogue (le « Blanc alpin », gris dans la planche fournisseur, est prélevé sur l'ambiance réelle). Le crédit fournisseur n'apparaît plus qu'une fois, dans les mentions de la 4e de couverture.

## 1. Version PDF (`print/`)

- `catalogue-print.html` : la mise en page complète (20 pages A4), avec les images embarquées dans `print/media/`.
- `build-pdf.mjs` : script Playwright qui reproduit exactement la méthode déjà utilisée par ADOM SENIOR pour ses autres documents (`documents/gen.mjs` dans le repo du site).
- `set-print-boxes.py` : appelé par `build-pdf.mjs`, renseigne la zone de coupe (TrimBox) du PDF imprimeur.

Pour régénérer le PDF après une modification :

```bash
cd print
node build-pdf.mjs
```

Les deux fichiers sont produits dans `dist/` (~23 Mo chacun — poids plus élevé du fait des 36 finitions du nuancier et de la résolution ~300 dpi ; toujours raisonnable pour un envoi à un imprimeur).

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
- **Fiches produit avec références précises** : le catalogue présente les familles avec leurs caractéristiques et gammes réelles, mais sans tableau de références/dimensions détaillé comme dans le PDF fournisseur d'origine. Dites-moi si vous voulez ce niveau de détail (référence, dimensions, poids) repris dans le catalogue ADOM SENIOR.
- **Mentions légales** : SIRET, adresse, téléphone n'apparaissent nulle part sur le site actuel (seul `contact@adomsenior.fr` est public). Je ne les ai donc pas ajoutés au catalogue — à compléter si vous voulez qu'ils apparaissent en pied du PDF.
- **Carte des zones d'intervention** : silhouette de la France simplifiée (approximative, à visée illustrative) et points positionnés à partir de repères géographiques usuels (Pau pour le 64, Rennes pour la Bretagne, Nice) — dites-moi si vous voulez des points plus précis (adresse exacte de vos équipes/agences).
- **Version web** : les ajouts de cette session (nuancier, carte, configurations de parois) n'ont pour l'instant été appliqués qu'à la version PDF, comme les demandes précédentes qui ne concernaient que le PDF. Dites-moi si vous voulez que je les répercute aussi dans `web/catalogue.html`.
