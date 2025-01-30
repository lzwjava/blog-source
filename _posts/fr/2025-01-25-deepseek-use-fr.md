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

| Type              | Jetons    |
|-------------------|-----------|
| Entrée (Cache Hit)| 946,816   |
| Entrée (Cache Miss)| 2,753,752 |
| Sortie            | 3,100,977 |

Le calcul est le suivant :

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

Ainsi, selon la tâche, l'utilisation des jetons dépend largement de l'entrée (cache miss) et de la sortie.

Ce résultat est conforme au coût attendu.

[Tarification de l'API DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Source : Capture d'écran personnelle*{: .caption }

## Mistral

Le tarif des modèles Mistral est le suivant :

| Modèle                 | Entrée (USD par million de jetons) | Sortie (USD par million de jetons) |
|-----------------------|------------------------------|---------------------------------|
| `mistral-large-2411`  | 2                            | 6                               |
| `mistral-small-latest`| 0.2                          | 0.6                             |

En un jour, l'utilisation de mon compte Mistral était la suivante (Modèle : `mistral-large-2411`) :

| Type   | Jetons  | Coût (USD) |
|--------|---------|------------|
| Total  | 772,284 | 3.44       |
| Sortie | 474,855 | 2.85       |
| Entrée | 297,429 | 0.59       |

Pour le modèle `mistral-small-2409`, l'utilisation totale était de 1,022,407 jetons.

En supposant que 1/3 de ces jetons étaient des jetons d'entrée et 2/3 des jetons de sortie :

Il y avait 340,802 jetons d'entrée et 681,605 jetons de sortie.

Par conséquent, le coût total est calculé comme suit : 340,802 * 0.2 / 1,000,000 + 681,605 * 0.6 / 1,000,000 = 0.07 + 0.41 = 0.48 USD.

La console Mistral rapporte un coût total d'utilisation de 0.43 USD, ce qui correspond approximativement à notre calcul.