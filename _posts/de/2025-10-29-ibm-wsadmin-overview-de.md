---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht über das IBM WebSphere wsadmin Tool
translated: true
type: note
---

### Übersicht von wsadmin in IBM WebSphere Application Server (WAS)

Das `wsadmin`-Tool ist eine Skripting-Schnittstelle für die Befehlszeile zur Verwaltung des WebSphere Application Servers. Es ermöglicht die Automatisierung von Aufgaben wie dem Verwalten von Servern, dem Bereitstellen von Anwendungen, dem Konfigurieren von Ressourcen und dem Überwachen von Laufzeitoperationen. Skripte können in Jython (Python-basiert) oder JACL (Tcl-basiert) geschrieben werden, wobei Jython aufgrund seiner Lesbarkeit häufiger verwendet wird.

- **`wsadmin.bat`**: Wird auf Windows-Systemen verwendet.
- **`wsadmin.sh`**: Wird auf Unix/Linux/AIX-Systemen verwendet.

Beide Tools befinden sich im `bin`-Verzeichnis eines WebSphere-Profils (z.B. `<WAS_HOME>/profiles/<ProfileName>/bin/`) oder der Basisinstallation (`<WAS_HOME>/bin/`). Es wird empfohlen, sie aus dem `bin`-Verzeichnis des Profils auszuführen, um die korrekte Umgebung sicherzustellen.

#### wsadmin interaktiv starten
Dies startet eine Shell, in der Sie Befehle direkt eingeben können.

**Syntax:**
```
wsadmin[.bat|.sh] [Optionen]
```

**Einfaches Beispiel (Windows):**
```
cd C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin
wsadmin.bat -lang jython -user admin -password mypass
```

**Einfaches Beispiel (Unix/Linux):**
```
cd /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin
./wsadmin.sh -lang jython -user admin -password mypass
```

- `-lang jython`: Gibt Jython an (verwenden Sie `-lang jacl` für JACL).
- `-user` und `-password`: Erforderlich, wenn die globale Sicherheit aktiviert ist (weglassen, wenn deaktiviert).
- Wenn weggelassen, verbindet es sich mit dem lokalen Server über den standardmäßigen SOAP-Connector auf Port 8879 (oder RMI auf 2809).

Sobald Sie sich in der wsadmin-Eingabeaufforderung befinden (z.B. `wsadmin>`), können Sie Befehle mit Skripting-Objekten ausführen:
- **AdminConfig**: Für Konfigurationsänderungen (z.B. Erstellen von Ressourcen).
- **AdminControl**: Für Laufzeitoperationen (z.B. Starten/Stoppen von Servern).
- **AdminApp**: Für das Bereitstellen/Aktualisieren von Anwendungen.
- **AdminTask**: Für High-Level-Aufgaben (z.B. Synchronisieren von Nodes).
- **Help**: Für eingebaute Hilfe (z.B. `Help.help()`).

**Beispielbefehle in der Shell:**
- Alle Server auflisten: `print AdminConfig.list('Server')`
- Einen Server starten: `AdminControl.invoke(AdminControl.completeObjectName('type=ServerIndex,process=server1,*'), 'start')`
- Änderungen speichern: `AdminConfig.save()`
- Beenden: `quit`

#### Ausführen einer Skriptdatei
Verwenden Sie die Option `-f`, um ein Jython- (.py oder .jy) oder JACL-Skript (.jacl) nicht-interaktiv auszuführen.

**Beispielskript (deployApp.py):**
```python
# Verbinden und eine App bereitstellen
appName = 'MyApp'
AdminApp.install('/path/to/MyApp.ear', '[-appname ' + appName + ']')
AdminConfig.save()
print 'Application ' + appName + ' deployed successfully.'
```

**Ausführung unter Windows:**
```
wsadmin.bat -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

**Ausführung unter Unix/Linux:**
```
./wsadmin.sh -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

#### Ausführen eines einzelnen Befehls
Verwenden Sie die Option `-c` für Einzelbefehle (nützlich in Batch-Dateien oder für die Automatisierung).

**Beispiel (Windows Batch-Datei Ausschnitt):**
```batch
@echo off
call "C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin\wsadmin.bat" -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

**Beispiel (Unix Shell-Skript Ausschnitt):**
```bash
#!/bin/bash
./wsadmin.sh -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

#### Wichtige Optionen

| Option | Beschreibung | Beispiel |
|--------|-------------|---------|
| `-conntype` | Connector-Typ: `SOAP` (Standard, Port 8879) oder `RMI` (Port 2809). | `-conntype RMI` |
| `-host` | Remote-Host, zu dem verbunden werden soll. | `-host myhost.example.com` |
| `-port` | Connector-Port. | `-port 8879` |
| `-tracefile` | Ausgabe in eine Datei protokollieren. | `-tracefile wsadmin.log` |
| `-profile` | Führt ein Profil-Skript vor dem Hauptskript aus. | `-profile init.py` |
| `-c` | Führt einen einzelnen Befehl aus (nicht-interaktiv). | `-c "AdminConfig.save()"` |
| `-f` | Führt eine Skriptdatei aus. | `-f myscript.py` |
| `-job` | Führt einen Job-Manager-Befehl aus. | `-job deploy.xml` |

#### Tipps und Best Practices
- **Sicherheit**: Wenn die globale Sicherheit deaktiviert ist, lassen Sie `-user` und `-password` weg. Für sichere Setups verwenden Sie verschlüsselte Anmeldedaten oder Schlüsseldateien.
- **Thin Client Mode**: Für die Remote-Administration ohne eine vollständige WAS-Installation verwenden Sie `wsadmin -conntype NONE` mit Thin-Client-JARs (z.B. `com.ibm.ws.admin.client_*.jar`).
- **Leistung**: Verwenden Sie für mehrere Befehle ein einzelnes `-f`-Skript anstelle wiederholter `-c`-Aufrufe, um JVM-Overhead zu vermeiden.
- **Fehlerbehandlung**: Rufen Sie nach Konfigurationsänderungen immer `AdminConfig.save()` auf. Verwenden Sie try-except in Jython für Robustheit.
- **Befehle generieren**: Führen Sie in der WAS Admin Console eine Aktion aus und klicken Sie auf "View administrative scripting command for last action", um den entsprechenden wsadmin-Befehl zu erhalten.
- **Versionshinweise**: Das Verhalten ist konsistent über WAS 8.5+ und 9.0+ hinweg, aber überprüfen Sie die IBM-Dokumentation auf versionsspezifische Details (z.B. Jython 2.7 in neueren Versionen).

Für fortgeschrittene Verwendungszwecke erkunden Sie das AdminTask-Objekt für vereinfachte Befehle wie `AdminTask.importFile('path/to/file')`.

### Referenzen
- [wsadmin scripting tool - IBM Docs](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-wsadmin-tool)
- [Getting started with wsadmin scripting - IBM Docs](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.doc/ae/txml_script.html)
- [WAS - wsadmin (Jython) Tutorial](http://www.mtitek.com/tutorials/websphere/wsadmin_jython.php)
- [IBM WebSphere - Getting Started with wsadmin](https://www.freekb.net/Article?id=1563)
- [WSADMIN Tutorial – Part1](https://websphereapplicationservernotes.wordpress.com/2012/12/25/wsadmin-tutorial-part1/)