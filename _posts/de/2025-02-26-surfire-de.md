---
audio: false
generated: true
lang: de
layout: post
title: Maven Surefire Plugin
translated: true
type: note
---

Nachfolgend eine Erläuterung des **Maven Surefire Plugins**, einer Schlüsselkomponente in Maven-basierten Projekten zur Ausführung von Unit-Tests während des Build-Prozesses. Diese Erläuterung behandelt seinen Zweck, Konfiguration, Verwendung und Anpassungsmöglichkeiten.

---

## Was ist das Maven Surefire Plugin?

Das **Maven Surefire Plugin** ist ein Plugin in Apache Maven, das für die Ausführung von Unit-Tests während des Build-Lifecycles konzipiert ist. Es integriert sich nahtlos in die `test`-Phase von Maven und wird automatisch ausgelöst, wenn Sie Befehle wie `mvn test`, `mvn package` oder `mvn install` ausführen. Das Plugin unterstützt beliebte Test-Frameworks wie JUnit (Versionen 3, 4 und 5) und TestNG und generiert Testberichte, um Entwicklern die Bewertung der Testergebnisse zu erleichtern.

### Hauptmerkmale
- Führt Tests in einem separaten JVM-Prozess für Isolation aus.
- Unterstützt mehrere Test-Frameworks (JUnit, TestNG, etc.).
- Generiert Testberichte in Formaten wie XML und Klartext.
- Bietet Flexibilität, um Tests zu überspringen, bestimmte Tests auszuführen oder die Ausführung anzupassen.

---

## Grundlegende Einrichtung in `pom.xml`

Das Surefire Plugin ist standardmäßig im Build-Lifecycle von Maven enthalten, sodass Sie es für die grundlegende Verwendung nicht konfigurieren müssen. Sie können es jedoch explizit in Ihrer `pom.xml`-Datei deklarieren, um eine bestimmte Version anzugeben oder sein Verhalten anzupassen.

### Minimale Konfiguration
Wenn Sie keine Konfiguration hinzufügen, verwendet Maven das Plugin mit Standardeinstellungen:
- Tests befinden sich in `src/test/java`.
- Testdateien folgen Namensmustern wie `**/*Test.java`, `**/Test*.java` oder `**/*Tests.java`.

### Explizite Deklaration
Um das Plugin anzupassen oder eine bestimmte Version sicherzustellen, fügen Sie es dem Abschnitt `<build><plugins>` Ihrer `pom.xml` hinzu. Hier ist ein Beispiel:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M5</version> <!-- Verwenden Sie die neueste Version -->
        </plugin>
    </plugins>
</build>
```

---

## Ausführen von Tests mit Surefire

Das Plugin ist an die `test`-Phase des Maven-Lifecycles gebunden. So verwenden Sie es:

### Alle Tests ausführen
Um alle Unit-Tests auszuführen, führen Sie aus:

```
mvn test
```

### Tests in einem größeren Build ausführen
Tests werden automatisch ausgeführt, wenn Sie Befehle ausführen, die die `test`-Phase beinhalten, wie z.B.:

```
mvn package
mvn install
```

### Tests überspringen
Sie können die Testausführung über Kommandozeilen-Flags überspringen:
- **Ausführung von Tests überspringen**: `-DskipTests`
  ```
  mvn package -DskipTests
  ```
- **Test-Kompilierung und -Ausführung überspringen**: `-Dmaven.test.skip=true`
  ```
  mvn package -Dmaven.test.skip=true
  ```

---

## Anpassen des Surefire Plugins

Sie können das Verhalten des Plugins anpassen, indem Sie einen `<configuration>`-Abschnitt in der `pom.xml` hinzufügen. Hier sind einige gängige Anpassungen:

### Bestimmte Tests ein- oder ausschließen
Geben Sie an, welche Tests ausgeführt oder übersprungen werden sollen, indem Sie Muster verwenden:
```xml
<configuration>
    <includes>
        <include>**/My*Test.java</include>
    </includes>
    <excludes>
        <exclude>**/SlowTest.java</exclude>
    </excludes>
