---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung von WebSphere-Fehlern beim Hochladen großer EAR-Dateien
translated: true
type: note
---

### Problemverständnis
Der "Multipart File Upload Error" (oft in der Form `org.apache.commons.fileupload.FileUploadException: Processing of multipart/form-data request failed. File too large (errno:27)`) tritt typischerweise auf, wenn eine EAR-Datei im IBM WebSphere Application Server (WAS) über die Administrationskonsole aktualisiert wird. Dies ist bei größeren EAR-Dateien (z. B. >20 MB) üblich und liegt an Grenzwerten für Datei-Uploads, temporären Speicher, Heap-Speicher oder Betriebssystemressourcen. Es handelt sich nicht um ein Problem mit der EAR-Datei selbst, sondern damit, wie die Konsole den HTTP-Multipart-Upload verarbeitet.

### Schnelle Lösungsansätze zuerst
1. **Kopieren Sie die EAR auf den Server und führen Sie das Deployment lokal durch**:
   - Verwenden Sie FTP/SCP, um die neue EAR-Datei in ein Verzeichnis auf dem WAS-Server zu übertragen (z. B. `/opt/IBM/WebSphere/AppServer/installableApps/`).
   - Gehen Sie in der Admin-Konsole zu **Anwendungen > Anwendungstypen > WebSphere Enterprise-Anwendungen**.
   - Wählen Sie Ihre bestehende Anwendung > **Aktualisieren**.
   - Wählen Sie **Einzelnes Modul ersetzen oder hinzufügen** oder **Gesamte Anwendung ersetzen**, dann wählen Sie **Lokales Dateisystem** und zeigen Sie auf den kopierten EAR-Pfad.
   - Dies umgeht den Multipart-Upload über HTTP.

2. **Erhöhen Sie die Dateigrößenlimits des Betriebssystems (UNIX/Linux-Server)**:
   - Der Fehler `errno:27` bedeutet oft, dass die Datei das ulimit für den Prozess überschreitet.
   - Führen Sie `ulimit -f` als WAS-Benutzer aus (z. B. `webadmin`), um das aktuelle Limit zu prüfen.
   - Setzen Sie es auf unbegrenzt: Fügen Sie `ulimit -f unlimited` zum Shell-Profil des Benutzers hinzu (z. B. `~/.bash_profile`) oder zum Startskript des Servers.
   - Starten Sie den Deployment Manager (dmgr) neu und versuchen Sie den Upload erneut.

### Konfigurationsänderungen in WAS
1. **Erhöhen Sie die Heap-Größe für den Deployment Manager**:
   - Große EAR-Dateien können während der Verarbeitung zu OutOfMemory-Fehlern führen.
   - In der Admin-Konsole: **Server > Servertypen > Administratives Server > Deployment Manager**.
   - Unter **Java und Prozessmanagement > Prozessdefinition > Java Virtual Machine**:
     - Setzen Sie **Anfangsgröße des Heapspeichers** auf 1024 (oder höher, z. B. 2048 für sehr große EAR-Dateien).
     - Setzen Sie **Maximale Größe des Heapspeichers** auf 2048 (oder höher).
   - Speichern Sie, starten Sie den dmgr neu und versuchen Sie es erneut.

2. **Passen Sie die HTTP-Sitzungs- oder Post-Größenlimits an (falls zutreffend)**:
   - Für Web-Container-Limits: **Server > Servertypen > WebSphere-Anwendungsserver > [Ihr Server] > Web-Container > HTTP-Transports**.
   - Erhöhen Sie **Maximale Post-Größe** (in Bytes), falls sie niedrig eingestellt ist.
   - Hinweis: Dies wirkt sich indirekt auf die Web-App der Admin-Konsole aus.

### Empfohlene Langzeitlösung: Verwenden Sie wsadmin für Updates
Vermeiden Sie für große oder häufige Updates die Konsole vollständig – sie ist für große Dateien unzuverlässig. Verwenden Sie das wsadmin-Skripting-Tool (Jython oder JACL), um die Anwendung zu aktualisieren.

#### Schritte:
1. Kopieren Sie die neue EAR an einen serverzugänglichen Pfad (z. B. `/tmp/myapp.ear`).
2. Starten Sie wsadmin:  
   ```
   /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -lang jython -user admin -password pass
   ```
3. Führen Sie dieses Jython-Skript aus, um zu aktualisieren:  
   ```python
   AdminApp.update('MyAppName', 'app', [-Map ModulesToApps, '[-MapWebModToVH [[default_host MyContext virtual_host]] ]'], [-Operation update], [-appname MyAppName], [-MapModulesToServers [[MyModule MyServer]]], [-nodefaultoptions], [-preCompileJSPs false], [-contextroot MyContext], [-noTxImport], [-connType SERVER], [ -contenturi /tmp/myapp.ear ])
   AdminConfig.save()
   ```
   - Ersetzen Sie `MyAppName` durch den Namen Ihrer App, `MyContext` durch den Context Root, `MyServer` durch den Zielserver/das Zielcluster und `/tmp/myapp.ear` durch den EAR-Pfad.
4. Synchronisieren Sie die Nodes in einer Cluster-Umgebung: `AdminControl.invoke(AdminControl.completeServers(), 'sync')`.
5. Starten Sie die App neu: **Anwendungen > [App] > Neustart**.

Diese Methode ist schneller, umgeht Upload-Limits und ist für die Automatisierung (z. B. via Jenkins) skriptfähig.

### Zusätzliche Tipps
- **Prüfen Sie die Logs**: Überprüfen Sie `SystemOut.log` und `SystemErr.log` im dmgr-Profil für Details (z. B. `/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/logs/dmgr/`).
- **Testen Sie mit einer kleineren EAR**: Verifizieren Sie, ob das Problem größenbedingt ist, indem Sie eine minimale Version zippen.
- **WAS-Version**: Stellen Sie sicher, dass Sie eine unterstützte Version verwenden (z. B. 8.5, 9.0). Wenden Sie bei Bedarf die neuesten Fixes an.
- Wenn der Fehler bestehen bleibt (z. B. Timeout), erhöhen Sie den HTTP-Timeout in **Umgebung > Web-Anwendungsserver > [Server] > Container-Einstellungen > Web-Container-Einstellungen > Web-Container > Sitzungsverwaltung > Konfiguration > Timeout**.

Wenn keine dieser Lösungen funktioniert, teilen Sie die genaue Fehlermeldung und die WAS-Version für eine maßgeschneidertere Beratung mit.

### Referenzen
- [Error during deploy of war file on Websphere Application Server 7.0](https://coderanch.com/t/459530/application-servers/Error-deploy-war-file-Websphere)
- [OutOfMemory errors while deploying applications in WebSphere Application Server](https://www.ibm.com/support/pages/outofmemory-errors-while-deploying-applications-websphere-application-server)
- [Maximum size limit of an Ear that can be deployed in WAS](https://stackoverflow.com/questions/58748076/maximum-size-limit-of-an-ear-that-can-be-deployed-in-was)
- [Deploying the enterprise archive (EAR) using the WebSphere Administrative Console](https://www.ibm.com/docs/en/configurepricequote/9.5.0?topic=cwaso-deploying-enterprise-archive-ear-using-websphere-admin-console)