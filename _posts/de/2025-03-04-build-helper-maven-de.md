---
audio: false
generated: true
lang: de
layout: post
title: Maven-Plugin zum Erstellen von Builds
translated: true
---

Das `builder-helper-maven-plugin`, jetzt bekannt als **Build Helper Maven Plugin**, ist ein vielseitiges Werkzeug, das entwickelt wurde, um verschiedene Aufgaben im Maven-Build-Lebenszyklus zu unterstützen. Ursprünglich unter Codehaus gehostet, wird es jetzt von MojoHaus gepflegt, obwohl seine Maven-Koordinaten weiterhin die Gruppen-ID `org.codehaus.mojo` verwenden. Dieses Plugin bietet eine Reihe von Zielen, um bei Operationen wie dem Hinzufügen zusätzlicher Quellverzeichnisse, dem Anhängen zusätzlicher Artefakte, dem Parsen von Versionsinformationen und mehr zu helfen. Im Folgenden werde ich Ihnen zeigen, wie Sie dieses Plugin in Ihrem Maven-Projekt verwenden können.

### Was ist Maven?
Bevor wir uns mit dem Plugin beschäftigen, setzen wir den Kontext. Maven ist ein weit verbreitetes Build-Automatisierungswerkzeug, hauptsächlich für Java-Projekte. Es vereinfacht und standardisiert den Build-Prozess, indem es Abhängigkeiten verwaltet, Code kompiliert, Anwendungen verpackt und mehr, alles konfiguriert durch eine zentrale Datei namens `pom.xml`.

### Schritt 1: Plugin in Ihr `pom.xml` einbinden
Um das Build Helper Maven Plugin zu verwenden, müssen Sie es in die `pom.xml`-Datei Ihres Maven-Projekts im Abschnitt `<build><plugins>` einfügen. Hier ist, wie Sie es machen:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- Ausführungen für spezifische Ziele werden hier hinzugefügt -->
        </plugin>
    </plugins>
</build>
```

- **Gruppen-ID**: `org.codehaus.mojo` (spiegelt seine Ursprünge wider, obwohl es jetzt unter MojoHaus ist).
- **Artefakt-ID**: `build-helper-maven-plugin`.
- **Version**: Bis zu meinem letzten Update ist `3.6.0` die neueste Version, aber Sie sollten [Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin) für die neueste Veröffentlichung überprüfen.

Diese Deklaration macht das Plugin in Ihrem Projekt verfügbar, aber es wird nichts tun, bis Sie spezifische Ziele konfigurieren.

### Schritt 2: Ausführungen für spezifische Ziele konfigurieren
Das Build Helper Maven Plugin bietet mehrere Ziele, jedes für eine bestimmte Aufgabe entwickelt. Sie konfigurieren diese Ziele, indem Sie `<executions>`-Blöcke innerhalb der Plugin-Deklaration hinzufügen, in denen Sie festlegen, wann sie laufen sollen (über eine Maven-Lebenszyklusphase) und wie sie sich verhalten sollen.

Hier sind einige häufig verwendete Ziele und ihre Zwecke:

- **`add-source`**: Fügt zusätzliche Quellverzeichnisse zu Ihrem Projekt hinzu.
- **`add-test-source`**: Fügt zusätzliche Testquellverzeichnisse hinzu.
- **`add-resource`**: Fügt zusätzliche Ressourcenverzeichnisse hinzu.
- **`attach-artifact`**: Hängt zusätzliche Artefakte (z. B. Dateien) an Ihr Projekt für Installation und Bereitstellung an.
- **`parse-version`**: Parsed die Projektversion und setzt Eigenschaften (z. B. Haupt-, Neben-, Inkrementversions).

Jedes Ziel erfordert seine eigene Konfiguration, die Sie innerhalb eines `<execution>`-Blocks definieren.

### Schritt 3: Beispiel – Hinzufügen eines zusätzlichen Quellverzeichnisses
Ein häufiger Anwendungsfall für dieses Plugin ist das Hinzufügen eines zusätzlichen Quellverzeichnisses, da Maven standardmäßig nur eines unterstützt (`src/main/java`). Hier ist, wie Sie das Ziel `add-source` konfigurieren, um ein zusätzliches Quellverzeichnis zu enthalten:

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
                            <source>Pfad/zu/Ihrem/zusätzlichen/Quellverzeichnis</source>
                        </sources>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`<id>`**: Ein eindeutiger Bezeichner für diese Ausführung (z. B. `add-source`).
- **`<phase>`**: Die Maven-Lebenszyklusphase, in der das Ziel läuft (z. B. `generate-sources` stellt sicher, dass das Verzeichnis früh im Build hinzugefügt wird).
- **`<goals>`**: Gibt das auszuführende Ziel an (`add-source` in diesem Fall).
- **`<configuration>`**: Definiert das zusätzliche Quellverzeichnis (ersetzen Sie `Pfad/zu/Ihrem/zusätzlichen/Quellverzeichnis` durch Ihren tatsächlichen Pfad, z. B. `src/main/generated`).

Wenn Sie einen Maven-Befehl wie `mvn compile` ausführen, wird Maven dieses zusätzliche Verzeichnis als Quellordner einbeziehen.

### Zusätzliche Hinweise
- **Versionskompatibilität**: Ab Version 3.0.0 erfordert das Plugin Maven 3 oder höher. Wenn Sie eine ältere Maven-Version verwenden, müssen Sie eine Plugin-Version 1.12 oder früher verwenden.
- **Mehrere Ziele**: Sie können mehrere `<execution>`-Blöcke innerhalb desselben Plugins definieren, um verschiedene Ziele auszuführen. Zum Beispiel könnten Sie sowohl Quell- als auch Testquellverzeichnisse hinzufügen, indem Sie Ausführungen für `add-source` und `add-test-source` enthalten.
- **Ausführen des Plugins**: Sobald konfiguriert, wird das Ausführen eines Maven-Befehls (z. B. `mvn clean install`) die Ziele des Plugins während der angegebenen Phasen auslösen.

### Weitere Ressourcen
Für weitere Details und Beispiele anderer Ziele besuchen Sie die [offizielle Verwendungsseite](https://www.mojohaus.org/build-helper-maven-plugin/usage.html). Diese Seite bietet umfassende Dokumentation und Beispielkonfigurationen für alle verfügbaren Ziele.

### Schlussgedanken
Das Build Helper Maven Plugin ist eine mächtige Ergänzung zu Ihrem Maven-Werkzeugkasten, insbesondere für Projekte, die nicht standardmäßige Build-Konfigurationen erfordern. Durch das Einfügen in Ihr `pom.xml` und das Konfigurieren der entsprechenden Ziele können Sie Ihren Build-Prozess an spezifische Anforderungen anpassen. Obwohl es unter Codehaus seinen Ursprung hatte, ist sein derzeitiges Zuhause MojoHaus, und es bleibt eine zuverlässige Wahl zur Verbesserung von Maven-Builds.