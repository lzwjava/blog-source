---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Comprendre l'Intégration de JaCoCo et Maven
translated: true
type: note
---

Compris — voici comment les éléments JaCoCo dans **votre POM exact** fonctionnent ensemble, étape par étape, et pourquoi.

---

# Les deux flux de couverture que ce POM crée

1. **Couverture des tests unitaires (chemin Surefire)**

* Vous liez l'objectif **`prepare-agent`** de JaCoCo sans configuration spéciale :

  ```xml
  <execution>
    <id>prepare-agent</id>
    <goals><goal>prepare-agent</goal></goals>
  </execution>
  ```

  Ceci injecte `-javaagent:...org.jacoco.agent-<ver>-runtime.jar` dans la JVM de test **Surefire** via la propriété `argLine`.
  • Le **destfile** par défaut est `${project.build.directory}/jacoco.exec`.
  • Le **append** par défaut est `true` (l'agent JaCoCo ajoute au fichier s'il existe déjà).
  • Effet : lorsque vous exécutez les tests unitaires (s'il y en a) pendant `test`, la couverture va dans `target/jacoco.exec`.

2. **Couverture des tests d'intégration (chemin Jetty)**

* Vous définissez un **fichier séparé** pour la couverture des tests d'intégration :

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
  </properties>
  ```
* Vous démarrez Jetty **avec son propre agent JaCoCo** pointant vers ce fichier :

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
        </jvmArgs>
        ...
      </configuration>
    </execution>
  </plugin>
  ```

  • Jetty s'exécute dans une **JVM distincte** ; son agent écrit dans `target/jacoco-it.exec`.
  • Parce que `append` n'est pas spécifié, la valeur par défaut de JaCoCo `append=true` s'applique — donc plusieurs lancements de Jetty ajoutent au même fichier sauf si vous faites un `clean` ou définissez `append=false`.

---

# Flux du lifecycle (ce qui se passe sur `mvn verify`)

1. **compile**

   * Spotless formate (`spotless-maven-plugin`) et Checkstyle s'exécute (`maven-checkstyle-plugin`).
   * Votre WAR est préparé (`maven-war-plugin`).

2. **test (Surefire)**

   * Si vous avez des tests unitaires, ils s'exécutent sous l'`argLine` injecté par **`prepare-agent`** → la couverture va dans `target/jacoco.exec`.

3. **pre-integration-test**

   * Jetty est démarré **en mode démon** :

     ```xml
     <daemon>true</daemon>
     ```

     Maven reprend immédiatement le contrôle ; Jetty continue de tourner avec l'agent JaCoCo attaché, écrivant dans `jacoco-it.exec`.

4. **integration-test**

   * Vos tests Python accèdent à l'application en cours d'exécution :

     ```xml
     <plugin>
       <artifactId>exec-maven-plugin</artifactId>
       <execution>
         <id>python-integration-tests</id>
         <phase>integration-test</phase>
         <goals><goal>exec</goal></goals>
         <configuration>
           <executable>python3</executable>
           <workingDirectory>${project.parent.basedir}</workingDirectory>
           <arguments>
             <argument>-m</argument><argument>unittest</argument>
             <argument>discover</argument><argument>tests/</argument>
             <argument>-v</argument>
           </arguments>
         </configuration>
       </execution>
     </plugin>
     ```

     Ces tests sollicitent Jetty, donc la couverture s'accumule dans **`target/jacoco-it.exec`** via l'agent de la JVM Jetty.

5. **post-integration-test**

   * Jetty est arrêté proprement :

     ```xml
     <execution>
       <id>stop-jetty</id>
       <phase>post-integration-test</phase>
       <goals><goal>stop</goal></goals>
       ...
     </execution>
     ```

6. **verify**

   * Vous générez un **rapport de tests d'intégration séparé** en utilisant le fichier de données des tests d'intégration et un répertoire de sortie personnalisé :

     ```xml
     <execution>
       <id>report-it</id>
       <phase>verify</phase>
       <goals><goal>report</goal></goals>
       <configuration>
         <dataFile>${jacoco.it.exec}</dataFile>
         <outputDirectory>${project.reporting.outputDirectory}/jacoco-it
         </outputDirectory>
       </configuration>
     </execution>
     ```
   * Résultat : le HTML est généré dans `target/site/jacoco-it/index.html` résumant uniquement la couverture des **tests d'intégration** (depuis Jetty).

> Note : Si vous voulez aussi un rapport de **tests unitaires**, vous pourriez ajouter une autre exécution `jacoco:report` qui pointe vers le `target/jacoco.exec` par défaut et sort dans `target/site/jacoco` — gardant ainsi les rapports unitaires et d'intégration séparés.

---

# À propos de « créer un nouveau ou remplacer ? » pour les fichiers `.exec`

* **La valeur par défaut de l'agent JaCoCo est `append=true`**.

  * Pour **les tests unitaires**, le fichier est `target/jacoco.exec`. Lorsque vous exécutez `mvn verify` répétitivement **sans `clean`**, les données peuvent s'ajouter d'une exécution à l'autre.
  * Pour **les tests d'intégration Jetty**, votre `jvmArgs` ne remplace pas `append`, donc `target/jacoco-it.exec` **ajoute** aussi par défaut.

**Bonnes pratiques** (pour éviter de mélanger d'anciennes données) :

* Exécutez `mvn clean verify`, **ou** ajoutez `append=false` dans la ligne de l'agent Jetty :

  ```xml
  -javaagent:...org.jacoco.agent-...-runtime.jar=destfile=${jacoco.it.exec},append=false
  ```
* Si jamais vous voulez fusionner plusieurs fichiers `.exec` intentionnellement, utilisez `jacoco:merge` avant `jacoco:report`.

---

# Ce que chaque bloc pertinent dans votre XML original fait (par référence)

* **Emplacement du fichier de tests d'intégration**

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
    <it.report.skip>false</it.report.skip>
  </properties>
  ```

  Définit où la couverture des tests d'intégration est stockée. `it.report.skip` est déclaré mais pas encore connecté à l'exécution du rapport (voir l'astuce ci-dessous).

* **Agent des tests unitaires (chemin Surefire)**

  ```xml
  <plugin>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>prepare-agent</id>
        <goals><goal>prepare-agent</goal></goals>
      </execution>
      ...
    </executions>
  </plugin>
  ```

* **Jetty avec JaCoCo pour les tests d'intégration**

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <jvmArgs>
      -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
    </jvmArgs>
    ...
  </plugin>
  ```

* **Tests d'intégration Python pendant l'exécution de Jetty**

  ```xml
  <plugin>
    <artifactId>exec-maven-plugin</artifactId>
    <execution>
      <id>python-integration-tests</id>
      <phase>integration-test</phase>
      <goals><goal>exec</goal></goals>
      ...
    </execution>
  </plugin>
  ```

* **Générer le rapport de couverture des tests d'intégration à `verify`**

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

---

# Conseils pratiques / petites améliorations

* **Éviter les données de tests d'intégration obsolètes**
  Ajoutez `append=false` à l'agent Jetty (montré ci-dessus), ou exécutez toujours `mvn clean verify`.

* **Connectez votre interrupteur `it.report.skip`**
  Si vous voulez sauter la génération du rapport de tests d'intégration via une propriété :

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <skip>${it.report.skip}</skip>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

* **Garder les rapports unitaires et d'intégration séparés**
  Vous avez déjà séparé le rapport de tests d'intégration vers `site/jacoco-it`. Si vous avez aussi besoin du rapport unitaire, ajoutez un autre `jacoco:report` (sans remplacement de `dataFile`) écrivant vers `site/jacoco`.

* **Note multi-module**
  Cette configuration locale au module rapporte la couverture pour **PlaygroundWeb** uniquement. Si plus tard vous voulez une vue **combinée**, utilisez `jacoco:merge` (pour combiner les fichiers `.exec`) et/ou `report-aggregate` depuis un `pom` parent avec `packaging=pom` (JaCoCo 0.8.8+).

---

# TL;DR

* **Tests unitaires** → `prepare-agent` injecte JaCoCo dans la JVM Surefire → `target/jacoco.exec`.
* **Tests d'intégration** → Jetty démarre avec son propre agent JaCoCo → `target/jacoco-it.exec`.
* **Rapport** → À `verify`, `jacoco:report` génère **uniquement la couverture des tests d'intégration** vers `target/site/jacoco-it`.
* **Comportement des fichiers** → JaCoCo **ajoute par défaut** ; préférez `mvn clean verify` ou `append=false` pour éviter de mélanger les exécutions.