---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Testen von JDBC-Datenquellen in WebSphere
translated: true
type: note
---

### Testen von JDBC-Datenquellen in der IBM WebSphere Application Server (WAS) Administrationskonsole

In IBM WebSphere Application Server (WAS) können Sie die Funktion "Verbindung testen" in der Integrated Solutions Console (Admin-Konsole) verwenden, um zu überprüfen, ob eine JDBC-Datenquelle korrekt konfiguriert ist und eine Verbindung zur zugrunde liegenden Datenbank herstellen kann. Dies ist nützlich für die Fehlerbehebung bei Konnektivitätsproblemen, ohne eine Anwendung bereitzustellen.

Hier ist eine Schritt-für-Schritt-Anleitung (unter der Annahme, dass Sie WAS Traditional oder Liberty mit der vollständigen Konsole verwenden; die Versionen können leicht variieren, z.B. v8.5, v9.x):

#### Voraussetzungen
- Stellen Sie sicher, dass Sie administrativen Zugriff auf den WAS-Server und die Konsole haben.
- Die Datenquelle muss bereits konfiguriert sein (unter Ressourcen > JDBC > Datenquellen) mit Details wie JNDI-Name, JDBC-Provider, Datenbank-URL, Benutzername, Passwort usw.
- Der Datenbankserver sollte laufen und vom WAS-Server aus erreichbar sein (Firewalls, Netzwerk usw. prüfen).
- Bei Verwendung eines sicheren Setups (z.B. SSL) müssen die Zertifikate konfiguriert sein.

#### Schritte zum Testen der Verbindung

1. **In der Administrationskonsole anmelden**:
   - Öffnen Sie einen Webbrowser und navigieren Sie zur Konsolen-URL: `http://<was-host>:<admin-port>/ibm/console` (Standard-Admin-Port ist 9060 für HTTP oder 9043 für HTTPS; ersetzen Sie dies mit Ihrem tatsächlichen Host und Port).
   - Melden Sie sich mit Ihren Admin-Zugangsdaten an.

2. **Zu JDBC-Datenquellen navigieren**:
   - Erweitern Sie im linken Navigationsbereich **Ressourcen** > **JDBC**.
   - Klicken Sie auf **Datenquellen**.

3. **Den entsprechenden Bereich auswählen**:
   - Die Konsole fordert Sie auf, einen Bereich auszuwählen, falls dieser noch nicht festgelegt ist (z.B. Zelle, Knoten, Server oder Cluster). Wählen Sie den Bereich aus, in dem Ihre Datenquelle definiert ist.
   - Klicken Sie auf **OK** oder **Weiter**, um fortzufahren.

4. **Ihre Datenquelle finden**:
   - Suchen Sie in der Liste der Datenquellen diejenige, die Sie testen möchten, und wählen Sie sie aus (z.B. anhand des JNDI-Namens wie `jdbc/myDataSource`).
   - Wenn sie nicht aufgeführt ist, stellen Sie sicher, dass sie erstellt und gespeichert wurde. Sie können bei Bedarf über **Neu** eine erstellen.

5. **Auf die Funktion "Verbindung testen" zugreifen**:
   - Wählen Sie die Datenquelle aus und klicken Sie auf **Verbindung testen** (diese Schaltfläche befindet sich typischerweise oben auf der Seite mit den Datenquellendetails).
   - Wenn die Schaltfläche ausgegraut oder nicht verfügbar ist:
     - Prüfen Sie, ob die Datenquelle aktiviert ist (suchen Sie nach einer Option "Aktivieren", falls sie deaktiviert ist).
     - Stellen Sie sicher, dass ein JDBC-Provider zugeordnet ist (unter Ressourcen > JDBC > JDBC-Provider).
     - Bei einigen Setups müssen Sie möglicherweise zuerst den Server stoppen/starten oder die Konfiguration speichern.

6. **Den Test ausführen**:
   - Die Konsole versucht, eine Verbindung mit den konfigurierten Einstellungen (URL, Treiber, Anmeldeinformationen usw.) herzustellen.
   - Warten Sie auf das Ergebnis (dies kann je nach Netzwerk-/Datenbankantwort einige Sekunden dauern).
   - **Erfolg**: Sie sehen eine Meldung wie "Testverbindung für Datenquelle <Name> auf Server <ServerName> am Knoten <NodeName> war erfolgreich."
   - **Fehler**: Sie erhalten eine Fehlermeldung mit Details, wie z.B.:
     - Verbindung abgelehnt (Netzwerkproblem).
     - Ungültige Anmeldeinformationen (falscher Benutzername/Passwort).
     - Treiber nicht gefunden (JDBC-Provider fehlerhaft konfiguriert).
     - SQLException-Details von der Datenbank.

7. **Überprüfen und Fehlerbehebung durchführen**:
   - Wenn der Test fehlschlägt, prüfen Sie den Bereich **Meldungen** (oben auf der Seite) der Konsole für weitere Details.
   - Server-Logs einsehen: Gehen Sie zu **Fehlerbehebung** > **Logs und Trace** > Wählen Sie Ihren Server aus > **JVM-Logs** oder **Anwendungslogs** für Stack Traces.
   - Häufige Lösungen:
     - Überprüfen Sie das Format der Datenbank-URL (z.B. `jdbc:oracle:thin:@localhost:1521:orcl` für Oracle).
     - Testen Sie die Anmeldeinformationen manuell mit einem Datenbanktool wie SQL*Plus oder DBeaver.
     - Stellen Sie sicher, dass das JDBC-Treiber-JAR am richtigen Ort bereitgestellt ist (z.B. über den JDBC-Provider).
     - Überprüfen Sie bei Connection Pools die Einstellungen wie minimale/maximale Verbindungen unter **Verbindungspool-Eigenschaften**.

#### Zusätzliche Tipps
- **Sicherheit**: Wenn die Datenquelle container-verwaltete Authentifizierung verwendet, stellen Sie sicher, dass die Anmeldeinformationen unter **Sicherheit** > **Globale Sicherheit** oder über JAAS gesetzt sind.
- **Benutzerdefinierte Eigenschaften**: Überprüfen Sie auf der Datenquellenseite Registerkarten wie **Verbindungspool**, **Container-verwalteter Authentifizierungs-Alias** und **Benutzerdefinierte Eigenschaften** auf Probleme.
- **Mehrere Server/Cluster**: Der Test wird gegen den spezifisch ausgewählten Server/Knoten ausgeführt. Für Cluster testen Sie bei Bedarf auf jedem Mitglied.
- **WAS Liberty Profile**: Bei Verwendung von Liberty ist der Prozess ähnlich, verwendet jedoch die `server.xml`-Datei oder das Liberty Admin Center. Aktivieren Sie das Feature `adminCenter-1.0` und greifen Sie über `http://localhost:9080/adminCenter` zu. Der Test befindet sich unter **Server** > Ihr Server > **Ressourcen** > **Datenquellen**.
- **Automatisierung**: Für Skripting verwenden Sie wsadmin (Jython/Python) Befehle wie `AdminConfig.testConnection(dsId)`, wobei `dsId` die Konfigurations-ID der Datenquelle ist.

Wenn Sie auf eine spezifische Fehlermeldung oder Version von WAS stoßen, geben Sie weitere Details für gezielte Hilfe an! Für offizielle Dokumentationen konsultieren Sie das IBM Knowledge Center für Ihre WAS-Version.