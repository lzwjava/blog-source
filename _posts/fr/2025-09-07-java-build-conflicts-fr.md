---
audio: false
date: 2025-09-07
generated: true
image: false
lang: fr
layout: post
title: Résoudre les conflits de version de build Java
translated: true
type: note
---

Vous compilez avec **Java 8** (version de classe 52.0), mais certains plugins/libs de build dans votre POM ont été compilés pour des versions plus récentes de Java. Le premier à causer un problème est **Spotless** (version de classe 55.0 = Java 11). Vous avez également d'autres éléments nécessitant Java 11+ qui poseront problème même si Spotless est supprimé (Checkstyle 10.x, Logback 1.5, et le namespace Jakarta Servlet 5 vs le namespace javax de Spring 5).

Voici deux solutions propres pour résoudre ce problème. Choisissez-en une et tout fonctionnera.

---

## Option A — Rester sur Java 8 (fonctionne avec Spring 5.2.x et Jetty 9.4)

* Supprimez/retrogradez les plugins et libs nécessitant Java 11+.
* Utilisez **javax.servlet-api 4.0.1** (Spring 5 utilise `javax.*`, pas `jakarta.*`).
* Gardez Jetty 9.4 (ère Servlet 3.1/4).

Collez ce POM (seules les parties ci-dessous diffèrent du vôtre) :

