---
audio: false
generated: true
lang: de
layout: post
title: Lineare Transformationen – Gemini
translated: true
type: note
---

Okay, tauchen wir ein in ein ausführliches Tutorial über lineare Transformationen, das die Definition, Beispiele, Matrixdarstellung, Kern, Bild und Eigenschaften wie Injektivität und Surjektivität abdeckt. Dies ist ein grundlegendes Thema der linearen Algebra.

## 6. Lineare Transformationen: Ein ausführliches Tutorial

Eine **lineare Transformation** ist eine Funktion zwischen zwei Vektorräumen, die die Operationen der Vektoraddition und der skalaren Multiplikation erhält. Seien \\(V\\) und \\(W\\) Vektorräume über demselben Körper \\(F\\) (was oft die Menge der reellen Zahlen \\(\mathbb{R}\\) oder komplexen Zahlen \\(\mathbb{C}\\) ist).

**Definition:** Eine Funktion \\(T: V \rightarrow W\\) ist eine lineare Transformation, wenn sie die folgenden zwei Eigenschaften für alle Vektoren \\(\mathbf{u}, \mathbf{v} \in V\\) und alle Skalare \\(c \in F\\) erfüllt:

1.  **Additivität:** \\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})\\)
2.  **Homogenität (Skalare Multiplikation):** \\(T(c\mathbf{u}) = cT(\mathbf{u})\\)

Diese beiden Eigenschaften können zu einer einzigen Bedingung kombiniert werden:
\\(T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})\\) für alle \\(\mathbf{u}, \mathbf{v} \in V\\) und alle Skalare \\(c, d \in F\\).

**Wichtige Konsequenzen der Linearität:**

* \\(T(\mathbf{0}_V) = \mathbf{0}_W\\), wobei \\(\mathbf{0}_V\\) der Nullvektor in \\(V\\) und \\(\mathbf{0}_W\\) der Nullvektor in \\(W\\) ist. (Beweis: \\(T(\mathbf{0}_V) = T(0\mathbf{u}) = 0T(\mathbf{u}) = \mathbf{0}_W\\) für jedes \\(\mathbf{u} \in V\\)).
* \\(T(-\mathbf{u}) = -T(\mathbf{u})\\). (Beweis: \\(T(-\mathbf{u}) = T((-1)\mathbf{u}) = (-1)T(\mathbf{u}) = -T(\mathbf{u})\\)).

### Beispiele für lineare Transformationen

Schauen wir uns einige Beispiele an, um das Konzept besser zu verstehen.

**Beispiel 1: Transformation in \\(\mathbb{R}^2\\) (Rotation)**

Betrachten Sie eine Transformation \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\), die jeden Vektor in \\(\mathbb{R}^2\\) gegen den Uhrzeigersinn um einen Winkel \\(\theta\\) dreht. Wenn \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\), dann ist \\(T(\mathbf{v}) = \begin{pmatrix} x\cos\theta - y\sin\theta \\ x\sin\theta + y\cos\theta \end{pmatrix}\\).

Prüfen wir, ob dies eine lineare Transformation ist. Seien \\(\mathbf{u} = \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}\\) und \\(\mathbf{v} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix}\\), und sei \\(c\\) ein Skalar.

* **Additivität:**
    \\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2)\cos\theta - (y_1 + y_2)\sin\theta \\ (x_1 + x_2)\sin\theta + (y_1 + y_2)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} (x_1\cos\theta - y_1\sin\theta) + (x_2\cos\theta - y_2\sin\theta) \\ (x_1\sin\theta + y_1\cos\theta) + (x_2\sin\theta + y_2\cos\theta) \end{pmatrix} = T(\mathbf{u}) + T(\mathbf{v})\\)

* **Homogenität:**
    \\(T(c\mathbf{u}) = T\left(\begin{pmatrix} cx_1 \\ cy_1 \end{pmatrix}\right) = \begin{pmatrix} (cx_1)\cos\theta - (cy_1)\sin\theta \\ (cx_1)\sin\theta + (cy_1)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} c(x_1\cos\theta - y_1\sin\theta) \\ c(x_1\sin\theta + y_1\cos\theta) \end{pmatrix} = c \begin{pmatrix} x_1\cos\theta - y_1\sin\theta \\ x_1\sin\theta + y_1\cos\theta \end{pmatrix} = cT(\mathbf{u})\\)

Somit ist die Rotation eine lineare Transformation.

**Beispiel 2: Transformation in \\(\mathbb{R}^2\\) (Projektion auf die x-Achse)**

