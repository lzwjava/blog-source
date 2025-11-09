---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Emplacements des sources et classes JavaCC
translated: true
type: note
---

### Présentation de JavaCC
JavaCC (Java Compiler Compiler) est un outil qui génère du code source Java (par exemple, des classes d'analyseur syntaxique) à partir de fichiers de spécification de grammaire (fichiers .jj). Il **ne** compile **pas** directement le code en bytecode (fichiers .class) — cette tâche est prise en charge par un compilateur Java standard comme `javac`. Si vous utilisez JavaCC de manière programmatique (par exemple, dans un IDE ou un environnement d'exécution) pour générer et compiler du code dynamique, les emplacements de sortie dépendent de la façon dont vous le configurez. Je vais décomposer cela étape par étape, en me basant sur le comportement standard de JavaCC et les modèles d'utilisation courants.

### Où JavaCC génère les fichiers source
- **Emplacement de sortie par défaut** : JavaCC génère les fichiers `.java` dans le **répertoire de travail courant** (ou dans un sous-répertoire appelé "output" s'il n'est pas spécifié). Vous pouvez modifier cela avec des options en ligne de commande comme `-OUTPUT_DIRECTORY=<chemin>` ou programmatiquement via la classe `JavaCCOptions` si vous l'invoquez dans le code.
- **Exemple d'utilisation en ligne de commande** :
  ```
  javacc -OUTPUT_DIRECTORY=/chemin/vers/generes MaGrammaire.jj
  ```
  Cela créerait les fichiers `.java` (par exemple, `Token`, `Parser`, `ParseException`) dans `/chemin/vers/generes`.
- **Utilisation programmatique** : Si vous appelez JavaCC depuis votre application Java (par exemple, en utilisant `org.javacc.JavaCC.main()` ou des API similaires), vous pouvez définir des options pour spécifier le chemin de sortie. Les fichiers source sont simplement des fichiers `.java` standards qui nécessitent une compilation ultérieure.

Ceci est conforme à la documentation officielle de JavaCC (par exemple, du projet legacy JavaCC sur SourceForge ou des distributions basées sur Maven), qui indique que les classes générées sont produites sous forme de code source dans le répertoire spécifié, et non sous forme de bytecode.

### Où les classes compilées sont stockées si vous compilez le code généré
JavaCC lui-même ne compile pas en fichiers `.class` — vous devez le faire manuellement ou l'automatiser dans votre code. Voici ce qui se passe ensuite :

- **Compilation manuelle** : Utilisez `javac` sur les fichiers `.java` générés :
  ```
  javac -d /chemin/vers/classes MonParserGenere.java
  ```
  - Le drapeau `-d` spécifie le répertoire de sortie pour les fichiers `.class`, souvent un dossier `classes/` ou la cible de build de votre projet (par exemple, `target/classes/` dans Maven/Gradle).
  - Emplacements courants : `bin/`, `build/classes/`, ou `target/classes/` selon votre système de build (par exemple, Ant, Maven).

- **Compilation dynamique dans le code** : Si vous utilisez JavaCC à l'exécution pour générer des analyseurs syntaxiques pour du code dynamique (par exemple, pour l'interprétation de scripts ou l'analyse à la volée), vous devriez typiquement :
  1. Générer les fichiers `.java` programmatiquement (par exemple, en les écrivant dans un répertoire temporaire comme `System.getProperty("java.io.tmpdir")`).
  2. Les compiler en utilisant l'API Java Compiler (javax.tools.JavaCompiler) ou une bibliothèque comme Janino.
     - Exemple : Définir la sortie de compilation vers un répertoire personnalisé, tel que `new File("generated/classes")`.
     - Les fichiers `.class` compilés sont stockés dans ce répertoire. À l'exécution, utilisez un ClassLoader personnalisé pour les charger à partir de là ou de tampons mémoire.
  - **Valeur par défaut de la JVM** : Sans chemins personnalisés, les classes pourraient aller dans `target/classes` par défaut si vous utilisez des outils de build, ou dans tout répertoire que vous spécifiez dans la tâche de compilation.

- **Scénarios dynamiques courants** :
  - **Compilation en mémoire** : Les bibliothèques comme l'API Compiler permettent de compiler sans écrire sur le disque, en stockant le bytecode en mémoire via `ClassLoader.defineClass()`. Aucun stockage physique n'a lieu.
  - **Stockage temporaire** : Si le code généré est compilé et persisté, il va souvent dans `/tmp/` sur les systèmes de type Unix ou dans des dossiers temporaires. Pour les applications en production, utilisez un répertoire dédié `generated/` ou `cache/` dans le système de fichiers de votre projet.
  - **Frameworks** : Des outils comme ANTLR (alternative à JavaCC) ou des exécuteurs personnalisés peuvent automatiser cela, en stockant les classes en RAM ou dans un dossier du classpath (par exemple, des entrées `CLASSPATH`).

### Considérations clés et bonnes pratiques
- **Sécurité à l'exécution** : La compilation dynamique de code comporte des risques (par exemple, des problèmes de sécurité). Assurez-vous que les grammaires générées par l'utilisateur sont sandboxées.
- **Intégration des outils de build** : Si vous utilisez Maven ou Gradle, les plugins JavaCC (par exemple, `javacc-maven-plugin`) génèrent dans `target/generated-sources/javacc/` pour les sources et `target/classes/` pour les classes compilées, configurable dans votre `pom.xml` ou `build.gradle`.
- **Débogage** : Si la compilation échoue, vérifiez la sortie d'erreur ou les journaux de JavaCC. Les fichiers générés sont généralement stockés là où votre application s'exécute, pas globalement.
- **Preuve provenant de la documentation** : Selon le guide officiel de JavaCC (javacc.github.io ou la documentation legacy), la sortie est basée sur un répertoire et la gestion post-compilation est à la charge de l'utilisateur. Des exemples concrets dans des dépôts GitHub (par exemple, cherchez l'utilisation de JavaCC) montrent des répertoires de sortie personnalisés comme `src/main/generated/`.

Si cela ne correspond pas à votre configuration (par exemple, un framework ou un IDE spécifique), fournissez plus de détails comme votre extrait de code ou votre environnement, et je pourrai affiner la réponse !