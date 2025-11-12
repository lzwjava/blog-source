---
audio: false
generated: true
lang: es
layout: post
title: Subespacio
translated: true
type: note
---

Para determinar cuál de los conjuntos dados es un subespacio de $\mathbb{R}^2$, necesitamos verificar si satisfacen las tres condiciones para ser un subespacio:

1.  **El vector cero está en el subespacio.**
2.  **El subespacio es cerrado bajo la suma de vectores.** Si $\mathbf{u}$ y $\mathbf{v}$ están en el subespacio, entonces $\mathbf{u} + \mathbf{v}$ también está en el subespacio.
3.  **El subespacio es cerrado bajo la multiplicación por escalar.** Si $\mathbf{u}$ está en el subespacio y $c$ es cualquier escalar, entonces $c\mathbf{u}$ también está en el subespacio.

Examinemos cada opción:

**a) La recta y = x + 1**

1.  **Vector cero:** El vector cero en $\mathbb{R}^2$ es $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$. Para que este vector esté en la recta, debe satisfacer la ecuación $y = x + 1$. Sustituyendo $x=0$ y $y=0$, obtenemos $0 = 0 + 1$, que es $0 = 1$. Esto es falso, por lo que el vector cero no está en la recta $y = x + 1$.

Dado que la primera condición no se cumple, la recta $y = x + 1$ no es un subespacio de $\mathbb{R}^2$.

**b) La recta y = 2x**

1.  **Vector cero:** Para que el vector cero $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$ esté en la recta, debe satisfacer la ecuación $y = 2x$. Sustituyendo $x=0$ y $y=0$, obtenemos $0 = 2(0)$, que es $0 = 0$. Esto es verdadero, por lo que el vector cero está en la recta $y = 2x$.

2.  **Clausura bajo la suma de vectores:** Sean $\mathbf{u} = \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}$ y $\mathbf{v} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix}$ dos vectores en la recta $y = 2x$. Esto significa que $y_1 = 2x_1$ y $y_2 = 2x_2$.
    Su suma es $\mathbf{u} + \mathbf{v} = \begin{pmatrix} x_1 + x_2 \\ y_1 + y_2 \end{pmatrix}$. Necesitamos verificar si este vector se encuentra en la recta $y = 2x$. Sustituyendo las componentes, obtenemos $y_1 + y_2 = 2(x_1 + x_2)$. Dado que $y_1 = 2x_1$ y $y_2 = 2x_2$, tenemos $2x_1 + 2x_2 = 2x_1 + 2x_2$, lo cual es verdadero. Por lo tanto, la recta es cerrada bajo la suma de vectores.

3.  **Clausura bajo la multiplicación por escalar:** Sea $\mathbf{u} = \begin{pmatrix} x \\ y \end{pmatrix}$ un vector en la recta $y = 2x$, así que $y = 2x$. Sea $c$ cualquier escalar. Entonces $c\mathbf{u} = \begin{pmatrix} cx \\ cy \end{pmatrix}$. Necesitamos verificar si este vector se encuentra en la recta $y = 2x$. Sustituyendo las componentes, obtenemos $cy = 2(cx)$. Dado que $y = 2x$, tenemos $c(2x) = 2(cx)$, que es $2cx = 2cx$. Esto es verdadero, por lo que la recta es cerrada bajo la multiplicación por escalar.

Dado que se cumplen las tres condiciones, la recta $y = 2x$ es un subespacio de $\mathbb{R}^2$.

**c) El círculo unitario**

El círculo unitario en $\mathbb{R}^2$ se define por la ecuación $x^2 + y^2 = 1$.

1.  **Vector cero:** El vector cero es $\begin{pmatrix} 0 \\ 0 \end{pmatrix}$. Sustituyendo en la ecuación, obtenemos $0^2 + 0^2 = 1$, que es $0 = 1$. Esto es falso, por lo que el vector cero no está en el círculo unitario.

Dado que la primera condición no se cumple, el círculo unitario no es un subespacio de $\mathbb{R}^2$.

Respuesta Final: La respuesta final es $\boxed{La recta y = 2x}$

---

El requisito de que "El vector cero está en el subespacio" es una de las **tres condiciones fundamentales** que un subconjunto de un espacio vectorial debe satisfacer para ser considerado un **subespacio**. Analicemos *por qué* esta condición es necesaria.

El concepto de subespacio se trata de identificar conjuntos más pequeños dentro de un espacio vectorial más grande que ellos mismos se comportan como espacios vectoriales. Para comportarse como un espacio vectorial, estos conjuntos más pequeños deben heredar ciertas propiedades esenciales. Una de las propiedades más fundamentales de cualquier espacio vectorial es la existencia de un **vector cero** (a menudo denotado como $\mathbf{0}$). Este vector tiene la propiedad crucial de que cuando se suma a cualquier otro vector en el espacio, deja ese vector sin cambios: $\mathbf{v} + \mathbf{0} = \mathbf{v}$ para todos los vectores $\mathbf{v}$ en el espacio.

He aquí por qué el vector cero debe estar en un subespacio:

1.  **Heredar la Estructura del Espacio Vectorial:** Un subespacio está destinado a ser un "mini-espacio vectorial" dentro de uno más grande. Si un subconjunto no contiene el vector cero, carece de un elemento crucial requerido para satisfacer los axiomas del espacio vectorial. Sin un vector cero, el concepto de inversos aditivos (otro axioma importante) se vuelve problemático.

2.  **Clausura bajo la Multiplicación por Escalar:** Considere un subconjunto no vacío $W$ de un espacio vectorial $V$ que es cerrado bajo la multiplicación por escalar. Si $\mathbf{w}$ es cualquier vector en $W$, y $W$ es un subespacio, entonces para cualquier escalar $c$, el vector $c\mathbf{w}$ también debe estar en $W$. Si elegimos el escalar $c = 0$, entonces $0\mathbf{w} = \mathbf{0}$ (esta es una propiedad de los espacios vectoriales). Por lo tanto, si un subespacio es cerrado bajo la multiplicación por escalar y contiene al menos un vector, *debe* contener el vector cero.

3.  **Garantizar los Inversos Aditivos:** Si bien la presencia del vector cero por sí sola no garantiza la existencia de inversos aditivos dentro del subespacio, su ausencia crea un problema fundamental. Si un vector $\mathbf{v}$ está en el subespacio, y el subespacio es cerrado bajo la multiplicación por escalar, entonces $(-1)\mathbf{v} = -\mathbf{v}$ también debe estar en el subespacio (este es el inverso aditivo de $\mathbf{v}$). Para que la suma de $\mathbf{v}$ y $-\mathbf{v}$ resulte en un vector *dentro* del subespacio, ese vector resultante debe ser el vector cero. Si el vector cero no está en el subconjunto, entonces la clausura bajo la suma podría verse violada incluso si los inversos aditivos existen dentro del espacio vectorial más grande.

En términos más simples, si un subconjunto ni siquiera contiene el "elemento identidad" para la suma de vectores (que es el vector cero), no puede funcionar realmente como un sistema autónomo bajo la suma de vectores y la multiplicación por escalar, que son las operaciones definitorias de un espacio vectorial.

Por lo tanto, la condición de que el vector cero debe estar en el subespacio no es arbitraria; es una consecuencia directa del requisito de que un subespacio debe heredar la estructura algebraica esencial del espacio vectorial más grande en el que reside.