---
audio: false
generated: true
lang: es
layout: post
title: Transformaciones Lineales - Gemini
translated: true
type: note
---

De acuerdo, profundicemos en un tutorial detallado sobre transformaciones lineales, cubriendo la definición, ejemplos, representación matricial, núcleo, imagen y propiedades como la inyectividad y la sobreyectividad. Este es un tema fundamental en álgebra lineal.

## 6. Transformaciones Lineales: Un Tutorial Detallado

Una **transformación lineal** es una función entre dos espacios vectoriales que preserva las operaciones de suma de vectores y multiplicación por escalar. Sean \\(V\\) y \\(W\\) espacios vectoriales sobre el mismo campo \\(F\\) (que a menudo es el conjunto de los números reales \\(\mathbb{R}\\) o los números complejos \\(\mathbb{C}\\)).

**Definición:** Una función \\(T: V \rightarrow W\\) es una transformación lineal si satisface las siguientes dos propiedades para todos los vectores \\(\mathbf{u}, \mathbf{v} \in V\\) y todos los escalares \\(c \in F\\):

1.  **Aditividad:** \\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})\\)
2.  **Homogeneidad (Multiplicación por Escalar):** \\(T(c\mathbf{u}) = cT(\mathbf{u})\\)

Estas dos propiedades se pueden combinar en una sola condición:
\\(T(c\mathbf{u} + d\mathbf{v}) = cT(\mathbf{u}) + dT(\mathbf{v})\\) para todos \\(\mathbf{u}, \mathbf{v} \in V\\) y todos los escalares \\(c, d \in F\\).

**Consecuencias Clave de la Linealidad:**

* \\(T(\mathbf{0}_V) = \mathbf{0}_W\\), donde \\(\mathbf{0}_V\\) es el vector cero en \\(V\\) y \\(\mathbf{0}_W\\) es el vector cero en \\(W\\). (Demostración: \\(T(\mathbf{0}_V) = T(0\mathbf{u}) = 0T(\mathbf{u}) = \mathbf{0}_W\\) para cualquier \\(\mathbf{u} \in V\\)).
* \\(T(-\mathbf{u}) = -T(\mathbf{u})\\). (Demostración: \\(T(-\mathbf{u}) = T((-1)\mathbf{u}) = (-1)T(\mathbf{u}) = -T(\mathbf{u})\\)).

### Ejemplos de Transformaciones Lineales

Veamos algunos ejemplos para entender mejor el concepto.

**Ejemplo 1: Transformación en \\(\mathbb{R}^2\\) (Rotación)**

Considera una transformación \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) que rota cada vector en \\(\mathbb{R}^2\\) en sentido antihorario por un ángulo \\(\theta\\). Si \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\), entonces \\(T(\mathbf{v}) = \begin{pmatrix} x\cos\theta - y\sin\theta \\ x\sin\theta + y\cos\theta \end{pmatrix}\\).

Comprobemos si esto es una transformación lineal. Sean \\(\mathbf{u} = \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}\\) y \\(\mathbf{v} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix}\\), y sea \\(c\\) un escalar.

* **Aditividad:**
    \\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2)\cos\theta - (y_1 + y_2)\sin\theta \\ (x_1 + x_2)\sin\theta + (y_1 + y_2)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} (x_1\cos\theta - y_1\sin\theta) + (x_2\cos\theta - y_2\sin\theta) \\ (x_1\sin\theta + y_1\cos\theta) + (x_2\sin\theta + y_2\cos\theta) \end{pmatrix} = T(\mathbf{u}) + T(\mathbf{v})\\)

