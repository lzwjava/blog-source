---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Kibana-Protokollprüfungsleitfaden
translated: true
type: note
---

Kibana ist ein Open-Source-Datenvisualisierungs- und Explorationstool, das von Elastic entwickelt wurde. Es ist eine Schlüsselkomponente des **ELK-Stacks** (Elasticsearch, Logstash, Kibana), der weit verbreitet ist für zentralisiertes Logging, Monitoring und Analytics. Kibana bietet eine webbasierte Oberfläche zur Interaktion mit in Elasticsearch gespeicherten Daten, ermöglicht es Ihnen, Logs in Echtzeit zu durchsuchen, zu visualisieren und zu analysieren. Es ist besonders leistungsstark für die Überprüfung von Logs von Anwendungen, Servern oder Cloud-Diensten.

Dieser Leitfaden konzentriert sich auf die Verwendung von Kibana zur Inspektion und Abfrage von Logs. Wir behandeln Setup, grundlegende Verwendung, Arbeitsabläufe zur Log-Prüfung und fortgeschrittene Tipps. Gehen Sie davon aus, dass Sie mit einem grundlegenden ELK-Setup arbeiten; wenn Sie neu bei ELK sind, beginnen Sie mit der Installation von Elasticsearch und Logstash (Kibana benötigt Elasticsearch, um zu funktionieren).

