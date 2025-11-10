---
audio: false
generated: true
lang: de
layout: post
title: Beherrschen von SonarQube für Java- und Spring-Projekte
translated: true
type: note
---

# Umfassende Anleitung zur Verwendung von SonarQube mit Java- und Spring-Projekten

## Einführung
SonarQube ist eine Open-Source-Plattform für die kontinuierliche Überprüfung der Code-Qualität. Sie führt statische Code-Analysen durch, um Fehler, Code Smells, Sicherheitslücken zu erkennen und berechnet die Code-Abdeckung. Diese Anleitung bietet einen umfassenden Überblick über die Einrichtung und Verwendung von SonarQube in einem Java-Spring-Projekt, einschließlich Installation, Konfiguration, Integration und Best Practices.

## Inhaltsverzeichnis
1. [Was ist SonarQube?](#was-ist-sonarqube)
2. [Voraussetzungen](#voraussetzungen)
3. [Installation von SonarQube](#installation-von-sonarqube)
4. [Einrichtung eines Java-Spring-Projekts](#einrichtung-eines-java-spring-projekts)
5. [Konfiguration von SonarQube für das Projekt](#konfiguration-von-sonarqube-für-das-projekt)
6. [Ausführung der SonarQube-Analyse](#ausführung-der-sonarqube-analyse)
7. [Interpretation der SonarQube-Ergebnisse](#interpretation-der-sonarqube-ergebnisse)
8. [Best Practices](#best-practices)
9. [Behebung häufiger Probleme](#behebung-häufiger-probleme)
10. [Fazit](#fazit)

## Was ist SonarQube?
SonarQube ist ein Tool, das eine kontinuierliche Code-Qualitätsüberprüfung bietet, indem es Quellcode analysiert auf:
- **Bugs**: Potenzielle Fehler im Code.
- **Code Smells**: Wartbarkeitsprobleme, die zu technischen Schulden führen könnten.
- **Sicherheitslücken**: Sicherheitsprobleme, die ausgenutzt werden könnten.
- **Code-Abdeckung**: Prozentsatz des Codes, der durch Unit-Tests abgedeckt ist.
- **Duplikationen**: Wiederholte Code-Blöcke, die refaktorisiert werden könnten.

Es unterstützt mehrere Sprachen, einschließlich Java, und integriert sich nahtlos mit Build-Tools wie Maven und Gradle sowie CI/CD-Pipelines.

## Voraussetzungen
Bevor Sie SonarQube einrichten, stellen Sie sicher, dass Sie Folgendes haben:
- **Java Development Kit (JDK)**: Version 11 oder höher (SonarQube erfordert Java 11 oder 17).
- **Maven oder Gradle**: Build-Tool für das Java-Spring-Projekt.
- **SonarQube Server**: Version 9.9 LTS oder höher (Community Edition ist für die meisten Anwendungsfälle ausreichend).
- **SonarScanner**: CLI-Tool zum Ausführen der Analyse.
- **Datenbank**: SonarQube erfordert eine Datenbank (z.B. PostgreSQL, MySQL oder eingebettete H2 für Tests).
- **Spring-Projekt**: Ein funktionierendes Spring Boot oder Spring Framework Projekt.
- **IDE**: IntelliJ IDEA, Eclipse oder VS Code für die Entwicklung.

## Installation von SonarQube

### Schritt 1: SonarQube herunterladen und installieren
1. **SonarQube herunterladen**:
   - Besuchen Sie die [SonarQube Download-Seite](https://www.sonarqube.org/downloads/).
   - Wählen Sie die Community Edition (kostenlos) oder eine andere Edition basierend auf Ihren Anforderungen.
   - Laden Sie die ZIP-Datei herunter (z.B. `sonarqube-9.9.0.zip`).

2. **ZIP entpacken**:
   - Entpacken Sie die heruntergeladene Datei in ein Verzeichnis, z.B. `/opt/sonarqube` oder `C:\sonarqube`.

3. **Datenbank konfigurieren**:
   - SonarQube erfordert eine Datenbank. Für die Produktion verwenden Sie PostgreSQL oder MySQL. Für Tests ist die eingebettete H2-Datenbank ausreichend.
   - Beispiel für PostgreSQL:
     - Installieren Sie PostgreSQL und erstellen Sie eine Datenbank (z.B. `sonarqube`).
     - Aktualisieren Sie die SonarQube-Konfigurationsdatei (`conf/sonar.properties`):
       ```properties
       sonar.jdbc.url=jdbc:postgresql://localhost:5432/sonarqube
       sonar.jdbc.username=sonarqube_user
       sonar.jdbc.password=sonarqube_pass
       ```

4. **SonarQube starten**:
   - Navigieren Sie zum SonarQube-Verzeichnis (`bin/<platform>`).
   - Führen Sie das Startskript aus:
     - Unter Linux/Mac: `./sonar.sh start`
     - Unter Windows: `StartSonar.bat`
   - Greifen Sie auf SonarQube unter `http://localhost:9000` zu (Standard-Port).

5. **Anmelden**:
   - Standard-Anmeldedaten: `admin/admin`.
   - Ändern Sie das Passwort nach der ersten Anmeldung.

### Schritt 2: SonarScanner installieren
1. **SonarScanner herunterladen**:
   - Laden Sie es von der [SonarQube Scanner Seite](https://docs.sonarqube.org/latest/analyzing-source-code/scanners/sonarscanner/) herunter.
   - Extrahieren Sie es in ein Verzeichnis, z.B. `/opt/sonar-scanner`.

2. **Umgebungsvariablen konfigurieren**:
   - Fügen Sie SonarScanner zu Ihrem PATH hinzu:
     - Unter Linux/Mac: `export PATH=$PATH:/opt/sonar-scanner/bin`
     - Unter Windows: Fügen Sie `C:\sonar-scanner\bin` zum System-PATH hinzu.

3. **Installation überprüfen**:
   - Führen Sie `sonar-scanner --version` aus, um die Installation zu bestätigen.

## Einrichtung eines Java-Spring-Projekts
Für diese Anleitung verwenden wir ein Spring Boot-Projekt mit Maven. Die Schritte sind ähnlich für Gradle oder nicht-Boot Spring-Projekte.

1. **Spring Boot-Projekt erstellen**:
   - Verwenden Sie [Spring Initializer](https://start.spring.io/), um ein Projekt zu erstellen mit:
     - Abhängigkeiten: Spring Web, Spring Data JPA, H2 Database, Spring Boot Starter Test.
     - Build-Tool: Maven.
   - Laden Sie das Projekt herunter und entpacken Sie es.

2. **Unit-Tests hinzufügen**:
   - Stellen Sie sicher, dass Ihr Projekt Unit-Tests hat, um die Code-Abdeckung zu messen.
   - Beispiel-Testklasse:
     ```java
     import org.junit.jupiter.api.Test;
     import org.springframework.boot.test.context.SpringBootTest;

     @SpringBootTest
     public class ApplicationTests {
         @Test
         void contextLoads() {
         }
     }
     ```

3. **Jacoco für Code-Abdeckung hinzufügen**:
   - Fügen Sie das JaCoCo Maven-Plugin zur `pom.xml` hinzu, um Code-Abdeckungsberichte zu generieren:
     ```xml
     <plugin>
         <groupId>org.jacoco</groupId>
         <artifactId>jacoco-maven-plugin</artifactId>
         <version>0.8.8</version>
         <executions>
             <execution>
                 <goals>
                     <goal>prepare-agent</goal>
                 </goals>
             </execution>
             <execution>
                 <id>report</id>
                 <phase>test</phase>
                 <goals>
                     <goal>report</goal>
                 </goals>
             </execution>
         </executions>
     </plugin>
     ```

## Konfiguration von SonarQube für das Projekt

1. **SonarQube-Projekt erstellen**:
   - Melden Sie sich bei SonarQube an (`http://localhost:9000`).
   - Klicken Sie auf **Create Project** > **Manually**.
   - Geben Sie einen **Project Key** (z.B. `my-spring-project`) und einen **Display Name** an.
   - Generieren Sie einen Token zur Authentifizierung (z.B. `my-token`).

2. **`sonar-project.properties` konfigurieren**:
   - Erstellen Sie im Stammverzeichnis Ihres Spring-Projekts eine `sonar-project.properties` Datei:
     ```properties
     sonar.projectKey=my-spring-project
     sonar.projectName=My Spring Project
     sonar.host.url=http://localhost:9000
     sonar.token=my-token
     sonar.java.binaries=target/classes
     sonar.sources=src/main/java
     sonar.tests=src/test/java
     sonar.junit.reportPaths=target/surefire-reports
     sonar.jacoco.reportPaths=target/jacoco.exec
     sonar.sourceEncoding=UTF-8
     ```

3. **Maven-Integration (Alternative)**:
   - Anstelle von `sonar-project.properties` können Sie SonarQube in der `pom.xml` konfigurieren:
     ```xml
     <properties>
         <sonar.host.url>http://localhost:9000</sonar.host.url>
         <sonar.token>my-token</sonar.token>
         <sonar.projectKey>my-spring-project</sonar.projectKey>
         <sonar.projectName>My Spring Project</sonar.projectName>
     </properties>
     <build>
         <plugins>
             <plugin>
                 <groupId>org.sonarsource.scanner.maven</groupId>
                 <artifactId>sonar-maven-plugin</artifactId>
                 <version>3.9.1.2184</version>
             </plugin>
         </plugins>
     </build>
     ```

## Ausführung der SonarQube-Analyse

1. **Verwendung von SonarScanner**:
   - Navigieren Sie zum Projektstammverzeichnis.
   - Führen Sie aus:
     ```bash
     sonar-scanner
     ```
   - Stellen Sie sicher, dass Tests vor der Analyse ausgeführt werden (`mvn test` für Maven-Projekte).

2. **Verwendung von Maven**:
   - Führen Sie aus:
     ```bash
     mvn clean verify sonar:sonar
     ```
   - Dieser Befehl kompiliert den Code, führt Tests aus, generiert Abdeckungsberichte und sendet die Ergebnisse an SonarQube.

3. **Ergebnisse überprüfen**:
   - Öffnen Sie SonarQube (`http://localhost:9000`) und navigieren Sie zu Ihrem Projekt.
   - Überprüfen Sie das Dashboard auf Analyseergebnisse.

## Interpretation der SonarQube-Ergebnisse
Das SonarQube-Dashboard bietet:
- **Übersicht**: Zusammenfassung der Probleme, Abdeckung und Duplikationen.
- **Probleme**: Liste von Bugs, Sicherheitslücken und Code Smells mit Schweregrad (Blocker, Critical, Major, etc.).
- **Code-Abdeckung**: Prozentsatz des durch Tests abgedeckten Codes (via JaCoCo).
- **Duplikationen**: Wiederholte Code-Blöcke.
- **Quality Gate**: Bestehen/Fehlschlag-Status basierend auf vordefinierten Schwellenwerten (z.B. Abdeckung > 80%).

### Beispielaktionen:
- **Bugs beheben**: Kritische Probleme wie Null-Pointer-Dereferenzierungen angehen.
- **Code Smells refaktorisieren**: Komplexe Methoden vereinfachen oder ungenutzten Code entfernen.
- **Abdeckung verbessern**: Zusätzliche Unit-Tests für ungedeckten Code schreiben.

## Best Practices
1. **Integration mit CI/CD**:
   - Fügen Sie die SonarQube-Analyse Ihrer CI/CD-Pipeline hinzu (z.B. Jenkins, GitHub Actions).
   - Beispiel GitHub Actions Workflow:
     ```yaml
     name: CI with SonarQube
     on: [push]
     jobs:
       build:
         runs-on: ubuntu-latest
         steps:
           - uses: actions/checkout@v3
           - name: Set up JDK 11
             uses: actions/setup-java@v3
             with:
               java-version: '11'
           - name: Build and Analyze
             run: mvn clean verify sonar:sonar -Dsonar.host.url=http://localhost:9000 -Dsonar.token=${{ secrets.SONAR_TOKEN }}
     ```

2. **Quality Gates definieren**:
   - Legen Sie Schwellenwerte für Code-Abdeckung, Bugs und Sicherheitslücken in SonarQube fest.
   - Beispiel: Build fehlschlagen lassen, wenn Abdeckung < 80% oder kritische Probleme existieren.

3. **SonarLint verwenden**:
   - Installieren Sie das SonarLint-Plugin in Ihrer IDE (z.B. IntelliJ IDEA), um Probleme während der Entwicklung zu erkennen.

4. **Regelmäßige Analyse**:
   - Führen Sie die SonarQube-Analyse bei jedem Commit oder täglich durch, um Probleme frühzeitig zu erkennen.

5. **Regeln anpassen**:
   - Passen Sie die SonarQube-Regeln an die Bedürfnisse Ihres Projekts an (z.B. deaktivieren Sie irrelevante Regeln oder fügen Sie benutzerdefinierte hinzu).

## Behebung häufiger Probleme
1. **Analyse-Upload schlägt fehl**:
   - Überprüfen Sie `sonar.host.url` und `sonar.token` in der Konfiguration.
   - Stellen Sie sicher, dass der SonarQube-Server läuft (`http://localhost:9000`).

2. **Keine Code-Abdeckung**:
   - Überprüfen Sie, ob das JaCoCo-Plugin korrekt in der `pom.xml` konfiguriert ist.
   - Führen Sie `mvn test` vor der Analyse aus, um `jacoco.exec` zu generieren.

3. **Datenbankverbindungsfehler**:
   - Bestätigen Sie die Datenbank-Anmeldedaten in `sonar.properties`.
   - Stellen Sie sicher, dass der Datenbankserver läuft.

4. **Speichermangel**:
   - Erhöhen Sie den JVM-Speicher in `sonar.properties`:
     ```properties
     sonar.web.javaOpts=-Xmx2g -Xms1g
     ```

## Fazit
SonarQube ist ein leistungsstarkes Tool zur Aufrechterhaltung der Code-Qualität in Java-Spring-Projekten. Durch die Integration in Ihren Entwicklungs-Workflow können Sie Probleme frühzeitig erkennen, die Code-Wartbarkeit verbessern und eine robuste Sicherheit gewährleisten. Regelmäßige Analysen, kombiniert mit Best Practices wie CI/CD-Integration und SonarLint, helfen Ihnen, eine hochwertige Codebasis zu erhalten.