Betrachten Sie \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) definiert durch \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x \\ 0 \end{pmatrix}\\). Diese Transformation projiziert jeden Vektor auf die x-Achse. Sie können überprüfen, dass dies ebenfalls eine lineare Transformation ist, indem Sie die Definition verwenden.

**Beispiel 3: Transformation in \\(\mathbb{R}^2\\) (Translation)**

Betrachten Sie \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) definiert durch \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + a \\ y + b \end{pmatrix}\\), wobei \\(a\\) und \\(b\\) Konstanten sind (nicht beide null).

Prüfen wir die erste Eigenschaft:
\\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2) + a \\ (y_1 + y_2) + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)

Das scheint korrekt zu sein, prüfen wir noch einmal nach.
\\(T(\mathbf{u} + \mathbf{v}) = \begin{pmatrix} x_1 + x_2 + a \\ y_1 + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + x_2 + 2a \\ y_1 + y_2 + 2b \end{pmatrix}\\)

Wenn \\(a \neq 0\\) oder \\(b \neq 0\\), dann ist \\(T(\mathbf{u} + \mathbf{v}) \neq T(\mathbf{u}) + T(\mathbf{v})\\). Außerdem ist \\(T(\mathbf{0}) = T\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} a \\ b \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \end{pmatrix}\\), wenn \\(a\\) oder \\(b\\) ungleich null ist. Daher ist die Translation im Allgemeinen **keine** lineare Transformation.

**Beispiel 4: Transformation von \\(\mathbb{R}^n\\) nach \\(\mathbb{R}^m\\) definiert durch eine Matrix**

Sei \\(A\\) eine \\(m \times n\\)-Matrix. Die Transformation \\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\) definiert durch \\(T(\mathbf{x}) = A\mathbf{x}\\) (wobei \\(\mathbf{x}\\) ein \\(n \times 1\\)-Spaltenvektor ist) ist eine lineare Transformation. Dies liegt daran, dass die Matrixmultiplikation die Eigenschaften der Additivität und Homogenität erfüllt:
\\(A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}\\)
\\(A(c\mathbf{u}) = c(A\mathbf{u})\\)

**Beispiel 5: Differentiation von Polynomen**

Sei \\(P_n\\) der Vektorraum der Polynome vom Grad höchstens \\(n\\). Die Transformation \\(D: P_n \rightarrow P_{n-1}\\) definiert durch \\(D(p(x)) = p'(x)\\) (die Ableitung von \\(p(x)\\)) ist eine lineare Transformation.
Wenn \\(p(x)\\) und \\(q(x)\\) Polynome sind und \\(c\\) ein Skalar ist:
\\(D(p(x) + q(x)) = (p(x) + q(x))' = p'(x) + q'(x) = D(p(x)) + D(q(x))\\)
\\(D(cp(x)) = (cp(x))' = cp'(x) = cD(p(x))\\)

**Beispiel 6: Integration von Funktionen**

Sei \\(C[a, b]\\) der Vektorraum der stetigen Funktionen auf dem Intervall \\([a, b]\\). Die Transformation \\(I: C[a, b] \rightarrow \mathbb{R}\\) definiert durch \\(I(f) = \int_a^b f(x) dx\\) ist eine lineare Transformation.
\\(I(f + g) = \int_a^b (f(x) + g(x)) dx = \int_a^b f(x) dx + \int_a^b g(x) dx = I(f) + I(g)\\)
\\(I(cf) = \int_a^b cf(x) dx = c \int_a^b f(x) dx = cI(f)\\)

### Matrixdarstellung einer linearen Transformation

Ein grundlegendes Ergebnis der linearen Algebra ist, dass jede lineare Transformation zwischen endlichdimensionalen Vektorräumen durch eine Matrix dargestellt werden kann.

Sei \\(V\\) ein \\(n\\)-dimensionaler Vektorraum mit Basis \\(\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\) und \\(W\\) ein \\(m\\)-dimensionaler Vektorraum mit Basis \\(\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2, ..., \mathbf{c}_m\}\\). Sei \\(T: V \rightarrow W\\) eine lineare Transformation.

Um die Matrixdarstellung von \\(T\\) bezüglich der Basen \\(\mathcal{B}\\) und \\(\mathcal{C}\\) zu finden (bezeichnet als \\([T]_{\mathcal{B}}^{\mathcal{C}}\\) oder einfach \\([T]\\), wenn die Basen klar sind), müssen wir die Bilder der Basisvektoren von \\(V\\) unter \\(T\\) bestimmen und diese Bilder als Linearkombinationen der Basisvektoren von \\(W\\) ausdrücken.

Für jedes \\(\mathbf{b}_j \in \mathcal{B}\\) ist \\(T(\mathbf{b}_j)\\) ein Vektor in \\(W\\), also kann er eindeutig als Linearkombination der Basisvektoren in \\(\mathcal{C}\\) geschrieben werden:
\\(T(\mathbf{b}_j) = a_{1j}\mathbf{c}_1 + a_{2j}\mathbf{c}_2 + ... + a_{mj}\mathbf{c}_m = \sum_{i=1}^{m} a_{ij}\mathbf{c}_i\\)

Die Koeffizienten dieser Linearkombination bilden die \\(j\\)-te Spalte der Matrixdarstellung \\([T]_{\mathcal{B}}^{\mathcal{C}}\\):
$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}$