* **Homogeneidad:**
    \\(T(c\mathbf{u}) = T\left(\begin{pmatrix} cx_1 \\ cy_1 \end{pmatrix}\right) = \begin{pmatrix} (cx_1)\cos\theta - (cy_1)\sin\theta \\ (cx_1)\sin\theta + (cy_1)\cos\theta \end{pmatrix}\\)
    \\(= \begin{pmatrix} c(x_1\cos\theta - y_1\sin\theta) \\ c(x_1\sin\theta + y_1\cos\theta) \end{pmatrix} = c \begin{pmatrix} x_1\cos\theta - y_1\sin\theta \\ x_1\sin\theta + y_1\cos\theta \end{pmatrix} = cT(\mathbf{u})\\)

Por lo tanto, la rotación es una transformación lineal.

**Ejemplo 2: Transformación en \\(\mathbb{R}^2\\) (Proyección sobre el eje x)**

Considera \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) definida por \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x \\ 0 \end{pmatrix}\\). Esta transformación proyecta cada vector sobre el eje x. Puedes verificar que esto también es una transformación lineal usando la definición.

**Ejemplo 3: Transformación en \\(\mathbb{R}^2\\) (Traslación)**

Considera \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^2\\) definida por \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + a \\ y + b \end{pmatrix}\\), donde \\(a\\) y \\(b\\) son constantes (no ambas cero).

Comprobemos la primera propiedad:
\\(T(\mathbf{u} + \mathbf{v}) = T\left(\begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}\right) = \begin{pmatrix} (x_1 + x_2) + a \\ (y_1 + y_2) + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + a + x_2 + a \\ y_1 + b + y_2 + b \end{pmatrix}\\)

Esto parece correcto, verifiquemos de nuevo.
\\(T(\mathbf{u} + \mathbf{v}) = \begin{pmatrix} x_1 + x_2 + a \\ y_1 + y_2 + b \end{pmatrix}\\)
\\(T(\mathbf{u}) + T(\mathbf{v}) = \begin{pmatrix} x_1 + a \\ y_1 + b \end{pmatrix} + \begin{pmatrix} x_2 + a \\ y_2 + b \end{pmatrix} = \begin{pmatrix} x_1 + x_2 + 2a \\ y_1 + y_2 + 2b \end{pmatrix}\\)

Si \\(a \neq 0\\) o \\(b \neq 0\\), entonces \\(T(\mathbf{u} + \mathbf{v}) \neq T(\mathbf{u}) + T(\mathbf{v})\\). Además, \\(T(\mathbf{0}) = T\left(\begin{pmatrix} 0 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} a \\ b \end{pmatrix} \neq \begin{pmatrix} 0 \\ 0 \end{pmatrix}\\) si \\(a\\) o \\(b\\) es distinto de cero. Por lo tanto, la traslación generalmente **no** es una transformación lineal.

**Ejemplo 4: Transformación de \\(\mathbb{R}^n\\) a \\(\mathbb{R}^m\\) definida por una matriz**

Sea \\(A\\) una matriz \\(m \times n\\). La transformación \\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\) definida por \\(T(\mathbf{x}) = A\mathbf{x}\\) (donde \\(\mathbf{x}\\) es un vector columna \\(n \times 1\\)) es una transformación lineal. Esto se debe a que la multiplicación de matrices satisface las propiedades de aditividad y homogeneidad:
\\(A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}\\)
\\(A(c\mathbf{u}) = c(A\mathbf{u})\\)

**Ejemplo 5: Diferenciación de Polinomios**

