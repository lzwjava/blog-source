---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Introducción al Algoritmo Union-Find
translated: true
type: note
---

### Introducción al Algoritmo Union-Find (Disjoint Set Union)

El algoritmo **Union-Find** (también llamado **Disjoint Set Union** o **DSU**) es una estructura de datos y un conjunto de operaciones utilizadas para gestionar una colección de conjuntos disjuntos (grupos de elementos que no se superponen). Es eficiente para problemas que implican agrupación, fusión o verificación de conectividad, como en algoritmos de grafos o clustering.

Operaciones clave:
- **Find**: Determina a qué conjunto pertenece un elemento (a menudo encontrando la "raíz" o representante del conjunto).
- **Union**: Fusiona dos conjuntos en uno.

El algoritmo destaca debido a optimizaciones como la **compresión de ruta** (aplanar la estructura de árbol durante las operaciones find) y la **unión por rango/tamaño** (fusionar árboles más pequeños en otros más grandes para mantener la estructura balanceada). Esto hace que el tiempo por operación sea casi O(1) amortizado—muy rápido para grandes conjuntos de datos.

#### Estructura de Datos Principal
- Un array `p[]` (array de padres): `p[i]` apunta al padre del elemento `i`. Inicialmente, cada elemento es su propio padre (`p[i] = i`).
- Opcional: Un array `rank[]` para la unión por rango y balancear las fusiones.

#### La Operación Find (con Compresión de Ruta)
La función `find` rastrea desde un elemento hasta su raíz. La línea que mencionaste—`if (p[i] != -1) i = p[i]`—es un paso recursivo o iterativo en este proceso. Sigue los punteros de los padres hasta alcanzar la raíz (donde `p[root] == root` o `p[root] == -1` para un centinela).

Aquí hay una implementación iterativa simple en pseudocódigo:

```
function find(i):
    if p[i] != -1:  # No es la raíz (o centinela)
        i = p[i]     # Mover al padre (¡esta es tu línea!)
        return find(i)  # Recursivo: continuar hasta la raíz
    else:
        return i     # Raíz encontrada
```

**Con compresión de ruta completa** (para optimizar futuras búsquedas), aplanamos la ruta estableciendo todos los nodos directamente a la raíz:

```
function find(i):
    if p[i] != i:  # No es la raíz
        p[i] = find(p[i])  # Comprimir: establecer el padre a la raíz encontrada
    return p[i]
```

- `-1` se usa a menudo como centinela para las raíces (en lugar de `i` para auto-paternidad), especialmente en algunas implementaciones para distinguir nodos no inicializados o inválidos.
- Sin compresión, las búsquedas repetidas pueden hacer que la estructura sea una cadena larga (peor caso O(n)). La compresión la hace casi plana.

#### La Operación Union
Para fusionar los conjuntos de `x` e `y`:
1. Encontrar las raíces: `rootX = find(x)`, `rootY = find(y)`.
2. Si `rootX != rootY`, enlazar una a la otra (por ejemplo, por rango: adjuntar el de rango más pequeño al más grande).

Pseudocódigo:
```
function union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            p[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            p[rootX] = rootY
        else:
            p[rootY] = rootX
            rank[rootX] += 1  # Aumentar el rango para el nuevo padre
```

#### Cómo Usar el Algoritmo
Union-Find es ideal para problemas de conectividad dinámica. Aquí hay una guía paso a paso con ejemplos:

1. **Inicialización**:
   - Crear `p[]` de tamaño `n` (número de elementos): `for i in 0 to n-1: p[i] = -1` (o `i` para auto-paternidad).
   - Opcional: `rank[]` todo establecido en 0 o 1.

2. **Flujo de Uso Básico**:
   - Para verificar si dos elementos están en el mismo conjunto: `if find(a) == find(b)`.
   - Para fusionar: `union(a, b)`.
   - Procesar consultas/fusiones en cualquier orden—¡es dinámico!

3. **Ejemplo: Detectar Componentes Conectados en un Grafo**
   Imagina un grafo con 5 nodos (0-4) y aristas como (0-1), (1-2), (3-4).
   ```
   // Inicialización
   p = [-1, -1, -1, -1, -1]
   rank = [0, 0, 0, 0, 0]

   // Unir aristas
   union(0, 1)  // Fusiona 0 y 1, digamos p[0]=-1, p[1]=0
   union(1, 2)  // Fusiona 2 en {0,1}, p[2]=0
   union(3, 4)  // Fusiona {3,4}, digamos p[3]=-1, p[4]=3

   // Consulta: ¿Están 0 y 2 conectados? find(0)=0, find(2)=0 → Sí
   // ¿Están 2 y 3 conectados? find(2)=0, find(3)=-1 → No
   ```

4. **Aplicaciones en el Mundo Real**:
   - **Árbol de Expansión Mínima de Kruskal**: Ordenar aristas por peso, unir aristas que no formen ciclos (omitir si `find(u) == find(v)`).
   - **Amigos en una Red Social**: Unir amigos, encontrar conexiones mutuas.
   - **Segmentación de Imágenes**: Unir píxeles adyacentes de color similar.
   - **Detección de Ciclos en Grafos No Dirigidos**: Unir extremos; si ya están en el mismo conjunto, existe un ciclo.

#### Implementación Simple en Python
```python
class UnionFind:
    def __init__(self, n):
        self.p = [-1] * n
        self.rank = [0] * n
    
    def find(self, i):
        if self.p[i] != -1 and self.p[i] != i:  # Maneja centinela + auto-paternidad
            self.p[i] = self.find(self.p[i])  # Compresión de ruta
        return self.p[i] if self.p[i] != -1 else i
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.p[py] = px
            elif self.rank[px] < self.rank[py]:
                self.p[px] = py
            else:
                self.p[py] = px
                self.rank[px] += 1

# Uso
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.find(0) == uf.find(2))  # True
```

Esto mantiene las cosas eficientes—¡pruébalo con un `n` más grande para ver la velocidad!

Para mayor profundidad, consulta [GeeksforGeeks: Union-Find Algorithm](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank-and-path-compression/) o [CP-Algorithms: DSU](https://cp-algorithms.com/data_structures/disjoint_set_union.html).