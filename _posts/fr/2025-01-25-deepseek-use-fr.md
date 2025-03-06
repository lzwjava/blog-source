---
audio: false
generated: false
lang: fr
layout: post
title: Usage de l'Api de Deepseek et Mistral
translated: true
---

## DeepSeek

En un mois, 15 millions de tokens m'ont coûté environ 23,5 CNY.

Voici mon utilisation en une journée :

| Type              | Tokens    |
|-------------------|-----------|
| Entrée (Cache Hit)  | 946,816   |
| Entrée (Cache Miss) | 2,753,752 |
| Sortie            | 3,100,977 |

Le calcul est le suivant :

0,94 * 0,1 + 2,75 * 1 + 3,10 * 2 = 11,83

Ainsi, en fonction de la tâche, l'utilisation des tokens dépend largement de l'entrée (cache miss) et de la sortie.

Ce résultat est en accord avec le coût attendu.

[DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg)
*Source: Self-Screenshot*{: .caption }

## Mistral

La tarification pour les modèles Mistral est la suivante :

| Modèle                 | Entrée (USD par million de tokens) |  Sortie (USD par million de tokens) |
|-----------------------|------------------------------|---------------------------------|
| `mistral-large-2411`  | 2                            | 6                               |
| `mistral-small-latest`| 0,2                          | 0,6                             |

En une journée, mon utilisation du compte Mistral était la suivante (Modèle : `mistral-large-2411`):

| Type   | Tokens  | Coût (USD) |
|--------|---------|------------|
| Total  | 772,284 | 3,44       |
| Sortie | 474,855 | 2,85       |
| Entrée  | 297,429 | 0,59       |

Pour le modèle `mistral-small-2409`, l'utilisation totale était de 1,022,407 tokens.

En supposant que 1/3 de ces tokens étaient des tokens d'entrée et 2/3 étaient des tokens de sortie :

Il y avait 340,802 tokens d'entrée et 681,605 tokens de sortie.

Le coût total est donc calculé comme 340,802 * 0,2 / 1,000,000 + 681,605 * 0,6 / 1,000,000 = 0,07 + 0,41 = 0,48 USD.

La console Mistral rapporte un coût d'utilisation total de 0,43 USD, ce qui correspond approximativement à notre calcul.

## Grok

| Modèle         | Entrée (USD par million de tokens) | Sortie (USD par million de tokens) |
|---------------|------------------------------|---------------------------------|
| `grok-2-latest` | 2                            | 10                              |