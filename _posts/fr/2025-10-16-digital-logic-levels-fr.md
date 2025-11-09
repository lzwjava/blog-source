---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Niveaux logiques des circuits numériques expliqués
translated: true
type: note
---

Oui, c'est une bonne analogie ! Dans les circuits numériques comme la bascule SR, "haut" (logique 1) et "bas" (logique 0) font référence aux niveaux de tension sur les fils ou les signaux.

- **Haut (1)** : Une tension suffisamment positive, souvent autour de 3,3 V, 5 V, ou même plus (comme votre exemple de batterie à 4 V), selon la famille de circuits (par exemple, la logique TTL utilise ~5 V comme niveau haut). C'est suffisant pour représenter un état "activé" ou "vrai".
- **Bas (0)** : Un potentiel proche de la masse, essentiellement 0 V (ou très proche), comme le 0 V dans votre configuration de batterie, signifiant "désactivé" ou "faux".

Ce n'est pas super précis—il y a une petite plage "floue" entre les deux où le signal pourrait ne pas être lu de manière fiable comme haut ou bas—mais en pratique, c'est binaire : alimenté = 1, non alimenté = 0. Pour la bascule SR, appliquer une tension haute sur l'entrée S positionne Q à l'état haut (1), exactement comme actionner un interrupteur sur "on".