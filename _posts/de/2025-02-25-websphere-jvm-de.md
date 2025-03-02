---
audio: true
generated: true
lang: de
layout: post
title: JVM-Optionen im WebSphere Liberty Server
translated: true
---

Um die JVM-Optionen zu überprüfen, die in der Datei `jvm.options` festgelegt sind, die sich im Serververzeichnis eines WebSphere Liberty Profile (WLP) Servers befindet, können Sie den `jinfo`-Befehl verwenden, der vom Java Development Kit (JDK) bereitgestellt wird. Diese Methode ermöglicht es Ihnen, die angewendeten Optionen eines laufenden Servers effizient zu überprüfen. Hier ist eine Schritt-für-Schritt-Anleitung, um dies zu erreichen:

### Schritte zum Überprüfen der JVM-Optionen

1. **Verstehen des Kontexts**
   Die `jvm.options`-Datei im Serververzeichnis (typischerweise `<WLP_HOME>/usr/servers/<serverName>/jvm.options`) wird verwendet, um JVM-Argumente wie die Heap-Größe (z.B. `-Xmx`), Garbage Collection-Einstellungen (z.B. `-XX:+UseG1GC`) oder Systemeigenschaften (z.B. `-Dmy.property=value`) festzulegen, die angewendet werden, wenn der Liberty-Server startet.

2. **Starten des Servers**
   Beginnen Sie damit, Ihren Liberty-Server im Hintergrund zu starten, indem Sie den folgenden Befehl verwenden:
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```
   Ersetzen Sie `<WLP_HOME>` durch den Pfad zu Ihrer WebSphere Liberty-Installation und `<serverName>` durch den Namen Ihres Servers. Dieser Befehl startet den Server als Hintergrundprozess.

3. **Lokalisieren der Prozess-ID (PID)**
   Nach dem Starten des Servers benötigen Sie die Prozess-ID des laufenden Java-Prozesses. Liberty speichert diese in einer `.pid`-Datei, die sich befindet unter:
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```
   Öffnen Sie diese Datei (z.B. mit `cat` auf Unix-ähnlichen Systemen oder einem Texteditor), um die PID zu erhalten, die einen numerischen Wert darstellt, der den Prozess des Servers repräsentiert.

4. **Überprüfen der JVM-Flags**
   Verwenden Sie den `jinfo`-Befehl, um die JVM-Flags zu überprüfen, die auf den laufenden Server angewendet werden. Führen Sie aus:
   ```
   jinfo -flags <pid>
   ```
   Ersetzen Sie `<pid>` durch die Prozess-ID, die Sie aus der `.pid`-Datei erhalten haben. Dieser Befehl gibt die Befehlszeilen-Flags aus, die an die JVM übergeben wurden, wie z.B. `-Xmx1024m` oder `-XX:+PrintGCDetails`. Durchsuchen Sie die Ausgabe, um sicherzustellen, dass die Flags, die Sie in `jvm.options` festgelegt haben, vorhanden sind.

5. **Überprüfen der Systemeigenschaften**
   Wenn Ihre `jvm.options`-Datei Systemeigenschaften enthält (z.B. `-Dmy.property=value`), überprüfen Sie diese separat mit:
   ```
   jinfo -sysprops <pid>
   ```
   Dies zeigt alle Systemeigenschaften an, die für die JVM festgelegt wurden. Suchen Sie in der Ausgabe nach den spezifischen Eigenschaften, die Sie definiert haben, um sicherzustellen, dass sie korrekt angewendet wurden.

### Voraussetzungen
- **JDK installiert**: Der `jinfo`-Befehl ist Teil des JDK, nicht der JRE. Stellen Sie sicher, dass ein JDK installiert ist und dass das `jinfo`-Programm sich im Systempfad befindet.
- **Berechtigungen**: Führen Sie `jinfo` mit demselben Benutzer aus, der den Server gestartet hat, oder mit ausreichenden Berechtigungen, um sich an den Prozess anzuhängen.

### Alternative Methoden
Wenn `jinfo` nicht verfügbar ist oder Sie eine andere Vorgehensweise bevorzugen, gibt es zwei zusätzliche Optionen:

