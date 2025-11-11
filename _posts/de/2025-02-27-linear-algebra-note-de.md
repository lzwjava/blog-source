---
audio: false
generated: true
lang: de
layout: post
title: Lineare Algebra Notizen
translated: true
type: note
---

## Beispiel

Betrachten Sie die quadratische Form in zwei Variablen \\( x \\) und \\(y\\):

\\[ Q(x, y) = 2x^2 + 4xy + 3y^2 \\]

### Schritt-für-Schritt-Transformation in die kanonische Form

1.  **Matrixdarstellung:**
    - Schreiben Sie die quadratische Form als Matrixgleichung. Die Matrix \\(A\\), die dieser quadratischen Form zugeordnet ist, lautet:

\\[
A = \begin{pmatrix}
2 & 2 \\
2 & 3
\end{pmatrix}
\\]

    Beachten Sie, dass die Nicht-Diagonalelemente die Hälfte des Koeffizienten des \\(xy\\)-Terms sind.

2.  **Eigenwerte und Eigenvektoren finden:**
    - Berechnen Sie die Eigenwerte von \\(A\\), indem Sie die charakteristische Gleichung \\( \det(A - \lambda I) = 0 \\) lösen.
    - Finden Sie für jeden Eigenwert den entsprechenden Eigenvektor.

3.  **Diagonalisierung:**
    - Konstruieren Sie eine Matrix \\(P\\), deren Spalten die Eigenvektoren von \\(A\\) sind.
    - Berechnen Sie \\(D = P^TAP\\). Dies wird eine Diagonalmatrix mit den Eigenwerten von \\(A\\) auf der Diagonalen sein.

4.  **Variablenwechsel:**
    - Definieren Sie neue Variablen \\(u\\) und \\(v\\), sodass:

\\[
\begin{pmatrix}
x \\
y
\end{pmatrix} = P \begin{pmatrix}
u \\
v
\end{pmatrix}
\\]

    - Setzen Sie diese in die ursprüngliche quadratische Form ein, um eine neue Form in Bezug auf \\(u\\) und \\(v\\) zu erhalten.

5.  **Kanonische Form:**
    - Die resultierende quadratische Form wird in der kanonischen Form vorliegen, die eine Summe von Quadraten ist:

\\[
Q(u, v) = \lambda_1 u^2 + \lambda_2 v^2
\\]

    wobei \\(\lambda_1\\) und \\(\lambda_2\\) die Eigenwerte von \\(A\\) sind.

### Interpretation

-   Die kanonische Form offenbart die geometrische Natur der quadratischen Form.
-   Wenn beide Eigenwerte positiv sind, ist die Form positiv definit.
-   Wenn beide negativ sind, ist sie negativ definit.
-   Wenn sie unterschiedliche Vorzeichen haben, ist die Form indefinit.

Dieser Prozess vereinfacht die quadratische Form und erleichtert die Analyse ihrer Eigenschaften.

---

Im Kontext quadratischer Formen übersetzt sich der Begriff "二次型的规范形" ins Englische als "canonical form of a quadratic form". Das Verständnis dieses Konzepts beinhaltet die Erkenntnis, wie eine quadratische Form durch lineare Algebra Techniken vereinfacht oder in eine Standardform transformiert werden kann.

### Quadratische Formen
Eine quadratische Form ist ein homogenes Polynom zweiten Grades in mehreren Variablen. Zum Beispiel könnte eine quadratische Form in zwei Variablen \\(x\\) und \\(y\\) so aussehen:

\\[ Q(x, y) = ax^2 + bxy + cy^2 \\]

### Kanonische Form
Die kanonische Form einer quadratischen Form ist eine vereinfachte Version, die wesentliche Eigenschaften offenbart, wie den Rang und die Signatur (die Anzahl der positiven, negativen und null Eigenwerte). Um diese Form zu erreichen, führen wir typischerweise einen Variablenwechsel durch, oft durch Diagonalisierung oder andere orthogonale Transformationen.

#### Schritte zum Finden der kanonischen Form:
1.  **Matrixdarstellung:** Stellen Sie die quadratische Form als eine symmetrische Matrix \\(A\\) dar. Für das obige Beispiel wäre die Matrix:
\\[
A = \begin{pmatrix}
a & \frac{b}{2} \\
\frac{b}{2} & c
\end{pmatrix}
\\]

