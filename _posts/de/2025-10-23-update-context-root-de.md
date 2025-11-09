---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Aktualisierung des WebSphere-Kontextstamms
translated: true
type: note
---

### Aktualisieren des Web Context Root in IBM WebSphere Application Server (WAS)

Der Web Context Root definiert den Basis-URL-Pfad für Ihre Webanwendung (z. B. `/myapp`). In IBM WebSphere Application Server können Sie ihn entweder während der Erstbereitstellung oder für eine bestehende Anwendung über die Administrationskonsole aktualisieren. Nachfolgend sind die Schritte für eine bestehende Anwendung aufgeführt. Stellen Sie sicher, dass Sie administrativen Zugriff auf die WAS-Konsole haben.

#### Voraussetzungen
- Zugriff auf die WebSphere Administrationskonsole (typischerweise unter `https://your-server:9043/ibm/console`).
- Die Anwendung muss installiert und gestoppt sein (empfohlen), bevor Änderungen vorgenommen werden, um Konflikte zu vermeiden.

#### Schritte zum Aktualisieren des Context Root
1. **In der Administrationskonsole anmelden**:
   - Öffnen Sie einen Webbrowser und navigieren Sie zur WAS-Konsolen-URL.
   - Geben Sie Ihre Admin-Anmeldedaten ein.

2. **Zur Anwendung navigieren**:
   - Erweitern Sie im linken Navigationsbereich **Anwendungen** > **Anwendungstypen** > **WebSphere Enterprise-Anwendungen**.
   - Suchen und wählen Sie Ihre bereitgestellte Anwendung aus der Liste aus.

3. **Auf Context Root-Einstellungen zugreifen**:
   - Scrollen Sie auf der Seite mit den Anwendungsdetails zum Abschnitt **Web Module Properties**.
   - Klicken Sie auf **Context root for web modules**.

4. **Den Context Root bearbeiten**:
   - Suchen Sie in der angezeigten Tabelle das Web-Modul (z. B. Ihren WAR-Dateinamen).
   - Aktualisieren Sie das Feld **Context root** mit dem neuen Wert (z. B. Ändern von `/oldapp` zu `/newapp`). Vermeiden Sie führende Schrägstriche, wenn sie nicht benötigt werden, aber verwenden Sie sie für Pfade wie `/myapp`.
   - Klicken Sie auf **OK**, um die Änderungen zu speichern.

5. **Konfiguration speichern und synchronisieren**:
   - Klicken Sie in der Konsole auf **Speichern** (oder **Save directly to the master configuration**, wenn dazu aufgefordert).
   - Wenn Sie sich in einer Cluster- oder Netzwerkbereitstellungsumgebung befinden:
     - Gehen Sie zu **Systemverwaltung** > **Knoten**.
     - Wählen Sie alle relevanten Knoten aus und klicken Sie auf **Full Resynchronize**.

6. **Die Anwendung neu starten**:
   - Kehren Sie zu **Anwendungen** > **WebSphere Enterprise-Anwendungen** zurück.
   - Wählen Sie Ihre Anwendung aus und klicken Sie auf **Stop**, dann auf **Start**.
   - Alternativ können Sie den gesamten Server über **Server** > **Servertypen** > **WebSphere Application-Server** > Server auswählen > **Restart** neu starten.

7. **Die Änderung überprüfen**:
   - Rufen Sie die Anwendungs-URL in einem Browser auf (z. B. `http://your-server:9080/newapp`).
   - Überprüfen Sie die Server-Logs (z. B. `SystemOut.log`) auf Fehler im Zusammenhang mit der Bereitstellung.

#### Zusätzliche Hinweise
- **Während der Erstbereitstellung**: Wenn Sie eine neue Anwendung bereitstellen, geben Sie den Context Root im Schritt **Select installation options** unter **Context root** für jedes Web-Modul an.
- **EAR-Dateien**: Für Anwendungen, die in einer EAR gebündelt sind, stellen Sie sicher, dass die `application.xml` den Context Root nicht fest codiert; Überschreibungen in der Konsole haben Vorrang.
- **Häufige Probleme**:
  - Änderungen werden möglicherweise nicht übernommen, wenn die Anwendung läuft – stoppen Sie sie immer zuerst.
  - In WebSphere Liberty oder Open Liberty verwenden Sie stattdessen `server.xml`-Konfigurationen.
  - Für virtuelle Hosts oder Plugins aktualisieren Sie die Web-Server-Plugin-Konfiguration nach den Änderungen.
- Wenn die Anwendung Sicherheit oder Shared Libraries verwendet, testen Sie sie nach der Aktualisierung gründlich.

Weitere Details finden Sie in der offiziellen IBM-Dokumentation oder in Community-Guides.

#### Referenzen
- [Context root for web modules settings](https://www.ibm.com/docs/SSEQTP_9.0.5/com.ibm.websphere.base.doc/ae/uweb_contextroot.html)
- [IBM WebSphere - Context root of an application](https://www.freekb.net/Article?id=1647)
- [WebSphere 8.5 context root change not applying to WAR file](https://stackoverflow.com/questions/24472790/websphere-8-5-context-root-change-not-applying-to-war-file)