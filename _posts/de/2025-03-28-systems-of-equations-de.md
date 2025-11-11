---
audio: false
generated: true
lang: de
layout: post
title: Lineare Gleichungssysteme und der Gauß-Algorithmus
translated: true
type: note
---

Dieses Tutorial bietet eine detaillierte Anleitung zu **Gleichungssystemen**, ihrer Darstellung, Lösungen und der **Gauß-Elimination** Methode zu ihrer Lösung.

---

## **1. Gleichungssysteme: Definition und Darstellung**

Ein **System linearer Gleichungen** besteht aus mehreren linearen Gleichungen, die Variablen gemeinsam haben. Ein allgemeines System mit \\( n \\) Variablen und \\( m \\) Gleichungen kann geschrieben werden als:

\\[
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\
\vdots & \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n &= b_m
\end{aligned}
\\]

wobei:
- \\( x_1, x_2, \dots, x_n \\) die unbekannten Variablen sind.
- \\( a_{ij} \\) die Koeffizienten sind.
- \\( b_1, b_2, \dots, b_m \\) die Konstanten auf der rechten Seite sind.

### **Matrixdarstellung**

Ein Gleichungssystem kann mit **Matrizen** dargestellt werden:

\\[
A \mathbf{x} = \mathbf{b}
\\]

wobei:

- \\( A \\) die **Koeffizientenmatrix** ist:

  \\[
  A =
  \begin{bmatrix}
  a_{11} & a_{12} & \dots & a_{1n} \\
  a_{21} & a_{22} & \dots & a_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  a_{m1} & a_{m2} & \dots & a_{mn}
  \end{bmatrix}
  \\]

- \\( \mathbf{x} \\) der **Variablen-Spaltenvektor** ist:

  \\[
  \mathbf{x} =
  \begin{bmatrix}
  x_1 \\
  x_2 \\
  \vdots \\
  x_n
  \end{bmatrix}
  \\]

- \\( \mathbf{b} \\) der **Konstanten-Spaltenvektor** ist:

  \\[
  \mathbf{b} =
  \begin{bmatrix}
  b_1 \\
  b_2 \\
  \vdots \\
  b_m
  \end{bmatrix}
  \\]

Die **erweiterte Koeffizientenmatrix** wird geschrieben als:

\\[
[A | \mathbf{b}]
\\]

Beispiel:
\\[
\begin{aligned}
2x + 3y &= 8 \\
5x - y &= 3
\end{aligned}
\\]

Matrixdarstellung:
\\[
\begin{bmatrix}
2 & 3 \\
5 & -1
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
8 \\
3
\end{bmatrix}
\\]

Erweiterte Matrix:
\\[
\left[
\begin{array}{cc|c}
2 & 3 & 8 \\
5 & -1 & 3
\end{array}
\right]
\\]

---

## **2. Gauß-Eliminationsverfahren**

Die Gauß-Elimination ist eine systematische Methode zum Lösen von Gleichungssystemen, indem die erweiterte Matrix in **Zeilenstufenform (REF)** umgewandelt und dann die Variablen mittels **Rückwärtseinsetzen** gelöst werden.

### **Schritte der Gauß-Elimination**
1. **Umwandeln der erweiterten Matrix in eine obere Dreiecksform (Zeilenstufenform)** durch Zeilenoperationen:
   - Zeilen vertauschen, falls nötig.
   - Eine Zeile mit einer Konstanten ungleich Null multiplizieren.
   - Ein Vielfaches einer Zeile zu einer anderen Zeile addieren oder subtrahieren.

2. **Rückwärtseinsetzen**, um die Lösung zu finden.

---

### **Beispiel 1: Lösen eines Systems mit Gauß-Elimination**

Löse das System:
\\[
\begin{aligned}
2x + y - z &= 3 \\
4x - 6y &= 2 \\
-2x + 7y + 2z &= 5
\end{aligned}
\\]

#### **Schritt 1: Umwandeln in die erweiterte Matrix**
\\[
\left[
\begin{array}{ccc|c}
2 & 1 & -1 & 3 \\
4 & -6 & 0 & 2 \\
-2 & 7 & 2 & 5
\end{array}
\right]
\\]

#### **Schritt 2: Ersten Pivot zu 1 machen**
Dividiere Zeile 1 durch 2:
\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\
4 & -6 & 0 & 2 \\
-2 & 7 & 2 & 5
\end{array}
\right]
\\]

#### **Schritt 3: Eliminieren der ersten Spalte unter dem Pivot**
Ersetze Zeile 2 durch Subtraktion des 4-fachen von Zeile 1:
Ersetze Zeile 3 durch Addition des 2-fachen von Zeile 1:

\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\
0 & -8 & 2 & -4 \\
0 & 8 & 1 & 8
\end{array}
\right]
\\]

#### **Schritt 4: Zweiten Pivot zu 1 machen**
Dividiere Zeile 2 durch -8:

\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\
0 & 1 & -0.25 & 0.5 \\
0 & 8 & 1 & 8
\end{array}
\right]
\\]

#### **Schritt 5: Eliminieren der zweiten Spalte unter dem Pivot**
Ersetze Zeile 3 durch Subtraktion des 8-fachen von Zeile 2:

\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\
0 & 1 & -0.25 & 0.5 \\
0 & 0 & 3 & 4
\end{array}
\right]
\\]

#### **Schritt 6: Rückwärtseinsetzen**
Löse von unten nach oben:
- \\( 3z = 4 \Rightarrow z = \frac{4}{3} \\)
- \\( y - 0.25z = 0.5 \Rightarrow y = 0.5 + 0.25(4/3) = \frac{7}{6} \\)
- \\( x + 0.5y - 0.5z = 1.5 \Rightarrow x = 1.5 - 0.5(7/6) + 0.5(4/3) = \frac{11}{6} \\)

**Lösung:**
\\[
x = \frac{11}{6}, \quad y = \frac{7}{6}, \quad z = \frac{4}{3}
\\]

---

## **3. Lösungstypen**
1. **Eindeutige Lösung**: Eine einzige Lösung für \\( x_1, x_2, \dots \\).
2. **Unendlich viele Lösungen**: Viele Lösungen (System ist abhängig).
3. **Keine Lösung**: Inkonsistentes System.

---

## **4. Homogene vs. Nicht-Homogene Systeme**
- **Homogenes System**: \\( A\mathbf{x} = 0 \\)
  - Hat immer mindestens die **triviale Lösung** \\( \mathbf{x} = 0 \\).
  - Kann unendlich viele Lösungen haben, wenn die Determinante von \\( A \\) null ist.

- **Nicht-Homogenes System**: \\( A\mathbf{x} = \mathbf{b} \\)
  - Kann **eindeutige, unendlich viele oder keine Lösungen** haben.

---

## **Schlussfolgerung**
- Die Gauß-Elimination ist eine leistungsstarke Methode zum Lösen von Systemen.
- Die Anzahl der Lösungen hängt vom **Rang** der Matrix ab.
- Homogene Systeme haben immer eine triviale Lösung.

Lass mich wissen, wenn du weitere Beispiele oder Erklärungen benötigst! 🚀