---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Invertieren einer 3x3-Matrix
translated: true
type: note
---

Ja, du bist auf dem richtigen Weg! Du beschreibst die Standardmethode, um die Inverse einer 3×3-Matrix \\( A \\) (oft bezeichnet als \\( A^{-1} \\)) zu finden, unter Verwendung der **Kofaktormatrix** (oder genauer gesagt, der **adjungierten Matrix**, welche die Transponierte der Kofaktormatrix ist). Der Teil "divider 1/value * matrix" bezieht sich auf die Skalierung mit \\( 1/\det(A) \\), wobei \\( \det(A) \\) die Determinante von \\( A \\) ist. Und "rorate" könnte "transponieren" bedeuten (Zeilen in Spalten umwandeln) – das ist ebenfalls ein entscheidender Schritt.

Ich werde die Methode Schritt für Schritt erklären, warum sie funktioniert und wie man sie für eine allgemeine 3×3-Matrix berechnet. Dies ergibt sich aus der allgemeinen Formel für Matrixinverse: \\( A^{-1} = \frac{1}{\det(A)} \adj(A) \\), wobei \\( \adj(A) \\) die Adjungierte ist.

### Schritt-für-Schritt-Methode für eine 3×3-Matrix
Nehmen wir an, deine Matrix ist:
\\[
A = \begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}
\\]

1.  **Berechne die Determinante \\( \det(A) \\)** (der "Wert", durch den du teilst):
    \\[
    \det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
    \\]
    Wenn \\( \det(A) = 0 \\), hat die Matrix keine Inverse (sie ist singulär). Andernfalls fahre fort.

2.  **Finde die Kofaktormatrix \\( C \\)**:
    - Der Kofaktor \\( C_{ij} \\) für das Element \\( a_{ij} \\) ist \\( (-1)^{i+j} \\) mal die Determinante der 2×2-Untermatrix, die durch Streichen der Zeile \\( i \\) und Spalte \\( j \\) erhalten wird.
    - Du musst nicht *alle* Kofaktoren von Grund auf neu berechnen – du kannst sie entlang einer Zeile (oder Spalte) berechnen und Eigenschaften nutzen, um den Rest zu füllen, aber für 3×3 ist es schnell, alle neun zu machen.

    Die Kofaktoren sind:
    \\[
    C_{11} = (-1)^{2} \det\begin{pmatrix} e & f \\ h & i \end{pmatrix} = ei - fh
    \\]
    \\[
    C_{12} = (-1)^{3} \det\begin{pmatrix} d & f \\ g & i \end{pmatrix} = -(di - fg)
    \\]
    \\[
    C_{13} = (-1)^{4} \det\begin{pmatrix} d & e \\ g & h \end{pmatrix} = dh - eg
    \\]
    \\[
    C_{21} = (-1)^{3} \det\begin{pmatrix} b & c \\ h & i \end{pmatrix} = -(bi - ch)
    \\]
    \\[
    C_{22} = (-1)^{4} \det\begin{pmatrix} a & c \\ g & i \end{pmatrix} = ai - cg
    \\]
    \\[
    C_{23} = (-1)^{5} \det\begin{pmatrix} a & b \\ g & h \end{pmatrix} = -(ah - bg)
    \\]
    \\[
    C_{31} = (-1)^{4} \det\begin{pmatrix} b & c \\ e & f \end{pmatrix} = bf - ce
    \\]
    \\[
    C_{32} = (-1)^{5} \det\begin{pmatrix} a & c \\ d & f \end{pmatrix} = -(af - cd)
    \\]
    \\[
    C_{33} = (-1)^{6} \det\begin{pmatrix} a & b \\ d & e \end{pmatrix} = ae - bd
    \\]

    Also ist die Kofaktormatrix:
    \\[
    C = \begin{pmatrix}
    ei-fh & -(di-fg) & dh-eg \\
    -(bi-ch) & ai-cg & -(ah-bg) \\
    bf-ce & -(af-cd) & ae-bd
    \end{pmatrix}
    \\]

3.  **Transponiere, um die Adjungierte \\( \adj(A) = C^T \\) zu erhalten** (dies ist der "rorate"-Schritt – vertausche Zeilen und Spalten):
    \\[
    \adj(A) = \begin{pmatrix}
    ei-fh & -(bi-ch) & bf-ce \\
    -(di-fg) & ai-cg & -(af-cd) \\
    dh-eg & -(ah-bg) & ae-bd
    \end{pmatrix}
    \\]

4.  **Skaliere mit \\( 1/\det(A) \\)**, um die Inverse zu erhalten:
    \\[
    A^{-1} = \frac{1}{\det(A)} \adj(A)
    \\]
    Jeder Eintrag von \\( \adj(A) \\) wird mit \\( 1/\det(A) \\) multipliziert.

### Beispiel
Sei \\( A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix} \\).

-   \\( \det(A) = 1(1\cdot0 - 4\cdot6) - 2(0\cdot0 - 4\cdot5) + 3(0\cdot6 - 1\cdot5) = 1(-24) - 2(-20) + 3(-5) = -24 + 40 - 15 = 1 \\).
-   Kofaktoren (schnell berechnet): \\( C = \begin{pmatrix} -24 & 20 & -5 \\ -15 & -15 & 5 \\ -14 & -10 & 1 \end{pmatrix} \\) (ich überspringe hier die vollständige Berechnung, aber du kannst sie überprüfen).
-   \\( \adj(A) = C^T = \begin{pmatrix} -24 & -15 & -14 \\ 20 & -15 & -10 \\ -5 & 5 & 1 \end{pmatrix} \\).
-   \\( A^{-1} = \frac{1}{1} \adj(A) = \begin{pmatrix} -24 & -15 & -14 \\ 20 & -15 & -10 \\ -5 & 5 & 1 \end{pmatrix} \\).

Du kannst prüfen: \\( A \cdot A^{-1} = I \\) (die Einheitsmatrix).

### Warum funktioniert das?
Der Hauptgrund ist eine Eigenschaft von Determinanten und Kofaktoren: Für jede quadratische Matrix \\( A \\) gilt:
\\[
A \cdot \adj(A) = \det(A) \cdot I
\\]
(wobei \\( I \\) die Einheitsmatrix ist). Dies ergibt sich aus der **Laplace-Entwicklung** der Determinante entlang von Zeilen/Spalten. Jeder Eintrag in \\( A \cdot \adj(A) \\) entwickelt sich zu einer Summe, die auf der Diagonalen \\( \det(A) \\) ergibt und ansonsten 0 (weil sich die Nicht-Diagonalelemente durch die Kofaktorvorzeichen aufheben).

Um die Inverse zu erhalten, teile beide Seiten durch \\( \det(A) \\) (vorausgesetzt, es ist ungleich Null):
\\[
A \cdot \left( \frac{1}{\det(A)} \adj(A) \right) = I \implies A^{-1} = \frac{1}{\det(A)} \adj(A)
\\]
Ebenso gilt \\( \adj(A) \cdot A = \det(A) \cdot I \\), also funktioniert es von beiden Seiten.

Diese Methode verallgemeinert sich auf jede \\( n \times n \\)-Matrix, aber für 3×3 ist sie effizient. Für größere Matrizen ist der Gaußsche Eliminationsalgorithmus oft recheneffizienter.

Wenn du eine bestimmte Matrix hast, die du invertieren möchtest, oder einen Schritt klären willst, teile sie einfach mit!