Wenn \\(\mathbf{v} \in V\\) einen Koordinatenvektor \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}\\) bezüglich der Basis \\(\mathcal{B}\\) hat, dann ist der Koordinatenvektor von \\(T(\mathbf{v})\\) bezüglich der Basis \\(\mathcal{C}\\), bezeichnet als \\([T(\mathbf{v})]_{\mathcal{C}}\\), gegeben durch das Matrixprodukt:
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}}\\)

**Beispiel: Matrixdarstellung**

Sei \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) eine lineare Transformation definiert durch \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\). Seien die Standardbasen für \\(\mathbb{R}^2\\) und \\(\mathbb{R}^3\\) \\(\mathcal{B} = \{\mathbf{e}_1, \mathbf{e}_2\} = \left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right\}\\) und \\(\mathcal{C} = \{\mathbf{f}_1, \mathbf{f}_2, \mathbf{f}_3\} = \left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\\).

Wir finden die Bilder der Basisvektoren von \\(\mathbb{R}^2\\) unter \\(T\\):
\\(T(\mathbf{e}_1) = T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 + 0 \\ 2(1) - 0 \\ 3(0) \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} = 1\mathbf{f}_1 + 2\mathbf{f}_2 + 0\mathbf{f}_3\\)
\\(T(\mathbf{e}_2) = T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 0 + 1 \\ 2(0) - 1 \\ 3(1) \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} = 1\mathbf{f}_1 - 1\mathbf{f}_2 + 3\mathbf{f}_3\\)

Die Matrixdarstellung von \\(T\\) bezüglich der Standardbasen ist:
\\([T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix}\\)

Nehmen wir nun einen beliebigen Vektor \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\) in \\(\mathbb{R}^2\\). Sein Koordinatenvektor bezüglich \\(\mathcal{B}\\) ist \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x \\ y \end{pmatrix}\\).
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)
Der Koordinatenvektor bezüglich \\(\mathcal{C}\\) ist tatsächlich \\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\), was dem Vektor \\(T(\mathbf{v})\\) entspricht, den wir zuvor definiert haben.

### Kern (Nullraum) einer linearen Transformation

Der **Kern** (oder Nullraum) einer linearen Transformation \\(T: V \rightarrow W\\), bezeichnet mit \\(\text{ker}(T)\\) oder \\(N(T)\\), ist die Menge aller Vektoren in \\(V\\), die auf den Nullvektor in \\(W\\) abgebildet werden:
\\(\text{ker}(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}_W\}\\)

**Eigenschaften des Kerns:**

* Der Kern einer linearen Transformation ist immer ein Unterraum des Definitionsbereichs \\(V\\).
    * **Enthält den Nullvektor:** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\), also \\(\mathbf{0}_V \in \text{ker}(T)\\).
    * **Abgeschlossen unter Addition:** Wenn \\(\mathbf{u}, \mathbf{v} \in \text{ker}(T)\\), dann \\(T(\mathbf{u}) = \mathbf{0}_W\\) und \\(T(\mathbf{v}) = \mathbf{0}_W\\). Somit ist \\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) = \mathbf{0}_W + \mathbf{0}_W = \mathbf{0}_W\\), also \\(\mathbf{u} + \mathbf{v} \in \text{ker}(T)\\).
    * **Abgeschlossen unter skalarer Multiplikation:** Wenn \\(\mathbf{u} \in \text{ker}(T)\\) und \\(c\\) ein Skalar ist, dann ist \\(T(c\mathbf{u}) = cT(\mathbf{u}) = c\mathbf{0}_W = \mathbf{0}_W\\), also \\(c\mathbf{u} \in \text{ker}(T)\\).

