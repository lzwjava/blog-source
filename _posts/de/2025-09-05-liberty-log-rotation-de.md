---
audio: false
generated: true
image: false
lang: de
layout: post
title: Konfigurationshandbuch für die Rotation von Liberty-Protokolldateien
translated: true
type: note
---

Hier die Kurzfassung, dann Beispiele, die Sie in `server.xml` einfügen können.

### So funktioniert die Log-Rotation bei Liberty

* **Was rotiert wird:** `messages.log` und `trace.log`.
  Die Rotation kann **größenbasiert** und/oder **zeitbasiert** sein. ([openliberty.io][1])
* **Was nicht rotiert wird:** `console.log` (es ist nur stdout/stderr). Sie können sie stattdessen reduzieren oder deaktivieren. ([openliberty.io][2], [IBM][3])
* **Konfigurationsort:** das `<logging …/>`-Element in `server.xml`. (Sie können dieselben Werte auch in `bootstrap.properties`/Umgebungsvariablen setzen, falls diese gelten müssen, *bevor* `server.xml` geladen wird.) ([openliberty.io][2])
* **Access Logs:** Das HTTP-Access-Log hat **eigene** zeitbasierte Rollover-Einstellungen unter `httpAccessLogging` / `accessLogging`. ([openliberty.io][4])
* **Sowohl Größe + Zeit:** Moderne Liberty unterstützt zeitbasierten Rollover zusätzlich zur klassischen größenbasierten Option, Sie können also eine oder beide Optionen verwenden (außer für `console.log`). ([IBM][5])

---

### Häufige `server.xml`-Beispiele

#### 1) Größenbasierte Rotation (klassisch)

Behält bis zu 10 Dateien, jede bis zu 256 MB.

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="10"/>
```

Effekt: Wenn `messages.log` oder `trace.log` 256 MB überschreitet, rolled Liberty sie in eine zeitgestempelte Datei und behält maximal 10 solcher Dateien. (Betrifft `console.log` nicht.) ([openliberty.io][1])

#### 2) Zeitbasierte Rotation (z.B. täglich um Mitternacht)

```xml
<logging
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

Effekt: `messages.log` und `trace.log` rolled jeden Tag um 00:00. Sie können auch Minuten (`m`) oder Stunden (`h`) verwenden, z.B. `30m` oder `6h`. ([openliberty.io][2])

#### 3) Kombination aus Größe + Zeit (typisch für Produktion)

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="14"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

Effekt: Rollover **je nachdem, was zuerst eintritt** (Größe oder Zeitplan), und ein 14-Dateien-History wird beibehalten. ([IBM][5])

#### 4) `console.log`-Wachstum zähmen oder deaktivieren

`console.log` kann nicht rotieren; reduzieren oder deaktivieren Sie sie und verlassen Sie sich auf `messages.log`.

```xml
<logging
  consoleLogLevel="OFF"
  copySystemStreams="false"/>
```

Hinweis: Das Deaktivieren der Konsole stoppt Libertys eigene Log-Kopie in `console.log`, aber die JVM kann weiterhin Dinge wie `-verbose:gc` nach stdout/stderr schreiben. ([openliberty.io][2])

#### 5) Namen/Format-Anpassungen (optional)

```xml
<logging
  messageFileName="messages.log"
  traceFileName="trace.log"
  messageFormat="JSON"/>
```

JSON ist praktisch für den Versand an einen Log-Stack; belassen Sie die Standardeinstellungen, wenn Sie es nicht benötigen. ([openliberty.io][1])

---

### HTTP-Access-Log (separat vom Obigen)

Aktivieren Sie Access-Logging und rolled es täglich um Mitternacht:

```xml
<httpAccessLogging id="accessLogging"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>

<httpEndpoint id="defaultHttpEndpoint"
  httpPort="9080" httpsPort="9443"
  accessLoggingRef="accessLogging"/>
```

(Oder setzen Sie `rolloverStartTime`/`rolloverInterval` direkt auf einem `<accessLogging …/>`-Child von `httpEndpoint`.) ([openliberty.io][4])

---

### Schnell-Checkliste

* Verwenden Sie **`maxFileSize` + `maxFiles`** für größenbasierten Rollover. ([openliberty.io][1])
* Verwenden Sie **`rolloverStartTime` + `rolloverInterval`** für zeitbasierten Rollover. ([openliberty.io][2])
* **Erwarten Sie keine Rotation von `console.log`**; setzen Sie `consoleLogLevel="OFF"` und `copySystemStreams="false"`, wenn Sie große Konsolendateien vermeiden möchten. ([openliberty.io][2], [IBM][3])

Wenn Sie Ihren aktuellen `server.xml`-Ausschnitt oder Ihre Aufbewahrungsziele teilen (z.B. "~7 Tage behalten" oder "auf 2 GB begrenzen"), passe ich die genauen Werte an.

[1]: https://openliberty.io/docs/latest/reference/config/logging.html "Logging (logging) :: Open Liberty Docs"
[2]: https://openliberty.io/docs/latest/log-trace-configuration.html "Log and trace configuration :: Open Liberty Docs"
[3]: https://www.ibm.com/support/pages/how-turn-console-logging-prevent-excess-file-growth-and-use-only-message-log-rotation-liberty-profile-or-open-liberty?utm_source=chatgpt.com "How to turn off Console logging, prevent excess file growth ..."
[4]: https://openliberty.io/docs/latest/access-logging.html "HTTP access logging :: Open Liberty Docs"
[5]: https://www.ibm.com/support/pages/how-setup-liberty-log-rollover-both-time-based-and-size-based-options-similar-traditional-websphere-0?utm_source=chatgpt.com "How to setup Liberty Log Rollover with both Time-Based ..."