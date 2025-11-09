---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Bolsillo de Álgebra Lineal con NumPy
translated: true
type: note
---

Como tu tutor enfocado en ingeniería, esta guía se basa en las formulaciones explícitas con índices anteriores integrando demostraciones prácticas de NumPy mediante `import numpy as np` y `np.linalg`. Toda la matemática sigue siendo verificable con índices (por ejemplo, \\( A = [a_{ij}]_{i=1}^2, j=1^2 \\)); el código usa arreglos explícitos para claridad. Los resultados provienen de ejecuciones verificadas (por ejemplo, para \\( A = \begin{pmatrix} a_{11}=1 & a_{12}=2 \\ a_{21}=3 & a_{22}=4 \end{pmatrix} \\), \\( B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} \\)). Úsalos para cálculos rápidos en la preparación de exámenes—enfócate en interpretar los resultados frente a las fórmulas.

## 1. Operaciones con Matrices
Matemáticas como antes: \\( (AB)_{ij} = \sum_{k=1}^2 a_{ik} b_{kj} \\), etc.

**Demo de NumPy**:
```python
import numpy as np
A = np.array([[1, 2], [3, 4]], dtype=float)
B = np.array([[5, 6], [7, 8]], dtype=float)
```
- Suma: `A + B` produce \\( \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix} \\) (elemento por elemento \\( a_{ij} + b_{ij} \\)).
- Escalar: `2 * A` produce \\( \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix} \\) (\\( c a_{ij} \\)).
- Multiplicación: `A @ B` (o `np.dot(A, B)`) produce \\( \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix} \\) (verifica: suma fil1-col1 \\( 1\cdot5 + 2\cdot7 = 19 \\)). Nota la no conmutatividad: `np.allclose(A @ B, B @ A)` es `False`.
- Transpuesta: `A.T` produce \\( \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \\) (\\( (A^T)_{ij} = a_{ji} \\)).
- Inversa: `np.linalg.inv(A)` produce \\( \begin{pmatrix} -2 & 1 \\ 1.5 & -0.5 \end{pmatrix} \\) (verifica: `A @ inv_A` ≈ \\( I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \\), con pequeños errores de punto flotante ~1e-16).

## 2. Determinantes
Matemáticas: \\( \det A = \sum_{j=1}^2 a_{1j} C_{1j} \\), \\( C_{1j} = (-1)^{1+j} \det(M_{1j}) \\) (por ejemplo, \\( M_{11} = [4] \\), así que \\( C_{11} = 4 \\); completo \\( \det A = 1\cdot4 - 2\cdot3 = -2 \\)).

**Demo de NumPy** (continuando lo anterior):
- `np.linalg.det(A)`: -2.0 (coincide con la fórmula; precisión de punto flotante -2.0000000000000004).
- Producto: `np.linalg.det(A @ B)` = 4.0; `det_A * np.linalg.det(B)` ≈ 4.0 (verifica \\( \det(AB) = \det A \cdot \det B \\)).
- Transpuesta: `np.linalg.det(A.T)` = -2.0 (verifica \\( \det(A^T) = \det A \\)).

Para el vínculo adjunta/inversa: La inversa usa el det en el denominador, como en la fórmula \\( A^{-1} = \frac{1}{\det A} \adj A \\).

## 3. Sistemas Lineales y Eliminación Gaussiana
Matemáticas: Aumentar \\( [A | b] \\) con \\( b = [b_i]_{i=1}^2 = [5, 11]^T \\); resolver por sustitución hacia atrás después de REF.

**Demo de NumPy**:
- `np.linalg.solve(A, b)` produce [1. 2.] (exacto: \\( x_1 = \frac{\det A_1}{\det A} \\), donde \\( A_1 \\) intercambia col1 con b, det= -2 igual; verifica Cramer).
- Comprobar: `A @ x` = [5. 11.] (residual 0).
- Rango: `np.linalg.matrix_rank(A)` = 2 (completo; para singular, rango < 2 implica infinitas/ninguna solución).

El `solve` de NumPy realiza factorización tipo LU internamente (no se necesita código Gaussiano explícito; para personalizado, usa `scipy.linalg.lu` pero quédate con np.linalg aquí).

## 4. Espacios Vectoriales
Matemáticas: rango A = # pivotes = dim Col(A); nulidad = 2 - rango A.

**Demo de NumPy**:
- Rango como antes: 2.
- Estimación de nulidad vía SVD: `U, S, Vt = np.linalg.svd(A)`; contar valores singulares > 1e-10: 2, así que nulidad = 2 - 2 = 0 (Nul(A) = {0}). Para base, vectores del espacio nulo de las filas de Vt con S pequeño.

## 5. Transformaciones Lineales
Matemáticas: T(x)_i = \\( \sum_j a_{ij} x_j \\); la representación matricial es A.

**Vínculo con NumPy**: Igual que las operaciones con matrices; por ejemplo, `T_x = A @ x` aplica la transformación (vectorizada).

## 6. Valores Propios
Matemáticas: Resolver det(A - λ I) = 0, (A - λ I)_{ij} = a_{ij} - λ δ_{ij}; luego (A - λ I) v = 0 para v_j.

**Demo de NumPy**:
- `eigvals, eigvecs = np.linalg.eig(A)`: eigvals ≈ [-0.372, 5.372] (raíces de λ² - tr(A)λ + det A = λ² - 5λ -2 =0).
- Columnas de Eigvecs: por ejemplo, col0 ≈ [-0.825, 0.566]^T para λ≈-0.372.
- Comprobar: `A @ eigvecs[:,0]` ≈ λ eigvecs[:,0] (verificación escalada: `A @ eigvecs[:,0] / eigvals[0]` coincide con eigvecs[:,0]).

Para diagonalizable: Eigvecs de rango completo (det ≠0).

## 7. Productos Internos y Ortogonalización
Matemáticas: <u,v> = \\( \sum_i u_i v_i \\); proy = (<v,w>/<w,w>) w (mult escalar en w_i).

**Demo de NumPy** (u=[1,2], v=[3,4]):
- `np.dot(u, v)` = 11 (o `u @ v`).
- `np.linalg.norm(u)` ≈ 2.236 (√<u,u>).

Gram-Schmidt: Usa `np.linalg.qr(V)` para la matriz V (columnas como vectores base); Q = ortonormal.
- Ejemplo V = \\( \begin{pmatrix} 3 & 0 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 3 \end{pmatrix} \\) (cols v^{(1)}=[3,1,0]^T, etc.).
- `ortho = np.linalg.qr(V)[0]` produce ≈ \\( \begin{pmatrix} -0.949 & -0.316 & 0 \\ -0.316 & 0.949 & 0 \\ 0 & 0 & 1 \end{pmatrix} \\) (cambios de signo ok).
- Comprobar: `np.allclose(ortho.T @ ortho, np.eye(3))` = True (δ_{ij}).

Forma Cuadrática: `u @ A @ u` = 27.0 (x^T A x con x_i = u_i; para def pos, todos eigvals >0—aquí signos mixtos).

**Consejo Rápido de Verificación**: Siempre `np.allclose` para floats; reduce por filas manualmente para n pequeño, luego coincide con `solve` o `eig`. Practica: Intercambia con tus matrices 3×3.

[Documentación de NumPy linalg](https://numpy.org/doc/stable/reference/routines.linalg.html)  
[Álgebra Lineal en NumPy - SciPy Lecture Notes](https://scipy-lectures.org/intro/numpy/auto_examples/plot_linear_algebra.html)