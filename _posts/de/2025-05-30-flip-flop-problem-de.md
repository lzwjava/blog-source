---
audio: false
generated: true
lang: de
layout: post
title: JK-Flipflop-Experiment und Zustandstabelle
translated: true
type: note
---

**42. JK-Flipflop-Experiment – Einzeltakt-Trigger-Takt**
- **Ziel**: Verständnis des Arbeitsprinzips und der Eigenschaften eines JK-Flipflops.
- **Ausrüstung**: JK-Flipflop-Modul, Impulsgenerator, Stromversorgung, Verbindungskabel usw.

**Abbildung 42 Zustandsübergangstabelle**

| Q₂ⁿ | Q₁ⁿ | Q₀ⁿ | Q₂ⁿ⁺¹ | Q₁ⁿ⁺¹ | Q₀ⁿ⁺¹ | Z |
|-----|-----|-----|-------|-------|-------|---|
| 0   | 0   | 0   | 0     | 0     | 1     | 0 |
| 0   | 0   | 1   | 0     | 1     | 0     | 0 |
| 0   | 1   | 0   | 0     | 1     | 1     | 0 |
| 0   | 1   | 1   | 1     | 0     | 0     | 0 |
| 1   | 0   | 0   | 0     | 0     | 0     | 1 |

### Antwort:
Die Tabelle stellt den Zustandsübergang eines 3-Bit-JK-Flipflops dar, wobei Q₂ⁿ, Q₁ⁿ und Q₀ⁿ die aktuellen Zustände sind und Q₂ⁿ⁺¹, Q₁ⁿ⁺¹ und Q₀ⁿ⁺¹ die nächsten Zustände nach einem Taktimpuls. Der Ausgang Z ist nur dann 1, wenn der aktuelle Zustand 100 ist, was eine spezifische Bedingung oder ein Ausgangssignal anzeigt. Dieses Verhalten ist typisch für ein JK-Flipflop, das seinen Zustand basierend auf den Eingängen (J und K) und dem Taktimpuls halten, setzen, zurücksetzen oder toggeln kann.

Lassen Sie uns die JK-Flipflop-Zustandsübergangstabelle aufschlüsseln und ihr Verhalten im Detail erklären.

### Überblick über ein JK-Flipflop
Ein JK-Flipflop ist eine Art sequenzieller Logikschaltung, die in der Digitaltechnik verwendet wird, um ein einzelnes Bit zu speichern. Es hat zwei Eingänge, J und K, einen Takteingang (CLK) und zwei Ausgänge, Q (der aktuelle Zustand) und Q' (das Komplement von Q). Das JK-Flipflop ist eine Verbesserung gegenüber dem SR-Flipflop, da es den "ungültigen" Zustand (wenn beide Eingänge 1 sind) eliminiert. Sein Verhalten ist wie folgt:

- **J = 0, K = 0**: Keine Änderung (Q bleibt gleich).
- **J = 0, K = 1**: Rücksetzen (Q wird 0).
- **J = 1, K = 0**: Setzen (Q wird 1).
- **J = 1, K = 1**: Toggle (Q wechselt in den entgegengesetzten Zustand).

Die Tabelle im Bild repräsentiert ein System mit drei JK-Flipflops (Q₂, Q₁, Q₀), die einen 3-Bit-Zustandsautomaten bilden, wobei Q₂ⁿ, Q₁ⁿ und Q₀ⁿ die aktuellen Zustände sind und Q₂ⁿ⁺¹, Q₁ⁿ⁺¹ und Q₀ⁿ⁺¹ die nächsten Zustände nach einem Taktimpuls. Z ist ein Ausgangssignal, das auf dem aktuellen Zustand basiert.

### Erklärung der Zustandsübergangstabelle
Die Tabelle zeigt, wie das System zwischen Zuständen wechselt und wann der Ausgang Z aktiviert wird. Analysieren wir jede Zeile:

| Q₂ⁿ | Q₁ⁿ | Q₀ⁿ | Q₂ⁿ⁺¹ | Q₁ⁿ⁺¹ | Q₀ⁿ⁺¹ | Z |
|-----|-----|-----|-------|-------|-------|---|
| 0   | 0   | 0   | 0     | 0     | 1     | 0 |
| 0   | 0   | 1   | 0     | 1     | 0     | 0 |
| 0   | 1   | 0   | 0     | 1     | 1     | 0 |
| 0   | 1   | 1   | 1     | 0     | 0     | 0 |
| 1   | 0   | 0   | 0     | 0     | 0     | 1 |

