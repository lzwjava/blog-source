---
audio: false
generated: true
lang: es
layout: post
title: Álgebra Lineal Plus Nota
translated: true
type: note
---

En álgebra lineal, dos matrices cuadradas \\( A \\) y \\( B \\) se dicen similares si existe una matriz invertible \\( P \\) tal que:

\\[ B = P^{-1}AP \\]

Esta relación se conoce como una transformación de similitud. La matriz \\( P \\) se llama la matriz de cambio de base, y transforma la matriz \\( A \\) en la matriz \\( B \\).

### Propiedades Clave de Matrices Similares:
1. **Mismos Valores Propios**: Las matrices similares tienen los mismos valores propios. Esto se debe a que los valores propios se conservan bajo transformaciones de similitud.
2. **Mismo Determinante**: El determinante de matrices similares es el mismo porque \\(\det(P^{-1}AP) = \det(A)\\).
3. **Misma Traza**: La traza (suma de los elementos de la diagonal) de matrices similares es la misma porque \\(\text{tr}(P^{-1}AP) = \text{tr}(A)\\).
4. **Mismo Rango**: Las matrices similares tienen el mismo rango.
5. **Mismo Polinomio Característico**: Las matrices similares comparten el mismo polinomio característico.

### Intuición:
Las matrices similares representan la misma transformación lineal pero en diferentes bases. La matriz \\( P \\) puede pensarse como un cambio de coordenadas, transformando la base en la que se representa la transformación lineal.

### Ejemplo:
Considera dos matrices \\( A \\) y \\( B \\):

\\[ A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}, \quad B = \begin{pmatrix} 3 & 0 \\ 2 & 1 \end{pmatrix} \\]

Para verificar si son similares, necesitamos encontrar una matriz invertible \\( P \\) tal que \\( B = P^{-1}AP \\).

¿Te gustaría ver un ejemplo de cómo encontrar dicha matriz \\( P \\) para matrices específicas \\( A \\) y \\( B \\)?

---

Sí, la matriz:

\\[
A = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\\]

sí tiene una Descomposición en Valores Singulares (SVD). Repasemos el proceso para encontrar la SVD de esta matriz.

### Paso 1: Calcular \\( A^T A \\)

Primero, calculamos la matriz \\( A^T A \\):

\\[
A^T = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}
\\]

Ahora, multiplicamos \\( A^T \\) y \\( A \\):

\\[
A^T A = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} = \begin{bmatrix} 1 + 9 & 2 + 12 \\ 2 + 12 & 4 + 16 \end{bmatrix} = \begin{bmatrix} 10 & 14 \\ 14 & 20 \end{bmatrix}
\\]

### Paso 2: Valores Propios y Vectores Propios de \\( A^T A \\)

Para encontrar los valores singulares, necesitamos los valores propios de \\( A^T A \\). Resolvemos la ecuación característica \\( \text{det}(A^T A - \lambda I) = 0 \\):

\\[
\text{det}\begin{bmatrix} 10 - \lambda & 14 \\ 14 & 20 - \lambda \end{bmatrix} = 0
\\]

Esto da:

\\[
(10 - \lambda)(20 - \lambda) - 14 \times 14 = 0
\\]

\\[
\lambda^2 - 30\lambda + 100 - 196 = 0
\\]

\\[
\lambda^2 - 30\lambda - 96 = 0
\\]

Resolviendo esta ecuación cuadrática:

\\[
\lambda = \frac{-(-30) \pm \sqrt{(-30)^2 - 4(1)(-96)}}{2(1)} = \frac{30 \pm \sqrt{900 + 384}}{2} = \frac{30 \pm \sqrt{1284}}{2}
\\]

\\[
\lambda = \frac{30 \pm 35.86}{2}
\\]

Así, los valores propios son:

\\[
\lambda_1 \approx 32.93 \quad \text{y} \quad \lambda_2 \approx 0.93
\\]

### Paso 3: Calcular los Valores Singulares

Los valores singulares son las raíces cuadradas de los valores propios de \\( A^T A \\). Por lo tanto, tenemos:

\\[
\sigma_1 = \sqrt{32.93} \approx 5.73 \quad \text{y} \quad \sigma_2 = \sqrt{0.93} \approx 0.96
\\]

### Paso 4: Calcular las Matrices \\( U \\) y \\( V \\)

Para encontrar las matrices \\( U \\) y \\( V \\), necesitamos calcular los vectores propios de \\( A^T A \\) y \\( A A^T \\), pero dado que esto requiere pasos detallados que van más allá del cálculo básico, normalmente se resolverían numéricamente.

