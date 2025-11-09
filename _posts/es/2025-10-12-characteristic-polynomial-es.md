---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Definición y Propiedades del Polinomio Característico
translated: true
type: note
---

En álgebra lineal, el **polinomio característico** de una matriz cuadrada \\( A \\) (de tamaño \\( n \times n \\)) es un polinomio que codifica información sobre los valores propios de la matriz. Se define como:

\\[
p(\lambda) = \det(A - \lambda I)
\\]

donde:
- \\( A \\) es la matriz \\( n \times n \\).
- \\( \lambda \\) es un escalar (la variable del polinomio).
- \\( I \\) es la matriz identidad \\( n \times n \\).
- \\( \det \\) denota el determinante.

### Características Clave
1. **Forma**: El polinomio característico es un polinomio mónico de grado \\( n \\), lo que significa que su coeficiente principal (para el término \\( \lambda^n \\)) es 1.
   - Para una matriz \\( 2 \times 2 \\) \\( A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \\), el polinomio característico es:
     \\[
     p(\lambda) = \det \begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix} = \lambda^2 - (a + d)\lambda + (ad - bc)
     \\]
     donde \\( a + d \\) es la traza y \\( ad - bc \\) es el determinante.

2. **Valores propios**: Las raíces del polinomio característico \\( p(\lambda) = 0 \\) son los valores propios de la matriz \\( A \\). Estos pueden ser números reales o complejos.

3. **Coeficientes**: Los coeficientes del polinomio están relacionados con las propiedades de la matriz:
   - El coeficiente de \\( \lambda^{n-1} \\) es \\( -\text{traza}(A) \\).
   - El término constante es \\( (-1)^n \det(A) \\).
   - Otros coeficientes están determinados por las sumas de los menores principales de \\( A \\).

4. **Invarianza**: El polinomio característico es invariante bajo transformaciones de similitud. Si \\( B = P^{-1}AP \\), entonces \\( A \\) y \\( B \\) tienen el mismo polinomio característico.

5. **Teorema de Cayley-Hamilton**: La matriz \\( A \\) satisface su propio polinomio característico, es decir, si \\( p(\lambda) \\) es el polinomio característico, entonces \\( p(A) = 0 \\) (la matriz cero).

### Ejemplo
Para una matriz \\( A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \\):
- Calcula \\( A - \lambda I = \begin{bmatrix} 1 - \lambda & 2 \\ 3 & 4 - \lambda \end{bmatrix} \\).
- El polinomio característico es:
  \\[
  p(\lambda) = \det \begin{bmatrix} 1 - \lambda & 2 \\ 3 & 4 - \lambda \end{bmatrix} = (1 - \lambda)(4 - \lambda) - (2)(3) = \lambda^2 - 5\lambda + 4 - 6 = \lambda^2 - 5\lambda - 2
  \\]
- Los valores propios se encuentran resolviendo \\( \lambda^2 - 5\lambda - 2 = 0 \\).

### Aplicaciones
- **Cálculo de valores propios**: Resolver \\( p(\lambda) = 0 \\) da los valores propios.
- **Propiedades de matrices**: Ayuda a determinar la diagonalizabilidad, la invertibilidad y otras propiedades.
- **Ecuaciones diferenciales**: Se utiliza en sistemas de ecuaciones diferenciales lineales para encontrar soluciones.

¡Si necesitas un ejemplo específico o más detalles, házmelo saber!