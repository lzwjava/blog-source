---
audio: false
generated: true
image: false
lang: de
layout: post
title: Erklärte JaCoCo-Abdeckungsmetriken
translated: true
type: note
---

Ja — **JaCoCo bietet mehrere Ebenen von Coverage-Metriken**, einschließlich der von Ihnen genannten:

* **File/Class Coverage**
  Verfolgt die Abdeckung auf Klassenebene und zeigt, wie viel jeder Klasse während der Tests ausgeführt wurde.

* **Package Coverage**
  Aggregiert die Abdeckung über alle Klassen in einem Package, sodass Sie die Testabdeckung für übergeordnete Module sehen können.

* **Method/Function Coverage**
  Misst, ob einzelne Methoden (Funktionen) aufgerufen wurden und ob ihre Anweisungen/Zweige abgedeckt wurden.

* **Instruction & Branch Coverage**
  Auf der granularsten Ebene zeigt es, welche Bytecode-Anweisungen und bedingten Zweige ausgeführt wurden.

Wenn Sie einen JaCoCo HTML-Bericht generieren, sehen Sie typischerweise eine Baumansicht:

* Oberster Knoten = gesamte Projektabdeckung.
* Darunter = Abdeckung pro Package.
* Dann = Abdeckung pro Klasse.
* Innerhalb jeder Klasse = Abdeckung pro Methode, mit zeilenweiser Hervorhebung.

👉 Zurück zu Ihrer Frage: Ja, JaCoCo unterstützt **File (Class), Package und Function (Method) Coverage** sofort einsatzbereit.

Möchten Sie, dass ich **erläutere, wie JaCoCo jede Metrik berechnet** (z.B. Unterschied zwischen Instruction, Branch, Line, Method Coverage), damit Sie ein klareres Bild davon bekommen, was tatsächlich gemessen wird?