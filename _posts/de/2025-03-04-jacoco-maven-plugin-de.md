---
audio: false
generated: true
lang: de
layout: post
title: JaCoCo Maven-Plugin
translated: true
type: note
---

Hier ist eine Schritt-für-Schritt-Anleitung zur Verwendung des **JaCoCo Maven Plugins** zur Messung der Code-Abdeckung in einem Maven-basierten Java-Projekt. JaCoCo (Java Code Coverage) ist ein Tool, das sich in Maven integrieren lässt, um zu verfolgen, wie viel Ihres Codes durch Tests, typischerweise Unit-Tests, ausgeführt wird. Durch das Hinzufügen und Konfigurieren des JaCoCo Maven Plugins in Ihrem Projekt können Sie während des Build-Prozesses detaillierte Abdeckungsberichte generieren.

---

### **Schritte zur Verwendung des JaCoCo Maven Plugins**

#### **1. Fügen Sie das JaCoCo Maven Plugin zu Ihrer `pom.xml` hinzu**
Um das JaCoCo Maven Plugin zu verwenden, müssen Sie es im Abschnitt `<build><plugins>` Ihrer Projekt-`pom.xml`-Datei einbinden. Nachfolgend finden Sie eine grundlegende Konfiguration für das Plugin:

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

- **`groupId`, `artifactId` und `version`**: Diese identifizieren das JaCoCo Maven Plugin. Ersetzen Sie `0.8.12` durch die neueste Version auf [Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin).
- **`<executions>`**: Dieser Abschnitt konfiguriert, wann und wie das Plugin während des Maven Build-Lifecycles ausgeführt wird:
  - **`<goal>prepare-agent</goal>`**: Bereitet den JaCoCo-Agenten vor, um während der Testausführung Abdeckungsdaten zu sammeln. Standardmäßig bindet es sich an eine frühe Phase (wie `initialize`) und erfordert, sofern nicht angepasst, keine explizite Phase.
  - **`<goal>report</goal>`**: Generiert den Abdeckungsbericht, nachdem die Tests ausgeführt wurden. Hier ist es an die `verify`-Phase gebunden, die nach der `test`-Phase stattfindet und somit sicherstellt, dass alle Testdaten verfügbar sind.

#### **2. Stellen Sie sicher, dass Tests konfiguriert sind**
Das JaCoCo Plugin funktioniert, indem es die Testausführung analysiert, typischerweise Unit-Tests, die vom Maven Surefire Plugin ausgeführt werden. In den meisten Maven-Projekten ist Surefire standardmäßig enthalten und führt Tests im Verzeichnis `src/test/java` aus. Es ist keine zusätzliche Konfiguration erforderlich, es sei denn, Ihre Tests sind nicht standardmäßig. Stellen Sie sicher, dass:
- Sie Unit-Tests geschrieben haben (z. B. mit JUnit oder TestNG).
- Das Surefire Plugin vorhanden ist (in den meisten Fällen wird es vom standardmäßigen Maven Parent POM geerbt).

Falls Sie Surefire explizit konfigurieren müssen, könnte dies wie folgt aussehen:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- Verwenden Sie die neueste Version -->
</plugin>
```

Das `prepare-agent`-Goal richtet den JaCoCo-Agenten ein, indem es die `argLine`-Eigenschaft modifiziert, die Surefire verwendet, um Tests mit aktivierter Abdeckungsverfolgung auszuführen.

#### **3. Führen Sie den Maven Build aus**
Um den Abdeckungsbericht zu generieren, führen Sie den folgenden Befehl in Ihrem Projektverzeichnis aus:

```bash
mvn verify
```

- **`mvn verify`**: Dies führt alle Phasen bis einschließlich `verify` aus, inklusive `compile`, `test` und `verify`. Das JaCoCo Plugin wird:
  1. Den Agenten vor der Testausführung vorbereiten.
  2. Während der `test`-Phase (wenn Surefire die Tests ausführt) Abdeckungsdaten sammeln.
  3. Während der `verify`-Phase den Bericht generieren.

Alternativ, wenn Sie nur Tests ausführen möchten, ohne bis `verify` fortzufahren, verwenden Sie:

```bash
mvn test
```

Da das `report`-Goal in dieser Konfiguration jedoch an `verify` gebunden ist, müssen Sie `mvn verify` ausführen, um den Bericht zu sehen. Wenn Sie bevorzugen, dass der Bericht während `mvn test` generiert wird, können Sie die `<phase>` für die `report`-Ausführung auf `test` ändern, obwohl `verify` eine gängige Konvention ist.

#### **4. Sehen Sie sich den Abdeckungsbericht an**
Nach dem Ausführen von `mvn verify` generiert JaCoCo standardmäßig einen HTML-Bericht. Sie finden ihn unter:

```
target/site/jacoco/index.html
```

- Öffnen Sie diese Datei in einem Webbrowser, um eine detaillierte Aufschlüsselung der Code-Abdeckung zu sehen, einschließlich Prozentsätzen für Pakete, Klassen, Methoden und Zeilen.
- Der Bericht enthält auch XML- und CSV-Formate im selben Verzeichnis (`jacoco.xml` und `jacoco.csv`), die nützlich für die Integration in Tools wie CI-Systeme sind.

---

### **Optionale Anpassungen**
Für fortgeschrittenere Anwendungsfälle können Sie die Plugin-Konfiguration anpassen:

- **Klassen oder Pakete ausschließen**:
  Um bestimmten Code von der Abdeckungsanalyse auszuschließen (z. B. generierten Code), fügen Sie einen `<configuration>`-Abschnitt hinzu:

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  Platzieren Sie dies innerhalb des `<plugin>`-Tags, oberhalb von `<executions>`.

- **Abdeckungsschwellenwerte durchsetzen**:
  Um den Build fehlschlagen zu lassen, wenn die Abdeckung unter einen Schwellenwert fällt, fügen Sie das `check`-Goal hinzu:

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

- **Ausgabeverzeichnis für Berichte ändern**:
  Um den Speicherort des Berichts anzupassen, fügen Sie hinzu:

  ```xml
  <configuration>
      <destFile>${project.build.directory}/custom-jacoco.exec</destFile>
      <dataFile>${project.build.directory}/custom-jacoco.exec</dataFile>
      <outputDirectory>${project.build.directory}/custom-reports</outputDirectory>
  </configuration>
  ```

---

### **Zusammenfassung**
So verwenden Sie das JaCoCo Maven Plugin:
1. Fügen Sie das Plugin mit den Goals `prepare-agent` und `report` zu Ihrer `pom.xml` hinzu.
2. Stellen Sie sicher, dass Ihr Projekt konfigurierte Tests hat (typischerweise über Surefire).
3. Führen Sie `mvn verify` aus, um den Abdeckungsbericht zu generieren.
4. Überprüfen Sie den Bericht unter `target/site/jacoco/index.html`.

Dieses Setup bietet eine unkomplizierte Möglichkeit, Code-Abdeckung in Ihren Maven Build-Prozess zu integrieren, um die Effektivität Ihrer Tests zu bewerten. Für die neueste Plugin-Version oder erweiterte Konfigurationen lesen Sie die [offizielle JaCoCo-Dokumentation](https://www.jacoco.org/jacoco/trunk/doc/maven.html).