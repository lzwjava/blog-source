---
audio: false
generated: true
lang: fr
layout: post
title: Git Stash
translated: true
type: note
---

Voici comment utiliser efficacement `git stash` et changer fréquemment de branches/tags avec des modifications non validées :

## Utilisation de `git stash`

`git stash` est une commande puissante qui vous permet de sauvegarder temporairement vos modifications non validées (à la fois indexées et non indexées) et de réinitialiser votre répertoire de travail au dernier commit. Ceci est utile lorsque vous devez changer de branche ou travailler sur autre chose sans valider votre travail actuel et non terminé.

Voici un aperçu des opérations courantes de `git stash` :

**1. Mettre de côté vos modifications actuelles :**

```bash
git stash
```

Cette commande prend vos modifications non validées, les sauvegarde en tant que nouvelle stash, et nettoie votre répertoire de travail. Vous verrez un message comme :

```
Saved working directory and index state WIP on <your_branch>: <commit_hash> <commit_message>
```

**2. Mettre de côté avec un message :**

Il est utile d'ajouter un message descriptif à vos stashes, surtout si vous en avez plusieurs :

```bash
git stash save "votre message descriptif"
# ou
git stash push -m "votre message descriptif"
```

**3. Lister vos stashes :**

Pour voir la liste de toutes vos stashes sauvegardées, utilisez :

```bash
git stash list
```

Cela affichera une liste de stashes, généralement dans le format :

```
stash@{0}: On <branch_name>: <commit_hash> <stash_message>
stash@{1}: WIP on <another_branch>: ...
```

`stash@{0}` est la stash la plus récente.

**4. Appliquer une stash :**

Pour récupérer les modifications d'une stash, vous pouvez utiliser `git stash apply`. Cela applique les modifications mais garde la stash dans la liste. Par défaut, elle applique la dernière stash (`stash@{0}`).

```bash
git stash apply
# ou pour appliquer une stash spécifique :
git stash apply stash@{1}
```

**5. Appliquer et supprimer une stash :**

Si vous voulez appliquer les modifications et immédiatement supprimer la stash de la liste, utilisez `git stash pop`. Cela cible aussi par défaut la dernière stash.

```bash
git stash pop
# ou pour "pop" une stash spécifique :
git stash pop stash@{1}
```

**6. Voir les détails d'une stash :**

Vous pouvez voir un résumé des modifications dans une stash en utilisant :

```bash
git stash show
# ou pour une stash spécifique :
git stash show stash@{2}
```

Pour voir le diff complet d'une stash, ajoutez l'option `-p` ou `--patch` :

```bash
git stash show -p stash@{0}
```

**7. Mettre de côté les fichiers non suivis :**

Par défaut, `git stash` ne sauvegarde que les modifications des fichiers suivis. Pour inclure les fichiers non suivis, utilisez l'option `-u` ou `--include-untracked` :

```bash
git stash -u
git stash save -u "stash avec fichiers non suivis"
```

**8. Mettre de côté les fichiers ignorés également :**

Pour inclure à la fois les fichiers non suivis et les fichiers ignorés, utilisez l'option `-a` ou `--all` :

```bash
git stash -a
git stash save -a "stash avec tout"
```

**9. Créer une branche à partir d'une stash :**

Si vous avez mis de côté des modifications et que vous voulez maintenant travailler dessus dans une nouvelle branche, vous pouvez créer une branche directement à partir de la stash :

```bash
git stash branch <new_branch_name> stash@{0}
# ou pour la dernière stash :
git stash branch <new_branch_name>
```

Cette commande crée une nouvelle branche basée sur le commit où la stash a été créée, applique les modifications stashées à la nouvelle branche, puis supprime la stash.

**10. Supprimer des stashes :**

* Pour supprimer une stash spécifique :
    ```bash
    git stash drop stash@{1}
    ```
* Pour supprimer toutes les stashes :
    ```bash
    git stash clear
    ```

