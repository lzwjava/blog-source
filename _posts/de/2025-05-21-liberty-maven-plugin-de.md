---
audio: false
generated: true
lang: de
layout: post
title: Liberty Maven Plugin
translated: true
type: note
---

Um Ihr Ziel zu erreichen, ein Skript in IntelliJ IDEA unter Windows auszuführen, das Ihren Liberty-Server schnell verwaltet und Ihr Programm baut, während sichergestellt wird, dass der Server vor dem Ersetzen der EAR-Datei gestoppt wird, empfehle ich die Verwendung des **Liberty Maven Plugins**. Dieser Ansatz ist unkompliziert, integriert sich gut in Ihren Maven-Build-Prozess und vermeidet die Probleme, die Sie mit der Befehlsformatierung und Batch-Dateien hatten.

So richten Sie es ein:

---

### Lösung: Verwenden des Liberty Maven Plugins

#### Schritt 1: Fügen Sie das Liberty Maven Plugin zu Ihrer `pom.xml` hinzu
Das Liberty Maven Plugin ermöglicht es Ihnen, den Liberty-Server (starten, stoppen, deployen etc.) direkt über Maven zu steuern, was komplexe Skripte oder Batch-Dateien überflüssig macht.

- Öffnen Sie die `pom.xml`-Datei Ihres Projekts.
- Fügen Sie die folgende Plugin-Konfiguration im Abschnitt `<build>` hinzu:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>io.openliberty.tools</groupId>
            <artifactId>liberty-maven-plugin</artifactId>
            <version>3.3.4</version>
            <configuration>
                <serverName>default</serverName>
                <installDirectory>C:\pfad\zu\liberty</installDirectory>
            </configuration>
        </plugin>
    </plugins>
</build>
```

- **Ersetzen** Sie `C:\pfad\zu\liberty` mit dem tatsächlichen Pfad zu Ihrem Liberty-Installationsverzeichnis (z.B. `C:\Program Files\IBM\WebSphere\Liberty`).
- Der `<serverName>default</serverName>` entspricht Ihrer Verwendung von `default` in den Befehlen `server start default` und `server stop default`.

#### Schritt 2: Erstellen Sie eine Maven-Run-Konfiguration in IntelliJ IDEA
Anstatt ein Skript oder eine Batch-Datei zu verwenden, können Sie IntelliJ IDEA so konfigurieren, dass eine Abfolge von Maven-Goals ausgeführt wird, die den Server stoppt, Ihr Projekt baut und den Server wieder startet.

- Gehen Sie in IntelliJ IDEA zu **Run > Edit Configurations...**.
- Klicken Sie auf den **+**-Button und wählen Sie **Maven** aus der Liste aus.
- Konfigurieren Sie die Run-Konfiguration:
  - **Name:** Vergeben Sie einen aussagekräftigen Namen, z.B. `Run Liberty`.
  - **Working directory:** Stellen Sie sicher, dass es auf Ihr Projektverzeichnis gesetzt ist (wird normalerweise automatisch erkannt).
  - **Command line:** Geben Sie die folgende Abfolge von Maven-Goals ein:
    ```
    liberty:stop package liberty:start
    ```
- Klicken Sie auf **Apply** und dann auf **OK**.

#### Schritt 3: Führen Sie die Konfiguration aus
- Verwenden Sie den **Run**-Button (grünes Dreieck) in IntelliJ IDEA, um diese Konfiguration auszuführen.
- Dies wird:
  1. **Den Liberty-Server stoppen** (`liberty:stop`): Stellt sicher, dass der Server nicht läuft, wenn die EAR-Datei ersetzt wird.
  2. **Ihr Projekt bauen** (`package`): Führt `mvn package` aus, um die EAR-Datei zu generieren.
  3. **Den Liberty-Server starten** (`liberty:start`): Startet den Server mit der aktualisierten EAR-Datei neu.

---

### Warum das für Sie funktioniert
- **Behebt Probleme mit der Befehlsformatierung:** Sie erwähnten, dass die Verwendung von "Script text" in der Run-Konfiguration `server start default` in separate Argumente (`server`, `start`, `default`) aufteilt. Der Maven-Ansatz umgeht dies vollständig durch die Verwendung von wohldefinierten Plugin-Goals.
- **Vermeidet die Komplexität von Batch-Dateien:** Sie fanden es schwierig, eine `.bat`-Datei korrekt zum Laufen zu bringen (z.B. aufgrund von Pfaden oder Umgebungseinstellungen). Das Liberty Maven Plugin übernimmt die Serververwaltung intern, sodass Sie keine Batch-Datei-Befehle oder Pfade debuggen müssen.
- **Erfüllt Ihre Anforderung:** Sie benötigen, dass der Server beim Ersetzen der EAR-Datei gestoppt wird, um Startprobleme zu vermeiden. Diese Lösung stoppt den Server explizit vor dem Bauen und startet ihn anschließend wieder, was einen sauberen Prozess gewährleistet.

---

### Alternative: Verwendung einer Batch-Datei (falls bevorzugt)
Wenn Sie lieber bei einer Batch-Datei bleiben möchten, hier ein funktionierendes Beispiel, obwohl es aufgrund der von Ihnen geschilderten Probleme weniger empfohlen wird:

1. Erstellen Sie eine Datei namens `runLiberty.bat` in Ihrem Projektverzeichnis mit folgendem Inhalt:

```bat
@echo off
set LIBERTY_BIN=C:\pfad\zu\liberty\bin
set MAVEN_HOME=C:\pfad\zu\maven
set PATH=%PATH%;%LIBERTY_BIN%;%MAVEN_HOME%\bin

"%LIBERTY_BIN%\server" stop default
mvn package
"%LIBERTY_BIN%\server" start default
```

- Ersetzen Sie `C:\pfad\zu\liberty` und `C:\pfad\zu\maven` mit den tatsächlichen Pfaden zu Ihren Liberty- und Maven-Installationen.

2. In IntelliJ IDEA:
   - Gehen Sie zu **Run > Edit Configurations...**.
   - Klicken Sie auf **+** und wählen Sie **Batch file**.
   - Setzen Sie den **Path to batch file** auf den Speicherort von `runLiberty.bat`.
   - Setzen Sie das **Working directory** auf Ihr Projektverzeichnis.
   - Klicken Sie auf **Apply** und **OK**.

3. Führen Sie sie mit dem **Run**-Button aus.

Allerdings erfordert diese Methode, dass Sie manuell sicherstellen, dass Pfade und Umgebungsvariablen korrekt sind, was Sie als schwierig empfanden. Der Maven-Plugin-Ansatz ist einfacher und zuverlässiger.

---

### Empfehlung
Verwenden Sie die oben beschriebene **Liberty Maven Plugin**-Methode. Sie ist:
- **Integriert:** Bindet sich in Ihren bestehenden Maven-Build-Prozess ein.
- **Einfach:** Kein Kampf mit der Batch-Datei-Syntax oder Pfaden notwendig.
- **Zuverlässig:** Verwaltet das Stoppen und Starten des Servers korrekt und vermeidet Probleme beim Ersetzen der EAR-Datei.

Dieses Setup ermöglicht es Ihnen, Ihr Programm schnell und konsistent in IntelliJ IDEA auf Ihrem Liberty-Server auszuführen!