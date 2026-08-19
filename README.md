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

## 1. Version PDF (`print/`)

- `catalogue-print.html` : la mise en page complète (15 pages A4), avec les images embarquées dans `print/media/`.
- `build-pdf.mjs` : script Playwright qui reproduit exactement la méthode déjà utilisée par ADOM SENIOR pour ses autres documents (`documents/gen.mjs` dans le repo du site).

Pour régénérer le PDF après une modification :

```bash
cd print
node build-pdf.mjs
```

Le fichier est produit dans `dist/catalogue-adomsenior.pdf`.

**Charte graphique reprise à l'identique** de vos documents existants (`pv-reception-adomsenior.html`, `notice-entretien-adomsenior.html`) : bleu profond `#0e4c5a`, ambre `#d98a3d`/`#e7a551`, titres en serif (Iowan Old Style / Georgia), logo maison.

## 2. Version web (`web/catalogue.html`)

Un **fichier HTML unique et autonome**, à transmettre tel quel à ChatGPT avec l'instruction :

> « Intègre ce fichier comme nouvelle page `/catalogue/index.html` sur le site adomsenior.fr (repo Wawa33230/WEB-ADOMSENIOR), et ajoute un lien "Catalogue" dans la navigation du header, entre "La solution" et "Réalisations". »

Points importants :

- Le fichier **réutilise à 100 % les classes CSS déjà définies** dans `src/styles.css` du site (header, nav, `section`, `card-grid`, boutons, `.reveal`, etc.) et le script partagé `src/main.js` (thème clair/sombre, menu mobile, animations au scroll, formulaire de contact). **Aucune modification de `main.js` ou `styles.css` n'est nécessaire.**
- Il ajoute son propre `<style>` (styles complémentaires only, aucune redéfinition) et un petit `<script type="module">` en bas de page, autonome, pour :
  - une **galerie « produit animé »** par famille de produits (identique dans l'esprit à celle déjà présente sur la page d'accueil), avec vignettes cliquables et rotation automatique ;
  - une **sous-navigation collante** avec les 5 catégories, dont l'onglet actif se met à jour automatiquement au scroll (scrollspy).
- Toutes les images référencées (`/media/...`) sont déjà présentes dans le repo du site — aucun nouvel asset à copier.
- Testé en conditions réelles avec le vrai `styles.css` du site (rendu conforme à la charte, cf. captures fournies en aparté).

### Vidéos produit (prêt, mais pas encore alimenté)

Chaque bloc `[data-catalogue-story]` peut accueillir une vidéo à la place d'une photo (le script gère déjà la lecture au clic). Voir le commentaire dans la section « Receveurs de douche » du fichier. **Il manque les fichiers vidéo eux-mêmes** — dès que vous en avez (ex. time-lapse de pose, vidéo produit LT Showertec avec droits d'usage), transmettez-les et j'intègre les emplacements réels.

## 3. Ce qui a servi de base

- Le site `adomsenior.fr` (repo `Wawa33230/WEB-ADOMSENIOR`, cloné en lecture seule pour cette mission) : présentation de l'activité, secteurs d'intervention, charte graphique, photos réelles de chantiers, et références produit du fournisseur **LT Showertec**.
- Les gammes citées (Slim, Futura, Moderna, Design pour les receveurs ; panneaux vitrés fixes ; panneaux muraux design) sont les gammes réellement commercialisées par LT Showertec — sourcées publiquement, pas inventées.

## 4. Ce qu'il reste à trancher avec vous

- **Tarifs** : volontairement absents (mention « sur devis personnalisé » partout). Dites-moi si vous voulez afficher des tarifs indicatifs par gamme.
- **Fiches produit détaillées** : le catalogue présente les 5 familles avec leurs caractéristiques génériques (celles réellement mises en avant par ADOM SENIOR). Si vous voulez des fiches par référence précise (dimensions, coloris exacts, réf. fournisseur), il faudra les données LT Showertec correspondantes — je n'ai pas pu accéder à ltshowertec.com ni akw.fr directement (bloqués par le proxy réseau de cet environnement) : je me suis basé sur les informations publiques déjà indexées.
- **Photos par produit** : chaque famille a 3 à 4 photos réelles (réalisations ADOM SENIOR + rendus LT Showertec). Si vous avez d'autres visuels fournisseur (notamment pour les accessoires et les travaux annexes, moins couverts sur le site actuel), transmettez-les pour enrichir encore le catalogue.
- **Mentions légales** : SIRET, adresse, téléphone n'apparaissent nulle part sur le site actuel (seul `contact@adomsenior.fr` est public). Je ne les ai donc pas ajoutés au catalogue — à compléter si vous voulez qu'ils apparaissent en pied du PDF.
