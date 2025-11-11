---
audio: false
generated: true
lang: es
layout: post
title: Prueba de Independencia Lineal
translated: true
type: note
---

23. Dado que los vectores \\( \alpha_1, \alpha_2, \alpha_3 \\) son linealmente independientes, y los vectores \\( \beta_1 = \alpha_1 + 2\alpha_2 \\), \\( \beta_2 = -\alpha_1 + \alpha_2 - 3\alpha_3 \\), \\( \beta_3 = 3\alpha_1 + 6\alpha_3 \\). Demuestre que los vectores \\( \beta_1, \beta_2, \beta_3 \\) son linealmente dependientes.

### Solución:
Para demostrar que los vectores \\( \beta_1, \beta_2, \beta_3 \\) son linealmente dependientes, necesitamos mostrar que existen escalares \\( c_1, c_2, c_3 \\) (no todos cero) tales que:

\\[ c_1 \beta_1 + c_2 \beta_2 + c_3 \beta_3 = 0 \\]

Dado:
\\[ \beta_1 = \alpha_1 + 2\alpha_2 \\]
\\[ \beta_2 = -\alpha_1 + \alpha_2 - 3\alpha_3 \\]
\\[ \beta_3 = 3\alpha_1 + 6\alpha_3 \\]

Necesitamos encontrar constantes \\( c_1, c_2, c_3 \\) tales que:

\\[ c_1 (\alpha_1 + 2\alpha_2) + c_2 (-\alpha_1 + \alpha_2 - 3\alpha_3) + c_3 (3\alpha_1 + 6\alpha_3) = 0 \\]

Esto se puede reescribir como:

\\[ (c_1 - c_2 + 3c_3)\alpha_1 + (2c_1 + c_2)\alpha_2 + (-3c_2 + 6c_3)\alpha_3 = 0 \\]

Dado que \\( \alpha_1, \alpha_2, \alpha_3 \\) son linealmente independientes, los coeficientes de \\( \alpha_1, \alpha_2, \alpha_3 \\) deben ser cada uno cero:

1. \\( c_1 - c_2 + 3c_3 = 0 \\)
2. \\( 2c_1 + c_2 = 0 \\)
3. \\( -3c_2 + 6c_3 = 0 \\)

Resolvamos este sistema de ecuaciones:

De la ecuación 2:
\\[ 2c_1 + c_2 = 0 \implies c_2 = -2c_1 \\]

De la ecuación 3:
\\[ -3c_2 + 6c_3 = 0 \implies -3(-2c_1) + 6c_3 = 0 \implies 6c_1 + 6c_3 = 0 \implies c_3 = -c_1 \\]

Sustituya \\( c_2 = -2c_1 \\) y \\( c_3 = -c_1 \\) en la ecuación 1:
\\[ c_1 - (-2c_1) + 3(-c_1) = 0 \implies c_1 + 2c_1 - 3c_1 = 0 \implies 0 = 0 \\]

Esto se cumple para cualquier \\( c_1 \\). Elijamos \\( c_1 = 1 \\):

Entonces:
\\[ c_2 = -2 \\]
\\[ c_3 = -1 \\]

Por lo tanto, hemos encontrado constantes \\( c_1 = 1, c_2 = -2, c_3 = -1 \\) tales que:

\\[ 1 \cdot \beta_1 - 2 \cdot \beta_2 - 1 \cdot \beta_3 = 0 \\]

Esto demuestra que los vectores \\( \beta_1, \beta_2, \beta_3 \\) son linealmente dependientes.