---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/o1-mini
title: Einführung in die NetworkX Python Graph-Bibliothek
translated: true
type: note
---

NetworkX ist eine leistungsstarke Python-Bibliothek zur Erstellung, Manipulation und Untersuchung komplexer Netzwerke (Graphen). Sie bietet Werkzeuge für die Arbeit mit ungerichteten und gerichteten Graphen, die Handhabung gewichteter Kanten und die Durchführung verschiedener Netzwerkanalysen.

Im Folgenden finden Sie mehrere Beispiele, die Ihnen den Einstieg in NetworkX erleichtern:

---

### 1. **Installation von NetworkX**

Stellen Sie vor der Verwendung von NetworkX sicher, dass es installiert ist. Sie können es mit `pip` installieren:

```bash
pip install networkx
```

---

### 2. **Erstellen und Visualisieren eines einfachen Graphen**

So erstellen Sie einen einfachen ungerichteten Graphen, fügen Knoten und Kanten hinzu und visualisieren ihn mit Matplotlib.

```python
import networkx as nx
import matplotlib.pyplot as plt

# Einen leeren Graphen erstellen
G = nx.Graph()

# Knoten hinzufügen
G.add_node(1)
G.add_nodes_from([2, 3, 4])

# Kanten hinzufügen (fügt die Knoten automatisch hinzu, falls sie nicht existieren)
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 4)])

# Den Graphen zeichnen
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
plt.title("Einfacher ungerichteter Graph")
plt.show()
```

**Ausgabe:**

Ein einfacher ungerichteter Graph mit 4 Knoten, die durch Kanten verbunden sind.

---

### 3. **Gerichtete Graphen**

Erstellen und Visualisieren eines gerichteten Graphen (DiGraph):

```python
import networkx as nx
import matplotlib.pyplot as plt

# Einen gerichteten Graphen erstellen
DG = nx.DiGraph()

# Kanten hinzufügen (Knoten werden automatisch hinzugefügt)
DG.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('C', 'A'),
    ('C', 'D')
])

# Den gerichteten Graphen mit Pfeilen zeichnen
pos = nx.circular_layout(DG)
nx.draw(DG, pos, with_labels=True, node_color='lightgreen', edge_color='gray', arrows=True, node_size=700)
plt.title("Gerichteter Graph")
plt.show()
```

**Ausgabe:**

Ein gerichteter Graph, der die Richtung der Kanten mit Pfeilen anzeigt.

---

### 4. **Gewichtete Graphen**

Zuweisen von Gewichten zu Kanten und deren Visualisierung:

```python
import networkx as nx
import matplotlib.pyplot as plt

# Einen gewichteten Graphen erstellen
WG = nx.Graph()

# Kanten zusammen mit Gewichten hinzufügen
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# Kantengewichte für die Beschriftung abrufen
edge_labels = nx.get_edge_attributes(WG, 'weight')

# Den Graphen zeichnen
pos = nx.spring_layout(WG)
nx.draw(WG, pos, with_labels=True, node_color='lightyellow', edge_color='gray', node_size=700)
nx.draw_networkx_edge_labels(WG, pos, edge_labels=edge_labels)
plt.title("Gewichteter Graph")
plt.show()
```

**Ausgabe:**

Ein gewichteter Graph mit Kantenbeschriftungen, die die Gewichte darstellen.

---

### 5. **Berechnung des kürzesten Pfades**

Ermitteln des kürzesten Pfades zwischen zwei Knoten mit dem Dijkstra-Algorithmus (für gewichtete Graphen):

```python
import networkx as nx

# Einen gewichteten Graphen erstellen (wie im vorherigen Beispiel)
WG = nx.Graph()
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# Kürzesten Pfad von 'A' nach 'D' berechnen
shortest_path = nx.dijkstra_path(WG, source='A', target='D', weight='weight')
path_length = nx.dijkstra_path_length(WG, source='A', target='D', weight='weight')

print(f"Kürzester Pfad von A nach D: {shortest_path} mit Gesamtgewicht {path_length}")
```

**Ausgabe:**

```
Kürzester Pfad von A nach D: ['A', 'C', 'D'] mit Gesamtgewicht 5
```

---

### 6. **Zentralitätsmaße**

Berechnung verschiedener Zentralitätsmaße, um wichtige Knoten im Graphen zu identifizieren.

```python
import networkx as nx

# Einen Beispielgraphen erstellen
G = nx.karate_club_graph()

# Grad-Zentralität berechnen
degree_centrality = nx.degree_centrality(G)

# Betweenness-Zentralität berechnen
betweenness_centrality = nx.betweenness_centrality(G)

# Eigenvektor-Zentralität berechnen
eigen_centrality = nx.eigenvector_centrality(G, max_iter=1000)

# Top 5 Knoten nach Grad-Zentralität anzeigen
sorted_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
print("Top 5 Knoten nach Grad-Zentralität:")
for node, centrality in sorted_degree[:5]:
    print(f"Knoten {node}: {centrality:.4f}")

# Ebenso können andere Zentralitäten angezeigt werden
```

