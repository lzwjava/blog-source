---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Aperçu de Git Fetch et Prune
translated: true
type: note
---

### Qu'est-ce que `git fetch` ?
`git fetch` télécharge les derniers changements (commits, branches, tags) d'un dépôt distant sans les fusionner dans votre branche actuelle. Il met à jour vos branches de suivi distantes locales (par exemple, `origin/main`) pour qu'elles correspondent à l'état du dépôt distant. Cela permet de maintenir votre dépôt local synchronisé sans modifier vos fichiers de travail ou vos branches locales.

### Qu'est-ce que l'option `--prune` ?
Le flag `--prune` indique à Git de supprimer les branches de suivi distantes qui n'existent plus sur le dépôt distant. Par exemple, si quelqu'un supprime une branche sur GitHub, votre copie locale (par exemple, `origin/old-branch`) persiste à moins d'être élaguée.

### Comment fonctionne `git fetch --prune` ?
- **Exécution** : Exécutez-le avec `git fetch --prune` (ou `git fetch -p` en version raccourcie). Il combine fetch et prune en une seule commande.
- **Étapes** :
  1. Git se connecte au dépôt distant et récupère les mises à jour, mettant à jour les branches de suivi distantes pour refléter les nouveaux commits, les branches ajoutées ou les branches supprimées.
  2. Il recherche les branches de suivi distantes obsolètes (celles qui n'ont plus de contrepartie sur le dépôt distant) et les supprime localement.
- **Résultat** : Votre dépôt local reste à jour et propre. Aucune fusion n'a lieu — c'est une synchronisation en lecture seule.

### Exemple pratique
Supposons que vous ayez :
- Une branche locale : `main`, suivant `origin/main`.
- Une branche de suivi distante locale obsolète : `origin/deleted-feature`.

L'exécution de `git fetch --prune` pour `origin` :
- Récupère tous les nouveaux commits.
- Supprime `origin/deleted-feature` (puisqu'elle a été supprimée sur le dépôt distant).
- Ne touche pas à vos branches locales.

### Ce que cela signifie
Cela signifie « récupérer les dernières données distantes et nettoyer les références obsolètes » dans votre dépôt local. Utilisez-la régulièrement pour éviter la confusion due aux anciennes références de branches. Équivalent à `git fetch` suivi de `git remote prune origin`, mais combiné de manière pratique. Par sécurité, cela n'affecte que les branches de suivi distantes, et non votre propre travail.