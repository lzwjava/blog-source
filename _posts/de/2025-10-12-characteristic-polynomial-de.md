---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Definition und Eigenschaften des charakteristischen Polynoms
translated: true
type: note
---

In der linearen Algebra ist das **charakteristische Polynom** einer quadratischen Matrix \\( A \\) (der Größe \\( n \times n \\)) ein Polynom, das Informationen über die Eigenwerte der Matrix kodiert. Es ist definiert als:

\\[
p(\lambda) = \det(A - \lambda I)
\\]

wobei:
- \\( A \\) die \\( n \times n \\)-Matrix ist.
- \\( \lambda \\) ein Skalar ist (die Variable des Polynoms).
- \\( I \\) die \\( n \times n \\)-Einheitsmatrix ist.
- \\( \det \\) die Determinante bezeichnet.

### Wichtige Eigenschaften
1. **Form**: Das charakteristische Polynom ist ein normiertes Polynom vom Grad \\( n \\), was bedeutet, dass sein führender Koeffizient (für den \\( \lambda^n \\)-Term) 1 ist.
   - Für eine \\( 2 \times 2 \\)-Matrix \\( A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \\) lautet das charakteristische Polynom:
     \\[
     p(\lambda) = \det \begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix} = \lambda^2 - (a + d)\lambda + (ad - bc)
     \\]
     wobei \\( a + d \\) die Spur und \\( ad - bc \\) die Determinante ist.

2. **Eigenwerte**: Die Wurzeln des charakteristischen Polynoms \\( p(\lambda) = 0 \\) sind die Eigenwerte der Matrix \\( A \\). Diese können reelle oder komplexe Zahlen sein.

3. **Koeffizienten**: Die Koeffizienten des Polynoms hängen mit den Eigenschaften der Matrix zusammen:
   - Der Koeffizient von \\( \lambda^{n-1} \\) ist \\( -\text{Spur}(A) \\).
   - Der konstante Term ist \\( (-1)^n \det(A) \\).
   - Andere Koeffizienten werden durch Summen der Hauptminoren von \\( A \\) bestimmt.

4. **Invarianz**: Das charakteristische Polynom ist invariant unter Ähnlichkeitstransformationen. Wenn \\( B = P^{-1}AP \\), dann haben \\( A \\) und \\( B \\) dasselbe charakteristische Polynom.

5. **Satz von Cayley-Hamilton**: Die Matrix \\( A \\) erfüllt ihr eigenes charakteristisches Polynom, d.h. wenn \\( p(\lambda) \\) das charakteristische Polynom ist, dann gilt \\( p(A) = 0 \\) (die Nullmatrix).

### Beispiel
Für eine Matrix \\( A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \\):
- Berechne \\( A - \lambda I = \begin{bmatrix} 1 - \lambda & 2 \\ 3 & 4 - \lambda \end{bmatrix} \\).
- Das charakteristische Polynom lautet:
  \\[
  p(\lambda) = \det \begin{bmatrix} 1 - \lambda & 2 \\ 3 & 4 - \lambda \end{bmatrix} = (1 - \lambda)(4 - \lambda) - (2)(3) = \lambda^2 - 5\lambda + 4 - 6 = \lambda^2 - 5\lambda - 2
  \\]
- Die Eigenwerte ergeben sich durch Lösen von \\( \lambda^2 - 5\lambda - 2 = 0 \\).

### Anwendungen
- **Eigenwertberechnung**: Das Lösen von \\( p(\lambda) = 0 \\) ergibt die Eigenwerte.
- **Matrixeigenschaften**: Hilft bei der Bestimmung von Diagonalisierbarkeit, Invertierbarkeit und anderen Eigenschaften.
- **Differentialgleichungen**: Wird in Systemen linearer Differentialgleichungen verwendet, um Lösungen zu finden.

Wenn Sie ein bestimmtes Beispiel oder weitere Details benötigen, lassen Sie es mich wissen!