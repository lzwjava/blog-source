---
audio: false
generated: true
image: false
lang: de
layout: post
title: 'Determinante: Entwicklung durch Linearität und Alternierung'
translated: true
type: note
---

Wenn man lernt, dass die Determinante eine Funktion ist, die

1. **multilinear** in den Zeilen (oder Spalten) ist, und
2. **alternierend** ist (das Vertauschen zweier Zeilen kehrt ihr Vorzeichen um),

dann ergibt sich die Kofaktor-Entwicklungsformel auf natürliche Weise. Hier ist eine schrittweise Erklärung des „Warums“ für den 3×3-Fall:

---

### 1. Determinante über Permutationen

Die allgemeinste Definition einer 3×3-Determinante ist

$$
\det A \;=\;
\sum_{\sigma\in S_3}\!\mathrm{sgn}(\sigma)\,a_{1,\sigma(1)}\,a_{2,\sigma(2)}\,a_{3,\sigma(3)},
$$

wobei man über alle sechs Permutationen σ von {1,2,3} summiert und sgn(σ) für gerade Permutationen +1 und für ungerade –1 ist.

Wenn man sie ausschreibt, erhält man genau die sechs Terme:

$$
a_{11}a_{22}a_{33},\;a_{12}a_{23}a_{31},\;a_{13}a_{21}a_{32}
\;-\;
\bigl(a_{13}a_{22}a_{31}+a_{11}a_{23}a_{32}+a_{12}a_{21}a_{33}\bigr).
$$

---

### 2. Gruppierung nach einer Zeile oder Spalte

Man kann diese sechs Terme **gruppieren**, je nachdem, welchen Eintrag aus der ersten Zeile sie verwenden:

* Terme, die \$a\_{11}\$ enthalten:

  $$
    a_{11}\,(a_{22}a_{33} - a_{23}a_{32})
    = a_{11}\det\!\begin{pmatrix}a_{22}&a_{23}\\a_{32}&a_{33}\end{pmatrix}.
  $$
* Terme, die \$a\_{12}\$ enthalten:

  $$
    a_{12}\,(a_{23}a_{31} - a_{21}a_{33})
    = -\,a_{12}\det\!\begin{pmatrix}a_{21}&a_{23}\\a_{31}&a_{33}\end{pmatrix}.
  $$
* Terme, die \$a\_{13}\$ enthalten:

  $$
    a_{13}\,(a_{21}a_{32} - a_{22}a_{31})
    = \;a_{13}\det\!\begin{pmatrix}a_{21}&a_{22}\\a_{31}&a_{32}\end{pmatrix}.
  $$

Das ist genau die **Kofaktor-Entwicklung entlang der ersten Zeile**:

$$
\det A
= a_{11}C_{11} \;+\; a_{12}C_{12} \;+\; a_{13}C_{13},
$$

wobei jeder Kofaktor $C_{1j} = (-1)^{1+j}\det(\text{Minor}_{1j})$ ist.

---

### 3. Warum „Minoren“ und „Vorzeichen“?

* **Minor**: $\det(\text{Minor}_{ij})$ ist die Determinante der 2×2-Untermatrix, die man erhält, indem man die i-te Zeile und die j-te Spalte streicht.
* **Vorzeichenfaktor** $(−1)^{i+j}$: stellt sicher, dass sich das Gesamtvorzeichen umkehrt, wenn man zwei Zeilen von $A$ vertauscht – genau wie es die Permutationsdefinition verlangt.

Weil die Determinante in jeder Zeile linear sein muss, kann man einen Eintrag aus einer Zeile „herausziehen“, wobei die Determinante der kleineren Matrix mit diesem Eintrag multipliziert bleibt. Die alternierende Eigenschaft erzwingt diese $(−1)$-Vorzeichen.

---

### 4. Geometrische Intuition

Für eine 3×3-Matrix, deren Zeilen Vektoren $\mathbf{u},\mathbf{v},\mathbf{w}\in\mathbb{R}^3$ sind, ist $\det A$ das orientierte Volumen des von ihnen aufgespannten Parallelepipeds.

* Die Entwicklung entlang, sagen wir, der ersten Zeile, zerlegt dieses Volumen in „Scheiben“, die senkrecht zu den Koordinatenachsen stehen.
* Die Fläche jeder Scheibe ist die Fläche des von den anderen beiden Zeilenvektoren aufgespannten Parallelogramms (eine 2×2-Determinante), und man skaliert sie mit der entsprechenden Koordinate $u_j$ von $\mathbf{u}$.
* Das Vorzeichen $(−1)^{1+j}$ behält die Orientierung im Auge.

---

### 5. Verallgemeinerung auf $n\times n$

All dies funktioniert auf die gleiche Weise für jede Größe $n$: Die Permutationsdefinition hat $n!$ Terme, man gruppiert sie nach einer Zeile oder Spalte, und jede Gruppe reduziert sich auf

$$
a_{ij}\,(-1)^{i+j}\det(\text{Minor}_{ij}).
$$

Das ist das Prinzip der **Kofaktor-Entwicklung**.

---

**Kurz gesagt:**
Die Kofaktor-Entwicklung ist einfach die Permutationssummen-Definition der Determinante, neu organisiert nach einer Zeile (oder Spalte), zusammen mit den Anforderungen der Linearität und Vorzeichenalternierung. Sie bietet eine rekursive Berechnungsmethode – und ein klares geometrisches Bild – der Determinante.