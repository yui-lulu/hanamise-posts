# Hanamisé · Instagram (@hanamise.albi)

Ce dépôt contient les visuels Instagram de **Hanamisé**, le bar **fictif** que Rayane
imagine pour son diplôme de BP barman. Le compte doit donner l'impression d'un vrai bar
vivant : le jury doit se demander si le bar existe vraiment. Chaque post est pensé
comme s'il était fait par un graphiste payé : riche, détaillé, jamais simpliste.

Le dépôt est public : Metricool récupère les images via leur lien
`https://raw.githubusercontent.com/yui-lulu/hanamise-posts/main/<chemin>`.

## Le bar

- Speakeasy & cocktail lab, influences asiatiques & mixologie moderne. 花見 (hanami) :
  contempler les cerisiers en fleurs. 隠れ家 (kakurega) : le repaire caché.
- Adresse à afficher : **Place du Palais · 81000 Albi**, toujours **sans numéro**
  (le vrai bar où travaille Rayane est au n°2 : ne jamais l'indiquer).
- Horaires : **du mardi au samedi, 17h – 2h**. Fermé dimanche et lundi.
- Ouverture (fictive) : vendredi 23 octobre 2026. Saison 01.
- Mot de passe à la porte : **sakura** (clin d'œil aux speakeasy de la Prohibition).
  Il peut changer chaque mois, annoncé dans un post. Ce post sort tôt dans la journée
  (vers 12h), jamais à 18h : les clients doivent le connaître bien avant l'ouverture.
  Novembre 2026 : à annoncer le mardi 3 novembre.
- Carte : artefact « Carte Hanamisé » https://claude.ai/code/artifact/ccb3eb58-634e-4560-bd9f-31f95a2b842e
  (6 chapitres : L'art du short drink, La sagesse du long drink, Creation Lab &
  Signatures, L'essence sans alcool, Infusions & softs artisanaux, Cuvées &
  fermentations). Pour parler d'un cocktail, prendre ses vrais nom et ingrédients
  dans la carte, ne rien inventer de chiffré (prix, degrés) qui n'y est pas.

## Identité visuelle des posts (format 1080 × 1350)

Inspiration : les affiches d'événements du compte speakeasy_albi (titres massifs
condensés, date énorme, image centrale forte, bande d'infos en bas), mélangées à une
touche japonaise. Pas de fond noir uni façon carte : fonds de couleur.

- Couleurs : crème `#efe7da`, rose sakura `#ff4f9a`, rouge laque `#b8261d`,
  encre `#141414`, rose pâle `#ffc2da` / `#f2a3c3`, crème clair `#f6eadb`.
- Typos : Anton (titres), Cormorant Garamond italique 600 (un mot élégant en
  contraste), Montserrat 700–800 en capitales espacées (infos), Noto Sans JP 900
  (kanji).
- Éléments signature à réutiliser et varier :
  - cadre fin à 36 px + repères d'imprimerie (cercle + croix) aux 4 coins ;
  - barre d'infos en haut (« N°xx / yy », thème, « SAISON 01 ») avec un filet ;
  - logo dans un rond noir, entouré d'un texte circulaire (SVG textPath) et d'une
    trame de points (radial-gradient) ;
  - pétales de sakura en SVG qui tombent par-dessus les couches ;
  - tampon japonais (hanko) carré, légèrement tourné, avec kanji vertical ;
  - grand kanji vertical en fond, texte en contour décalé, bandeau en diagonale,
    ticket d'entrée, bloc horaires façon fiche technique ;
  - grain papier par-dessus tout (`.grain` avec l'asset grain) ;
  - bande noire en bas : « PLACE DU PALAIS · 81000 ALBI · … ».
- Sources de référence : `sources/semaine-01/*.dc.html`.

Textes des posts : en français, courts, chaleureux, un emoji 🌸 au maximum, 4 à 6
hashtags (#Albi #Hanamisé #Speakeasy …). Tout post qui parle d'alcool ou de cocktail
se termine par « L'abus d'alcool est dangereux pour la santé, à consommer avec
modération. » (loi Évin). Jamais de faux avis clients, de faux témoignages, de
personnes réelles nommées, ni de faux partenariats avec de vraies entreprises.

## Où vivent les fichiers

- Canevas Design « Posts Instagram Hanamisé » :
  https://claude.ai/artifact/Ntj67uYmcfHUUbGmMMqxR5 — une rangée d'artboards par
  semaine (semaine N à `y = (N-1) × 1750`, artboards de 1080 × 1350 espacés de 80 px,
  titre `kind: title1` « Semaine N · Thème » à `y = ligne − 280`). Assets déjà
  téléversés : logo `/_blob/302f95d38de2a2e84e8ceba002bed708`, branche
  `/_blob/b75e081c46bfed884d7c8d8b17318ca8`, grain `/_blob/1dfaa85f7b4878d129931caebe89f8e4`.
- `assets/` + `assets/blobs.json` : copies locales des assets (id → fichier). Tout
  nouvel asset téléversé sur le canevas doit aussi être ajouté ici.
- `sources/semaine-NN/` : les `.dc.html` de la semaine (copie des artboards).
- `semaine-NN/` : les JPG publiés.
- Rendu : `python3 tools/render.py semaine-NN sources/semaine-NN/*.dc.html`
  (installe les polices depuis github.com/google/fonts au premier lancement).

## Metricool

- Marque `blogId` **7410965**, compte Instagram **hanamise.albi**, fuseau Europe/Paris.
- Rythme : 3 posts par semaine, les jours d'ouverture (mardi, jeudi, samedi vers
  18h par défaut), en comptant les posts déjà programmés (`getScheduledPosts`).
- Rien n'est publié sans l'accord de Rayane : créer d'abord les posts en
  **brouillon** (`draft: true`), puis passer `draft: false` une fois son OK reçu.

## Parler à Rayane

Français, phrases courtes et claires, peu de jargon (il est dyslexique). Lui montrer
les visuels en images et les textes prêts à lire, puis poser une seule question.
