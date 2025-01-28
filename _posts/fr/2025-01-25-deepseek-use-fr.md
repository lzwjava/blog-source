---
audio: true
lang: fr
layout: post
title: Utilisation de l'API DeepSeek
translated: true
---

## DeepSeek

En un mois, 15 millions de jetons m'ont coûté environ 23,5 CNY.

Voici mon utilisation en un jour :

| Type              | Jetons    |
|-------------------|-----------|
| Entrée (accès cache)  | 946,816   |
| Entrée (manque cache) | 2,753,752 |
| Sortie            | 3,100,977 |

Le calcul est le suivant :

0,94 * 0,1 + 2,75 * 1 + 3,10 * 2 = 11,83

Ainsi, selon la tâche, l'utilisation des jetons dépend largement de l'entrée (manque cache) et de la sortie.

Ce résultat est en accord avec le coût attendu.

[Tarification de l'API DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Source : Capture d'écran personnelle*{: .caption }

## Mistral

Modèle : `mistral-large-2411`

En un jour, mon compte Mistral a consommé les jetons suivants :

| Type   | Jetons  | Coût (USD) |
|--------|---------|------------|
| Total  | 772,284 | 3,44       |
| Sortie | 474,855 | 2,85       |
| Entrée | 297,429 | 0,59       |

La tarification pour Mistral Large est la suivante :

*   Entrée : 2 USD par million de jetons
*   Sortie : 6 USD par million de jetons