Sea \\(P_n\\) el espacio vectorial de polinomios de grado como máximo \\(n\\). La transformación \\(D: P_n \rightarrow P_{n-1}\\) definida por \\(D(p(x)) = p'(x)\\) (la derivada de \\(p(x)\\)) es una transformación lineal.
Si \\(p(x)\\) y \\(q(x)\\) son polinomios y \\(c\\) es un escalar:
\\(D(p(x) + q(x)) = (p(x) + q(x))' = p'(x) + q'(x) = D(p(x)) + D(q(x))\\)
\\(D(cp(x)) = (cp(x))' = cp'(x) = cD(p(x))\\)

**Ejemplo 6: Integración de Funciones**

Sea \\(C[a, b]\\) el espacio vectorial de funciones continuas en el intervalo \\([a, b]\\). La transformación \\(I: C[a, b] \rightarrow \mathbb{R}\\) definida por \\(I(f) = \int_a^b f(x) dx\\) es una transformación lineal.
\\(I(f + g) = \int_a^b (f(x) + g(x)) dx = \int_a^b f(x) dx + \int_a^b g(x) dx = I(f) + I(g)\\)
\\(I(cf) = \int_a^b cf(x) dx = c \int_a^b f(x) dx = cI(f)\\)

### Representación Matricial de una Transformación Lineal

Un resultado fundamental en álgebra lineal es que cualquier transformación lineal entre espacios vectoriales de dimensión finita puede ser representada por una matriz.

Sea \\(V\\) un espacio vectorial de dimensión \\(n\\) con base \\(\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\) y \\(W\\) un espacio vectorial de dimensión \\(m\\) con base \\(\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2, ..., \mathbf{c}_m\}\\). Sea \\(T: V \rightarrow W\\) una transformación lineal.

Para encontrar la representación matricial de \\(T\\) con respecto a las bases \\(\mathcal{B}\\) y \\(\mathcal{C}\\) (denotada como \\([T]_{\mathcal{B}}^{\mathcal{C}}\\) o simplemente \\([T]\\) cuando las bases se entienden), necesitamos determinar las imágenes de los vectores base de \\(V\\) bajo \\(T\\) y expresar estas imágenes como combinaciones lineales de los vectores base de \\(W\\).

Para cada \\(\mathbf{b}_j \in \mathcal{B}\\), \\(T(\mathbf{b}_j)\\) es un vector en \\(W\\), por lo que puede escribirse de manera única como una combinación lineal de los vectores base en \\(\mathcal{C}\\):
\\(T(\mathbf{b}_j) = a_{1j}\mathbf{c}_1 + a_{2j}\mathbf{c}_2 + ... + a_{mj}\mathbf{c}_m = \sum_{i=1}^{m} a_{ij}\mathbf{c}_i\\)

Los coeficientes de esta combinación lineal forman la \\(j\\)-ésima columna de la representación matricial \\([T]_{\mathcal{B}}^{\mathcal{C}}\\):
$[T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}$

Si \\(\mathbf{v} \in V\\) tiene un vector de coordenadas \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}\\) con respecto a la base \\(\mathcal{B}\\), entonces el vector de coordenadas de \\(T(\mathbf{v})\\) con respecto a la base \\(\mathcal{C}\\), denotado como \\([T(\mathbf{v})]_{\mathcal{C}}\\), está dado por el producto matricial:
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}}\\)

**Ejemplo: Representación Matricial**

Sea \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) una transformación lineal definida por \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\). Sean las bases estándar para \\(\mathbb{R}^2\\) y \\(\mathbb{R}^3\\) \\(\mathcal{B} = \{\mathbf{e}_1, \mathbf{e}_2\} = \left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right\}\\) y \\(\mathcal{C} = \{\mathbf{f}_1, \mathbf{f}_2, \mathbf{f}_3\} = \left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \right\\).

Encontramos las imágenes de los vectores base de \\(\mathbb{R}^2\\) bajo \\(T\\):
\\(T(\mathbf{e}_1) = T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 + 0 \\ 2(1) - 0 \\ 3(0) \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix} = 1\mathbf{f}_1 + 2\mathbf{f}_2 + 0\mathbf{f}_3\\)
\\(T(\mathbf{e}_2) = T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 0 + 1 \\ 2(0) - 1 \\ 3(1) \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} = 1\mathbf{f}_1 - 1\mathbf{f}_2 + 3\mathbf{f}_3\\)

La representación matricial de \\(T\\) con respecto a las bases estándar es:
\\([T]_{\mathcal{B}}^{\mathcal{C}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix}\\)

