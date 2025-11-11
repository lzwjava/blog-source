---
audio: false
generated: true
lang: de
layout: post
title: Lineare Algebra Plus Notizen
translated: true
type: note
---

In der linearen Algebra heißen zwei quadratische Matrizen \\( A \\) und \\( B \\) ähnlich, wenn eine invertierbare Matrix \\( P \\) existiert, so dass:

\\[ B = P^{-1}AP \\]

Diese Beziehung wird als Ähnlichkeitstransformation bezeichnet. Die Matrix \\( P \\) wird Basiswechselmatrix genannt und transformiert die Matrix \\( A \\) in die Matrix \\( B \\).

### Wichtige Eigenschaften ähnlicher Matrizen:
1. **Gleiche Eigenwerte**: Ähnliche Matrizen haben die gleichen Eigenwerte. Dies liegt daran, dass die Eigenwerte unter Ähnlichkeitstransformationen erhalten bleiben.
2. **Gleiche Determinante**: Die Determinante ähnlicher Matrizen ist gleich, da \\(\det(P^{-1}AP) = \det(A)\\) gilt.
3. **Gleiche Spur**: Die Spur (Summe der Diagonalelemente) ähnlicher Matrizen ist gleich, da \\(\text{tr}(P^{-1}AP) = \text{tr}(A)\\) gilt.
4. **Gleicher Rang**: Ähnliche Matrizen haben den gleichen Rang.
5. **Gleiches charakteristisches Polynom**: Ähnliche Matrizen teilen sich dasselbe charakteristische Polynom.

### Intuition:
Ähnliche Matrizen stellen dieselbe lineare Transformation dar, jedoch in verschiedenen Basen. Die Matrix \\( P \\) kann als Koordinatenwechsel betrachtet werden, der die Basis transformiert, in der die lineare Transformation dargestellt wird.

### Beispiel:
Betrachten Sie zwei Matrizen \\( A \\) und \\( B \\):

\\[ A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}, \quad B = \begin{pmatrix} 3 & 0 \\ 2 & 1 \end{pmatrix} \\]

Um zu prüfen, ob sie ähnlich sind, müssen wir eine invertierbare Matrix \\( P \\) finden, so dass \\( B = P^{-1}AP \\) gilt.

Möchten Sie ein Beispiel sehen, wie man eine solche Matrix \\( P \\) für spezifische Matrizen \\( A \\) und \\( B \\) findet?

---

Ja, die Matrix:

\\[
A = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\\]

besitzt tatsächlich eine Singulärwertzerlegung (SVD). Lassen Sie uns den Prozess zur Ermittlung der SVD dieser Matrix durchgehen.

### Schritt 1: Berechne \\( A^T A \\)

Zuerst berechnen wir die Matrix \\( A^T A \\):

\\[
A^T = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}
\\]

Nun multiplizieren wir \\( A^T \\) und \\( A \\):

\\[
A^T A = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 1 + 9 & 2 + 12 \\ 2 + 12 & 4 + 16 \end{bmatrix} = \begin{bmatrix} 10 & 14 \\ 14 & 20 \end{bmatrix}
\\]

### Schritt 2: Eigenwerte und Eigenvektoren von \\( A^T A \\)

Um die Singulärwerte zu finden, benötigen wir die Eigenwerte von \\( A^T A \\). Wir lösen die charakteristische Gleichung \\( \text{det}(A^T A - \lambda I) = 0 \\):

\\[
\text{det}\begin{bmatrix} 10 - \lambda & 14 \\ 14 & 20 - \lambda \end{bmatrix} = 0
\\]

Dies ergibt:

\\[
(10 - \lambda)(20 - \lambda) - 14 \times 14 = 0
\\]

\\[
\lambda^2 - 30\lambda + 100 - 196 = 0
\\]

\\[
\lambda^2 - 30\lambda - 96 = 0
\\]

Lösen dieser quadratischen Gleichung:

\\[
\lambda = \frac{-(-30) \pm \sqrt{(-30)^2 - 4(1)(-96)}}{2(1)} = \frac{30 \pm \sqrt{900 + 384}}{2} = \frac{30 \pm \sqrt{1284}}{2}
\\]

\\[
\lambda = \frac{30 \pm 35.86}{2}
\\]

Somit sind die Eigenwerte:

\\[
\lambda_1 \approx 32.93 \quad \text{und} \quad \lambda_2 \approx 0.93
\\]

### Schritt 3: Berechne Singulärwerte

Die Singulärwerte sind die Quadratwurzeln der Eigenwerte von \\( A^T A \\). Daher haben wir:

\\[
\sigma_1 = \sqrt{32.93} \approx 5.73 \quad \text{und} \quad \sigma_2 = \sqrt{0.93} \approx 0.96
\\]

### Schritt 4: Berechne die Matrizen \\( U \\) und \\( V \\)

Um die Matrizen \\( U \\) und \\( V \\) zu finden, müssen wir die Eigenvektoren von \\( A^T A \\) und \\( A A^T \\) berechnen, aber da dies detaillierte Schritte erfordert, die über die grundlegende Berechnung hinausgehen, würde man sie typischerweise numerisch lösen.

Basierend auf den obigen Eigenwerten wissen wir jedoch, dass die Singulärwerte \\( 5.73 \\) und \\( 0.96 \\) sind, und \\( U \\) und \\( V \\) wären orthogonale Matrizen, die den Eigenvektoren von \\( A A^T \\) bzw. \\( A^T A \\) entsprechen.

