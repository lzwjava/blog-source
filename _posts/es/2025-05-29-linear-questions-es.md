---
audio: false
generated: true
lang: es
layout: post
title: Preguntas de Álgebra Lineal
translated: true
type: note
---

**18. Sean las matrices X y A que satisfacen la relación XA = X + A. Si $A = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix}$, encuentre la matriz X.**

**Respuesta:**
Dada la ecuación $XA = X + A$.
Podemos reescribirla como $XA - X = A$, entonces $X(A - I) = A$.
Si $(A - I)$ es invertible, entonces $X = A(A - I)^{-1}$.

Primero, calculemos $A - I$:

$A - I = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\\ 0 & 1 & 0 \\\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\\ 2 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$.

Luego, encontramos la inversa de $(A - I)$. Sea $B = A - I$.
El determinante de B es $\det(B) = 0(0 - 0) - (-3)(2 - 0) + 0(0 - 0) = 6$.
Dado que $\det(B) \neq 0$, B es invertible.

La matriz adjunta de B es:
$adj(B) = \begin{pmatrix} 0 & 3 & 0 \\\ -2 & 0 & 0 \\\ 0 & 0 & 6 \end{pmatrix}$.

Entonces, $(A - I)^{-1} = \frac{1}{\det(B)} adj(B) = \frac{1}{6} \begin{pmatrix} 0 & 3 & 0 \\\ -2 & 0 & 0 \\\ 0 & 0 & 6 \end{pmatrix} = \begin{pmatrix} 0 & 1/2 & 0 \\\ -1/3 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$.

Ahora, calculamos $X = A(A - I)^{-1}$:
$X = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} \begin{pmatrix} 0 & 1/2 & 0 \\\ -1/3 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$
$X = \begin{pmatrix} (1)(0) + (-3)(-1/3) + (0)(0) & (1)(1/2) + (-3)(0) + (0)(0) & (1)(0) + (-3)(0) + (0)(1) \\\ (2)(0) + (1)(-1/3) + (0)(0) & (2)(1/2) + (1)(0) + (0)(0) & (2)(0) + (1)(0) + (0)(1) \\\ (0)(0) + (0)(-1/3) + (2)(0) & (0)(1/2) + (0)(0) + (2)(0) & (0)(0) + (0)(0) + (2)(1) \end{pmatrix}$
$X = \begin{pmatrix} 0+1+0 & 1/2+0+0 & 0+0+0 \\\ 0-1/3+0 & 1+0+0 & 0+0+0 \\\ 0+0+0 & 0+0+0 & 0+0+2 \end{pmatrix}$
$X = \begin{pmatrix} 1 & 1/2 & 0 \\\ -1/3 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix}$.

**19. Determine el valor de k para el cual los vectores $\alpha_1 = (1, 1, k)^T$, $\alpha_2 = (1, k, 1)^T$, $\alpha_3 = (k, 1, 1)^T$ son linealmente dependientes. Encuentre un conjunto linealmente independiente máximo y exprese el(los) vector(es) restante(s) como una combinación lineal de este conjunto.**

**Respuesta:**
Los vectores $\alpha_1, \alpha_2, \alpha_3$ son linealmente dependientes si el determinante de la matriz formada por estos vectores es cero.
Sea $A = \begin{pmatrix} 1 & 1 & k \\\ 1 & k & 1 \\\ k & 1 & 1 \end{pmatrix}$.
$\det(A) = 1(k - 1) - 1(1 - k) + k(1 - k^2)$
$= k - 1 - 1 + k + k - k^3$
$= -k^3 + 3k - 2$.
Necesitamos encontrar $k$ tal que $-k^3 + 3k - 2 = 0$, o $k^3 - 3k + 2 = 0$.
Podemos probar raíces enteras que sean divisores de 2 (es decir, $\pm 1, \pm 2$).
Si $k=1$, $1^3 - 3(1) + 2 = 1 - 3 + 2 = 0$. Entonces, $(k-1)$ es un factor.
Si $k=-2$, $(-2)^3 - 3(-2) + 2 = -8 + 6 + 2 = 0$. Entonces, $(k+2)$ es un factor.
Usando división polinomial o división sintética para $(k^3 - 3k + 2) / (k-1)$:
$(k-1)(k^2+k-2) = 0$
$(k-1)(k+2)(k-1) = 0$
Entonces, las raíces son $k=1$ (raíz repetida) y $k=-2$.
Los vectores son linealmente dependientes si $k=1$ o $k=-2$.

