---
audio: false
generated: true
lang: fr
layout: post
title: Maven Dependency Plugin
translated: true
---

Le **Maven Dependency Plugin** est un outil puissant dans Maven, un outil d'automatisation de build largement utilisé pour les projets Java, qui vous aide à gérer et manipuler les dépendances de votre projet. Les dépendances dans un projet Maven sont des bibliothèques ou modules externes déclarés dans le fichier `pom.xml`, que Maven télécharge depuis des dépôts et rend disponibles pendant la compilation, l'exécution ou les tests. Le Dependency Plugin étend cette fonctionnalité en fournissant divers objectifs (tâches) pour analyser, copier, lister ou autrement gérer ces dépendances. Voici comment l'utiliser efficacement :

---

#### **1. Vue d'ensemble de l'utilisation**
Vous pouvez utiliser le Maven Dependency Plugin de deux manières principales :
- **Le configurer dans le fichier `pom.xml`** : Cela vous permet de lier des objectifs spécifiques du plugin à des phases du cycle de vie de build de Maven (par exemple, `package`, `install`) pour une exécution automatique pendant le processus de build.
- **Exécuter des objectifs directement depuis la ligne de commande** : Cela est idéal pour des tâches ponctuelles ou lorsque vous ne souhaitez pas modifier le `pom.xml`.

Le plugin est identifié par ses coordonnées : `groupId: org.apache.maven.plugins`, `artifactId: maven-dependency-plugin`. Vous devrez spécifier une version (par exemple, `3.2.0`) lors de sa configuration, bien que Maven puisse souvent résoudre la dernière version si elle est omise dans l'utilisation en ligne de commande.

---

#### **2. Ajouter le plugin à `pom.xml`**
Pour utiliser le plugin dans votre processus de build, ajoutez-le à la section `<build><plugins>` de votre `pom.xml`. Voici un exemple de base :

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
        </plugin>
    </plugins>
</build>
```

Avec cette configuration, vous pouvez configurer des objectifs spécifiques à exécuter pendant le cycle de vie du build en ajoutant des blocs `<executions>`.

---

#### **3. Objectifs courants et comment les utiliser**
Le plugin fournit plusieurs objectifs pour gérer les dépendances. Voici quelques-uns des plus couramment utilisés, avec des exemples de leur utilisation :

##### **a. `copy-dependencies`**
- **But** : Copie les dépendances du projet dans un répertoire spécifié (par exemple, pour les regrouper dans un dossier `lib`).
- **Configuré dans `pom.xml`** :
  Liez cet objectif à la phase `package` pour copier les dépendances pendant `mvn package` :

  ```xml
  <build>
      <plugins>
          <plugin>
              <groupId>org.apache.maven.plugins</groupId>
              <artifactId>maven-dependency-plugin</artifactId>
              <version>3.2.0</version>
              <executions>
                  <execution>
                      <id>copy-dependencies</id>
                      <phase>package</phase>
                      <goals>
                          <goal>copy-dependencies</goal>
                      </goals>
                      <configuration>
                          <outputDirectory>${project.build.directory}/lib</outputDirectory>
                          <includeScope>runtime</includeScope>
                      </configuration>
                  </execution>
              </executions>
          </plugin>
      </plugins>
  </build>
  ```

  - `${project.build.directory}/lib` se résout en `target/lib` dans votre projet.
  - `<includeScope>runtime</includeScope>` limite la copie aux dépendances avec les portées `compile` et `runtime`, excluant `test` et `provided`.

- **Ligne de commande** :
  Exécutez-le directement sans modifier `pom.xml` :

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib
  ```

##### **b. `tree`**
- **But** : Affiche l'arbre des dépendances, montrant toutes les dépendances directes et transitives et leurs versions. Cela est utile pour identifier les conflits de versions.
- **Ligne de commande** :
  Exécutez simplement :

  ```bash
  mvn dependency:tree
  ```

  Cela affiche une vue hiérarchique des dépendances dans la console.