Somit ist die SVD der Matrix \\( A \\):

\\[
A = U \Sigma V^T
\\]

Wobei:

- \\( \Sigma = \begin{bmatrix} 5.73 & 0 \\ 0 & 0.96 \end{bmatrix} \\)
- \\( U \\) und \\( V \\) orthogonale Matrizen sind, die den Eigenvektoren von \\( A A^T \\) bzw. \\( A^T A \\) entsprechen.

Die exakten Werte für \\( U \\) und \\( V \\) können durch Lösen der Eigenwertprobleme für \\( A^T A \\) und \\( A A^T \\) gefunden werden.

---

Die Aussage beschreibt das Verhalten der Matrix als lineare Transformation. Lassen Sie uns das aufschlüsseln, um zu verstehen, warum dies passiert:

### Matrix als lineare Transformation:
- **Eingaberaum**: Die Matrix operiert auf Vektoren aus einem 3-dimensionalen Raum (da sie 3 Spalten hat). Das bedeutet, sie nimmt 3-komponentige Vektoren als Eingabe.
- **Ausgaberaum**: Die Matrix bildet diese Vektoren auf einen 2-dimensionalen Raum ab (da sie 2 Zeilen hat). Das bedeutet, sie erzeugt 2-komponentige Vektoren als Ausgabe.

### Nullraum:
- **Definition**: Der Nullraum (oder Kern) einer Matrix besteht aus allen Vektoren, die, wenn mit der Matrix multipliziert, den Nullvektor ergeben.
- **Dimension**: Die Nullität der Matrix ist die Dimension dieses Nullraums. In diesem Fall ist die Nullität 1, was bedeutet, dass es einen 1-dimensionalen Unterraum von Vektoren gibt, die auf Null abgebildet werden.
- **Interpretation**: Dieser 1-dimensionale Unterraum stellt eine Gerade (im 3-dimensionalen Eingaberaum) von Vektoren dar, die auf den Nullvektor im 2-dimensionalen Ausgaberaum "zusammengequetscht" oder "kollabiert" werden.

### Warum dies passiert:
- **Rangsatz**: Der Satz besagt, dass für jede \\(m \times n\\)-Matrix der Rang (Dimension des Spaltenraums) plus der Nullität (Dimension des Nullraums) gleich der Anzahl der Spalten \\(n\\) ist. Hier ist der Rang 2 und die Anzahl der Spalten ist 3, also muss die Nullität 1 sein.
- **Lineare Abhängigkeit**: Die Existenz eines Nullraums der Dimension 1 zeigt an, dass es eine Redundanz oder lineare Abhängigkeit zwischen den Spalten der Matrix gibt. Das bedeutet, dass eine der Spalten als Linearkombination der anderen beiden ausgedrückt werden kann.

### Visualisierung:
- Stellen Sie sich einen 3D-Raum vor, in dem alle Punkte auf einer bestimmten Geraden (dem Nullraum) auf den Ursprung in einem 2D-Raum abgebildet werden. Diese Gerade repräsentiert die Vektoren, die durch die von der Matrix definierte Transformation "verloren" gehen oder "ignoriert" werden.

Dieses Verhalten ist ein grundlegender Aspekt linearer Transformationen und zeigt, wie Matrizen die Dimensionalität des Raums, auf den sie wirken, reduzieren können.

---

Um zu bestimmen, welche Option für eine Matrix notwendig ist, damit sie diagonalisierbar ist, werde ich jede Aussage untersuchen.

Eine quadratische Matrix A ist genau dann diagonalisierbar, wenn eine invertierbare Matrix P existiert, so dass P⁻¹AP eine Diagonalmatrix ist. Dies geschieht genau dann, wenn A einen vollständigen Satz linear unabhängiger Eigenvektoren besitzt.

Lassen Sie uns jede Option analysieren:

a) Die Matrix muss mindestens einen Eigenwert haben.
Während alle n×n-Matrizen (im komplexen Zahlenkörper) mindestens einen Eigenwert haben, garantiert dies allein nicht die Diagonalisierbarkeit. Eine Matrix könnte Eigenwerte haben, aber dennoch nicht diagonalisierbar sein, wenn sie nicht genügend linear unabhängige Eigenvektoren besitzt.

b) Die Matrix muss verschiedene Eigenwerte haben.
Verschiedene Eigenwerte zu haben ist hinreichend, aber nicht notwendig für Diagonalisierbarkeit. Eine Matrix mit wiederholten Eigenwerten kann immer noch diagonalisierbar sein, wenn sie genügend linear unabhängige Eigenvektoren besitzt, die diesen wiederholten Eigenwerten zugeordnet sind.

c) Die Matrix muss genügend linear unabhängige Eigenvektoren haben.
Dies ist genau die notwendige und hinreichende Bedingung für Diagonalisierbarkeit. Insbesondere ist eine n×n-Matrix genau dann diagonalisierbar, wenn sie n linear unabhängige Eigenvektoren besitzt, die eine Basis für den Vektorraum bilden.

Daher ist Option c) die richtige Antwort: Eine Matrix ist genau dann diagonalisierbar, wenn sie genügend linear unabhängige Eigenvektoren besitzt.