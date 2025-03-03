---
audio: false
generated: true
lang: de
layout: post
title: JaCoCo Maven Plugin
translated: true
---

Hier ist eine Schritt-für-Schritt-Anleitung zur Verwendung des **JaCoCo Maven Plugins**, um den Codeabdeckung in einem Maven-basierten Java-Projekt zu messen. JaCoCo (Java Code Coverage) ist ein Tool, das sich in Maven integriert, um zu verfolgen, wie viel von Ihrem Code durch Tests, typischerweise Unit-Tests, ausgeführt wird. Durch das Hinzufügen und Konfigurieren des JaCoCo Maven Plugins in Ihrem Projekt können Sie detaillierte Abdeckungsberichte während des Build-Prozesses erstellen.

---

### **Schritte zur Verwendung des JaCoCo Maven Plugins**

#### **1. JaCoCo Maven Plugin zum `pom.xml` hinzufügen**
Um das JaCoCo Maven Plugin zu verwenden, müssen Sie es im `<build><plugins>`-Bereich der `pom.xml`-Datei Ihres Projekts hinzufügen. Hier ist eine grundlegende Konfiguration, die das Plugin einrichtet:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- Verwenden Sie die neueste verfügbare Version -->
            <executions>
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>verify</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`groupId`, `artifactId` und `version`**: Diese identifizieren das JaCoCo Maven Plugin. Ersetzen Sie `0.8.12` durch die neueste Version, die im [Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin) verfügbar ist.
- **`<executions>`**: Dieser Abschnitt konfiguriert, wann und wie das Plugin während des Maven Build-Lebenszyklus läuft:
  - **`<goal>prepare-agent</goal>`**: Bereitet den JaCoCo-Agenten vor, um Abdeckungsdaten während der Testausführung zu sammeln. Standardmäßig bindet es an eine frühe Phase (wie `initialize`) und erfordert keine explizite Phase, es sei denn, es wurde angepasst.
  - **`<goal>report</goal>`**: Erstellt den Abdeckungsbericht nach Abschluss der Tests. Es ist hier an die `verify`-Phase gebunden, die nach der `test`-Phase erfolgt, sodass alle Testdaten verfügbar sind.

#### **2. Stellen Sie sicher, dass die Tests konfiguriert sind**
Das JaCoCo Plugin arbeitet durch die Analyse der Testausführung, typischerweise Unit-Tests, die vom Maven Surefire Plugin ausgeführt werden. In den meisten Maven-Projekten ist Surefire standardmäßig enthalten und führt Tests aus, die sich in `src/test/java` befinden. Keine zusätzliche Konfiguration ist erforderlich, es sei denn, Ihre Tests sind nicht standardmäßig. Stellen Sie sicher, dass:
- Sie haben Unit-Tests geschrieben (z. B. mit JUnit oder TestNG).
- Das Surefire-Plugin vorhanden ist (es wird in den meisten Fällen vom Standard-Maven-Eltern-POM geerbt).

