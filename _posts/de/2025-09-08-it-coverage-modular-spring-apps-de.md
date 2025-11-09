---
audio: false
date: 2025-09-08
generated: true
image: false
lang: de
layout: post
title: IT-Abdeckung für modulare Spring-Apps
translated: true
type: note
---

### Gesamteinschätzung Ihres Setups

Ihre aktuelle Konfiguration ist solide für ein kleines Multi-Modul-Projekt wie dieses, insbesondere da Sie den Kernablauf bereits zum Laufen gebracht haben: Anhängen des JaCoCo-Agents an Jetty, Ausführung externer Python-Integrationstests über das Exec Plugin und Generierung eines Berichts im `PlaygroundWeb`-Modul. Dies erfasst die Laufzeit-Abdeckung von API-Endpunkten, die von Pythons `unittest` getestet werden, was genau das ist, was Sie für die Integrationstest-Abdeckung (IT) in einer Spring-Web-App benötigen.

**Stärken:**
- **Modular und phasengebunden**: Die Verwendung von Maven-Phasen (`pre-integration-test` für Jetty-Start, `integration-test` für Python-Tests, `post-integration-test` für Stopp, `verify` für Bericht) gewährleistet Zuverlässigkeit und Reproduzierbarkeit.
- **Agent-Anbindung**: Das JVM-Arg (`-javaagent:...`) auf Jetty instrumentiert die Laufzeit korrekt und erfasst die Abdeckung in `jacoco.it.exec`.
- **Integration externer Tests**: Das Exec Plugin handhabt Python gut, und das Behalten der Tests im Repository-Stammverzeichnis (`${project.parent.basedir}/tests`) entkoppelt sie von Java-Modulen.
- **Keine unnötige Duplizierung**: Sie vermeiden es, Jetty/Python in `PlaygroundUtils` (welches keine Controller hat) auszuführen, was effizient ist.

**Herausforderungen, die Sie identifiziert haben:**
- **Abdeckung für Bibliotheksmodule wie `PlaygroundUtils`**: Da Utils-Code in der `PlaygroundWeb`-JVM läuft (als Abhängigkeit im WAR), wird er instrumentiert und erscheint in `PlaygroundWeb`s `jacoco.it.exec`. Aber Ihre Berichte sind modulspezifisch, sodass die `PlaygroundUtils`-Abdeckung nicht sichtbar ist, es sei denn, sie wird aggregiert oder eingeschlossen.
- **Nicht in sich geschlossene Natur von JaCoCo**: Im Gegensatz zu Checkstyle/Spotless (die nur Quell-/statische Artefakte analysieren) benötigt JaCoCo Laufzeitdaten (`.exec`-Dateien) von externen Tests und Agent-Anbindung. Dies macht es für Multi-Modul-Setups ohne sorgfältige Koordination anfällig.
- **Einschränkungen des Aggregate-Ziels**: `jacoco:report-aggregate` erwartet pro Modul `.exec`-Dateien (z.B. von Unit-Tests), aber Ihre Abdeckung stammt rein aus IT in einem Modul. Erzwingte Aggregation kann zu leeren Berichten für Bibliotheken wie `PlaygroundUtils` führen.
- **Skalierbarkeit auf 10+ Module**: Das Duplizieren von Jetty/Python-Setups über Module hinweg wäre verschwenderisch (redundante Server/Tests). Umständliche Workarounds wie das Kopieren von `.exec`-Dateien oder doppelte Ausführung (wie Sie erwähnten) führen zu Wartungsaufwand und Build-Zeit-Explosion.

Ihr Rückgriff auf modulspezifische Berichte ist pragmatisch, aber wir können die Abdeckungseinschlüsse ohne Duplizierung optimieren.

### Empfohlene Strategie

Konzentrieren Sie sich auf die **Generierung eines einzigen, umfassenden IT-Abdeckungsberichts in dem Modul, das die App ausführt** (hier `PlaygroundWeb`), während **Abdeckungsdaten für abhängige Module** wie `PlaygroundUtils` eingeschlossen werden. Dies vermeidet mehrfaches Testen und nutzt die Tatsache, dass aller Code in einer JVM ausgeführt wird.

**Warum dies gegenüber Aggregation?**
- Aggregation (`report-aggregate`) ist besser für verteilte Unit-Test-Abdeckung über Module hinweg. Für IT-Abdeckung aus einer einzelnen Laufzeit (Ihr Fall) ist sie überdimensioniert und passt nicht natürlich.
- Ein einheitlicher Bericht gibt einen ganzheitlichen Überblick über die Abdeckung der App, was oft nützlicher ist als isolierte modulspezifische Berichte (z.B. "80 % insgesamt, aber die Utils-Schicht liegt bei 60 %").
- Für größere Projekte skaliert dies, indem das "App-Modul" (WAR/EAR) als Abdeckungs-Hub behandelt wird, der Abhängigkeiten einbindet.

