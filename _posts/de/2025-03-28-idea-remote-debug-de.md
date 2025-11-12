---
audio: false
generated: true
lang: de
layout: post
title: Integrierte Fernentwicklung von IntelliJ IDEA
translated: true
type: note
---

Um IntelliJ IDEA mit dem Debug-Port eines WebSphere Liberty Servers zu verbinden, den Sie mit `server debug default` gestartet haben, ohne das WebSphere Liberty Plugin zu verwenden, können Sie die integrierte Remote-Debugging-Funktion von IntelliJ IDEA nutzen. Dieser Ansatz funktioniert, weil WebSphere Liberty im Debug-Modus einen Debug-Port (standardmäßig typischerweise 7777) freigibt, an den sich jeder JVM-Debugger, einschließlich IntelliJ IDEA, anbinden kann. Im Folgenden finden Sie die detaillierten Schritte, um dies zu erreichen:

---

### Schritt 1: Starten Sie den WebSphere Liberty Server im Debug-Modus
Wenn Sie `server debug default` ausführen (angenommen, "default" ist der Name Ihres Servers; ersetzen Sie ihn durch Ihren tatsächlichen Servernamen, falls dieser abweicht), startet WebSphere Liberty mit aktiviertem Debugging. Standardmäßig konfiguriert dieser Befehl den Server so, dass er auf Debug-Verbindungen auf Port **7777** lauscht.

- **Befehl**:
  ```bash
  server debug default
  ```
- **Was es tut**: Dies startet den "default"-Server im Debug-Modus und aktiviert automatisch die JVM-Debugging-Optionen (z.B. `-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=7777`).
- **Überprüfung**: Überprüfen Sie nach Ausführung des Befehls die Server-Konsolenausgabe oder die Logs (z.B. `messages.log`), um zu bestätigen, dass der Server auf den Debug-Port lauscht. Suchen Sie nach einer Meldung, die den Debug-Port angibt (normalerweise 7777, es sei denn, er wurde überschrieben oder ist nicht verfügbar).

---

### Schritt 2: Bestätigen Sie den Debug-Port
Der Standard-Debug-Port für WebSphere Liberty ist **7777**. Wenn dieser Port jedoch belegt ist oder angepasst wurde:
- Überprüfen Sie die Konsolenausgabe nach dem Start des Servers. Dort sollte eine Meldung wie "Listening for debugger connections on port 7777." erscheinen.
- Wenn der Port abweicht (z.B. aufgrund eines Konflikts ein zufälliger Port zugewiesen wurde), notieren Sie sich die tatsächliche Portnummer für die Verwendung in IntelliJ IDEA.

Für diese Anleitung gehen wir vom Standard-Port **7777** aus, sofern Ihr Setup nichts anderes anzeigt.

---

### Schritt 3: Konfigurieren Sie das Remote-Debugging in IntelliJ IDEA
Die Remote-Debugging-Funktion von IntelliJ IDEA ermöglicht es Ihnen, eine Verbindung zur JVM des Servers herzustellen, ohne ein spezifisches WebSphere-Plugin zu benötigen. So richten Sie es ein:

1. **Öffnen Sie die Run/Debug-Konfigurationen**:
   - Gehen Sie in IntelliJ IDEA im oberen Menü zu **Run > Edit Configurations**.

2. **Fügen Sie eine neue Remote-Debug-Konfiguration hinzu**:
   - Klicken Sie auf die **+** Schaltfläche (oder "Add New Configuration") in der oberen linken Ecke.
   - Wählen Sie aus der Liste **Remote JVM Debug** (je nach IntelliJ-Version könnte es auch nur "Remote" heißen).

3. **Legen Sie die Konfigurationsdetails fest**:
   - **Name**: Vergeben Sie einen aussagekräftigen Namen, z.B. "WebSphere Liberty Debug".
   - **Host**: Setzen Sie ihn auf `localhost` (vorausgesetzt, der Server läuft auf demselben Rechner wie IntelliJ IDEA; verwenden Sie die IP-Adresse des Servers, wenn er remote ist).
   - **Port**: Setzen Sie ihn auf `7777` (oder den tatsächlichen Debug-Port, falls abweichend).
   - **Transport**: Stellen Sie sicher, dass er auf **Socket** gesetzt ist.
   - **Debugger Mode**: Wählen Sie **Attach** (dies weist IntelliJ an, sich zu einer bereits laufenden JVM zu verbinden).
   - Belassen Sie andere Einstellungen (wie "Command line arguments for remote JVM") standardmäßig, sofern Sie keine spezifischen JVM-Optionen benötigen.

4. **Speichern Sie die Konfiguration**:
   - Klicken Sie auf **Apply** und dann auf **OK**, um zu speichern.

---

