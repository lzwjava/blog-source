---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Nettoyer les branches distantes avec prune
translated: true
type: note
---

`git fetch --prune` est un moyen de garder vos références locales vers les branches distantes propres et à jour.

### Ce que cela fait

* **`git fetch`** met normalement à jour votre copie locale des branches distantes (comme `origin/main`, `origin/feature-x`) sans toucher à vos propres branches locales.
* Au fil du temps, le dépôt distant peut supprimer ou renommer certaines branches. Sans nettoyage, votre dépôt local continuera d'afficher ces anciennes branches de suivi distant (par exemple, `origin/feature-old`).
* **Ajouter `--prune`** indique à Git : *"Si le dépôt distant n'a plus une branche, supprime ma référence de suivi distant correspondante."*

Ainsi, après avoir exécuté `git fetch --prune`, votre liste locale de branches distantes correspond exactement à ce que le dépôt distant possède actuellement.

### Exemple

1. Le dépôt distant a les branches : `main`, `feature-a`.
2. Vous exécutez `git fetch` → vous avez maintenant `origin/main`, `origin/feature-a`.
3. Quelqu'un supprime `feature-a` sur le dépôt distant.
4. Si vous exécutez `git fetch`, vous verrez toujours `origin/feature-a` localement (référence obsolète).
5. Si vous exécutez `git fetch --prune`, Git remarquera que `feature-a` a disparu et supprimera `origin/feature-a` de votre dépôt local.

### Pourquoi c'est utile

* Garde la liste `git branch -r` (branches distantes) propre.
* Évite la confusion lors du changement ou de la fusion dans des branches qui n'existent plus en amont.
* Souvent utilisé avec des alias (par exemple, `git fetch -p`) ou défini par défaut avec :

  ```bash
  git config fetch.prune true
  ```

De cette façon, chaque `git fetch` nettoie automatiquement les branches obsolètes.

---

Souhaitez-vous que j'explique également comment **le nettoyage interagit avec les tags** (puisque `git fetch --prune` ne gère par défaut que les branches, mais les tags se comportent différemment) ?