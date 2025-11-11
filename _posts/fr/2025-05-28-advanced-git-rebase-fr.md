---
audio: false
generated: true
lang: fr
layout: post
title: 'Git avancé : Rebase, Merge, Gestion des Conflits, Squash'
translated: true
type: note
---

Ce guide couvre l'utilisation avancée de `git rebase` et `git merge`, la résolution des conflits, l'utilisation des stratégies `ours` et `theirs`, et le squashing de commits. Je fournirai des explications concises et des exemples pratiques pour chaque sujet, en me concentrant sur les workflows avancés qui supposent une familiarité avec les commandes Git de base.

## 1. Git Merge : Utilisation Avancée
`git merge` combine plusieurs séquences de développement en un historique unifié. L'utilisation avancée comprend la gestion des fusions complexes, l'utilisation des stratégies de fusion et la gestion des commits de fusion.

### Stratégies de Fusion Clés
- **Récursive (par défaut)**: Gère plusieurs ancêtres communs et convient à la plupart des fusions.
  - Exemple : `git merge --strategy=recursive nom-de-la-branche`
- **Ours**: Conserve les modifications de la branche actuelle, en ignorant les modifications de la branche fusionnée.
  - Exemple : `git merge --strategy=ours branche-de-fonctionnalité`
- **Theirs**: N'est pas une véritable stratégie mais peut être émulée (voir ci-dessous pour la résolution de conflits).
- **Octopus**: Fusionne plusieurs branches à la fois (utilisée pour >2 branches).
  - Exemple : `git merge branche1 branche2 branche3`

### Options de Fusion Avancées
- `--no-ff`: Force un commit de fusion même si un fast-forward est possible, préservant l'historique de la branche.
  - Exemple : `git merge --no-ff branche-de-fonctionnalité`
- `--squash`: Combine tous les commits de la branche fusionnée en un seul commit sur la branche actuelle.
  - Exemple : `git merge --squash branche-de-fonctionnalité && git commit`
- `--allow-unrelated-histories`: Fusionne des branches sans historique commun.
  - Exemple : `git merge --allow-unrelated-histories branche-de-repo-externe`

### Exemple : Fusion avec No Fast-Forward
```bash
git checkout main
git merge --no-ff branche-de-fonctionnalité
# Crée un commit de fusion, préservant l'historique de branche-de-fonctionnalité
```

## 2. Git Rebase : Utilisation Avancée
`git rebase` réécrit l'historique en déplaçant ou en modifiant les commits pour créer un historique linéaire. C'est puissant pour nettoyer les branches mais modifie l'historique, à utiliser avec précaution sur les branches partagées.

### Types de Rebase
- **Rebase Standard**: Rejoue les commits de la branche actuelle sur la branche de base.
  - Exemple : `git rebase main` (tout en étant sur `branche-de-fonctionnalité`)
- **Rebase Interactif**: Permet de modifier, squasher ou réordonner les commits.
  - Exemple : `git rebase -i main`

### Commandes de Rebase Interactif
Exécutez `git rebase -i <base>` (par exemple, `git rebase -i HEAD~3` pour les 3 derniers commits). Cela ouvre un éditeur avec des commandes comme :
- `pick`: Conserver le commit tel quel.
- `reword`: Modifier le message du commit.
- `edit`: Mettre en pause le rebase pour modifier le commit.
- `squash`: Combiner avec le commit précédent.
- `fixup`: Comme squash, mais ignore le message du commit.
- `drop`: Supprimer le commit.

### Exemple : Rebase Interactif
Pour squasher les 3 derniers commits :
```bash
git rebase -i HEAD~3
# Dans l'éditeur, changez "pick" en "squash" ou "fixup" pour les commits à combiner
# Sauvegardez et quittez pour terminer
```

### Rebase sur une Base Différente
Pour déplacer une branche vers une nouvelle base (par exemple, déplacer `branche-de-fonctionnalité` de `ancienne-base` vers `main`) :
```bash
git rebase --onto main ancienne-base branche-de-fonctionnalité
```

### Rebase avec les Commits de Fusion
Par défaut, le rebase aplatit les commits de fusion. Pour les préserver :
```bash
git rebase -i --preserve-merges main
```

### Annuler un Rebase
Si quelque chose ne va pas :
```bash
git rebase --abort
```

## 3. Résolution des Conflits de Merge/Rebase
Les conflits surviennent lorsque Git ne peut pas concilier automatiquement les modifications. Les `merge` et `rebase` peuvent tous deux entraîner des conflits, résolus de manière similaire.

### Étapes pour Résoudre les Conflits
1. **Identifier les Conflits**: Git met en pause et liste les fichiers en conflit.
   - Pour merge : `git status` montre les fichiers avec des conflits.
   - Pour rebase : Les conflits sont résolus commit par commit pendant `git rebase -i`.
2. **Modifier les Fichiers en Conflit**: Ouvrez les fichiers et cherchez les marqueurs de conflit :
   ```text
   <<<<<<< HEAD
   Vos modifications
   =======
   Modifications entrantes
   >>>>>>> nom-de-la-branche
   ```
   Modifiez manuellement pour conserver les modifications souhaitées, puis supprimez les marqueurs.
3. **Marquer comme Résolu**:
   - Pour merge : `git add <fichier>`
   - Pour rebase : `git add <fichier>`, puis `git rebase --continue`
4. **Terminer le Processus**:
   - Merge : `git commit` (Git peut générer automatiquement un message de commit).
   - Rebase : `git rebase --continue` jusqu'à ce que tous les commits soient appliqués.

