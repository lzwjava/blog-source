---
audio: false
date: 2025-09-07
generated: true
image: false
lang: de
layout: post
title: Verständnis von JaCoCo-Ausführungsdatendateien
translated: true
type: note
---

Hier ist eine praktische, alles-umfassende Übersicht.

# Was ist `jacoco-it.exec`?

* Es ist eine **JaCoCo-Ausführungsdatendatei**, die während **Integrationstests** erzeugt wird.
* Das "`-it`" ist lediglich eine **Konvention** (vom *report-integration*-Goal des `jacoco-maven-plugin` und der Failsafe-Phase). Unit-Tests schreiben oft in `jacoco.exec`, während Integrationstests in `jacoco-it.exec` schreiben.
* Sie können viele `.exec`-Dateien haben (pro Modul, pro Phase, pro Durchlauf) und sie später **zusammenführen**, um einen einzelnen Coverage-Bericht zu erstellen.

Typisches Maven-Setup:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <!-- für Unit-Tests -->
    <execution>
      <id>prepare-agent</id>
      <goals><goal>prepare-agent</goal></goals>
    </execution>
    <!-- für Integrationstests -->
    <execution>
      <id>prepare-agent-integration</id>
      <goals><goal>prepare-agent-integration</goal></goals>
    </execution>
    <execution>
      <id>report</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
    </execution>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-integration</goal></goals>
    </execution>
  </executions>
</plugin>
```

Dies schreibt üblicherweise `target/jacoco.exec` (Unit) und `target/jacoco-it.exec` (Integration).

# Was befindet sich in einer `.exec`-Datei?

* **Nur Probe Hits**, nach Klasse geordnet.
* Konkret: Für jede geladene Klasse berechnet JaCoCo eine **ID** (basierend auf dem Bytecode) und speichert ein **boolean-Array von Probes** (welche Instruktionen/Zweige ausgeführt wurden).
* Es speichert auch eine **Session-ID** und Zeitstempel.
* **Sie enthält *keinen* Klassen-Bytecode, Methodennamen, Zeilennummern oder Quellcode.** Diese strukturellen Informationen kommen später von Ihren **Klassendateien** und **Quelltexten**, wenn Sie `jacoco:report` ausführen, um HTML/XML zu rendern.

Implikationen:

* Wenn sich Ihre Klassen nach dem Erzeugen der `.exec`-Datei ändern, stimmt die Datei möglicherweise nicht mehr überein (IDs passen nicht). Generieren Sie den Bericht immer mit **exakt derselben Build-Version** der Klassendateien, die die .exec-Datei erzeugt hat.

# Enthält sie Klassenstrukturinformationen?

* **Nein.** Keine Methoden, keine Zeilennummern, kein Quellcode.
* Es ist eine kompakte, binäre **Hit-Map** pro Klasse. Der Berichtsschritt liest Ihre **kompilierten Klassen** (und optional Quelltexte), um diese Treffer Packages, Klassen, Methoden, Zeilen und Branches zuzuordnen.

# Wird sie aktualisiert, wenn sie via `-javaagent` angehängt wird?

Kurze Antwort: **Ja**, mit Details:

* Wenn Sie Ihre JVM mit dem Agent starten, instrumentiert dieser Klassen **on the fly** und zeichnet Probe Hits **im Speicher** auf.
* Der Agent **schreibt** in die `destfile`:

  * **Beim JVM-Exit** (für `output=file`, die Standardeinstellung), oder
  * Wenn Sie explizit ein **Dump** auslösen (TCP/JMX/API), oder
  * Wenn `append=true` gesetzt ist, wird er an eine bestehende Datei **anfügen/zusammenführen**, anstatt sie zu überschreiben.

Häufige Agent-Optionen:

```bash
-javaagent:/pfad/zu/org.jacoco.agent.jar=\
destfile=/pfad/zu/jacoco-it.exec,\
append=true,\
output=file
```

Andere nützliche Modi:

* `output=tcpserver` (an einem Port lauschen; Sie können sich verbinden und ein Dump auslösen)
* `output=tcpclient` (zu einem Server pushen)
* `jmx=true` (ein JMX MBean exportieren, um Dump/Reset durchzuführen)
* Programmatisch: `org.jacoco.agent.rt.RT.getAgent().dump(/*reset*/ true|false)`

Anmerkungen zu "aktualisiert":

* Mit `output=file` **und** `append=true` führt **jedes Dump** die Probe-Arrays mit der bestehenden Datei zusammen (logisches ODER der Hits).
* Ohne `append=true` **überschreibt** der nächste Schreibvorgang die Datei beim Dump/Exit.
* Wenn Sie **mehrere JVMs** haben (Microservices, geforkte Tests), zeigen Sie jede auf **unterschiedliche Dateien**, oder verwenden Sie TCP/JMX, um zentral zu sammeln, und führen Sie sie dann zusammen.

# Typische Workflows

**Integrationstest-Phase (Failsafe):**

* Maven hängt den Agent an die Integrationstest-JVM(s) mit `destfile=target/jacoco-it.exec` an.
* Am Ende wird `jacoco:report-integration` ausgeführt, welches liest:

  * `target/jacoco-it.exec` (Hits)
  * `target/classes` (Struktur)
  * `src/main/java` (optional für Quelltextzeilen)
* Ausgabe: HTML/XML/CSV-Coverage *nur für Integrationstests*.

**Zusammenführen mehrerer Durchläufe:**

```bash
# via Maven
mvn jacoco:merge -Djacoco.destFile=target/merged.exec \
  -Djacoco.dataFileList="target/jacoco.exec,target/jacoco-it.exec,other.exec"
