---
audio: false
generated: true
lang: es
layout: post
title: Forma cuadrática
translated: true
type: note
---

En álgebra lineal, una **forma cuadrática** es una función $Q: \mathbb{R}^n \rightarrow \mathbb{R}$ que puede expresarse como:

$Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$

donde:
* $\mathbf{x}$ es un vector columna en $\mathbb{R}^n$:
    $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}$
* $A$ es una matriz simétrica de $n \times n$ con entradas reales. Esta matriz se denomina **matriz de la forma cuadrática**.
* $\mathbf{x}^T$ es la transpuesta de $\mathbf{x}$, que es un vector fila.

**En términos más simples:**

Una forma cuadrática es un polinomio homogéneo de grado dos en $n$ variables. "Homogéneo" significa que cada término del polinomio tiene un grado total de dos.

Por ejemplo, en dos variables ($n=2$), una forma cuadrática se ve así:
$Q(x_1, x_2) = a x_1^2 + b x_1 x_2 + c x_2^2$

Esto puede escribirse en forma matricial como:
$Q(x_1, x_2) = \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} a & b/2 \\ b/2 & c \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$

Nótese que las entradas fuera de la diagonal de la matriz $A$ son la mitad del coeficiente del término cruzado ($x_1 x_2$). Usamos una matriz simétrica $A$ porque para cualquier matriz $B$, $\mathbf{x}^T B \mathbf{x} = \mathbf{x}^T \left( \frac{B + B^T}{2} \right) \mathbf{x}$, y $\frac{B + B^T}{2}$ es siempre una matriz simétrica. Usar la forma simétrica simplifica muchas propiedades y teoremas relacionados con las formas cuadráticas.

**Aspectos Clave de las Formas Cuadráticas:**

* **Representación Matricial:** Toda forma cuadrática puede ser representada de manera única por una matriz simétrica.
* **Evaluación:** El valor de la forma cuadrática $Q(\mathbf{x})$ es un escalar obtenido por la multiplicación matricial $\mathbf{x}^T A \mathbf{x}$.
* **Clasificación:** Las formas cuadráticas pueden clasificarse según los valores que toman para vectores no nulos $\mathbf{x}$:
    * **Definida positiva:** $Q(\mathbf{x}) > 0$ para todo $\mathbf{x} \neq \mathbf{0}$. Esto ocurre si y solo si todos los valores propios de $A$ son positivos.
    * **Semidefinida positiva:** $Q(\mathbf{x}) \ge 0$ para todo $\mathbf{x}$. Esto ocurre si y solo si todos los valores propios de $A$ son no negativos.
    * **Definida negativa:** $Q(\mathbf{x}) < 0$ para todo $\mathbf{x} \neq \mathbf{0}$. Esto ocurre si y solo si todos los valores propios de $A$ son negativos.
    * **Semidefinida negativa:** $Q(\mathbf{x}) \le 0$ para todo $\mathbf{x}$. Esto ocurre si y solo si todos los valores propios de $A$ son no positivos.
    * **Indefinida:** $Q(\mathbf{x})$ toma valores tanto positivos como negativos. Esto ocurre si y solo si $A$ tiene tanto valores propios positivos como negativos.
* **Cambio de Variables:** Al realizar un cambio lineal de variables $\mathbf{x} = P\mathbf{y}$, donde $P$ es una matriz invertible, la forma cuadrática puede transformarse en una nueva forma cuadrática en términos de $\mathbf{y}$ con una representación matricial diferente ($P^T A P$). Un objetivo clave a menudo es encontrar una transformación ortogonal (donde $P$ es una matriz ortogonal) que diagonalice la matriz $A$, resultando en una forma cuadrática sin términos cruzados (solo términos al cuadrado). Esto está relacionado con el Teorema del Eje Principal.

**Aplicaciones de las Formas Cuadráticas:**

Las formas cuadráticas aparecen en varias áreas de las matemáticas, la física, la estadística y la ingeniería, incluyendo:

* **Secciones Cónicas y Superficies Cuádricas:** Las ecuaciones de estos objetos geométricos pueden expresarse usando formas cuadráticas.
* **Optimización:** Determinar la naturaleza de los puntos críticos de funciones multivariables a menudo implica analizar la forma cuadrática de la matriz Hessiana.
* **Análisis de Estabilidad:** En sistemas dinámicos, las formas cuadráticas (como las funciones de Lyapunov) se utilizan para analizar la estabilidad de los puntos de equilibrio.
* **Estadística:** Las matrices de covarianza definen formas cuadráticas que describen la dispersión y correlación de los datos.
* **Mecánica y Física:** La energía cinética y potencial en algunos sistemas puede expresarse como formas cuadráticas.

En resumen, una forma cuadrática es un concepto fundamental en álgebra lineal que proporciona una forma de expresar y analizar polinomios cuadráticos homogéneos usando el lenguaje de vectores y matrices. Su representación matricial y clasificación basada en la definición son cruciales para comprender sus propiedades y aplicaciones.