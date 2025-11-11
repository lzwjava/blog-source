---
audio: false
generated: true
lang: es
layout: post
title: El Núcleo de una Transformación Lineal
translated: true
type: note
---

El **kernel** de una transformación lineal es el conjunto de todos los vectores de entrada que la transformación mapea al vector cero.

### Definición:
Si \\( T: V \to W \\) es una transformación lineal entre dos espacios vectoriales \\( V \\) y \\( W \\), entonces el **kernel** (o **espacio nulo**) de \\( T \\) es:

\\[
\ker(T) = \{ v \in V \mid T(v) = 0 \}
\\]

### Propiedades Clave:
1. **Subespacio**: El kernel de una transformación lineal es siempre un subespacio del dominio \\( V \\).
2. **Dimensión**: La dimensión del kernel se denomina **nulidad** de la transformación.
3. **Relación con la Inyectividad**:
   - Si \\( \ker(T) = \{0\} \\), entonces \\( T \\) es **inyectiva** (uno a uno).
   - Si \\( \ker(T) \\) tiene dimensión mayor que cero, entonces \\( T \\) no es inyectiva.

### Ejemplo:
Considera la transformación matricial \\( T: \mathbb{R}^3 \to \mathbb{R}^2 \\) dada por:

\\[
T(x, y, z) = (x + y, y + z)
\\]

Escribiendo esto como una matriz,

<div>
$$
T \begin{bmatrix} x \\ y \\ z \end{bmatrix} =
\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
$$
</div>

Para encontrar el kernel, resuelve:

\\[
\begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}
\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\\]

Esto da el sistema:

\\[
x + y = 0
\\]
\\[
y + z = 0
\\]

Resolviendo para \\( x, y, z \\):

\\[
x = -y, \quad z = -y
\\]

Por lo tanto, el kernel consiste en todos los vectores de la forma:

<div>
$$
\ker(T) = \text{span} \left\{ \begin{bmatrix} -1 \\ 1 \\ -1 \end{bmatrix} \right\}
$$
</div>

que es un subespacio unidimensional de \\( \mathbb{R}^3 \\).

¡Avísame si necesitas más aclaraciones!