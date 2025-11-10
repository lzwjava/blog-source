---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Modèles Imagen 4 de Vertex AI
translated: true
type: note
---

D'après l'extrait de code que vous avez fourni, vous utilisez `genai.Client` pour interagir avec un modèle de génération d'images sur Vertex AI. Le modèle que vous avez spécifié est `"imagen-4.0-generate-preview-06-06"`.

Voici une analyse de ce qui est nouveau et de ce que ce modèle représente :

### Les derniers modèles de génération d'images sur Vertex AI

Le modèle que vous utilisez, `imagen-4.0-generate-preview-06-06`, fait partie de la dernière famille de modèles **Imagen 4** sur Vertex AI. Cette famille de modèles inclut également :

* **`imagen-4.0-generate-preview-06-06`** : Il s'agit du modèle Imagen 4 standard, offrant un équilibre entre vitesse et qualité.
* **`imagen-4.0-ultra-generate-preview-06-06`** : Cette version "Ultra" est conçue pour une qualité supérieure, mais elle est plus lente et plus coûteuse.
* **`imagen-4.0-fast-generate-preview-06-06`** : Cette variante "Fast" privilégie la vitesse et une faible latence par rapport à la qualité la plus élevée possible.

Ces modèles Imagen 4 constituent une mise à jour significative, s'appuyant sur les versions précédentes telles qu'Imagen 3 et Imagen 2. Les principales fonctionnalités et mises à jour d'Imagen 4 incluent :

* **Une qualité d'image améliorée** : Les nouveaux modèles sont conçus pour générer des images de qualité supérieure par rapport à leurs prédécesseurs.
* **Une prise en charge étendue des ratios d'aspect** : Imagen 4 prend en charge plusieurs ratios d'aspect, notamment `1:1`, `3:4`, `4:3`, `9:16` et `16:9`, vous offrant ainsi plus de contrôle sur le résultat.
* **L'invite multilingue** : Bien que l'anglais soit la langue principale, ces modèles prennent également en charge les invites textuelles dans plusieurs autres langues, notamment le chinois (simplifié et traditionnel), l'hindi, le japonais, le coréen, le portugais et l'espagnol (en preview).
* **Les fonctionnalités de sécurité** : Les modèles incluent des paramètres de sécurité configurables par l'utilisateur et intègrent le tatouage numérique (SynthID) pour identifier le contenu généré par l'IA.

Les paramètres `person_generation` et `safety_filter_level` dans votre extrait de code sont toujours pertinents et vous permettent de configurer le comportement du modèle pour une IA responsable, comme vous l'avez fait avec `person_generation="ALLOW_ADULT"` et `safety_filter_level="BLOCK_LOW_AND_ABOVE"`.

### Au-delà de la génération d'images

En plus des modèles Imagen mis à jour, Google Cloud a également récemment introduit d'autres nouveaux modèles d'IA générative sur Vertex AI, notamment :

* **Veo 3 et Veo 3 Fast** : Il s'agit des derniers modèles de génération vidéo, vous permettant de créer des vidéos de haute qualité à partir d'invites textuelles ou d'images. Veo 3 est destiné aux vidéos professionnelles de haute qualité avec des fonctionnalités comme l'audio natif et le synchronisme labial, tandis que Veo 3 Fast est optimisé pour la vitesse.
* **Les modèles Gemini 2.5** : Il s'agit des dernières versions de la famille de modèles Gemini, incluant Gemini 2.5 Pro, Gemini 2.5 Flash et Gemini 2.5 Flash-Lite, offrant un raisonnement avancé, une multimodalité et des performances améliorées pour diverses tâches.