---
audio: false
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Ejemplos de Creación y Análisis de Grafos con NetworkX
translated: true
type: note
---

NetworkX es una poderosa librería de Python para crear, analizar y visualizar redes complejas. Aquí hay varios ejemplos que demuestran sus capacidades:

## 1. Creación y Visualización Básica de Grafos

```python
import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío
G = nx.Graph()

# Añadir nodos
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from(range(4, 7))

# Añadir aristas
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4), (4, 5), (5, 6), (6, 1)])

# Visualizar el grafo
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
```

## 2. Ejemplo de Grafo Dirigido

```python
# Crear un grafo dirigido
D = nx.DiGraph()

# Añadir aristas (añade nodos automáticamente)
D.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Dibujar con diferentes colores de nodo
pos = nx.spring_layout(D)
nx.draw(D, pos, with_labels=True, node_color='lightgreen',
        edge_color='red', node_size=1000, arrowsize=20)
plt.show()
```

## 3. Ejemplo de Análisis de Grafos

```python
# Crear un grafo
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# Propiedades básicas del grafo
print("Número de nodos:", G.number_of_nodes())
print("Número de aristas:", G.number_of_edges())
print("Nodos:", G.nodes())
print("Aristas:", G.edges())
print("Grado del nodo 2:", G.degree(2))
print("Vecinos del nodo 2:", list(G.neighbors(2)))
print("¿Está el grafo conectado?", nx.is_connected(G))
print("Camino más corto de 1 a 5:", nx.shortest_path(G, 1, 5))
```

## 4. Ejemplo de Grafo Ponderado

```python
# Crear un grafo ponderado
G = nx.Graph()

# Añadir aristas ponderadas
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=1)
G.add_edge('C', 'D', weight=5)

# Dibujar con etiquetas en las aristas mostrando los pesos
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightcoral')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
```

## 5. Ejemplo de Análisis de Redes Sociales

```python
# Crear un grafo de red social
social = nx.Graph()

# Añadir personas y sus conexiones
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
social.add_nodes_from(people)

connections = [('Alice', 'Bob'), ('Alice', 'Charlie'),
               ('Bob', 'Charlie'), ('Bob', 'David'),
               ('Charlie', 'Eve'), ('David', 'Eve')]
social.add_edges_from(connections)

# Calcular medidas de centralidad
degree_centrality = nx.degree_centrality(social)
betweenness_centrality = nx.betweenness_centrality(social)
closeness_centrality = nx.closeness_centrality(social)

print("Centralidad de Grado:", degree_centrality)
print("Centralidad de Intermediación:", betweenness_centrality)
print("Centralidad de Cercanía:", closeness_centrality)

# Visualizar
nx.draw(social, with_labels=True, node_color='lightgreen', node_size=2000)
plt.show()
```

## 6. Generación de Grafos Aleatorios

```python
# Crear un grafo aleatorio Erdős–Rényi
random_graph = nx.erdos_renyi_graph(10, 0.3)  # 10 nodos, 30% probabilidad de arista

# Visualizar
nx.draw(random_graph, with_labels=True, node_color='skyblue')
plt.show()
```

## 7. Ejemplo de Algoritmos de Grafos

```python
# Crear un grafo
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

# Encontrar todos los caminos simples entre dos nodos
print("Todos los caminos de 1 a 6:", list(nx.all_simple_paths(G, 1, 6)))

# Árbol de expansión mínima
T = nx.minimum_spanning_tree(G)
print("Aristas en el MST:", T.edges())

# Detección de comunidades (requiere el paquete python-louvain)
# pip install python-louvain
try:
    import community as community_louvain
    partition = community_louvain.best_partition(G)
    print("Partición de comunidades:", partition)
except ImportError:
    print("Instala python-louvain para la detección de comunidades")
```

Estos ejemplos cubren la creación básica de grafos, visualización, análisis y algunos algoritmos comunes. NetworkX proporciona muchas más características para trabajar con redes complejas.