---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Bolsillo de Álgebra Lineal Precisa
translated: true
type: note
---

Como tu tutor enfocado en ingeniería, esta guía enfatiza cálculos verificables y explícitos en índices para matrices \\( A = [a_{ij}]_{i=1}^m, j=1^n \in \mathbb{R}^{m \times n} \\) (filas indexadas por \\( i \\), columnas por \\( j \\), base 1). Todos los pasos se muestran con índices para mayor claridad; los ejemplos anotan las entradas en línea. Revisa mediante eliminación gaussiana y resolución de valores propios en casos 2×2/3×3.

## 1. Operaciones con Matrices
- **Suma**: \\( (A + B)_{ij} = a_{ij} + b_{ij} \\) para todo \\( i,j \\).
- **Multiplicación por Escalar**: \\( (cA)_{ij} = c a_{ij} \\) para un escalar \\( c \\), todo \\( i,j \\).
- **Multiplicación de Matrices** (si \\( m \times p \\) y \\( p \times n \\)): \\( (AB)_{ij} = \sum_{k=1}^p a_{ik} b_{kj} \\) para todo \\( i=1^m \\), \\( j=1^n \\).
- **Transpuesta**: \\( (A^T)_{ij} = a_{ji} \\); así \\( (AB)^T_{ij} = \sum_k b_{ki} a_{kj} = (B^T A^T)_{ij} \\).
- **Inversa** (para matriz cuadrada \\( n \times n \\), \\( \det A \neq 0 \\)): \\( A^{-1} \\) satisface \\( \sum_k a_{ik} (A^{-1})_{kj} = \delta_{ij} \\) (delta de Kronecker: 1 si \\( i=j \\), 0 en otro caso). Propiedades: \\( (AB)^{-1}_{ij} = \sum_k (B^{-1})_{ik} (A^{-1})_{kj} = (B^{-1} A^{-1})_{ij} \\); \\( (A^T)^{-1}_{ij} = \sum_k (A^{-1})_{ki} (A^T)_{kj} ? Espera, no: (A^{-1})^T_{ij} = (A^{-1})_{ji} \\), así que \\( [(A^T)^{-1}]_{ij} = (A^{-1})_{ji} \\).

