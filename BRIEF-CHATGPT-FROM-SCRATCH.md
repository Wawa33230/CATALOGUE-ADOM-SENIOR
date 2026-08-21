# Brief — Création du catalogue produits ADOM SENIOR (à partir de zéro)

> Ce document rassemble l'ensemble des éléments, faits et demandes exprimés pour la création d'un catalogue produits pour ADOM SENIOR. Il ne contient aucune mise en page, texte rédigé ou choix créatif déjà réalisé — c'est un cahier des charges brut, à toi de proposer ta propre structure, ta rédaction et ta direction artistique.
>
> **Documents à joindre en pièce jointe en même temps que ce brief** (indispensables, ils contiennent les données produit et les visuels) :
> - `Catalogue_LT_SHOWERTEC.pdf` — catalogue complet du fournisseur principal (68 pages) : fiches produits, caractéristiques techniques, gammes, visuels 3D.
> - `Nos_panneaux_2_1.pdf` — document dédié aux panneaux muraux : 9 gammes, 36 finitions avec visuels couleur.

## 1. L'entreprise

**ADOM SENIOR** est une société spécialisée dans l'adaptation de salles de bain pour les seniors et les personnes à mobilité réduite (PMR) : transformation de baignoires en douches sécurisées, à domicile.

- Site web actuel : **adomsenior.fr** (repo `Wawa33230/WEB-ADOMSENIOR`, à gérer via ChatGPT Plus, sans accès dev direct).
- L'entreprise dispose déjà d'une charte graphique et de documents existants (PV de réception, notice d'entretien) utilisant :
  - Couleurs : bleu profond `#0e4c5a`, ambre `#d98a3d` / `#e7a551`, fond sable `#f5f1ea`, fond papier `#fffdf8`, ligne `#e1ddd2`.
  - Typographies : titres en serif (Iowan Old Style / Georgia), texte courant en sans-serif système (-apple-system, Segoe UI, Roboto, Helvetica, Arial).
  - Logo maison déjà existant.
- Fournisseur principal des produits : **LT Showertec** (site : ltshowertec.com).
- Référence de style/qualité perçue citée explicitement par le client : **akw.fr** — « j'aime bien ce style et le rendu pro qu'il y a ».

### Chantiers types / promesse

- Intervention rapide : douche prête à vivre après un délai de séchage court (~36h évoqué comme donnée technique, à ne pas forcément mettre en avant textuellement).
- Travaux « sur mesure, au millimètre ».
- Interventions « sans casser » (pas de gros œuvre).
- Conformité **SS4** : l'entreprise dispose de modes opératoires permettant des interventions en **SS4 niveau d'empoussièrement 1** (relatif à l'amiante).
- Cible **bailleurs sociaux** : argument du **dégrèvement TFPB** (taxe foncière sur les propriétés bâties) pour ce public, et **suivi numérique via portail client InterFast**.
- Cible **patrimoine & amiante** : capacité à intervenir sur bâti ancien avec gestion du risque amiante (cf. SS4 ci-dessus).
- **Pas de tarifs affichés** — mention type « sur devis personnalisé » partout où le prix pourrait être attendu.

## 2. Zones d'intervention

Trois zones/points de rayonnement de l'activité, avec un rayon d'intervention d'environ **250 km** autour de chacun :

- **64 / Pyrénées-Atlantiques** (Sud-Ouest)
- **Bretagne** (Nord-Ouest)
- **Nice** (Sud-Est)

Formulation synthétique demandée pour désigner ces zones : **Sud-Ouest / Sud-Est / Nord-Ouest**.

But demandé : illustrer ces zones sur une carte de France (couverture géographique réelle, pas juste une liste textuelle).

## 3. Structure imposée du catalogue

Le catalogue doit suivre cet ordre logique de catégories produits, imposé par le client :

1. **Receveurs de douche**
2. **Revêtement mural**
3. **Parois de douche**
4. **Accessoires** (barres, siège, robinetterie)
5. **Travaux annexes** (remplacement lavabo, remplacement WC)
6. **Sols**

En plus des pages produits, le catalogue doit inclure une présentation de la société, de son activité et de ses secteurs d'intervention.

## 4. Exigence visuelle générale

- Le catalogue doit être **très visuel** : plusieurs photos/rendus pour chaque produit, pas seulement du texte.
- **Contrainte forte et non négociable : aucune photo déjà utilisée sur le site adomsenior.fr ne doit être réutilisée** dans le catalogue (ni photos de chantiers réels, ni rendus 3D déjà publiés en ligne) — objectif : éviter tout effet de doublon entre le catalogue et le reste du site.
- Les visuels doivent provenir des **rendus 3D du catalogue fournisseur LT Showertec** (`Catalogue_LT_SHOWERTEC.pdf`) — c'est la source à utiliser pour illustrer les produits, pas des photos de chantier.
- Exigence de netteté : les visuels utilisés doivent être nets, non pixelisés, non flous — qualité d'impression professionnelle (le PDF est destiné à être envoyé chez un imprimeur pour fabriquer un vrai catalogue papier).
- Éviter de répéter deux fois la même image dans le document.

## 5. Détails produits par catégorie (à extraire/vérifier dans les PDF fournisseur joints)

### 5.1 Receveurs de douche
- Plusieurs gammes existent chez LT Showertec (ex. gammes à recouper/adapter aux dimensions de la douche existante). Extraire du PDF fournisseur les gammes réellement commercialisées, leurs caractéristiques (antidérapance, finitions de surface, dimensions/recoupe) et les visuels 3D correspondants.
- Le client a explicitement demandé de **ne pas inclure** de gamme « à carreler » (receveur destiné à être carrelé) dans le catalogue final — cette gamme existe dans la doc fournisseur mais ne doit pas être mise en avant.

### 5.2 Revêtement mural (panneaux muraux)
- Utiliser le document `Nos_panneaux_2_1.pdf` comme source des gammes et couleurs : **9 gammes**, **36 finitions** au total.
- Format des panneaux : grand format (ordre de grandeur ~2,50 m × 1,20 m — à vérifier précisément dans la doc fournisseur), posables sans dépose du carrelage existant (pose sur l'existant, sans « casser »).
- Le client veut que **chaque gamme soit illustrée avec ses différentes couleurs/finitions disponibles**, avec les visuels réels des coloris (nuancier complet), en reprenant les visuels du document fournisseur — pas des couleurs génériques recréées à la main.
- Attention lors de l'extraction : dans `Nos_panneaux_2_1.pdf`, bien vérifier l'association exacte entre chaque visuel de couleur et le nom de sa gamme (le client a signalé que des couleurs « aspect béton » avaient été mal associées à une gamme lors d'un premier essai — elles appartiennent en réalité à la gamme **Design** et non **Futura**). Vérifier soigneusement chaque association gamme ↔ finition avant de livrer.

### 5.3 Parois de douche
- Plusieurs typologies à couvrir : **parois fixes**, **parois avec volet/porte rabattable**, **portes coulissantes**, configurations avec **parois pliantes**.
- Le client a mentionné une gamme/finition **Intimity** (à vérifier/détailler dans le PDF fournisseur).
- Le client a insisté sur le fait que l'offre inclut aussi des **parois coulissantes** — à ne pas oublier dans la présentation de cette catégorie.
- (Un essai de schémas de configuration en vue de dessus a été tenté en interne et rejeté comme peu fidèle/peu réaliste par le client — si un support visuel de configurations est envisagé, s'assurer qu'il reste fidèle aux configurations réellement proposées par le fournisseur et physiquement réalisables ; ne pas inventer de configurations non standards.)

### 5.4 Accessoires
- Barres d'appui/de maintien, dont une **barre en T** (barre d'angle avec une partie horizontale servant de main courante — bien montrer l'intégralité de la barre, y compris la partie basse horizontale, dans tout visuel utilisé).
- Siège de douche (gamme « Design » évoquée dans la doc fournisseur, à vérifier).
- Robinetterie.
- Le client souhaite mettre en avant un **ciel de pluie complet** (colonne de douche avec grande pomme de douche « pluie »), pas seulement un simple set de douche classique — argument : plus apprécié par les particuliers que le kit basique.

### 5.5 Travaux annexes
- Remplacement de lavabo.
- Remplacement de WC.
- (Contenu à construire à partir de la doc fournisseur si elle couvre ces éléments, sinon à rédiger simplement comme prestations complémentaires proposées par ADOM SENIOR.)

### 5.6 Sols
- Revêtement de sol **PVC clipsable** (pose sur l'existant), proposé notamment dans des finitions **chêne blanchi** et **gris ciment**.
- Attention : ne pas illustrer cette catégorie avec un visuel de sol carrelé — le produit réellement posé par l'entreprise est du PVC clipsable, pas du carrelage. Utiliser uniquement des visuels fidèles au produit réel (chêne blanchi ou gris ciment), et vérifier qu'ils sont nets avant de les utiliser.

## 6. Contraintes de contenu explicitement exprimées par le client

- Pas d'affichage de tarifs (mention « sur devis personnalisé »).
- Pas de mention « Garantie 5 ans » (à ne pas afficher comme argument dans le catalogue).
- Pas de mention légale imposée pour l'instant (SIRET/adresse/téléphone n'apparaissent pas publiquement sur le site actuel, seul `contact@adomsenior.fr` est public) — à confirmer avec le client si des mentions légales doivent apparaître en pied de catalogue.
- Le catalogue doit rester cohérent avec la charte graphique déjà utilisée par l'entreprise sur ses autres documents (voir section 1).

## 7. Livrables attendus

Le client attend **deux formats** :

1. **Un catalogue PDF imprimable**, au format A4, destiné à être envoyé chez un imprimeur pour fabriquer un vrai catalogue papier — donc avec une qualité d'image adaptée à l'impression (haute résolution, pas de compression visible).
2. **Une version web** destinée à être intégrée sur **adomsenior.fr** (repo `Wawa33230/WEB-ADOMSENIOR`). Cette version doit pouvoir être ajoutée au site existant en réutilisant autant que possible les composants/styles déjà en place sur le site (header, navigation, cartes produits, etc.), plutôt que de repartir sur une direction artistique complètement différente.

## 8. Sources disponibles pour construire ce catalogue

- `Catalogue_LT_SHOWERTEC.pdf` (joint) — catalogue complet du fournisseur, contient les fiches techniques et tous les visuels 3D utilisables.
- `Nos_panneaux_2_1.pdf` (joint) — nuancier détaillé des panneaux muraux (9 gammes / 36 finitions).
- Site fournisseur : **ltshowertec.com** (référence produit/contenu).
- Site de référence pour le style visuel/UX souhaité : **akw.fr**.
- Site actuel d'ADOM SENIOR : **adomsenior.fr** (structure, activité, secteurs d'intervention déjà décrits, charte graphique en place).

---

**Objectif de cet exercice** : construire un catalogue complet et cohérent à partir de ces seules informations (sans repartir d'une maquette déjà faite), en respectant strictement l'ordre des catégories imposé (section 3), les contraintes de contenu (section 6) et l'exigence visuelle (section 4).