</configuration>
```

### Tests parallel ausführen
Beschleunigen Sie die Ausführung, indem Sie Tests gleichzeitig ausführen:
```xml
<configuration>
    <parallel>methods</parallel>
    <threadCount>2</threadCount>
</configuration>
```
*Hinweis*: Stellen Sie sicher, dass Ihre Tests thread-sicher sind, bevor Sie dies aktivieren.

### System Properties übergeben
Legen Sie Properties für die Test-JVM fest:
```xml
<configuration>
    <systemPropertyVariables>
        <propertyName>propertyValue</propertyName>
    </systemPropertyVariables>
</configuration>
```

### Berichte generieren
Standardmäßig werden Berichte in `target/surefire-reports` gespeichert. Für einen HTML-Bericht verwenden Sie das `maven-surefire-report-plugin`:
```xml
<reporting>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-report-plugin</artifactId>
            <version>3.0.0-M5</version>
        </plugin>
    </plugins>
</reporting>
```
Führen Sie `mvn surefire-report:report` aus, um den HTML-Bericht zu generieren.

---

## Umgang mit Testfehlern

### Build bei Testfehlern fehlschlagen lassen
Standardmäßig führt ein fehlgeschlagener Test zu einem Build-Fehler. Um Fehler zu ignorieren und fortzufahren:
```
mvn test -Dmaven.test.failure.ignore=true
```

### Fehlgeschlagene Tests erneut ausführen
Behandeln Sie flaky Tests, indem Sie Fehlschläge wiederholen:
```xml
<configuration>
    <rerunFailingTestsCount>2</rerunFailingTestsCount>
</configuration>
```
Dies führt fehlgeschlagene Tests bis zu 2 Mal erneut aus.

---

## Verwendung von Surefire mit Test-Frameworks

Das Plugin unterstützt verschiedene Test-Frameworks mit minimalem Setup:

### JUnit 4
Keine zusätzliche Konfiguration erforderlich; Surefire erkennt JUnit 4-Tests automatisch.

### JUnit 5
Fügen Sie die JUnit 5-Abhängigkeit hinzu:
```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.8.1</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
Verwenden Sie Surefire Version 2.22.0 oder höher für volle Unterstützung.

### TestNG
Fügen Sie die TestNG-Abhängigkeit hinzu:
```xml
<dependencies>
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.4.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
Surefire führt TestNG-Tests automatisch aus.

---

## Wichtige Hinweise

- **Test-Pfad**: Tests sollten sich in `src/test/java` befinden, Ressourcen in `src/test/resources`.
- **Namenskonventionen**: Standardmuster umfassen `**/*Test.java`, `**/Test*.java`, etc., diese können jedoch angepasst werden.
- **Plugin-Version**: Verwenden Sie eine aktuelle Version (z.B. 3.0.0-M5) für die neuesten Funktionen und Framework-Unterstützung.

---

## Zusammenfassung

Das **Maven Surefire Plugin** ist unerlässlich für die Ausführung von Unit-Tests in Maven-Projekten. So verwenden Sie es:
1. Verlassen Sie sich auf sein Standardverhalten oder deklarieren Sie es explizit in `pom.xml` zur Anpassung.
2. Führen Sie Tests mit `mvn test` oder als Teil größerer Builds wie `mvn package` aus.
3. Passen Sie es mit Optionen wie Ein-/Ausschlussmustern, paralleler Ausführung oder System Properties an.
4. Behandeln Sie Fehler, indem Sie Tests überspringen, ignorieren oder flaky Tests erneut ausführen.
5. Stellen Sie die Kompatibilität mit Ihrem Test-Framework (JUnit, TestNG) sicher, indem Sie die richtigen Abhängigkeiten hinzufügen.

Dieses Plugin bietet eine robuste und flexible Möglichkeit, Unit-Testing in Ihren Maven-Projekten zu verwalten!