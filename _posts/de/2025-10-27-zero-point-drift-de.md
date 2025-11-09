---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Nullpunktsdrift in der Elektronik
translated: true
type: note
---

### Nullpunktdrift: Definition und Erklärung

Nullpunktdrift (auch als Offset-Drift oder DC-Offset-Drift bezeichnet) ist ein Fehler in elektronischen Schaltungen, Sensoren oder Messsystemen, bei dem der Ausgang eine unbeabsichtigte Offset-Spannung oder ein unbeabsichtigtes Signalniveau erzeugt – selbst wenn der Eingang exakt null ist. Dies führt zu einem "unerwünschten Ausgangsoffset bei Null-Eingang", der die Basislinie vom idealen Nullpunkt verschiebt. Es ist wie eine Waage, die langsam "1 kg" anzeigt, wenn nichts darauf liegt; die Anzeige driftet über die Zeit oder unter verschiedenen Bedingungen.

#### Wichtige Merkmale
- **Manifestation**: Die Ausgabe kehrt ohne Eingangssignal nicht zum wahren Nullpunkt zurück, was kumulative Fehler in mehrstufigen Systemen (z.B. Verstärkern) verursacht, bei denen kleine Offsets verstärkt werden.
- **Häufig in**: Operationsverstärkern (Op-Amps), Instrumentenverstärkern, Thermoelementen, Dehnungsmessstreifen und direktgekoppelten Schaltungen (keine Kondensatoren zur DC-Blockierung).
- **Messung**: Oft quantifiziert in μV/°C (Volt pro Grad Celsius) für thermische Drift oder ppm/°C für relative Änderungen.

#### Hauptursachen
- **Temperaturschwankungen**: Häufigste Ursache; Transistor- oder Widerstandsparameter (z.B. Basis-Emitter-Spannung) ändern sich mit der Temperatur, was zu Bias-Verschiebungen führt.
- **Bauteilalterung**: Allmähliche Verschlechterung von Halbleitern oder passiven Bauteilen über die Zeit.
- **Netzteilschwankungen**: Instabile Spannungswelligkeiten, die die Bias-Punkte beeinflussen.
- **Parameterabweichungen**: In mehrstufigen Verstärkern verstärken leichte Unterschiede in Transistorverstärkungen oder Widerständen die Offsets.

#### Auswirkungen und Gegenmaßnahmen
- **Auswirkung**: Verzerrt Signalschwankungen, verringert die Genauigkeit in Präzisionsanwendungen wie medizinischen Geräten oder Audio (z.B. Brummen oder Summen bei "Stille").
- **Lösungen**:
  - Auto-Zero- oder Chopper-Stabilisierungsschaltungen, um Offsets periodisch zurückzusetzen.
  - Abgeglichene Bauteile oder Trimmpotentiometer zur Kalibrierung.
  - Temperaturkompensation (z.B. mit Thermistoren).
  - AC-Kopplung zur DC-Blockierung in nicht-DC-Anwendungen.

In direktgekoppelten mehrstufigen Verstärkern (wie zuvor besprochen) ist es besonders tückisch, weil DC-Signale alle Stufen durchlaufen und winzige Drifts verstärken.

[Zero Drift Amplifiers Explained](https://www.analog.com/en/resources/analog-dialogue/articles/zero-drift-amplifiers.html)  
[Offset Drift in Op-Amps](https://www.ti.com/lit/an/sboa275/sboa275.pdf)  
[Wikipedia: Offset (electronics)](https://en.wikipedia.org/wiki/Offset_(electronics))