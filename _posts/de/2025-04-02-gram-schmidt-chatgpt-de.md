---
audio: false
generated: true
lang: de
layout: post
title: Gram-Schmidt-Verfahren
translated: true
type: note
---

Der **Gram-Schmidt-Prozess** ist ein Verfahren zur Orthonormalisierung einer Menge linear unabhängiger Vektoren in einem Innenproduktraum (typischerweise \\(\mathbb{R}^n\\) oder \\(\mathbb{C}^n\\)). Er wandelt eine gegebene Basis in eine **Orthonormalbasis** um, bei der die Vektoren zueinander orthogonal sind und die Länge 1 haben.

---

### **Algorithmus: Gram-Schmidt-Prozess**
Gegeben sei eine Menge **linear unabhängiger** Vektoren \\( \{v_1, v_2, \dots, v_n\} \\) in einem Innenproduktraum. Wir konstruieren eine **Orthonormalbasis** \\( \{u_1, u_2, \dots, u_n\} \\) wie folgt:

1. **Schritt 1: Berechne den ersten orthonormalen Vektor**  
   \\[
   u_1 = \frac{v_1}{\|v_1\|}
   \\]
   
2. **Schritt 2: Mache den zweiten Vektor orthogonal zum ersten und normalisiere ihn**  
   \\[
   v_2' = v_2 - \text{proj}_{u_1}(v_2) = v_2 - \frac{\langle v_2, u_1 \rangle}{\langle u_1, u_1 \rangle} u_1
   \\]
   \\[
   u_2 = \frac{v_2'}{\|v_2'\|}
   \\]

3. **Schritt 3: Wiederhole für die verbleibenden Vektoren**  
   Für \\( k = 3, \dots, n \\):
   \\[
   v_k' = v_k - \sum_{j=1}^{k-1} \frac{\langle v_k, u_j \rangle}{\langle u_j, u_j \rangle} u_j
   \\]
   \\[
   u_k = \frac{v_k'}{\|v_k'\|}
   \\]

Hierbei stellt \\( \text{proj}_{u_j}(v_k) = \frac{\langle v_k, u_j \rangle}{\langle u_j, u_j \rangle} u_j \\) die Projektion von \\( v_k \\) auf \\( u_j \\) dar.

---

### **Beispiel: Anwendung von Gram-Schmidt auf \\(\mathbb{R}^3\\)**  
Gegeben seien die Vektoren:

\\[
v_1 = (1, 1, 0), \quad v_2 = (1, 0, 1), \quad v_3 = (0, 1, 1)
\\]

#### **Schritt 1: Normalisiere \\( v_1 \\)**
\\[
u_1 = \frac{v_1}{\|v_1\|} = \frac{(1,1,0)}{\sqrt{2}} = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0\right)
\\]

#### **Schritt 2: Orthogonalisiere \\( v_2 \\) gegenüber \\( u_1 \\)**
\\[
\text{proj}_{u_1}(v_2) = \frac{\langle v_2, u_1 \rangle}{\langle u_1, u_1 \rangle} u_1
\\]

\\[
= \frac{(1,0,1) \cdot (1/\sqrt{2}, 1/\sqrt{2}, 0)}{1} \cdot (1/\sqrt{2}, 1/\sqrt{2}, 0)
\\]

\\[
= \frac{1 \cdot 1/\sqrt{2} + 0 \cdot 1/\sqrt{2} + 1 \cdot 0}{1} \cdot (1/\sqrt{2}, 1/\sqrt{2}, 0)
\\]

\\[
= \frac{1/\sqrt{2}}{1} \cdot (1/\sqrt{2}, 1/\sqrt{2}, 0) = \left(\frac{1}{2}, \frac{1}{2}, 0\right)
\\]

\\[
v_2' = v_2 - \text{proj}_{u_1}(v_2) = \left(1,0,1\right) - \left(\frac{1}{2}, \frac{1}{2}, 0\right) = \left(\frac{1}{2}, -\frac{1}{2}, 1\right)
\\]

\\[
u_2 = \frac{v_2'}{\|v_2'\|}
\\]

\\[
= \frac{\left(\frac{1}{2}, -\frac{1}{2}, 1\right)}{\sqrt{\left(\frac{1}{2}\right)^2 + \left(-\frac{1}{2}\right)^2 + (1)^2}}
\\]

\\[
= \frac{\left(\frac{1}{2}, -\frac{1}{2}, 1\right)}{\sqrt{\frac{1}{4} + \frac{1}{4} + 1}} = \frac{\left(\frac{1}{2}, -\frac{1}{2}, 1\right)}{\sqrt{\frac{3}{2}}}
\\]

#### **Schritt 3: Orthogonalisiere \\( v_3 \\) gegenüber \\( u_1 \\) und \\( u_2 \\)**
Befolge das gleiche Verfahren für \\( v_3 \\), projiziere auf \\( u_1 \\) und \\( u_2 \\) und normalisiere anschließend.

---

### **Zusammenfassung**
Der **Gram-Schmidt-Prozess** transformiert eine Menge linear unabhängiger Vektoren Schritt für Schritt in eine **Orthonormalbasis**, wobei sichergestellt wird, dass jeder Vektor orthogonal zu den vorherigen ist und die Länge 1 hat. Dieser Prozess ist grundlegend für Anwendungen wie:

- QR-Zerlegung in der numerischen linearen Algebra.
- Konstruktion von Orthonormalbasen für Funktionenräume in der Fourieranalyse.
- Verbesserung der numerischen Stabilität in computergestützten Algorithmen.

Lass mich wissen, wenn du das vollständige Beispiel explizit durchgerechnet haben möchtest oder wenn ich einen Teil näher erläutern soll! 🚀