**Beispiel: Finden des Kerns**

Betrachten Sie die lineare Transformation \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) definiert durch \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\).
Um den Kern zu finden, müssen wir \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\) lösen:
\\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\)

Dies ergibt das lineare Gleichungssystem:
\\(x + y = 0\\)
\\(2x - y = 0\\)
\\(3y = 0\\)

Aus der dritten Gleichung folgt \\(y = 0\\). Setzt man dies in die erste Gleichung ein, erhält man \\(x + 0 = 0\\), also \\(x = 0\\). Die zweite Gleichung ist ebenfalls erfüllt: \\(2(0) - 0 = 0\\).
Die einzige Lösung ist \\(x = 0\\) und \\(y = 0\\). Daher ist \\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}\\), was der Nullunterraum von \\(\mathbb{R}^2\\) ist.

### Bild (Wertebereich) einer linearen Transformation

Das **Bild** (oder der Wertebereich) einer linearen Transformation \\(T: V \rightarrow W\\), bezeichnet mit \\(\text{im}(T)\\) oder \\(R(T)\\), ist die Menge aller Vektoren in \\(W\\), die das Bild eines Vektors in \\(V\\) sind:
\\(\text{im}(T) = \{\mathbf{w} \in W \mid \mathbf{w} = T(\mathbf{v}) \text{ für ein } \mathbf{v} \in V\}\\)

**Eigenschaften des Bildes:**

* Das Bild einer linearen Transformation ist immer ein Unterraum des Zielraums \\(W\\).
    * **Enthält den Nullvektor:** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\), also \\(\mathbf{0}_W \in \text{im}(T)\\).
    * **Abgeschlossen unter Addition:** Wenn \\(\mathbf{w}_1, \mathbf{w}_2 \in \text{im}(T)\\), dann existieren \\(\mathbf{v}_1, \mathbf{v}_2 \in V\\) mit \\(T(\mathbf{v}_1) = \mathbf{w}_1\\) und \\(T(\mathbf{v}_2) = \mathbf{w}_2\\). Dann ist \\(\mathbf{w}_1 + \mathbf{w}_2 = T(\mathbf{v}_1) + T(\mathbf{v}_2) = T(\mathbf{v}_1 + \mathbf{v}_2)\\). Da \\(\mathbf{v}_1 + \mathbf{v}_2 \in V\\) ist, gilt \\(\mathbf{w}_1 + \mathbf{w}_2 \in \text{im}(T)\\).
    * **Abgeschlossen unter skalarer Multiplikation:** Wenn \\(\mathbf{w} \in \text{im}(T)\\) und \\(c\\) ein Skalar ist, dann existiert ein \\(\mathbf{v} \in V\\) mit \\(T(\mathbf{v}) = \mathbf{w}\\). Dann ist \\(c\mathbf{w} = cT(\mathbf{v}) = T(c\mathbf{v})\\). Da \\(c\mathbf{v} \in V\\) ist, gilt \\(c\mathbf{w} \in \text{im}(T)\\).

* Wenn \\(V\\) endlichdimensional mit einer Basis \\(\{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\) ist, dann ist das Bild von \\(T\\) die lineare Hülle der Bilder der Basisvektoren:
    \\(\text{im}(T) = \text{span}\{T(\mathbf{b}_1), T(\mathbf{b}_2), ..., T(\mathbf{b}_n)\}\\)

**Beispiel: Finden des Bildes**

Betrachten Sie die lineare Transformation \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) definiert durch \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\).
Unter Verwendung der Standardbasis von \\(\mathbb{R}^2\\), \\(\{\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}\}\\), haben wir:
\\(T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}\\)
\\(T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}\\)

Das Bild von \\(T\\) ist die lineare Hülle dieser beiden Vektoren:
\\(\text{im}(T) = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} \right\}\\)
Dies ist ein Unterraum von \\(\mathbb{R}^3\\). Da diese beiden Vektoren linear unabhängig sind (der eine ist kein skalares Vielfaches des anderen), ist das Bild eine Ebene durch den Ursprung in \\(\mathbb{R}^3\\).

**Beziehung zwischen Matrixdarstellung und Bild:**

Wenn \\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\) gegeben ist durch \\(T(\mathbf{x}) = A\mathbf{x}\\), wobei \\(A\\) eine \\(m \times n\\)-Matrix ist, dann ist das Bild von \\(T\\) der Spaltenraum der Matrix \\(A\\), d.h. die lineare Hülle der Spalten von \\(A\\).

