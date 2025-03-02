---
audio: false
generated: false
lang: de
layout: post
title: Prozess-ID (PID) des laufenden Servers
translated: true
---

Da Sie WebSphere Liberty Profile (WLP) Version 24.0.0.9 verwenden und die Prozess-ID (PID) des laufenden Servers finden müssen, aber angegeben haben, dass die erwartete `.pid`-Datei unter `<WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid` nicht verfügbar ist, hier ist, wie Sie die PID mit alternativen Methoden finden können.

Der Standardansatz, der in den Anweisungen beschrieben ist, basiert darauf, dass Liberty die PID in einer `.pid`-Datei speichert, nachdem der Server gestartet wurde. Wenn diese Datei jedoch fehlt – möglicherweise aufgrund einer Konfigurationsprobleme, eines fehlgeschlagenen Startvorgangs oder einer anderen Installationskonfiguration – können Sie die PID dennoch mit Systemtools identifizieren, vorausgesetzt, der Server läuft. Hier sind zuverlässige Schritte, um die PID auf einem Unix-ähnlichen System (z. B. Linux) zu finden. Wenn Sie Windows verwenden, lassen Sie es mich wissen, und ich kann die Anweisungen entsprechend anpassen.

### Schritt 1: Bestätigen Sie, dass der Server läuft
Bevor Sie nach der PID suchen, stellen Sie sicher, dass der Liberty-Server aktiv ist. Sie können:
- **Protokolle überprüfen**: Schauen Sie in `<WLP_HOME>/usr/servers/<serverName>/logs/console.log` oder `messages.log` nach Startnachrichten, wie z. B. "Server <serverName> gestartet."
- **Server zugreifen**: Wenn er eine Webanwendung hostet, versuchen Sie, darauf über einen Browser zuzugreifen (z. B. `http://localhost:<port>`).

Wenn der Server nicht läuft, gibt es keine PID zu finden, daher ist dieser Schritt entscheidend.

### Schritt 2: Verwenden Sie Systembefehle, um die PID zu finden
Da die `.pid`-Datei nicht verfügbar ist, können Sie Befehlszeilentools verwenden, um den Java-Prozess zu finden, der dem Liberty-Server zugeordnet ist. Liberty läuft als Java-Prozess, sodass Tools, die Java- oder Netzwerkprozesse auflisten, helfen können. Hier sind zwei effektive Methoden:

#### Methode 1: Verwenden von `ps`, um Java-Prozesse aufzulisten
Der `ps`-Befehl zeigt laufende Prozesse an. Um Java-Prozesse zu filtern, einschließlich des Liberty-Servers, führen Sie aus:
```bash
ps -ef | grep java
```
Dies listet alle Prozesse mit "java" in ihrer Befehlszeile auf. Die Ausgabe könnte so aussehen:
```
user  12345  1  0  10:00 ?  00:00:00 /path/to/java -jar /path/to/liberty/wlp/bin/tools/ws-server.jar <serverName>
```
- Die zweite Spalte (z. B. `12345`) ist die PID.
- Suchen Sie nach einer Zeile, die "liberty", "wlp" oder Ihren `<serverName>` (z. B. `defaultServer`) erwähnt, um den richtigen Prozess zu identifizieren.

Um dies weiter einzuschränken, versuchen Sie, wenn Sie den Servernamen kennen:
```bash
ps -ef | grep <serverName>
```

#### Methode 2: Verwenden von `jps` (Java-spezifisches Tool)
Wenn Sie das Java Development Kit (JDK) installiert haben, ist der `jps`-Befehl eine einfachere Möglichkeit, Java-Prozesse aufzulisten. Führen Sie aus:
```bash
jps -l
```
Die Ausgabe könnte so aussehen:
```
12345 com.ibm.ws.kernel.boot.Launcher
```
- Die erste Spalte (z. B. `12345`) ist die PID.
- Suchen Sie nach einem Klassenname, der mit Liberty in Verbindung steht, wie z. B. `com.ibm.ws.kernel.boot.Launcher`, der häufig mit dem Start von Liberty verbunden ist.

Diese Methode ist oft sauberer als `ps`, da sie nur Java-Prozesse anzeigt.

### Schritt 3: Optional - Verwenden Sie die Portnummer (falls bekannt)
Wenn Sie die Portnummer kennen, auf der der Liberty-Server hört (z. B. aus `server.xml` oder Protokollen), können Sie `netstat` verwenden, um die PID zu finden:
```bash
netstat -anp | grep <port_number>
```
Die Ausgabe könnte enthalten:
```
tcp  0  0  0.0.0.0:<port_number>  0.0.0.0:*  LISTEN  12345/java
```
- Die PID (z. B. `12345`) erscheint nach den Portdetails.

### Empfehlung
- **Bevorzugte Methode**: Verwenden Sie `jps -l`, wenn das JDK verfügbar ist, da es für Java-Prozesse ausgelegt ist und den Liberty-Server wahrscheinlich klar identifiziert.
- **Fallback**: Verwenden Sie `ps -ef | grep java`, wenn `jps` keine Option ist, und identifizieren Sie den Liberty-Prozess manuell, indem Sie die Befehlsdetails überprüfen.

### Fehlerbehebungstipps
Wenn keiner der Befehle den Liberty-Prozess findet:
- Überprüfen Sie erneut, ob der Server läuft (Schritt 1).
- Überprüfen Sie Ihre `<WLP_HOME>` und `<serverName>` Pfade; der Prozess könnte auf ein unerwartetes Verzeichnis verweisen.
- Starten Sie den Server mit `server start <serverName>` neu und überprüfen Sie, ob die `.pid`-Datei erscheint, oder sehen Sie sich die Startprotokolle nach Hinweisen darauf an, warum sie fehlt.

Mit diesen Schritten sollten Sie in der Lage sein, die PID Ihres laufenden Liberty 24.0.0.9-Servers trotz der fehlenden `.pid`-Datei zu finden. Lassen Sie mich wissen, wenn Sie weitere Hilfe benötigen!