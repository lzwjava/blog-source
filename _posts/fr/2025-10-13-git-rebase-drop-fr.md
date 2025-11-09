---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Git Rebase Supprime les Commits
translated: true
type: note
---

Oui — exactement.

Lorsque vous utilisez **`drop`** pendant un `git rebase -i` interactif, cela signifie **« supprimer complètement ce commit de l'historique »**.

Voici ce qui se passe :

* Git **omettra d'appliquer** ce commit lors de la relecture des autres.
* La branche résultante apparaîtra comme si ce commit **n'avait jamais existé** — ses modifications et son message de commit sont tous deux supprimés.
* Les commits suivants seront toujours appliqués (s'ils ne dépendent pas des modifications supprimées).

Exemple :

```bash
git rebase -i HEAD~4
```

Vous pourriez voir quelque chose comme :

```
pick a1b2c3d Corriger une faute de frappe
pick b2c3d4e Ajouter le README
pick c3d4e5f Implémenter la connexion
pick d4e5f6g Ajouter un log de débogage
```

Si vous changez la dernière ligne en :

```
drop d4e5f6g Ajouter un log de débogage
```

alors, après avoir sauvegardé et fermé l'éditeur, Git va rebaser la branche et **exclure ce commit**.

Donc oui — « drop » = **supprimer le commit de l'historique de la branche.**

Souhaitez-vous que j'explique en quoi cela diffère de `revert` (qui *annule* un commit mais en conserve une trace) ?