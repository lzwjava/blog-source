---
audio: false
generated: true
lang: de
layout: post
title: Build Helper Maven Plugin
translated: true
type: note
---

Das `builder-helper-maven-plugin`, nun bekannt als **Build Helper Maven Plugin**, ist ein vielseitiges Tool, das bei verschiedenen Aufgaben im Maven Build-Lifecycle hilft. Ursprünglich bei Codehaus gehostet, wird es jetzt von MojoHaus gepflegt, auch wenn seine Maven-Koordinaten weiterhin die `org.codehaus.mojo` Group-ID verwenden. Dieses Plugin bietet eine Reihe von Goals, die bei Operationen wie dem Hinzufügen zusätzlicher Quellverzeichnisse, dem Anhängen weiterer Artefakte, dem Parsen von Versionsinformationen und mehr helfen. Im Folgenden zeige ich Ihnen, wie Sie dieses Plugin in Ihrem Maven-Projekt verwenden können.

### Was ist Maven?
Bevor wir uns mit dem Plugin befassen, schaffen wir den Kontext. Maven ist ein weit verbreitetes Build-Automatisierungstool, hauptsächlich für Java-Projekte. Es vereinfacht und standardisiert den Build-Prozess, indem es Abhängigkeiten verwaltet, Code kompiliert, Anwendungen packaget und mehr, alles konfiguriert über eine zentrale Datei namens `pom.xml`.

### Schritt 1: Binden Sie das Plugin in Ihre `pom.xml` ein
Um das Build Helper Maven Plugin zu verwenden, müssen Sie es im Abschnitt `<build><plugins>` Ihrer Maven-Projekt-`pom.xml`-Datei hinzufügen. So geht das:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- Executions für spezifische Goals werden hier hinzugefügt -->
        </plugin>
    </plugins>
</build>
```

- **Group ID**: `org.codehaus.mojo` (spiegelt seinen Ursprung wider, obwohl es jetzt unter MojoHaus ist).
- **Artifact ID**: `build-helper-maven-plugin`.
- **Version**: Nach meinem letzten Stand ist `3.6.0` die neueste Version, aber Sie sollten [Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin) für die aktuellste Version überprüfen.

Diese Deklaration macht das Plugin in Ihrem Projekt verfügbar, aber es wird nichts tun, bis Sie spezifische Goals konfigurieren.

### Schritt 2: Konfigurieren Sie Executions für spezifische Goals
Das Build Helper Maven Plugin bietet mehrere Goals, die jeweils für eine bestimmte Aufgabe konzipiert sind. Sie konfigurieren diese Goals, indem Sie `<executions>`-Blöcke innerhalb der Plugin-Deklaration hinzufügen. Darin legen Sie fest, wann sie ausgeführt werden sollen (über eine Maven-Lifecycle-Phase) und wie sie sich verhalten sollen.

Hier sind einige häufig verwendete Goals und ihre Zwecke:

- **`add-source`**: Fügt zusätzliche Quellverzeichnisse zu Ihrem Projekt hinzu.
- **`add-test-source`**: Fügt zusätzliche Test-Quellverzeichnisse hinzu.
- **`add-resource`**: Fügt zusätzliche Ressourcenverzeichnisse hinzu.
- **`attach-artifact`**: Hängt zusätzliche Artefakte (z.B. Dateien) an Ihr Projekt für die Installation und das Deployment an.
- **`parse-version`**: Parst die Version des Projekts und setzt Properties (z.B. Major-, Minor-, Incremental-Version).

Jedes Goal erfordert seine eigene Konfiguration, die Sie innerhalb eines `<execution>`-Blocks definieren.

### Schritt 3: Beispiel – Hinzufügen eines zusätzlichen Quellverzeichnisses
Ein häufiger Anwendungsfall für dieses Plugin ist das Hinzufügen eines zusätzlichen Quellverzeichnisses, da Maven standardmäßig normalerweise nur eines unterstützt (`src/main/java`). So konfigurieren Sie das `add-source`-Goal, um ein zusätzliches Quellverzeichnis einzubinden:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <executions>
                <execution>
                    <id>add-source</id>
                    <phase>generate-sources</phase>
                    <goals>
                        <goal>add-source</goal>
                    </goals>
                    <configuration>
                        <sources>
                            <source>pfad/zu/ihrem/extra/quellverzeichnis</source>
                        </sources>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`<id>`**: Ein eindeutiger Bezeichner für diese Execution (z.B. `add-source`).
- **`<phase>`**: Die Maven-Lifecycle-Phase, in der das Goal ausgeführt wird (z.B. `generate-sources` stellt sicher, dass das Verzeichnis früh im Build hinzugefügt wird).
- **`<goals>`**: Spezifiziert das auszuführende Goal (`add-source` in diesem Fall).
- **`<configuration>`**: Definiert das zusätzliche Quellverzeichnis (ersetzen Sie `pfad/zu/ihrem/extra/quellverzeichnis` mit Ihrem tatsächlichen Pfad, z.B. `src/main/generated`).

Wenn Sie einen Maven-Befehl wie `mvn compile` ausführen, wird Maven dieses zusätzliche Verzeichnis als Quellordner einbeziehen.

### Zusätzliche Hinweise
- **Versionskompatibilität**: Seit Version 3.0.0 erfordert das Plugin Maven 3 oder höher. Wenn Sie eine ältere Maven-Version verwenden, benötigen Sie die Plugin-Version 1.12 oder früher.
- **Mehrere Goals**: Sie können mehrere `<execution>`-Blöcke innerhalb desselben Plugins definieren, um verschiedene Goals auszuführen. Sie könnten beispielsweise sowohl Quell- als auch Test-Quellverzeichnisse hinzufügen, indem Sie Executions für `add-source` und `add-test-source` einfügen.
- **Ausführen des Plugins**: Sobald es konfiguriert ist, wird das Ausführen eines Maven-Befehls (z.B. `mvn clean install`) die Goals des Plugins während der spezifizierten Phasen auslösen.

### Weitere Ressourcen
Weitere Details und Beispiele für andere Goals finden Sie auf der [offiziellen Usage-Seite](https://www.mojohaus.org/build-helper-maven-plugin/usage.html). Diese Seite bietet umfassende Dokumentation und Beispielkonfigurationen für alle verfügbaren Goals.

### Abschließende Gedanken
Das Build Helper Maven Plugin ist eine leistungsstarke Ergänzung für Ihr Maven-Werkzeugset, insbesondere für Projekte, die nicht-standardisierte Build-Konfigurationen erfordern. Indem Sie es in Ihre `pom.xml` aufnehmen und die entsprechenden Goals konfigurieren, können Sie Ihren Build-Prozess an spezifische Bedürfnisse anpassen. Obwohl es ursprünglich von Codehaus stammt, ist sein aktuelles Zuhause MojoHaus, und es bleibt eine zuverlässige Wahl zur Erweiterung von Maven-Builds.