---
audio: false
generated: true
lang: fr
layout: post
title: Génération de modèles autorégressifs
translated: true
type: note
---

Dans le contexte de modèles comme GPT (Generative Pre-trained Transformer), le terme « autogressif » (autoregressive) désigne la méthode par laquelle le modèle génère des séquences de sortie. Plus précisément, cela signifie que le modèle génère chaque élément d'une séquence un par un, en utilisant ses sorties précédentes comme contexte d'entrée supplémentaire pour générer l'élément suivant.

Voici une explication détaillée du fonctionnement du processus autogressif dans de tels modèles :

1. **Génération Séquentielle** : Le modèle génère du texte de manière séquentielle. Il commence par une entrée initiale (souvent appelée prompt) et génère un token (qui peut être un mot, une partie d'un mot ou un caractère) à la fois.

2. **Dépendance envers les Tokens Précédents** : Pour chaque nouveau token généré, le modèle prend en compte tous les tokens générés précédemment. Cela signifie que la sortie à chaque étape dépend des sorties de toutes les étapes précédentes.

3. **Boucle de Rétroaction** : Le modèle utilise une boucle de rétroaction où la sortie du modèle à l'étape de temps \\( t \\) est réinjectée en entrée à l'étape de temps \\( t+1 \\). Cela permet au modèle de maintenir une cohérence et un contexte sur des séquences plus longues.

4. **Distribution de Probabilité** : À chaque étape, le modèle génère une distribution de probabilité sur les prochains tokens possibles et en sélectionne un en fonction de cette distribution (en utilisant souvent des techniques comme l'échantillonnage ou la sélection du token le plus probable).

En résumé, « autogressif » dans le contexte de GPT et des modèles similaires signifie que le modèle génère des séquences étape par étape, chaque étape dépendant des précédentes, ce qui lui permet de produire un texte cohérent et pertinent dans son contexte.