- **Verwenden von `server dump`**:
  1. Starten Sie den Server mit `server start <serverName>`.
  2. Generieren Sie einen Server-Dump mit:
     ```
     <WLP_HOME>/bin/server dump <serverName>
     ```
  3. Suchen Sie die generierte `.zip`-Datei in `<WLP_HOME>/usr/servers/<serverName>/`, entpacken Sie sie und öffnen Sie die Datei `javacore.<timestamp>.txt`.
  4. Suchen Sie nach dem Abschnitt "CMDLINE", um die vollständige Java-Befehlszeile einschließlich der JVM-Flags und den Abschnitt "System Properties" für die Systemeigenschaften zu sehen.

- **Verfolgen des Startskripts** (Unix-ähnliche Systeme):
  1. Führen Sie das Server-Skript mit aktivierter Verfolgung aus:
     ```
     sh -x <WLP_HOME>/bin/server start <serverName>
     ```
  2. Überprüfen Sie die Ausgabe, um den Java-Befehl zu finden, der vom Skript ausgeführt wird, einschließlich aller Optionen aus `jvm.options`.

### Hinweise
- **Server läuft nicht**: Wenn der Server aufgrund ungültiger Optionen nicht startet, verwenden Sie `server run <serverName>`, um ihn im Vordergrund auszuführen und die Konsolenausgabe auf Fehler zu überprüfen, oder verwenden Sie die Skriptverfolgung, um den Befehl zu sehen.
- **Protokolldateien**: Die `console.log`-Datei in `<WLP_HOME>/usr/servers/<serverName>/logs/` kann einige Startinformationen enthalten, listet jedoch nicht zuverlässig alle JVM-Optionen auf, es sei denn, das ausführliche Protokollieren ist aktiviert (z.B. `-XX:+PrintFlagsFinal`).

### Fazit
Die `jinfo`-Methode ist die einfachste Möglichkeit, die in `jvm.options` festgelegten JVM-Optionen für einen laufenden Liberty-Server zu überprüfen. Durch die oben genannten Schritte können Sie bestätigen, dass sowohl JVM-Flags als auch Systemeigenschaften wie beabsichtigt angewendet werden.

---

Der `jinfo`-Befehl meldete, dass er sich nicht an den Prozess anhängen konnte.

Zusätzlich konnte die Datei `javacore.<timestamp>.txt` nach Verwendung des Dump-Befehls nicht gefunden werden.

Die Version des WebSphere Liberty Servers ist 24.0.0.9.

---

### Behebung von Problemen beim Überprüfen von JVM-Optionen in WebSphere Liberty 24.0.0.9

Sie haben Probleme beim Verwenden des `jinfo`-Befehls, um JVM-Optionen in Ihrem WebSphere Liberty Profile (WLP) Server der Version 24.0.0.9 zu überprüfen, mit einer Fehlermeldung, dass er "sich nicht an den Prozess anhängen konnte." Zusätzlich konnten Sie die Datei `javacore.<timestamp>.txt` nach der Generierung eines Server-Dumps nicht im erwarteten Verzeichnis (`<WLP_HOME>/usr/servers/<serverName>/`) innerhalb der entpackten `.zip`-Datei finden. Hier ist eine detaillierte Anleitung zur Fehlerbehebung und Behebung dieser Probleme, um sicherzustellen, dass Sie die in Ihrer `jvm.options`-Datei festgelegten JVM-Optionen überprüfen können.

---

### Verständnis des Problems

- **`jinfo`-Fehler**: Die Fehlermeldung "konnte sich nicht an den Prozess anhängen" deutet darauf hin, dass `jinfo` sich nicht mit der laufenden Java Virtual Machine (JVM) verbinden kann. Dies ist oft auf Berechtigungsprobleme (z.B. Ausführen des Befehls als ein anderer Benutzer als der, der den Server gestartet hat) oder Einschränkungen des JVM-Prozesses zurückzuführen.
- **Fehlende `javacore.<timestamp>.txt`**: Der Server-Dump-Prozess sollte eine `.zip`-Datei mit Diagnosedateien, einschließlich `javacore.<timestamp>.txt`, erzeugen, aber deren Fehlen deutet darauf hin, dass entweder der Dump fehlgeschlagen ist, die Datei sich an einem unerwarteten Ort befindet oder die erwarteten Inhalte nicht erzeugt wurden.

Da Sie WebSphere Liberty 24.0.0.9 auf einem Unix-ähnlichen System (basierend auf typischen Dateipfaden) verwenden, werden die Lösungen entsprechend angepasst.

---

### Schritt-für-Schritt-Lösungen

