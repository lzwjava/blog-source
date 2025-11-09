---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: API Tinker Simplifie l'Affinage des Modèles
translated: true
type: note
---

Tinker est une nouvelle API flexible lancée par Thinking Machines AI pour le fine-tuning de modèles de langage. Elle est conçue pour permettre aux chercheurs, développeurs et "hackers" d'expérimenter avec des modèles à poids ouverts (aussi bien les grands modèles comme Qwen-235B-A22B que les plus petits) tout en leur donnant un contrôle total sur les algorithmes et les données. Le service gère les aspects complexes de l'entraînement distribué—comme l'ordonnancement, l'allocation des ressources et la reprise sur erreur—sur leurs clusters internes, en utilisant des techniques comme LoRA pour le rendre efficace et économique.

Points clés :
- **Facilité d'utilisation** : Changez de modèle avec simplement une chaîne de caractères dans votre code Python.
- **Primitives d'API** : Des outils de bas niveau comme `forward_backward` et `sample` pour les méthodes courantes de post-training.
- **Support open-source** : Livré avec la bibliothèque Tinker Cookbook sur GitHub, proposant des implémentations modernes des techniques de fine-tuning.
- **Objectif** : Simplifie la recherche sur les modèles de pointe, en réduisant les problèmes d'infrastructure pour que vous puissiez vous concentrer sur l'innovation.

Il est actuellement en bêta privée (gratuit pour commencer, avec une tarification à l'usage prévue prochainement), et vous pouvez rejoindre la liste d'attente sur [thinkingmachines.ai/tinker](https://thinkingmachines.ai/tinker). Les premiers utilisateurs incluent des équipes de Princeton, Stanford, Berkeley et Redwood Research.

[Annonce de Tinker](https://thinkingmachines.ai/blog/announcing-tinker/)