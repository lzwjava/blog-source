---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Referencia Rápida para el Examen de Álgebra Lineal
translated: true
type: note
---

Referencia rápida de conceptos clave y fórmulas. Enfócate en matrices, determinantes, sistemas lineales, espacios vectoriales, transformaciones, valores propios y formas cuadráticas—temas centrales de exámenes anteriores. Revisa definiciones, propiedades y cálculos.

## 1. Matrices

- **Definición**: \\( A = [a_{ij}] \in \mathbb{R}^{m \times n} \\).
- **Operaciones**:
  - Suma: \\( (A + B)_{ij} = a_{ij} + b_{ij} \\).
  - Escalar: \\( (cA)_{ij} = c a_{ij} \\).
  - Multiplicación: \\( (AB)_{ij} = \sum_k a_{ik} b_{kj} \\) (si los tamaños son compatibles).
- **Transpuesta**: \\( (A^T)_{ij} = a_{ji} \\); \\( (AB)^T = B^T A^T \\), \\( (A^T)^T = A \\).
- **Inversa** (cuadrada): \\( AA^{-1} = I \\); \\( (AB)^{-1} = B^{-1} A^{-1} \\); \\( (A^T)^{-1} = (A^{-1})^T \\).
- **Tipos**:
  - Diagonal: Diferente de cero solo en la diagonal.
  - Triangular Superior/Inferior: Ceros debajo/encima de la diagonal.
  - Simétrica: \\( A = A^T \\).
  - Ortogonal: \\( A^T A = I \\) (columnas ortonormales).

## 2. Determinantes (det A)

- **Propiedades**:
  - \\( \det(AB) = \det A \cdot \det B \\); \\( \det(A^T) = \det A \\); \\( \det(cA) = c^n \det A \\).
  - Intercambio de fila/columna: Multiplica por -1.
  - Sumar múltiplo de fila/columna: Sin cambio.
  - Escalar fila/columna por c: Multiplica por c.
  - \\( \det I = 1 \\); \\( \det A = 0 \\) si es singular (filas/columnas dependientes).
- **Cálculo**:
  - 2x2: \\( \det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc \\).
  - Expansión por Cofactores (fila i): \\( \det A = \sum_j a_{ij} C_{ij} \\), donde \\( C_{ij} = (-1)^{i+j} M_{ij} \\) (det del menor).
  - Triangular: Producto de las entradas de la diagonal.
- **Adjunta/Inversa**: \\( A^{-1} = \frac{1}{\det A} \adj A \\), donde \\( \adj A = C^T \\) (transpuesta de la matriz de cofactores).
- **Regla de Cramer** (para \\( Ax = b \\), det A ≠ 0): \\( x_i = \frac{\det A_i}{\det A} \\) (A_i reemplaza la i-ésima columna con b).

## 3. Sistemas Lineales (Ax = b)

- **Eliminación Gaussiana**: Reducir por filas [A | b] a FER/FRER.
  - FER: Pivotes (1s principales) en escalera hacia abajo-derecha; ceros debajo de los pivotes.
  - Sustitución hacia atrás para solución única.
- **Soluciones**:
  - Única: rango A = n (rango de columna completo), espacio nulo {0}.
  - Infinitas: rango A = rango [A|b] < n (variables libres).
  - Ninguna: rango A < rango [A|b].
- **Solución Completa**: Solución particular + base del espacio nulo (soluciones homogéneas).
- **Descomposición LU** (sin pivoteo): A = LU (L triangular inferior unitaria, U triangular superior); resolver Ly = b, Ux = y.
- **Mínimos Cuadrados** (sobredeterminado): \\( \hat{x} = (A^T A)^{-1} A^T b \\) (si rango completo).

## 4. Espacios Vectoriales y Subespacios

- **Espacio Vectorial**: Cerrado bajo suma/multiplicación por escalar; axiomas (ej., vector 0, inversos).
- **Subespacios**: Span de vectores; cerrado, contiene 0.
  - Espacio Columna: Col(A) = span(columnas de A); dim = rango A.
  - Espacio Fila: Row(A) = Col(A^T); dim = rango A.
  - Espacio Nulo: Nul(A) = {x | Ax = 0}; dim = n - rango A.
  - Espacio Nulo Izquierdo: Nul(A^T).
- **Independencia Lineal**: c1 v1 + ... + ck vk = 0 ⇒ todos ci = 0.
- **Base**: Conjunto generador linealmente independiente.
- **Dimensión**: # de vectores en una base; dim Col(A) + dim Nul(A) = n (teorema de rango-nulidad).
- **Rango**: # de columnas pivote = dim Col(A) = dim Row(A).

## 5. Transformaciones Lineales

- **Definición**: T: V → W lineal si T(u + v) = T u + T v, T(cu) = c T u.
- **Rep. Matricial**: [T] respecto a bases = A donde T(x) = A x (base estándar).
- **Núcleo**: Ker T = Nul(A); Imagen: Im T = Col(A).
- **Isomorfismo**: 1-1 sobre (matriz invertible).
- **Teorema de Rango-Nulidad**: dim Ker T + dim Im T = dim V.

## 6. Valores Propios y Vectores Propios

- **Definición**: A v = λ v (v ≠ 0 vector propio, λ valor propio).
- **Ec. Característica**: det(A - λ I) = 0; raíces λi (multiplicidad algebraica).
- **Vectores Propios**: Resolver (A - λ I) v = 0; mult. geométrica = dim espacio propio.
- **Diagonalizable**: n vectores propios lin. indep. ⇒ A = X Λ X^{-1} (Λ diag(λi), X = [v1 ... vn]).
  - A Simétrica: Siempre diagonalizable; vectores propios ortogonales (A = Q Λ Q^T, Q ortogonal).
- **Traza**: tr A = ∑ λi.
- **Det**: det A = ∏ λi.
- **Matrices Similares**: A ~ B si A = P B P^{-1}; mismos valores propios, traza, det.

## 7. Productos Internos y Formas Cuadráticas

- **Producto Interno**: <u, v> = u^T v (Euclidiano); ||v|| = √<v,v>.
- **Ortogonal**: <u,v> = 0; Base Ortonormal: <ei, ej> = δij.
- **Gram-Schmidt**: Ortogonalizar base {v1,...,vn} → {u1,...,un}.
  - u1 = v1; uk = vk - proj_{span(u1..u_{k-1})} vk; proj_w v = (<v,w>/<w,w>) w.
- **Forma Cuadrática**: q(x) = x^T A x (A simétrica).
  - Definida Positiva: q(x) > 0 para x ≠ 0 (todos λi > 0).
  - Diagonalizar: q(x) = ∑ λi yi^2 (y = Q^T x).

## Consejos Rápidos

- Calcular rango: Reducir por filas para encontrar # de pivotes.
- Verificar diagonalizable: Mult. geométrica = mult. algebraica para cada λ.
- Para exámenes: Practica reducción por filas, expansión de determinantes, problemas de valores propios en matrices 2x2/3x3.
- Errores Comunes: Olvidar la multiplicidad; signo en cofactores; multiplicación no conmutativa.

¡Buena suerte mañana—enfócate en comprender más que en memorizar!

[Linear Algebra Cheat Sheet - Laurent Lessard](https://laurentlessard.com/teaching/ece532/cheat_sheet.pdf)  
[Linear Algebra Review - Yiping Lu](https://2prime.github.io/files/linear/finalsheet.pdf)  
[2023 Self-Exam Linear Algebra Questions](https://doc.quark.cn/preview/jiaoyukaoshi-shijuan-gaokao/1130FC966EE595249D3822AFF5DF0167)