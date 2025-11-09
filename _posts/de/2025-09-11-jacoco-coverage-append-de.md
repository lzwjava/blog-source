---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: JaCoCo-Abdeckungsdatei und Anhängemodus
translated: true
type: note
---

Das ist ein subtiler, aber wichtiger Detail in der Funktionsweise von JaCoCo.

### Verhalten von `jacoco:prepare-agent`

* Wenn Maven das Ziel **`prepare-agent`** ausführt, generiert es die Coverage-Datei nicht sofort.
* Stattdessen **konfiguriert es die JVM** (normalerweise über ein `-javaagent:jacocoagent.jar` Argument), sodass Coverage-Daten während der Ausführung Ihrer Tests oder Anwendung gesammelt werden.
* Der Speicherort der `.exec`-Datei wird durch die Property `jacoco.destFile` gesteuert (Standard ist `target/jacoco.exec`, wird aber oft angepasst, z.B. `target/jacoco-it.exec`).

### Was passiert, wenn die Datei bereits existiert?

* Standardmäßig **überschreibt JaCoCo die Datei**, wenn die JVM mit dem Agenten startet.
* Das bedeutet, dass jede Ausführung von `prepare-agent` → Testausführung eine *frische* `.exec`-Datei erzeugt.
* Es wird nicht automatisch angehängt — alte Daten gehen verloren, es sei denn, man konfiguriert es anders.

### Wie man stattdessen anfügt

Wenn Sie möchten, dass mehrere Durchläufe sich in derselben exec-Datei ansammeln, müssen Sie explizit den Append-Modus aktivieren:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <configuration>
    <destFile>${project.build.directory}/jacoco-it.exec</destFile>
    <append>true</append>   <!-- ✅ Coverage-Daten anfügen -->
  </configuration>
</plugin>
```

Mit `<append>true>` werden die neuen Coverage-Daten in die bestehende Datei zusammengeführt, falls sie existiert.

### Kurz gesagt

* **Standard:** Jeder Durchlauf ersetzt die alte `.exec`-Datei.
* **Mit `append=true`:** Coverage von mehreren JVM-Durchläufen (oder mehreren Modulen/Tests) wird in derselben Datei zusammengeführt.

---

Möchten Sie, dass ich auch erkläre, wie dies mit **Multi-Modul Maven Builds** interagiert (bei denen jedes Modul versucht, seine eigene JaCoCo exec-Datei zu schreiben), da dies oft der Grund ist, warum Leute auf Overwrite- vs. Append-Probleme stoßen?