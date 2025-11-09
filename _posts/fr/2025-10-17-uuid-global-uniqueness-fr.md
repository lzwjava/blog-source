---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Les UUID garantissent l'unicité globale sans coordination
translated: true
type: note
---

Les UUID peuvent servir à l'identification globalement unique sans autorité centrale car ils sont conçus avec un espace d'adressage énorme : 128 bits, fournissant environ 3,4 × 10^38 valeurs possibles. Ce nombre est bien plus grand que le nombre d'UUID qui seront jamais générés dans des scénarios pratiques à travers tous les systèmes mondiaux. Pour les UUID de version 4 (les UUID aléatoires, comme celui que vous avez partagé), 122 de ces bits sont remplis avec des données aléatoires de haute qualité, rendant les doublons extrêmement improbables.

Concernant les collisions : Oui, en théorie, il est possible que deux UUID soient identiques, mais la probabilité est si faible qu'elle est effectivement nulle pour une utilisation réelle. Ceci suit le "paradoxe des anniversaires" en probabilité — les collisions deviennent plus probables à mesure que le nombre d'éléments augmente, mais même dans ce cas :

- La chance que deux UUID aléatoires de version 4 entrent en collision est d'environ 1 sur 2,71 × 10^18.
- Vous auriez besoin de générer environ 4,8 × 10^18 UUID (c'est-à-dire que chaque personne sur Terre en posséderait environ 600 millions) pour avoir 50 % de chance d'avoir ne serait-ce qu'*un* doublon.
- Pour contextualiser, même générer 1 billion (10^12) d'UUID donne un risque de collision d'environ 1 sur un milliard ou moins.

Les différentes versions d'UUID ajoutent des garanties : la version 1 utilise des horodatages et des adresses MAC, la version 5 hache des noms avec des espaces de noms, etc. Mais la seule randomisation de la version 4 garantit l'unicité dans les systèmes distribués, les bases de données ou les applications sans coordination.

[Quelles sont les probabilités ?](https://jhall.io/archive/2021/05/19/what-are-the-odds/)  
[Identifiant universellement unique - Wikipédia](https://fr.wikipedia.org/wiki/Universally_unique_identifier)  
[Quelle est la probabilité d'une collision avec Java UUID.randomUUID ?](https://stackoverflow.com/questions/24876188/how-big-is-the-chance-to-get-a-java-uuid-randomuuid-collision)