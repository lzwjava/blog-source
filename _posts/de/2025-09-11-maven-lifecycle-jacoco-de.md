---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Verstehen von Maven-Lebenszyklen und JaCoCo
translated: true
type: note
---

Gute Frage – das hängt von Mavens *Lifecycle-Phasen* ab und wie Plugins an diese gebunden werden.

### Grundlagen des Lifecycles

Maven hat drei standardmäßige Lifecycles: `clean`, `default` (manchmal auch *build* genannt) und `site`.
Innerhalb des *default*-Lifecycles laufen die wichtigen Phasen in dieser Reihenfolge ab:

* `validate`
* `compile`
* `test`
* `package`
* `verify`
* `install`
* `deploy`

Jede Phase schließt alle vorherigen ein (wenn Sie `mvn verify` ausführen, führt Maven alles von `validate` bis `verify` aus). Die Ausführung von `mvn package` stoppt nach dem Erstellen des Artifakts (JAR/WAR), und `verify` wird nicht ausgeführt.

### Warum JaCoCo beteiligt ist

Das JaCoCo Maven Plugin bindet typischerweise sein **`prepare-agent`** Goal an die `initialize`- oder `verify`-Phase, abhängig von der Konfiguration.

* Wenn es an `verify` gebunden ist (das gängige Setup für Coverage-Reports), dann wird es durch `mvn verify` ausgelöst.
* `mvn package` gelangt nicht so weit im Lifecycle, daher wird die `verify`-Phase (und damit JaCoCos Schritt) übersprungen.

Deshalb wird JaCoCo ausgeführt, wenn Sie `mvn verify` ausführen, aber nicht bei `mvn package`.

### Praktische Erkenntnis

* Verwenden Sie **`mvn package`**, wenn Sie nur das Build-Artefakt wollen (schnell, ohne zusätzliche Prüfungen).
* Verwenden Sie **`mvn verify`**, wenn Sie *Integrationstests, Prüfungen, Coverage-Reports oder QA-Plugins* ausführen möchten, die an spätere Phasen gebunden sind.

👉 Wenn Sie möchten, dass JaCoCo auch bei `mvn package` immer ausgeführt wird, können Sie das `prepare-agent`-Goal in Ihrer `pom.xml` an eine frühere Phase wie `test` oder `package` binden.

Möchten Sie, dass ich Ihnen einen konkreten `pom.xml`-Ausschnitt zeige, der JaCoCos `prepare-agent` bereits bei `test` statt bei `verify` ausführen lässt?