- **Configuré dans `pom.xml`** (optionnel) :
  Si vous souhaitez que cela s'exécute pendant une phase de build (par exemple, `verify`), configurez-le de manière similaire à `copy-dependencies`.

##### **c. `analyze`**
- **But** : Analyse les dépendances pour identifier des problèmes, tels que :
  - Les dépendances utilisées mais non déclarées.
  - Les dépendances déclarées mais non utilisées.
- **Ligne de commande** :
  Exécutez :

  ```bash
  mvn dependency:analyze
  ```

  Cela génère un rapport dans la console.
- **Note** : Cet objectif peut nécessiter une configuration supplémentaire pour des projets complexes afin d'affiner son analyse.

##### **d. `list`**
- **But** : Liste toutes les dépendances résolues du projet.
- **Ligne de commande** :
  Exécutez :

  ```bash
  mvn dependency:list
  ```

  Cela fournit une liste plate des dépendances, utile pour une référence rapide.

##### **e. `unpack`**
- **But** : Extrait le contenu d'une dépendance spécifique (par exemple, un fichier JAR) dans un répertoire.
- **Ligne de commande** :
  Exemple pour décompresser une dépendance spécifique :

  ```bash
  mvn dependency:unpack -Dartifact=groupId:artifactId:version -DoutputDirectory=target/unpacked
  ```

  Remplacez `groupId:artifactId:version` par les coordonnées de la dépendance (par exemple, `org.apache.commons:commons-lang3:3.12.0`).

##### **f. `purge-local-repository`**
- **But** : Supprime les dépendances spécifiées de votre dépôt Maven local (`~/.m2/repository`), forçant un nouveau téléchargement depuis les dépôts distants.
- **Ligne de commande** :
  Exécutez :

  ```bash
  mvn dependency:purge-local-repository
  ```

  Cela est utile pour résoudre les fichiers de dépendance corrompus.

---

#### **4. Options de personnalisation**
De nombreux objectifs supportent des paramètres de configuration pour adapter leur comportement :
- **`outputDirectory`** : Spécifie où copier ou décompresser les fichiers (par exemple, `target/lib`).
- **`includeScope` ou `excludeScope`** : Filtre les dépendances par portée (par exemple, `runtime`, `test`).
- **`artifact`** : Cible une dépendance spécifique pour des objectifs comme `unpack`.

Celles-ci peuvent être définies dans la section `<configuration>` du `pom.xml` ou passées en arguments de ligne de commande avec `-D` (par exemple, `-DincludeScope=runtime`).

---

#### **5. Exemples pratiques**
- **Scénario 1 : Emballage d'une application autonome**
  Utilisez `copy-dependencies` pour regrouper toutes les dépendances d'exécution dans un dossier `lib` :

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
  ```

- **Scénario 2 : Débogage des conflits de dépendances**
  Exécutez `dependency:tree` pour inspecter les dépendances transitives :

  ```bash
  mvn dependency:tree
  ```

  Si vous repérez plusieurs versions d'une bibliothèque (par exemple, `commons-logging`), résolvez le conflit en ajoutant une section `<dependencyManagement>` dans `pom.xml`.

- **Scénario 3 : Extraction des ressources**
  Décompressez une dépendance pour accéder à son contenu :

  ```bash
  mvn dependency:unpack -Dartifact=org.example:my-lib:1.0.0 -DoutputDirectory=target/resources
  ```

---

#### **6. Résumé**
Pour utiliser le Maven Dependency Plugin :
- Ajoutez-le à votre `pom.xml` avec des objectifs et configurations spécifiques si vous souhaitez qu'il soit intégré dans votre processus de build.
- Exécutez des objectifs comme `copy-dependencies`, `tree`, `analyze`, `list`, ou `unpack` directement depuis la ligne de commande pour des tâches ponctuelles.
- Personnalisez le comportement avec des options de configuration pour répondre aux besoins de votre projet.

Ce plugin est un outil polyvalent pour gérer les dépendances au-delà de la simple déclaration, le rendant inestimable pour la construction, le débogage et la distribution des projets Maven.