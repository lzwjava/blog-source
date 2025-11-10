---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Commande Git Clean Expliquée
translated: true
type: note
---

### Ce que fait la commande
La commande `git clean -f -d` (en supposant que "clean clean" soit une faute de frappe et que vous vouliez dire `git clean`) supprime les fichiers et réperoires non suivis de votre répertoire de travail Git. Les drapeaux se décomposent comme suit :
- `-f` (force) : Nécessaire pour supprimer réellement les fichiers, car Git ne les supprimera pas par défaut pour éviter une perte de données accidentelle.
- `-d` (répertoires) : Étend le nettoyage pour inclure les répertoires non suivis, pas seulement les fichiers.

Vous avez écrit `-fd -f`, ce qui combine `-f -d -f`. Puisque `-f` apparaît deux fois, c'est redondant mais sans conséquence — les drapeaux peuvent être répétés sans problème. Si vous vouliez dire autre chose, précisez !

### Comment cela fonctionne
Git clean opère sur l'arbre de travail (vos fichiers locaux), et non sur le dépôt lui-même. Voici une explication étape par étape de son comportement :

1. **Scanne le répertoire de travail** : Il identifie les éléments "non suivis" — fichiers/répertoires qui ne sont pas dans l'index Git ou suivis par des commits. Exemples : fichiers temporaires comme `*.log`, artefacts de compilation, ou répertoires vides provenant de branches supprimées.

2. **Applique les options** :
   - Sans `-f`, il montre seulement ce qui serait supprimé (mode simulation). Avec `-f`, il procède à la suppression.
   - Sans `-d`, il ignore les répertoires. Avec `-d`, il supprime les répertoires vides ou récursivement vides contenant des fichiers non suivis.
   - Il respecte le fichier `.gitignore` par défaut : les fichiers ignorés ne sont pas touchés, sauf si vous ajoutez `-x` (eXclure des règles d'ignore) ou `-X` (nettoyer uniquement les fichiers ignorés).

3. **Mesures de sécurité** : Git avertit si `-f` n'est pas utilisé. Il ne supprimera pas les fichiers dans les répertoires ignorés sauf instruction explicite. Exécutez d'abord `git clean --dry-run -f -d` pour prévisualiser les changements.

4. **Exemple d'utilisation** :
   - Pour nettoyer de manière interactive : `git clean -i` (demande confirmation pour chaque élément).
   - Workflow typique : Après `git reset`, utilisez cette commande pour correspondre exactement à votre dernier commit.

### Mises en garde et preuves
- **Risque** : Supprimer des fichiers est irréversible sans sauvegardes ou `git reflog`. Committez toujours le travail important d'abord.
- **Preuve de la documentation Git** : La documentation officielle de Git (par exemple, `man git-clean` ou docs sur git-scm.com) confirme ceci : `-f` force la suppression, `-d` inclut les répertoires. Elle utilise des opérations du système de fichiers comme `unlink` et `rmdir`, mais uniquement sur les éléments non suivis pour éviter de corrompre les données suivies.
- **Conseil de test** : Dans un dépôt de test, créez un fichier et un répertoire non suivis, puis exécutez la commande — observez le résultat et les changements dans le système de fichiers.

Si cela ne correspond pas à votre intention, fournissez plus de contexte !