### Eigenschaften linearer Transformationen: Injektivität und Surjektivität

**Injektivität (Eineindeutigkeit)**

Eine lineare Transformation \\(T: V \rightarrow W\\) ist **injektiv** (oder eineindeutig), wenn es für jedes \\(\mathbf{w} \in W\\) höchstens ein \\(\mathbf{v} \in V\\) gibt, so dass \\(T(\mathbf{v}) = \mathbf{w}\\). Äquivalent dazu: Wenn \\(T(\mathbf{u}) = T(\mathbf{v})\\), dann ist \\(\mathbf{u} = \mathbf{v}\\).

**Satz:** Eine lineare Transformation \\(T: V \rightarrow W\\) ist genau dann injektiv, wenn ihr Kern der Nullunterraum ist, d.h. \\(\text{ker}(T) = \{\mathbf{0}_V\}\\).

**Beweis:**
* **(\\(\Rightarrow\\)) Angenommen, \\(T\\) ist injektiv.** Wenn \\(\mathbf{v} \in \text{ker}(T)\\), dann ist \\(T(\mathbf{v}) = \mathbf{0}_W\\). Wir wissen auch, dass \\(T(\mathbf{0}_V) = \mathbf{0}_W\\). Da \\(T\\) injektiv ist und \\(T(\mathbf{v}) = T(\mathbf{0}_V)\\), muss \\(\mathbf{v} = \mathbf{0}_V\\) sein. Somit ist \\(\text{ker}(T) = \{\mathbf{0}_V\}\\).
* **(\\(\Leftarrow\\)) Angenommen, \\(\text{ker}(T) = \{\mathbf{0}_V\}\\).** Angenommen, \\(T(\mathbf{u}) = T(\mathbf{v})\\) für einige \\(\mathbf{u}, \mathbf{v} \in V\\). Dann ist \\(T(\mathbf{u}) - T(\mathbf{v}) = \mathbf{0}_W\\). Aufgrund der Linearität ist \\(T(\mathbf{u} - \mathbf{v}) = \mathbf{0}_W\\). Das bedeutet, dass \\(\mathbf{u} - \mathbf{v} \in \text{ker}(T)\\). Da \\(\text{ker}(T) = \{\mathbf{0}_V\}\\) ist, haben wir \\(\mathbf{u} - \mathbf{v} = \mathbf{0}_V\\), was \\(\mathbf{u} = \mathbf{v}\\) impliziert. Daher ist \\(T\\) injektiv.

**Beispiel: Überprüfung auf Injektivität**

Für die Transformation \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) definiert durch \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) haben wir festgestellt, dass \\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}\\). Daher ist diese Transformation injektiv.

**Surjektivität (Onto)**

Eine lineare Transformation \\(T: V \rightarrow W\\) ist **surjektiv** (oder onto), wenn es für jedes \\(\mathbf{w} \in W\\) mindestens ein \\(\mathbf{v} \in V\\) gibt, so dass \\(T(\mathbf{v}) = \mathbf{w}\\). Mit anderen Worten, das Bild von \\(T\\) ist gleich dem Zielraum \\(W\\), d.h. \\(\text{im}(T) = W\\).

**Satz (Rangsatz):** Für eine lineare Transformation \\(T: V \rightarrow W\\), wobei \\(V\\) ein endlichdimensionaler Vektorraum ist, gilt:
\\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = \text{dim}(V)\\)
Hierbei wird \\(\text{dim}(\text{ker}(T))\\) als **Nullität** von \\(T\\) und \\(\text{dim}(\text{im}(T))\\) als **Rang** von \\(T\\) bezeichnet.

**Beziehung zwischen Surjektivität und Dimensionen:**

Wenn \\(T: V \rightarrow W\\) eine lineare Transformation zwischen endlichdimensionalen Vektorräumen ist, dann gilt:
* Wenn \\(\text{dim}(V) < \text{dim}(W)\\), dann kann \\(T\\) nicht surjektiv sein. (Nach dem Rangsatz gilt \\(\text{dim}(\text{im}(T)) \leq \text{dim}(V) < \text{dim}(W)\\)).
* Wenn \\(\text{dim}(V) > \text{dim}(W)\\), dann kann \\(T\\) nicht injektiv sein (weil \\(\text{dim}(\text{ker}(T)) = \text{dim}(V) - \text{dim}(\text{im}(T)) \geq \text{dim}(V) - \text{dim}(W) > 0\\), also ist der Kern nicht nur der Nullvektor).
* Wenn \\(\text{dim}(V) = \text{dim}(W)\\), dann ist \\(T\\) genau dann injektiv, wenn sie surjektiv ist. (Wenn \\(T\\) injektiv ist, dann ist \\(\text{dim}(\text{ker}(T)) = 0\\), also \\(\text{dim}(\text{im}(T)) = \text{dim}(V) = \text{dim}(W)\\), was \\(\text{im}(T) = W\\) bedeutet, also ist \\(T\\) surjektiv. Umgekehrt, wenn \\(T\\) surjektiv ist, dann ist \\(\text{dim}(\text{im}(T)) = \text{dim}(W) = \text{dim}(V)\\), also \\(\text{dim}(\text{ker}(T)) = 0\\), was bedeutet, dass \\(T\\) injektiv ist).

