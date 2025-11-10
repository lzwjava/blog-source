---
audio: false
generated: true
image: false
lang: de
layout: post
title: Konfiguration des JaCoCo-Agent-Ausgabeverzeichnisses
translated: true
type: note
---

Ja — genau 👍.

Standardmäßig wird, wenn Sie

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=jacoco.exec,output=file
```

schreiben, die Datei `jacoco.exec` im **aktuellen Arbeitsverzeichnis** des JVM-Prozesses erstellt (oft das Server-Stammverzeichnis oder von wo aus Sie Liberty gestartet haben).

Wenn Sie kontrollieren möchten, wo sie erstellt wird, geben Sie einen **absoluten oder relativen Pfad** an, zum Beispiel:

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=/opt/coverage-data/jacoco.exec,output=file
```

oder

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=target/jacoco.exec,output=file
```

(wobei `target/` relativ zum Startverzeichnis ist).

Also ja, wenn Sie sicherstellen möchten, wo die `.exec`-Datei landet, verwenden Sie den vollständigen Pfad.

👉 Tipp: In Maven/Gradle-Projekten ist es üblich, sie in `target/` (Maven) oder `build/` (Gradle) zu speichern, damit die Berichts-Plugins sie später automatisch finden können.

Soll ich Ihnen ein Liberty `jvm.options`-Beispiel mit konfiguriertem vollständigen Pfad zeigen?