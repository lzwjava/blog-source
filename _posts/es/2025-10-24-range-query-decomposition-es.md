---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descomposición de Raíz Cuadrada para Consultas de Rango
translated: true
type: note
---

### Descomposición de Raíz Cuadrada

La Descomposición de Raíz Cuadrada (a menudo abreviada como √-descomposición) es una técnica en ciencias de la computación y programación competitiva utilizada para optimizar consultas de rango y actualizaciones en arreglos o estructuras de datos grandes. Es particularmente útil cuando necesitas responder consultas como "encontrar la suma/máximo/mínimo de elementos en un subarreglo" de manera eficiente, sin depender de maquinaria pesada como árboles de segmentos o árboles de Fenwick, que pueden ser más complejos de implementar.

#### ¿Por qué usarla?
- **Compensación de Complejidad Temporal**: Para un arreglo de tamaño \\( n \\), las consultas de rango ingenuas toman \\( O(n) \\) tiempo por consulta. La Descomposición de Raíz Cuadrada reduce esto a \\( O(\sqrt{n}) \\) por consulta y actualización, lo cual es un buen equilibrio para muchos problemas donde \\( n \\) es hasta \\( 10^5 \\) o \\( 10^6 \\).
- **Simplicidad**: Es más fácil de codificar y depurar en comparación con estructuras de datos avanzadas.
- **Aplicaciones**: Común en problemas que involucran consultas de suma de rango, consultas de mínimo de rango (RMQ) o conteo de frecuencia en ventanas deslizantes.

#### Cómo Funciona
1. **Dividir en Bloques**: Divide el arreglo en bloques de tamaño \\( \sqrt{n} \\) (redondeado hacia abajo). Si \\( n = 100 \\), el tamaño del bloque \\( b = 10 \\), así obtienes 10 bloques.
   - Cada bloque almacena información precalculada (por ejemplo, la suma de los elementos en ese bloque para consultas de suma).

2. **Consultar un Rango [L, R]**:
   - **Bloques Completos**: Para bloques completos totalmente dentro de [L, R], simplemente obtén el valor precalculado en \\( O(1) \\) por bloque. Como máximo \\( O(\sqrt{n}) \\) bloques completos.
   - **Bloques Parciales**: Para los bordes (bloques parciales izquierdo y derecho), itera a través de los elementos individuales manualmente, lo que toma \\( O(\sqrt{n}) \\) tiempo en total (ya que cada bloque parcial es de tamaño \\( \sqrt{n} \\)).
   - Total: \\( O(\sqrt{n}) \\).

3. **Actualizaciones**: Al actualizar un elemento, reconstruye el valor precalculado para su bloque en \\( O(\sqrt{n}) \\) tiempo (recalculando la suma del bloque).

#### Ejemplo Simple: Consulta de Suma de Rango
Supongamos que tenemos un arreglo `A = [1, 3, 2, 4, 5]` y \\( n=5 \\), entonces el tamaño del bloque \\( b = \sqrt{5} \approx 2 \\). Bloques:
- Bloque 0: [1, 3] → suma = 4
- Bloque 1: [2, 4] → suma = 6
- Bloque 2: [5] → suma = 5 (el último bloque puede ser más pequeño)

Consulta de suma del índice 1 al 4 (basado en 0: elementos 3,2,4,5):
- Parcial izquierdo: Índice 1 (en Bloque 0) → suma 3
- Bloque Completo 1: Suma 6
- Parcial derecho: Índice 4 (en Bloque 2) → suma 5
- Total: 3 + 6 + 5 = 14

Para implementar en código (pseudocódigo Python):
```python
import math

class SqrtDecomp:
    def __init__(self, arr):
        self.n = len(arr)
        self.b = int(math.sqrt(self.n))
        self.arr = arr[:]
        self.block_sums = [0] * ((self.n + self.b - 1) // self.b)
        self._build()
    
    def _build(self):
        for i in range(self.n):
            block_id = i // self.b
            self.block_sums[block_id] += self.arr[i]
    
    def update(self, idx, val):
        diff = val - self.arr[idx]
        self.arr[idx] = val
        block_id = idx // self.b
        self.block_sums[block_id] += diff
    
    def query(self, left, right):
        res = 0
        l_block, r_block = left // self.b, right // self.b
        
        if l_block == r_block:
            for i in range(left, right + 1):
                res += self.arr[i]
        else:
            # Parcial izquierdo
            for i in range(left, (l_block + 1) * self.b):
                res += self.arr[i]
            # Bloques completos
            for blk in range(l_block + 1, r_block):
                res += self.block_sums[blk]
            # Parcial derecho
            for i in range(r_block * self.b, right + 1):
                res += self.arr[i]
        return res
```

Esta es una versión básica—adáptala para min/max almacenando min/max por bloque en lugar de sumas.

Para análisis más profundos, consulta recursos como [GeeksforGeeks on Square Root Decomposition](https://www.geeksforgeeks.org/sqrt-decomposition-algorithm-square-root-decomposition-technique-set-1-introduction/) o [CP-Algorithms](https://cp-algorithms.com/data_structures/sqrt_decomposition.html).