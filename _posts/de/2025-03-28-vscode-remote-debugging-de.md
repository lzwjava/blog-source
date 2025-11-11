---
audio: false
generated: true
lang: de
layout: post
title: Remotedebugging mit VSCode
translated: true
type: note
---

Um Remote Debugging in Visual Studio Code (VSCode) für einen WebSphere Liberty Server durchzuführen, der im Debug-Modus läuft, können Sie die integrierten Java-Debugging-Funktionen von VSCode verwenden. Im Folgenden finden Sie die detaillierten Schritte zur Einrichtung, ohne dass WebSphere Liberty-spezifische Plugins installiert werden müssen, vorausgesetzt, das standardmäßige **Java Extension Pack** (das den **Debugger for Java** enthält) ist bereits installiert.

---

### Schritt 1: Starten des WebSphere Liberty Servers im Debug-Modus
1. Öffnen Sie ein Terminal oder eine Eingabeaufforderung.
2. Navigieren Sie zu Ihrem WebSphere Liberty-Installationsverzeichnis.
3. Führen Sie den folgenden Befehl aus, um Ihren Server im Debug-Modus zu starten:
   ```
   server debug default
   ```
   - Ersetzen Sie `default` durch den Namen Ihres Servers, falls dieser abweicht.
4. Der Server startet mit aktiviertem Debugging, in der Regel lauschend auf Port **7777**.
5. Überprüfen Sie die Konsolenausgabe oder die Protokolle des Servers auf eine Meldung wie:
   ```
   Listening for transport dt_socket at address: 7777
   ```
   - Dies bestätigt den Debug-Port. Falls ein anderer Port verwendet wird (z.B. aufgrund eines Konflikts), notieren Sie die angezeigte Nummer.

---

### Schritt 2: Konfigurieren des Remote Debugging in VSCode
1. **Öffnen Sie Ihr Projekt in VSCode**:
   - Stellen Sie sicher, dass Ihr Java-Projekt (das den Quellcode enthält, der auf dem Server bereitgestellt wird) in VSCode geöffnet ist. Dies ermöglicht es dem Debugger, Breakpoints dem ausgeführten Code zuzuordnen.

2. **Zugriff auf die Ansicht "Run and Debug"**:
   - Klicken Sie auf das Symbol **Run and Debug** in der linken Seitenleiste (eine Wiedergabetaste mit einem Käfer) oder drücken Sie `Strg+Umschalt+D` (Windows/Linux) bzw. `Befehl+Umschalt+D` (Mac).

3. **Erstellen oder Bearbeiten der `launch.json`-Datei**:
   - Klicken Sie in der Ansicht **Run and Debug** auf das **Zahnradsymbol** neben dem Konfigurations-Dropdown-Menü.
   - Wenn Sie aufgefordert werden, eine Umgebung auszuwählen, wählen Sie **Java**. Dadurch wird eine `launch.json`-Datei im `.vscode`-Ordner Ihres Arbeitsbereichs erstellt.
   - Wenn die Datei bereits existiert, wird sie zur Bearbeitung geöffnet.

4. **Hinzufügen einer Debug-Konfiguration**:
   - Stellen Sie in der `launch.json`-Datei sicher, dass sie eine Konfiguration zum Anhängen an die entfernte JVM enthält. Hier ist ein Beispiel:
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "type": "java",
                 "name": "Attach to WebSphere Liberty",
                 "request": "attach",
                 "hostName": "localhost",
                 "port": 7777
             }
         ]
     }
     ```
   - **Erklärung der Felder**:
     - `"type": "java"`: Spezifiziert den Java-Debugger.
     - `"name": "Attach to WebSphere Liberty"`: Ein beschreibender Name für diese Konfiguration.
     - `"request": "attach"`: Zeigt an, dass VSCode sich an einen vorhandenen JVM-Prozess anhängt.
     - `"hostName": "localhost"`: Der Hostname des Rechners, auf dem der Server läuft. Verwenden Sie die IP-Adresse oder den Hostnamen des Servers, wenn er auf einem anderen Rechner läuft.
     - `"port": 7777`: Der Debug-Port aus Schritt 1. Aktualisieren Sie diesen Wert, falls der Server einen anderen Port verwendet.

5. **Speichern der Datei**:
   - Speichern Sie die `launch.json`-Datei nach dem Hinzufügen oder Bearbeiten der Konfiguration.

---

### Schritt 3: Starten der Debugging-Sitzung
1. **Stellen Sie sicher, dass der Server läuft**:
   - Vergewissern Sie sich, dass der WebSphere Liberty Server noch im Debug-Modus aus Schritt 1 läuft.

2. **Wählen Sie die Konfiguration aus**:
   - Wählen Sie in der Ansicht **Run and Debug** die Option **"Attach to WebSphere Liberty"** aus dem Dropdown-Menü oben aus.

3. **Starten Sie den Debugger**:
   - Klicken Sie auf den grünen **Wiedergabe-Button** oder drücken Sie `F5`. VSCode verbindet sich mit dem JVM-Prozess des Servers.

4. **Setzen Sie Breakpoints**:
   - Öffnen Sie Ihre Java-Quelldateien in VSCode.
   - Klicken Sie in den linken Rand (links von den Zeilennummern), um Breakpoints an den Stellen zu setzen, an denen die Ausführung pausieren soll.

5. **Interagieren Sie mit der Anwendung**:
   - Verwenden Sie Ihre Anwendung (z.B. senden Sie HTTP-Anfragen), um die Code-Pfade mit Breakpoints auszulösen. Wenn ein Breakpoint erreicht wird, hält VSCode die Ausführung an, sodass Sie Variablen inspizieren, den Code schrittweise durchgehen und debuggen können.

---

### Zusätzliche Hinweise
- **Lokaler vs. Entfernter Server**:
  - Wenn der Server auf einem anderen Rechner läuft, ersetzen Sie `"localhost"` durch den Hostnamen oder die IP-Adresse des Servers in der `launch.json`-Datei. Stellen Sie sicher, dass der Debug-Port über das Netzwerk erreichbar ist (z.B. nicht durch eine Firewall blockiert).

- **Bestätigung des Debug-Ports**:
  - Wenn Sie sich bezüglich des Ports unsicher sind, überprüfen Sie immer die Ausgabe des Servers nach dem Ausführen von `server debug default`. Sie gibt explizit den Port aus, auf dem gelauscht wird.

- **Übereinstimmung des Quellcodes**:
  - Der Quellcode in VSCode muss mit dem auf dem Server ausgeführten Code übereinstimmen, damit Breakpoints korrekt funktionieren. Stellen Sie sicher, dass Ihr Projekt auf dem neuesten Stand ist und mit Debug-Informationen kompiliert wurde (Standard in den meisten Java-Builds).

- **Server-Verhalten**:
  - Mit `server debug default` startet der Server sofort (wartet nicht auf einen Debugger). Sie können VSCode jederzeit anhängen, während er läuft.

- **Voraussetzungen**:
  - Das **Java Extension Pack** (oder mindestens die Erweiterung **Debugger for Java**) muss in VSCode installiert sein. Dies ist ein Standard-Tool für die Java-Entwicklung und bietet die notwendigen Debugging-Fähigkeiten.

---

Indem Sie diese Schritte befolgen, können Sie Ihren WebSphere Liberty Server effektiv remote debuggen, indem Sie die integrierten Funktionen von VSCode verwenden, ohne zusätzliche, spezifische WebSphere-Plugins zu benötigen.