---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Configuration de Couverture Multi-Module Spring avec JaCoCo
translated: true
type: note
---

Parfait — JaCoCo fonctionne bien pour un projet Spring multi-module. Vous aurez besoin de :

1. une couverture de tests unitaires par module ;
2. un rapport agrégé au niveau parent ;
3. un profil optionnel pour intégrer la couverture des **tests d'intégration** (ex: exécution Liberty+EAR testée par des tests Python).

Voici une configuration éprouvée que vous pouvez utiliser directement.

---

### Parent `pom.xml` (packaging `pom`)

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.myco.chat</groupId>
  <artifactId>chat-parent</artifactId>
  <version>1.0.0</version>
  <packaging>pom</packaging>

  <modules>
    <module>ChatCommon</module>
    <module>ChatLib</module>
    <module>ChatCore</module>
    <module>ChatWeb</module>
  </modules>

  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>org.jacoco</groupId>
          <artifactId>jacoco-maven-plugin</artifactId>
          <version>0.8.12</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>3.2.5</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-failsafe-plugin</artifactId>
          <version>3.2.5</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>

  <!-- Rapport agrégé pour les tests unitaires de TOUS les modules -->
  <reporting>
    <plugins>
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <reportSets>
          <reportSet>
            <reports>
              <!-- Ceci déclenche 'report-aggregate' quand vous exécutez 'mvn verify' au niveau parent -->
              <report>report-aggregate</report>
            </reports>
            <configuration>
              <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
              <!-- Filtres globaux optionnels -->
              <excludes>
                <exclude>**/*Application.class</exclude>
                <exclude>**/*Configuration.class</exclude>
                <exclude>**/generated/**</exclude>
              </excludes>
            </configuration>
          </reportSet>
        </reportSets>
      </plugin>
    </plugins>
  </reporting>

  <!-- Profil pour ajouter la couverture d'INTÉGRATION (ex: Liberty + tests Python) -->
  <profiles>
    <profile>
      <id>it-coverage</id>
      <activation><activeByDefault>false</activeByDefault></activation>
      <build>
        <plugins>
          <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version>
            <executions>
              <!-- Créer un rapport agrégé qui lit aussi les fichiers .exec externes -->
              <execution>
                <id>report-aggregate-it</id>
                <phase>verify</phase>
                <goals><goal>report-aggregate</goal></goals>
                <configuration>
                  <!-- Pointer vers un ou plusieurs fichiers .exec générés par l'agent JVM Liberty -->
                  <dataFiles>
                    <!-- Exemples de chemins ; ajustez selon votre environnement CI/Liberty -->
                    <dataFile>${project.basedir}/.jacoco/jacoco-it.exec</dataFile>
                    <!-- Vous pouvez ajouter plus d'entrées dataFile si vous voulez tous les fichiers par nœud -->
                  </dataFiles>
                  <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate-it</outputDirectory>
                  <reports>
                    <xml>true</xml>
                    <html>true</html>
                    <csv>false</csv>
                  </reports>
                  <excludes>
                    <exclude>**/generated/**</exclude>
                  </excludes>
                </configuration>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    </profile>
  </profiles>
</project>
```

---

### Chaque module enfant (`ChatCommon/pom.xml`, `ChatLib/pom.xml`, `ChatCore/pom.xml`, `ChatWeb/pom.xml`)

```xml
<project>
  <parent>
    <groupId>com.myco.chat</groupId>
    <artifactId>chat-parent</artifactId>
    <version>1.0.0</version>
  </parent>
  <modelVersion>4.0.0</modelVersion>
  <artifactId>ChatCommon</artifactId>
  <packaging>jar</packaging>

  <build>
    <plugins>
      <!-- Attacher l'agent pour les tests UNITAIRES dans ce module -->
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals><goal>prepare-agent</goal></goals>
            <configuration>
              <!-- Placer l'argLine dans une propriété nommée, pour pouvoir la mixer avec d'autres arguments -->
              <propertyName>jacocoArgLine</propertyName>
              <append>true</append>
              <excludes>
                <exclude>**/generated/**</exclude>
              </excludes>
            </configuration>
          </execution>
          <execution>
            <id>report</id>
            <phase>verify</phase>
            <goals><goal>report</goal></goals>
            <configuration>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
            </configuration>
          </execution>
          <!-- Optionnel : appliquer des minimums -->
          <execution>
            <id>check</id>
            <goals><goal>check</goal></goals>
            <configuration>
              <rules>
                <rule>
                  <element>PACKAGE</element>
                  <limits>
                    <limit>
                      <counter>LINE</counter>
                      <value>COVEREDRATIO</value>
                      <minimum>0.60</minimum>
                    </limit>
                    <limit>
                      <counter>BRANCH</counter>
                      <value>COVEREDRATIO</value>
                      <minimum>0.40</minimum>
                    </limit>
                  </limits>
                </rule>
              </rules>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <!-- S'assurer que Surefire utilise l'agent -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${surefireArgLine}</argLine>
        </configuration>
      </plugin>

      <!-- (Optionnel) Failsafe pour les tests d'intégration au niveau module -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-failsafe-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${failsafeArgLine}</argLine>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

> Faites de même dans `ChatLib`, `ChatCore`, et `ChatWeb`.
> Pour `ChatWeb` (un WAR/JAR Spring Boot), la configuration est identique.

---

### Exécution

**Couverture des tests unitaires à travers les modules (XML agrégé au niveau parent) :**

```bash
mvn -q clean verify
# XML:  target/site/jacoco-aggregate/jacoco.xml
# HTML: target/site/jacoco-aggregate/index.html
```

**Couverture d'intégration depuis Liberty + tests Python :**

1. Démarrez Liberty avec l'agent JaCoCo (comme discuté précédemment), exécutez les tests Python, arrêtez ou dump.
   Assurez-vous que le `.exec` se trouve à `${project.basedir}/.jacoco/jacoco-it.exec` (ou mettez à jour ce chemin dans le profil parent).
2. Construisez l'agrégat incluant les données d'intégration :

```bash
mvn -q -Pit-coverage verify
# XML:  target/site/jacoco-aggregate-it/jacoco.xml
# HTML: target/site/jacoco-aggregate-it/index.html
```

---

### Notes qui font gagner du temps

* **L'agrégation fonctionne uniquement depuis le parent** (packaging `pom`) avec les modules déclarés. Exécutez `mvn` depuis le répertoire parent.
* **Le XML** (`jacoco.xml`) est produit quand vous l'activez dans `<reports>` ; c'est ce qu'utilisent Codecov/Sonar.
* Si vous collectez plusieurs fichiers `.exec` (ex: plusieurs nœuds Liberty), soit :

  * listez-les tous sous `<dataFiles>…</dataFiles>` dans le profil `it-coverage`, soit
  * fusionnez-les d'abord (avec `jacococli.jar merge …`) puis pointez vers le fichier fusionné.
* Ne pointez pas les classfiles vers l'EAR ; le rapport JaCoCo a besoin des **classes compilées des modules** (`*/target/classes`) et des sources — géré automatiquement par `report-aggregate`.
* Si Surefire définit aussi son propre `argLine`, gardez `${jacocoArgLine}` en premier pour ne pas perdre l'agent.

Si vous partagez les racines de package exactes de vos modules et l'emplacement final de votre `.exec` Liberty, je peux adapter `<dataFiles>` et toutes les exclusions pour que votre XML agrégé soit propre et prêt pour l'intégration continue.