Falls Sie Surefire explizit konfigurieren müssen, könnte dies so aussehen:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- Verwenden Sie die neueste Version -->
</plugin>
```

Das `prepare-agent`-Ziel richtet den JaCoCo-Agenten ein, indem es die `argLine`-Eigenschaft ändert, die Surefire verwendet, um Tests mit aktivierter Abdeckungserfassung auszuführen.

#### **3. Maven Build ausführen**
Um den Abdeckungsbericht zu erstellen, führen Sie den folgenden Befehl im Verzeichnis Ihres Projekts aus:

```bash
mvn verify
```

- **`mvn verify`**: Dies führt alle Phasen bis `verify` aus, einschließlich `compile`, `test` und `verify`. Das JaCoCo Plugin wird:
  1. Den Agenten vor dem Ausführen der Tests vorbereiten.
  2. Abdeckungsdaten während der `test`-Phase (wenn Surefire die Tests ausführt) sammeln.
  3. Den Bericht während der `verify`-Phase erstellen.

Alternativ, wenn Sie nur die Tests ausführen möchten, ohne bis `verify` fortzufahren, verwenden Sie:

```bash
mvn test
```

Da das `report`-Ziel in dieser Konfiguration an `verify` gebunden ist, müssen Sie `mvn verify` ausführen, um den Bericht zu sehen. Wenn Sie den Bericht während `mvn test` erstellen möchten, können Sie die `<phase>` für die `report`-Ausführung in `test` ändern, obwohl `verify` eine gängige Konvention ist.

#### **4. Abdeckungsbericht anzeigen**
Nach dem Ausführen von `mvn verify` erstellt JaCoCo standardmäßig einen HTML-Bericht. Sie finden ihn unter:

```
target/site/jacoco/index.html
```

- Öffnen Sie diese Datei in einem Webbrowser, um eine detaillierte Aufschlüsselung der Codeabdeckung einschließlich Prozentsätzen für Pakete, Klassen, Methoden und Zeilen zu sehen.
- Der Bericht enthält auch XML- und CSV-Formate im selben Verzeichnis (`jacoco.xml` und `jacoco.csv`), die für die Integration mit Tools wie CI-Systemen nützlich sind.

---

### **Optionale Anpassungen**
Für fortgeschrittenere Anwendungsfälle können Sie die Plugin-Konfiguration anpassen:

- **Klassen oder Pakete ausschließen**:
  Um bestimmten Code von der Abdeckungsanalyse auszuschließen (z. B. generierten Code), fügen Sie einen `<configuration>`-Bereich hinzu:

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  Platzieren Sie dies innerhalb des `<plugin>`-Tags, über `<executions>`.

- **Abdeckungsschwellenwerte durchsetzen**:
  Um den Build zu stoppen, wenn die Abdeckung unter einen Schwellenwert fällt, fügen Sie das `check`-Ziel hinzu:

  ```xml
  <execution>
      <id>check</id>
      <phase>verify</phase>
      <goals>
          <goal>check</goal>
      </goals>
      <configuration>
          <rules>
              <rule>
                  <element>BUNDLE</element>
                  <limits>
                      <limit>
                          <counter>LINE</counter>
                          <value>COVEREDRATIO</value>
                          <minimum>0.80</minimum> <!-- 80% Zeilenabdeckung -->
                      </limit>
                  </limits>
              </rule>
          </rules>
      </configuration>
  </execution>
  ```

- **Berichtsausgabeverzeichnis ändern**:
  Um den Berichtstandort anzupassen, fügen Sie hinzu:

  ```xml
  <configuration>
      <destFile>${project.build.directory}/custom-jacoco.exec</destFile>
      <dataFile>${project.build.directory}/custom-jacoco.exec</dataFile>
      <outputDirectory>${project.build.directory}/custom-reports</outputDirectory>
  </configuration>
  ```

---

### **Zusammenfassung**
Um das JaCoCo Maven Plugin zu verwenden:
1. Fügen Sie das Plugin zu Ihrem `pom.xml` mit den Zielen `prepare-agent` und `report` hinzu.
2. Stellen Sie sicher, dass Ihr Projekt Tests konfiguriert hat (typischerweise über Surefire).
3. Führen Sie `mvn verify` aus, um den Abdeckungsbericht zu erstellen.
4. Überprüfen Sie den Bericht unter `target/site/jacoco/index.html`.

Diese Einrichtung bietet eine einfache Möglichkeit, die Codeabdeckung in Ihren Maven-Build-Prozess zu integrieren und Ihnen zu helfen, die Wirksamkeit Ihrer Tests zu bewerten. Für die neueste Plugin-Version oder fortgeschrittene Konfigurationen verweisen Sie auf die [offizielle JaCoCo-Dokumentation](https://www.jacoco.org/jacoco/trunk/doc/maven.html).