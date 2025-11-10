---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Git expliqué par le ramasse-miettes
translated: true
type: note
---

`git gc` signifie **Git garbage collection** (nettoyage de la mémoire). C'est une commande de maintenance qui nettoie et optimise votre dépôt local.

### Ce qu'elle fait

* **Compresse l'historique des fichiers** : Git stocke les objets (commits, arbres, blobs) dans une base de données. Au fil du temps, de nombreux objets non empaquetés s'accumulent. `git gc` les regroupe dans un fichier binaire compact, économisant ainsi de l'espace disque.
* **Supprime les objets inaccessibles** : Si vous avez supprimé des branches ou effectué un rebase, certains commits peuvent ne plus être accessibles depuis aucune référence. Git les conserve par sécurité, mais `git gc` finit par les nettoyer.
* **Optimise les références** : Il réécrit et empaquette les refs comme les tags et les branches pour accélérer les recherches.
* **Élague les reflogs** : Les anciennes entrées du reflog (historique des changements de HEAD) au-delà de la période d'expiration sont supprimées.

### Pourquoi elle s'exécute parfois automatiquement

* Git exécute un **`gc` automatique en arrière-plan** lorsque le nombre d'objets non empaquetés ou de fichiers de pack dépasse un certain seuil. Par exemple, si vous avez effectué de nombreux commits, rebases ou merges, Git peut le déclencher.
* De nombreuses commandes Git (comme `git fetch`, `git merge` ou `git rebase`) vérifient si un `gc` est conseillé et l'exécutent automatiquement si nécessaire.
* Cela permet de maintenir les performances de votre dépôt sans que vous ayez à y penser.

### Quand l'exécuter manuellement

* Si votre dépôt semble **lent** ou **gonflé** (par exemple, un dossier `.git` volumineux).
* Après avoir effectué un **grand nettoyage** (comme supprimer des branches ou retirer des fichiers volumineux de l'historique).
* Si vous voulez forcer un nettoyage immédiat :

  ```bash
  git gc --prune=now --aggressive
  ```

  *(soyez prudent : `--aggressive` peut prendre beaucoup de temps, surtout sur les grands dépôts)*

---

Souhaitez-vous que j'explique également comment **vérifier quand Git a exécuté `gc` automatiquement pour la dernière fois** et quels seuils le déclenchent ?