---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Calcul du temps d'attente de réponse du modèle
translated: true
type: note
---

Nous pouvons travailler étape par étape.

D'après l'enregistrement :

* **tokens_completion** = 9532
* Le **throughput** n'est pas indiqué ici, mais vous avez demandé "tokens ÷ tokens par seconde".

La requête indique :

* `generation_time = 203477 ms` → 203,477 secondes
* `tokens_completion = 9532`

Calculons maintenant le débit réel :

$$
\text{tokens par seconde} = \frac{9532}{203,477} \approx 46,8
$$

Ainsi, l'utilisateur a dû attendre environ **203 secondes (\~3 minutes 23 secondes)** pour la réponse.

Si vous connaissez déjà le débit du modèle (tokens/seconde), alors le temps d'attente est simplement :

$$
\text{temps d'attente} = \frac{\text{tokens\_completion}}{\text{tokens par seconde}}
$$

Dans ce cas, le journal fournit déjà les deux côtés (temps et tokens), donc le calcul correspond.

👉 Réponse courte : L'utilisateur a attendu environ **203 secondes (\~3 minutes 23 secondes)** pour les 9532 tokens, à environ 47 tokens/seconde.

Souhaitez-vous que je vous montre également une **formule générale** que vous pouvez réutiliser pour d'autres journaux (en utilisant la latence, le débit et les nombres de tokens) ?