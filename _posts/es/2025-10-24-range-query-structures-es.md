---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Estructuras de Datos Eficientes para Consultas de Rango
translated: true
type: note
---

### Segment Trees y Fenwick Trees: Descripción General

Los Segment Trees y los Fenwick Trees (también llamados Binary Indexed Trees) son estructuras de datos eficientes utilizadas en programación competitiva y algoritmos para manejar consultas de rango y actualizaciones en arreglos. Permiten operaciones como consultas de suma sobre un rango o actualizaciones de puntos en tiempo logarítmico, lo que es mucho más rápido que los enfoques simples de O(n) para grandes conjuntos de datos.

#### Segment Trees
Un **Segment Tree** es una estructura basada en un árbol binario que representa un arreglo dividiéndolo en segmentos (intervalos). Cada nodo en el árbol corresponde a un rango del arreglo:
- Los nodos hoja representan elementos individuales.
- Los nodos padre representan la unión de los rangos de sus hijos (por ejemplo, suma, mínimo, máximo de los subrangos).
- El árbol se construye recursivamente, típicamente con una altura de O(log n) para un arreglo de tamaño n.

**Operaciones Clave:**
- **Construir:** Tiempo O(n) para construir el árbol.
- **Actualizar:** Modificar un solo elemento y propagar los cambios hacia arriba en el árbol en O(log n).
- **Consultar:** Calcular un agregado (por ejemplo, la suma) sobre un rango recorriendo los nodos relevantes en O(log n).

**Casos de Uso:** Consultas de rango de suma/mínimo/máximo, conteo de frecuencia, o cualquier operación asociativa. Es más flexible pero usa un espacio de O(4n).

**Ejemplo Simple (Suma de Rango):**
Imagina un arreglo [1, 3, 5, 7]. El segment tree podría verse así:
- Raíz: suma de [1-7] = 16
- Hijo izquierdo: suma de [1-3] = 4
- Hijo derecho: suma de [5-7] = 12
- Y así sucesivamente, hasta las hojas.

#### Fenwick Trees
Un **Fenwick Tree** (introducido por Peter Fenwick en 1994) es una estructura basada en arreglos más compacta para sumas de prefijo y operaciones similares. Utiliza operaciones bit a bit para indexar elementos de manera eficiente, rastreando sumas acumulativas de forma inteligente:
- Cada índice almacena la suma de un rango que termina en ese índice.
- Las actualizaciones y consultas utilizan manipulación de bits bajos (por ejemplo, `index & -index` para encontrar el bit menos significativo).

**Operaciones Clave:**
- **Construir:** O(n log n) u optimizado a O(n).
- **Actualizar:** Sumar/restar un valor en un índice en O(log n).
- **Consultar:** Obtener la suma de prefijo hasta un índice en O(log n); suma de rango mediante diferencias de prefijo.

**Casos de Uso:** Similar a los segment trees pero optimizado para sumas de prefijo 1D, estadísticas de orden o conteos de inversión. Utiliza un espacio de O(n), lo que lo hace más ligero.

**Ejemplo Simple (Suma de Rango):**
Para el arreglo [1, 3, 5, 7], el arreglo de Fenwick podría ser [1, 4, 5, 16] (ajustes acumulativos). Para consultar la suma[1-3]: prefijo(3) - prefijo(0) = 9.

#### Comparación

| Aspecto          | Segment Tree                  | Fenwick Tree                  |
|------------------|-------------------------------|-------------------------------|
| **Espacio**      | O(4n)                         | O(n)                          |
| **Tiempo Const.**| O(n)                          | O(n log n)                    |
| **Flexibilidad** | Soporta cualquier agregado de rango | Mejor para sumas/actualizaciones de prefijo |
| **Complejidad**  | Código ligeramente más complejo | Implementación más simple     |

Ambas son básicas en algoritmos (por ejemplo, en LeetCode o Codeforces). Si las vas a implementar, ¡comienza con Fenwick por su simplicidad!

Para profundizar más:  
[Tutorial de Segment Tree - GeeksforGeeks](https://www.geeksforgeeks.org/segment-tree-data-structure/)  
[Fenwick Tree Explicado - CP-Algorithms](https://cp-algorithms.com/data_structures/fenwick.html)