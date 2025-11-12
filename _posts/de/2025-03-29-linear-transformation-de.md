---
audio: false
generated: true
lang: de
layout: post
title: Lineare Transformationen
translated: true
type: note
---

**Definition, Beispiele, Matrixdarstellung, Kern, Bild, Eigenschaften (Injektivität, Surjektivität)**

Lineare Abbildungen sind grundlegend in der linearen Algebra und bilden eine Brücke zwischen Vektorräumen und Matrizen. Dieses Tutorial behandelt:
- **Definition** linearer Abbildungen
- **Beispiele** häufiger linearer Abbildungen
- **Matrixdarstellung** linearer Abbildungen
- **Kern (Nullraum)** und **Bild (Wertebereich)**
- **Eigenschaften**: Injektivität (eineindeutig) und Surjektivität (onto)

---

## **1. Definition einer linearen Abbildung**
Eine **lineare Abbildung** (oder linearer Homomorphismus) zwischen zwei Vektorräumen \\( V \\) und \\( W \\) über einem Körper \\( \mathbb{F} \\) (üblicherweise \\( \mathbb{R} \\) oder \\( \mathbb{C} \\)) ist eine Funktion \\( T: V \to W \\), die folgende Bedingungen erfüllt:
1. **Additivität**:
   \\[
   T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \quad \forall \mathbf{u}, \mathbf{v} \in V
   \\]
2. **Homogenität (Skalarmultiplikation)**:
   \\[
   T(c \mathbf{v}) = c T(\mathbf{v}) \quad \forall c \in \mathbb{F}, \mathbf{v} \in V
   \\]

**Grundidee**: Lineare Abbildungen erhalten Vektoraddition und Skalarmultiplikation.

---

## **2. Beispiele linearer Abbildungen**

### **(a) Nullabbildung**
- \\( T(\mathbf{v}) = \mathbf{0} \\) für alle \\( \mathbf{v} \in V \\).

### **(b) Identitätsabbildung**
- \\( T(\mathbf{v}) = \mathbf{v} \\) für alle \\( \mathbf{v} \in V \\).

### **(c) Rotation in \\( \mathbb{R}^2 \\)**
- Drehung eines Vektors um den Winkel \\( \theta \\):
  \\[
  T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
  \\]

### **(d) Differentiation (Polynomraum)**
- \\( T: P_n \to P_{n-1} \\), wobei \\( T(p(x)) = p'(x) \\).

### **(e) Matrixmultiplikation**
- Für eine feste \\( m \times n \\)-Matrix \\( A \\) ist \\( T: \mathbb{R}^n \to \mathbb{R}^m \\) definiert durch \\( T(\mathbf{x}) = A\mathbf{x} \\).

---

## **3. Matrixdarstellung linearer Abbildungen**
Jede lineare Abbildung \\( T: \mathbb{R}^n \to \mathbb{R}^m \\) kann durch eine \\( m \times n \\)-Matrix \\( A \\) dargestellt werden, sodass gilt:
\\[
T(\mathbf{x}) = A\mathbf{x}
\\]

### **Wie man die Matrix \\( A \\) findet**
1. Wende \\( T \\) auf die Standardbasisvektoren \\( \mathbf{e}_1, \mathbf{e}_2, \dots, \mathbf{e}_n \\) von \\( \mathbb{R}^n \\) an.
2. Die Spalten von \\( A \\) sind \\( T(\mathbf{e}_1), T(\mathbf{e}_2), \dots, T(\mathbf{e}_n) \\).

**Beispiel**:
Sei \\( T: \mathbb{R}^2 \to \mathbb{R}^2 \\) definiert durch:
\\[
T \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2x + y \\ x - 3y \end{pmatrix}
\\]
- Berechne \\( T(\mathbf{e}_1) = T(1, 0) = (2, 1) \\)
- Berechne \\( T(\mathbf{e}_2) = T(0, 1) = (1, -3) \\)
- Somit ist die Matrix \\( A \\):
  \\[
  A = \begin{pmatrix} 2 & 1 \\ 1 & -3 \end{pmatrix}
  \\]

---

## **4. Kern (Nullraum) und Bild (Wertebereich)**

### **(a) Kern (Nullraum)**
Der **Kern** von \\( T \\) ist die Menge aller Vektoren in \\( V \\), die auf \\( \mathbf{0} \\) abgebildet werden:
\\[
\ker(T) = \{ \mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0} \}
\\]

