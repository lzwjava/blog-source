---
audio: false
date: 2025-09-08
generated: true
image: false
lang: fr
layout: post
title: Stratégie de couverture d'intégration mono JVM
translated: true
type: note
---

Vous n'avez pas besoin d'exécuter Jetty deux fois ou de créer un fichier `.exec` JaCoCo séparé par module. Un agent sur la JVM unique qui sert votre WAR peut enregistrer la couverture pour **toutes les classes que cette JVM charge** — y compris `PlaygroundUtils` — dans **un seul fichier exec partagé**. Ensuite, chaque module peut générer son propre rapport en pointant vers ce même fichier exec. Pour un réacteur de taille importante (10+ modules), cette approche s'adapte proprement.

Voici un plan concret et minimal, ainsi que les modifications prêtes à l'emploi pour votre dépôt.

---

## La stratégie

1.  **Utiliser un seul fichier exec d'intégration partagé au niveau parent.**
    Démarrer Jetty **une seule fois**, instrumenté avec JaCoCo, écrivant dans `../target/it-coverage/jacoco-it.exec` (un chemin défini au niveau parent).
2.  **Exécuter vos tests Python externes une seule fois.**
    Ils accèdent à l'application déployée ; l'agent enregistre les accès pour toutes les classes chargées (web + libs).
3.  **Générer des rapports par module**, chaque module pointant vers le `jacoco-it.exec` partagé.
    `PlaygroundUtils` obtiendra un rapport même s'il n'a pas de tests — il mappe le fichier exec partagé à son propre `target/classes`.
4.  (Optionnel) **Générer également un rapport HTML agrégé** au niveau parent avec `report-aggregate`, ou simplement conserver les rapports par module.

Ce n'est que lorsque vous avez véritablement **plusieurs JVM** (par exemple, plusieurs microservices) que vous avez besoin de plusieurs fichiers exec et d'une étape `jacoco:merge`. Pour votre build actuel avec une seule JVM (Jetty), conservez un seul fichier exec.

---

## Modifications exactes

### 1) `pom.xml` parent (PlaygroundLib)

Ajoutez des propriétés partagées pour que chaque module puisse référencer le même fichier exec :

```xml
<properties>
  <!-- ... vos versions existantes ... -->
  <it.coverage.dir>${project.basedir}/target/it-coverage</it.coverage.dir>
  <jacoco.it.exec>${it.coverage.dir}/jacoco-it.exec</jacoco.it.exec>
  <!-- Activer/Désactiver la génération du rapport d'intégration par module -->
  <it.report.skip>false</it.report.skip>
</properties>
```

(Optionnel) Si vous souhaitez un seul rapport **agrégé** HTML au niveau parent, ajoutez cette exécution :

```xml
<build>
  <pluginManagement>
    <!-- conservez vos blocs existants -->
  </pluginManagement>

  <plugins>
    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>it-aggregate-report</id>
          <phase>verify</phase>
          <goals>
            <goal>report-aggregate</goal>
          </goals>
          <configuration>
            <!-- Utiliser le fichier exec d'intégration partagé produit par l'exécution Jetty -->
            <dataFile>${jacoco.it.exec}</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

> Si votre version de JaCoCo rejette `<dataFile>` sur `report-aggregate`, ignorez ce bloc optionnel et fiez-vous aux rapports par module ci-dessous. Vous pouvez toujours ajouter plus tard un petit module agrégateur de "couverture" pour exécuter `merge` + `report`.

---

### 2) `PlaygroundWeb/pom.xml`

Faites pointer l'agent Jetty vers le chemin défini au **niveau parent** et activez l'ajout (`append`) :

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.parent.basedir}/target/it-coverage/jacoco-it.exec,append=true,includes=org.lzw.*
        </jvmArgs>
        <httpConnector>
          <port>8080</port>
          <host>127.0.0.1</host>
        </httpConnector>
        <webApp><contextPath>/</contextPath></webApp>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals><goal>stop</goal></goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

Mettez à jour votre `jacoco:report` dans `PlaygroundWeb` pour lire le **même** fichier exec partagé :

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
      <configuration>
        <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
        <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

Votre Exec Maven Plugin existant qui exécute `python -m unittest discover tests -v` est parfait — laissez-le tel quel.

---

### 3) `PlaygroundUtils/pom.xml`

Ajoutez une exécution de **rapport uniquement** pour qu'il puisse mapper le fichier exec partagé à ses propres classes :

```xml
<build>
  <plugins>
    <!-- conservez vos plugins existants -->

    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>report-it</id>
          <phase>verify</phase>
          <goals><goal>report</goal></goals>
          <configuration>
            <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
            <skip>${it.report.skip}</skip>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

