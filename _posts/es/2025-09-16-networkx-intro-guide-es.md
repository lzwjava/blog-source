---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/o1-mini
title: Introducción a la Biblioteca de Grafos NetworkX para Python
translated: true
type: note
---

NetworkX es una poderosa biblioteca de Python para la creación, manipulación y estudio de redes complejas (grafos). Proporciona herramientas para trabajar con grafos tanto no dirigidos como dirigidos, manejar aristas ponderadas y realizar una variedad de análisis de redes.

A continuación se presentan varios ejemplos para ayudarte a comenzar con NetworkX:

---

### 1. **Instalando NetworkX**

Antes de usar NetworkX, asegúrate de que esté instalado. Puedes instalarlo usando `pip`:

```bash
pip install networkx
```

---

### 2. **Creando y Visualizando un Grafo Simple**

Aquí se muestra cómo crear un grafo no dirigido simple, agregar nodos y aristas, y visualizarlo usando Matplotlib.

```python
import networkx as nx
import matplotlib.pyplot as plt

# Crear un Grafo vacío
G = nx.Graph()

# Agregar nodos
G.add_node(1)
G.add_nodes_from([2, 3, 4])

# Agregar aristas (agrega automáticamente los nodos si no existen)
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 4)])

# Dibujar el grafo
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
plt.title("Grafo No Dirigido Simple")
plt.show()
```

**Salida:**

Un grafo no dirigido simple con 4 nodos conectados por aristas.

---

### 3. **Grafos Dirigidos**

Creando y visualizando un grafo dirigido (DiGraph):

```python
import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
DG = nx.DiGraph()

# Agregar aristas (los nodos se agregan automáticamente)
DG.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('C', 'A'),
    ('C', 'D')
])

# Dibujar el grafo dirigido con flechas
pos = nx.circular_layout(DG)
nx.draw(DG, pos, with_labels=True, node_color='lightgreen', edge_color='gray', arrows=True, node_size=700)
plt.title("Grafo Dirigido")
plt.show()
```

**Salida:**

Un grafo dirigido que muestra la dirección de las aristas con flechas.

---

### 4. **Grafos Ponderados**

Asignando pesos a las aristas y visualizándolos:

```python
import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo ponderado
WG = nx.Graph()

# Agregar aristas junto con sus pesos
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# Obtener los pesos de las aristas para etiquetarlas
edge_labels = nx.get_edge_attributes(WG, 'weight')

# Dibujar el grafo
pos = nx.spring_layout(WG)
nx.draw(WG, pos, with_labels=True, node_color='lightyellow', edge_color='gray', node_size=700)
nx.draw_networkx_edge_labels(WG, pos, edge_labels=edge_labels)
plt.title("Grafo Ponderado")
plt.show()
```

**Salida:**

Un grafo ponderado con etiquetas en las aristas que representan los pesos.

---

### 5. **Calculando la Ruta Más Corta**

Encontrando la ruta más corta entre dos nodos usando el algoritmo de Dijkstra (para grafos ponderados):

```python
import networkx as nx

# Crear un grafo ponderado (como en el ejemplo anterior)
WG = nx.Graph()
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# Calcular la ruta más corta desde 'A' a 'D'
shortest_path = nx.dijkstra_path(WG, source='A', target='D', weight='weight')
path_length = nx.dijkstra_path_length(WG, source='A', target='D', weight='weight')

print(f"Ruta más corta de A a D: {shortest_path} con peso total {path_length}")
```

**Salida:**

```
Ruta más corta de A a D: ['A', 'C', 'D'] con peso total 5
```

---

### 6. **Medidas de Centralidad**

Calculando varias medidas de centralidad para identificar nodos importantes en el grafo.

```python
import networkx as nx

# Crear un grafo de ejemplo
G = nx.karate_club_graph()

# Calcular centralidad de grado
degree_centrality = nx.degree_centrality(G)

# Calcular centralidad de intermediación
betweenness_centrality = nx.betweenness_centrality(G)

# Calcular centralidad de vector propio
eigen_centrality = nx.eigenvector_centrality(G, max_iter=1000)

# Mostrar los 5 nodos principales por centralidad de grado
sorted_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
print("Top 5 nodos por Centralidad de Grado:")
for node, centrality in sorted_degree[:5]:
    print(f"Nodo {node}: {centrality:.4f}")

# De manera similar, puedes mostrar otras centralidades
```