**Eigenschaften**:
- \\( \ker(T) \\) ist ein Untervektorraum von \\( V \\).
- \\( T \\) ist **injektiv (eineindeutig)** genau dann, wenn \\( \ker(T) = \{ \mathbf{0} \} \\).

**Beispiel**:
Für \\( T(\mathbf{x}) = A\mathbf{x} \\) mit \\( A = \begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix} \\) ist
\\[
\ker(T) = \text{Span} \left\{ \begin{pmatrix} -2 \\ 1 \end{pmatrix} \right\}
\\]

### **(b) Bild (Wertebereich)**
Das **Bild** von \\( T \\) ist die Menge aller Ausgaben in \\( W \\):
\\[
\text{Im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \}
\\]

**Eigenschaften**:
- \\( \text{Im}(T) \\) ist ein Untervektorraum von \\( W \\).
- \\( T \\) ist **surjektiv (onto)** genau dann, wenn \\( \text{Im}(T) = W \\).

**Beispiel**:
Für \\( T(\mathbf{x}) = A\mathbf{x} \\) mit \\( A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix} \\) ist
\\[
\text{Im}(T) = \text{Span} \left\{ \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \right\}
\\]

---

## **5. Eigenschaften: Injektivität und Surjektivität**

### **(a) Injektivität (Eineindeutigkeit)**
Eine lineare Abbildung \\( T \\) ist **injektiv**, wenn gilt:
\\[
T(\mathbf{u}) = T(\mathbf{v}) \implies \mathbf{u} = \mathbf{v}
\\]
**Test**:
- \\( T \\) ist injektiv \\( \iff \ker(T) = \{ \mathbf{0}} \\).
- Wenn \\( \dim(V) < \dim(W) \\), dann ist \\( T \\) möglicherweise nicht injektiv.

### **(b) Surjektivität (Onto)**
Eine lineare Abbildung \\( T \\) ist **surjektiv**, wenn gilt:
\\[
\forall \mathbf{w} \in W, \exists \mathbf{v} \in V \text{ mit } T(\mathbf{v}) = \mathbf{w}
\\]
**Test**:
- \\( T \\) ist surjektiv \\( \iff \text{Im}(T) = W \\).
- Wenn \\( \dim(V) > \dim(W) \\), dann ist \\( T \\) möglicherweise nicht surjektiv.

### **(c) Dimensionssatz (Rangsatz)**
Für \\( T: V \to W \\) gilt:
\\[
\dim(V) = \dim(\ker(T)) + \dim(\text{Im}(T))
\\]
- **Rang** \\( = \dim(\text{Im}(T)) \\)
- **Nullität** \\( = \dim(\ker(T)) \\)

**Beispiel**:
Wenn \\( T: \mathbb{R}^3 \to \mathbb{R}^2 \\) und \\( \dim(\ker(T)) = 1 \\), dann ist \\( \dim(\text{Im}(T)) = 2 \\).

---

## **Zusammenfassung**

| Konzept | Definition | Wichtige Eigenschaft |
|---------|------------|--------------|
| **Lineare Abbildung** | \\( T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \\) und \\( T(c\mathbf{v}) = cT(\mathbf{v}) \\) | Erhält lineare Struktur |
| **Matrixdarstellung** | \\( T(\mathbf{x}) = A\mathbf{x} \\), wobei die Spalten von \\( A \\) die \\( T(\mathbf{e}_i) \\) sind | Kodiert die Abbildung |
| **Kern** | \\( \ker(T) = \{ \mathbf{v} \mid T(\mathbf{v}) = \mathbf{0} \} \\) | Misst Injektivität |
| **Bild** | \\( \text{Im}(T) = \{ T(\mathbf{v}) \mid \mathbf{v} \in V \} \\) | Misst Surjektivität |
| **Injektivität** | \\( \ker(T) = \{ \mathbf{0} \} \\) | Eineindeutig |
| **Surjektivität** | \\( \text{Im}(T) = W \\) | Onto |

---

## **Übungsaufgaben**
1. Finde die Matrixdarstellung von \\( T(x, y, z) = (2x - y, y + 3z) \\).
2. Bestimme, ob \\( T(\mathbf{x}) = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \mathbf{x} \\) injektiv/surjektiv ist.
3. Berechne \\( \ker(T) \\) und \\( \text{Im}(T) \\) für \\( T(x, y) = (x + y, 2x - y, x) \\).

---

Dieses Tutorial behandelt die Kernkonzepte linearer Abbildungen, wie sie typischerweise in einem Grundstudium der linearen Algebra gelehrt werden. Lass mich wissen, wenn du weitere Erklärungen oder zusätzliche Beispiele benötigst!