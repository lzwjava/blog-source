---
audio: false
generated: true
lang: fr
layout: post
title: Branches Git divergées
translated: true
type: note
---

Lorsque votre branche locale `main` et la branche distante `origin/main` ont divergé dans Git — avec respectivement 74 et 70 commits différents — cela signifie qu'elles partagent un ancêtre commun mais ont depuis développé des commits uniques. Votre objectif est de faire correspondre votre branche locale `main` à `origin/main` en réinitialisant votre branche locale à l'ancêtre commun (le « parent des deux ») puis en utilisant `git pull` pour récupérer les changements distants, ce qui a pour effet de rejeter vos commits locaux divergents en faveur de ceux du dépôt distant. Voici les étapes pour y parvenir.

### Étapes pour Corriger la Divergence

1. **Récupérer les Derniers Changements Distants**  
   Commencez par vous assurer que votre dépôt local a les dernières informations du dépôt distant. Cela met à jour votre référence à `origin/main` sans modifier votre branche locale `main` pour le moment.

   ```bash
   git fetch origin
   ```

2. **Trouver le Commit Ancêtre Commun**  
   Utilisez `git merge-base` pour identifier le commit ancêtre commun entre votre branche locale `main` et `origin/main`. C'est le point où les branches ont divergé.

   ```bash
   ancestor=$(git merge-base main origin/main)
   ```

   Cette commande stocke le hash du commit de l'ancêtre commun dans la variable `ancestor`.

3. **Réinitialiser la Branche Locale `main` à l'Ancêtre Commun**  
   Réinitialisez votre branche locale `main` au commit de l'ancêtre commun. L'option `--hard` garantit que le pointeur de branche et votre répertoire de travail sont mis à jour, rejetant tous les commits locaux et les modifications effectuées après ce point.

   ```bash
   git reset --hard $ancestor
   ```

   **Attention** : Cette étape supprimera toutes les modifications non validées dans votre répertoire de travail et votre zone de staging, ainsi que les 74 commits uniques à votre branche locale `main`. Si vous devez les conserver, envisagez de créer d'abord une branche de sauvegarde (voir « Sauvegarde Optionnelle » ci-dessous).

4. **Récupérer les Changements Distants**  
   Maintenant, récupérez les changements depuis `origin/main`. Étant donné que votre branche locale `main` est maintenant sur l'ancêtre commun et que `origin/main` est en avance de 70 commits, cela effectuera un fast-forward de votre branche locale `main` pour qu'elle corresponde à `origin/main`.

   ```bash
   git pull origin main
   ```

   Après cela, votre branche locale `main` sera identique à `origin/main`, tous les commits locaux divergents ayant été rejetés.

### Séquence de Commandes Complète

Voici la séquence complète des commandes à exécuter :

```bash
git fetch origin
ancestor=$(git merge-base main origin/main)
git reset --hard $ancestor
git pull origin main
```

### Ce qui se Passe
- **Après l'Étape 1** : Votre dépôt local connaît le dernier état de `origin/main`.
- **Après l'Étape 2** : Vous avez identifié le commit ancêtre commun (par exemple, un hash comme `abc123`).
- **Après l'Étape 3** : Votre branche locale `main` est réinitialisée à `abc123`, perdant ainsi les 74 commits locaux uniques.
- **Après l'Étape 4** : `git pull` effectue un fast-forward de `main` vers `origin/main`, intégrant les 70 commits de la branche distante.

Le résultat est que votre branche locale `main` correspond exactement à `origin/main`, atteignant ainsi votre objectif d'utiliser la branche distante.

### Sauvegarde Optionnelle
Si vous n'êtes pas sûr de vouloir rejeter vos commits locaux et souhaitez les conserver pour plus tard, créez une branche de sauvegarde avant la réinitialisation :

```bash
git branch backup-main
```

Exécutez cette commande avant la commande `git reset`. Vos 74 commits locaux resteront sur `backup-main`, et vous pourrez les consulter plus tard si nécessaire.

### Notes Importantes
- **Modifications Non Validées** : Si vous avez des modifications non validées (dans votre répertoire de travail ou votre zone de staging) que vous souhaitez conserver, mettez-les de côté avant la réinitialisation :
  ```bash
  git stash
  ```
  Après avoir terminé le processus, vous pouvez les récupérer avec `git stash pop`.
- **Pourquoi Cela Fonctionne** : La réinitialisation à l'ancêtre commun et le pull garantissent un fast-forward propre vers `origin/main`, évitant les conflits de fusion qui pourraient survenir en tirant directement avec des branches divergentes.

En suivant ces étapes, vous réussirez à réinitialiser votre branche locale `main` pour qu'elle corresponde à `origin/main` comme souhaité.