Sin embargo, basándonos en los valores propios anteriores, sabemos que los valores singulares son \\( 5.73 \\) y \\( 0.96 \\), y \\( U \\) y \\( V \\) serían matrices ortogonales correspondientes a los vectores propios de \\( A A^T \\) y \\( A^T A \\).

Así, la SVD de la matriz \\( A \\) es:

\\[
A = U \Sigma V^T
\\]

Donde:

- \\( \Sigma = \begin{bmatrix} 5.73 & 0 \\ 0 & 0.96 \end{bmatrix} \\)
- \\( U \\) y \\( V \\) son matrices ortogonales correspondientes a los vectores propios de \\( A A^T \\) y \\( A^T A \\).

Puedes encontrar los valores exactos para \\( U \\) y \\( V \\) resolviendo los problemas de valores propios para \\( A^T A \\) y \\( A A^T \\).

---

La declaración describe el comportamiento de la matriz como una transformación lineal. Desglosémoslo para entender por qué sucede esto:

### Matriz como una Transformación Lineal:
- **Espacio de Entrada**: La matriz opera sobre vectores de un espacio tridimensional (ya que tiene 3 columnas). Esto significa que toma vectores de 3 componentes como entrada.
- **Espacio de Salida**: La matriz mapea estos vectores a un espacio bidimensional (ya que tiene 2 filas). Esto significa que produce vectores de 2 componentes como salida.

### Espacio Nulo:
- **Definición**: El espacio nulo (o kernel) de una matriz consiste en todos los vectores que, al ser multiplicados por la matriz, resultan en el vector cero.
- **Dimensión**: La nulidad de la matriz es la dimensión de este espacio nulo. En este caso, la nulidad es 1, lo que significa que hay un subespacio unidimensional de vectores que se mapean a cero.
- **Interpretación**: Este subespacio unidimensional representa una línea (en el espacio de entrada tridimensional) de vectores que son "colapsados" o "comprimidos" al vector cero en el espacio de salida bidimensional.

### Por Qué Sucede Esto:
- **Teorema de Rango-Nulidad**: El teorema establece que para cualquier matriz \\(m \times n\\), el rango (dimensión del espacio de columnas) más la nulidad (dimensión del espacio nulo) es igual al número de columnas \\(n\\). Aquí, el rango es 2 y el número de columnas es 3, por lo que la nulidad debe ser 1.
- **Dependencia Lineal**: La existencia de un espacio nulo con dimensión 1 indica que hay alguna redundancia o dependencia lineal entre las columnas de la matriz. Esto significa que una de las columnas puede expresarse como una combinación lineal de las otras dos.

### Visualización:
- Imagina un espacio 3D donde todos los puntos en una línea específica (el espacio nulo) se mapean al origen en un espacio 2D. Esta línea representa los vectores que se "pierden" o son "ignorados" por la transformación definida por la matriz.

Este comportamiento es un aspecto fundamental de las transformaciones lineales y destaca cómo las matrices pueden reducir la dimensionalidad del espacio sobre el que actúan.

---

Para determinar qué opción es necesaria para que una matriz sea diagonalizable, examinaré cada declaración.

Una matriz cuadrada A es diagonalizable si y solo si existe una matriz invertible P tal que P⁻¹AP es una matriz diagonal. Esto sucede precisamente cuando A tiene un conjunto completo de vectores propios linealmente independientes.

Analicemos cada opción:

a) La matriz debe tener al menos un valor propio.
Si bien todas las matrices n×n tienen al menos un valor propio (en el campo complejo), esto por sí solo no garantiza la diagonalizabilidad. Una matriz podría tener valores propios pero aún no ser diagonalizable si no tiene suficientes vectores propios linealmente independientes.

b) La matriz debe tener valores propios distintos.
Tener valores propios distintos es suficiente pero no necesario para la diagonalizabilidad. Una matriz con valores propios repetidos aún puede ser diagonalizable si tiene suficientes vectores propios linealmente independientes asociados con esos valores propios repetidos.

c) La matriz debe tener suficientes vectores propios linealmente independientes.
Esta es exactamente la condición necesaria y suficiente para la diagonalizabilidad. Específicamente, una matriz n×n es diagonalizable si y solo si tiene n vectores propios linealmente independientes, formando una base para el espacio vectorial.

Por lo tanto, la opción c) es la respuesta correcta: una matriz es diagonalizable si y solo si tiene suficientes vectores propios linealmente independientes.