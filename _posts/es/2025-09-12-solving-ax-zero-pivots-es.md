---
audio: false
date: 2025-09-12
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Resolución de Ax Igual a Cero Variables Pivote
translated: true
type: note
---

Este video es la **Clase 7** del curso **18.06 Álgebra Lineal del MIT (Primavera 2005)**, impartido por el **Profesor Gilbert Strang**. El tema es:

### **"Resolviendo \\( A\mathbf{x} = \mathbf{0} \\): Variables Pivote y Soluciones Especiales"**

---

### **Conceptos Clave Cubiertos en la Clase:**
1. **Sistemas Homogéneos (\\( A\mathbf{x} = \mathbf{0} \\))**
   - Un sistema de ecuaciones lineales donde el lado derecho es el vector cero.
   - Siempre tiene al menos la **solución trivial** \\( \mathbf{x} = \mathbf{0} \\).
   - Si hay **variables libres**, hay infinitas soluciones.

2. **Variables Pivote vs. Variables Libres**
   - **Variables pivote**: Corresponden a columnas con pivotes (entradas principales distintas de cero) en la **forma escalonada reducida por filas (RREF)** de \\( A \\).
   - **Variables libres**: Corresponden a columnas **sin pivotes** (pueden tomar cualquier valor).
   - El número de variables libres = número de columnas − rango de \\( A \\).

3. **Soluciones Especiales (Base para el Espacio Nulo)**
   - Para cada variable libre, se le asigna el valor **1** y a las otras **0**, luego se resuelve para las variables pivote.
   - Estas soluciones forman una **base** para el **espacio nulo** de \\( A \\) (todas las soluciones a \\( A\mathbf{x} = \mathbf{0} \\)).
   - El espacio nulo es un **subespacio** de \\( \mathbb{R}^n \\).

4. **Rango y el Espacio Nulo**
   - Si \\( A \\) es una matriz \\( m \times n \\) con rango \\( r \\):
     - Número de variables pivote = \\( r \\).
     - Número de variables libres = \\( n - r \\).
     - Dimensión del espacio nulo = \\( n - r \\).

5. **Ejemplo Paso a Paso**
   - Strang trabaja con un ejemplo (probablemente una matriz con rango < número de columnas) para ilustrar:
     - Encontrar la RREF.
     - Identificar variables pivote y libres.
     - Construir soluciones especiales.
     - Expresar la solución general como una combinación lineal de soluciones especiales.

6. **Interpretación Geométrica**
   - El espacio nulo representa todos los vectores \\( \mathbf{x} \\) que son "colapsados" a cero cuando se multiplican por \\( A \\).
   - Para una matriz 3×3 con rango 2, el espacio nulo es una **línea** que pasa por el origen.

---

### **Por Qué Esta Clase es Importante:**
- Introduce el **espacio nulo** (un subespacio fundamental en álgebra lineal).
- Conecta la **reducción por filas (eliminación)** con la estructura de las soluciones.
- Sienta las bases para comprender la **independencia lineal**, las **bases** y la **dimensión** en clases posteriores.
- Esencial para resolver sistemas, comprender transformaciones y aplicaciones como **ecuaciones diferenciales** o **machine learning**.

---
### **Dónde Encontrar Más:**
- **Material completo del curso**: [MIT OCW 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- **Libro de texto**: *"Introduction to Linear Algebra"* de Strang (el Capítulo 2 cubre este tema).
- **Clases siguientes**: Las próximas clases discuten **resolver \\( A\mathbf{x} = \mathbf{b} \\)** (sistemas no homogéneos) y el **espacio de columnas**.

---
### **Resumen en Una Oración:**
Esta clase enseña cómo encontrar **todas las soluciones** a \\( A\mathbf{x} = \mathbf{0} \\) identificando variables pivote/libres y construyendo una base para el espacio nulo usando soluciones especiales.