Ahora, tomemos un vector arbitrario \\(\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}\\) en \\(\mathbb{R}^2\\). Su vector de coordenadas con respecto a \\(\mathcal{B}\\) es \\([\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} x \\ y \end{pmatrix}\\).
\\([T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}} = \begin{pmatrix} 1 & 1 \\ 2 & -1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\)
El vector de coordenadas con respecto a \\(\mathcal{C}\\) es efectivamente \\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\), que corresponde al vector \\(T(\mathbf{v})\\) que definimos anteriormente.

### Núcleo (Espacio Nulo) de una Transformación Lineal

El **núcleo** (o espacio nulo) de una transformación lineal \\(T: V \rightarrow W\\), denotado por \\(\text{ker}(T)\\) o \\(N(T)\\), es el conjunto de todos los vectores en \\(V\\) que se mapean al vector cero en \\(W\\):
\\(\text{ker}(T) = \{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}_W\}\\)

**Propiedades del Núcleo:**

* El núcleo de una transformación lineal es siempre un subespacio del dominio \\(V\\).
    * **Contiene el vector cero:** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\), por lo que \\(\mathbf{0}_V \in \text{ker}(T)\\).
    * **Cerrado bajo la suma:** Si \\(\mathbf{u}, \mathbf{v} \in \text{ker}(T)\\), entonces \\(T(\mathbf{u}) = \mathbf{0}_W\\) y \\(T(\mathbf{v}) = \mathbf{0}_W\\). Así, \\(T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) = \mathbf{0}_W + \mathbf{0}_W = \mathbf{0}_W\\), por lo que \\(\mathbf{u} + \mathbf{v} \in \text{ker}(T)\\).
    * **Cerrado bajo la multiplicación por escalar:** Si \\(\mathbf{u} \in \text{ker}(T)\\) y \\(c\\) es un escalar, entonces \\(T(c\mathbf{u}) = cT(\mathbf{u}) = c\mathbf{0}_W = \mathbf{0}_W\\), por lo que \\(c\mathbf{u} \in \text{ker}(T)\\).

**Ejemplo: Encontrar el Núcleo**

Considera la transformación lineal \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) definida por \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\).
Para encontrar el núcleo, necesitamos resolver \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\):
\\(\begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}\\)

Esto da el sistema de ecuaciones lineales:
\\(x + y = 0\\)
\\(2x - y = 0\\)
\\(3y = 0\\)

De la tercera ecuación, \\(y = 0\\). Sustituyendo esto en la primera ecuación, \\(x + 0 = 0\\), así que \\(x = 0\\). La segunda ecuación también se satisface: \\(2(0) - 0 = 0\\).
La única solución es \\(x = 0\\) e \\(y = 0\\). Por lo tanto, \\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}\\), que es el subespacio cero de \\(\mathbb{R}^2\\).

### Imagen (Rango) de una Transformación Lineal

La **imagen** (o rango) de una transformación lineal \\(T: V \rightarrow W\\), denotada por \\(\text{im}(T)\\) o \\(R(T)\\), es el conjunto de todos los vectores en \\(W\\) que son la imagen de algún vector en \\(V\\):
\\(\text{im}(T) = \{\mathbf{w} \in W \mid \mathbf{w} = T(\mathbf{v}) \text{ para algún } \mathbf{v} \in V\}\\)

**Propiedades de la Imagen:**

