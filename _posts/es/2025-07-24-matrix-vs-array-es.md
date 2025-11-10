---
audio: false
generated: true
lang: es
layout: post
title: Matrices frente a Arreglos Multidimensionales
translated: true
type: note
---

Aquí tienes un modelo mental rápido que suele ayudar a los programadores a distinguir ambos conceptos.

---

### 1  Idea central que comparten

* **Almacenamiento en forma de cuadrícula** – Tanto una matriz matemática como un array multidimensional organizan elementos mediante múltiples índices enteros (fila/columna, o fila/col/…/k).
* **Acceso indexado** – Se accede a un elemento con una coordenada triple como `A[i][j]` (matriz → dos índices; array general → cualquier número de índices).
* **Operaciones en bloque** – Pensar en bloques en lugar de escalares fomenta código vectorizado o basado en bucles, layouts de memoria cache-friendly, uso de GPU, etc.

---

### 2  Donde se diferencian

**a. Propósito y semántica**

*Matriz*

* Puramente **matemática**: cada elemento es un número de un campo (ℝ, ℂ, …).
* Conlleva álgebra incorporada: suma, múltiplo escalar, determinante, inversa, eigen-valores/vectores, etc.
* La forma es siempre 2-D; un "tensor de rango 3" no se llama matriz.

*Array multidimensional*

* **Contenedor de programación**: puede almacenar cualquier tipo de dato, numérico o no.
* Sin álgebra inherente; las operaciones son las que programes (o las que proporcione la librería).
* El rango es arbitrario: 1-D (vector), 2-D, 5-D, … incluso estructuras irregulares (jagged).

**b. Detalles de implementación**

*Librerías de matrices* (NumPy `ndarray`, MATLAB, Eigen, BLAS, etc.)

* Suelen prestar atención al orden **row-major vs column-major** porque afecta al rendimiento de los kernels algebraicos.
* Pueden mantener metadatos como la dimensión principal (leading dimension), stride, formas triangulares/empaquetadas.
* Proporcionan operadores sobrecargados para que `C = A @ B` desencadene una multiplicación de matrices de alto rendimiento.

*Arrays generales* (Arrays en C, arrays en Java, slices en Rust, listas de listas en Python)

* El layout de memoria es específico del lenguaje: contiguo, array-de-punteros, o incluso fragmentado (en listas de Python).
* Carecen de álgebra automática; para multiplicar dos arrays 2-D hay que escribir bucles anidados o llamar a una librería matemática.
* Pueden ser sparse (dispersos), jagged (irregulares) o de tipo mixto en lenguajes de tipado dinámico.

**c. Operaciones típicas**

*Matriz* – productos escalares (dot products), descomposición LU/QR, resolver sistemas lineales, SVD, gradientes en Machine Learning, transformaciones gráficas.

*Array multidimensional* – cualquier cosa: píxeles de imagen RGBA, un mundo de vóxeles 3-D, una tabla de búsqueda (lookup table) de strings, estados de un tablero de juego.

---

### 3  Analogía en código

```python
# Perspectiva de Matriz (NumPy)
import numpy as np
A = np.array([[1, 2],
              [3, 4]])          # matriz 2×2
B = np.array([[5, 6],
              [7, 8]])
C = A @ B                       # multiplicación de matrices, con conocimiento algebraico
detA = np.linalg.det(A)         # determinante

# Perspectiva de Array multidimensional puro (Python vanilla)
table = [[1, 2], [3, 4]]        # lista de listas
value = table[1][0]             # 3
# ¿Multiplicación? Se necesitan bucles explícitos o comprehensions
product = [[sum(table[i][k]*B[k][j] for k in range(2))
           for j in range(2)] for i in range(2)]
```

---

### 4  TL;DR (Resumen)

* **Misma forma, significado diferente:** Una matriz es un array numérico 2-D *más* un conjunto de leyes de álgebra lineal; un array multidimensional es solo un contenedor indexado—nada más, nada menos.
* En la práctica, a menudo almacenas matrices *dentro* de arrays multidimensionales, y luego dependes de librerías para dotarlas de semántica de matriz y velocidad.