### Exemple : Résolution d'un Conflit de Merge
```bash
git checkout main
git merge branche-de-fonctionnalité
# Un conflit survient
git status  # Liste les fichiers en conflit
# Modifiez les fichiers pour résoudre les conflits
git add fichier-resolu.txt
git commit  # Finalise la fusion
```

### Exemple : Résolution d'un Conflit de Rebase
```bash
git checkout branche-de-fonctionnalité
git rebase main
# Un conflit survient
# Modifiez les fichiers en conflit
git add fichier-resolu.txt
git rebase --continue
# Répétez jusqu'à la fin du rebase
```

## 4. Utilisation de Ours et Theirs dans la Résolution de Conflits
Pendant les conflits, vous pouvez vouloir favoriser les modifications d'un côté (`ours` ou `theirs`). La signification de `ours` et `theirs` dépend de l'opération.

### Merge : Ours vs. Theirs
- `ours`: Modifications de la branche actuelle (par exemple, `main`).
- `theirs`: Modifications de la branche en cours de fusion (par exemple, `branche-de-fonctionnalité`).
- Utilisez l'option `--strategy-option` (`-X`) :
  - Garder `ours`: `git merge -X ours branche-de-fonctionnalité`
  - Garder `theirs`: `git merge -X theirs branche-de-fonctionnalité`

### Rebase : Ours vs. Theirs
- `ours`: Modifications de la branche de base (par exemple, `main`).
- `theirs`: Modifications de la branche en cours de rebase (par exemple, `branche-de-fonctionnalité`).
- Utilisez pendant la résolution de conflit de rebase :
  ```bash
  git checkout --ours fichier.txt  # Garder la version de la branche de base
  git checkout --theirs fichier.txt  # Garder la version de la branche en rebase
  git add fichier.txt
  git rebase --continue
  ```

### Exemple : Merge avec Theirs
Pour fusionner `branche-de-fonctionnalité` dans `main` et favoriser les modifications de `branche-de-fonctionnalité` :
```bash
git checkout main
git merge -X theirs branche-de-fonctionnalité
```

### Exemple : Rebase avec Ours
Pendant le rebase de `branche-de-fonctionnalité` sur `main`, résolvez un conflit en gardant la version de `main` :
```bash
git checkout branche-de-fonctionnalité
git rebase main
# Un conflit survient
git checkout --ours fichier.txt
git add fichier.txt
git rebase --continue
```

## 5. Squashing de Commits
Le squashing combine plusieurs commits en un seul, créant un historique plus propre. Cela se fait généralement avec un rebase interactif.

### Étapes pour Squasher les Commits
1. Démarrez un rebase interactif pour les commits souhaités :
   ```bash
   git rebase -i HEAD~n  # n = nombre de commits à squasher
   ```
2. Dans l'éditeur, changez `pick` en `squash` (ou `fixup`) pour les commits à combiner avec le commit précédent.
3. Sauvegardez et quittez. Git peut demander de modifier le message du commit combiné.
4. Poussez l'historique mis à jour (force push si déjà partagé) :
   ```bash
   git push --force-with-lease
   ```

### Exemple : Squasher 3 Commits
```bash
git rebase -i HEAD~3
# L'éditeur montre :
# pick abc123 Commit 1
# pick def456 Commit 2
# pick ghi789 Commit 3
# Changez en :
# pick abc123 Commit 1
# squash def456 Commit 2
# squash ghi789 Commit 3
# Sauvegardez et quittez
# Modifiez le message du commit combiné si demandé
git push --force-with-lease
```

### Squashing Pendant un Merge
Pour squasher tous les commits d'une branche pendant une fusion :
```bash
git checkout main
git merge --squash branche-de-fonctionnalité
git commit  # Crée un seul commit
```

## Bonnes Pratiques et Conseils
- **Sauvegarde Avant Rebase**: Le rebase réécrit l'historique. Créez une branche de sauvegarde :
  ```bash
  git branch branche-de-sauvegarde
  ```
- **Évitez de Rebaser les Branches Partagées**: Réécrire l'historique sur les branches publiques peut causer des problèmes aux collaborateurs. Utilisez `merge` à la place.
- **Utilisez `--force-with-lease` pour la Sécurité**: Lors du push d'un historique réécrit, cela empêche l'écrasement des modifications des autres.
- **Testez Après la Résolution des Conflits**: Assurez-vous que votre projet se compile et que les tests passent après la résolution des conflits.
- **Utilisez des Outils pour les Conflits**: Les outils graphiques comme VS Code, SourceTree ou `git mergetool` peuvent simplifier la résolution des conflits.
- **Communiquez avec l'Équipe**: Si vous travaillez en équipe, coordonnez les rebases pour éviter les conflits.

## Pièges Courants
- **Perdre du Travail dans un Rebase**: Sauvegardez toujours ou utilisez `git reflog` pour récupérer les commits perdus.
- **Mauvaise Utilisation de Ours/Theirs**: Vérifiez quelle branche est `ours` vs `theirs` dans les contextes de merge vs rebase.
- **Force Push Sans Coordination**: Le force-push des branches partagées peut perturber les coéquipiers. Utilisez `--force-with-lease` et communiquez.

## Récupération après des Erreurs
- **Voir l'Historique**: Utilisez `git reflog` pour voir les états précédents et récupérer les commits perdus :
  ```bash
  git reflog
  git checkout <hash-du-commit>
  ```
- **Reset à l'État Pré-Merge**:
  ```bash
  git reset --hard HEAD^  # Annule le dernier commit de merge
  ```
- **Annuler un Merge**: Si une fusion se passe mal :
  ```bash
  git merge --abort
  ```

Ce guide fournit une base solide pour les workflows Git avancés. Pour des scénarios spécifiques ou des erreurs, faites-le-moi savoir, et je peux approfondir ou rechercher des solutions en temps réel !