Ce module ne démarre jamais Jetty ni n'exécute de tests Python ; il se contente de consommer le fichier exec partagé et son propre `target/classes`. Si des classes de `PlaygroundUtils` sont utilisées par l'application web pendant les tests, elles apparaîtront avec une couverture. Si elles ne sont pas exercées, elles seront à 0% — ce qui est le signal correct.

---

## Comment l'exécuter

Depuis la racine du dépôt :

```bash
mvn -pl PlaygroundWeb -am clean verify
```

L'ordre de compilation compile les deux modules, démarre Jetty une fois avec l'agent, exécute vos tests Python, arrête Jetty, puis génère :

*   `PlaygroundWeb/target/site/jacoco-it/index.html`
*   `PlaygroundUtils/target/site/jacoco-it/index.html`
*   Optionnellement, un rapport agrégé sous le module parent si vous avez activé `report-aggregate`.

---

## Quand vous avez 10 modules

*   Si les 10 modules finissent dans le **même WAR/JVM**, conservez le modèle du **fichier exec unique partagé**. Chaque module ajoute une exécution `report` qui pointe vers le fichier exec partagé. Vous démarrez toujours Jetty une fois et exécutez les tests Python une fois.

*   Si vous avez **plusieurs JVM** (par exemple, des services séparés), donnez à chaque JVM son propre `destfile` (par exemple, `it-coverage/serviceA.exec`, `serviceB.exec`), puis exécutez au niveau parent :

    ```xml
    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>merge-it</id>
          <phase>post-integration-test</phase>
          <goals><goal>merge</goal></goals>
          <configuration>
            <destFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</destFile>
            <files>
              <file>${project.basedir}/target/it-coverage/serviceA.exec</file>
              <file>${project.basedir}/target/it-coverage/serviceB.exec</file>
              <!-- ajoutez-en plus si nécessaire -->
            </files>
          </configuration>
        </execution>

        <execution>
          <id>aggregate-report</id>
          <phase>verify</phase>
          <goals><goal>report-aggregate</goal></goals>
          <configuration>
            <dataFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
          </configuration>
        </execution>
      </executions>
    </plugin>
    ```

*   Si vous voulez limiter le bruit, définissez `includes=org.lzw.*` (déjà montré) ou ajoutez `excludes` à la ligne de l'agent pour filtrer les librairies tierces.

---

## Pourquoi votre problème actuel se produit

*   Vous créiez **des fichiers exec par module**, vous vous sentiez donc obligé de ré-exécuter Jetty avec différents agents pour remplir chacun d'eux. C'est inutile. L'agent ne se soucie pas du module auquel une classe "appartient" — il enregistre toute classe chargée. Centralisez le fichier exec et faites pointer le `report` de chaque module vers celui-ci.

---

## Liste de contrôle rapide

*   Un **fichier exec partagé** `${jacoco.it.exec}` sous le module parent.
*   Jetty démarré **une fois** avec `append=true` et `includes=org.lzw.*`.
*   Les tests Python exécutés **une fois**.
*   Chaque module a un `jacoco:report` qui lit le fichier exec partagé.
*   Optionnellement, un `report-aggregate` parent pour un seul rapport HTML de haut niveau.

Cela devrait rendre votre configuration à la fois plus simple et plus évolutive. Si vous le souhaitez, je peux produire les diffs exacts pour vos POM actuels avec ces modifications appliquées.