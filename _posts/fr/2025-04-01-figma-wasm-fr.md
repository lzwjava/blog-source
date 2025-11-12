---
audio: false
generated: true
lang: fr
layout: post
title: Figma Exploite WebAssembly
translated: true
type: note
---

Figma exploite WebAssembly (Wasm) pour décupler ses performances, ce qui en fait un exemple remarquable de la façon dont cette technologie peut transformer les applications web. Fondamentalement, Figma est un outil de conception collaboratif qui fonctionne principalement dans le navigateur, et il utilise WebAssembly pour exécuter des tâches critiques et gourmandes en performances à des vitesses quasi natives. Voici comment cela fonctionne :

Le moteur de Figma est construit en C++, un langage réputé pour sa vitesse et son efficacité mais qui n'est pas nativement pris en charge par les navigateurs. Pour combler cette lacune, Figma compile son codebase C++ en WebAssembly à l'aide d'Emscripten, une chaîne d'outils qui convertit le C/C++ en binaires Wasm. Ces fichiers `.wasm` sont ensuite chargés dans le navigateur, où ils gèrent les tâches intensives—comme le rendu de graphiques vectoriels complexes, la gestion de documents de conception volumineux et le traitement des mises à jour en temps réel entre plusieurs utilisateurs.

Un grand avantage de cette approche est le **temps de chargement**. Figma a rapporté que le passage à WebAssembly a réduit son temps de chargement de plus de 3 fois par rapport à son utilisation antérieure d'asm.js (un sous-ensemble de JavaScript pour exécuter du code C++). Le format binaire de WebAssembly est plus compact et plus rapide à analyser que JavaScript, et une fois chargé, le navigateur met en cache le code machine compilé, ce qui rend les chargements suivants encore plus rapides. Ceci est crucial pour Figma, où les utilisateurs jonglent souvent avec des fichiers volumineux et s'attendent à une réactivité instantanée.

Le **moteur de rendu** est un autre domaine clé où WebAssembly excelle. Figma utilise WebGL pour les graphiques accélérés par GPU, mais la logique qui pilote cela—comme le rendu des courbes, le masquage, les flous et les modes de fusion—est gérée par le code C++ compilé en Wasm. Cette configuration contourne le pipeline de rendu HTML du navigateur, donnant à Figma un contrôle affiné sur les performances et la cohérence entre les plateformes. C'est pourquoi le zoom et le panoramique dans Figma sont si fluides, même avec des milliers de calques.

La **collaboration en temps réel** en bénéficie également. Les fonctionnalités multijoueurs de Figma reposent sur les Conflict-Free Replicated Data Types (CRDTs) pour synchroniser instantanément les modifications entre les utilisateurs. Bien que la logique CRDT elle-même ne s'exécute pas entièrement en Wasm, le moteur alimenté par C++ gère efficacement l'état du document et les mises à jour, garantissant que les modifications collaboratives ne ralentissent pas le système. La vitesse de WebAssembly contribue à maintenir cette fluidité, même avec des dizaines de collaborateurs.

Une architecture hybride est ici à l'œuvre : le moteur central (C++/Wasm) gère le document et le canevas, tandis que l'interface utilisateur environnante—comme les barres d'outils et les menus—est construite avec JavaScript (maintenant TypeScript + React). Les deux communiquent via un pont, Wasm exportant des fonctions que JavaScript peut appeler, et vice versa. Cette division permet à Figma d'optimiser les performances là où cela compte le plus, tout en conservant la flexibilité web-native de JavaScript pour les tâches moins intensives en calcul.

Un bémol : Figma n'utilise pas WebAssembly de manière uniforme sur tous les navigateurs. Historiquement, il s'appuyait davantage sur Wasm dans Firefox en raison de bogues précoces de Chrome (par exemple, l'absence de mise en cache pour le code Wasm traduit), bien que les implémentations modernes aient probablement résolu ce problème. Néanmoins, le pipeline C++-vers-Wasm reste central dans son architecture.

En bref, Figma utilise WebAssembly pour apporter des performances de niveau desktop au navigateur, en compilant son cœur C++ en binaires efficaces qui gèrent le rendu, la gestion des documents et la synchronisation en temps réel. C'est un cas d'école montrant comment Wasm permet à une application web de surpasser largement les capacités de JavaScript. Vous voulez approfondir les détails techniques ou voir comment cela se compare à d'autres outils ?