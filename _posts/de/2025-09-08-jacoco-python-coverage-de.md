---
audio: false
date: 2025-09-08
generated: true
image: false
lang: de
layout: post
title: Abdeckungsstrategie mit JaCoCo für Python-Tests
translated: true
type: note
---

# Analyse und Strategie für JaCoCo-Abdeckung mit Python-Integrationstests

## Analyse der aktuellen Situation

Sie haben ein Multi-Modul-Maven-Projekt eingerichtet mit:
- Parent POM (`PlaygroundLib`)
- `PlaygroundUtils`-Modul (JAR mit Utility-Klassen)
- `PlaygroundWeb`-Modul (WAR mit Spring MVC Controllern)

Ihr Ziel ist es, Pythons `unittest` zu verwenden, um API-Endpunkte zu testen und Abdeckungsberichte für den Java-Code zu generieren. Die Herausforderung besteht darin, dass die Python-Tests außerhalb des Java-Projekts liegen und Sie Jetty ausführen müssen, um die Anwendung während des Testens zu bedienen.

## Probleme mit dem aktuellen Ansatz

1. **Problem mehrfacher Ausführungen**: Sie führen `PlaygroundWeb` mehrfach aus, um separate Abdeckungsberichte für verschiedene Module zu generieren, was ineffizient ist.

2. **Skalierbarkeitsbedenken**: Dieser Ansatz skaliert nicht gut mit mehr Modulen. Für ein Projekt mit 10 Modulen wären 10 separate Ausführungen erforderlich.

3. **Fragmentierte Abdeckung**: Pro-Modul-Berichte erschweren die ganzheitliche Betrachtung der Abdeckung über die gesamte Anwendung hinweg.

## Empfohlene Strategie

### 1. Konsolidierter Ansatz zur Abdeckungserfassung

Anstatt die Anwendung mehrfach auszuführen, empfehle ich:

1. **Webanwendung einmal ausführen** mit angehängtem JaCoCo-Agent
2. **Alle Python-Integrationstests ausführen** gegen diese einzelne Instanz
3. **Konsolidierten Abdeckungsbericht generieren**, der alle Module enthält

Dieser Ansatz ist effizienter und bietet eine einheitliche Sicht auf die Abdeckung Ihrer gesamten Anwendung.

### 2. Implementierungsschritte

#### Änderungen am Parent POM (`PlaygroundLib`)

Fügen Sie ein Profil für Integrationstests mit JaCoCo hinzu:

```xml
<profiles>
    <profile>
        <id>integration-test</id>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.jacoco</groupId>
                    <artifactId>jacoco-maven-plugin</artifactId>
                    <executions>
                        <execution>
                            <id>merge</id>
                            <phase>post-integration-test</phase>
                            <goals>
                                <goal>merge</goal>
                            </goals>
                            <configuration>
                                <fileSets>
                                    <fileSet>
                                        <directory>${project.basedir}</directory>
                                        <includes>
                                            <include>*/target/jacoco-it.exec</include>
                                        </includes>
                                    </fileSet>
                                </fileSets>
                                <destFile>${project.build.directory}/jacoco-merged.exec</destFile>
                            </configuration>
                        </execution>
                        <execution>
                            <id>report-merged</id>
                            <phase>verify</phase>
                            <goals>
                                <goal>report</goal>
                            </goals>
                            <configuration>
                                <dataFile>${project.build.directory}/jacoco-merged.exec</dataFile>
                                <outputDirectory>${project.reporting.outputDirectory}/jacoco-merged</outputDirectory>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
```

#### Änderungen am PlaygroundWeb POM

Ändern Sie die JaCoCo-Agent-Konfiguration, um alle Module einzubeziehen:

```xml
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
                    -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.build.directory}/jacoco-it.exec,includes=org.lzw.*
                </jvmArgs>
                <!-- Rest der Konfiguration bleibt gleich -->
            </configuration>
        </execution>
        <!-- Rest der Executions bleibt gleich -->
    </executions>
</plugin>
```

Beachten Sie die Ergänzung von `includes=org.lzw.*` in der JaCoCo-Agent-Konfiguration. Dies stellt sicher, dass alle Klassen im `org.lzw`-Package (über alle Module hinweg) in den Abdeckungsbericht aufgenommen werden.

### 3. Ausführungsablauf

Der empfohlene Ausführungsablauf wäre:

```bash
# Alle Module bauen
mvn clean install

# Integrationstests mit Abdeckung ausführen
mvn verify -Pintegration-test
```

Dies wird:
1. Alle Module kompilieren
2. Jetty mit angehängtem JaCoCo-Agent starten
3. Python-Integrationstests ausführen
4. Jetty stoppen
5. Einen zusammengeführten Abdeckungsbericht für alle Module generieren

### 4. Skalierung auf größere Projekte

Für ein größeres Projekt mit zehn Modulen:

1. **Web-Module** (wie `PlaygroundWeb`) würden konfiguriert, um die Anwendung mit angehängtem JaCoCo-Agent auszuführen.
2. **Utility-Module** (wie `PlaygroundUtils`) würden keine spezielle Konfiguration benötigen.
3. Das Parent POM würde das Zusammenführen der Abdeckungsdaten aller Module handhaben.

Wenn Sie mehrere Web-Module haben, die unabhängig getestet werden müssen, könnten Sie separate Maven-Profile für jedes Web-Modul erstellen und Integrationstests für jedes separat ausführen, dann alle Abdeckungsdaten auf Parent-Ebene zusammenführen.

### 5. Umgang mit JaCoCo-Komplexität

Um die Komplexität von JaCoCo zu managen:

1. **Kapseln Sie die Konfiguration** in Maven-Profilen, um das Haupt-POM sauber zu halten
2. **Dokumentieren Sie den Prozess** klar, damit Teammitglieder verstehen, wie Tests ausgeführt und Berichte generiert werden
3. **Erwägen Sie CI/CD-Automatisierung**, um die manuelle Komplexität für Entwickler zu reduzieren

## Zusammenfassung

Der empfohlene Ansatz konsolidiert die Abdeckungserfassung, indem die Webanwendung einmal mit angehängtem JaCoCo-Agent ausgeführt wird, alle Python-Integrationstests gegen diese Instanz ausgeführt werden und ein konsolidierter Abdeckungsbericht generiert wird. Dieser Ansatz ist effizienter, skalierbarer und bietet eine einheitliche Sicht auf die Abdeckung Ihrer gesamten Anwendung.

Diese Strategie sollte Ihre aktuellen Herausforderungen lösen und gut skalieren, wenn Ihr Projekt wächst, während gleichzeitig die Verwaltung der JaCoCo-Komplexität vereinfacht wird.