2.  **Diagonalisierung:** Finden Sie eine orthogonale Matrix \\(P\\), sodass \\(P^TAP\\) eine Diagonalmatrix \\(D\\) ist. Dieser Prozess beinhaltet das Finden der Eigenwerte und Eigenvektoren von \\(A\\).

3.  **Variablenwechsel:** Verwenden Sie die Matrix \\(P\\) für einen Variablenwechsel, der die ursprüngliche quadratische Form in eine Summe von Quadraten transformiert, von denen jedes einem Eigenwert entspricht.

4.  **Kanonische Form:** Die resultierende Diagonalmatrix \\(D\\) repräsentiert die kanonische Form der quadratischen Form, wobei jeder Diagonaleintrag ein Eigenwert von \\(A\\) ist.

Die kanonische Form hilft bei der Analyse der Eigenschaften der quadratischen Form, wie z.B. der Bestimmung, ob sie positiv definit, negativ definit oder indefinit ist, was in der Optimierung und anderen mathematischen Anwendungen entscheidend ist.

---

Die **Normalform einer quadratischen Form** bezieht sich auf die vereinfachte Standarddarstellung einer quadratischen Form nach Anwendung eines geeigneten Variablenwechsels. Diese Transformation macht die Struktur der quadratischen Form klarer und einfacher zu analysieren.

---

### **1. Definition einer quadratischen Form**
Eine **quadratische Form** in \\( n \\) Variablen ist eine Funktion der Form:

\\[
Q(x) = x^T A x
\\]

wobei:
- \\( x = (x_1, x_2, \dots, x_n)^T \\) ein \\( n \\)-dimensionaler Spaltenvektor ist,
- \\( A \\) eine \\( n \times n \\) symmetrische Matrix ist.

Das Ziel ist es, diese quadratische Form in eine einfachere, standardisierte Form zu transformieren.

---

### **2. Finden der Normalform**
Um die quadratische Form zu vereinfachen, verwenden wir einen orthogonalen Variablenwechsel:

1.  **Finden der Eigenwerte und Eigenvektoren von \\( A \\):**
    - Berechnen Sie die Eigenwerte \\( \lambda_1, \lambda_2, \dots, \lambda_n \\).
    - Finden Sie eine Orthonormalbasis von Eigenvektoren.

2.  **Diagonalisierung von \\( A \\):**
    - Da \\( A \\) symmetrisch ist, kann sie diagonalisiert werden als \\( A = P D P^T \\), wobei:
        - \\( P \\) eine orthogonale Matrix ist (deren Spalten Eigenvektoren von \\( A \\) sind).
        - \\( D \\) eine Diagonalmatrix mit den Eigenwerten \\( \lambda_1, \lambda_2, \dots, \lambda_n \\) auf der Diagonalen ist.

3.  **Variablenwechsel:**
    - Definieren Sie eine neue Variable \\( y = P^T x \\), dann gilt:

\\[
Q(x) = x^T A x = (P y)^T A (P y) = y^T (P^T A P) y = y^T D y
\\]

    - Da \\( D \\) diagonal ist, vereinfacht sich die quadratische Form zu:

\\[
Q(y) = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \dots + \lambda_n y_n^2
\\]

    Dies ist die **Normalform der quadratischen Form**.

---

### **3. Interpretation der Normalform**
-   Die Normalform drückt die quadratische Form als eine Summe von Quadraten aus, gewichtet mit den Eigenwerten.
-   Die **Vorzeichen der Eigenwerte** bestimmen die Natur der quadratischen Form:
    -   Wenn alle Eigenwerte positiv sind, ist die Form **positiv definit**.
    -   Wenn alle negativ sind, ist sie **negativ definit**.
    -   Wenn es gemischte Vorzeichen gibt, ist sie **indefinit**.

Dieser Prozess ist wesentlich in der **Analysis von Kegelschnitten, Optimierung und Differentialgleichungen**, da er hilft, quadratische Flächen und Funktionen zu klassifizieren.

Möchten Sie ein detaillierteres Beispiel?