Hier sind mehrere Methoden, um Ihre JVM-Optionen abzurufen, beginnend mit den einfachsten Alternativen zu `jinfo` und der Behebung des Server-Dump-Problems.

#### 1. Überprüfen Sie, ob der Server läuft
Bevor Sie fortfahren, stellen Sie sicher, dass Ihr Liberty-Server aktiv ist:

- **Befehl**:
  ```bash
  <WLP_HOME>/bin/server status <serverName>
  ```
- **Erwartete Ausgabe**:
  Wenn er läuft, sehen Sie eine Meldung wie "Server <serverName> läuft mit der Prozess-ID <pid>." Wenn nicht, starten Sie ihn:
  ```bash
  <WLP_HOME>/bin/server start <serverName>
  ```

- **Lokalisieren der PID**:
  Finden Sie die Prozess-ID in `<WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid` mit:
  ```bash
  cat <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
  ```
  Notieren Sie sich diese PID für spätere Schritte.

#### 2. Verwenden Sie `jps -v` als Alternative zu `jinfo`
Der `jps`-Befehl (Teil des JDK) listet Java-Prozesse und deren Optionen auf und umgeht oft die Anhangsprobleme, die `jinfo` begegnet.

- **Befehl**:
  ```bash
  jps -v
  ```
- **Ausgabe**:
  Eine Liste von Java-Prozessen, z.B.:
  ```
  12345 Liberty -Xmx1024m -XX:+UseG1GC -Dmy.property=value
  ```
- **Aktion**:
  Identifizieren Sie Ihren Liberty-Server-Prozess, indem Sie die PID aus der `.pid`-Datei oder nach "Liberty" oder Ihrem `<serverName>` in der Befehlszeile suchen. Die aufgelisteten Optionen (z.B. `-Xmx1024m`, `-Dmy.property=value`) enthalten diejenigen aus `jvm.options`.

- **Berechtigungsprüfung**:
  Wenn `jps -v` fehlschlägt oder keine Ausgabe zeigt, führen Sie es als denselben Benutzer aus, der den Server gestartet hat (z.B. `sudo -u <serverUser> jps -v`) oder mit `sudo`:
  ```bash
  sudo jps -v
  ```

#### 3. Verwenden Sie `jcmd` für detaillierte JVM-Informationen
Wenn `jps -v` nicht ausreicht, kann `jcmd` (ein weiteres JDK-Tool) einen laufenden JVM abfragen, ohne einige der Anhangsbeschränkungen von `jinfo`.

- **Befehle**:
  - Für JVM-Optionen:
    ```bash
    jcmd <pid> VM.command_line
    ```
    Ausgabe: Die vollständige Befehlszeile, z.B. `java -Xmx1024m -XX:+UseG1GC -Dmy.property=value ...`
  - Für Systemeigenschaften:
    ```bash
    jcmd <pid> VM.system_properties
    ```
    Ausgabe: Eine Liste von Eigenschaften, z.B. `my.property=value`.

- **Aktion**:
  Ersetzen Sie `<pid>` durch die PID Ihres Servers. Stellen Sie sicher, dass Sie diese Befehle mit den entsprechenden Berechtigungen ausführen (z.B. `sudo jcmd <pid> ...` wenn nötig).

#### 4. Generieren und überprüfen Sie eine Javacore-Datei
Da der Server-Dump keine erwartete `javacore.<timestamp>.txt`-Datei erzeugt, versuchen Sie, eine eigenständige Javacore-Datei zu generieren:

- **Befehl**:
  ```bash
  <WLP_HOME>/bin/server javadump <serverName>
  ```
- **Erwartete Ausgabe**:
  Eine Meldung, die den Speicherort der Javacore-Datei angibt, typischerweise `<WLP_HOME>/usr/servers/<serverName>/javacore.<timestamp>.txt`.

- **Aktion**:
  - Überprüfen Sie das Verzeichnis:
    ```bash
    ls <WLP_HOME>/usr/servers/<serverName>/javacore.*.txt
    ```
  - Öffnen Sie die Datei und suchen Sie nach:
    - **CMDLINE**: Listet JVM-Optionen (z.B. `-Xmx1024m`).
    - **Systemeigenschaften**: Listet `-D`-Eigenschaften.

- **Fehlerbehebung**:
  Wenn keine Datei erscheint, überprüfen Sie die Serverprotokolle `console.log` oder `messages.log` in `<WLP_HOME>/usr/servers/<serverName>/logs/` auf Fehler während der Befehlsausführung.

