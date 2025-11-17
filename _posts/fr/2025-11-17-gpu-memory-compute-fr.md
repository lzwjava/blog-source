---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Mémoire GPU et utilisation du calcul expliquées
translated: true
type: note
---

Ah, c'est un point de confusion fréquent. Le fait que l'utilisation de la mémoire du GPU soit élevée (comme 90% dans votre cas) **ne signifie pas que votre GPU est pleinement utilisé**. L'utilisation de la mémoire et l'utilisation du calcul sont des métriques liées mais distinctes. Voici pourquoi vous observez cela :

1. **Le modèle et l'optimiseur consomment beaucoup de mémoire**

   * Votre modèle de 125 millions de paramètres + l'optimiseur Adam + les gradients + les tampons temporaires peuvent facilement occuper **la majeure partie de la mémoire du GPU**, surtout sur les GPU avec 12 Go comme votre 4070.
   * Il s'agit de **mémoire allouée**, pas de calcul actif.

2. **Petit modèle = faible utilisation des FLOPs**

   * Même si presque toute la mémoire est utilisée, l'**utilisation réelle du calcul (MFU)** peut rester faible parce que les opérations sont petites. Le GPU ne fait pas assez de calculs parallèles pour saturer tous les cœurs.

3. **Fragmentation et mise en cache de la mémoire**

   * PyTorch (ou CUDA) **pré-alloue ou met souvent en cache la mémoire** pour éviter des allocations répétées. Ainsi, la barre de mémoire semble pleine même si une partie n'est pas activement utilisée à cet instant.

4. **Impact de la taille du lot (batch size)**

   * Des lots plus grands augmentent à la fois l'utilisation de la mémoire **et** l'utilisation du calcul. Mais si votre lot est petit, la mémoire est surtout occupée par les paramètres statiques du modèle et les états de l'optimiseur, et non par un calcul intensif réel.

Donc, dans votre cas :

* ~90% d'utilisation de la mémoire = normal pour un modèle + un optimiseur sur un GPU de 12 Go.
* ~10% de MFU = normal pour un petit modèle avec de petits lots — le GPU attend de petites multiplications matricielles au lieu de traiter d'énormes matrices.

Si vous le souhaitez, je peux décomposer **approximativement la quantité de mémoire que chaque partie (modèle, optimiseur, gradients, etc.) prend** pour votre modèle NanoGPT de 125M. C'est très instructif.