* La imagen de una transformación lineal es siempre un subespacio del codominio \\(W\\).
    * **Contiene el vector cero:** \\(T(\mathbf{0}_V) = \mathbf{0}_W\\), por lo que \\(\mathbf{0}_W \in \text{im}(T)\\).
    * **Cerrado bajo la suma:** Si \\(\mathbf{w}_1, \mathbf{w}_2 \in \text{im}(T)\\), entonces existen \\(\mathbf{v}_1, \mathbf{v}_2 \in V\\) tales que \\(T(\mathbf{v}_1) = \mathbf{w}_1\\) y \\(T(\mathbf{v}_2) = \mathbf{w}_2\\). Entonces \\(\mathbf{w}_1 + \mathbf{w}_2 = T(\mathbf{v}_1) + T(\mathbf{v}_2) = T(\mathbf{v}_1 + \mathbf{v}_2)\\). Dado que \\(\mathbf{v}_1 + \mathbf{v}_2 \in V\\), \\(\mathbf{w}_1 + \mathbf{w}_2 \in \text{im}(T)\\).
    * **Cerrado bajo la multiplicación por escalar:** Si \\(\mathbf{w} \in \text{im}(T)\\) y \\(c\\) es un escalar, entonces existe \\(\mathbf{v} \in V\\) tal que \\(T(\mathbf{v}) = \mathbf{w}\\). Entonces \\(c\mathbf{w} = cT(\mathbf{v}) = T(c\mathbf{v})\\). Dado que \\(c\mathbf{v} \in V\\), \\(c\mathbf{w} \in \text{im}(T)\\).

* Si \\(V\\) es de dimensión finita con una base \\(\{\mathbf{b}_1, \mathbf{b}_2, ..., \mathbf{b}_n\}\\), entonces la imagen de \\(T\\) es el espacio generado por las imágenes de los vectores base:
    \\(\text{im}(T) = \text{span}\{T(\mathbf{b}_1), T(\mathbf{b}_2), ..., T(\mathbf{b}_n)\}\\)

**Ejemplo: Encontrar la Imagen**

Considera la transformación lineal \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) definida por \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\).
Usando la base estándar de \\(\mathbb{R}^2\\), \\(\{\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}\}\\), tenemos:
\\(T\left(\begin{pmatrix} 1 \\ 0 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}\\)
\\(T\left(\begin{pmatrix} 0 \\ 1 \end{pmatrix}\right) = \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}\\)

La imagen de \\(T\\) es el espacio generado por estos dos vectores:
\\(\text{im}(T) = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} \right\}\\)
Este es un subespacio de \\(\mathbb{R}^3\\). Dado que estos dos vectores son linealmente independientes (uno no es un múltiplo escalar del otro), la imagen es un plano que pasa por el origen en \\(\mathbb{R}^3\\).

**Relación entre la Representación Matricial y la Imagen:**

Si \\(T: \mathbb{R}^n \rightarrow \mathbb{R}^m\\) está dada por \\(T(\mathbf{x}) = A\mathbf{x}\\), donde \\(A\\) es una matriz \\(m \times n\\), entonces la imagen de \\(T\\) es el espacio columna de la matriz \\(A\\), es decir, el espacio generado por las columnas de \\(A\\).

### Propiedades de las Transformaciones Lineales: Inyectividad y Sobreyectividad

**Inyectividad (Uno a uno)**

Una transformación lineal \\(T: V \rightarrow W\\) es **inyectiva** (o uno a uno) si para cada \\(\mathbf{w} \in W\\), hay como máximo un \\(\mathbf{v} \in V\\) tal que \\(T(\mathbf{v}) = \mathbf{w}\\). Equivalentemente, si \\(T(\mathbf{u}) = T(\mathbf{v})\\), entonces \\(\mathbf{u} = \mathbf{v}\\).

**Teorema:** Una transformación lineal \\(T: V \rightarrow W\\) es inyectiva si y sólo si su núcleo es el subespacio cero, es decir, \\(\text{ker}(T) = \{\mathbf{0}_V\}\\).

