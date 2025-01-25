---
audio: true
lang: fr
layout: post
title: Utilisation de l'API DeepSeek
translated: true
---

En un mois, 15 millions de tokens m'ont coûté environ 23,5 CNY.

Voici mon utilisation sur une journée :

| Type              | Tokens    |
|-------------------|-----------|
| Entrée (Cache Hit)  | 946,816   |
| Entrée (Cache Miss) | 2,753,752 |
| Sortie            | 3,100,977 |

Le calcul est le suivant :

0.94 * 0.1 + 2.75 * 1 + 3.10 * 2 = 11.83

Ainsi, selon la tâche, l'utilisation des tokens dépend largement de l'entrée (cache miss) et de la sortie.

Ce résultat correspond au coût attendu.

[Prix de l'API DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/)

{: .centered }
![](assets/images/deepseek/d.jpg){: .responsive }
*Source : Capture d'écran personnelle*{: .caption }