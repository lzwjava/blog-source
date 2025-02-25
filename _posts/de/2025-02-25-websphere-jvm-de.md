---
audio: true
lang: de
layout: post
title: JVM-Optionen im WebSphere Liberty Server
translated: true
---

Um die JVM-Optionen zu überprüfen, die in der Datei `jvm.options` im Serververzeichnis eines WebSphere Liberty Profile (WLP)-Servers festgelegt sind, können Sie den `jinfo`-Befehl verwenden, der vom Java Development Kit (JDK) bereitgestellt wird. Diese Methode ermöglicht es Ihnen, die auf einen laufenden Server angewendeten Optionen effizient zu überprüfen. Hier ist eine Schritt-für-Schritt-Anleitung, um dies zu erreichen:

### Schritte zum Überprüfen der JVM-Optionen

1. **Kontext verstehen**
   Die Datei `jvm.options` im Serververzeichnis (typischerweise `<WLP_HOME>/usr/servers/<serverName>/jvm.options`) wird verwendet, um JVM-Argumente wie Heap-Größe (z. B. `-Xmx`), Garbage Collection-Einstellungen (z. B. `-XX:+UseG1GC`) oder Systemeigenschaften (z. B. `-Dmy.property=value`) festzulegen, die angewendet werden, wenn der Liberty-Server startet.

2. **Server starten**
   Beginnen Sie damit, Ihren Liberty-Server im Hintergrund zu starten, indem Sie den folgenden Befehl verwenden:
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```
   Ersetzen Sie `<WLP_HOME>` durch den Pfad zu Ihrer WebSphere Liberty-Installation und `<serverName>` durch den Namen Ihres Servers. Dieser Befehl startet den Server als Hintergrundprozess.

3. **Prozess-ID (PID) ermitteln**
   Nachdem der Server gestartet wurde, benötigen Sie die Prozess-ID des laufenden Java-Prozesses. Liberty speichert diese bequemerweise in einer `.pid`-Datei, die sich befindet unter:
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```
   Öffnen Sie diese Datei (z. B. mit `cat` auf Unix-ähnlichen Systemen oder einem Texteditor), um die PID zu erhalten, die ein numerischer Wert ist, der den Serverprozess darstellt.

4. **JVM-Flags überprüfen**
   Verwenden Sie den `jinfo`-Befehl, um die auf den laufenden Server angewendeten JVM-Flags zu inspizieren. Führen Sie aus:
   ```
   jinfo -flags <pid>
   ```
   Ersetzen Sie `<pid>` durch die Prozess-ID, die Sie aus der `.pid`-Datei erhalten haben. Dieser Befehl gibt die Befehlszeilen-Flags aus, die an die JVM übergeben wurden, wie z. B. `-Xmx1024m` oder `-XX:+PrintGCDetails`. Durchsuchen Sie die Ausgabe, um sicherzustellen, dass die Flags, die Sie in `jvm.options` festgelegt haben, vorhanden sind.

5. **Systemeigenschaften überprüfen**
   Wenn Ihre `jvm.options`-Datei Systemeigenschaften enthält (z. B. `-Dmy.property=value`), überprüfen Sie diese separat mit:
   ```
   jinfo -sysprops <pid>
   ```
   Dies zeigt alle für die JVM festgelegten Systemeigenschaften an. Suchen Sie in der Ausgabe nach den spezifischen Eigenschaften, die Sie definiert haben, um sicherzustellen, dass sie korrekt angewendet wurden.

### Voraussetzungen
- **JDK installiert**: Der `jinfo`-Befehl ist Teil des JDK, nicht des JRE. Stellen Sie sicher, dass ein JDK installiert ist und dass das `jinfo`-Programm sich im Pfad Ihres Systems befindet.
- **Berechtigungen**: Führen Sie `jinfo` mit demselben Benutzer aus, der den Server gestartet hat, oder mit ausreichenden Berechtigungen, um sich an den Prozess anzuhängen.

### Alternative Methoden
Wenn `jinfo` nicht verfügbar ist oder Sie eine andere Vorgehensweise bevorzugen, gibt es zwei zusätzliche Optionen:

- **Verwendung von `server dump`**:
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
- **Server läuft nicht**: Wenn der Server aufgrund ungültiger Optionen nicht startet, verwenden Sie `server run <serverName>`, um ihn im Vordergrund auszuführen und die Konsolenausgabe auf Fehler zu überprüfen, oder verwenden Sie die Skriptverfolgungsmethode, um den Befehl zu sehen.
- **Protokolldateien**: Die Datei `console.log` in `<WLP_HOME>/usr/servers/<serverName>/logs/` kann einige Startinformationen enthalten, listet aber nicht zuverlässig alle JVM-Optionen auf, es sei denn, das ausführliche Protokollieren ist aktiviert (z. B. `-XX:+PrintFlagsFinal`).

### Fazit
Die `jinfo`-Methode ist die einfachste Möglichkeit, die in `jvm.options` festgelegten JVM-Optionen für einen laufenden Liberty-Server zu überprüfen. Durch die obigen Schritte können Sie bestätigen, dass sowohl JVM-Flags als auch Systemeigenschaften wie beabsichtigt angewendet werden.

---

Der `jinfo`-Befehl meldete, dass er sich nicht an den Prozess anhängen konnte.

Zusätzlich konnte die Datei `javacore.<timestamp>.txt` nach Verwendung des Dump-Befehls nicht gefunden werden.

Die Version des WebSphere Liberty Servers ist 24.0.0.9.