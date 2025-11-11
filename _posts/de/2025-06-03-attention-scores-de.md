---
audio: false
generated: true
lang: de
layout: post
title: Stabilisierung der Aufmerksamkeitswerte in Transformatoren
translated: true
type: note
---

Die Division durch die Quadratwurzel der Schlüsseldimension, \\(\sqrt{d_k}\\), im Skalierten Dot-Product Attention-Mechanismus (wie in der Formel \\(\text{Scaled Scores} = \frac{Q K^T}{\sqrt{d_k}}\\) dargestellt) ist eine bewusste Entscheidung, um Gradienten zu stabilisieren und große Werte zu verhindern, insbesondere im Kontext von Transformern. Hier ist der Grund, warum \\(\sqrt{d_k}\\) anstelle von nur \\(d_k\\) verwendet wird:

1.  **Varianz des Skalarprodukts**:
    - Das Skalarprodukt \\( Q K^T \\) berechnet die Ähnlichkeit zwischen Query- (\\( Q \\)) und Key-Vektoren (\\( K \\)), wobei jeder Vektor die Dimension \\( d_k \\) hat. Wenn angenommen wird, dass die Elemente von \\( Q \\) und \\( K \\) unabhängig sind und einen Mittelwert von 0 und eine Varianz von 1 haben (häufig nach der Initialisierung oder Normalisierung), dann hat das Skalarprodukt \\( Q_i \cdot K_j \\) (für ein einzelnes Paar von Query- und Key-Vektoren) eine Varianz von \\( d_k \\). Dies liegt daran, dass die Varianz der Summe von \\( d_k \\) unabhängigen Produkten zweier standardnormalverteilter Variablen linear mit \\( d_k \\) skaliert.
    - Ohne Skalierung wächst die Größenordnung von \\( Q K^T \\) mit \\( d_k \\), was zu sehr großen Werten für große \\( d_k \\) führt (üblich in Transformern, wo \\( d_k \\) 64, 128 oder größer sein könnte). Große Werte in den Attention-Scores können Probleme verursachen, wenn sie durch die Softmax-Funktion geleitet werden.

2.  **Softmax-Stabilität**:
    - Die Attention-Scores \\( \frac{Q K^T}{\sqrt{d_k}} \\) werden in eine Softmax-Funktion eingespeist, um die Attention-Gewichte zu berechnen. Wenn die Scores zu groß sind (wie es ohne Skalierung oder mit unzureichender Skalierung der Fall wäre), kann die Softmax-Funktion sehr spitze Verteilungen erzeugen, bei denen ein Element dominiert (nahe 1) und andere nahe 0 liegen. Dies führt zu verschwindenden Gradienten für die meisten Elemente, was es dem Modell erschwert, effektiv zu lernen.
    - Die Division durch \\(\sqrt{d_k}\\) stellt sicher, dass die Varianz der skalierten Scores ungefähr 1 beträgt. Dies hält die Scores in einem Bereich, in dem die Softmax-Funktion sich gut verhält, wodurch ausgewogenere Attention-Gewichte und stabile Gradienten erzeugt werden.

3.  **Warum nicht \\( d_k \\)?**:
    - Eine Division durch \\( d_k \\) anstelle von \\(\sqrt{d_k}\\) würde das Skalarprodukt übermäßig skalieren und die Varianz der Scores auf \\( \frac{1}{d_k} \\) reduzieren. Für große \\( d_k \\) würden dies die Scores sehr klein machen, was dazu führen würde, dass die Softmax-Funktion nahezu gleichmäßige Verteilungen erzeugt (da kleine Eingaben für Softmax zu Ausgaben nahe \\( \frac{1}{n} \\) führen). Dies würde die Fähigkeit des Attention-Mechanismus, sich auf relevante Keys zu konzentrieren, verwässern, da die Unterschiede zwischen den Scores verringert würden.
    - Eine Über-Skalierung mit \\( d_k \\) könnte in einigen Fällen auch zu numerischer Instabilität führen, da sehr kleine Werte in der Gleitkomma-Arithmetik möglicherweise schwerer präzise zu handhaben sind.

4.  **Warum \\(\sqrt{d_k}\\)?**:
    - Die Division durch \\(\sqrt{d_k}\\) normalisiert die Varianz des Skalarprodukts auf ungefähr 1, da \\( \text{Var}\left(\frac{Q K^T}{\sqrt{d_k}}\right) = \frac{\text{Var}(Q K^T)}{d_k} = \frac{d_k}{d_k} = 1 \\). Dies hält die Scores in einem vernünftigen Bereich und stellt sicher, dass die Softmax-Funktion aussagekräftige Attention-Gewichte erzeugt, ohne übermäßig spitz oder übermäßig gleichmäßig zu sein.
    - Die Quadratwurzel ergibt sich natürlich aus der mathematischen Eigenschaft der Varianz des Skalarprodukts. Sie schafft einen Ausgleich zwischen der Verhinderung explodierender Werte (was ohne Skalierung passieren würde) und der Vermeidung einer übermäßigen Unterdrückung der Scores (was mit \\( d_k \\) passieren würde).

5.  **Empirische Wirksamkeit**:
    - Die Wahl von \\(\sqrt{d_k}\\) wurde im ursprünglichen Transformer-Paper ("Attention is All You Need" von Vaswani et al., 2017) eingeführt und wurde in vielen transformer-basierten Modellen empirisch validiert. Sie funktioniert in der Praxis gut für eine große Bandbreite von \\( d_k \\)-Werten und gewährleistet stabiles Training und gute Leistung.

Zusammenfassend ist die Division durch \\(\sqrt{d_k}\\) eine mathematisch motivierte Wahl, die die Varianz der Attention-Scores stabilisiert, sicherstellt, dass die Softmax-Funktion in einem wohldefinierten Bereich arbeitet, und die Probleme sowohl explodierender als auch verschwindender Gradienten vermeidet. Eine Division durch \\( d_k \\) würde die Scores übermäßig reduzieren, was zu weniger unterscheidungsfähigen Attention-Gewichten führen und die Modellleistung potenziell beeinträchtigen würde.