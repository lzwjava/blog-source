---
audio: false
generated: true
lang: es
layout: post
title: Diagonalizable
translated: true
type: note
---

Para determinar qué opción es necesaria para que una matriz sea diagonalizable, examinaré cada afirmación.

Una matriz cuadrada A es diagonalizable si y solo si existe una matriz invertible P tal que P⁻¹AP es una matriz diagonal. Esto ocurre precisamente cuando A tiene un conjunto completo de vectores propios linealmente independientes.

Analicemos cada opción:

a) La matriz debe tener al menos un valor propio.
Si bien todas las matrices n×n tienen al menos un valor propio (en el campo complejo), esto por sí solo no garantiza la diagonalizabilidad. Una matriz podría tener valores propios pero aún no ser diagonalizable si no tiene suficientes vectores propios linealmente independientes.

b) La matriz debe tener valores propios distintos.
Tener valores propios distintos es suficiente pero no necesario para la diagonalizabilidad. Una matriz con valores propios repetidos aún puede ser diagonalizable si tiene suficientes vectores propios linealmente independientes asociados con esos valores propios repetidos.

c) La matriz debe tener suficientes vectores propios linealmente independientes.
Esta es exactamente la condición necesaria y suficiente para la diagonalizabilidad. Específicamente, una matriz n×n es diagonalizable si y solo si tiene n vectores propios linealmente independientes, formando una base para el espacio vectorial.

Por lo tanto, la opción c) es la respuesta correcta: una matriz es diagonalizable si y solo si tiene suficientes vectores propios linealmente independientes.

---

Explicaré por qué la opción (c) - tener suficientes vectores propios linealmente independientes - es la condición necesaria para la diagonalizabilidad.

Cuando decimos que una matriz A es diagonalizable, queremos decir que podemos encontrar una matriz invertible P tal que P⁻¹AP = D, donde D es una matriz diagonal. Las columnas de P son los vectores propios de A, y las entradas diagonales de D son los valores propios correspondientes.

He aquí por qué cada opción funciona o no funciona:

Para la opción (a): Si bien toda matriz cuadrada tiene al menos un valor propio (en el campo complejo), tener valores propios por sí solo no garantiza la diagonalizabilidad. Considere la matriz:
[1 1]
[0 1]

Tiene un valor propio (λ = 1) con multiplicidad algebraica 2, pero solo un vector propio linealmente independiente. Esta matriz no es diagonalizable a pesar de tener valores propios.

Para la opción (b): Tener valores propios distintos es suficiente pero no necesario. Cuando una matriz tiene valores propios distintos, los vectores propios son automáticamente linealmente independientes. Sin embargo, las matrices con valores propios repetidos aún pueden ser diagonalizables si tienen suficientes vectores propios linealmente independientes.

Para la opción (c): Esta es precisamente la definición de diagonalizabilidad. Una matriz n×n es diagonalizable si y solo si tiene n vectores propios linealmente independientes. Esto se debe a que:
- El proceso de diagonalización requiere que P sea invertible
- P es invertible si y solo si sus columnas son linealmente independientes
- Las columnas de P son los vectores propios de A

Esta condición aborda directamente el requisito fundamental para la diagonalización: tener una base completa de vectores propios para el espacio vectorial.