#### Schritt-für-Schritt-Implementierung für Ihr 2-Modul-Projekt

Fangen Sie klein an: Wenden Sie dies auf Ihr aktuelles Setup an (1 App-Modul + 1 Bibliothek). Testen Sie es und erweitern Sie es dann.

1.  **Behalten Sie die IT-Ausführung nur in `PlaygroundWeb` bei**:
    - Hier sind keine Änderungen nötig. Jetty startet das WAR (das `PlaygroundUtils` einbettet), Python-Tests treffen Endpunkte, Abdeckung wird in `${project.build.directory}/jacoco.it.exec` erfasst.
    - Bestätigen Sie, dass Utils-Code ausgeführt wird: Wenn Ihre Python-Tests Endpunkte aufrufen, die `PlaygroundUtils`-Klassen verwenden (z.B. `SystemUtils`), wird deren Abdeckung in der `.exec`-Datei sein.

2.  **Erweitern Sie den JaCoCo-Bericht in `PlaygroundWeb`, um `PlaygroundUtils` einzuschließen**:
    - Verwenden Sie JaCoCos `<additionalClassesDirectories>` und `<additionalSourceDirectories>` im `report`-Ziel. Dies weist JaCoCo an, Klassen/Quellen aus `PlaygroundUtils` gegen dieselbe `.exec`-Datei zu prüfen.
    - Aktualisieren Sie die POM von `PlaygroundWeb` (in der `jacoco-maven-plugin`-Konfiguration):

      ```xml
      <plugin>
          <groupId>org.jacoco</groupId>
          <artifactId>jacoco-maven-plugin</artifactId>
          <executions>
              <!-- Vorhandener prepare-agent -->
              <execution>
                  <id>prepare-agent</id>
                  <goals>
                      <goal>prepare-agent</goal>
                  </goals>
              </execution>
              <!-- Erweiterter Bericht: Utils-Modul einschließen -->
              <execution>
                  <id>report-it</id>
                  <phase>verify</phase>
                  <goals>
                      <goal>report</goal>
                  </goals>
                  <configuration>
                      <dataFile>${jacoco.it.exec}</dataFile>
                      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
                      <!-- Fügen Sie diese hinzu, um PlaygroundUtils-Abdeckung einzuschließen -->
                      <additionalClassesDirectories>
                          <directory>${project.parent.basedir}/PlaygroundUtils/target/classes</directory>
                      </additionalClassesDirectories>
                      <additionalSourceDirectories>
                          <directory>${project.parent.basedir}/PlaygroundUtils/src/main/java</directory>
                      </additionalSourceDirectories>
                  </configuration>
              </execution>
          </executions>
      </plugin>
      ```

    - Dies generiert einen Bericht (in `PlaygroundWeb/target/site/jacoco-it`), der beide Module abdeckt. Sie sehen Aufschlüsselungen nach Paket/Klasse, einschließlich `org.lzw` von utils.

3.  **Deaktivieren/Entfernen Sie JaCoCo aus `PlaygroundUtils`**:
    - Da es keine eigenen IT hat, entfernen Sie jegliche JaCoCo-Konfiguration/Properties (z.B. `<jacoco.it.exec>`, `<it.report.skip>`). Es muss keinen eigenen Bericht generieren – die Abdeckung wird upstream behandelt.
    - Wenn Sie Unit-Tests in utils haben, behalten Sie einen separaten `prepare-agent` + `report` für Unit-Abdeckung (standardmäßig `jacoco.exec`) bei, isolieren Sie diesen aber von IT.

4.  **Build und Verifikation**:
    - Führen Sie `mvn clean verify` vom Parent aus.
    - Jetty/Python läuft nur einmal (in `PlaygroundWeb`).
    - Prüfen Sie `PlaygroundWeb/target/site/jacoco-it/index.html`: Es sollte Abdeckung für Klassen beider Module anzeigen.
    - Wenn die Utils-Abdeckung bei 0 % liegt, stellen Sie sicher, dass Ihre Python-Tests diese Klassen ausführen (z.B. fügen Sie einen Test hinzu, der `SystemUtils` via einem Endpunkt triggert).

