---
audio: false
generated: true
image: false
lang: es
layout: post
title: 'Determinante: Expansión por Linealidad y Alternación'
translated: true
type: note
---

Cuando aprendes que el determinante es una función que es

1. **multilineal** en las filas (o columnas), y
2. **alternante** (intercambiar dos filas cambia su signo),

la fórmula de expansión por cofactores surge de forma natural. Aquí tienes un paso a paso del "por qué" para el caso 3×3:

---

### 1. Determinante mediante permutaciones

La definición más general de un determinante 3×3 es

$$
\det A \;=\;
\sum_{\sigma\in S_3}\!\mathrm{sgn}(\sigma)\,a_{1,\sigma(1)}\,a_{2,\sigma(2)}\,a_{3,\sigma(3)},
$$

donde sumas sobre todas las seis permutaciones σ de {1,2,3}, y sgn(σ) es +1 para permutaciones pares y –1 para las impares.

Si las escribes todas, obtienes exactamente los seis términos:

$$
a_{11}a_{22}a_{33},\;a_{12}a_{23}a_{31},\;a_{13}a_{21}a_{32}
\;-\;
\bigl(a_{13}a_{22}a_{31}+a_{11}a_{23}a_{32}+a_{12}a_{21}a_{33}\bigr).
$$

---

### 2. Agrupación por una fila o columna

Observa que puedes **agrupar** esos seis términos según qué entrada de la primera fila usen:

* Términos que contienen \$a\_{11}\$:

  $$
    a_{11}\,(a_{22}a_{33} - a_{23}a_{32}) 
    = a_{11}\det\!\begin{pmatrix}a_{22}&a_{23}\\a_{32}&a_{33}\end{pmatrix}.
  $$
* Términos que contienen \$a\_{12}\$:

  $$
    a_{12}\,(a_{23}a_{31} - a_{21}a_{33}) 
    = -\,a_{12}\det\!\begin{pmatrix}a_{21}&a_{23}\\a_{31}&a_{33}\end{pmatrix}.
  $$
* Términos que contienen \$a\_{13}\$:

  $$
    a_{13}\,(a_{21}a_{32} - a_{22}a_{31}) 
    = \;a_{13}\det\!\begin{pmatrix}a_{21}&a_{22}\\a_{31}&a_{32}\end{pmatrix}.
  $$

Esa es exactamente la **expansión por cofactores a lo largo de la primera fila**:

$$
\det A
= a_{11}C_{11} \;+\; a_{12}C_{12} \;+\; a_{13}C_{13},
$$

donde cada cofactor $C_{1j} = (-1)^{1+j}\det(\text{minor}_{1j})$.

---

### 3. ¿Por qué "menores" y "signos"?

* **Menor**: $\det(\text{minor}_{ij})$ es el determinante de la submatriz 2×2 que obtienes al eliminar la fila i y la columna j.
* **Factor de signo** $(−1)^{i+j}$: asegura que si intercambias dos filas de $A$, el signo general cambia—exactamente como lo exige la definición por permutaciones.

Debido a que el determinante debe ser lineal en cada fila, puedes "sacar" una entrada de una fila, dejando el determinante de la matriz más pequeña multiplicado por esa entrada. La propiedad alternante fuerza esos signos $(−1)$.

---

### 4. Intuición geométrica

Para una matriz 3×3 cuyas filas son vectores $\mathbf{u},\mathbf{v},\mathbf{w}\in\mathbb{R}^3$, $\det A$ es el volumen con signo del paralelepípedo que generan.

* Expandir a lo largo de, digamos, la primera fila, significa descomponer ese volumen en "láminas" perpendiculares a cada eje coordenado.
* El área de cada lámina es el área del paralelogramo generado por los otros dos vectores-fila (un determinante 2×2), y lo escalas por la coordenada correspondiente $u_j$ de $\mathbf{u}$.
* El signo $(−1)^{1+j}$ lleva la cuenta de la orientación.

---

### 5. Generalización a $n\times n$

Todo esto funciona de la misma manera para cualquier tamaño $n$: la definición por permutaciones tiene $n!$ términos, los agrupas por una fila o columna, y cada grupo se colapsa a

$$
a_{ij}\,(-1)^{i+j}\det(\text{minor}_{ij}).
$$

Ese es el principio de **expansión por cofactores**.

---

**En resumen:**
La expansión por cofactores es simplemente la definición del determinante como suma de permutaciones, reorganizada por una fila (o columna), junto con los requisitos de linealidad y alternancia de signo. Ofrece una forma recursiva de calcular—y una imagen geométrica clara de—el determinante.