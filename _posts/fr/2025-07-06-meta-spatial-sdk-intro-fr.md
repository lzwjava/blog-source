---
audio: false
generated: true
lang: fr
layout: post
title: 'Kit de développement spatial Meta : Android vers XR'
translated: true
type: note
---

Le **Meta Spatial SDK** est un changement de paradigme pour les développeurs cherchant à créer des applications immersives pour les casques VR/MR de Meta, spécifiquement ceux exécutant **Meta Horizon OS** (comme la série Meta Quest). Son objectif principal est de combler le fossé entre le développement traditionnel d'applications mobiles Android et les capacités uniques du calcul spatial.

Voici une introduction concise au Meta Spatial SDK :

**Qu'est-ce que c'est ?**

Le Meta Spatial SDK est un nouveau framework qui permet aux développeurs Android de tirer parti de leurs compétences, outils et bibliothèques existants (comme Android Studio et Kotlin) pour créer des expériences riches, immersives et de réalité mixte sur les appareils Meta Quest. Avant ce SDK, le développement pour Quest nécessitait souvent l'utilisation d'un moteur de jeu complet comme Unity ou Unreal, ce qui pouvait représenter un obstacle significatif pour les développeurs orientés mobile.

**Objectifs et Avantages Clés :**

* **Démocratiser le Développement XR :** Il abaisse la barrière à l'entrée pour les développeurs mobiles, permettant à un plus large éventail de créateurs de construire pour le calcul spatial.
* **Tirer Parti des Compétences Existantes :** Les développeurs peuvent utiliser leur environnement de développement Android familier, réduisant ainsi les courbes d'apprentissage et accélérant le développement.
* **Étendre les Applications 2D vers la 3D :** Il permet aux développeurs de porter des applications Android 2D existantes vers Meta Horizon OS et de les enrichir avec des éléments 3D, des fonctionnalités de réalité mixte et des interactions spatiales.
* **Itération Rapide :** Le SDK offre un workflow rapide, permettant un prototypage, une construction et des tests plus rapides des idées spatiales.
* **Expérience Utilisateur Améliorée :** Il facilite la création d'applications qui vont au-delà des écrans plats traditionnels, offrant des fonctionnalités telles que le rendu 3D, la vidéo en transparence (passthrough), le suivi des mains, l'audio spatial et la physique pour des interactions plus engageantes.

**Fonctionnalités et Capacités Principales :**

* **Développement Android Natif :** Construit sur Kotlin, il s'intègre parfaitement à l'écosystème Android.
* **Fonctionnalités de Réalité Mixte :** Accès à la caméra de transparence (Camera2 API) permettant de fusionner le contenu virtuel avec le monde réel.
* **Rendu 3D :** Prend en charge les pipelines graphiques modernes, y compris les modèles GLTF, le rendu physiquement réaliste (PBR), les animations et la physique des corps rigides.
* **Panneaux Interactifs :** Permet la création de panneaux d'interface utilisateur 2D dans l'environnement 3D, construits à l'aide de frameworks d'interface utilisateur Android familiers comme Jetpack Compose.
* **Entrées et Interactions :** Fournit des API pour le suivi des mains, l'entrée des contrôleurs et d'autres interactions utilisateur naturelles.
* **Compréhension de la Scène :** Permet aux développeurs d'accéder aux données concernant l'environnement physique de l'utilisateur.
* **Audio Spatial :** Des outils pour incorporer un son spatialisé afin d'améliorer l'immersion.
* **Meta Spatial Editor :** Un outil compagnon qui permet aux développeurs d'agencer et de composer visuellement des éléments 2D et 3D dans leurs applications spatiales sans avoir besoin d'un éditeur de moteur de jeu complet.
* **Entity-Component-System (ECS) :** Un modèle architectural utilisé au sein du SDK pour construire des applications spatiales modulaires et performantes.

En substance, le Meta Spatial SDK permet aux développeurs Android de franchir facilement le pas vers le monde de la réalité virtuelle et mixte, transformant les applications mobiles traditionnelles en expériences spatiales captivantes sur les appareils Meta Quest.