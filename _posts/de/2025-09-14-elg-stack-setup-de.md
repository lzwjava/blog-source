---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Einrichtung und Installation des ELG-Stacks
translated: true
type: note
---

### Überblick über den ELG-Stack (Elasticsearch, Logstash, Grafana)

Der ELG-Stack (oft eine Variante des ELK-Stacks, bei dem Kibana durch Grafana zur Visualisierung ersetzt wird) ist eine leistungsstarke Open-Source-Suite zum Sammeln, Verarbeiten, Speichern und Visualisieren großer Datenmengen, insbesondere von Logs aus Anwendungen, Servern und der Infrastruktur. Er ermöglicht Echtzeit-Monitoring, Analysen und Warnmeldungen. Wichtige Komponenten:

- **Elasticsearch**: Eine verteilte Such- und Analysemaschine zum Speichern, Durchsuchen und Analysieren von Daten in großem Maßstab.
- **Logstash**: Eine Datenverarbeitungspipeline, die Daten aus mehreren Quellen erfasst, transformiert und an Elasticsearch sendet.
- **Grafana**: Ein Visualisierungs- und Monitoring-Dashboard-Tool, das eine Verbindung zu Datenquellen wie Elasticsearch herstellt, um Diagramme, Graphen und Warnungen zu erstellen.

Diese Anleitung setzt grundlegende Linux-Kenntnisse voraus (z.B. Ubuntu/Debian; für andere Betriebssysteme anpassen). Verwenden Sie für vollständige Details die offizielle Dokumentation. Installation über Downloads von elastic.co und grafana.com.

#### 1. Elasticsearch installieren
Elasticsearch übernimmt die Datenspeicherung und Indizierung.

- **Voraussetzungen**: Java 11+ (Installation via `sudo apt update && sudo apt install openjdk-11-jdk`).
- Herunterladen und installieren:
  ```
  wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
  echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
  sudo apt update && sudo apt install elasticsearch
  ```
- Starten und aktivieren: `sudo systemctl start elasticsearch && sudo systemctl enable elasticsearch`.
- Überprüfen: Rufen Sie `http://localhost:9200` auf – es sollte ein JSON mit Cluster-Informationen zurückgegeben werden.
- Grundlegende Konfiguration (bearbeiten Sie `/etc/elasticsearch/elasticsearch.yml`): Setzen Sie `network.host: 0.0.0.0` für Fernzugriff (im Produktivbetrieb mit TLS/Firewall absichern).

#### 2. Logstash installieren
Logstash holt Daten aus Quellen (z.B. Dateien, Syslogs) und sendet sie an Elasticsearch.

- Installieren Sie es zusammen mit Elasticsearch:
  ```
  sudo apt install logstash
  ```
- Starten und aktivieren: `sudo systemctl start logstash && sudo systemctl enable logstash`.
- Beispielkonfiguration zum Erfassen von Logs (`/etc/logstash/conf.d/simple.conf`):
  ```
  input {
    file {
      path => "/var/log/syslog"
      start_position => "beginning"
    }
  }
  filter {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{SYSLOGHOST:host} %{WORD:program}: %{GREEDYDATA:message}" }
    }
  }
  output {
    elasticsearch {
      hosts => ["localhost:9200"]
    }
    stdout { codec => rubydebug }
  }
  ```
- Pipeline testen: `sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/simple.conf` (für dauerhaften Betrieb im Hintergrund ausführen).
- Konfiguration neu laden: `sudo systemctl restart logstash`.

#### 3. Grafana installieren
Grafana bietet Dashboards zur Visualisierung der Elasticsearch-Daten.

- Installieren:
  ```
  wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
  echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
  sudo apt update && sudo apt install grafana
  ```
- Starten und aktivieren: `sudo systemctl start grafana-server && sudo systemctl enable grafana-server`.
- Zugriff: Rufen Sie `http://localhost:3000` auf (Standard-Login: admin/admin; Passwort ändern).
- Verbindung zu Elasticsearch herstellen:
  1. Gehen Sie zu Configuration > Data Sources > Add data source.
  2. Wählen Sie "Elasticsearch", setzen Sie die URL auf `http://localhost:9200`, den Indexnamen (z.B. `logstash-*`) und das Zeitfeld (z.B. `@timestamp`).
  3. Verbindung speichern und testen.

#### Aufbau der vollständigen ELG-Pipeline
1. **Datenfluss**: Logstash sammelt/parst Logs → sendet sie an Elasticsearch → Grafana fragt ab und visualisiert.
2. **Beispiel-Workflow**:
   - Beispieldaten senden: Verwenden Sie Logstash-Input-Plugins oder Tools wie `stdout` zum Testen.
   - In Elasticsearch indizieren: Logs erscheinen als Dokumente (z.B. über die Kibana-API oder direkt mit curl: `curl -X GET "localhost:9200/_search?pretty"`).
   - Dashboard in Grafana: Erstellen Sie Panels (z.B. Liniendiagramm für Log-Fehler über die Zeit mit Lucene-Abfragen wie `program:kern*`).
3. **Sicherheitsgrundlagen**: Verwenden Sie HTTPS/TLS, Authentifizierung (z.B. X-Pack für Elasticsearch) und Firewalls. Skalieren Sie für den Produktivbetrieb mit mehreren Nodes/Clustern.
4. **Monitoring**: Aktivieren Sie JVM-Monitoring in Elasticsearch; Grafana hat integrierte Warnungen für Schwellenwerte.

#### Häufige Probleme und Tipps
- **Nicht genug Arbeitsspeicher**: Erhöhen Sie den JVM-Heap in `/etc/elasticsearch/jvm.options` (z.B. `-Xms1g -Xmx1g`).
- **Port-Konflikte**: Standard-Ports: Elasticsearch 9200/9300, Logstash 5044, Grafana 3000 – prüfen Sie mit `netstat -tulpn`.
- **Leistung**: Verwenden Sie Beats (z.B. Filebeat) anstelle von Logstash für leichtgewichtiges Versenden.
- **Lernressourcen**: Offizielle Anleitungen von Elastic (elastic.co/guide), Grafana-Dokumentation (grafana.com/docs). Üben Sie mit Docker: Suchen Sie auf GitHub nach "ELG stack Docker Compose".

Für benutzerdefinierte Setups oder die Fehlerbehebung bei spezifischen Problemen geben Sie bitte weitere Details an. Dies ist ein Ausgangspunkt; ELG eignet sich hervorragend für Log-Analyse, IoT-Daten und App-Monitoring.