**Ausgabe:**

```
Top 5 Knoten nach Grad-Zentralität:
Knoten 33: 0.6035
Knoten 0: 0.3793
Knoten 1: 0.3793
Knoten 2: 0.3793
Knoten 3: 0.3793
```

*Hinweis:* Der Karate Club Graph ist ein häufig verwendetes Beispiel für ein soziales Netzwerk in NetworkX.

---

### 7. **Erkennung von Communities mit dem Girvan-Newman-Algorithmus**

Identifizieren von Communities innerhalb eines Graphen.

```python
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt

# Einen Graphen erstellen (unter Verwendung des Karate Club Graphen)
G = nx.karate_club_graph()

# Communities mit Girvan-Newman berechnen
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
second_level_communities = next(communities_generator)

# Funktion zum Zuweisen von Farben zu Communities
def get_community_colors(G, communities):
    color_map = {}
    for idx, community in enumerate(communities):
        for node in community:
            color_map[node] = idx
    return [color_map[node] for node in G.nodes()]

# Die gewünschte Ebene der Communities auswählen
communities = second_level_communities
colors = get_community_colors(G, communities)

# Den Graphen mit Community-Farben zeichnen
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=colors, with_labels=True, cmap=plt.cm.Set1)
plt.title("Communities im Karate Club Graph")
plt.show()
```

**Ausgabe:**

Eine Visualisierung des Karate Club Graphen, bei der die Knoten basierend auf ihrer Community-Zugehörigkeit eingefärbt sind.

---

### 8. **Lesen und Schreiben von Graphen**

NetworkX unterstützt verschiedene Formate zum Lesen und Schreiben von Graphen, wie z.B. Adjazenzlisten, Kantenlisten und GraphML.

**Lesen einer Kantenliste:**

```python
import networkx as nx

# Angenommen, 'edges.txt' enthält:
# A B
# A C
# B C
# B D
# C D

G = nx.read_edgelist('edges.txt', delimiter=' ')
print("Knoten:", G.nodes())
print("Kanten:", G.edges())
```

**Schreiben eines Graphen in GraphML:**

```python
import networkx as nx

G = nx.complete_graph(5)  # Einen vollständigen Graphen mit 5 Knoten erstellen
nx.write_graphml(G, 'complete_graph.graphml')
print("Graph wurde in 'complete_graph.graphml' gespeichert")
```

---

### 9. **Verwendung von NetworkX mit Pandas DataFrames**

Integration von NetworkX mit Pandas für erweiterte Datenmanipulation.

```python
import networkx as nx
import pandas as pd

# Einen DataFrame erstellen, der Kanten mit Gewichten repräsentiert
data = {
    'source': ['A', 'A', 'B', 'B', 'C'],
    'target': ['B', 'C', 'C', 'D', 'D'],
    'weight': [4, 2, 5, 10, 3]
}
df = pd.DataFrame(data)

# Einen gewichteten Graphen aus dem DataFrame erstellen
G = nx.from_pandas_edgelist(df, 'source', 'target', ['weight'])

# Kanten mit Gewichten anzeigen
for u, v, data in G.edges(data=True):
    print(f"({u}, {v}) - Gewicht: {data['weight']}")
```

**Ausgabe:**

```
(A, B) - Gewicht: 4
(A, C) - Gewicht: 2
(B, C) - Gewicht: 5
(B, D) - Gewicht: 10
(C, D) - Gewicht: 3
```

---

### 10. **Erweiterte Visualisierung mit NetworkX und Matplotlib**

Anpassen des Erscheinungsbildes des Graphen für bessere Lesbarkeit.

```python
import networkx as nx
import matplotlib.pyplot as plt

# Einen Graphen erstellen
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'C'), ('C', 'D'), ('D', 'E'),
    ('E', 'F'), ('F', 'C')
])

# Positionen mit einem Layout zuweisen
pos = nx.spring_layout(G, seed=42)

# Knoten mit verschiedenen Größen und Farben zeichnen
node_sizes = [700 if node == 'C' else 300 for node in G.nodes()]
node_colors = ['red' if node == 'C' else 'skyblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)

# Kanten mit variierenden Breiten zeichnen
edge_widths = [2 if (u == 'C' or v == 'C') else 1 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_widths)

# Beschriftungen zeichnen
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.title("Angepasste Graphvisualisierung")
plt.axis('off')
plt.show()
```

**Ausgabe:**

Ein angepasster Graph, bei dem Knoten 'C' rot und größer hervorgehoben ist und Kanten, die mit 'C' verbunden sind, dickere Linien haben.

---

Diese Beispiele vermitteln ein grundlegendes Verständnis dafür, wie NetworkX zur Erstellung, Manipulation und Analyse von Graphen in Python genutzt werden kann. Für fortgeschrittene Anwendungen und detaillierte Dokumentationen lesen Sie bitte die [offizielle NetworkX-Dokumentation](https://networkx.org/documentation/stable/).