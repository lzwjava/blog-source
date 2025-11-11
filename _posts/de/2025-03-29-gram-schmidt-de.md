---
audio: false
generated: true
lang: de
layout: post
title: Gram-Schmidt-Verfahren
translated: true
type: note
---

Der **Gram-Schmidt-Prozess** ist eine Methode in der linearen Algebra, die verwendet wird, um eine Menge linear unabhängiger Vektoren in einen orthonormalen Satz von Vektoren umzuwandeln, die denselben Unterraum aufspannen. Dies ist besonders nützlich in verschiedenen Anwendungen wie QR-Zerlegung, der Lösung von Problemen der kleinsten Quadrate und der Vereinfachung von Berechnungen in Vektorräumen.

### **Schlüsselkonzepte**

- **Linear unabhängige Vektoren**: Vektoren, die nicht als Linearkombination voneinander ausgedrückt werden können.
- **Orthogonale Vektoren**: Vektoren, die senkrecht zueinander stehen, d.h. ihr Skalarprodukt ist null.
- **Orthonormale Menge**: Eine Menge von Vektoren, die sowohl orthogonal sind als auch die Einheitslänge haben (Norm gleich 1).

### **Zweck des Gram-Schmidt-Prozesses**

- **Orthogonalisierung**: Umwandlung einer Menge von Vektoren in eine Menge, bei der jeder Vektor orthogonal zu den anderen ist.
- **Normalisierung**: Anpassung der Länge jedes Vektors, um ihn zu einem Einheitsvektor zu machen.
- **Vereinfachung**: Ermöglichung einfacherer Berechnungen bei Projektionen, Zerlegungen und Transformationen in Vektorräumen.

### **Der Prozess im Detail**

Gegeben eine Menge linear unabhängiger Vektoren \\( \{ \mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \} \\) in einem Skalarproduktraum (wie \\( \mathbb{R}^n \\)), konstruiert der Gram-Schmidt-Prozess eine orthonormale Menge \\( \{ \mathbf{q}_1, \mathbf{q}_2, \ldots, \mathbf{q}_n \} \\) nach folgenden Schritten:

1. **Initialisiere den ersten Vektor**:
   \\[
   \mathbf{u}_1 = \mathbf{v}_1
   \\]
   Normalisiere, um zu erhalten:
   \\[
   \mathbf{q}_1 = \frac{\mathbf{u}_1}{\| \mathbf{u}_1 \|}
   \\]

2. **Iterative Orthogonalisierung und Normalisierung** für \\( k = 2 \\) bis \\( n \\):
   - **Orthogonalisiere**:
     \\[
     \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \text{proj}_{\mathbf{q}_j} \mathbf{v}_k
     \\]
     wobei die Projektion \\( \text{proj}_{\mathbf{q}_j} \mathbf{v}_k \\) berechnet wird als:
     \\[
     \text{proj}_{\mathbf{q}_j} \mathbf{v}_k = (\mathbf{v}_k \cdot \mathbf{q}_j) \mathbf{q}_j
     \\]
   - **Normalisiere**:
     \\[
     \mathbf{q}_k = \frac{\mathbf{u}_k}{\| \mathbf{u}_k \|}
     \\]

### **Detaillierte Schritte**

1. **Berechne \\( \mathbf{u}_1 \\) und \\( \mathbf{q}_1 \\)**:
   - \\( \mathbf{u}_1 = \mathbf{v}_1 \\)
   - \\( \mathbf{q}_1 = \frac{\mathbf{u}_1}{\| \mathbf{u}_1 \|} \\)

2. **Für jeden nachfolgenden Vektor \\( \mathbf{v}_k \\)**:
   - **Subtrahiere die Projektionen auf alle vorherigen \\( \mathbf{q}_j \\)**:
     \\[
     \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} (\mathbf{v}_k \cdot \mathbf{q}_j) \mathbf{q}_j
     \\]
   - **Normalisiere \\( \mathbf{u}_k \\) um \\( \mathbf{q}_k \\) zu erhalten**:
     \\[
     \mathbf{q}_k = \frac{\mathbf{u}_k}{\| \mathbf{u}_k \|}
     \\]

### **Beispiel**

Wenden wir den Gram-Schmidt-Prozess auf die Vektoren \\( \mathbf{v}_1 = [1, 1] \\) und \\( \mathbf{v}_2 = [1, 0] \\) in \\( \mathbb{R}^2 \\) an.

1. **Erster Vektor**:
   - \\( \mathbf{u}_1 = \mathbf{v}_1 = [1, 1] \\)
   - Normalisiere:
     \\[
     \| \mathbf{u}_1 \| = \sqrt{1^2 + 1^2} = \sqrt{2}
     \\]
     \\[
     \mathbf{q}_1 = \frac{[1, 1]}{\sqrt{2}} = \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right]
     \\]

2. **Zweiter Vektor**:
   - Berechne die Projektion von \\( \mathbf{v}_2 \\) auf \\( \mathbf{q}_1 \\):
     \\[
     \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = (\mathbf{v}_2 \cdot \mathbf{q}_1) \mathbf{q}_1
     \\]
     \\[
     \mathbf{v}_2 \cdot \mathbf{q}_1 = [1, 0] \cdot \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right] = \frac{1}{\sqrt{2}}
     \\]
     \\[
     \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = \frac{1}{\sqrt{2}} \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right] = \left[ \frac{1}{2}, \frac{1}{2} \right]
     \\]
   - Subtrahiere die Projektion:
     \\[
     \mathbf{u}_2 = \mathbf{v}_2 - \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = [1, 0] - \left[ \frac{1}{2}, \frac{1}{2} \right] = \left[ \frac{1}{2}, -\frac{1}{2} \right]
     \\]
   - Normalisiere \\( \mathbf{u}_2 \\):
     \\[
     \| \mathbf{u}_2 \| = \sqrt{\left( \frac{1}{2} \right)^2 + \left( -\frac{1}{2} \right)^2} = \frac{1}{\sqrt{2}}
     \\]
     \\[
     \mathbf{q}_2 = \frac{\left[ \frac{1}{2}, -\frac{1}{2} \right]}{\frac{1}{\sqrt{2}}} = \left[ \frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right]
     \\]

### **Ergebnis**

Die orthonormale Menge ist:
\\[
\mathbf{q}_1 = \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right], \quad \mathbf{q}_2 = \left[ \frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right]
\\]

Diese Vektoren sind orthogonal (\\( \mathbf{q}_1 \cdot \mathbf{q}_2 = 0 \\)) und haben die Einheitslänge (\\( \| \mathbf{q}_1 \| = \| \mathbf{q}_2 \| = 1 \\)).

### **Anwendungen**

- **QR-Zerlegung**: Zerlegung einer Matrix in eine orthogonale Matrix \\( Q \\) und eine obere Dreiecksmatrix \\( R \\).
- **Probleme der kleinsten Quadrate**: Finden der besten Näherungslösung für überbestimmte Systeme.
- **Numerische Methoden**: Verbesserung der Stabilität und Effizienz in computergestützten Algorithmen.

### **Zusammenfassung**

Der Gram-Schmidt-Prozess ist eine systematische Methode zur Orthonormalisierung einer Menge von Vektoren in einem Skalarproduktraum, die sicherstellt, dass der neue Satz einfacher zu handhaben ist, während der Spann der ursprünglichen Vektoren erhalten bleibt. Er ist grundlegend in der linearen Algebra und hat weitreichende Anwendungen in Mathematik, Physik und Ingenieurwesen.