**Beispiel: Überprüfung auf Surjektivität**

Für die Transformation \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) definiert durch \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\) haben wir festgestellt, dass \\(\text{im}(T) = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} \right\}\\). Die Dimension des Bildes (Rang von \\(T\\)) ist 2, da die beiden aufspannenden Vektoren linear unabhängig sind. Die Dimension des Definitionsbereichs ist \\(\text{dim}(\mathbb{R}^2) = 2\\). Nach dem Rangsatz gilt \\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = 2\\), also \\(\text{dim}(\text{ker}(T)) + 2 = 2\\), was \\(\text{dim}(\text{ker}(T)) = 0\\) ergibt, was mit unserer früheren Feststellung übereinstimmt.

Da die Dimension des Bildes (2) kleiner ist als die Dimension des Zielraums (3), ist das Bild ein echter Unterraum des Zielraums, und somit ist die Transformation nicht surjektiv. Es gibt Vektoren in \\(\mathbb{R}^3\\), die nicht im Bild von \\(T\\) liegen. Zum Beispiel kann \\(\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}\\) nicht als Linearkombination von \\(\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}\\) und \\(\begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}\\) ausgedrückt werden.

**Isomorphismus**

Eine lineare Transformation \\(T: V \rightarrow W\\) wird **Isomorphismus** genannt, wenn sie sowohl injektiv als auch surjektiv ist. Wenn es einen Isomorphismus zwischen zwei Vektorräumen \\(V\\) und \\(W\\) gibt, dann heißen \\(V\\) und \\(W\\) **isomorph**, bezeichnet mit \\(V \cong W\\). Isomorphe Vektorräume haben im Wesentlichen die gleiche algebraische Struktur.

Für endlichdimensionale Vektorräume sind zwei Vektorräume genau dann isomorph, wenn sie die gleiche Dimension haben. Wenn \\(\text{dim}(V) = \text{dim}(W) = n\\), dann ist eine lineare Transformation \\(T: V \rightarrow W\\) genau dann ein Isomorphismus, wenn sie entweder injektiv oder surjektiv ist.

**Zusammenfassung der Schlüsselkonzepte:**

* **Lineare Transformation:** Eine Funktion zwischen Vektorräumen, die Vektoraddition und skalare Multiplikation erhält.
* **Matrixdarstellung:** Eine Möglichkeit, eine lineare Transformation zwischen endlichdimensionalen Vektorräumen als Matrix darzustellen.
* **Kern (Nullraum):** Die Menge der Vektoren im Definitionsbereich, die auf den Nullvektor im Zielraum abgebildet werden. Es ist ein Unterraum des Definitionsbereichs.
* **Bild (Wertebereich):** Die Menge der Vektoren im Zielraum, die das Bild eines Vektors im Definitionsbereich sind. Es ist ein Unterraum des Zielraums.
* **Injektivität (Eineindeutigkeit):** Eine lineare Transformation ist genau dann injektiv, wenn ihr Kern der Nullunterraum ist.
* **Surjektivität (Onto):** Eine lineare Transformation ist genau dann surjektiv, wenn ihr Bild gleich dem Zielraum ist.
* **Rangsatz:** Für eine lineare Transformation \\(T: V \rightarrow W\\) mit endlichdimensionalem \\(V\\) gilt \\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = \text{dim}(V)\\).
* **Isomorphismus:** Eine lineare Transformation, die sowohl injektiv als auch surjektiv ist.

Dieses ausführliche Tutorial sollte eine solide Grundlage für das Verständnis linearer Transformationen bieten. Denken Sie daran, mit verschiedenen Beispielen zu üben, um Ihr Verständnis dieser Konzepte zu festigen. Viel Erfolg bei Ihren Studien!