## 1. Voraussetzungen
Bevor Sie Kibana verwenden:
- **Elasticsearch**: Version 8.x oder höher (Kibana ist eng mit Elasticsearch-Versionen gekoppelt). Laden Sie es von [elastic.co](https://www.elastic.co/downloads/elasticsearch) herunter.
- **Java**: Elasticsearch benötigt JDK 11 oder höher.
- **Systemanforderungen**: Mindestens 4 GB RAM für die Entwicklung; mehr für die Produktion.
- **Datenquelle**: Logs, die via Logstash, Filebeat oder direkt in Elasticsearch ingestiert wurden (z.B. JSON-Format mit Zeitstempeln).
- **Netzwerkzugriff**: Kibana läuft standardmäßig auf Port 5601; stellen Sie sicher, dass dieser erreichbar ist.

Wenn Sie noch keine Logs haben, verwenden Sie Tools wie Filebeat, um Beispiel-Logs (z.B. System-Logs) an Elasticsearch zu senden.

## 2. Installation von Kibana
Die Installation von Kibana ist unkompliziert und plattformunabhängig. Laden Sie die neueste Version von [elastic.co/downloads/kibana](https://www.elastic.co/downloads/kibana) herunter (stimmen Sie die Version auf Ihre Elasticsearch-Version ab).

### Unter Linux (Debian/Ubuntu):
1. Fügen Sie das Elastic-Repository hinzu:
   ```
   wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
   sudo apt-get install apt-transport-https
   echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
   sudo apt-get update && sudo apt-get install kibana
   ```
2. Starten Sie Kibana:
   ```
   sudo systemctl start kibana
   sudo systemctl enable kibana  # Für automatischen Start beim Booten
   ```

### Unter Windows:
1. Laden Sie das ZIP-Archiv herunter und extrahieren Sie es nach `C:\kibana-8.x.x-windows-x86_64`.
2. Öffnen Sie die Eingabeaufforderung als Administrator und navigieren Sie zum extrahierten Ordner.
3. Führen Sie aus: `bin\kibana.bat`

### Unter macOS:
1. Verwenden Sie Homebrew: `brew tap elastic/tap && brew install elastic/tap/kibana-full`.
2. Oder laden Sie das TAR.GZ herunter, extrahieren Sie es und führen Sie `./bin/kibana` aus.

Für Docker: Verwenden Sie das offizielle Image:
```
docker run --name kibana -p 5601:5601 -e ELASTICSEARCH_HOSTS=http://elasticsearch:9200 docker.elastic.co/kibana/kibana:8.10.0
```

## 3. Grundlegende Konfiguration
Bearbeiten Sie die Konfigurationsdatei `kibana.yml` (befindet sich unter `/etc/kibana/` auf Linux oder im `config/`-Ordner auf anderen Systemen).

Wichtige Einstellungen für die Log-Prüfung:
```yaml
# Verbindung zu Elasticsearch (Standard ist localhost:9200)
elasticsearch.hosts: ["http://localhost:9200"]

# Server-Einstellungen
server.port: 5601
server.host: "0.0.0.0"  # An alle Schnittstellen binden für Fernzugriff

# Sicherheit (für Produktion aktivieren)
# elasticsearch.username: "elastic"
# elasticsearch.password: "Ihr_Passwort"

# Logging
logging.verbose: true  # Zum Debuggen von Kibana selbst

# Index Pattern (optionaler Standard)
defaultIndex: "logs-*"
```
- Starten Sie Kibana nach Änderungen neu: `sudo systemctl restart kibana`.
- Wenn Sie Sicherheitsfunktionen (X-Pack) verwenden, generieren Sie Zertifikate oder verwenden Sie Basic Auth.

## 4. Starten und Zugreifen auf Kibana
- Starten Sie zuerst Elasticsearch (z.B. `sudo systemctl start elasticsearch`).
- Starten Sie Kibana wie oben beschrieben.
- Öffnen Sie einen Webbrowser und gehen Sie zu `http://localhost:5601` (oder der IP Ihres Servers:5601).
- Beim ersten Login sehen Sie den Setup-Assistenten. Erstellen Sie bei Aufforderung einen Admin-Benutzer (Standard: elastic/changeme).

Die Oberfläche enthält Apps wie **Discover** (für Logs), **Visualize**, **Dashboard**, **Dev Tools** und **Management**.

## 5. Daten vorbereiten: Index Patterns
Logs in Elasticsearch werden in **Indizes** gespeichert (z.B. `logs-2023-10-01`). Um sie in Kibana abzufragen, erstellen Sie ein **Index Pattern**.

1. Gehen Sie zu **Stack Management** > **Index Patterns** (linke Seitenleiste, Hamburger-Menü > Management).
2. Klicken Sie auf **Create index pattern**.
3. Geben Sie ein Pattern wie `logs-*` ein (passt auf alle Log-Indizes) oder `filebeat-*` (für Filebeat-Logs).
4. Wählen Sie das **Time field** (z.B. `@timestamp` für Log-Zeitstempel – entscheidend für zeitbasierte Abfragen).
5. Klicken Sie auf **Create index pattern**.
   - Dies mappt Felder wie `message` (Log-Text), `host.name`, `level` (error/warn/info) usw.

Aktualisieren Sie die Felder, wenn sich Ihre Logs ändern. Verwenden Sie **Discover** für eine Vorschau.

## 6. Verwenden von Discover zum Überprüfen von Logs
Die **Discover**-App ist Ihr primäres Tool zur Inspektion von Logs. Es ist wie ein durchsuchbarer Log-Viewer.

### Grundlegende Navigation:
1. Klicken Sie auf **Discover** in der linken Seitenleiste.
2. Wählen Sie Ihr Index Pattern aus dem Dropdown-Menü (oben links).
3. Legen Sie den Zeitbereich fest (oben rechts): Verwenden Sie schnelle Optionen wie "Last 15 minutes" oder benutzerdefinierte (z.B. Last 7 days). Dies filtert Logs nach `@timestamp`.

### Logs anzeigen:
- **Trefferanzahl**: Zeigt die gesamte Anzahl passender Logs an (z.B. 1.234 Treffer).
- **Dokumententabelle**: Zeigt rohe Log-Einträge als JSON oder formatierten Text an.
  - Spalten: Standardmäßig `@timestamp` und `_source` (vollständiger Log). Ziehen Sie Felder aus der linken Seitenleiste (z.B. `message`, `host.name`) per Drag & Drop hinzu, um Spalten hinzuzufügen.
  - Erweitern Sie eine Zeile (klicken Sie auf den Pfeil), um das vollständige JSON-Dokument zu sehen.
- **Histogramm**: Das obere Diagramm zeigt das Log-Aufkommen über die Zeit an. Zoomen Sie durch Ziehen.

### Logs durchsuchen:
Verwenden Sie die Suchleiste (oben) für Abfragen. Kibana verwendet standardmäßig **KQL (Kibana Query Language)** – einfach und intuitiv.

- **Einfache Suche**:
  - Nach einem Schlüsselwort suchen: `error` (findet Logs, die "error" enthalten).
  - Feld-spezifisch: `host.name:webserver AND level:error` (Logs von "webserver" mit Fehler-Level).
  - Phrasen: `"user login failed"` (exakte Übereinstimmung).

- **Filter**:
  - Hinzufügen über die Seitenleiste: Klicken Sie auf einen Feldwert (z.B. `level: ERROR`) > Add filter (heftet ihn an die Abfrage).
  - Boolesche Logik: `+error -info` (muss "error" enthalten, schließe "info" aus).
  - Bereich: Für Zahlen/Zeiten, z.B. `bytes:>1000` (Feld > 1000).

- **Erweiterte Abfragen**:
  - Wechseln Sie zur **Lucene query syntax** (über das Abfragesprachen-Dropdown) für komplexe Anforderungen: `message:(error OR warn) AND host.name:prod*`.
  - Verwenden Sie **Query DSL** in Dev Tools für Elasticsearch-native Abfragen (z.B. POST /logs-*/_search mit JSON-Body).

### Suchen speichern:
- Klicken Sie auf **Save** (oben rechts), um eine Suche zur Wiederverwendung zu speichern.
- Teilen über **Share** > CSV/URL für Exporte.

Beispiel Arbeitsablauf: Anwendungslogs überprüfen
1. Logs ingestieren (z.B. via Logstash: input file > filter grok/parse > output Elasticsearch).
2. In Discover: Zeitbereich "Last 24 hours".
3. Suche: `app.name:myapp AND level:ERROR`.
4. Filter hinzufügen: `host.name` = bestimmter Server.
5. Inspizieren: Sehen Sie sich `message` für Stack Traces an, korrelieren Sie mit `@timestamp`.

## 7. Visualisierung von Logs
Während Discover für die rohe Überprüfung ist, visualisieren Sie für Muster.

### Visualisierungen erstellen:
1. Gehen Sie zu **Visualize Library** > **Create new visualization**.
2. Wählen Sie den Typ:
   - **Lens** (einfach): Ziehen Sie Felder in Buckets (z.B. X-Achse: `@timestamp`, Y-Achse: Anzahl der Fehler).
   - **Area/Line Chart**: Für Log-Aufkommen über die Zeit (Metrics: Count, Buckets: Date Histogram on `@timestamp`).
   - **Data Table**: Tabellarische Log-Zusammenfassung.
   - **Pie Chart**: Aufschlüsselung nach `level` (error 40%, info 60%).
3. Wenden Sie Filter/Suchen von Discover an.
4. Speichern und zu einem **Dashboard** hinzufügen (Analytics > Dashboard > Create new > Add visualization).

Beispiel: Error Rate Dashboard
- Visualisieren: Liniendiagramm der Fehler-Logs pro Stunde.
- Filter: Globaler Zeitbereich.
- In Dashboard einbetten für Monitoring.

## 8. Erweiterte Funktionen für die Log-Analyse
- **Alerts und Monitoring**:
  - Verwenden Sie **Alerts** (Stack Management > Rules) für Benachrichtigungen bei Log-Mustern (z.B. E-Mail, wenn "critical" >5 Mal/Stunde erscheint).
  - **Uptime Monitoring** oder **APM** für App-Logs.

- **Machine Learning**:
  - Aktivieren Sie ML-Jobs (Stack Management > Machine Learning), um Anomalien im Log-Aufkommen zu erkennen.

- **Dev Tools**:
  - Konsole für rohe Elasticsearch-Abfragen: z.B.
    ```
    GET logs-*/_search
    {
      "query": { "match": { "message": "error" } },
      "sort": [ { "@timestamp": "desc" } ]
    }
    ```
  - Testen Sie Index Patterns oder ingestieren Sie Daten.

- **Rollen und Sicherheit**:
  - Verwenden Sie in der Produktion **Spaces**, um Log-Ansichten zu isolieren (z.B. dev/prod).
  - Rollenbasierter Zugriff: Beschränken Sie Benutzer auf bestimmte Indizes.

- **Export/Import**:
  - Exportieren Sie Suchen/Dashboards als NDJSON via **Stack Management > Saved Objects**.
  - Importieren Sie Logs via **Console** oder Beats.

- **Performance-Tipps**:
  - Verwenden Sie **Field Analyzer** (Index Patterns > field) für benutzerdefinierte Mappings.
  - Paginieren Sie große Ergebnisse: Passen Sie Treffer pro Seite an (Discover-Einstellungen).
  - Für große Datenmengen, sharden Sie Indizes und verwenden Sie ILM (Index Lifecycle Management).

## 9. Integration mit Log-Quellen
- **Filebeat/Logstash**: Senden Sie Logs an Elasticsearch.
  - Beispiel Filebeat-Konfiguration (`filebeat.yml`):
    ```yaml
    filebeat.inputs:
    - type: log
      paths: [/var/log/*.log]
      fields:
        app: myapp
    output.elasticsearch:
      hosts: ["localhost:9200"]
      index: "logs-%{+yyyy.MM.dd}"
    ```
  - Ausführen: `./filebeat -e`.
- **Cloud-Logs**: Integrieren Sie mit AWS S3, Azure oder Elastic Cloud für verwaltete Setups.

## 10. Fehlerbehebung bei häufigen Problemen
- **Keine Daten in Discover**:
  - Überprüfen Sie die Elasticsearch-Verbindung: `curl localhost:9200/_cat/indices`.
  - Stellen Sie sicher, dass das Index Pattern mit den Indizes übereinstimmt (z.B. kein `*`-Mismatch).
  - Stellen Sie sicher, dass `@timestamp` als Datum gemappt ist.

- **Kibana startet nicht**:
  - Logs: Überprüfen Sie `/var/log/kibana/kibana.log` oder die Konsolenausgabe.
  - Häufig: Port 5601 belegt, oder Elasticsearch läuft nicht/ist gesichert.

- **Langsame Abfragen**:
  - Optimieren: Verwenden Sie Keyword-Felder für Filter, vermeiden Sie Wildcards bei großen Texten.
  - Erhöhen Sie den Heap: Bearbeiten Sie `jvm.options` für Elasticsearch (z.B. `-Xms4g -Xmx4g`).

- **Fehler in Logs**:
  - 403/401: Authentifizierungsprobleme – aktivieren Sie Sicherheit in `elasticsearch.yml`.
  - Versionskonflikt: Stellen Sie sicher, dass Kibana == Elasticsearch-Version.

- **Ressourcen**:
  - Offizielle Dokumentation: [elastic.co/guide/en/kibana/current](https://www.elastic.co/guide/en/kibana/current/index.html).
  - Foren: Elastic Discuss oder Stack Overflow.
  - Beispieldaten: Laden via Kibana (Stack Management > Kibana > Sample Data).

Dieser Leitfaden sollte Ihnen den Einstieg in Kibana für die Log-Überprüfung ermöglichen. Fangen Sie klein an: Richten Sie einen lokalen ELK-Stack ein, ingestieren Sie Beispiel-Logs und experimentieren Sie in Discover. Für die Produktion ziehen Sie Elastic Cloud für Einfachheit in Betracht. Wenn Sie ein bestimmtes Setup haben (z.B. Docker, AWS), geben Sie mehr Details für maßgeschneiderte Ratschläge an!