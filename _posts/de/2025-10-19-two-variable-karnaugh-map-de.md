---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Karnaugh-Veitch-Diagramm für zwei Variablen Beispiel
translated: true
type: note
---

### Einfaches Karnaugh-Diagramm-Beispiel: 2-Variable Funktion

Verwenden wir eine sehr einfache 2-variable Boolesche Funktion: f(A, B) = A'B + AB' + AB (Summe der Minterme m(1, 2, 3)). Dies ist das ODER-Gatter: f = A + B, aber wir werden das mit einem K-Diagramm "entdecken".

#### Schritt 1: Konstruiere das K-Diagramm
Ein 2-variables K-Diagramm ist ein 2x2-Raster. Zeilen für A (0, 1), Spalten für B (0, 1) in Gray-Code (bereits einfach). Setze 1en für die Minterme:

| A \ B | 0 (B') | 1 (B) |
|-------|--------|-------|
| **0 (A')** | 0 (m0) | 1 (m1) |
| **1 (A)**  | 1 (m2) | 1 (m3) |

#### Schritt 2: Gruppiere benachbarte 1en
Suche nach den größten Gruppen von 1en (Zweierpotenzen: 1, 2, 4...). Benachbart bedeutet, eine Seite zu teilen (keine Diagonalen).

- **Gruppe 1**: Rechte Spalte (m1 und m3) — vertikales Paar. Gemeinsam: B (A variiert, also egal).
- **Gruppe 2**: Untere Zeile (m2 und m3) — horizontales Paar. Gemeinsam: A (B variiert).

(Überlappung bei m3 ist in Ordnung.)

#### Schritt 3: Leite den minimierten Ausdruck ab
Jede Gruppe ergibt einen Term:
- Gruppe 1: **B**
- Gruppe 2: **A**

Minimiert: f = A + B

Dies vereinfacht von 3 Termen (ursprünglich 9 Literale, Moment mal nein: 3 Terme mit je 2 Literalen) auf 2 Terme mit je 1 Literal — weniger Gatter!

Es entspricht der ODER-Funktion. Für noch einfachere Übung, versuche es mit allen 1en: gruppiert zu nur 1 (wahr).

[All About Circuits: Karnaugh Maps](https://www.allaboutcircuits.com/textbook/digital/chpt-7/karnaugh-mapping/)