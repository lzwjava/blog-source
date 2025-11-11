---
audio: false
generated: true
lang: fr
layout: post
title: Compatibilité des versions de Java avec Spring Boot
translated: true
type: note
---

### Comprendre l'erreur

Lorsque vous exécutez `mvn spring-boot:run` avec Spring Boot 3.4.3 et que vous rencontrez l'erreur "class file has wrong version 61.0, should be 52.0", cela indique un problème de compatibilité de version Java. En Java, les fichiers de classe ont un numéro de version correspondant à la version de Java avec laquelle ils ont été compilés :

- **La version 52.0** correspond à Java 8.
- **La version 61.0** correspond à Java 17.

L'erreur suggère que les fichiers de classe de votre application Spring Boot ont été compilés avec Java 17 (version 61.0), mais la Machine Virtuelle Java (JVM) qui tente de les exécuter attend des fichiers de classe compatibles avec Java 8 (version 52.0). Étant donné que la JVM de Java 8 ne peut pas exécuter des fichiers de classe compilés avec Java 17 (car Java est rétrocompatible mais pas compatible vers l'avant dans ce contexte), vous obtenez cette erreur.

### Pourquoi cela arrive

Spring Boot 3.4.3 nécessite **Java 17 ou une version ultérieure** comme version minimale prise en charge. Cela signifie que votre projet doit être à la fois compilé et exécuté en utilisant au moins Java 17. L'inadéquation se produit probablement parce que :

1. **Compilation** : Votre projet est configuré pour compiler avec Java 17, produisant des fichiers de classe de version 61.0. Ceci est généralement défini dans votre `pom.xml` avec le `maven-compiler-plugin` ou la propriété `<java.version>`.
2. **Temps d'exécution** : Lorsque vous exécutez `mvn spring-boot:run`, le plugin Maven Spring Boot lance un nouveau processus Java pour exécuter l'application. Cependant, l'exécutable `java` qu'il utilise provient d'une installation Java 8 (version 52.0), qui ne peut pas gérer les fichiers de classe compilés avec Java 17.

### Étapes pour corriger le problème

Pour résoudre ceci, vous devez vous assurer que l'environnement de compilation et celui d'exécution utilisent tous deux Java 17. Voici comment le corriger :

#### 1. Vérifier la version Java de votre projet
Tout d'abord, confirmez que votre projet est configuré pour utiliser Java 17. Dans votre `pom.xml`, vérifiez la présence des éléments suivants :

```xml
<properties>
    <java.version>17</java.version>
</properties>
```

Cette propriété indique au `maven-compiler-plugin` de compiler votre code avec Java 17. Spring Boot 3.4.3 définit ceci par défaut, mais il est bon de le vérifier. S'il est manquant ou défini sur une version différente (par exemple, 8), mettez-le à jour vers 17.

#### 2. Installer Java 17
Assurez-vous que Java 17 est installé sur votre système. Vous pouvez le télécharger depuis :