#### 5. Überprüfen Sie die Server-Dump-Methode erneut
Stellen Sie sicher, dass der vollständige Server-Dump korrekt funktioniert:

- **Befehl**:
  ```bash
  <WLP_HOME>/bin/server dump <serverName>
  ```
- **Erwartete Ausgabe**:
  Eine `.zip`-Datei wie `<serverName>.dump-<timestamp>.zip` in `<WLP_HOME>/usr/servers/<serverName>/`.

- **Aktion**:
  - Überprüfen Sie, ob die Datei existiert:
    ```bash
    ls <WLP_HOME>/usr/servers/<serverName>/*.zip
    ```
  - Entpacken Sie sie:
    ```bash
    unzip <serverName>.dump-<timestamp>.zip -d temp_dir
    ```
  - Suchen Sie nach `javacore.<timestamp>.txt`:
    ```bash
    find temp_dir -name "javacore.*.txt"
    ```
  - Öffnen Sie die Datei und überprüfen Sie die Abschnitte "CMDLINE" und "Systemeigenschaften".

- **Fehlerbehebung**:
  - Überprüfen Sie die Konsolenausgabe des Befehls auf Fehler.
  - Stellen Sie sicher, dass der Server während des Dumps lief (obwohl `server dump` auch auf einem gestoppten Server funktionieren kann, benötigt die Javacore einen laufenden JVM).
  - Wenn die `.zip`-Datei fehlt, überprüfen Sie die Protokolle in `<WLP_HOME>/usr/servers/<serverName>/logs/` auf Hinweise.

#### 6. Aktivieren Sie die ausführliche JVM-Ausgabe (letzter Ausweg)
Wenn alles andere fehlschlägt, ändern Sie `jvm.options`, um alle JVM-Flags zu protokollieren:

- **Bearbeiten Sie `<WLP_HOME>/usr/servers/<serverName>/jvm.options`**:
  Fügen Sie hinzu:
  ```
  -XX:+PrintFlagsFinal
  ```
- **Starten Sie den Server neu**:
  ```bash
  <WLP_HOME>/bin/server stop <serverName>
  <WLP_HOME>/bin/server start <serverName>
  ```
- **Überprüfen Sie die Protokolle**:
  Öffnen Sie `<WLP_HOME>/usr/servers/<serverName>/logs/console.log` und suchen Sie nach einer Tabelle der JVM-Flags, z.B.:
  ```
  [uintx] MaxHeapSize = 1073741824 {product}
  ```

---

### Zusätzliche Hinweise

- **Berechtigungen**:
  Der `jinfo`-Fehler deutet auf eine Berechtigungskonflikt hin. Verwenden Sie konsistent denselben Benutzer, der den Server gestartet hat (z.B. über `sudo -u <serverUser>` oder durch Anmelden als dieser Benutzer) für alle Befehle.
- **WebSphere Liberty 24.0.0.9**:
  Das Dump-Verhalten sollte mit dem dokumentierten Prozess übereinstimmen (`.zip` in `<WLP_HOME>/usr/servers/<serverName>/` enthaltend `javacore.<timestamp>.txt`). Wenn es abweicht, überprüfen Sie die IBM-Dokumentation auf versionsspezifische Änderungen, obwohl die `server javadump`-Methode zuverlässig bleibt.
- **JDK-Anforderung**:
  Stellen Sie sicher, dass Ihr JDK (nicht nur JRE) installiert ist, da `jps`, `jcmd` und `jinfo` JDK-Tools sind.

---

### Empfohlene Vorgehensweise

1. **Versuchen Sie `jps -v` zuerst**: Es ist schnell und kann Anhangsprobleme umgehen.
2. **Fallen Sie auf `jcmd` zurück**: Bietet detaillierte Ausgabe, wenn `jps` nicht ausreicht.
3. **Verwenden Sie `server javadump`**: Generiert eine Javacore direkt, umgeht die Komplexität des vollständigen Dumps.
4. **Debuggen Sie den Dump**: Führen Sie `server dump` erneut aus und überprüfen Sie die Inhalte der `.zip`-Datei, wenn nötig.

Durch die oben genannten Schritte sollten Sie erfolgreich Ihre JVM-Optionen abrufen und die Probleme mit `jinfo` und der fehlenden Javacore-Datei beheben. Lassen Sie mich wissen, wenn Sie auf spezifische Fehler stoßen!