**Demostración:**
* **(\\(\Rightarrow\\)) Supongamos que \\(T\\) es inyectiva.** Si \\(\mathbf{v} \in \text{ker}(T)\\), entonces \\(T(\mathbf{v}) = \mathbf{0}_W\\). También sabemos que \\(T(\mathbf{0}_V) = \mathbf{0}_W\\). Dado que \\(T\\) es inyectiva y \\(T(\mathbf{v}) = T(\mathbf{0}_V)\\), debe ser que \\(\mathbf{v} = \mathbf{0}_V\\). Así, \\(\text{ker}(T) = \{\mathbf{0}_V\}\\).
* **(\\(\Leftarrow\\)) Supongamos que \\(\text{ker}(T) = \{\mathbf{0}_V\}\\).** Supongamos que \\(T(\mathbf{u}) = T(\mathbf{v})\\) para algunos \\(\mathbf{u}, \mathbf{v} \in V\\). Entonces \\(T(\mathbf{u}) - T(\mathbf{v}) = \mathbf{0}_W\\). Por linealidad, \\(T(\mathbf{u} - \mathbf{v}) = \mathbf{0}_W\\). Esto significa que \\(\mathbf{u} - \mathbf{v} \in \text{ker}(T)\\). Dado que \\(\text{ker}(T) = \{\mathbf{0}_V\}\\), tenemos \\(\mathbf{u} - \mathbf{v} = \mathbf{0}_V\\), lo que implica \\(\mathbf{u} = \mathbf{v}\\). Por lo tanto, \\(T\\) es inyectiva.

**Ejemplo: Comprobación de la Inyectividad**

Para la transformación \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) definida por \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\), encontramos que \\(\text{ker}(T) = \left\{ \begin{pmatrix} 0 \\ 0 \end{pmatrix} \right\}\\). Por lo tanto, esta transformación es inyectiva.

**Sobreyectividad (Sobre)**

Una transformación lineal \\(T: V \rightarrow W\\) es **sobreyectiva** (o sobre) si para cada \\(\mathbf{w} \in W\\), existe al menos un \\(\mathbf{v} \in V\\) tal que \\(T(\mathbf{v}) = \mathbf{w}\\). En otras palabras, la imagen de \\(T\\) es igual al codominio \\(W\\), es decir, \\(\text{im}(T) = W\\).

**Teorema (Teorema de la Nulidad y el Rango):** Para una transformación lineal \\(T: V \rightarrow W\\), donde \\(V\\) es un espacio vectorial de dimensión finita,
\\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = \text{dim}(V)\\)
Aquí, \\(\text{dim}(\text{ker}(T))\\) se llama la **nulidad** de \\(T\\), y \\(\text{dim}(\text{im}(T))\\) se llama el **rango** de \\(T\\).

**Relación entre la Sobreyectividad y las Dimensiones:**

Si \\(T: V \rightarrow W\\) es una transformación lineal entre espacios vectoriales de dimensión finita, entonces:
* Si \\(\text{dim}(V) < \text{dim}(W)\\), \\(T\\) no puede ser sobreyectiva. (Por el Teorema de la Nulidad y el Rango, \\(\text{dim}(\text{im}(T)) \leq \text{dim}(V) < \text{dim}(W)\\)).
* Si \\(\text{dim}(V) > \text{dim}(W)\\), \\(T\\) no puede ser inyectiva (porque \\(\text{dim}(\text{ker}(T)) = \text{dim}(V) - \text{dim}(\text{im}(T)) \geq \text{dim}(V) - \text{dim}(W) > 0\\), por lo que el núcleo no es solo el vector cero).
* Si \\(\text{dim}(V) = \text{dim}(W)\\), entonces \\(T\\) es inyectiva si y sólo si es sobreyectiva. (Si \\(T\\) es inyectiva, \\(\text{dim}(\text{ker}(T)) = 0\\), así que \\(\text{dim}(\text{im}(T)) = \text{dim}(V) = \text{dim}(W)\\), lo que significa \\(\text{im}(T) = W\\), así que \\(T\\) es sobreyectiva. Recíprocamente, si \\(T\\) es sobreyectiva, \\(\text{dim}(\text{im}(T)) = \text{dim}(W) = \text{dim}(V)\\), así que \\(\text{dim}(\text{ker}(T)) = 0\\), lo que significa que \\(T\\) es inyectiva).

