---
audio: false
generated: false
image: false
lang: es
layout: post
title: Álgebra Lineal
translated: true
---

- La **Singular Value Decomposition** (SVD) puede utilizarse para la compresión de imágenes.

- El **determinante** de una matriz indica cuánto cambia el área cuando la matriz se aplica a una forma.

- Los **valores propios** (eigenvalues) se definen mediante la ecuación \\[ \det(\lambda I - A) = 0 \\].

- El paquete `linalg` de **NumPy** puede usarse para estudiar y resolver problemas de álgebra lineal.

- Utiliza transformaciones de **álgebra lineal** en espacios de **n** dimensiones para comprender las matrices.

- Una **matriz** es un conjunto de números dispuestos en filas y columnas.

- La ecuación \\[ Ax = B \\] tiene solución cuando \\[ \text{rango}(A) = \text{rango}([A \mid B]) \\].

- El **rango** de una matriz es el número de filas (o columnas) linealmente independientes en su **forma escalonada**.

---

¿Para qué sirve el concepto de **rango**?
Indica cuántas filas conservan información durante una transformación lineal. En cambio, la **nulidad** (dimensión del espacio nulo) cuenta cuántas filas se mapean a cero.

¿Cuál es la diferencia entre una matriz y un simple arreglo de números?
Un arreglo no tiene dirección inherente, mientras que una matriz sí.

¿Cuál es la diferencia entre una matriz y un vector?
Un **vector** es una columna unidimensional de números y tiene dirección.

La multiplicación de matrices sigue una regla fija: el número de columnas de la primera matriz debe ser igual al número de filas de la segunda. Una matriz 2×3 multiplicada por una 3×4 da como resultado una matriz 2×4. En la matriz resultante, el valor en la posición (i, j) es el **producto punto** de la i-ésima fila de la matriz A y la j-ésima columna de la matriz B.

El determinante de una matriz tiene significado: si no es igual a 0, la matriz es **invertible**.