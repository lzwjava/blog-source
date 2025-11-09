---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Ersetzungs-EAR in WebSphere bereitstellen
translated: true
type: note
---

### Bereitstellen einer neuen EAR-Datei zum Ersetzen einer bestehenden in IBM WebSphere Application Server (WAS)

Das Ersetzen einer EAR-Datei (Enterprise Archive) in IBM WAS ist eine standardmäßige Bereitstellungsaufgabe, es ist jedoch entscheidend, Best Practices zu befolgen, um Ausfallzeiten, Konfigurationsfehler oder Laufzeitfehler zu vermeiden. Im Folgenden werden die wichtigsten Details beschrieben, die Sie vor, während und nach dem Upload/der Bereitstellung bestätigen und überprüfen sollten. Dies setzt voraus, dass Sie die WAS Administrative Console (oder wsadmin-Skripte für die Automatisierung) verwenden und in einer unterstützten Umgebung arbeiten (z. B. WAS 8.5, 9.x oder Liberty Profile).

#### 1. **Vorbereitungen vor der Bereitstellung (Vor dem Upload bestätigen)**
   - **Sichern der aktuellen Anwendung**:
     - Exportieren Sie die bestehende EAR aus der Console (Anwendungen > Enterprise Applications > [App-Name] > Export) oder sichern Sie die gesamte Konfiguration mit dem Befehl `backupConfig` über wsadmin.
     - Warum? Ermöglicht ein Rollback, falls die neue EAR Probleme verursacht. Bestätigen Sie, dass das Backup abgeschlossen und sicher gespeichert ist.

   - **Kompatibilitätsprüfungen**:
     - Stellen Sie sicher, dass die neue EAR für die korrekte WAS-Version erstellt wurde (z. B. Java-Version, EJB-Spezifikationen wie Jakarta EE vs. Java EE).
     - Prüfen Sie auf veraltete Funktionen in Ihrer WAS-Version (z. B. über IBM Knowledge Center Docs). Führen Sie `wsadmin` mit `AdminConfig.validateAppDeployment` aus, falls möglich.
     - Bestätigen Sie, dass der Bereitstellungsdeskriptor der EAR (application.xml, ibm-application-ext.xmi) mit den Modulen Ihres Servers übereinstimmt (WARs, JARs innerhalb der EAR).

   - **Umgebungs- und Ressourcenabhängigkeiten**:
     - Überprüfen Sie JNDI-Ressourcen: Datenquellen, JMS-Warteschlangen, Umgebungsvariablen. Stellen Sie sicher, dass alle referenzierten Ressourcen (z. B. JDBC-Provider) konfiguriert und fehlerfrei sind. Testen Sie Verbindungen über die Console (Ressourcen > JDBC > Data sources).
     - Sicherheit: Bestätigen Sie, dass Benutzerrollen, Sicherheitseinschränkungen und Zuordnungen (z. B. in ibm-application-bnd.xmi) mit Ihrer Realm übereinstimmen (z. B. LDAP, federated). Prüfen Sie, ob die neue EAR neue benutzerdefinierte Realms oder Zertifikate erfordert.
     - Classloader-Richtlinien: Notieren Sie sich den aktuellen WAR-Classloader-Modus (PARENT_FIRST oder PARENT_LAST) und Shared Library-Referenzen – stellen Sie sicher, dass es keine Konflikte mit der neuen EAR gibt.
     - Clustering/High Availability: Wenn Sie sich in einer geclusterten Umgebung befinden, bestätigen Sie, dass die neue EAR auf allen Knoten identisch ist, und planen Sie Rolling Deployments, um Ausfallzeiten zu minimieren.

   - **Anwendungsspezifische Details**:
     - Context Root und Virtual Hosts: Bestätigen Sie, dass der Context Root nicht mit anderen Apps kollidiert (Anwendungen > [App-Name] > Context Root for Web Modules).
     - Port und Mapping: Überprüfen Sie Servlet-Mappings und URL-Muster.
     - Benutzerdefinierte Eigenschaften: Prüfen Sie auf anwendungsspezifische benutzerdefinierte Eigenschaften, die in der Console gesetzt wurden – diese müssen möglicherweise nach der Bereitstellung erneut angewendet werden.

   - **Testen der neuen EAR**:
     - Bauen und testen Sie die EAR zuerst in einer Staging/Dev-Umgebung. Verwenden Sie Tools wie Rational Application Developer oder Eclipse mit WAS-Plugins zur Validierung.
     - Scannen Sie nach bekannten Problemen: Verwenden Sie IBM's Fix Packs und APARs Suche für Ihre WAS-Version.