## Changer fréquemment de Branches ou de Tags avec des Modifications Non Validées

Voici comment utiliser `git stash` pour faciliter le changement fréquent entre des branches ou des tags lorsque vous avez des modifications non validées :

**Scénario 1 : Changer pour une autre branche**

1.  **Mettez de côté vos modifications actuelles :**
    ```bash
    git stash save "WIP sur la branche actuelle"
    ```
2.  **Passez à la branche cible :**
    ```bash
    git checkout <target_branch_name>
    # ou en utilisant la nouvelle commande `git switch` :
    git switch <target_branch_name>
    ```
3.  **Faites votre travail sur la branche cible.**
4.  **Lorsque vous devez retourner à votre branche originale :**
    ```bash
    git checkout <original_branch_name>
    # ou
    git switch <original_branch_name>
    ```
5.  **Réappliquez vos modifications stashées :**
    ```bash
    git stash pop  # Si vous voulez appliquer et supprimer la stash
    # ou
    git stash apply # Si vous voulez appliquer et garder la stash
    ```
6.  **Résolvez tout conflit de fusion potentiel** qui pourrait survenir si la branche originale a divergé de manière significative depuis que vous avez créé la stash.

**Scénario 2 : Changer pour un tag**

Changer directement pour un tag vous place dans un état "detached HEAD", ce qui n'est généralement pas recommandé pour faire des commits. Si vous voulez juste inspecter le code à un tag spécifique :

1.  **Mettez de côté vos modifications actuelles :**
    ```bash
    git stash save "WIP avant inspection du tag"
    ```
2.  **Passez au tag :**
    ```bash
    git checkout <tag_name>
    ```
3.  **Inspectez le code.**
4.  **Pour retourner à votre branche :**
    ```bash
    git checkout <your_branch_name>
    # ou
    git switch <your_branch_name>
    ```
5.  **Réappliquez vos modifications stashées :**
    ```bash
    git stash pop
    # ou
    git stash apply
    ```

**Scénario 3 : Créer une nouvelle branche à partir d'un tag avec vos modifications stashées**

Si vous voulez commencer à travailler sur une nouvelle fonctionnalité ou correction basée sur un tag spécifique, et que vous avez des modifications stashées d'un contexte précédent :

1.  **Mettez de côté vos modifications actuelles (si vous ne l'avez pas déjà fait) :**
    ```bash
    git stash save "WIP"
    ```
2.  **Créez une nouvelle branche à partir du tag :**
    ```bash
    git checkout -b <new_branch_name> <tag_name>
    # ou
    git switch -c <new_branch_name> <tag_name>
    ```
3.  **Appliquez vos modifications stashées à la nouvelle branche :**
    ```bash
    git stash pop # ou git stash apply
    ```
4.  **Résolvez tout conflit de fusion potentiel.**

**Considérations importantes :**

* **Gardez vos stashes organisées :** Utilisez des messages descriptifs pour identifier facilement vos stashes.
* **Stash est local :** Les stashes sont stockées localement dans votre dépôt et ne sont pas poussées vers les dépôts distants.
* **Risque de conflits :** Lorsque vous réappliquez une stash, il y a une possibilité de conflits de fusion si la branche sur laquelle vous appliquez a changé de manière significative depuis que vous avez créé la stash. Vous devrez résoudre ces conflits manuellement.
* **Envisagez de créer des branches temporaires :** Pour un travail à plus long terme que vous n'êtes pas prêt à valider, créer une branche temporaire pourrait être une meilleure approche que de compter lourdement sur les stashes. Vous pouvez facilement changer de branche et valider votre progression.

En utilisant `git stash` efficacement, vous pouvez passer de manière transparente entre les branches et les tags même lorsque vous avez des modifications non validées, permettant un flux de travail plus flexible et efficace. N'oubliez pas de gérer vos stashes et soyez prêt à gérer les conflits de fusion potentiels.