---
audio: false
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Beispiele zur Erstellung und Analyse von Netzwerken mit NetworkX
translated: true
type: note
---

NetworkX ist eine leistungsstarke Python-Bibliothek zum Erstellen, Analysieren und Visualisieren komplexer Netzwerke. Hier sind mehrere Beispiele, die ihre Fähigkeiten demonstrieren:

## 1. Grundlegende Graphen-Erstellung und Visualisierung

```python
import networkx as nx
import matplotlib.pyplot as plt

# Einen leeren Graphen erstellen
G = nx.Graph()

# Knoten hinzufügen
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from(range(4, 7))

# Kanten hinzufügen
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4), (4, 5), (5, 6), (6, 1)])

# Den Graphen visualisieren
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
```

## 2. Beispiel für einen gerichteten Graphen

```python
# Einen gerichteten Graphen erstellen
D = nx.DiGraph()

# Kanten hinzufügen (fügt automatisch Knoten hinzu)
D.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Mit verschiedenen Knotenfarben zeichnen
pos = nx.spring_layout(D)
nx.draw(D, pos, with_labels=True, node_color='lightgreen',
        edge_color='red', node_size=1000, arrowsize=20)
plt.show()
```

## 3. Beispiel für Graphen-Analyse

```python
# Einen Graphen erstellen
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# Grundlegende Graphen-Eigenschaften
print("Anzahl der Knoten:", G.number_of_nodes())
print("Anzahl der Kanten:", G.number_of_edges())
print("Knoten:", G.nodes())
print("Kanten:", G.edges())
print("Grad von Knoten 2:", G.degree(2))
print("Nachbarn von Knoten 2:", list(G.neighbors(2)))
print("Ist der Graph verbunden?", nx.is_connected(G))
print("Kürzester Pfad von 1 zu 5:", nx.shortest_path(G, 1, 5))
```

## 4. Beispiel für einen gewichteten Graphen

```python
# Einen gewichteten Graphen erstellen
G = nx.Graph()

# Gewichtete Kanten hinzufügen
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=1)
G.add_edge('C', 'D', weight=5)

# Mit Kantenbeschriftungen für die Gewichte zeichnen
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightcoral')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
```

## 5. Beispiel für die Analyse sozialer Netzwerke

```python
# Einen Graphen für ein soziales Netzwerk erstellen
social = nx.Graph()

# Personen und ihre Verbindungen hinzufügen
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
social.add_nodes_from(people)

connections = [('Alice', 'Bob'), ('Alice', 'Charlie'),
               ('Bob', 'Charlie'), ('Bob', 'David'),
               ('Charlie', 'Eve'), ('David', 'Eve')]
social.add_edges_from(connections)

# Zentrale Maßzahlen berechnen
degree_centrality = nx.degree_centrality(social)
betweenness_centrality = nx.betweenness_centrality(social)
closeness_centrality = nx.closeness_centrality(social)

print("Degree Centrality:", degree_centrality)
print("Betweenness Centrality:", betweenness_centrality)
print("Closeness Centrality:", closeness_centrality)

# Visualisieren
nx.draw(social, with_labels=True, node_color='lightgreen', node_size=2000)
plt.show()
```

## 6. Zufallsgraphen-Generierung

```python
# Einen Erdős–Rényi Zufallsgraphen erstellen
random_graph = nx.erdos_renyi_graph(10, 0.3)  # 10 Knoten, 30% Kantenwahrscheinlichkeit

# Visualisieren
nx.draw(random_graph, with_labels=True, node_color='skyblue')
plt.show()
```

## 7. Beispiel für Graph-Algorithmen

```python
# Einen Graphen erstellen
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

# Alle einfachen Pfade zwischen zwei Knoten finden
print("Alle Pfade von 1 zu 6:", list(nx.all_simple_paths(G, 1, 6)))

# Minimaler Spannbaum
T = nx.minimum_spanning_tree(G)
print("Kanten im MST:", T.edges())

# Community-Erkennung (benötigt das python-louvain Paket)
# pip install python-louvain
try:
    import community as community_louvain
    partition = community_louvain.best_partition(G)
    print("Community-Partition:", partition)
except ImportError:
    print("Installieren Sie python-louvain für Community-Erkennung")
```

Diese Beispiele decken grundlegende Graphen-Erstellung, Visualisierung, Analyse und einige gängige Algorithmen ab. NetworkX bietet viele weitere Funktionen für die Arbeit mit komplexen Netzwerken.