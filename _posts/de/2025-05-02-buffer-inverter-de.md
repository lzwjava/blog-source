---
audio: false
generated: true
lang: de
layout: post
title: Puffer- und Inverter-Schaltungen
translated: true
type: note
---

Hier ist ein Tutorial zu Buffer- und Inverter-Schaltungen basierend auf dem bereitgestellten YouTube-Video:

### Grundlegendes zu Transistorschaltungen

* Das Video untersucht zwei Transistorschaltungen mit Eingängen und Ausgängen, wobei der Schwerpunkt auf der Spannung liegt.
* Transistoren fungieren als Stromschalter; eine positive Eingangsspannung (z.B. +5V) erzeugt Strom und schaltet den Transistor ein. Null Volt bedeuten keinen Strom, und der Transistor ist ausgeschaltet.
* Eingänge und Ausgänge werden im Hinblick auf Einsen und Nullen diskutiert, wobei 0 für 0V und 1 für +5V steht.

### Schaltung 1: Emitterfolger / Buffer

* **Eingang ist 0 (0V):** Der Transistor ist ausgeschaltet, und der Ausgang ist über einen Widerstand mit Masse verbunden, was zu einem Ausgang von 0 führt.
* **Eingang ist 1 (+5V):** Strom fließt, und der Ausgang ist direkt mit +5V verbunden, sodass der Ausgang 1 ist.
* Diese Schaltung wird als **Emitterfolger** bezeichnet, weil der Emitter der Basis (dem Eingang) folgt.
* Ein anderer Name dafür ist **Buffer**, der die gleiche Spannungsebene wie der Eingang ausgibt.
* Der Buffer wird in digitalen Logikschaltbildern durch ein Dreieck symbolisiert.

### Schaltung 2: Inverter

* **Eingang ist 0:** Es fließt kein Strom, der Transistor ist ausgeschaltet, und der Ausgang ist über einen Pull-up-Widerstand mit +5V verbunden, sodass der Ausgang 1 ist.
* **Eingang ist 1:** Strom fließt, verbindet den Ausgang mit Masse, was zu einem Ausgang von 0 führt.
* Diese Schaltung ist als **Inverter** bekannt.
* Das Logiksymbol des Inverters ähnelt einem Buffer, hat jedoch eine Blase am Ausgang, was die Inversion anzeigt.
* Eine Inverterschaltung gibt das Gegenteil des Eingangs aus.

Zusammenfassend erklärt das Video, wie Transistorschaltungen als Buffer, der das Eingangssignal beibehält, oder als Inverter, der das Eingangssignal umkehrt, fungieren können.
http://googleusercontent.com/youtube_content/0