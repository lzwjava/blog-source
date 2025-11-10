---
audio: false
generated: true
image: false
lang: de
layout: post
title: Jacoco Multi-Module Spring Coverage Setup
translated: true
type: note
---

Gut – JaCoCo funktioniert gut für ein Multi-Modul Spring-Projekt. Sie benötigen:

1.  Unit-Test-Abdeckung pro Modul;
2.  Einen aggregierten Bericht auf der Eltern-Ebene;
3.  Ein optionales Profil, um **Integrations**-Abdeckung zu erfassen (z.B. Liberty+EAR-Lauf, getroffen durch Python-Tests).

Unten finden Sie eine erprobte Einrichtung, die Sie übernehmen können.

---

### Eltern-`pom.xml` (Packaging `pom`)

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

  <!-- Aggregierter Bericht für ALLE Unit-Tests der Module -->
  <reporting>
    <plugins>
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <reportSets>
          <reportSet>
            <reports>
              <!-- Dies löst 'report-aggregate' aus, wenn Sie 'mvn verify' auf der Eltern-Ebene ausführen -->
              <report>report-aggregate</report>
            </reports>
            <configuration>
              <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
              <!-- Optionale globale Filter -->
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

  <!-- Profil zum Hinzufügen von INTEGRATIONS-Abdeckung (z.B. Liberty + Python-Tests) -->
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
              <!-- Erstellt einen aggregierten Bericht, der auch externe .exec-Dateien einliest -->
              <execution>
                <id>report-aggregate-it</id>
                <phase>verify</phase>
                <goals><goal>report-aggregate</goal></goals>
                <configuration>
                  <!-- Zeigt auf eine oder mehrere .exec-Dateien, die vom Liberty JVM-Agenten erzeugt wurden -->
                  <dataFiles>
                    <!-- Beispielpfade; passen Sie diese an Ihren CI/Liberty-Ort an -->
                    <dataFile>${project.basedir}/.jacoco/jacoco-it.exec</dataFile>
                    <!-- Sie können weitere dataFile-Einträge hinzufügen, wenn Sie pro Node speichern und alle einbeziehen möchten -->
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

### Jedes Kindmodul (`ChatCommon/pom.xml`, `ChatLib/pom.xml`, `ChatCore/pom.xml`, `ChatWeb/pom.xml`)

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
      <!-- Agent für UNIT-Tests in diesem Modul anhängen -->
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals><goal>prepare-agent</goal></goals>
            <configuration>
              <!-- Platziert die argLine in eine benannte Property, um sie mit anderen Args zu mischen -->
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
          <!-- Optional: Mindestwerte durchsetzen -->
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

      <!-- Sicherstellen, dass Surefire den Agenten verwendet -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${surefireArgLine}</argLine>
        </configuration>
      </plugin>

      <!-- (Optional) Failsafe für modulinterne ITs -->
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

> Machen Sie dasselbe in `ChatLib`, `ChatCore` und `ChatWeb`.
> Für `ChatWeb` (ein Spring Boot WAR/JAR) ist die Konfiguration identisch.

---

### Ausführung

**Unit-Test-Abdeckung über Module hinweg (aggregiertes XML auf der Eltern-Ebene):**

```bash
mvn -q clean verify
# XML:  target/site/jacoco-aggregate/jacoco.xml
# HTML: target/site/jacoco-aggregate/index.html
```

**Integrations-Abdeckung von Liberty + Python-Tests:**

1.  Starten Sie Liberty mit dem JaCoCo-Agenten (wie zuvor besprochen), führen Sie Python-Tests aus, stoppen Sie oder geben Sie einen Dump aus.
    Stellen Sie sicher, dass die `.exec`-Datei unter `${project.basedir}/.jacoco/jacoco-it.exec` landet (oder passen Sie den Pfad im Eltern-Profil an).
2.  Bauen Sie die Aggregation inklusive IT-Daten:

```bash
mvn -q -Pit-coverage verify
# XML:  target/site/jacoco-aggregate-it/jacoco.xml
# HTML: target/site/jacoco-aggregate-it/index.html
```

---

### Hinweise, die Zeit sparen

*   **Aggregation funktioniert nur von der Eltern-Ebene** (Packaging `pom`) mit deklarierten Modulen. Führen Sie `mvn` aus dem Eltern-Verzeichnis aus.
*   **XML** (`jacoco.xml`) wird erzeugt, wenn Sie es in `<reports>` aktivieren; dies wird von Codecov/Sonar verwendet.
*   Wenn Sie mehrere `.exec`-Dateien sammeln (z.B. mehrere Liberty-Nodes), können Sie entweder:

    *   alle unter `<dataFiles>…</dataFiles>` im `it-coverage`-Profil auflisten, oder
    *   sie zuerst zusammenführen (mit `jacococli.jar merge …`) und dann auf die zusammengeführte Datei zeigen.
*   Zeigen Sie nicht mit classfiles auf das EAR; JaCoCos Bericht benötigt die **kompilierten Klassen der Module** (`*/target/classes`) und Quellen – dies wird automatisch von `report-aggregate` behandelt.
*   Wenn Surefire ebenfalls eine eigene `argLine` setzt, lassen Sie `${jacocoArgLine}` an erster Stelle, damit der Agent nicht verloren geht.

Wenn Sie Ihre genauen Modul-Package-Roots und den Ort, an dem Ihre Liberty-`.exec`-Datei landet, mitteilen, kann ich `<dataFiles>` und etwaige Ausschlüsse anpassen, damit Ihr aggregiertes XML sauber und CI-ready ist.