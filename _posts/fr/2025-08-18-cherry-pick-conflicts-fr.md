---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Sélection des Conflits de Cerises et Solutions
translated: true
type: note
---

La commande **cherry-pick** de Git permet d'extraire un commit d'une branche et de l'appliquer sur une autre, sans fusionner l'historique complet de la branche.

---

### Fonctionnement

* Lorsque vous exécutez `git cherry-pick <commit-hash>`, Git :

  1. Localise les modifications introduites par ce commit (un diff par rapport à son parent).
  2. Réapplique ces modifications sur votre branche actuelle, en créant un nouveau commit avec un nouveau hash.
  3. Cela signifie que le contenu du commit est réutilisé, mais il ne conserve pas l'ascendance du commit d'origine.

C'est comme dire :
*"Prends juste le patch de ce commit unique et applique-le là où je suis actuellement."*

---

### Pourquoi des conflits surviennent

Les conflits surviennent parce que cherry-pick applique des modifications **hors de leur contexte d'origine**. Quelques raisons courantes :

1. **Divergence du code**
   Si la branche cible a été modifiée dans les mêmes zones de code depuis le commit d'origine, Git ne peut pas appliquer le patch proprement. Par exemple :

   * Le commit d'origine a ajouté une fonction dans `fileA`.
   * Dans la branche cible, quelqu'un a renommé ou supprimé cette fonction.
     → Conflit lors du cherry-pick.

2. **Commits dépendants manquants**
   Parfois, un commit dépend de commits antérieurs (ex: refactorings, renommages de variables). Si vous le cherry-pickez sans ceux-ci, le contexte est différent et des conflits apparaissent.

3. **Modifications qui se chevauchent**
   Si les deux branches ont modifié les mêmes lignes de code (même pour des raisons différentes), Git ne peut pas décider automatiquement et s'arrête pour une résolution manuelle.

---

### Exemple de scénario

* `feature-branch` a les commits A → B → C.
* Vous voulez le commit B dans `main`.
* Vous exécutez `git checkout main && git cherry-pick B`.
* Si `main` a déjà modifié le même fichier/les mêmes lignes que B, Git signale un conflit. Vous devez ouvrir le fichier, résoudre les différences, faire `git add`, puis `git cherry-pick --continue`.

---

👉 En bref : **Cherry-pick rejoue un patch dans un nouveau contexte. Les conflits surviennent lorsque ce contexte a trop divergé de l'original.**

Souhaitez-vous que je vous explique également **les bonnes pratiques pour réduire les conflits de cherry-pick** (comme l'ordonnancement des commits, l'utilisation de `-x`, ou un rebase au préalable) ?