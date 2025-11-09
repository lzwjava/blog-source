---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Apache Bench Web Server Testleitfaden
translated: true
type: note
---

### Was ist Apache Bench (ab)?

Apache Bench (ab) ist ein einfaches Kommandozeilen-Tool, das mit dem Apache HTTP Server ausgeliefert wird, um die Leistung von Webservern zu benchmarken. Es sendet eine bestimmte Anzahl von HTTP-Anfragen an eine URL und misst Metriken wie Anfragen pro Sekunde, Zeit pro Anfrage, Transferraten und Fehlerquoten. Es ist hervorragend für schnelle Lasttests geeignet, aber für komplexe Szenarien eingeschränkt (z. B. keine HTTPS-Unterstützung standardmäßig oder kein erweitertes Scripting – für solche Zwecke sollten Tools wie JMeter in Betracht gezogen werden).

### Installation

ab ist im Lieferumfang des Apache HTTP Servers enthalten. So installieren Sie es:

- **Unter Ubuntu/Debian (Linux)**:
  ```
  sudo apt update
  sudo apt install apache2-utils
  ```

- **Unter macOS (via Homebrew)**:
  ```
  brew install httpd
  ```

- **Unter Windows**:
  Laden Sie den Apache HTTP Server von der offiziellen Website herunter und fügen Sie dessen `bin`-Verzeichnis zu Ihrem PATH hinzu.

- **Installation überprüfen**:
  Führen Sie `ab -V` aus, um die Version zu prüfen.

### Grundlegende Verwendung

Die grundlegende Befehls-Syntax lautet:
```
ab [Optionen] URL
```

- **URL-Format**: Muss eine vollständige HTTP-URL sein, z. B. `http://example.com/`. (Für HTTPS verwenden Sie einen Wrapper wie `openssl s_client` oder wechseln Sie zu Tools wie `wrk`.)

Wichtige Optionen:
- `-n <Anzahl>`: Anzahl der durchzuführenden Anfragen (Standard: 1). Beginnen Sie mit 100–1000 zum Testen.
- `-c <Nebenläufigkeit>`: Anzahl der gleichzeitig auszuführenden Anfragen (Standard: 1). Halten Sie sie niedrig (z. B. 10–50), um eine Überlastung des Servers zu vermeiden.
- `-t <Sekunden>`: Führt den Test für eine bestimmte Zeitdauer anstelle einer festen Anfragenzahl aus.
- `-k`: Aktiviert HTTP Keep-Alive (Wiederverwendung von Verbindungen).
- `-H "Header: Wert"`: Fügt benutzerdefinierte Header hinzu (z. B. für Authentifizierung).
- `-p <Datei>`: POST-Daten aus einer Datei.
- `-T <Content-Type>`: Content-Type für POST-Anfragen.
- `-l`: Akzeptiert variable Dokumentlängen (für dynamische Inhalte).

### Schritt-für-Schritt-Beispiel

1. **Einfache GET-Anfrage testen**:
   Simulieren Sie 100 Anfragen mit 10 gleichzeitigen Benutzern gegen einen lokalen Server:
   ```
   ab -n 100 -c 10 http://localhost:8080/
   ```
   Beispielhafte Ausgabe:
   ```
   Server Software:        Apache/2.4.41
   Server Hostname:        localhost
   Server Port:            8080

   Document Path:          /
   Document Length:        1234 bytes

   Concurrency Level:      10
   Time taken for tests:   1.234 seconds
   Complete requests:      100
   Failed requests:        0
   Requests per second:    81.03 [#/sec] (mean)
   Time per request:       123.456 [ms] (mean)
   ```

2. **Test mit POST-Daten** (z. B. Formularübermittlung):
   Erstellen Sie eine Datei `postdata.txt` mit Ihren Daten (z. B. `key=value`).
   ```
   ab -n 50 -c 5 -p postdata.txt -T application/x-www-form-urlencoded http://example.com/api/endpoint
   ```

3. **Test für eine Zeitdauer ausführen**:
   ```
   ab -n 10000 -c 20 -t 30 http://example.com/  # Bis zu 10k Anfragen oder 30 Sekunden
   ```

### Ergebnisse interpretieren

- **Anfragen pro Sekunde**: Höher ist besser (Durchsatz).
- **Zeit pro Anfrage**: Niedriger ist besser (Latenz).
- **Transferrate**: Bandbreiteneffizienz.
- Achten Sie auf "Failed requests" oder "Non-2xx responses", um Probleme zu erkennen.
- Führen Sie mehrere Durchläufe durch und mitteln Sie die Ergebnisse, da Caching/Netzwerk einzelne Läufe verzerren können.

### Tipps und Einschränkungen

- **Von einem separaten Rechner ausführen**: Testen Sie nach Möglichkeit nicht gegen localhost, um echten Datenverkehr zu simulieren.
- **Aufwärmphase**: Senden Sie zuerst einige Anfragen, um Caches zu füllen.
- **Skalierung**: Für höhere Lasten verwenden Sie Tools wie `wrk`, `siege` oder Locust.
- **HTTPS**: ab unterstützt es nicht nativ; verwenden Sie `ab -n 100 -c 10 http://example.com/` mit einem Proxy oder Alternativen.
- **Fehler**: Wenn Sie "socket: Too many open files" sehen, erhöhen Sie das Dateideskriptor-Limit Ihres Betriebssystems (z. B. `ulimit -n 4096`).

Weitere Details finden Sie in der Manpage (`man ab`) oder der offiziellen Dokumentation.

[Apache Bench Dokumentation](https://httpd.apache.org/docs/2.4/programs/ab.html)