#### Zeile 1: Zustand 000 → 001, Z = 0
- **Aktueller Zustand (Q₂ⁿ, Q₁ⁿ, Q₀ⁿ)**: 000 (dezimal 0)
- **Nächster Zustand (Q₂ⁿ⁺¹, Q₁ⁿ⁺¹, Q₀ⁿ⁺¹)**: 001 (dezimal 1)
- **Z-Ausgang**: 0
- **Erklärung**: Das System startet im Zustand 000. Nach einem Taktimpuls toggelt Q₀ von 0 auf 1 (wahrscheinlich weil J₀ = 1, K₀ = 1), während Q₁ und Q₂ 0 bleiben (möglicherweise J₁ = 0, K₁ = 0; J₂ = 0, K₂ = 0). Z ist 0, was darauf hinweist, dass die Ausgangsbedingung nicht erfüllt ist.

#### Zeile 2: Zustand 001 → 010, Z = 0
- **Aktueller Zustand**: 001 (dezimal 1)
- **Nächster Zustand**: 010 (dezimal 2)
- **Z-Ausgang**: 0
- **Erklärung**: Vom Zustand 001 toggelt Q₀ von 1 auf 0 (J₀ = 1, K₀ = 1), Q₁ toggelt von 0 auf 1 (J₁ = 1, K₁ = 1) und Q₂ bleibt 0. Z bleibt 0.

#### Zeile 3: Zustand 010 → 011, Z = 0
- **Aktueller Zustand**: 010 (dezimal 2)
- **Nächster Zustand**: 011 (dezimal 3)
- **Z-Ausgang**: 0
- **Erklärung**: Vom Zustand 010 toggelt Q₀ von 0 auf 1 (J₀ = 1, K₀ = 1), Q₁ bleibt 1 und Q₂ bleibt 0. Z ist immer noch 0.

#### Zeile 4: Zustand 011 → 100, Z = 0
- **Aktueller Zustand**: 011 (dezimal 3)
- **Nächster Zustand**: 100 (dezimal 4)
- **Z-Ausgang**: 0
- **Erklärung**: Vom Zustand 011 toggelt Q₀ von 1 auf 0, Q₁ toggelt von 1 auf 0 und Q₂ toggelt von 0 auf 1 (J₂ = 1, K₂ = 1). Z bleibt 0.

#### Zeile 5: Zustand 100 → 000, Z = 1
- **Aktueller Zustand**: 100 (dezimal 4)
- **Nächster Zustand**: 000 (dezimal 0)
- **Z-Ausgang**: 1
- **Erklärung**: Vom Zustand 100 toggelt Q₂ von 1 auf 0, Q₁ bleibt 0 und Q₀ bleibt 0. Der Ausgang Z ist 1, was darauf hinweist, dass der Zustand 100 die Ausgangsbedingung auslöst (möglicherweise Z = Q₂ UND NICHT Q₁ UND NICHT Q₀).

### Systemverhalten
- **Zustandssequenz**: Das System durchläuft Zustände in dieser Reihenfolge: 000 → 001 → 010 → 011 → 100 → 000 und wiederholt sich. Dies ist eine 5-Zustands-Sequenz (von 8 möglichen Zuständen für 3 Bits), was auf eine spezifische Konfiguration der J- und K-Eingänge für jedes Flipflop hindeutet.
- **Ausgang Z**: Z ist nur 1, wenn der aktuelle Zustand 100 ist. Dies könnte eine Bedingung darstellen, bei der das System den Abschluss eines Zyklus oder ein bestimmtes Ereignis signalisiert (z. B. das Erreichen eines bestimmten Werts in einem Zähler).

### Praktische Interpretation
Dieser JK-Flipflop-Aufbau scheint ein Modulo-5-Zähler zu sein (da er 5 Zustände durchläuft). Der Zähler erhöht sich mit jedem Taktimpuls, und der Ausgang Z signalisiert, wenn der Zustand 100 erreicht wird, bevor er auf 000 zurückgesetzt wird. Solche Schaltungen werden in digitalen Systemen für das Zählen, die Frequenzteilung oder das Erzeugen spezifischer Sequenzen verwendet.

### Zusammenfassung
Die JK-Flipflop-Schaltung in der Tabelle funktioniert als 3-Bit-Zustandsautomat mit einem 5-Zustands-Zyklus (000 → 001 → 010 → 011 → 100 → 000). Der Ausgang Z ist nur im Zustand 100 gleich 1, was wahrscheinlich auf ein bestimmtes Ereignis oder eine Rücksetzbedingung hinweist. Die Übergänge werden durch die J- und K-Eingänge gesteuert, die so konfiguriert sind, dass diese Sequenz erzeugt wird.