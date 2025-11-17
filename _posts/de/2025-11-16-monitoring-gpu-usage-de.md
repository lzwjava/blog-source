---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Überwachung der GPU-Nutzung mit nvidia-smi
translated: true
type: note
---

Um die GPU-Auslastung im Zeitverlauf mit `nvidia-smi` zu beobachten, benötigen Sie nur die Loop-Option:

**Grundlegendes Live-Update**

```
nvidia-smi -l 1
```

Dies aktualisiert die Anzeige jede 1 Sekunde. Sie können die `1` durch ein beliebiges Intervall in Sekunden ersetzen.

**Wenn Sie detailliertere Statistiken möchten (Prozess-Auslastung)**

```
nvidia-smi pmon -s um -d 1
```

Dies zeigt die GPU-Auslastung (`u`) und Speichernutzung (`m`) pro Prozess jede Sekunde an.

**Wenn Sie vollständige GPU-Statistiken in Wiederholung möchten**

```
nvidia-smi --query-gpu=timestamp,utilization.gpu,utilization.memory,memory.used,memory.total --format=csv -l 1
```

Dies gibt jede Sekunde eine kompakte Zeile mit Auslastung und Speicherinformationen aus.

Lassen Sie mich wissen, wenn Sie die Ausgabe in einer Datei protokollieren möchten oder ein benutzerdefiniertes Format benötigen.