# dann
mvn jacoco:report -Djacoco.dataFile=target/merged.exec
```

# Praktische Fallstricke und Tipps

* **Builds abgleichen**: Generieren Sie Berichte mit **denselben kompilierten Klassen**, die die `.exec`-Datei erzeugt haben.
* **Parallele Forks**: Wenn Sie Tests parallel oder in mehreren JVMs ausführen, vermeiden Sie viele Schreiber auf dieselbe Datei, es sei denn, `append=true` ist gesetzt und Sie sind mit gleichzeitigem Anhängen einverstanden (sicherer ist eine Datei pro JVM und dann Zusammenführen).
* **Langlebige Services**: Aktivieren Sie **TCP/JMX** oder rufen Sie die Runtime-API auf, um **periodisch ein Dump** zu machen; warten Sie nicht auf das Prozessende.
* **Classloader-Isolation**: Einige App-Server laden dieselbe Klasse zweimal; JaCoCo dedupliziert nach Klassen-ID, aber seien Sie sich dessen in komplexen Containern bewusst.
* **Offline Instrumentation** existiert, aber der **Javaagent**-Ansatz ist normalerweise einfacher und robuster.

---

## Direkte Antworten auf Ihre Fragen

* **"Was ist `jacoco-it.exec`?"**
  Die Ausführungsdatendatei (Probe Hits), die während **Integrationstests** erfasst wird. Es ist nur eine Namenskonvention; funktional hat sie dasselbe Format wie `jacoco.exec`.

* **"Enthält sie Klassenstrukturinformationen?"**
  **Nein.** Sie speichert nur **Probe-Hit-Arrays** pro Klasse und Session-Metadaten. Klassen-/Methoden-/Zeilennummern-Informationen kommen von Ihren kompilierten Klassen/Quelltexten während des Berichtsschritts.

* **"Wird sie aktualisiert, wenn sie via `-javaagent` angehängt wird?"**
  **Ja.** Mit `output=file` schreibt der Agent beim **JVM-Exit** oder **auf Anfrage** (TCP/JMX/API). Mit `append=true` **führt er sie** mit einer bestehenden Datei zusammen; ohne überschreibt er sie. Für Multi-JVM-Läufe verwenden Sie separate Dateien oder ein Remote-Dump und **führen sie** später zusammen.