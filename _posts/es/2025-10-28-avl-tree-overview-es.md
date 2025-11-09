---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descripción General del Árbol AVL
translated: true
type: note
---

### ¿Qué es un árbol AVL?

Un árbol AVL es un tipo de **árbol binario de búsqueda auto-balanceado (BST)**, inventado en 1962 por Georgy Adelson-Velsky y Evgenii Landis (de ahí el nombre). Como cualquier BST, almacena datos de manera ordenada: todos los nodos en el subárbol izquierdo son menores que el padre, y todos en el derecho son mayores. La característica clave es que ajusta automáticamente su estructura después de inserciones o eliminaciones para mantenerse equilibrado.

### ¿Cómo funciona?

- **Factor de Equilibrio**: Para cada nodo, el árbol calcula un "factor de equilibrio" como la altura del subárbol izquierdo menos la altura del subárbol derecho. Este debe ser siempre -1, 0 o +1 (es decir, los subárboles difieren como máximo en un nivel).
- **Rotaciones para el Equilibrio**: Si una inserción o eliminación viola el factor de equilibrio:
  - **Rotaciones simples** (izquierda o derecha) corrigen desequilibrios donde la violación está en el hijo más cercano.
  - **Rotaciones dobles** (izquierda-derecha o derecha-izquierda) manejan casos donde está en el hijo más lejano.
- Estas rotaciones preservan la propiedad BST mientras restauran el equilibrio, y se ejecutan en tiempo O(1) por operación.

Ejemplo: Insertar nodos en orden secuencial en un BST simple lo convertiría en una lista enlazada (desequilibrado). En un árbol AVL, las rotaciones lo mantienen aproximadamente equilibrado en altura, como este antes/después simplificado:

```
Desequilibrado (después de inserciones: 1,2,3):
    2
   /
  1
 /
3  (en realidad, sesgado a la derecha: 1->2->3)

Después de la rotación:
  2
 / \
1   3
```

### ¿Por qué es especial?

- **Eficiencia Garantizada**: A diferencia de los BST regulares, que pueden volverse O(n) en el peor caso (por ejemplo, sesgado como una lista), los árboles AVL garantizan un tiempo **O(log n)** promedio y en el peor caso para buscar, insertar y eliminar. Esto los hace ideales para aplicaciones que necesitan un rendimiento consistente, como bases de datos o tablas de símbolos.
- **Compromiso**: Son más estrictos que otros árboles equilibrados (por ejemplo, los árboles rojo-negro, que permiten un poco más de desequilibrio para inserciones/eliminaciones más rápidas). AVL prioriza la velocidad de búsqueda sobre la velocidad de modificación.
- **Espacio**: Utiliza un campo adicional por nodo para el seguimiento de la altura/equilibrio, pero es menor.

En resumen, los árboles AVL son "especiales" por su riguroso auto-equilibrio, transformando BSTs potencialmente caóticos en ejecutores logarítmicos confiables.

Para más detalles: [Árbol AVL en Wikipedia](https://en.wikipedia.org/wiki/AVL_tree)