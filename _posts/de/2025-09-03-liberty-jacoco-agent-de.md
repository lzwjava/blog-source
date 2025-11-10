---
audio: false
generated: true
image: false
lang: de
layout: post
title: Vergleich von Liberty Agent und JaCoCo Agent
translated: true
type: note
---

In WebSphere Liberty (WLP) ist das `ws-javaagent.jar` der eigene Java-Instrumentierungs-Agent von IBM. Er wird hauptsächlich für Runtime-Monitoring, Diagnose und die Integration mit Tools wie Application Performance Management (APM), Health Center oder den eigenen Monitoring-Fähigkeiten von Liberty verwendet. Wenn Sie ihn aktivieren, kann Liberty automatisch Profiling-, Garbage Collection-, Thread- und andere JVM-Level-Metriken sammeln.

JaCoCos `jacocoagent.jar` ist hingegen speziell ein **Code-Coverage-Agent**. Sein Zweck ist es, Bytecode zur Laufzeit zu instrumentieren, damit Testläufe oder Applikationsausführungen Coverage-Daten erzeugen (z.B. welche Klassen, Methoden und Branches ausgeführt wurden).

Die Unterscheidung ist also:

* **`ws-javaagent.jar`** → Allgemeines Monitoring, Profiling, Diagnose für Liberty und IBM-Tooling.
* **`jacocoagent.jar`** → Test-/Code-Coverage-Berichterstattung, unabhängig von Liberty.

Sie sollten den JaCoCo-Agenten nicht durch den von Liberty ersetzen. Wenn Ihr Ziel **Test-Coverage-Berichterstattung** ist (für CI-Pipelines, SonarQube, Maven/Gradle-Reports, etc.), müssen Sie den **JaCoCo-Agenten** weiterverwenden. Der Liberty-Agent wird keine JaCoCo `.exec` Coverage-Dateien erzeugen.

Sie können jedoch bei Bedarf *beide* gleichzeitig ausführen – Java unterstützt mehrere `-javaagent`-Argumente. Zum Beispiel:

```bash
-javaagent:/path/to/ws-javaagent.jar
-javaagent:/path/to/jacocoagent.jar=destfile=jacoco.exec,output=file
```

👉 Kurz gesagt:
Verwenden Sie **`jacocoagent.jar`** für Coverage.
Verwenden Sie **`ws-javaagent.jar`**, wenn Sie Liberty-Diagnose/Profiling benötigen.
Sie erfüllen unterschiedliche Zwecke und sind nicht austauschbar.

Möchten Sie, dass ich Ihnen auch zeige, wie man beide zusammen in einer Liberty-Server-JVM-Options-Datei konfiguriert?