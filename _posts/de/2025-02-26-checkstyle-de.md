---
audio: false
generated: true
lang: de
layout: post
title: Maven Checkstyle Plugin
translated: true
---

## Was ist das Maven Checkstyle Plugin?

Das **Maven Checkstyle Plugin** ist ein Werkzeug, das Checkstyle—a statische Code-Analyse-Tool—in Ihren Maven-Build-Prozess integriert. Checkstyle untersucht Ihren Java-Code anhand einer Reihe vordefinierter Regeln, wie z.B. Benennungskonventionen, Code-Formatierung und Komplexität, um Codierungsstandards durchzusetzen. Durch die Einbettung dieser Funktionalität in Maven ermöglicht das Plugin die Automatisierung dieser Überprüfungen während des Builds, sodass sichergestellt wird, dass Ihre Codebasis konsistenten Stil- und Qualitätsrichtlinien entspricht.

## Warum das Maven Checkstyle Plugin verwenden?

Die Verwendung des Maven Checkstyle Plugins bietet mehrere Vorteile:

- **Konsistenz**: Es stellt sicher, dass alle Entwickler denselben Codierungsstandards folgen, was die Lesbarkeit und Wartbarkeit verbessert.
- **Qualität**: Es erkennt potenzielle Probleme frühzeitig, wie z.B. übermäßig komplexe Methoden oder fehlende Javadoc-Kommentare.
- **Automatisierung**: Die Überprüfungen laufen automatisch als Teil des Maven-Build-Prozesses.
- **Anpassungsfähigkeit**: Sie können die Regeln an die spezifischen Bedürfnisse Ihres Projekts anpassen.

## So richten Sie das Maven Checkstyle Plugin ein

Hier erfahren Sie, wie Sie mit dem Plugin in Ihrem Maven-Projekt beginnen:

### 1. Fügen Sie das Plugin zu Ihrer `pom.xml` hinzu

Fügen Sie das Plugin in den Abschnitt `<build><plugins>` Ihrer `pom.xml` ein. Wenn Sie ein Eltern-POM wie `spring-boot-starter-parent` verwenden, wird die Version möglicherweise für Sie verwaltet; andernfalls geben Sie sie explizit an.

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.1.2</version> <!-- Ersetzen Sie durch die neueste Version -->
        </plugin>
    </plugins>
</build>
```

### 2. Konfigurieren Sie das Plugin

Geben Sie eine Checkstyle-Konfigurationsdatei (z.B. `checkstyle.xml`) an, die die durchzusetzen Regeln definiert. Sie können eingebaute Konfigurationen wie Sun Checks oder Google Checks verwenden oder Ihre eigene benutzerdefinierte Datei erstellen.

Beispielkonfiguration:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.1.2</version>
            <configuration>
                <configLocation>checkstyle.xml</configLocation>
            </configuration>
        </plugin>
    </plugins>
</build>
```

### 3. Stellen Sie eine Checkstyle-Konfigurationsdatei bereit

Legen Sie Ihre `checkstyle.xml` im Projektverzeichnis oder einem Unterverzeichnis ab. Alternativ können Sie eine externe Konfiguration wie die von Google referenzieren:

```xml
<configLocation>google_checks.xml</configLocation>
```

Um eine externe Konfiguration wie Google Checks zu verwenden, müssen Sie möglicherweise die Checkstyle-Abhängigkeit hinzufügen:

```xml
<dependencies>
    <dependency>
        <groupId>com.puppycrawl.tools</groupId>
        <artifactId>checkstyle</artifactId>
        <version>8.44</version>
    </dependency>
</dependencies>
```

## Ausführen des Maven Checkstyle Plugins

Das Plugin integriert sich in den Maven-Lebenszyklus und kann auf verschiedene Weise ausgeführt werden:

- **Checkstyle explizit ausführen**:
  Um auf Verletzungen zu überprüfen und den Build gegebenenfalls zu stoppen:
  ```
  mvn checkstyle:check
  ```

- **Während des Builds ausführen**:
  Standardmäßig bindet das Plugin an die `verify`-Phase. Verwenden Sie:
  ```
  mvn verify
  ```
  Um einen Bericht zu erstellen, ohne den Build zu stoppen:
  ```
  mvn checkstyle:checkstyle
  ```

Berichte werden normalerweise in `target/site/checkstyle.html` erstellt.

## Anpassen des Plugins

Sie können das Verhalten des Plugins im Abschnitt `<configuration>` Ihrer `pom.xml` anpassen:

- **Build bei Verletzung stoppen**:
  Standardmäßig stoppt der Build, wenn Verletzungen gefunden werden. Um dies zu deaktivieren:
  ```xml
  <configuration>
      <failOnViolation>false</failOnViolation>
  </configuration>
  ```

- **Dateien ein- oder ausschließen**:
  Steuern Sie, welche Dateien überprüft werden:
  ```xml
  <configuration>
      <includes>**/*.java</includes>
      <excludes>**/generated/**/*.java</excludes>
  </configuration>
  ```

- **Schweregrad der Verletzung festlegen**:
  Definieren Sie den Schweregrad, der einen Build-Stopp auslöst:
  ```xml
  <configuration>
      <violationSeverity>warning</violationSeverity>
  </configuration>
  ```

## Beispiel `checkstyle.xml`

Hier ist eine grundlegende `checkstyle.xml`-Datei, die Benennungskonventionen und Javadoc-Anforderungen durchsetzt:

```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name="Checker">
    <module name="TreeWalker">
        <module name="JavadocMethod"/>
        <module name="MethodName"/>
        <module name="ConstantName"/>
    </module>
</module>
```

## Gängige Anwendungsfälle

Das Plugin unterstützt eine Vielzahl von Überprüfungen, einschließlich:
- Benennungskonventionen für Klassen, Methoden und Variablen.
- Richtige Verwendung von Leerzeichen und Formatierung.
- Vorhandensein und Richtigkeit von Javadoc-Kommentaren.
- Erkennung komplexer oder langer Methoden.

## Integration und Fehlerbehebung

- **IDE-Integration**: Tools wie IntelliJ IDEA und Eclipse können dieselbe `checkstyle.xml` für Echtzeit-Feedback verwenden.
- **Continuous Integration**: Fügen Sie Checkstyle in Ihre CI-Pipeline ein, um Standards bei jedem Commit durchzusetzen.
- **Fehlerbehebung**: Wenn die Konfigurationsdatei nicht gefunden wird, überprüfen Sie den `<configLocation>`-Pfad. Stellen Sie sicher, dass die Versionsabhängigkeiten mit dem Plugin übereinstimmen.

## Zusammenfassung

Das **Maven Checkstyle Plugin** ist eine wertvolle Ergänzung für jedes Java-Projekt, das Maven verwendet. Um es zu verwenden:
1. Fügen Sie das Plugin in Ihrer `pom.xml` hinzu und konfigurieren Sie es.
2. Stellen Sie eine `checkstyle.xml` mit Ihren gewünschten Regeln bereit.
3. Führen Sie `mvn checkstyle:check` aus, um Standards durchzusetzen, oder `mvn checkstyle:checkstyle` für Berichte.
4. Passen Sie nach Bedarf an, um Ihren Workflow zu unterstützen.

Dieses Plugin hilft, hochwertigen, konsistenten Code mit minimalem Aufwand zu erhalten!