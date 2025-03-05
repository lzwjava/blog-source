---
audio: false
generated: true
lang: fr
layout: post
title: Branches Git Divergentes
translated: true
---

Lorsque votre branche locale `main` et la branche distante `origin/main` ont divergé dans Git—avec 74 et 70 commits différents respectivement—cela signifie qu'elles partagent un ancêtre commun mais ont depuis développé des commits uniques. Votre objectif est de faire en sorte que votre branche locale `main` corresponde à `origin/main` en réinitialisant votre branche locale à l'ancêtre commun (le "parent des deux") puis en utilisant `git pull` pour importer les modifications distantes, en rejetant ainsi vos commits locaux divergents au profit des distants. Voici les étapes à suivre pour y parvenir.

### Étapes pour corriger la divergence

1. **Récupérer les dernières modifications distantes**
   Commencez par vous assurer que votre dépôt local dispose des dernières informations provenant du distant. Cela met à jour votre référence à `origin/main` sans modifier votre branche locale `main` pour l'instant.

   ```bash
   git fetch origin
   ```

2. **Trouver le commit ancêtre commun**
   Utilisez `git merge-base` pour identifier le commit ancêtre commun entre votre `main` local et `origin/main`. Il s'agit du point où les branches ont divergé.

   ```bash
   ancestor=$(git merge-base main origin/main)
   ```

   Cette commande stocke le hash du commit ancêtre commun dans la variable `ancestor`.

3. **Réinitialiser `main` local à l'ancêtre commun**
   Réinitialisez votre branche locale `main` au commit ancêtre commun. L'option `--hard` garantit que le pointeur de branche et votre répertoire de travail sont mis à jour, rejetant tous les commits et modifications locaux effectués après ce point.

   ```bash
   git reset --hard $ancestor
   ```

   **Attention** : Cette étape rejettera toutes les modifications non validées dans votre répertoire de travail et la zone de staging, ainsi que les 74 commits uniques à votre `main` local. Si vous devez les conserver, envisagez de créer une branche de sauvegarde au préalable (voir "Sauvegarde optionnelle" ci-dessous).

4. **Tirer les modifications distantes**
   Maintenant, tirez les modifications de `origin/main`. Puisque votre `main` local est maintenant à l'ancêtre commun, et que `origin/main` est en avance de 70 commits, cela mettra à jour votre `main` local pour correspondre à `origin/main`.

   ```bash
   git pull origin main
   ```

   Après cela, votre branche locale `main` sera identique à `origin/main`, avec tous les commits locaux divergents rejetés.

### Séquence de commandes complète

Voici la séquence complète des commandes à exécuter :

```bash
git fetch origin
ancestor=$(git merge-base main origin/main)
git reset --hard $ancestor
git pull origin main
```

### Ce qui se passe ?
- **Après l'Étape 1** : Votre dépôt local connaît le dernier état de `origin/main`.
- **Après l'Étape 2** : Vous avez identifié le commit ancêtre commun (par exemple, un hash comme `abc123`).
- **Après l'Étape 3** : Votre `main` local est réinitialisé à `abc123`, perdant les 74 commits locaux uniques.
- **Après l'Étape 4** : `git pull` met à jour `main` pour correspondre à `origin/main`, en intégrant les 70 commits de la branche distante.

Le résultat est que votre `main` local correspond exactement à `origin/main`, réalisant ainsi votre objectif d'utiliser la branche distante.

### Sauvegarde optionnelle
Si vous n'êtes pas sûr de vouloir rejeter vos commits locaux et souhaitez les conserver pour plus tard, créez une branche de sauvegarde avant de réinitialiser :

```bash
git branch backup-main
```

Exécutez cette commande avant la commande `git reset`. Vos 74 commits locaux resteront sur `backup-main`, et vous pourrez les consulter plus tard si nécessaire.

### Notes importantes
- **Modifications non validées** : Si vous avez des modifications non validées (dans votre répertoire de travail ou la zone de staging) que vous souhaitez conserver, stockez-les avant de réinitialiser :
  ```bash
  git stash
  ```
  Après avoir terminé le processus, vous pouvez les récupérer avec `git stash pop`.
- **Pourquoi cela fonctionne** : Réinitialiser à l'ancêtre commun et tirer assure une mise à jour propre en avance rapide vers `origin/main`, évitant les conflits de fusion qui pourraient survenir en tirant directement avec des branches divergentes.

En suivant ces étapes, vous réinitialiserez avec succès votre `main` local pour correspondre à `origin/main` comme souhaité.