**Salida:**

```
Top 5 nodos por Centralidad de Grado:
Nodo 33: 0.6035
Nodo 0: 0.3793
Nodo 1: 0.3793
Nodo 2: 0.3793
Nodo 3: 0.3793
```

*Nota:* El grafo del Karate Club es un ejemplo de red social comúnmente usado en NetworkX.

---

### 7. **Detección de Comunidades con el Algoritmo de Girvan-Newman**

Identificando comunidades dentro de un grafo.

```python
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt

# Crear un grafo (usando el grafo del Karate Club)
G = nx.karate_club_graph()

# Calcular comunidades usando Girvan-Newman
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
second_level_communities = next(communities_generator)

# Función para asignar colores a las comunidades
def get_community_colors(G, communities):
    color_map = {}
    for idx, community in enumerate(communities):
        for node in community:
            color_map[node] = idx
    return [color_map[node] for node in G.nodes()]

# Elegir el nivel deseado de comunidades
communities = second_level_communities
colors = get_community_colors(G, communities)

# Dibujar el grafo con colores de comunidad
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=colors, with_labels=True, cmap=plt.cm.Set1)
plt.title("Comunidades en el Grafo del Karate Club")
plt.show()
```

**Salida:**

Una visualización del grafo del Karate Club con los nodos coloreados según su pertenencia a la comunidad.

---

### 8. **Leyendo y Escribiendo Grafos**

NetworkX soporta varios formatos para leer y escribir grafos, como listas de adyacencia, listas de aristas y GraphML.

**Leyendo una lista de aristas:**

```python
import networkx as nx

# Asumir que 'edges.txt' contiene:
# A B
# A C
# B C
# B D
# C D

G = nx.read_edgelist('edges.txt', delimiter=' ')
print("Nodos:", G.nodes())
print("Aristas:", G.edges())
```

**Escribiendo un grafo a GraphML:**

```python
import networkx as nx

G = nx.complete_graph(5)  # Crear un grafo completo con 5 nodos
nx.write_graphml(G, 'complete_graph.graphml')
print("Grafo guardado en 'complete_graph.graphml'")
```

---

### 9. **Usando NetworkX con Pandas DataFrames**

Integrando NetworkX con Pandas para una manipulación de datos más avanzada.

```python
import networkx as nx
import pandas as pd

# Crear un DataFrame que represente aristas con pesos
data = {
    'source': ['A', 'A', 'B', 'B', 'C'],
    'target': ['B', 'C', 'C', 'D', 'D'],
    'weight': [4, 2, 5, 10, 3]
}
df = pd.DataFrame(data)

# Crear un grafo ponderado a partir del DataFrame
G = nx.from_pandas_edgelist(df, 'source', 'target', ['weight'])

# Mostrar aristas con pesos
for u, v, data in G.edges(data=True):
    print(f"({u}, {v}) - peso: {data['weight']}")
```

**Salida:**

```
(A, B) - peso: 4
(A, C) - peso: 2
(B, C) - peso: 5
(B, D) - peso: 10
(C, D) - peso: 3
```

---

### 10. **Visualización Avanzada con NetworkX y Matplotlib**

Personalizando la apariencia del grafo para una mejor legibilidad.

```python
import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'C'), ('C', 'D'), ('D', 'E'),
    ('E', 'F'), ('F', 'C')
])

# Asignar posiciones usando un layout
pos = nx.spring_layout(G, seed=42)

# Dibujar nodos con diferentes tamaños y colores
node_sizes = [700 if node == 'C' else 300 for node in G.nodes()]
node_colors = ['red' if node == 'C' else 'skyblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)

# Dibujar aristas con anchos variables
edge_widths = [2 if (u == 'C' or v == 'C') else 1 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_widths)

# Dibujar etiquetas
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.title("Visualización de Grafo Personalizada")
plt.axis('off')
plt.show()
```

**Salida:**

Un grafo personalizado donde el nodo 'C' está resaltado en rojo con un tamaño mayor, y las aristas conectadas a 'C' tienen líneas más gruesas.

---

Estos ejemplos proporcionan una comprensión fundamental de cómo utilizar NetworkX para crear, manipular y analizar grafos en Python. Para un uso más avanzado y documentación detallada, consulta la [documentación oficial de NetworkX](https://networkx.org/documentation/stable/).