### Schritt 4: Starten Sie das Debugging
Wenn der Server im Debug-Modus läuft und die Konfiguration eingerichtet ist:
- Gehen Sie zu **Run > Debug** (oder klicken Sie auf das Käfer-Symbol) und wählen Sie Ihre neue Konfiguration aus (z.B. "WebSphere Liberty Debug").
- IntelliJ IDEA wird versuchen, sich an die JVM des Servers auf dem angegebenen Host und Port anzubinden.
- Bei Erfolg sehen Sie eine Meldung im Debug-Fenster wie "Connected to the target VM, address: 'localhost:7777'."

---

### Schritt 5: Debuggen Sie Ihre Anwendung
- **Setzen Sie Breakpoints**: Klicken Sie in Ihrem Quellcode in den Gutter neben den Zeilennummern, um Breakpoints an den Stellen zu setzen, an denen die Ausführung pausieren soll.
- **Lösen Sie die Ausführung aus**: Interagieren Sie mit Ihrer Anwendung (z.B. senden Sie eine Anfrage an den Server), um die Breakpoints zu treffen.
- **Debuggen**: Sobald ein Breakpoint getroffen wird, verwenden Sie die Debugging-Werkzeuge von IntelliJ (step over, step into, resume usw.), um Variablen zu inspizieren und die Ausführung zu steuern.

---

### Zusätzliche Hinweise
- **Lokaler vs. Remote-Server**: Wenn WebSphere Liberty auf einem anderen Rechner läuft, ersetzen Sie `localhost` durch die IP-Adresse des Servers in der Remote-Debug-Konfiguration. Stellen Sie sicher, dass der Debug-Port (z.B. 7777) offen und nicht durch eine Firewall blockiert ist.
- **Port-Konflikte**: Wenn Port 7777 beim Serverstart nicht verfügbar ist, könnte WebSphere Liberty einen zufälligen Port wählen. Überprüfen Sie die Serverausgabe, um den Port zu bestätigen, und passen Sie die IntelliJ-Konfiguration entsprechend an.
- **Kein Plugin erforderlich**: Diese Methode verwendet die standardmäßige Remote-Debugging-Funktion von IntelliJ IDEA, sodass kein WebSphere Liberty Plugin benötigt wird.

---

### Zusammenfassung
Indem Sie Ihren WebSphere Liberty Server mit `server debug default` starten (was standardmäßig das Debugging auf Port 7777 aktiviert) und ein Remote-Debug-Setup in IntelliJ IDEA konfigurieren, können Sie sich ohne das WebSphere Liberty Plugin mit dem Debug-Port des Servers verbinden. Dies gibt Ihnen volle Debugging-Fähigkeiten – Breakpoints, Variableninspektion und schrittweise Ausführung – direkt innerhalb von IntelliJ IDEA.

---

Das Ausführen und Debuggen von WebSphere Liberty-Anwendungen in IntelliJ IDEA ohne das dedizierte Liberty Tools Plugin ist durch manuelles Einrichten der Liberty-Laufzeitumgebung und Konfigurieren von IntelliJ IDEA für Remote-Debugging und die Ausführung externer Tools erreichbar. Dieser Ansatz erfordert im Vergleich zur Verwendung des integrierten Plugins einige manuelle Schritte, bietet aber die notwendige Funktionalität, um Ihre Liberty-Anwendungen zu entwickeln und zu troubleshooten.

Hier ist eine Aufschlüsselung des Prozesses:

**1. Beschaffen und Installieren der WebSphere Liberty Runtime:**

Da Sie das Plugin nicht haben, das die Laufzeitumgebung für Sie verwaltet, müssen Sie die WebSphere Liberty Runtime manuell herunterladen und installieren. Sie können die Runtime von der offiziellen IBM-Website beziehen oder über andere Verteilungsmethoden wie Maven oder Gradle, wenn Sie Ihr Projekt mit diesen Tools verwalten.

Typischerweise beinhaltet die manuelle Installation das Herunterladen einer ZIP- oder JAR-Datei und das Extrahieren in ein Verzeichnis auf Ihrem System. Dieses Verzeichnis wird Ihr Liberty-Installationsverzeichnis (`<LIBERTY_HOME>`).

**2. Konfigurieren des Liberty-Servers für das Debugging:**

Um Ihre Anwendung zu debuggen, müssen Sie den Liberty-Server mit aktiviertem Debugging starten. Dies geschieht durch das Hinzufügen spezifischer JVM-Optionen beim Start des Servers. Diese Optionen weisen die Java Virtual Machine (JVM) an, auf einer bestimmten Port auf eine Debugger-Verbindung zu warten.

