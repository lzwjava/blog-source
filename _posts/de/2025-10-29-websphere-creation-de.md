---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Korrekte Erstellung von WebSphere Application Server
translated: true
type: note
---

Nein, der Befehl `nodeName -name serverName admin create applciation server` (mit dem Tippfehler in "applciation") ist nicht korrekt, um einen Anwendungsserver in IBM WebSphere Application Server (WAS) mittels wsadmin-Scripting zu erstellen.

### Korrekte Syntax
Der richtige Befehl verwendet die Methode `AdminTask.createApplicationServer` in Jython (der empfohlenen Scripting-Sprache für wsadmin). Er benötigt:
- Den **Namen des Knotens** als ersten Argument (ein String).
- Eine **Liste von Optionen** als zweites Argument, inklusive `-name` für den Servernamen.

**Grundlegendes Beispiel:**
```jython
AdminTask.createApplicationServer('IhrKnotenName', ['-name', 'IhrServerName'])
```

- Ersetzen Sie `'IhrKnotenName'` mit dem tatsächlichen Knotennamen (z.B. `ndnode1`).
- Ersetzen Sie `'IhrServerName'` mit dem gewünschten Servernamen (z.B. `appServer1`).
- Optionale Parameter können zur Liste hinzugefügt werden, wie `'-templateName', 'default'` für die Verwendung einer Standard-Servervorlage.

### Schritte zur Ausführung
1. Starten Sie wsadmin im Jython-Modus: `./wsadmin.sh -lang jython -user admin -password pass`.
2. Führen Sie den obigen Befehl aus.
3. Speichern Sie die Konfiguration: `AdminConfig.save()`.
4. Beenden: `quit`.

Dies erstellt einen grundlegenden Anwendungsserver auf dem angegebenen Knoten. Für weitere Optionen (z.B. Ports, JVM-Einstellungen) konsultieren Sie bitte die vollständige AdminTask-Dokumentation.

[ServerManagement-Befehlsgruppe für das AdminTask-Objekt](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-servermanagement-command-group-admintask-object)  
[Erstellen eines Servers mit Scripting](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-creating-server-using)