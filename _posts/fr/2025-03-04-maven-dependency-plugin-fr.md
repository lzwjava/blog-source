---
audio: false
generated: true
lang: fr
layout: post
title: Plugin de Dépendances Maven
translated: true
type: note
---

Le **Maven Dependency Plugin** est un outil puissant dans Maven, un outil d'automatisation de build largement utilisé pour les projets Java, qui vous aide à gérer et manipuler les dépendances du projet. Les dépendances dans un projet Maven sont des bibliothèques externes ou des modules déclarés dans le fichier `pom.xml`, que Maven télécharge depuis des dépôts et rend disponibles pendant la compilation, l'exécution ou les tests. Le Dependency Plugin étend cette fonctionnalité en fournissant divers goals (tâches) pour analyser, copier, lister ou autrement gérer ces dépendances. Voici comment l'utiliser efficacement :

---

#### **1. Aperçu de l'utilisation**
Vous pouvez utiliser le Maven Dependency Plugin de deux manières principales :
- **Le configurer dans le fichier `pom.xml`** : Cela vous permet de lier des goals spécifiques du plugin à des phases du cycle de vie de build Maven (par exemple, `package`, `install`) pour une exécution automatique pendant le processus de build.
- **Exécuter les goals directement depuis la ligne de commande** : C'est idéal pour des tâches ponctuelles ou lorsque vous ne voulez pas modifier le `pom.xml`.

Le plugin est identifié par ses coordonnées : `groupId: org.apache.maven.plugins`, `artifactId: maven-dependency-plugin`. Vous devrez spécifier une version (par exemple, `3.2.0`) lors de sa configuration, bien que Maven puisse souvent résoudre la dernière version si elle est omise dans l'utilisation en ligne de commande.

---

#### **2. Ajouter le plugin au `pom.xml`**
Pour utiliser le plugin dans le cadre de votre processus de build, ajoutez-le à la section `<build><plugins>` de votre `pom.xml`. Voici un exemple basique :

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

Avec cette configuration, vous pouvez configurer des goals spécifiques à exécuter pendant le cycle de vie du build en ajoutant des blocs `<executions>`.

---

#### **3. Goals courants et comment les utiliser**
Le plugin fournit plusieurs goals pour gérer les dépendances. Voici quelques-uns des plus couramment utilisés, avec des exemples d'utilisation :

##### **a. `copy-dependencies`**
- **Objectif** : Copie les dépendances du projet vers un répertoire spécifié (par exemple, pour les empaqueter dans un dossier `lib`).
- **Configuré dans `pom.xml`** :
  Liez ce goal à la phase `package` pour copier les dépendances pendant `mvn package` :

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
  - `<includeScope>runtime</includeScope>` limite la copie aux dépendances avec les scopes `compile` et `runtime`, excluant `test` et `provided`.

- **Ligne de commande** :
  Exécutez-le directement sans modifier le `pom.xml` :

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib
  ```

##### **b. `tree`**
- **Objectif** : Affiche l'arborescence des dépendances, montrant toutes les dépendances directes et transitives ainsi que leurs versions. C'est utile pour identifier les conflits de version.
- **Ligne de commande** :
  Exécutez simplement :

  ```bash
  mvn dependency:tree
  ```

  Cela affiche une vue hiérarchique des dépendances dans la console.
- **Configuré dans `pom.xml`** (optionnel) :
  Si vous voulez que cela s'exécute pendant une phase de build (par exemple, `verify`), configurez-le de manière similaire à `copy-dependencies`.

##### **c. `analyze`**
- **Objectif** : Analyse les dépendances pour identifier des problèmes, tels que :
  - Dépendances utilisées mais non déclarées.
  - Dépendances déclarées mais non utilisées.
- **Ligne de commande** :
  Exécutez :

  ```bash
  mvn dependency:analyze
  ```

  Cela génère un rapport dans la console.
- **Remarque** : Ce goal peut nécessiter une configuration supplémentaire pour les projets complexes afin d'affiner son analyse.

##### **d. `list`**
- **Objectif** : Liste toutes les dépendances résolues du projet.
- **Ligne de commande** :
  Exécutez :

  ```bash
  mvn dependency:list
  ```

  Cela fournit une liste plate des dépendances, utile pour une référence rapide.

##### **e. `unpack`**
- **Objectif** : Extrait le contenu d'une dépendance spécifique (par exemple, un fichier JAR) vers un répertoire.
- **Ligne de commande** :
  Exemple pour décompresser un artifact spécifique :

  ```bash
  mvn dependency:unpack -Dartifact=groupId:artifactId:version -DoutputDirectory=target/unpacked
  ```

  Remplacez `groupId:artifactId:version` par les coordonnées de la dépendance (par exemple, `org.apache.commons:commons-lang3:3.12.0`).

##### **f. `purge-local-repository`**
- **Objectif** : Supprime les dépendances spécifiées de votre dépôt Maven local (`~/.m2/repository`), forçant un nouveau téléchargement depuis les dépôts distants.
- **Ligne de commande** :
  Exécutez :

  ```bash
  mvn dependency:purge-local-repository
  ```

  C'est utile pour résoudre les problèmes liés aux fichiers de dépendances corrompus.

---

#### **4. Options de personnalisation**
De nombreux goals prennent en charge des paramètres de configuration pour adapter leur comportement :
- **`outputDirectory`** : Spécifie où copier ou décompresser les fichiers (par exemple, `target/lib`).
- **`includeScope` ou `excludeScope`** : Filtre les dépendances par scope (par exemple, `runtime`, `test`).
- **`artifact`** : Cible une dépendance spécifique pour des goals comme `unpack`.

Ceux-ci peuvent être définis dans la section `<configuration>` du `pom.xml` ou passés comme arguments en ligne de commande avec `-D` (par exemple, `-DincludeScope=runtime`).

---

#### **5. Exemples pratiques**
- **Scénario 1 : Empaqueter une application autonome**
  Utilisez `copy-dependencies` pour rassembler toutes les dépendances d'exécution dans un dossier `lib` :

  ```bash
  mvn dependency:copy-dependencies -DoutputDirectory=lib -DincludeScope=runtime
  ```

- **Scénario 2 : Déboguer les conflits de dépendances**
  Exécutez `dependency:tree` pour inspecter les dépendances transitives :

  ```bash
  mvn dependency:tree
  ```

  Si vous repérez plusieurs versions d'une bibliothèque (par exemple, `commons-logging`), résolvez le conflit en ajoutant une section `<dependencyManagement>` dans le `pom.xml`.

- **Scénario 3 : Extraire des ressources**
  Décompressez une dépendance pour accéder à son contenu :

  ```bash
  mvn dependency:unpack -Dartifact=org.example:my-lib:1.0.0 -DoutputDirectory=target/resources
  ```

---

#### **6. Résumé**
Pour utiliser le Maven Dependency Plugin :
- Ajoutez-le à votre `pom.xml` avec des goals et configurations spécifiques si vous voulez l'intégrer à votre processus de build.
- Exécutez des goals comme `copy-dependencies`, `tree`, `analyze`, `list` ou `unpack` directement depuis la ligne de commande pour des tâches ponctuelles.
- Personnalisez le comportement avec les options de configuration pour répondre aux besoins de votre projet.

Ce plugin est un outil polyvalent pour gérer les dépendances au-delà de la simple déclaration, le rendant indispensable pour construire, déboguer et distribuer des projets Maven.