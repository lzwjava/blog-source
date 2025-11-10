---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser Git Pull et Push avec des clones superficiels
translated: true
type: note
---

Oui, vous pouvez toujours utiliser `git pull` ou `git push` après avoir cloné un dépôt avec un historique limité en utilisant `--depth=20`. Cependant, il y a quelques considérations importantes à garder à l'esprit :

### 1. **Ce que fait `--depth=20`**
   - L'option `--depth=20` crée un *clone superficiel (shallow clone)*, récupérant uniquement les 20 commits les plus récents (ou le nombre spécifié) depuis la branche par défaut (ou la branche spécifiée si vous utilisez `--branch`).
   - Cela réduit la quantité d'historique téléchargée, rendant le clone plus rapide et de plus petite taille, mais le dépôt ne contiendra pas l'historique complet des commits.

### 2. **Utiliser `git pull` avec un clone superficiel**
   - **Oui, vous pouvez utiliser `git pull`** dans un clone superficiel pour récupérer et fusionner de nouveaux commits depuis le dépôt distant.
   - Par défaut, `git pull` va récupérer les nouveaux commits et mettre à jour l'historique superficiel, en le maintenant cohérent avec la branche distante.
   - Si de nouveaux commits sont ajoutés à la branche distante, `git pull` les récupérera et étendra l'historique dans votre dépôt local, tout en respectant la nature superficielle du clone.

   **Note** : Si l'historique de la branche change d'une manière qui affecte les commits plus anciens que votre historique superficiel (par exemple, un `push --force` ou un `rebase` sur le dépôt distant), vous pourriez rencontrer des problèmes. Dans de tels cas, vous pourriez avoir besoin d'approfondir l'historique (en utilisant `git fetch --deepen=<n>` ou `git fetch --unshallow` pour récupérer l'historique complet) pour résoudre les conflits ou continuer à travailler.

### 3. **Utiliser `git push` avec un clone superficiel**
   - **Oui, vous pouvez utiliser `git push`** pour pousser vos commits locaux vers le dépôt distant.
   - Un clone superficiel ne restreint pas votre capacité à créer de nouveaux commits et à les pousser vers le dépôt distant, tant que le dépôt distant accepte vos modifications.
   - Cependant, si le dépôt distant nécessite des opérations qui dépendent de l'historique complet (par exemple, une fusion ou un rebase impliquant des commits plus anciens), vous pourriez avoir besoin de récupérer plus d'historique pour finaliser le `push` avec succès.

### 4. **Limitations des clones superficiels**
   - **Historique limité** : Certaines opérations Git, comme `git log`, `git blame` ou `git rebase`, peuvent être limitées car les commits plus anciens ne sont pas disponibles localement.
   - **Fusion et Rebase** : Si vous avez besoin de fusionner ou de rebaser avec des commits en dehors de votre historique superficiel, vous pourriez avoir besoin de récupérer plus d'historique en utilisant `git fetch --deepen=<n>` ou `git fetch --unshallow`.
   - **Poussées forcées (Force Pushes)** : Si la branche distante est réécrite (par exemple, avec `git push --force`), votre clone superficiel pourrait ne pas avoir suffisamment de contexte pour gérer les changements, vous obligeant à approfondir l'historique ou à re-cloner.

### 5. **Comment approfondir un clone superficiel (si nécessaire)**
   Si vous rencontrez des problèmes avec `git pull` ou `git push` dus à l'historique limité, vous pouvez récupérer de l'historique supplémentaire :
   - **Approfondir d'un nombre spécifique de commits** :
     ```bash
     git fetch --deepen=20
     ```
     Cela récupère 20 commits d'historique supplémentaires.
   - **Récupérer l'historique complet** :
     ```bash
     git fetch --unshallow
     ```
     Cela convertit votre clone superficiel en un clone complet avec l'historique entier.

### 6. **Conseils pratiques**
   - Un clone superficiel avec `--depth=20` est généralement suffisant pour la plupart des workflows, surtout si vous travaillez uniquement sur des changements récents ou contribuez de petites mises à jour.
   - Si vous anticipez d'avoir besoin de l'historique complet (par exemple, pour des fusions complexes, des rebases ou du débogage), envisagez de cloner le dépôt complet sans l'option `--depth` ou d'approfondir l'historique plus tard si nécessaire.
   - Assurez-vous toujours d'avoir les droits d'écriture sur le dépôt distant (par exemple, `git@github.com:cisco/ChezScheme.git`) avant de tenter de pousser (`push`).

### Exemple de Workflow
```bash
# Cloner avec un historique limité
git clone git@github.com:cisco/ChezScheme.git --depth=20
cd ChezScheme

# Effectuer des changements et committer
git commit -m "Mes changements"

# Récupérer les derniers changements
git pull origin main

# Pousser vos changements
git push origin main
```

Si vous rencontrez des problèmes dus au clone superficiel, approfondissez l'historique comme décrit ci-dessus.

### Résumé
Oui, vous pouvez utiliser `git pull` et `git push` avec un clone superficiel créé en utilisant `--depth=20`. Cependant, vous pourriez avoir besoin de récupérer de l'historique supplémentaire pour certaines opérations si l'historique superficiel est insuffisant. Utilisez `git fetch --deepen` ou `git fetch --unshallow` pour résoudre toute limitation.