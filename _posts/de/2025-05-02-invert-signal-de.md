---
audio: false
generated: true
lang: de
layout: post
title: Signal invertieren
translated: true
type: note
---

Hier ist ein umfassendes Tutorial basierend auf dem Video:

Der Ersteller modifiziert eine Transistorschaltung wie folgt, um ein Signal zu invertieren:

1.  Das Video beginnt mit zwei identischen Transistorschaltungen, die parallel geschaltet sind. Jede Schaltung hat eine Stromversorgung, eine LED, einen Widerstand und einen Transistor. Ein Signal von einem "mystery device" ist mit der Basis beider Transistoren verbunden, wodurch diese ihre LEDs ein- und ausschalten.
2.  Die LED wird aus der oberen Schaltung entfernt, sodass nur der Widerstand, der Transistor und die Verbindungen zur Stromversorgung und Masse übrig bleiben. Auch ohne visuelle Ausgabe schaltet der Transistor weiterhin basierend auf dem Signal.
3.  Die Spannung an einem bestimmten Punkt (Punkt A) in der modifizierten Schaltung wird erklärt:
    * Wenn der Transistor ausgeschaltet ist, liegt Punkt A auf 5 Volt relativ zu Masse.
    * Wenn der Transistor eingeschaltet (gesättigt) ist, liegt Punkt A auf 0 Volt relativ zu Masse.
4.  Eine LED wird dann zwischen Kollektor und Emitter des Transistors in der modifizierten Schaltung angeschlossen. Diese neue LED verhält sich umgekehrt zur ursprünglichen LED in der unteren Schaltung: wenn die ursprüngliche LED an ist, ist die neue LED aus, und umgekehrt.
5.  Eine Analogie mit einer Batterie, einem Widerstand, einer LED und einem Schalter wird verwendet, um diese Inversion zu erklären. Wenn der Schalter aus (offen) ist, leuchtet die LED. Wenn der Schalter an (geschlossen) ist, überbrückt er die LED und schaltet sie aus.
6.  Der Transistor fungiert als Schalter. Wenn der Transistor ausgeschaltet ist, fließt Strom durch die LED und schaltet sie ein. Wenn der Transistor eingeschaltet ist, erzeugt er einen Kurzschluss, der die LED überbrückt und sie ausschaltet.

Zusammenfassend lässt sich sagen, dass durch den Anschluss einer LED in dieser Konfiguration die Schaltung in der Lage ist, das Eingangssignal zu invertieren.
http://googleusercontent.com/youtube_content/0