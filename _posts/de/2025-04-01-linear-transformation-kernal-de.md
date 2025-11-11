---
audio: false
generated: true
lang: de
layout: post
title: Der Kern einer linearen Abbildung
translated: true
type: note
---

Der **Kernel** einer linearen Transformation ist die Menge aller Eingabevektoren, die von der Transformation auf den Nullvektor abgebildet werden.

### Definition:
Wenn \\( T: V \to W \\) eine lineare Transformation zwischen zwei Vektorräumen \\( V \\) und \\( W \\) ist, dann ist der **Kernel** (oder **Nullraum**) von \\( T \\):

\\[
\ker(T) = \{ v \in V \mid T(v) = 0 \}
\\]

### Wichtige Eigenschaften:
1. **Unterraum**: Der Kernel einer linearen Transformation ist immer ein Unterraum des Definitionsbereichs \\( V \\).
2. **Dimension**: Die Dimension des Kernels wird als **Nullität** der Transformation bezeichnet.
3. **Beziehung zur Injektivität**:
   - Wenn \\( \ker(T) = \{0\} \\), dann ist \\( T \\) **injektiv** (eineindeutig).
   - Wenn \\( \ker(T) \\) eine Dimension größer als Null hat, dann ist \\( T \\) nicht injektiv.

### Beispiel:
Betrachten Sie die Matrixtransformation \\( T: \mathbb{R}^3 \to \mathbb{R}^2 \\) gegeben durch:

\\[
T(x, y, z) = (x + y, y + z)
\\]

Geschrieben als Matrix:

<div>
$$
T \begin{bmatrix} x \\ y \\ z \end{bmatrix} =
\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
$$
</div>

Um den Kernel zu finden, lösen Sie:

\\[
\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\\]

Dies ergibt das System:

\\[
x + y = 0
\\]
\\[
y + z = 0
\\]

Lösen nach \\( x, y, z \\):

\\[
x = -y, \quad z = -y
\\]

Somit besteht der Kernel aus allen Vektoren der Form:

<div>
$$
\ker(T) = \text{span} \left\{ \begin{bmatrix} -1 \\ 1 \\ -1 \end{bmatrix} \right\}
$$
</div>

was ein eindimensionaler Unterraum von \\( \mathbb{R}^3 \\) ist.

Lassen Sie mich wissen, wenn Sie weitere Erklärungen benötigen!