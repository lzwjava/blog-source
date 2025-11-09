---
audio: false
date: 2025-09-07
generated: true
image: false
lang: de
layout: post
title: Auflösen von Java-Build-Versionskonflikten
translated: true
type: note
---

Sie verwenden **Java 8** (Class-Datei 52.0), aber einige Build-Plugins/Bibliotheken in Ihrer POM wurden für neuere Java-Versionen kompiliert. Das erste Problem verursacht **Spotless** (Class-Datei 55.0 = Java 11). Sie haben auch einige andere Java-11+-Elemente, die Probleme bereiten werden, selbst wenn Spotless entfernt wird (Checkstyle 10.x, Logback 1.5 und der Jakarta Servlet 5 vs. Spring 5's javax-Namespace).

Unten finden Sie zwei saubere Lösungen. Wählen Sie eine aus und das Problem ist behoben.

---

## Option A — Bei Java 8 bleiben (funktioniert mit Spring 5.2.x und Jetty 9.4)

* Entfernen/Setzen Sie Java-11+-Plugins und Bibliotheken zurück.
* Verwenden Sie **javax.servlet-api 4.0.1** (Spring 5 verwendet `javax.*`, nicht `jakarta.*`).
* Behalten Sie Jetty 9.4 (Servlet 3.1/4 Ära) bei.

Fügen Sie diese POM ein (nur die untenstehenden Teile unterscheiden sich von Ihrer):

```xml
<project>
  ...
  <properties>
    <maven.compiler.source>8</maven.compiler.source>
    <maven.compiler.target>8</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <!-- Spring 5.x ist in Ordnung -->
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

    <!-- Test-Abhängigkeiten unverändert -->
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

    <!-- SLF4J 2.0 ist Java 8+, OK -->
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-api</artifactId>
      <version>2.0.17</version>
    </dependency>

    <!-- ↓ Logback auf Java-8-kompatible Version downgraden -->
    <dependency>
      <groupId>ch.qos.logback</groupId>
      <artifactId>logback-classic</artifactId>
      <version>1.2.13</version>
    </dependency>

    <!-- ↓ javax servlet für Spring 5.x + Jetty 9.4 verwenden -->
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
      <!-- Behalten Sie exec-maven-plugin, falls Sie JavadocRemover benötigen -->
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

      <!-- ↓ ENTFERNEN Sie Spotless oder schalten Sie es hinter ein Java-11+-Profil frei.
           Wenn Sie es wirklich auf Java 8 verwenden möchten, nutzen Sie ein altes Spotless + JDK8,
           aber am einfachsten ist es, es jetzt zu entfernen. -->
      <!-- (Spotless Plugin-Block entfernt) -->

      <!-- ↓ Checkstyle: Java-8-kompatible Engine wählen -->
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

      <!-- Jetty 9.4 funktioniert gut mit Java 8 + javax.servlet -->
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

  <!-- Behalten Sie Ihr 'python-integration-tests'-Profil,
       aber beachten Sie, dass spring-boot-maven-plugin 3.5.0 Java 17+ benötigt.
       Schalten Sie dieses Profil AUS, wenn Sie mit Java 8 bauen. -->
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

          <!-- Lassen Sie dieses Boot-Plugin hier, aber aktivieren Sie dieses Profil NICHT unter Java 8 -->
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

Dann führen Sie aus:

```bash
mvn -v                # Bestätigen, dass ein JDK 1.8.x verwendet wird
mvn clean package
# oder für die Entwicklung
mvn jetty:run
```

---

## Option B — Ihr Build-JDK upgraden (Java 17 ist ein guter Kompromiss)

* Wechseln Sie Ihren **Build** zu JDK 17+ (und `mvn -v` sollte Java 17 anzeigen).
* Behalten Sie Spotless und Checkstyle 10.x wie sie sind.
* Sie können `jakarta.servlet-api` **nur dann** behalten, wenn Sie auch die Runtime auf Jetty 11+ oder Tomcat 10+ umstellen und Ihren Code auf `jakarta.*`-Namespaces migrieren (Spring 6 / Spring Boot 3 Welt). Wenn Sie bei Spring 5.2.x bleiben, verwenden Sie `javax.servlet-api:4.0.1` und einen Servlet-4-Container stattdessen.

Typische Befehle:

```bash
# Unter Ubuntu, installieren Sie ein JDK 17 und wählen es aus:
sudo apt install openjdk-17-jdk
sudo update-alternatives --config java
sudo update-alternatives --config javac

mvn -v             # sollte Java Version 17 ausgeben
mvn clean package
```

Wenn Sie immer noch Java-8-Bytecode generieren müssen, während Sie auf Java 17 bauen, setzen Sie:

```xml
<properties>
  <maven.compiler.release>8</maven.compiler.release>
</properties>
```

(Aber beachten Sie: Abhängigkeiten wie Logback 1.5 sind sowieso Java 11+, also muss Ihre **Runtime** 11+ sein, wenn Sie sie einbinden.)

---

## Warum es fehlgeschlagen ist (Kurzversion)

* `UnsupportedClassVersionError ... class file version 55.0` = Plugin/Bibliothek kompiliert mit **Java 11**, aber Maven lief unter **Java 8**.
* Ihre spezifischen Problemverursacher unter Java 8:

  * Spotless Plugin 2.44.5 (Java 11+)
  * Checkstyle 10.25.0 (Java 11+)
  * Logback 1.5.x (Java 11+)
  * `jakarta.servlet-api:5.0.0` passt nicht zu Spring 5's `javax.*` und Jetty 9.4.

---

Wenn Sie mir mitteilen, welchen Weg Sie bevorzugen (bei Java 8 bleiben vs. zu Java 17+ wechseln), werde ich die POM genau für diesen Setup optimieren und Ihnen, falls nötig, die minimalen Unterschiede für Ihre `web.xml`/Spring-Konfiguration und Jetty/Tomcat-Auswahl geben.