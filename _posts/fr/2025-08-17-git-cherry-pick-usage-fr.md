---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Aperçu et utilisation de Git Cherry-Pick
translated: true
type: note
---

### Qu’est-ce que Git Cherry-Pick ?

Git cherry-pick est une commande qui vous permet d’appliquer les modifications d’un commit spécifique (ou d’un ensemble de commits) sur votre branche actuelle, en créant un nouveau commit avec ces changements. C’est utile lorsque vous souhaitez récupérer une correction ou une fonctionnalité particulière d’une branche sans fusionner l’intégralité de celle-ci. Contrairement à une fusion, qui intègre tout l’historique, cherry-pick copie les changements de manière sélective.

### Fonctionnement interne de Git Cherry-Pick

1. **Sélection du Commit** : Vous spécifiez un hash de commit (par exemple, via `git log` pour le trouver) qui contient les modifications souhaitées.

2. **Application des Changements** : Git prend le diff (les modifications de code réelles) de ce commit et tente de l’appliquer au répertoire de travail de votre branche actuelle, en utilisant si possible la logique de fusion à trois voies de Git.

3. **Création d’un Nouveau Commit** : En cas de succès, un nouveau commit est créé sur votre branche avec :
   - Les mêmes modifications que le commit d’origine.
   - Un nouveau hash de commit (car il s’agit d’un commit frais).
   - Un message de commit qui référence l’original (par exemple, via l’option `-x` pour ajouter "cherry picked from commit <hash>").

   Si des conflits de fusion surviennent (par exemple, la branche cible a des modifications incompatibles), Git s’interrompt et vous laisse les résoudre manuellement avant de committer.

Ce processus ne modifie pas l’historique du commit d’origine — il copie simplement les changements. Cela rend cherry-pick idéal pour le backport de corrections de bugs ou l’application sélective de fonctionnalités.

### Étapes d’utilisation de base

1. Assurez-vous d’être sur la branche cible (changez avec `git checkout <branche>`).
2. Trouvez le hash du commit souhaité (par exemple, `git log --oneline`).
3. Exécutez : `git cherry-pick <hash-du-commit>`
   - Pour plusieurs commits : `git cherry-pick <hash1> <hash2>`
   - Avec des options comme `-n` (pas de commit, pour staging) ou `-x` (référence l’original).

4. Si des conflits surviennent, modifiez les fichiers, ajoutez-les avec `git add`, puis `git cherry-pick --continue`.
5. Pour annuler en cours de route : `git cherry-pick --abort`.

### Exemple de scénario

Supposons que vous ayez une branche de fonctionnalité avec les commits A -> B -> C, et que vous souhaitiez appliquer le commit B sur la branche main.

- Sur main : `git checkout main`
- `git cherry-pick B` (en remplaçant B par le hash réel)

Cela ajoute les modifications de B sous la forme d’un nouveau commit D sur main, sans inclure A ou C. Le commit B d’origine reste dans la branche de fonctionnalité.

### Mises en garde et conseils

- Évitez de cherry-pick des fusions (commits avec plusieurs parents), car cela peut causer des problèmes — utilisez `git cherry-pick -m 1 <merge-commit>` pour spécifier un parent.
- La commande ne conserve pas les métadonnées du commit, comme la date de l’auteur, mais `git cherry-pick --edit` vous permet de modifier le message.
- Pour des changements séquentiels, appliquez plusieurs commits dans l’ordre pour éviter les dépendances manquantes.
- Testez toujours après un cherry-pick, car cela peut introduire des bugs si les contextes diffèrent.

Pour plus de détails, la documentation officielle de Git fournit un guide complet : https://git-scm.com/docs/git-cherry-pick. Si vous rencontrez des problèmes spécifiques, partagez la sortie de votre `git log` !