**Ejemplo (Anotación de Inversa 2×2)**: Sea \\( A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \\). Entonces \\( A^{-1} = \frac{1}{\det A} \begin{pmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{pmatrix} \\), donde \\( \det A = a_{11} a_{22} - a_{12} a_{21} \\).

## 2. Determinantes
- **Definición**: Para \\( A \\) cuadrada, \\( \det A \\) vía expansión por cofactores a lo largo de la fila \\( i \\): \\( \det A = \sum_{j=1}^n a_{ij} C_{ij} \\), donde el menor \\( M_{ij} \\) es la submatriz eliminando la fila \\( i \\) y la columna \\( j \\) (así que \\( M_{ij} = [m_{pq}] \\) con \\( p=1^{n-1} \setminus i \\), \\( q=1^{n-1} \setminus j \\), reetiquetado base 1), cofactor \\( C_{ij} = (-1)^{i+j} \det(M_{ij}) \\).
- **Propiedades**:
  - \\( \det(AB) = \det A \cdot \det B \\); \\( \det(A^T) = \det A \\) (ya que la expansión es simétrica).
  - \\( \det(cA) = c^n \det A \\).
  - Intercambio de filas: \\( \det \\) se multiplica por -1; sumar múltiplo de la fila \\( k \\) a la fila \\( i \neq k \\): sin cambios; escalar fila \\( i \\) por \\( c \\): multiplica por \\( c \\).
  - \\( \det I = 1 \\) (unos en la diagonal); singular si \\( \det A = 0 \\) (rango < n).
- **Adjunta**: \\( \adj(A)_{ij} = C_{ji} = [C^T]_{ij} \\), donde \\( C = [C_{pq}] \\). Inversa: \\( A^{-1} = \frac{1}{\det A} \adj A \\), así que \\( (A^{-1})_{ij} = \frac{1}{\det A} \sum_k \delta_{ik} C_{kj} ? No: la forma matricial verifica \\( A \adj A = (\det A) I \\).

**Ejemplo (Cofactores 2×2)**: Para la \\( A \\) anterior, \\( M_{11} = [a_{22}] \\), \\( C_{11} = (-1)^{1+1} a_{22} = a_{22} \\); \\( M_{12} = [a_{21}] \\), \\( C_{12} = (-1)^{1+2} a_{21} = -a_{21} \\); similarmente \\( C_{21} = -a_{12} \\), \\( C_{22} = a_{11} \\). Así \\( \adj A = \begin{pmatrix} C_{11} & C_{21} \\ C_{12} & C_{22} \end{pmatrix} = \begin{pmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{pmatrix} \\).

- **Regla de Cramer** (para \\( \sum_j a_{ij} x_j = b_i \\), \\( i=1^n \\), \\( \det A \neq 0 \\)): \\( x_r = \frac{\det A_r}{\det A} \\), donde \\( A_r \\) reemplaza la columna \\( r \\) de \\( A \\) con \\( [b_i]_{i=1}^n \\), así que \\( (A_r)_{ij} = a_{ij} \\) si \\( j \neq r \\), si no \\( b_i \\).

## 3. Sistemas Lineales & Eliminación Gaussiana
- **Matriz Aumentada**: \\( [A | b] = [a_{ij} | b_i] \\) para \\( i=1^m \\), \\( j=1^n \\).
- **Reducción por Filas a FER**: Aplica operaciones elementales (intercambiar filas \\( p \leftrightarrow q \\); escalar fila \\( p \\) por \\( c \neq 0 \\): fila \\( p \leftarrow c \\) fila \\( p \\); sumar \\( c \\) fila \\( q \\) a fila \\( p \\)) para obtener la forma escalonada por filas: entrada principal (pivote) en fila \\( i \\) en columna \\( p_i \geq p_{i-1} \\), ceros debajo de los pivotes.
- **A FRER**: Continúa para obtener ceros encima de los pivotes, escala pivotes a 1.
- **Rango**: Número de filas distintas de cero en FER (o pivotes).
- **Soluciones**:
  - Única si rango \\( A = n \\), rango \\( [A|b] = n \\) (nulidad 0).
  - Infinitas si rango \\( A = \\) rango \\( [A|b] = r < n \\) (n-r variables libres).
  - Inconsistente si rango \\( A < \\) rango \\( [A|b] \\).
- **Solución General**: \\( x = x_p + x_h \\), particular \\( x_p \\) de FRER, homogénea \\( x_h \\) genera el espacio nulo (base de variables libres).
- **Ejemplo Paso a Paso (Anotación Sistema 2×2)**: Resolver \\( a_{11} x_1 + a_{12} x_2 = b_1 \\), \\( a_{21} x_1 + a_{22} x_2 = b_2 \\). Fila2 ← Fila2 - (a_{21}/a_{11}) Fila1: nueva fila2 = [0, a_{22} - (a_{21} a_{12}/a_{11}), b_2 - (a_{21} b_1 / a_{11}) ]. Sustitución hacia atrás: \\( x_2 = \\) ... / término det, etc.

## 4. Espacios Vectoriales
- **Subespacios**: Col(A) = span{ col j de A, j=1^n } = { \\( \sum_j x_j \\) col j | x }; dim = rango A.
- **Espacio de Filas**: Fil(A) = Col(A^T); dim = rango A.
- **Espacio Nulo**: Nul(A) = { x | \\( \sum_j a_{ij} x_j = 0 \\) ∀ i }; base a partir de columnas libres en FRER.
- **Teorema de la Dimensión**: rango A + dim Nul(A) = n.

## 5. Transformaciones Lineales
- **Representación Matricial**: T(x)_i = \\( \sum_j a_{ij} x_j \\).
- **Núcleo**: Ker T = Nul(A); Im T = Col(A).

## 6. Valores Propios
- **Polinomio Característico**: det(A - λ I) = 0, donde (A - λ I)_{ij} = a_{ij} - λ δ_{ij}.
- **Vectores Propios**: Para λ, resolver \\( \sum_j (a_{ij} - λ δ_{ij}) v_j = 0 \\), v = [v_j] ≠ 0.
- **Diagonalizable**: Si mult alg(λ_k) = mult geo(λ_k) ∀ k (dimensión completa del espacio propio), entonces A = P D P^{-1}, D_{ij} = λ_i δ_{ij}, columnas de P = vectores propios.
- **Simétrica**: A = A^T ⇒ diagonalización ortogonal: A = Q D Q^T, Q^T Q = I.

## 7. Productos Internos & Ortogonalización
- **Euclidiano**: <u,v> = \\( \sum_i u_i v_i = u^T v \\).
- **Paso de Gram-Schmidt**: Para base {v^{(k)}}, u^{(1)} = v^{(1)}; u^{(k)} = v^{(k)} - \sum_{m=1}^{k-1} \proj_{u^{(m)}} v^{(k)}, donde \proj_w v = \frac{<v,w>}{<w,w>} w (componente \\( \sum_i ... \\)).

**Consejo Rápido de Verificación**: Siempre reduce por filas [A - λI | 0] para espacios propios; verifica det vía expansión si n≤3.

[Hoja de Referencias de Álgebra Lineal - Fórmulas Indexadas](https://laurentlessard.com/teaching/ece532/cheat_sheet.pdf)  
[Auto-Examen 02198 Revisión](https://doc.quark.cn/preview/jiaoyukaoshi-shijuan-gaokao/1130FC966EE595249D3822AFF5DF0167)