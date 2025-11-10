---
audio: false
generated: true
lang: de
layout: post
title: 'Maven Shade Plugin: Erstellen von Uber-JARs'
translated: true
type: note
---

Das `maven-shade-plugin` ist ein Maven-Plugin, das verwendet wird, um einen "Uber-JAR" (eine einzelne, eigenständige JAR-Datei) zu erstellen, indem der kompilierte Code eines Projekts mit seinen Abhängigkeiten kombiniert wird. Es wird häufig in Java-Projekten verwendet, um eine Anwendung und alle ihre benötigten Bibliotheken in eine ausführbare JAR-Datei zu packen, was die Verteilung und das Deployment vereinfacht.

### Wichtige Details:
- **Group ID**: `org.apache.maven.plugins` (zeigt an, dass es sich um ein offizielles Apache Maven-Plugin handelt).
- **Artifact ID**: `maven-shade-plugin` (der spezifische Plugin-Name).
- **Zweck**:
  - **Shading**: Verschiebt (benennt um) Pakete von Abhängigkeiten, um Klassenkonflikte zu vermeiden (z.B. wenn mehrere Bibliotheken verschiedene Versionen derselben Klasse verwenden).
  - **Packaging**: Bündelt Abhängigkeiten in die finale JAR-Datei, um sie eigenständig zu machen.
  - **Resource Transformation**: Kann Ressourcen modifizieren (z.B. Konfigurationsdateien wie `MANIFEST.MF` zusammenführen).
- **Häufige Anwendungsfälle**:
  - Erstellen von ausführbaren JARs für Kommandozeilenanwendungen.
  - Beheben von Classpath-Konflikten in Projekten mit mehreren Abhängigkeiten.
  - Vereinfachen des Deployments für Anwendungen wie Spark- oder Hadoop-Jobs.
- **Wie es funktioniert**:
  - Wird in der `pom.xml`-Datei im Abschnitt `<plugins>` konfiguriert.
  - Während des Build-Prozesses (typischerweise in der `package`-Phase) kombiniert es Klassen und Ressourcen, verschiebt optional Pakete und erzeugt die finale JAR-Datei.
- **Beispielkonfiguration** in `pom.xml`:
  ```xml
  <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-shade-plugin</artifactId>
      <version>3.5.0</version> <!-- Verwenden Sie die neueste Version -->
      <executions>
          <execution>
              <phase>package</phase>
              <goals>
                  <goal>shade</goal>
              </goals>
              <configuration>
                  <transformers>
                      <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                          <mainClass>com.example.Main</mainClass>
                      </transformer>
                  </transformers>
              </configuration>
          </execution>
      </executions>
  </plugin>
  ```
  Dieses Beispiel gibt die Hauptklasse für eine ausführbare JAR-Datei an und führt das Plugin während der `package`-Phase aus.

- **Wichtige Funktionen**:
  - **Dependency Inclusion**: Bettet Abhängigkeiten in die JAR-Datei ein.
  - **Package Relocation**: Benennt Pakete um, um Konflikte zu vermeiden (z.B. `com.google.common` zu `shaded.com.google.common`).
  - **Resource Filtering**: Führt Ressourcendateien zusammen oder transformiert sie.
  - **Executable JAR**: Fügt Manifest-Einträge hinzu, um die JAR-Datei mit `java -jar` ausführbar zu machen.

### Wann man es verwendet:
- Wenn Sie eine einzelne JAR-Datei für eine einfache Verteilung benötigen.
- Wenn Sie mit Abhängigkeitskonflikten umgehen müssen (z.B. verschiedene Versionen derselben Bibliothek).
- Für das Deployment von Anwendungen in Umgebungen, in denen externe Abhängigkeiten schwer zu verwalten sind.

Wenn Sie eine spezifische Frage zu seiner Konfiguration oder seinem Anwendungsfall haben, lassen Sie es mich wissen!