```xml
<project>
  ...
  <properties>
    <maven.compiler.source>8</maven.compiler.source>
    <maven.compiler.target>8</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <!-- Spring 5.x est compatible -->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-web</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-webmvc</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-core</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>

    <!-- Dépendances de test inchangées -->
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter-api</artifactId>
      <version>5.13.1</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter-engine</artifactId>
      <version>5.13.1</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.mockito</groupId>
      <artifactId>mockito-core</artifactId>
      <version>5.18.0</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-test</artifactId>
      <version>5.2.2.RELEASE</version>
      <scope>test</scope>
    </dependency>

    <!-- AOP ok -->
    <dependency>
      <groupId>org.aspectj</groupId>
      <artifactId>aspectjrt</artifactId>
      <version>1.9.24</version>
    </dependency>
    <dependency>
      <groupId>org.aspectj</groupId>
      <artifactId>aspectjweaver</artifactId>
      <version>1.9.24</version>
    </dependency>

    <!-- SLF4J 2.0 est Java 8+, OK -->
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-api</artifactId>
      <version>2.0.17</version>
    </dependency>

    <!-- ↓ Rétrogradez Logback vers la ligne compatible Java 8 -->
    <dependency>
      <groupId>ch.qos.logback</groupId>
      <artifactId>logback-classic</artifactId>
      <version>1.2.13</version>
    </dependency>

    <!-- ↓ Utilisez javax servlet pour Spring 5.x + Jetty 9.4 -->
    <dependency>
      <groupId>javax.servlet</groupId>
      <artifactId>javax.servlet-api</artifactId>
      <version>4.0.1</version>
      <scope>provided</scope>
    </dependency>

    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-lang3</artifactId>
      <version>3.17.0</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <!-- Gardez votre exec-maven-plugin si vous avez besoin de JavadocRemover -->
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.1</version>
        <executions>
          <execution>
            <id>remove-javadoc</id>
            <phase>compile</phase>
            <goals><goal>java</goal></goals>
            <configuration>
              <mainClass>org.lzw.JavadocRemover</mainClass>
              <arguments><argument>src/main</argument></arguments>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <!-- ↓ SUPPRIMEZ Spotless ou conditionnez-le derrière un profil Java 11+.
           Si vous voulez absolument l'utiliser sur Java 8, utilisez une ancienne version de Spotless + JDK8,
           mais la solution la plus simple est de le supprimer pour l'instant. -->
      <!-- (Bloc de plugin Spotless supprimé) -->

      <!-- ↓ Checkstyle : choisissez un moteur compatible Java 8 -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-checkstyle-plugin</artifactId>
        <version>3.1.2</version>
        <dependencies>
          <dependency>
            <groupId>com.puppycrawl.tools</groupId>
            <artifactId>checkstyle</artifactId>
            <version>9.3</version>
          </dependency>
        </dependencies>
        <configuration>
          <configLocation>${project.basedir}/checks.xml</configLocation>
          <failOnViolation>true</failOnViolation>
        </configuration>
        <executions>
          <execution>
            <id>checkstyle-check</id>
            <phase>compile</phase>
            <goals><goal>check</goal></goals>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
        <configuration>
          <failOnMissingWebXml>true</failOnMissingWebXml>
        </configuration>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.5.3</version>
      </plugin>

      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals><goal>prepare-agent</goal></goals>
          </execution>
          <execution>
            <id>report</id>
            <phase>verify</phase>
            <goals><goal>report</goal></goals>
          </execution>
        </executions>
      </plugin>

      <!-- Jetty 9.4 fonctionne sur Java 8 + javax.servlet -->
      <plugin>
        <groupId>org.eclipse.jetty</groupId>
        <artifactId>jetty-maven-plugin</artifactId>
        <version>9.4.54.v20240208</version>
        <configuration>
          <httpConnector><port>8080</port></httpConnector>
          <webApp><contextPath>/</contextPath></webApp>
        </configuration>
      </plugin>
    </plugins>
  </build>

  <!-- Gardez votre profil 'python-integration-tests',
       mais notez que spring-boot-maven-plugin 3.5.0 nécessite Java 17+.
       LAISSEZ ce profil INACTIF lors de la compilation sur Java 8. -->
  <profiles>
    <profile>
      <id>python-integration-tests</id>
      <build>
        <plugins>
          <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version>
            <executions>
              <execution>
                <id>prepare-agent-integration</id>
                <goals><goal>prepare-agent-integration</goal></goals>
                <configuration>
                  <destFile>${project.build.directory}/jacoco-it.exec</destFile>
                  <propertyName>jacoco.agent.it</propertyName>
                </configuration>
              </execution>
            </executions>
          </plugin>

          <!-- Laissez ce plugin Boot ici mais N'ACTIVEZ PAS ce profil sur Java 8 -->
          <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <version>3.5.0</version>
          </plugin>

          <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.5.1</version>
            <executions>
              <execution>
                <id>python-integration-tests</id>
                <phase>integration-test</phase>
                <goals><goal>exec</goal></goals>
                <configuration>
                  <executable>python</executable>
                  <workingDirectory>${project.basedir}</workingDirectory>
                  <arguments>
                    <argument>-m</argument><argument>unittest</argument>
                    <argument>discover</argument><argument>tests/</argument>
                    <argument>-v</argument>
                  </arguments>
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

Puis exécutez :

```bash
mvn -v                # confirmez l'utilisation d'un JDK 1.8.x
mvn clean package
# ou pour le développement
mvn jetty:run
```

---

## Option B — Mettre à jour votre JDK de build (Java 17 est un bon choix)

* Passez votre **build** à JDK 17+ (et `mvn -v` doit afficher Java 17).
* Gardez Spotless et Checkstyle 10.x tels quels.
* Vous pouvez garder `jakarta.servlet-api` **seulement si** vous passez également l'exécution à Jetty 11+ ou Tomcat 10+ et migrez votre code vers les namespaces `jakarta.*` (monde Spring 6 / Spring Boot 3). Si vous restez sur Spring 5.2.x, utilisez `javax.servlet-api:4.0.1` et un conteneur Servlet 4 à la place.

Commandes typiques :

```bash
# Sur Ubuntu, installez un JDK 17 et sélectionnez-le :
sudo apt install openjdk-17-jdk
sudo update-alternatives --config java
sudo update-alternatives --config javac

mvn -v             # doit afficher la version Java 17
mvn clean package
```

Si vous devez toujours générer du bytecode Java 8 tout en compilant sur Java 17, définissez :

```xml
<properties>
  <maven.compiler.release>8</maven.compiler.release>
</properties>
```

(Mais notez : les dépendances comme Logback 1.5 nécessitent Java 11+ de toute façon, donc votre **runtime** doit être 11+ si vous les incluez.)

---

## Pourquoi cela a échoué (version courte)

* `UnsupportedClassVersionError ... class file version 55.0` = plugin/library compilé avec **Java 11**, mais Maven exécuté sous **Java 8**.
* Vos contrevenants spécifiques sur Java 8 :

  * Spotless plugin 2.44.5 (Java 11+)
  * Checkstyle 10.25.0 (Java 11+)
  * Logback 1.5.x (Java 11+)
  * `jakarta.servlet-api:5.0.0` est incompatible avec le `javax.*` de Spring 5 et Jetty 9.4.

---

Si vous me dites quelle voie vous préférez (rester sur Java 8 vs passer à Java 17+), je peux ajuster le POM exactement pour cette configuration et, si nécessaire, vous donner les diffs minimaux pour votre `web.xml`/configuration Spring et votre choix de Jetty/Tomcat.