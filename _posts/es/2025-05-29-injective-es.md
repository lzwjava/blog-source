---
audio: false
generated: true
lang: es
layout: post
title: Funciones Inyectivas
translated: true
type: note
---

En matemáticas, el término "inyectiva" se refiere a una función o mapeo entre dos conjuntos donde elementos distintos del primer conjunto se mapean a elementos distintos del segundo conjunto. En otras palabras, no hay dos elementos diferentes en el dominio (el primer conjunto) que se mapeen al mismo elemento en el codominio (el segundo conjunto).

Esta propiedad también se conoce como "uno a uno". Si una función \\( f \\) es inyectiva, entonces para cualesquiera dos elementos \\( x \\) e \\( y \\) en el dominio, si \\( f(x) = f(y) \\), entonces debe ser el caso que \\( x = y \\). Esto asegura que cada elemento en el codominio es mapeado por como máximo un elemento en el dominio.

---

Para entender por qué una transformación lineal \\( T \\) es inyectiva si su kernel contiene solo el vector cero, desglosemos las definiciones e implicaciones:

1.  **Kernel de una Transformación**: El kernel de una transformación lineal \\( T: V \rightarrow W \\) (denotado como \\( \ker(T) \\)) es el conjunto de todos los vectores en \\( V \\) que se mapean al vector cero en \\( W \\). Matemáticamente, \\( \ker(T) = \{ v \in V \mid T(v) = 0 \} \\).

2.  **Transformación Inyectiva**: Una transformación lineal \\( T \\) es inyectiva (o uno a uno) si vectores diferentes en \\( V \\) se mapean a vectores diferentes en \\( W \\). En otras palabras, si \\( T(u) = T(v) \\), entonces \\( u = v \\).

Ahora, conectemos estos dos conceptos:

- Supongamos que \\( \ker(T) = \{0\} \\). Esto significa que el único vector en \\( V \\) que se mapea al vector cero en \\( W \\) es el propio vector cero.
- Para mostrar que \\( T \\) es inyectiva, asumamos que \\( T(u) = T(v) \\). Por la linealidad de \\( T \\), tenemos \\( T(u) - T(v) = T(u - v) = 0 \\).
- Dado que \\( \ker(T) = \{0\} \\), \\( T(u - v) = 0 \\) implica que \\( u - v = 0 \\), lo que significa que \\( u = v \\).

Así, si \\( \ker(T) = \{0\} \\), la transformación \\( T \\) es inyectiva. Esto se debe a que la única solución para \\( T(v) = 0 \\) es \\( v = 0 \\), asegurando que no hay dos vectores distintos en \\( V \\) que se mapeen al mismo vector en \\( W \\).

---

La ecuación \\( T(u) - T(v) = T(u - v) \\) es una consecuencia de la propiedad de linealidad de una transformación lineal \\( T \\). Desglosemos por qué esto se cumple:

1.  **Linealidad de \\( T \\)**: Una transformación lineal \\( T \\) satisface dos propiedades clave para cualquier vector \\( u \\) y \\( v \\) en el espacio vectorial y cualquier escalar \\( c \\):
    - **Aditividad**: \\( T(u + v) = T(u) + T(v) \\)
    - **Homogeneidad**: \\( T(cu) = cT(u) \\)

2.  **Derivación de \\( T(u) - T(v) = T(u - v) \\)**:
    - Usando la propiedad de aditividad, podemos expresar \\( T(u - v) \\) como \\( T(u + (-v)) \\), lo que equivale a \\( T(u) + T(-v) \\).
    - Por la propiedad de homogeneidad, \\( T(-v) = -T(v) \\).
    - Por lo tanto, \\( T(u - v) = T(u) + (-T(v)) = T(u) - T(v) \\).

Así, \\( T(u) - T(v) = T(u - v) \\) es un resultado directo de la linealidad de \\( T \\). Esta propiedad es fundamental en álgebra lineal y se usa frecuentemente en demostraciones y derivaciones que involucran transformaciones lineales.