**Ejemplo: Comprobación de la Sobreyectividad**

Para la transformación \\(T: \mathbb{R}^2 \rightarrow \mathbb{R}^3\\) definida por \\(T\left(\begin{pmatrix} x \\ y \end{pmatrix}\right) = \begin{pmatrix} x + y \\ 2x - y \\ 3y \end{pmatrix}\\), encontramos que \\(\text{im}(T) = \text{span}\left\{ \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix} \right\\}\). La dimensión de la imagen (rango de \\(T\\)) es 2, ya que los dos vectores generadores son linealmente independientes. La dimensión del dominio es \\(\text{dim}(\mathbb{R}^2) = 2\\). Por el Teorema de la Nulidad y el Rango, \\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = 2\\), así que \\(\text{dim}(\text{ker}(T)) + 2 = 2\\), lo que da \\(\text{dim}(\text{ker}(T)) = 0\\), consistente con nuestro hallazgo anterior.

Dado que la dimensión de la imagen (2) es menor que la dimensión del codominio (3), la imagen es un subespacio propio del codominio, y por lo tanto la transformación no es sobreyectiva. Hay vectores en \\(\mathbb{R}^3\\) que no están en la imagen de \\(T\\). Por ejemplo, \\(\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}\\) no puede expresarse como una combinación lineal de \\(\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}\\) y \\(\begin{pmatrix} 1 \\ -1 \\ 3 \end{pmatrix}\\).

**Isomorfismo**

Una transformación lineal \\(T: V \rightarrow W\\) se llama **isomorfismo** si es tanto inyectiva como sobreyectiva. Si existe un isomorfismo entre dos espacios vectoriales \\(V\\) y \\(W\\), entonces se dice que \\(V\\) y \\(W\\) son **isomorfos**, denotado por \\(V \cong W\\). Los espacios vectoriales isomorfos tienen esencialmente la misma estructura algebraica.

Para espacios vectoriales de dimensión finita, dos espacios vectoriales son isomorfos si y sólo si tienen la misma dimensión. Si \\(\text{dim}(V) = \text{dim}(W) = n\\), entonces una transformación lineal \\(T: V \rightarrow W\\) es un isomorfismo si y sólo si es inyectiva o sobreyectiva.

**Resumen de Conceptos Clave:**

* **Transformación Lineal:** Una función entre espacios vectoriales que preserva la suma de vectores y la multiplicación por escalar.
* **Representación Matricial:** Una forma de representar una transformación lineal entre espacios vectoriales de dimensión finita como una matriz.
* **Núcleo (Espacio Nulo):** El conjunto de vectores en el dominio que se mapean al vector cero en el codominio. Es un subespacio del dominio.
* **Imagen (Rango):** El conjunto de vectores en el codominio que son la imagen de algún vector en el dominio. Es un subespacio del codominio.
* **Inyectividad (Uno a uno):** Una transformación lineal es inyectiva si y sólo si su núcleo es el subespacio cero.
* **Sobreyectividad (Sobre):** Una transformación lineal es sobreyectiva si y sólo si su imagen es igual al codominio.
* **Teorema de la Nulidad y el Rango:** Para una transformación lineal \\(T: V \rightarrow W\\) con \\(V\\) de dimensión finita, \\(\text{dim}(\text{ker}(T)) + \text{dim}(\text{im}(T)) = \text{dim}(V)\\).
* **Isomorfismo:** Una transformación lineal que es tanto inyectiva como sobreyectiva.

Este tutorial detallado debería proporcionar una base sólida para comprender las transformaciones lineales. Recuerda practicar con varios ejemplos para solidificar tu comprensión de estos conceptos. ¡Buena suerte con tus estudios!