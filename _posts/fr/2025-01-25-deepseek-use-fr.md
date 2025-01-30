---
audio: false
lang: fr
layout: post
title: Utilisation de l'API de Deepseek et Mistral
translated: true
---

## DeepSeek

En un mois, 15 millions de jetons m'ont coûté environ 23,5 CNY.

Voici mon utilisation en un jour :

| Type              | Jeton     |
|-------------------|-----------|
| Entrée (Cache Hit) | 946 816   |
| Entrée (Cache Miss) | 2 753 752 |
| Sortie            | 3 100 977 |

Le calcul est le suivant :

0,94 * 0,1 + 2,75 * 1 + 3,10 * 2 = 11,83

Ainsi, selon la tâche, l'utilisation des jetons dépend largement de l'entrée (cache miss) et de la sortie.

Ce résultat correspond aux coûts attendus.

[Tarification de l'API DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Source : Capture d'écran personnelle*{: .caption }

## Mistral

En un jour, l'utilisation de mon compte Mistral était la suivante (Modèle : `mistral-large-2411`) :

| Type   | Jeton    | Coût (USD) |
|--------|----------|------------|
| Total  | 772 284  | 3,44       |
| Sortie | 474 855  | 2,85       |
| Entrée | 297 429  | 0,59       |

La tarification pour les modèles Mistral est la suivante :

| Modèle                 | Entrée (USD par million de jetons) | Sortie (USD par million de jetons) |
|-----------------------|------------------------------------|------------------------------------|
| `mistral-large-2411`  | 2                                 | 6                                  |
| `mistral-small-latest`| 0,2                               | 0,6                                |