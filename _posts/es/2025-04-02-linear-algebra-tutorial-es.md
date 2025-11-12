---
audio: false
generated: true
lang: es
layout: post
title: Tutorial de Álgebra Lineal
translated: true
type: note
---

## 1. Introducción
### Definición e Importancia
El álgebra lineal es la rama de las matemáticas que se ocupa de los espacios vectoriales y las aplicaciones lineales entre ellos. Es fundamental en ingeniería, física, informática y economía.

### Escalares, Vectores y Matrices
- **Escalares**: Números individuales (por ejemplo, números reales o complejos)
- **Vectores**: Listas ordenadas de números, que representan magnitud y dirección
- **Matrices**: Arreglos rectangulares de números que representan transformaciones o sistemas

### Aplicaciones
- Física (mecánica cuántica, relatividad)
- Ingeniería (sistemas de control, circuitos)
- Economía (optimización, teoría de juegos)
- Data Science & Machine Learning

## 2. Sistemas de Ecuaciones
### Representación
Un sistema de ecuaciones lineales se puede escribir en forma matricial como:
\\[ Ax = b \\]
donde \\( A \\) es una matriz, \\( x \\) es un vector de variables y \\( b \\) es un vector constante.

### Métodos de Solución
- **Eliminación Gaussiana**: Convierte el sistema a forma escalonada para resolver las incógnitas.
- **Reducción por Filas (Forma Escalonada Reducida, RREF)**: Reduce aún más la matriz para identificar soluciones.
- **Tipos de Solución**:
  - **Solución única**: Un punto de intersección
  - **Infinitas soluciones**: Múltiples intersecciones
  - **Sin solución**: Líneas paralelas (sistema inconsistente)
- **Homogéneo vs. No Homogéneo**:
  - Homogéneo: \\( Ax = 0 \\) (siempre tiene al menos una solución)
  - No homogéneo: \\( Ax = b \\)

## 3. Matrices y Operaciones
### Notación y Tipos
- **Matriz Cuadrada**: Mismo número de filas y columnas
- **Matriz Identidad (I)**: Los elementos de la diagonal son 1, los demás son 0
- **Matriz Cero (0)**: Todos los elementos son cero

### Operaciones
- **Suma y Resta**: Elemento por elemento
- **Multiplicación por Escalar**: Multiplica cada elemento por un escalar
- **Multiplicación de Matrices**: \\( (AB)_{ij} = \sum_{k} A_{ik} B_{kj} \\)
- **Transpuesta**: Intercambiar filas y columnas
- **Inversa (A\\(^-1\\))**: Existe solo si el determinante es distinto de cero

## 4. Determinantes
### Definición
Un valor escalar asociado a una matriz cuadrada, útil para resolver ecuaciones lineales y comprender las propiedades de las matrices.

### Cálculo
- **Matriz 2×2**: \\( \text{det} \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc \\)
- **Matriz 3×3**: Usar expansión por cofactores o la Regla de Sarrus
- **Matrices de Orden Superior**: Usar expansión por filas o expansión de Laplace

### Propiedades y Aplicaciones
- **Regla de Cramer**: Utiliza determinantes para resolver sistemas \\( Ax = b \\)
- **Matrices Singulares vs. No Singulares**: Determinante \\( = 0 \\) significa no invertible

## 5. Espacios Vectoriales
### Definición
Un conjunto de vectores que se pueden sumar entre sí y multiplicar por escalares, permaneciendo dentro del conjunto.

### Conceptos Clave
- **Subespacios**: Un subconjunto de un espacio vectorial que satisface las propiedades de clausura
- **Base**: Un conjunto mínimo de vectores linealmente independientes que generan un espacio
- **Dimensión**: El número de vectores en la base
- **Independencia Lineal**: Un conjunto de vectores donde ningún vector es una combinación lineal de los otros
- **Espacio Generado (Span)**: Todas las posibles combinaciones lineales de un conjunto dado de vectores
- **Cambio de Base**: Transición entre diferentes representaciones del espacio vectorial

## 6. Transformaciones Lineales
### Definición
Una función \\( T: V \to W \\) que preserva la suma de vectores y la multiplicación por escalares.

### Representación
Toda transformación lineal puede representarse como una matriz.

### Propiedades
- **Núcleo (Espacio Nulo)**: Conjunto de vectores que se mapean a cero
- **Imagen (Rango)**: Conjunto de vectores de salida
- **Inyectividad (Uno a Uno)**: \\( \text{Ker}(T) = \{0\} \\)
- **Sobreyectividad (Sobre)**: La imagen abarca todo el codominio

## 7. Valores Propios y Vectores Propios
### Definiciones
- **Valores Propios (λ)**: Escalares donde \\( Av = \lambda v \\)
- **Vectores Propios (v)**: Vectores distintos de cero que satisfacen \\( Av = \lambda v \\)

### Cálculo
- Resolver la ecuación característica \\( \det(A - \lambda I) = 0 \\)
- Encontrar los vectores propios correspondientes a partir de \\( (A - \lambda I)v = 0 \\)

### Aplicaciones
- Análisis de estabilidad
- Procesos de Markov
- Análisis de Componentes Principales (PCA) en machine learning

## 8. Espacios con Producto Interno
### Producto Punto y Normas
- **Producto Punto**: \\( a \cdot b = \sum a_i b_i \\)
- **Norma (Magnitud)**: \\( \|v\| = \sqrt{v \cdot v} \\)

### Ortogonalidad y Bases Ortonormales
- **Vectores Ortogonales**: Producto punto = 0
- **Base Ortonormal**: Base donde todos los vectores son ortogonales y tienen longitud unitaria
- **Proceso de Gram-Schmidt**: Convierte una base en una ortonormal

## 9. Aplicaciones
### Problemas del Mundo Real
- **Flujos en Redes**: Optimización usando álgebra lineal
- **Ajuste de Datos**: Técnicas de regresión usando mínimos cuadrados

### Métodos Computacionales
- **Matrices en Programación**: Se utilizan en Python, MATLAB y NumPy para computación científica