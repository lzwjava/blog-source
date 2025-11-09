---
audio: false
date: 2025-09-08
generated: true
image: false
lang: de
layout: post
title: Abdeckungsberichterstattungsstrategie für Jacoco-Multi-Module-Projekte
translated: true
type: note
---

Selbstverständlich. Ihre Analyse trifft den Kern, insbesondere was die Komplexitäten von JaCoCo mit externen Integrationstests betrifft. Den Build zweimal auszuführen, ist definitiv nicht ideal.

Die Strategie, nach der Sie suchen, beinhaltet die Zentralisierung der Testausführung und die anschließende Aggregation der Ergebnisse. Sie sind auf der richtigen Spur, und das `aggregate`-Goal ist tatsächlich das richtige Werkzeug, es muss jedoch in einer bestimmten Weise für dieses Szenario angewendet werden.

Hier ist die empfohlene Strategie: **Generieren Sie eine einzige Coverage-Datei (`.exec`) in Ihrem Webanwendungsmodul und verwenden Sie dann ein separates, dediziertes Reporting-Modul, um einen einzelnen, aggregierten Bericht für alle relevanten Module zu erstellen.**

Dieser Ansatz ist sauber, skalierbar und vermeidet redundante Builds.

-----

## Das Grundkonzept

Wenn Ihre `PlaygroundWeb`-Anwendung auf Jetty mit dem JaCoCo-Agenten läuft, instrumentiert der Agent **alle Klassen, die durch den Classloader der Anwendung geladen werden**. Dies schließt Klassen von `PlaygroundWeb` selbst *und* alle seine Abhängigkeiten, wie `PlaygroundUtils.jar`, ein.

Daher enthält die einzelne, während des `PlaygroundWeb`-Builds generierte `jacoco-it.exec`-Datei bereits die Coverage-Daten für **beide Module**. Die Herausforderung besteht lediglich darin, das JaCoCo-Reporting-Tool auf den Quellcode aller Module zu verweisen, die es für die Erstellung des endgültigen HTML-Reports benötigt.

-----

## Eine skalierbare Strategie in 4 Schritten

Hier eine Schritt-für-Schritt-Anleitung, um Ihr Projekt für sauberes, aggregiertes Coverage-Reporting umzustrukturieren.

### Schritt 1: Erstellen Sie ein dediziertes Reporting-Modul

Erstellen Sie zunächst ein neues Modul ausschließlich für die Aggregation. Dies ist eine Maven-Best-Practice, die die Zuständigkeiten trennt.

1.  Fügen Sie in Ihrer Root-`pom.xml` (`PlaygroundLib`) das neue Modul hinzu:
    ```xml
    <modules>
        <module>PlaygroundUtils</module>
        <module>PlaygroundWeb</module>
        <module>PlaygroundReports</module> </modules>
    ```
2.  Erstellen Sie ein neues Verzeichnis `PlaygroundReports` im Root mit einer eigenen `pom.xml`.

Ihre neue Projektstruktur wird so aussehen:

```
.
├── PlaygroundReports
│   └── pom.xml
├── PlaygroundUtils
│   └── pom.xml
├── PlaygroundWeb
│   └── pom.xml
└── pom.xml
```

### Schritt 2: Konfigurieren Sie die `pom.xml` des Reporting-Moduls

In dieser neuen `pom.xml` passiert die Magie. Es wird von allen Modulen abhängen, die Sie im Bericht haben möchten, und wird das `report-aggregate`-Goal ausführen.

**`PlaygroundReports/pom.xml`:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.lzw</groupId>
        <artifactId>PlaygroundLib</artifactId>
        <version>1.0</version>
    </parent>
    <artifactId>PlaygroundReports</artifactId>
    <packaging>pom</packaging>
    <name>PlaygroundReports</name>

    <dependencies>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundWeb</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundUtils</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <executions>
                    <execution>
                        <id>aggregate-report</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>report-aggregate</goal>
                        </goals>
                        <configuration>
                            <dataFiles>
                                <dataFile>${project.basedir}/../PlaygroundWeb/target/jacoco-it.exec</dataFile>
                            </dataFiles>
                            <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### Schritt 3: Vereinfachen Sie das `PlaygroundWeb`-Modul

Ihr `PlaygroundWeb`-Modul ist jetzt nur noch für die **Generierung der Coverage-Daten** verantwortlich, nicht für die Berichterstellung darüber. Sie können die `jacoco:report`-Execution aus seiner `pom.xml` entfernen.

**`PlaygroundWeb/pom.xml` (nur Änderungen):**

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
            <configuration>
                <propertyName>jacoco.it.agent</propertyName>
                <destFile>${project.build.directory}/jacoco-it.exec</destFile>
            </configuration>
        </execution>
        </executions>
</plugin>

<plugin>
    <groupId>org.eclipse.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>start-jetty</id>
            <phase>pre-integration-test</phase>
            <goals>
                <goal>start</goal>
            </goals>
            <configuration>
                <daemon>true</daemon>
                <jvmArgs>
                    ${jacoco.it.agent}
                </jvmArgs>
                </configuration>
        </execution>
        </executions>
</plugin>
```

*Hinweis*: Ich habe die `prepare-agent`-Konfiguration leicht modifiziert, um eine Property (`jacoco.it.agent`) zu verwenden und diese dann im `jetty-maven-plugin` zu referenzieren. Dies ist eine robuste Methode, um den Agent-String zu übergeben. Die vorherige Konfiguration in Ihrer `pom.xml` war auch in Ordnung, aber dies macht die Absicht klarer.

### Schritt 4: Bereinigen Sie `PlaygroundUtils`

Das `PlaygroundUtils`-Modul benötigt keine JaCoCo-Plugin-Konfiguration für Integrationstests. Sein Code wird über `PlaygroundWeb` gecovered, und die Berichterstellung wird von `PlaygroundReports` übernommen. Sie können alle JaCoCo-bezogenen Properties oder Plugins aus seiner `pom.xml` entfernen.

-----

## Wie dies das Problem löst

1.  **Einmaliger Build:** Sie führen `mvn clean verify` nur einmal aus dem Root-Verzeichnis aus.
2.  **Korrekter Lifecycle:**
      * Maven baut `PlaygroundUtils`.
      * Maven baut `PlaygroundWeb`, startet Jetty mit dem JaCoCo-Agenten, führt Ihre Python-Tests aus (die Code in beiden Modulen aufrufen), stoppt Jetty und erzeugt `PlaygroundWeb/target/jacoco-it.exec`.
      * Maven baut `PlaygroundReports`. In der `verify`-Phase wird das `report-aggregate`-Goal ausgeführt. Es findet die `.exec`-Datei von `PlaygroundWeb` und findet, aufgrund der Abhängigkeiten, den Quellcode für sowohl `PlaygroundWeb` als auch `PlaygroundUtils`.
      * Es generiert einen **einzigen, vereinheitlichten HTML-Report** mit Coverage für beide Module.
3.  **Skalierbarkeit:** Wenn Sie zehn weitere Bibliotheksmodule hinzufügen, fügen Sie diese einfach als Abhängigkeiten in der `PlaygroundReports/pom.xml` hinzu. Die Kernlogik ändert sich nicht. Dies ist die saubere, skalierbare Lösung, nach der Sie gesucht haben.