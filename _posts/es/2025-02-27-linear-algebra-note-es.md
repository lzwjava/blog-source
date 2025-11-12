---
audio: false
generated: true
lang: es
layout: post
title: Álgebra Lineal Notas
translated: true
type: note
---

## Ejemplo

Considere la forma cuadrática en dos variables \\( x \\) e \\(y\\):

\\[ Q(x, y) = 2x^2 + 4xy + 3y^2 \\]

### Transformación Paso a Paso a la Forma Canónica

1. **Representación Matricial:**
   - Escriba la forma cuadrática como una ecuación matricial. La matriz \\(A\\) asociada a esta forma cuadrática es:

\\[
A = \begin{pmatrix}
2 & 2 \\
2 & 3
\end{pmatrix}
\\]

   Nótese que los elementos fuera de la diagonal son la mitad del coeficiente del término \\(xy\\).

2. **Encontrar Valores Propios y Vectores Propios:**
   - Calcule los valores propios de \\(A\\) resolviendo la ecuación característica \\( \det(A - \lambda I) = 0 \\).
   - Para cada valor propio, encuentre el vector propio correspondiente.

3. **Diagonalización:**
   - Construya una matriz \\(P\\) cuyas columnas sean los vectores propios de \\(A\\).
   - Calcule \\(D = P^TAP\\), que será una matriz diagonal con los valores propios de \\(A\\) en la diagonal.

4. **Cambio de Variables:**
   - Defina nuevas variables \\(u\\) y \\(v\\) tales que:

\\[
\begin{pmatrix}
x \\
y
\end{pmatrix} = P \begin{pmatrix}
u \\
v
\end{pmatrix}
\\]

   - Sustituya estas en la forma cuadrática original para obtener una nueva forma en términos de \\(u\\) y \\(v\\).

5. **Forma Canónica:**
   - La forma cuadrática resultante estará en la forma canónica, que es una suma de cuadrados:

\\[
Q(u, v) = \lambda_1 u^2 + \lambda_2 v^2
\\]

   donde \\(\lambda_1\\) y \\(\lambda_2\\) son los valores propios de \\(A\\).

### Interpretación

- La forma canónica revela la naturaleza geométrica de la forma cuadrática.
- Si ambos valores propios son positivos, la forma es definida positiva.
- Si ambos son negativos, es definida negativa.
- Si tienen signos diferentes, la forma es indefinida.

Este proceso simplifica la forma cuadrática y facilita el análisis de sus propiedades.

---

En el contexto de las formas cuadráticas, el término "二次型的规范形" se traduce al inglés como "canonical form of a quadratic form". Comprender este concepto implica reconocer cómo una forma cuadrática puede simplificarse o transformarse en una forma estándar mediante técnicas de álgebra lineal.

### Formas Cuadráticas
Una forma cuadrática es un polinomio homogéneo de grado dos en varias variables. Por ejemplo, en dos variables \\(x\\) e \\(y\\), una forma cuadrática podría verse como:

\\[ Q(x, y) = ax^2 + bxy + cy^2 \\]

### Forma Canónica
La forma canónica de una forma cuadrática es una versión simplificada que revela propiedades esenciales, como el rango y la signatura (el número de valores propios positivos, negativos y cero). Para lograr esta forma, normalmente realizamos un cambio de variables, a menudo mediante diagonalización u otras transformaciones ortogonales.

#### Pasos para Encontrar la Forma Canónica:
1. **Representación Matricial:** Represente la forma cuadrática como una matriz simétrica \\(A\\). Para el ejemplo anterior, la matriz sería:
\\[
A = \begin{pmatrix}
a & \frac{b}{2} \\
\frac{b}{2} & c
\end{pmatrix}
\\]

2. **Diagonalización:** Encuentre una matriz ortogonal \\(P\\) tal que \\(P^TAP\\) sea una matriz diagonal \\(D\\). Este proceso implica encontrar los valores propios y vectores propios de \\(A\\).

3. **Cambio de Variables:** Use la matriz \\(P\\) para cambiar las variables, transformando la forma cuadrática original en una suma de cuadrados, cada uno correspondiente a un valor propio.

4. **Forma Canónica:** La matriz diagonal resultante \\(D\\) representa la forma canónica de la forma cuadrática, donde cada entrada diagonal es un valor propio de \\(A\\).

La forma canónica ayuda a analizar las propiedades de la forma cuadrática, como determinar si es definida positiva, definida negativa o indefinida, lo cual es crucial en optimización y otras aplicaciones matemáticas.

---

La **forma normal de una forma cuadrática** se refiere a la representación estándar simplificada de una forma cuadrática después de aplicar un cambio de variables apropiado. Esta transformación hace que la estructura de la forma cuadrática sea más clara y fácil de analizar.

---

### **1. Definición de una Forma Cuadrática**
Una **forma cuadrática** en \\( n \\) variables es una función de la forma:

\\[
Q(x) = x^T A x
\\]

donde:
- \\( x = (x_1, x_2, \dots, x_n)^T \\) es un vector columna \\( n \\)-dimensional,
- \\( A \\) es una matriz simétrica \\( n \times n \\).

El objetivo es transformar esta forma cuadrática en una forma más simple y estandarizada.

---

### **2. Encontrar la Forma Normal**
Para simplificar la forma cuadrática, utilizamos un cambio de variables ortogonal:

1. **Encontrar los Valores Propios y Vectores Propios de \\( A \\):**
   - Calcule los valores propios \\( \lambda_1, \lambda_2, \dots, \lambda_n \\).
   - Encuentre una base ortonormal de vectores propios.

2. **Diagonalización de \\( A \\):**
   - Dado que \\( A \\) es simétrica, puede ser diagonalizada como \\( A = P D P^T \\), donde:
     - \\( P \\) es una matriz ortogonal (cuyas columnas son vectores propios de \\( A \\)).
     - \\( D \\) es una matriz diagonal con los valores propios \\( \lambda_1, \lambda_2, \dots, \lambda_n \\) en la diagonal.

3. **Cambio de Variables:**
   - Defina una nueva variable \\( y = P^T x \\), entonces:

\\[
Q(x) = x^T A x = (P y)^T A (P y) = y^T (P^T A P) y = y^T D y
\\]

   - Dado que \\( D \\) es diagonal, la forma cuadrática se simplifica a:

\\[
Q(y) = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \dots + \lambda_n y_n^2
\\]

   Esta es la **forma normal de la forma cuadrática**.

---

### **3. Interpretación de la Forma Normal**
- La forma normal expresa la forma cuadrática como una suma de términos al cuadrado, ponderados por los valores propios.
- Los **signos de los valores propios** determinan la naturaleza de la forma cuadrática:
  - Si todos los valores propios son positivos, la forma es **definida positiva**.
  - Si todos son negativos, es **definida negativa**.
  - Si hay signos mixtos, es **indefinida**.

Este proceso es esencial en **secciones cónicas, optimización y ecuaciones diferenciales**, ya que ayuda a clasificar superficies y funciones cuadráticas.

¿Le gustaría un ejemplo más detallado?