Suchen Sie die Datei `jvm.options` in Ihrem Liberty-Server-Konfigurationsverzeichnis (`<LIBERTY_HOME>/usr/servers/<Ihr_Servername>/`). Wenn diese Datei nicht existiert, können Sie sie erstellen. Fügen Sie die folgende Zeile zur `jvm.options`-Datei hinzu:

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005
```

  * `-agentlib:jdwp`: Lädt die Java Debug Wire Protocol (JDWP)-Bibliothek.
  * `transport=dt_socket`: Spezifiziert, dass der Debugger sich über einen Socket verbindet.
  * `server=y`: Zeigt an, dass die JVM als Server agiert und auf eine Debugger-Verbindung wartet.
  * `suspend=n`: Spezifiziert, dass die JVM nicht warten soll, bis der Debugger verbunden ist, bevor sie startet. Sie können dies auf `suspend=y` ändern, wenn Sie Code debuggen müssen, der während des Serverstarts ausgeführt wird.
  * `address=5005`: Setzt die Portnummer, mit der sich der Debugger verbindet. Sie können dies auf jeden verfügbaren Port ändern.

**3. Konfigurieren von IntelliJ IDEA zum Ausführen von Liberty:**

Sie können die "External Tools"-Konfiguration von IntelliJ IDEA verwenden, um Ihren Liberty-Server aus der IDE heraus zu starten.

  * Gehen Sie zu `File` > `Settings` (oder `IntelliJ IDEA` > `Preferences` auf macOS).
  * Navigieren Sie zu `Tools` > `External Tools`.
  * Klicken Sie auf das `+` Symbol, um ein neues externes Tool hinzuzufügen.
  * Konfigurieren Sie das Tool mit den folgenden Details:
      * **Name:** Vergeben Sie einen beschreibenden Namen, z.B. "Start Liberty Server".
      * **Program:** Navigieren Sie zum Liberty-Server-Skript. Dies ist typischerweise `<LIBERTY_HOME>/bin/server` für Linux/macOS oder `<LIBERTY_HOME>\bin\server.bat` für Windows.
      * **Arguments:** Fügen Sie die Argumente hinzu, um Ihre spezifische Serverinstanz zu starten. Dies ist normalerweise `start <Ihr_Servername>`, wobei `<Ihr_Servername>` der Name Ihres Serververzeichnisses in `<LIBERTY_HOME>/usr/servers/` ist.
      * **Working directory:** Setzen Sie dies auf `<LIBERTY_HOME>/bin`.

Jetzt können Sie Ihren Liberty-Server starten, indem Sie zu `Tools` > `External Tools` gehen und das soeben konfigurierte Tool auswählen.

**4. Konfigurieren von IntelliJ IDEA für Remote-Debugging:**

Um Ihre Anwendung zu debuggen, die auf dem manuell gestarteten Liberty-Server läuft, verwenden Sie die "Remote JVM Debug"-Konfiguration von IntelliJ IDEA.

  * Gehen Sie zu `Run` > `Edit Configurations`.
  * Klicken Sie auf das `+` Symbol und wählen Sie `Remote JVM Debug`.
  * Konfigurieren Sie die Einstellungen:
      * **Name:** Vergeben Sie einen beschreibenden Namen, z.B. "Debug Liberty Server".
      * **Debugger mode:** Wählen Sie `Attach to remote JVM`.
      * **Host:** Geben Sie `localhost` ein (oder die IP-Adresse des Rechners, auf dem Liberty läuft, falls dieser nicht Ihr lokaler Rechner ist).
      * **Port:** Geben Sie die Portnummer ein, die Sie in der `jvm.options`-Datei konfiguriert haben (z.B. `5005`).
      * **Use module classpath of:** Wählen Sie das Modul in Ihrem IntelliJ IDEA-Projekt aus, das Ihren Liberty-Anwendungscode enthält. Dies hilft IntelliJ IDEA, den laufenden Code Ihren Quelldateien für das Debugging zuzuordnen.

**5. Ausführen und Debuggen:**

1.  Starten Sie den Liberty-Server mit der "External Tools"-Konfiguration, die Sie in IntelliJ IDEA erstellt haben.
2.  Warten Sie, bis der Server startet und anzeigt, dass er auf den konfigurierten Port für den Debugger lauscht (Sie sollten eine Meldung in der Server-Konsolenausgabe sehen).
3.  Setzen Sie Breakpoints in Ihrem Anwendungscode innerhalb von IntelliJ IDEA.
4.  Gehen Sie zu `Run` > `Debug` und wählen Sie die "Debug Liberty Server"-Konfiguration aus, die Sie erstellt haben.

IntelliJ IDEA wird versuchen, eine Verbindung zum laufenden Liberty-Server auf dem angegebenen Port herzustellen. Sobald verbunden, können Sie alle Debugging-Funktionen von IntelliJ IDEA nutzen, wie z.B. schrittweises Ausführen von Code, Inspizieren von Variablen und Auswerten von Ausdrücken.

Indem Sie diese Schritte befolgen, können Sie Ihre WebSphere Liberty-Anwendungen effektiv in IntelliJ IDEA ausführen und debuggen, ohne sich auf das dedizierte Liberty Tools Plugin zu verlassen, und behalten die direkte Kontrolle über den Server-Lebenszyklus und den Debugging-Prozess.