Caso 1: $k=1$
$\alpha_1 = (1, 1, 1)^T$, $\alpha_2 = (1, 1, 1)^T$, $\alpha_3 = (1, 1, 1)^T$.
En este caso, los tres vectores son idénticos.
Un conjunto linealmente independiente máximo puede ser $\{\alpha_1\}$.
Entonces $\alpha_2 = 1 \cdot \alpha_1$ y $\alpha_3 = 1 \cdot \alpha_1$.

Caso 2: $k=-2$
$\alpha_1 = (1, 1, -2)^T$, $\alpha_2 = (1, -2, 1)^T$, $\alpha_3 = (-2, 1, 1)^T$.
Verifiquemos si $\alpha_1$ y $\alpha_2$ son linealmente independientes. No son múltiplos escalares entre sí, por lo que son linealmente independientes. Por lo tanto, un conjunto linealmente independiente máximo puede ser $\{\alpha_1, \alpha_2\}$.
Queremos expresar $\alpha_3$ como una combinación lineal de $\alpha_1$ y $\alpha_2$:
$\alpha_3 = c_1 \alpha_1 + c_2 \alpha_2$
$(-2, 1, 1)^T = c_1 (1, 1, -2)^T + c_2 (1, -2, 1)^T$
Esto da el sistema de ecuaciones:
1) $c_1 + c_2 = -2$
2) $c_1 - 2c_2 = 1$
3) $-2c_1 + c_2 = 1$
Restando (2) de (1): $(c_1 + c_2) - (c_1 - 2c_2) = -2 - 1 \Rightarrow 3c_2 = -3 \Rightarrow c_2 = -1$.
Sustituyendo $c_2 = -1$ en (1): $c_1 - 1 = -2 \Rightarrow c_1 = -1$.
Verificando con (3): $-2(-1) + (-1) = 2 - 1 = 1$. Esto es consistente.
Entonces, $\alpha_3 = -1 \cdot \alpha_1 - 1 \cdot \alpha_2$.

**20. Resuelva el sistema de ecuaciones lineales { $x_1 - x_2 - 3x_4 = -2$ ; $x_1 + 2x_3 - 2x_4 = -1$ ; $2x_1 - 2x_2 + x_3 - 6x_4 = -5$ ; $-x_1 + 2x_2 + 3x_3 + 4x_4 = 2$ } (Encuentre una solución particular y la base fundamental de soluciones para el sistema homogéneo correspondiente).**

**Respuesta:**
La matriz aumentada es:
$\begin{pmatrix} 1 & -1 & 0 & -3 & | & -2 \\\ 1 & 0 & 2 & -2 & | & -1 \\\ 2 & -2 & 1 & -6 & | & -5 \\\ -1 & 2 & 3 & 4 & | & 2 \end{pmatrix}$

$R_2 \leftarrow R_2 - R_1$
$R_3 \leftarrow R_3 - 2R_1$
$R_4 \leftarrow R_4 + R_1$
$\begin{pmatrix} 1 & -1 & 0 & -3 & | & -2 \\\ 0 & 1 & 2 & 1 & | & 1 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 1 & 3 & 1 & | & 0 \end{pmatrix}$

$R_1 \leftarrow R_1 + R_2$
$R_4 \leftarrow R_4 - R_2$
$\begin{pmatrix} 1 & 0 & 2 & -2 & | & -1 \\\ 0 & 1 & 2 & 1 & | & 1 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 0 & 1 & 0 & | & -1 \end{pmatrix}$

$R_1 \leftarrow R_1 - 2R_3$
$R_2 \leftarrow R_2 - 2R_3$
$R_4 \leftarrow R_4 - R_3$
$\begin{pmatrix} 1 & 0 & 0 & -2 & | & 1 \\\ 0 & 1 & 0 & 1 & | & 3 \\\ 0 & 0 & 1 & 0 & | & -1 \\\ 0 & 0 & 0 & 0 & | & 0 \end{pmatrix}$

El sistema es equivalente a:
$x_1 - 2x_4 = 1 \Rightarrow x_1 = 1 + 2x_4$
$x_2 + x_4 = 3 \Rightarrow x_2 = 3 - x_4$
$x_3 = -1$
Sea $x_4 = t$ (variable libre).
La solución general es:
$x_1 = 1 + 2t$
$x_2 = 3 - t$
$x_3 = -1$
$x_4 = t$
En forma vectorial: $X = \begin{pmatrix} 1 \\\ 3 \\\ -1 \\\ 0 \end{pmatrix} + t \begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}$.

Una solución particular se obtiene estableciendo $t=0$: $X_p = \begin{pmatrix} 1 \\\ 3 \\\ -1 \\\ 0 \end{pmatrix}$.

El sistema homogéneo correspondiente tiene la solución $X_h = t \begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}$.
La base fundamental de soluciones para el sistema homogéneo es $\{\begin{pmatrix} 2 \\\ -1 \\\ 0 \\\ 1 \end{pmatrix}\}$.

