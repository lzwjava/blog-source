---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Temps d'exécution maximum d'un job GitHub Actions
translated: true
---

J'utilise GitHub Actions pour automatiser la traduction de mes articles de blog. Au départ, j'ai essayé de traduire tous les articles en une seule tâche, en validant les modifications dans le dépôt uniquement après que toutes les traductions étaient terminées.

J'étais optimiste et je suis allé dormir en m'attendant à ce que le processus se termine. Cependant, après 8 heures, je me suis réveillé pour découvrir l'erreur suivante :

> Le job exécuté sur le runner GitHub Actions 12 a dépassé le temps d'exécution maximum de 360 minutes.

Cela signifiait que les 6 heures de travail de traduction étaient perdues, car la validation n'avait lieu qu'à la fin.

Pour résoudre ce problème, j'ai modifié le workflow pour valider les modifications tous les 10 fichiers.

De plus, j'ai mis en place une programmation multithread pour réduire le temps total de traduction de 6 heures à environ une heure.

GitHub Actions offre une grande flexibilité. Il prend en charge plusieurs jobs de workflow, permettant de séparer les tâches. Certains jobs peuvent être déclenchés à chaque commit, tandis que d'autres peuvent être déclenchés par différents événements.