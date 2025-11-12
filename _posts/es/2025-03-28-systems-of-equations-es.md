---
audio: false
generated: true
lang: es
layout: post
title: Sistemas de Ecuaciones y Eliminación Gaussiana
translated: true
type: note
---

Este tutorial proporciona una guía detallada sobre **sistemas de ecuaciones**, su representación, soluciones y el método de **eliminación gaussiana** utilizado para resolverlos.

---

## **1. Sistemas de Ecuaciones: Definición y Representación**

Un **sistema de ecuaciones lineales** consiste en múltiples ecuaciones lineales que comparten variables. Un sistema general con \\( n \\) variables y \\( m \\) ecuaciones se puede escribir como:

\\[
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\
\vdots & \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n &= b_m
\end{aligned}
\\]

donde:
- \\( x_1, x_2, \dots, x_n \\) son las variables desconocidas.
- \\( a_{ij} \\) son los coeficientes.
- \\( b_1, b_2, \dots, b_m \\) son las constantes del lado derecho.

### **Representación Matricial**

Un sistema de ecuaciones se puede representar usando **matrices**:

\\[
A \mathbf{x} = \mathbf{b}
\\]

donde:

- \\( A \\) es la **matriz de coeficientes**:

  \\[
  A =
  \begin{bmatrix}
  a_{11} & a_{12} & \dots & a_{1n} \\
  a_{21} & a_{22} & \dots & a_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  a_{m1} & a_{m2} & \dots & a_{mn}
  \end{bmatrix}
  \\]

- \\( \mathbf{x} \\) es el **vector columna de variables**:

  \\[
  \mathbf{x} =
  \begin{bmatrix}
  x_1 \\
  x_2 \\
  \vdots \\
  x_n
  \end{bmatrix}
  \\]

- \\( \mathbf{b} \\) es el **vector columna de constantes**:

  \\[
  \mathbf{b} =
  \begin{bmatrix}
  b_1 \\
  b_2 \\
  \vdots \\
  b_m
  \end{bmatrix}
  \\]

La **matriz aumentada** se escribe como:

\\[
[A | \mathbf{b}]
\\]

Ejemplo:
\\[
\begin{aligned}
2x + 3y &= 8 \\
5x - y &= 3
\end{aligned}
\\]

Representación matricial:
\\[
\begin{bmatrix}
2 & 3 \\
5 & -1
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
8 \\
3
\end{bmatrix}
\\]

Matriz aumentada:
\\[
\left[
\begin{array}{cc|c}
2 & 3 & 8 \\
5 & -1 & 3
\end{array}
\right]
\\]

---

## **2. Método de Eliminación Gaussiana**

La eliminación gaussiana es un método sistemático para resolver sistemas de ecuaciones transformando la matriz aumentada a **forma escalonada por filas (REF)** y luego resolviendo para las variables usando **sustitución hacia atrás**.

### **Pasos de la Eliminación Gaussiana**
1. **Convertir la matriz aumentada a una forma triangular superior (escalonada por filas)** usando operaciones de fila:
   - Intercambiar filas si es necesario.
   - Multiplicar una fila por una constante distinta de cero.
   - Sumar o restar un múltiplo de una fila a otra.

2. **Sustitución hacia atrás** para encontrar la solución.

---

### **Ejemplo 1: Resolviendo un Sistema usando Eliminación Gaussiana**

Resuelve el sistema:
\\[
\begin{aligned}
2x + y - z &= 3 \\
4x - 6y &= 2 \\
-2x + 7y + 2z &= 5
\end{aligned}
\\]

#### **Paso 1: Convertir a Matriz Aumentada**
\\[
\left[
\begin{array}{ccc|c}
2 & 1 & -1 & 3 \\
4 & -6 & 0 & 2 \\
-2 & 7 & 2 & 5
\end{array}
\right]
\\]

#### **Paso 2: Hacer que el Primer Pivote sea 1**
Divide la fila 1 entre 2:
\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\
4 & -6 & 0 & 2 \\
-2 & 7 & 2 & 5
\end{array}
\right]
\\]

#### **Paso 3: Eliminar la Primera Columna Debajo del Pivote**
Reemplaza la fila 2 restando 4 veces la fila 1:
Reemplaza la fila 3 sumando 2 veces la fila 1:

\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\
0 & -8 & 2 & -4 \\
0 & 8 & 1 & 8
\end{array}
\right]
\\]

#### **Paso 4: Hacer que el Segundo Pivote sea 1**
Divide la fila 2 entre -8:

\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\
0 & 1 & -0.25 & 0.5 \\
0 & 8 & 1 & 8
\end{array}
\right]
\\]

#### **Paso 5: Eliminar la Segunda Columna Debajo del Pivote**
Reemplaza la fila 3 restando 8 veces la fila 2:

\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\
0 & 1 & -0.25 & 0.5 \\
0 & 0 & 3 & 4
\end{array}
\right]
\\]

#### **Paso 6: Sustitución hacia Atrás**
Resuelve de abajo hacia arriba:
- \\( 3z = 4 \Rightarrow z = \frac{4}{3} \\)
- \\( y - 0.25z = 0.5 \Rightarrow y = 0.5 + 0.25(4/3) = \frac{7}{6} \\)
- \\( x + 0.5y - 0.5z = 1.5 \Rightarrow x = 1.5 - 0.5(7/6) + 0.5(4/3) = \frac{11}{6} \\)

**Solución:**
\\[
x = \frac{11}{6}, \quad y = \frac{7}{6}, \quad z = \frac{4}{3}
\\]

---

## **3. Tipos de Solución**
1. **Solución Única**: Una única solución para \\( x_1, x_2, \dots \\).
2. **Infinitas Soluciones**: Muchas soluciones (el sistema es dependiente).
3. **Sin Solución**: Sistema inconsistente.

---

## **4. Sistemas Homogéneos vs. No Homogéneos**
- **Sistema homogéneo**: \\( A\mathbf{x} = 0 \\)
  - Siempre tiene al menos la **solución trivial** \\( \mathbf{x} = 0 \\).
  - Puede tener infinitas soluciones si el determinante de \\( A \\) es cero.

- **Sistema no homogéneo**: \\( A\mathbf{x} = \mathbf{b} \\)
  - Puede tener **solución única, infinitas soluciones o ninguna solución**.

---

## **Conclusión**
- La eliminación gaussiana es un método poderoso para resolver sistemas.
- El número de soluciones depende del **rango** de la matriz.
- Los sistemas homogéneos siempre tienen una solución trivial.

¡Házme saber si necesitas más ejemplos o explicaciones! 🚀