**21. Sea la matriz A = \begin{pmatrix} x & 0 & y \\\ 0 & 2 & 0 \\\ y & 0 & -2 \end{pmatrix} que tiene un valor propio de -3, y |A| = -12. Encuentre los valores de x y y.**

**Respuesta:**
La ecuación característica es $\det(A - \lambda I) = 0$.
$A - \lambda I = \begin{pmatrix} x-\lambda & 0 & y \\\ 0 & 2-\lambda & 0 \\\ y & 0 & -2-\lambda \end{pmatrix}$.
$\det(A - \lambda I) = (x-\lambda)[(2-\lambda)(-2-\lambda) - 0] - 0 + y[0 - y(2-\lambda)]$
$= (x-\lambda)(2-\lambda)(-2-\lambda) - y^2(2-\lambda)$
$= (2-\lambda)[(x-\lambda)(-2-\lambda) - y^2]$
$= (2-\lambda)[-2x - x\lambda + 2\lambda + \lambda^2 - y^2] = 0$.
Los valores propios son $\lambda_1 = 2$, y las raíces de $\lambda^2 + (2-x)\lambda - (2x+y^2) = 0$.
Se nos da que un valor propio es -3.
Si $2 = -3$, esto es falso. Entonces, -3 debe ser una raíz de $\lambda^2 + (2-x)\lambda - (2x+y^2) = 0$.
Sustituyendo $\lambda = -3$:
$(-3)^2 + (2-x)(-3) - (2x+y^2) = 0$
$9 - 6 + 3x - 2x - y^2 = 0$
$3 + x - y^2 = 0 \Rightarrow x - y^2 = -3$ (Ecuación 1)

También se nos da que $\det(A) = -12$.
$\det(A) = x(2(-2) - 0) - 0 + y(0 - 2y)$
$= -4x - 2y^2 = -12$
Dividiendo por -2: $2x + y^2 = 6$ (Ecuación 2)

Ahora tenemos un sistema de dos ecuaciones con x e y:
1) $x - y^2 = -3$
2) $2x + y^2 = 6$
Sumando la Ecuación 1 y la Ecuación 2:
$(x - y^2) + (2x + y^2) = -3 + 6$
$3x = 3 \Rightarrow x = 1$.
Sustituyendo $x=1$ en la Ecuación 1:
$1 - y^2 = -3$
$-y^2 = -4$
$y^2 = 4 \Rightarrow y = \pm 2$.

Entonces los valores son $x=1$ y $y=2$, o $x=1$ y $y=-2$.

**22. Sea la forma cuadrática de 3 variables $f(x_1, x_2, x_3) = t(x_1^2 + x_2^2 + x_3^2) + 2x_1x_2 + 2x_1x_3 - 2x_2x_3$. Determine para qué valor(es) de t esta forma cuadrática es definida positiva.**

**Respuesta:**
La matriz de la forma cuadrática A es:
$A = \begin{pmatrix} t & 1 & 1 \\\ 1 & t & -1 \\\ 1 & -1 & t \end{pmatrix}$.
Para que la forma cuadrática sea definida positiva, todos los menores principales principales de A deben ser positivos.

1. El primer menor principal principal es $M_1 = t$.
Para ser definida positiva, $t > 0$.

2. El segundo menor principal principal es $M_2 = \det \begin{pmatrix} t & 1 \\\ 1 & t \end{pmatrix} = t^2 - 1$.
Para ser definida positiva, $t^2 - 1 > 0 \Rightarrow t^2 > 1$.
Dado que ya tenemos $t > 0$, esto implica $t > 1$.

3. El tercer menor principal principal es $M_3 = \det(A)$.
$M_3 = t(t^2 - 1) - 1(t - (-1)) + 1(-1 - t)$
$= t(t^2 - 1) - (t + 1) - (1 + t)$
$= t^3 - t - t - 1 - 1 - t$
$= t^3 - 3t - 2$.
Para ser definida positiva, $t^3 - 3t - 2 > 0$.

Sabemos de la pregunta 19 que $k^3 - 3k - 2 = (k+1)^2(k-2)$. (Aquí $k$ es $t$)
Entonces, $t^3 - 3t - 2 = (t+1)^2(t-2)$.
Necesitamos $(t+1)^2(t-2) > 0$.
Dado que $(t+1)^2 \ge 0$, y para que no sea cero, $t \neq -1$.
Entonces necesitamos $t-2 > 0$, lo que significa $t > 2$.

Combinando las condiciones:
1) $t > 0$
2) $t > 1$
3) $t > 2$

La intersección de estas condiciones es $t > 2$.
Por lo tanto, la forma cuadrática es definida positiva cuando $t > 2$.