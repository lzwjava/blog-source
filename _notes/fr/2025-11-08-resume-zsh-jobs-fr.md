---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Reprise des travaux suspendus dans zsh
translated: true
type: note
---

Pour reprendre un travail suspendu (comme votre commande `bundle exec jekyll serve --incremental`, qui a probablement été mise en pause avec Ctrl+Z) dans zsh au sein de Ghostty, suivez ces étapes dans la même session de terminal :

1.  Listez tous les travaux en arrière-plan/suspendus pour confirmer sa présence :
    ```
    jobs
    ```
    Cela affichera quelque chose comme `[1]+  Suspendu  bundle exec jekyll serve --incremental`.

2.  Reprenez-le au premier plan (il reprendra le contrôle de votre terminal) :
    ```
    fg
    ```
    - Si vous avez plusieurs travaux, spécifiez celui que vous voulez avec `fg %1` (en remplaçant `1` par le numéro du travail issu de la sortie de `jobs`).

Si vous souhaitez l'exécuter en arrière-plan à la place (pour pouvoir utiliser le terminal pour autre chose pendant qu'il sert), utilisez `bg %1` (là encore, avec le numéro du travail).

Une fois repris, Jekyll devrait reprendre là où il s'était arrêté, en supposant qu'il n'y ait pas eu d'interruption majeure. Si le processus semble bloqué ou génère des erreurs, vous devrez peut-être l'arrêter avec `kill %1` et le redémarrer.