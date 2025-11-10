---
audio: false
generated: true
lang: fr
layout: post
title: Maven Compile Avant Commit Git
translated: true
type: note
---

Oui, vous pouvez exécuter `mvn compile` dans un dépôt Git local avant d'exécuter `git commit`. Voici une explication concise et les étapes :

1. **Vérifier l'Installation de Maven** : Assurez-vous que Maven est installé et configuré sur votre système (utilisez `mvn -version` pour vérifier).

2. **Naviguer vers Votre Dépôt Git** : Utilisez `cd chemin/vers/votre/repo` pour accéder à votre dépôt Git local contenant le projet Maven (avec un fichier `pom.xml`).

3. **Exécuter Maven Compile** : Exécutez `mvn compile` pour compiler votre code Java. Cela va :
   - Compiler le code source dans `src/main/java`.
   - Placer les classes compilées dans `target/classes`.
   - Signaler toute erreur de compilation.

4. **Vérifier le Statut de la Compilation** :
   - Si `mvn compile` réussit (se termine par `BUILD SUCCESS`), vous pouvez procéder aux opérations Git.
   - S'il échoue (par exemple, à cause d'erreurs de syntaxe), corrigez le code avant de committer.

5. **Workflow Git** :
   - Ajouter les modifications : `git add .` (ou des fichiers spécifiques).
   - Committer les modifications : `git commit -m "Votre message de commit"`.

### Optionnel : Automatiser avec les Git Hooks
Pour vous assurer que `mvn compile` s'exécute avant chaque `git commit`, vous pouvez utiliser un hook Git pre-commit :
1. Accédez à `.git/hooks` dans votre dépôt.
2. Créez ou modifiez le fichier `pre-commit` (sans extension de fichier).
3. Ajoutez un script comme :
   ```bash
   #!/bin/sh
   mvn compile
   if [ $? -ne 0 ]; then
       echo "La compilation a échoué, commit annulé."
       exit 1
   fi
   ```
4. Rendez-le exécutable : `chmod +x .git/hooks/pre-commit`.
   - Maintenant, `git commit` ne procédera que si `mvn compile` réussit.

### Notes
- **Dépendances** : Assurez-vous que `pom.xml` est correctement configuré et que les dépendances sont téléchargées (utilisez `mvn dependency:resolve` si nécessaire).
- **Performance** : Exécuter `mvn compile` avant chaque commit garantit la qualité du code mais peut ralentir votre workflow pour les grands projets.
- **Commandes Alternatives** : Si vous souhaitez inclure les tests, utilisez `mvn test` au lieu de `mvn compile` pour compiler et exécuter les tests unitaires.

Cette approche garantit que votre code est compilé avec succès avant d'être commité dans le dépôt Git.