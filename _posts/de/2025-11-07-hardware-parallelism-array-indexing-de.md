---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Hardware-Parallelismus beschleunigt Array-Indizierung
translated: true
type: note
---

### Warum ist Indizierung schneller als binäre Suche?

Dieser Blogbeitrag von Yin Wang aus dem Jahr 2013 untersucht den grundlegenden Grund, warum das direkte Indizieren eines Arrays (z.B. `arr[i]`) konstantzeitlich O(1) ist, während die binäre Suche in einem sortierten Array O(log n) Zeit benötigt. Er erklärt dies auf der Hardware-Ebene anhand einer einfachen Schaltkreis-Analogie und zeigt, dass Indizierung keine "Magie" ist – es ist lediglich eine massiv parallele binäre Suche, die in das Adressierungssystem des Computers eingebaut ist.

#### Wichtige Erklärung
- **Die Kernidee**: Das Indizieren eines Arrays verwendet einen **Adressierschaltkreis**, um einen Speicherort direkt aus einer Adresse (wie einem Index) auszuwählen. Für ein kleines Beispiel mit 4 Speicherorten (W, X, Y, Z) und einer 2-Bit-Adresse (Bits A und B):
  - Jedes Adress-Bit wirkt wie ein Schritt einer binären Suche, der die möglichen Auswahlen halbiert.
  - Bit A entscheidet zwischen zwei Gruppen: {W, X} oder {Y, Z}.
  - Bit B entscheidet zwischen einer weiteren Aufteilung: {W, Y} oder {X, Z}.
  - Diese Bits laufen nicht sequentiell ab – sie arbeiten **parallel** und verwenden UND-Gatter und Leitungen, um Signale zu kombinieren und genau eine Ausgabe auszuwählen (z.B. wenn A=0, B=1 → Wählen von W).

  Dies ahmt 2 Schritte der binären Suche (log₂(4) = 2) nach, wird aber in einem einzigen Hardware-"Takt" abgeschlossen, da alles gleichzeitig geschieht.

- **Hochskalierung**: Für eine vollständige n-Bit-Adresse (die 2ⁿ Elemente handhabt), führt der Schaltkreis alle log₂(n) Schritte der binären Suche parallel aus. Deshalb ist es O(1): Die Hardware führt die "Suche" sofort durch, ohne Schleifen oder Vergleiche in der Software.

- **Visuelle Hilfe**: Der Beitrag enthält ein Diagramm des Schaltkreises mit Invertern, Leitungen und UND-Gattern, die den Signalfluss zeigen. Es gibt keine Code-Ausschnitte, aber es ist konzeptionell – man kann es sich als einen Decoder vorstellen, der binäre Adressen in eine One-Hot-Auswahl umwandelt.

#### Warum das wichtig ist
Wang argumentiert, dass dies zeigt, wie Low-Level-Hardware-Optimierungen High-Level-Operationen mühelos erscheinen lassen. Die binäre Suche ist nur deshalb "langsam", weil sie diesen Schaltkreis sequentiell in Software nachahmt; der tatsächliche Speicherzugriff der CPU ist die parallele Version.

Es ist eine kurze, aufschlussreiche Lektüre für alle, die sich für CS-Grundlagen jenseits der Big-O-Notation interessieren.

[Warum ist Indizierung schneller als binäre Suche](https://yinwang0.wordpress.com/2013/04/02/indexing/)