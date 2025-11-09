---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Kibana Einrichtung Für PCF Logs
translated: true
type: note
---

Es sieht so aus, als ob "kabana" höchstwahrscheinlich eine Referenz zu **Kibana** ist, dem Open-Source-Datenvisualisierungs-Dashboard für Elasticsearch. Im Kontext von **Pivotal Cloud Foundry (PCF)** (jetzt umbenannt in VMware Tanzu Application Service) wird Kibana häufig verwendet, um Protokolle über das Logging-System der Plattform (Loggregator) zu durchsuchen, zu visualisieren und zu analysieren. PCF führt Kibana nicht nativ als Standalone-Anwendung aus, sondern integriert es über den **Log Search**-Tile/Service, der Protokolle in Elasticsearch speichert und Kibana für Abfragen bereitstellt.

Falls dies nicht das ist, was Sie gemeint haben, können Sie gerne nähere Angaben machen! Im Folgenden werde ich erklären, wie man Kibana mit PCF-Protokollen einrichtet und verwendet. Dies setzt voraus, dass Sie Administrator mit Zugriff auf die PCF Ops Manager sind und eine laufende PCF-Bereitstellung (Version 2.0+) haben. Beachten Sie, dass sich die PCF-Protokollierung weiterentwickelt hat; konsultieren Sie die Dokumentation Ihrer Version für genaue Angaben.

### Voraussetzungen
- **PCF-Version**: Log Search (mit Kibana) ist in PCF 2.2+ verfügbar. Frühere Versionen verwendeten einen separaten "ELK"-Tile (Elasticsearch, Logstash, Kibana).
- **Tiles/Services**: Stellen Sie sicher, dass der **Elastic Runtime**-Tile (für Loggregator) und der **Log Search**-Tile über den Pivotal Network (jetzt Broadcom Support Portal) installiert sind.
- **Zugriff**: Administratorrechte im Ops Manager und im PCF CLI (cf-Befehlszeilenwerkzeug).
- **Ressourcen**: Weisen Sie ausreichend Ressourcen zu (z. B. 4-8 GB RAM für Log Search, abhängig vom Protokollaufkommen).

### Schritt 1: Log Search Tile im Ops Manager installieren und konfigurieren
Der Log Search Tile leitet PCF-Protokolle (von Apps, Plattformen und Systemkomponenten) an Elasticsearch weiter, wodurch sie über Kibana durchsuchbar werden.

1. **Tile herunterladen und importieren**:
   - Melden Sie sich beim Broadcom Support Portal (ehemals Pivotal Network) an.
   - Laden Sie den **Log Search for PCF**-Tile herunter (z. B. die Version, die Ihrer PCF-Version entspricht).
   - Gehen Sie im Ops Manager (Web-UI) zu **Katalog** > **Produkt importieren** und laden Sie den Tile hoch.

2. **Tile konfigurieren**:
   - Gehen Sie im Ops Manager zum **Elastic Runtime**-Tile > **Loggregator** Tab:
     - Aktivieren Sie **Loggregator forwarding to external systems** (z. B. Syslog- oder HTTP-Weiterleitung einrichten, falls benötigt, aber für Log Search ist dies intern).
     - Setzen Sie **Loggregator log retention** auf einen Wert wie 5-30 Tage.
   - Gehen Sie zum **Log Search**-Tile:
     - **Assign Availability Zones**: Wählen Sie mindestens eine AZ für Hochverfügbarkeit.
     - **Elasticsearch Configuration**:
       - Legen Sie die Instanzanzahl fest (beginnen Sie mit 3 für Produktion).
       - Konfigurieren Sie den Speicher (z. B. 100 GB persistente Datenträger).
       - Aktivieren Sie die Sicherheit (z. B. TLS für Elasticsearch).
     - **Kibana Configuration**:
       - Aktivieren Sie Kibana (es ist gebündelt).
       - Legen Sie Administrator-Anmeldedaten (Benutzername/Passwort) fest.
     - **Loggregator Integration**:
       - Setzen Sie die maximale Anzahl an Protokollzeilen pro Sekunde (z. B. 1000-5000 basierend auf Ihrer Last).
       - Definieren Sie Index-Muster (z. B. Beibehaltung von Protokollen für 7-30 Tage).
     - **Networking**: Machen Sie Kibana über eine Route verfügbar (z. B. `kibana.IHR-PCF-DOMAIN.com`).
   - Klicken Sie auf **Änderungen anwenden**, um die Bereitstellung durchzuführen. Dies kann 30-60 Minuten dauern.

3. **Bereitstellung überprüfen**:
   - Führen Sie `cf tiles` aus oder prüfen Sie den Erfolg im Ops Manager.
   - SSH-en Sie in eine Log Search VM (mit BOSH CLI: `bosh ssh log-search/0`) und bestätigen Sie, dass Elasticsearch läuft (`curl localhost:9200`).

### Schritt 2: Auf Kibana zugreifen
Sobald bereitgestellt:

1. **Über PCF Apps Manager (GUI)**:
   - Melden Sie sich beim Apps Manager an (z. B. `https://apps.IHR-PCF-DOMAIN.com`).
   - Suchen Sie nach der "Log Search"-Serviceinstanz (eine wird automatisch erstellt).
   - Klicken Sie auf die Serviceinstanz > **Logs** Tab. Dies öffnet eine eingebettete Kibana-Ansicht für schnelle Protokollsuchen.

2. **Direkter Zugriff auf Kibana**:
   - Navigieren Sie zur im Tile konfigurierten Kibana-URL (z. B. `https://kibana.IHR-PCF-DOMAIN.com`).
   - Melden Sie sich mit den von Ihnen festgelegten Administrator-Anmeldedaten an.
   - Falls eine benutzerdefinierte Domain verwendet wird, stellen Sie sicher, dass DNS korrekt eingerichtet ist und Routen registriert sind (`cf routes` zur Überprüfung).

3. **CLI-Zugriff (Optional)**:
   - Verwenden Sie `cf logs APP-NAME` für grundlegende Protokolle, aber für erweiterte Abfragen nutzen Sie die Kibana-UI oder API.
   - Binden Sie Log Search an Ihre Apps: `cf create-service log-search standard my-log-search` dann `cf bind-service APP-NAME my-log-search`.

### Schritt 3: Kibana für PCF-Protokolle verwenden
Kibana bietet eine webbasierte Oberfläche zum Abfragen, Filtern und Visualisieren von Protokollen aus PCF-Komponenten (z. B. App-Protokolle, Diego Cells, Gorouter, etc.).

1. **Grundlegende Navigation**:
   - **Discover Tab**: Durchsuchen Sie Protokolle mit der Lucene-Abfragesyntax.
     - Beispiel: Nach Fehlern in einer bestimmten App suchen: `source_id:APP:ihr-app-name AND json.message:ERROR`.
     - Verfügbare Felder: `timestamp`, `source_id` (z. B. `APP:ihre-app`, `RTR:router`), `message`, `deployment`, etc.
   - **Visualize Tab**: Erstellen Sie Dashboards für Diagramme (z. B. Protokollvolumen über die Zeit, Fehlerraten).
     - Beispiel-Visualisierung: Balkendiagramm der Protokolle nach source_id.
   - **Dashboard Tab**: Speichern und teilen Sie vorgefertigte Dashboards (Log Search enthält Standard-Dashboards für PCF-Protokolle).

2. **Häufige Abfragen und Tipps**:
   - **Nach App filtern**: `source_id:APP:ihr-app-name` (ersetzen Sie mit der tatsächlichen App-GUID oder dem Namen).
   - **Nach Zeit filtern**: Verwenden Sie den Zeitauswähler (z. B. letzte 24 Stunden).
   - **Systemprotokolle**: `source_id:DEA` (für Diego Cells) oder `source_id:LOGGREGATOR`.
   - **Protokolle exportieren**: Laden Sie sie als CSV/JSON aus dem Discover-Tab herunter.
   - **Erweitert**: Verwenden Sie Kibanas Dev Tools (Konsole), um Elasticsearch direkt abzufragen, z. B.:
     ```
     GET /logstash-*/_search
     {
       "query": { "match": { "message": "error" } },
       "sort": [ { "timestamp": { "order": "desc" } } ]
     }
     ```
   - **Aufbewahrung und Indizierung**: Protokolle werden täglich indiziert (z. B. `logstash-YYYY.MM.DD`). Konfigurieren Sie den Rollover im Tile, um den Speicher zu verwalten.

3. **Fehlerbehebung bei Protokollen**:
   - **Erscheinen keine Protokolle?** Überprüfen Sie die Weiterleitungsregeln in Loggregator (Ops Manager > Elastic Runtime > Loggregator). Stellen Sie sicher, dass Apps Protokolle ausgeben (z. B. via `console.log` in Node.js).
   - **Leistungsprobleme?** Skalieren Sie die Elasticsearch-Instanzen hoch oder optimieren Sie die Protokollratenlimits.
   - **Sicherheit**: Aktivieren Sie die UAA-Integration in Log Search für SSO-Login bei Kibana.
   - **Fehler**: Überprüfen Sie PCF-Protokolle mit `cf logs log-search` oder Ops Manager Errand-Protokollen.

### Zusätzliche Ressourcen
- **Offizielle Dokumentation**: VMware Tanzu Docs zu [Log Search](https://docs.vmware.com/en/VMware-Tanzu-Application-Service/10.0/tas/GUID-log-search-index.html) (suchen Sie nach Ihrer Version).
- **CLI-Tools**: Installieren Sie `uaac` für UAA-Authentifizierung, falls benötigt, oder verwenden Sie `cf curl` für API-Zugriff.
- **Alternativen**: Für einfachere Anforderungen verwenden Sie den integrierten **Log Cache** von PCF (cf CLI: `cf tail APP-NAME`) oder integrieren Sie externe Tools wie Splunk über Syslog-Weiterleitung.
- **Upgrades**: Falls Sie sich auf einem Legacy-PCF befinden, migrieren Sie zum ELK-Tile oder wenden Sie sich an den Broadcom-Support.

Wenn Sie weitere Details angeben (z. B. Ihre PCF-Version, Fehlermeldungen oder spezifischen Anwendungsfall), kann ich dies weiter verfeinern!