5.  **Optional: Erzwingen von Abdeckungsgrenzwerten**:
    - Fügen Sie eine `check`-Ausführung in `PlaygroundWeb`s JaCoCo-Plugin hinzu, um den Build bei Unterschreitung eines Grenzwerts fehlschlagen zu lassen (z.B. 70 % Zeilenabdeckung insgesamt).
      ```xml
      <execution>
          <id>check-it</id>
          <goals>
              <goal>check</goal>
          </goals>
          <configuration>
              <dataFile>${jacoco.it.exec}</dataFile>
              <rules>
                  <rule>
                      <element>BUNDLE</element>
                      <limits>
                          <limit>
                              <counter>LINE</counter>
                              <value>COVEREDRATIO</value>
                              <minimum>0.70</minimum>
                          </limit>
                      </limits>
                  </rule>
              </rules>
          </configuration>
      </execution>
      ```

#### Skalierung auf ein größeres Projekt (z.B. 10 Module)

Für 10+ Module (z.B. mehrere Bibliotheken + 1-2 App/WAR-Module) erweitern Sie das Obige, um Komplexität zu vermeiden:

- **Zentralisieren Sie IT in App-Modulen**: Wenn Sie einen Haupt-WAR haben (wie `PlaygroundWeb`), machen Sie ihn zum "Abdeckungs-Hub". Fügen Sie `<additionalClassesDirectories>` und `<additionalSourceDirectories>` für alle abhängigen Bibliotheken hinzu (z.B. über eine Schleife oder Property-Listen in der Parent-POM).
  - Beispiel: Definieren Sie Pfade in Parent-Properties:
    ```xml
    <properties>
        <lib1.classes>${project.basedir}/Lib1/target/classes</lib1.classes>
        <lib1.sources>${project.basedir}/Lib1/src/main/java</lib1.sources>
        <!-- Wiederholen für 10 Libs -->
    </properties>
    ```
  - In der JaCoCo-Berichtskonfiguration des WAR: Referenzieren Sie diese dynamisch.

- **Falls mehrere Apps/WARs vorhanden sind**: Erstellen Sie dedizierte IT-Module (z.B. `App1-IT`, `App2-IT`), die vom WAR abhängen, konfigurieren Sie Jetty/Exec/JaCoCo dort und schließen Sie nur relevante Klassen/Quellen der Abhängigkeiten ein. Dies hält Builds modular (z.B. `mvn verify -pl App1-IT` für gezielte Abdeckung).

- **Vermeiden Sie IT-Duplikation pro Modul**: Führen Sie Jetty/Python niemals in Bibliotheksmodulen aus – das ist verschwenderisch. Wenn eine Bibliothek isolierte IT benötigt (selten), geben Sie ihr ihren eigenen Mini-Server/Test-Suite.

- **Aggregation für Berichterstattung (falls benötigt)**: Wenn Sie auf separaten modulspezifischen Berichten bestehen:
  - Generieren Sie die `.exec` im App-Modul.
  - Verwenden Sie Mavens `dependency:copy` oder ein benutzerdefiniertes Skript (via Exec Plugin) im Parent-`post-integration-test`, um die `.exec` in das `target/` jedes Bibliotheksmoduls zu kopieren (z.B. als `jacoco-it.exec`).
  - Konfigurieren Sie dann `report` in jeder Bibliothek, um diese kopierte Datei zu verwenden.
  - Aber dies ist komplexer – bevorzugen Sie den einheitlichen Bericht, es sei denn, Stakeholder verlangen nach modulspezifischen Metriken.

- **Tooling-Tipps für Skalierung**:
  - **Maven-Profile**: Verwenden Sie Profile (z.B. `-Pcoverage`), um IT/Berichterstattung für schnellere Dev-Builds umzuschalten.
  - **CI-Optimierung**: In CI (z.B. GitHub Actions) cachen Sie Maven-Abhängigkeiten und führen IT nur bei Änderungen an Tests/Endpunkten aus.
  - **Alternativen, falls JaCoCo zu komplex wird**: Ziehen Sie SonarQube für aggregierte Analyse in Betracht (es verarbeitet JaCoCo-Daten über Module hinweg). Oder wechseln Sie zu Laufzeit-Tools wie OpenClover, aber JaCoCo ist in Ordnung, wenn Sie bei der Hub-Strategie bleiben.
  - **Testen der Tests**: Fügen Sie einen Smoke-Test in Python hinzu, um den Serverstart zu verifizieren (z.B. Abfrage von `http://localhost:8080/health`).

Diese Strategie minimiert Läufe (ein Jetty/Python pro App), handhabt JaCoCos Abhängigkeiten sauber und skaliert ohne Explosion. Wenn Sie mehr Details teilen (z.B. wie utils in Endpunkten verwendet wird), kann ich die POM-Snippets weiter verfeinern.