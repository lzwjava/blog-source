---
audio: false
generated: false
lang: de
layout: post
title: Maximale Ausführungszeit eines GitHub Actions Jobs
translated: true
---

Ich habe GitHub Actions verwendet, um die Übersetzung meiner Blogbeiträge zu automatisieren. Anfangs habe ich versucht, alle Beiträge in einem einzigen Job zu übersetzen, wobei die Änderungen erst dann zurück in das Repository übertragen wurden, nachdem alle Übersetzungen abgeschlossen waren.

Ich war optimistisch und ging schlafen, in der Erwartung, dass der Prozess abgeschlossen sein würde. Doch nach 8 Stunden wachte ich auf und stellte den folgenden Fehler fest:

> Der auf Runner GitHub Actions 12 ausgeführte Job hat die maximale Ausführungszeit von 360 Minuten überschritten.

Das bedeutete, dass die 6 Stunden Übersetzungsarbeit verloren gingen, da der Commit erst am Ende erfolgte.

Um dies zu beheben, habe ich den Workflow so angepasst, dass Änderungen alle 10 Dateien committet werden.

Darüber hinaus habe ich Multithread-Programmierung implementiert, um die gesamte Übersetzungszeit von 6 Stunden auf etwa eine Stunde zu reduzieren.

GitHub Actions bietet eine große Flexibilität. Es unterstützt mehrere Workflow-Jobs, was die Trennung von Aufgaben ermöglicht. Einige Jobs können bei jedem Commit ausgelöst werden, während andere durch verschiedene Ereignisse ausgelöst werden können.