#### 2. **Während des Uploads und der Bereitstellung**
   - **Stoppen der aktuellen Anwendung**:
     - In der Console: Anwendungen > Enterprise Applications > [App-Name] > Stop. Bestätigen Sie, dass sie vollständig gestoppt ist (keine aktiven Sitzungen, falls Sitzungsaffinität aktiviert ist).
     - Speichern Sie die Konfiguration und synchronisieren Sie die Knoten in einem Cluster-Setup (System administration > Nodes > Synchronize).

   - **Hochladen der neuen EAR**:
     - Navigieren Sie zu Anwendungen > New Application > New Enterprise Application.
     - Laden Sie die EAR-Datei hoch. Während des Assistenten:
       - Wählen Sie "Replace existing application", wenn Sie dazu aufgefordert werden (oder deinstallieren Sie die alte zuerst über Anwendungen > [App-Name] > Uninstall).
       - Überprüfen Sie die Bereitstellungsoptionen: Module zu Servern, Zielclustern und Shared Libraries zuordnen.
       - Bestätigen Sie Schritt für Schritt im Assistenten: Security Role Bindings, Resource Refs und Vollständigkeit der Metadaten.
     - Bei Verwendung von wsadmin: Skripten mit `AdminApp.update` oder `installInteractive` für Ersetzungen. Beispiel:
       ```
       wsadmin> AdminApp.update('AppName', '[-operation update -contenturi /path/to/new.ear]')
       ```
       Validieren Sie immer mit `AdminConfig.validateAppDeployment` vor dem Anwenden.

   - **Konfigurationssynchronisation**:
     - Speichern Sie nach dem Upload die Master-Konfiguration und synchronisieren Sie sie mit den Deployment Managern/Knoten.
     - Prüfen Sie im Bereitstellungszusammenfassung auf Warnungen/Fehler – beheben Sie eventuelle Modulbindungsprobleme sofort.

   - **Starten der Anwendung**:
     - Starten Sie sie über die Console und bestätigen Sie, dass sie ohne Fehler initialisiert (überwachen Sie SystemOut.log und SystemErr.log im logs-Verzeichnis des Profils).

#### 3. **Verifizierung nach der Bereitstellung**
   - **Logs und Monitoring**:
     - Überwachen Sie die Logs (z. B. `tail -f profile/logs/server1/SystemOut.log`) auf Bereitstellungserfolg, Bindungsfehler oder Startausnahmen.
     - Verwenden Sie die Console's Troubleshooting > Logs and Trace für detaillierte Traces, falls nötig. Bestätigen Sie, dass keine ClassNotFoundExceptions oder NoSuchMethodErrors auftreten.

   - **Funktionale Tests**:
     - Smoke Test: Greifen Sie auf die App über ihre URL zu und verifizieren Sie die Kernfunktionen (z. B. Login, API-Aufrufe).
     - Lasttest bei kritischen Anwendungen – prüfen Sie auf Memory Leaks oder Performance-Regressionen.
     - Datenbank/Externe Integrationen: Führen Sie Abfragen oder Aufrufe durch, um den Datenfluss zu bestätigen.

   - **Rollback-Plan**:
     - Stellen Sie sicher, dass Sie die gesicherte EAR schnell erneut bereitstellen können. Richten Sie Health Checks ein (z. B. über IBM Health Center oder benutzerdefinierte Skripte).

#### Häufige Fallstricke, auf die man achten sollte
- **Sitzungsverwaltung**: Wenn die App HTTPSession verwendet, leiten Sie aktive Sitzungen vor dem Stoppen ab, um Datenverlust zu vermeiden.
- **Dateiberechtigungen**: Stellen Sie sicher, dass die EAR-Datei Leseberechtigungen für den WAS-Benutzer hat (z. B. wasadmin).
- **Größe und Zeit**: Große EARs können lange für die Bereitstellung benötigen – planen Sie dies während Wartungsfenstern ein.
- **Liberty Profile Unterschiede**: Bei Verwendung von WAS Liberty erfolgen Bereitstellungen über server.xml Änderungen oder `install-feature`; bestätigen Sie, dass die XML-Konfigurationen übereinstimmen.
- **Versionsspezifische Hinweise**: Für WAS 9+ prüfen Sie auf MicroProfile oder CDI-Änderungen. Konsultieren Sie immer die IBM Docs für Ihre genaue Version.

Wenn Sie weitere Details angeben (z. B. WAS-Version, Cluster-Setup oder spezifische Fehler, die Sie gesehen haben), kann ich diese Ratschläge verfeinern. Für offizielle Anleitungen lesen Sie das IBM Knowledge Center oder das Support-Portal. Lassen Sie mich wissen, wie ich Ihnen sonst helfen kann!