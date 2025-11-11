---
audio: false
generated: true
lang: de
layout: post
title: Quadratische Form
translated: true
type: note
---

In der linearen Algebra ist eine **quadratische Form** eine Funktion $Q: \mathbb{R}^n \rightarrow \mathbb{R}$, die ausgedrückt werden kann als:

$Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$

wobei:
* $\mathbf{x}$ ein Spaltenvektor in $\mathbb{R}^n$ ist:
    $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}$
* $A$ eine $n \times n$ symmetrische Matrix mit reellen Einträgen ist. Diese Matrix wird die **Matrix der quadratischen Form** genannt.
* $\mathbf{x}^T$ die Transponierte von $\mathbf{x}$ ist, also ein Zeilenvektor.

**Einfacher ausgedrückt:**

Eine quadratische Form ist ein homogenes Polynom zweiten Grades in $n$ Variablen. "Homogen" bedeutet, dass jeder Term im Polynom den Gesamtgrad zwei hat.

Zum Beispiel sieht eine quadratische Form in zwei Variablen ($n=2$) so aus:
$Q(x_1, x_2) = a x_1^2 + b x_1 x_2 + c x_2^2$

Dies kann in Matrixform geschrieben werden als:
$Q(x_1, x_2) = \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} a & b/2 \\ b/2 & c \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$

Beachten Sie, dass die Nicht-Diagonaleinträge der Matrix $A$ die Hälfte des Koeffizienten des gemischten Terms ($x_1 x_2$) sind. Wir verwenden eine symmetrische Matrix $A$, weil für jede Matrix $B$ gilt: $\mathbf{x}^T B \mathbf{x} = \mathbf{x}^T \left( \frac{B + B^T}{2} \right) \mathbf{x}$, und $\frac{B + B^T}{2}$ immer eine symmetrische Matrix ist. Die Verwendung der symmetrischen Form vereinfacht viele Eigenschaften und Theoreme im Zusammenhang mit quadratischen Formen.

**Wesentliche Aspekte quadratischer Formen:**

* **Matrixdarstellung:** Jede quadratische Form kann eindeutig durch eine symmetrische Matrix dargestellt werden.
* **Auswertung:** Der Wert der quadratischen Form $Q(\mathbf{x})$ ist ein Skalar, der durch die Matrixmultiplikation $\mathbf{x}^T A \mathbf{x}$ erhalten wird.
* **Klassifikation:** Quadratische Formen können basierend auf den Werten, die sie für nicht-null Vektoren $\mathbf{x}$ annehmen, klassifiziert werden:
    * **Positiv definit:** $Q(\mathbf{x}) > 0$ für alle $\mathbf{x} \neq \mathbf{0}$. Dies tritt genau dann auf, wenn alle Eigenwerte von $A$ positiv sind.
    * **Positiv semidefinit:** $Q(\mathbf{x}) \ge 0$ für alle $\mathbf{x}$. Dies tritt genau dann auf, wenn alle Eigenwerte von $A$ nicht-negativ sind.
    * **Negativ definit:** $Q(\mathbf{x}) < 0$ für alle $\mathbf{x} \neq \mathbf{0}$. Dies tritt genau dann auf, wenn alle Eigenwerte von $A$ negativ sind.
    * **Negativ semidefinit:** $Q(\mathbf{x}) \le 0$ für alle $\mathbf{x}$. Dies tritt genau dann auf, wenn alle Eigenwerte von $A$ nicht-positiv sind.
    * **Indefinit:** $Q(\mathbf{x})$ nimmt sowohl positive als auch negative Werte an. Dies tritt genau dann auf, wenn $A$ sowohl positive als auch negative Eigenwerte hat.
* **Variablenwechsel:** Durch einen linearen Variablenwechsel $\mathbf{x} = P\mathbf{y}$, wobei $P$ eine invertierbare Matrix ist, kann die quadratische Form in eine neue quadratische Form in Bezug auf $\mathbf{y}$ mit einer anderen Matrixdarstellung ($P^T A P$) transformiert werden. Ein Hauptziel ist oft, eine orthogonale Transformation zu finden (bei der $P$ eine orthogonale Matrix ist), die die Matrix $A$ diagonalisiert, was zu einer quadratischen Form ohne gemischte Terme (nur quadrierte Terme) führt. Dies hängt mit dem Hauptachsentheorem zusammen.

**Anwendungen quadratischer Formen:**

Quadratische Formen erscheinen in verschiedenen Bereichen der Mathematik, Physik, Statistik und Ingenieurwissenschaften, darunter:

* **Kegelschnitte und Quadriken:** Die Gleichungen dieser geometrischen Objekte können mit quadratischen Formen ausgedrückt werden.
* **Optimierung:** Die Bestimmung der Art von kritischen Punkten multivariabler Funktionen beinhaltet oft die Analyse der quadratischen Form der Hesse-Matrix.
* **Stabilitätsanalyse:** In dynamischen Systemen werden quadratische Formen (wie Lyapunov-Funktionen) verwendet, um die Stabilität von Gleichgewichtspunkten zu analysieren.
* **Statistik:** Kovarianzmatrizen definieren quadratische Formen, die die Streuung und Korrelation von Daten beschreiben.
* **Mechanik und Physik:** Kinetische und potentielle Energie in einigen Systemen können als quadratische Formen ausgedrückt werden.

Zusammenfassend ist eine quadratische Form ein grundlegendes Konzept in der linearen Algebra, das eine Möglichkeit bietet, homogene quadratische Polynome mithilfe der Sprache von Vektoren und Matrizen auszudrücken und zu analysieren. Ihre Matrixdarstellung und Klassifikation basierend auf Definitheit sind entscheidend für das Verständnis ihrer Eigenschaften und Anwendungen.