- [Adoptium (Eclipse Temurin)](https://adoptium.net/)
- [Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) (si vous acceptez les conditions de licence)

Pour vérifier si Java 17 est installé, ouvrez un terminal et exécutez :

```bash
java -version
```

Si cela n'affiche pas Java 17 (par exemple, `openjdk 17.x.x` ou similaire), installez-le et poursuivez.

#### 3. Mettre à jour votre environnement pour utiliser Java 17
Le plugin Maven Spring Boot utilise l'exécutable `java` de votre environnement, généralement déterminé par la variable d'environnement `JAVA_HOME` ou la commande `java` dans le PATH de votre système. Si votre commande `java` actuelle pointe vers Java 8, vous devez la mettre à jour.

##### Option A : Définir JAVA_HOME et PATH
Définissez votre variable d'environnement `JAVA_HOME` pour qu'elle pointe vers l'installation de Java 17 et assurez-vous que la commande `java` dans votre PATH l'utilise.

- **Sur Linux/Mac** :
  1. Trouvez votre répertoire d'installation de Java 17 (par exemple, `/usr/lib/jvm/java-17-openjdk` ou l'endroit où vous l'avez installé).
  2. Définissez `JAVA_HOME` et mettez à jour `PATH` dans votre terminal :
     ```bash
     export JAVA_HOME=/chemin/vers/java-17
     export PATH=$JAVA_HOME/bin:$PATH
     ```
  3. Vérifiez :
     ```bash
     java -version
     ```
     Cela devrait maintenant afficher Java 17.

  Pour rendre cela permanent, ajoutez les lignes `export` à votre fichier de configuration de shell (par exemple, `~/.bashrc`, `~/.zshrc`).

- **Sur Windows** :
  1. Trouvez le répertoire d'installation de Java 17 (par exemple, `C:\Program Files\Java\jdk-17`).
  2. Définissez `JAVA_HOME` :
     - Ouvrez la fenêtre des Propriétés système (recherchez "Variables d'environnement" dans le menu Démarrer).
     - Sous "Variables système", ajoutez ou modifiez `JAVA_HOME` pour qu'elle pointe vers `C:\Program Files\Java\jdk-17`.
  3. Mettez à jour `Path` :
     - Dans "Variables système", modifiez `Path` et ajoutez `%JAVA_HOME%\bin` (assurez-vous qu'il est en haut ou supprimez les anciens chemins Java comme Java 8).
  4. Ouvrez une nouvelle invite de commande et vérifiez :
     ```cmd
     java -version
     ```
     Cela devrait afficher Java 17.

##### Option B : Utiliser une version Java spécifique pour Maven
Si vous avez plusieurs versions de Java installées et que vous ne souhaitez pas modifier votre `JAVA_HOME` à l'échelle du système, vous pouvez exécuter Maven avec une version Java spécifique :

- Avant d'exécuter `mvn spring-boot:run`, définissez `JAVA_HOME` uniquement pour cette commande :
  ```bash
  JAVA_HOME=/chemin/vers/java-17 mvn spring-boot:run
  ```
  Cela garantit que le plugin Maven Spring Boot utilise Java 17 sans modifier les paramètres de votre système.

#### 4. Exécuter à nouveau l'application
Une fois Java 17 correctement configuré, exécutez :

```bash
mvn spring-boot:run
```

Le plugin utilisera maintenant Java 17 pour exécuter votre application, correspondant à la version des fichiers de classe compilés (61.0), et l'erreur devrait disparaître.

### Vérifications supplémentaires
- **Version Java de Maven** : Exécutez `mvn -version` pour voir quelle version de Java Maven utilise. Elle doit correspondre à votre `JAVA_HOME`. Si ce n'est pas le cas, assurez-vous que votre PATH et `JAVA_HOME` sont correctement configurés.
- **Dépendances** : Si l'erreur persiste, une dépendance pourrait être compilée avec Java 17 alors que votre environnement d'exécution est toujours mal configuré. Étant donné que Spring Boot 3.4.3 impose Java 17, s'assurer que votre environnement d'exécution est Java 17 devrait résoudre ce problème.

### Pourquoi pas Java 8 ?
Spring Boot 3.4.3 ne prend pas en charge Java 8. Si vous devez utiliser Java 8, vous devriez revenir à une ancienne version de Spring Boot (par exemple, 2.x), mais ce n'est pas recommandé à moins de contraintes spécifiques. Étant donné que vos fichiers de classe sont en version 61.0, rester sur Java 17 est conforme aux exigences de Spring Boot 3.4.3.

### Résumé de la solution finale
Pour corriger "class file has wrong version 61.0, should be 52.0" lors de l'exécution de `mvn spring-boot:run` avec Spring Boot 3.4.3 :

1. Assurez-vous que `<java.version>17</java.version>` est présent dans votre `pom.xml`.
2. Installez Java 17 s'il n'est pas déjà présent.
3. Définissez `JAVA_HOME` sur votre répertoire d'installation de Java 17.
4. Mettez à jour votre PATH pour que `java -version` affiche Java 17.
5. Exécutez à nouveau `mvn spring-boot:run`.

Cela garantit que votre environnement d'exécution correspond à vos fichiers de classe compilés en Java 17, résolvant le problème de compatibilité.