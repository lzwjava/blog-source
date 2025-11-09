---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/o1-mini
title: Présentation de la Bibliothèque de Graphes Python NetworkX
translated: true
type: note
---

NetworkX est une bibliothèque Python puissante pour la création, la manipulation et l'étude de réseaux complexes (graphes). Elle fournit des outils pour travailler avec des graphes non orientés et orientés, gérer des arêtes pondérées et effectuer diverses analyses de réseaux.

Voici plusieurs exemples pour vous aider à démarrer avec NetworkX :

---

### 1. **Installer NetworkX**

Avant d'utiliser NetworkX, assurez-vous qu'il est installé. Vous pouvez l'installer en utilisant `pip` :

```bash
pip install networkx
```

---

### 2. **Créer et visualiser un graphe simple**

Voici comment créer un graphe non orienté simple, ajouter des nœuds et des arêtes, et le visualiser en utilisant Matplotlib.

```python
import networkx as nx
import matplotlib.pyplot as plt

# Créer un Graph vide
G = nx.Graph()

# Ajouter des nœuds
G.add_node(1)
G.add_nodes_from([2, 3, 4])

# Ajouter des arêtes (ajoute automatiquement les nœuds s'ils n'existent pas)
G.add_edge(1, 2)
G.add_edges_from([(1, 3), (2, 4)])

# Dessiner le graphe
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
plt.title("Graphe non orienté simple")
plt.show()
```

**Sortie :**

Un graphe non orienté simple avec 4 nœuds connectés par des arêtes.

---

### 3. **Graphes orientés**

Création et visualisation d'un graphe orienté (DiGraph) :

```python
import networkx as nx
import matplotlib.pyplot as plt

# Créer un graphe orienté
DG = nx.DiGraph()

# Ajouter des arêtes (les nœuds sont ajoutés automatiquement)
DG.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('C', 'A'),
    ('C', 'D')
])

# Dessiner le graphe orienté avec des flèches
pos = nx.circular_layout(DG)
nx.draw(DG, pos, with_labels=True, node_color='lightgreen', edge_color='gray', arrows=True, node_size=700)
plt.title("Graphe orienté")
plt.show()
```

**Sortie :**

Un graphe orienté montrant la direction des arêtes avec des flèches.

---

### 4. **Graphes pondérés**

Attribution de poids aux arêtes et leur visualisation :

```python
import networkx as nx
import matplotlib.pyplot as plt

# Créer un graphe pondéré
WG = nx.Graph()

# Ajouter des arêtes avec leurs poids
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# Obtenir les poids des arêtes pour l'étiquetage
edge_labels = nx.get_edge_attributes(WG, 'weight')

# Dessiner le graphe
pos = nx.spring_layout(WG)
nx.draw(WG, pos, with_labels=True, node_color='lightyellow', edge_color='gray', node_size=700)
nx.draw_networkx_edge_labels(WG, pos, edge_labels=edge_labels)
plt.title("Graphe pondéré")
plt.show()
```

**Sortie :**

Un graphe pondéré avec des étiquettes sur les arêtes représentant les poids.

---

### 5. **Calcul du plus court chemin**

Trouver le plus court chemin entre deux nœuds en utilisant l'algorithme de Dijkstra (pour les graphes pondérés) :

```python
import networkx as nx

# Créer un graphe pondéré (comme dans l'exemple précédent)
WG = nx.Graph()
WG.add_edge('A', 'B', weight=4)
WG.add_edge('A', 'C', weight=2)
WG.add_edge('B', 'C', weight=5)
WG.add_edge('B', 'D', weight=10)
WG.add_edge('C', 'D', weight=3)

# Calculer le plus court chemin de 'A' à 'D'
shortest_path = nx.dijkstra_path(WG, source='A', target='D', weight='weight')
path_length = nx.dijkstra_path_length(WG, source='A', target='D', weight='weight')

print(f"Plus court chemin de A à D : {shortest_path} avec un poids total de {path_length}")
```

**Sortie :**

```
Plus court chemin de A à D : ['A', 'C', 'D'] avec un poids total de 5
```

---

### 6. **Mesures de centralité**

Calcul de diverses mesures de centralité pour identifier les nœuds importants dans le graphe.

```python
import networkx as nx

# Créer un graphe exemple
G = nx.karate_club_graph()

# Calculer la centralité de degré
degree_centrality = nx.degree_centrality(G)

# Calculer la centralité d'intermédiarité
betweenness_centrality = nx.betweenness_centrality(G)

# Calculer la centralité de vecteur propre
eigen_centrality = nx.eigenvector_centrality(G, max_iter=1000)

# Afficher les 5 premiers nœuds par centralité de degré
sorted_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
print("Top 5 des nœuds par Centralité de Degré :")
for node, centrality in sorted_degree[:5]:
    print(f"Nœud {node} : {centrality:.4f}")

# De même, vous pouvez afficher les autres centralités
```

**Sortie :**

```
Top 5 des nœuds par Centralité de Degré :
Nœud 33 : 0.6035
Nœud 0 : 0.3793
Nœud 1 : 0.3793
Nœud 2 : 0.3793
Nœud 3 : 0.3793
```

*Note :* Le graphe du Karate Club est un exemple de réseau social couramment utilisé dans NetworkX.

---

### 7. **Détection de communautés avec l'algorithme de Girvan-Newman**

Identification des communautés à l'intérieur d'un graphe.

```python
import networkx as nx
from networkx.algorithms import community
import matplotlib.pyplot as plt

# Créer un graphe (en utilisant le graphe du Karate Club)
G = nx.karate_club_graph()

# Calculer les communautés en utilisant Girvan-Newman
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
second_level_communities = next(communities_generator)

# Fonction pour assigner des couleurs aux communautés
def get_community_colors(G, communities):
    color_map = {}
    for idx, community in enumerate(communities):
        for node in community:
            color_map[node] = idx
    return [color_map[node] for node in G.nodes()]

# Choisir le niveau de communautés souhaité
communities = second_level_communities
colors = get_community_colors(G, communities)

# Dessiner le graphe avec les couleurs des communautés
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=colors, with_labels=True, cmap=plt.cm.Set1)
plt.title("Communautés dans le graphe du Karate Club")
plt.show()
```

**Sortie :**

Une visualisation du graphe du Karate Club avec les nœuds colorés en fonction de leur appartenance à une communauté.

---

### 8. **Lire et écrire des graphes**

NetworkX supporte divers formats pour lire et écrire des graphes, tels que les listes d'adjacence, les listes d'arêtes et GraphML.

**Lire une liste d'arêtes :**

```python
import networkx as nx

# Supposons que 'edges.txt' contient :
# A B
# A C
# B C
# B D
# C D

G = nx.read_edgelist('edges.txt', delimiter=' ')
print("Nœuds :", G.nodes())
print("Arêtes :", G.edges())
```

**Écrire un graphe en GraphML :**

```python
import networkx as nx

G = nx.complete_graph(5)  # Créer un graphe complet avec 5 nœuds
nx.write_graphml(G, 'complete_graph.graphml')
print("Graphe sauvegardé sous 'complete_graph.graphml'")
```

---

### 9. **Utiliser NetworkX avec les Pandas DataFrames**

Intégrer NetworkX avec Pandas pour des manipulations de données plus avancées.

```python
import networkx as nx
import pandas as pd

# Créer un DataFrame représentant des arêtes avec des poids
data = {
    'source': ['A', 'A', 'B', 'B', 'C'],
    'target': ['B', 'C', 'C', 'D', 'D'],
    'weight': [4, 2, 5, 10, 3]
}
df = pd.DataFrame(data)

# Créer un graphe pondéré à partir du DataFrame
G = nx.from_pandas_edgelist(df, 'source', 'target', ['weight'])

# Afficher les arêtes avec leurs poids
for u, v, data in G.edges(data=True):
    print(f"({u}, {v}) - poids : {data['weight']}")
```

**Sortie :**

```
(A, B) - poids : 4
(A, C) - poids : 2
(B, C) - poids : 5
(B, D) - poids : 10
(C, D) - poids : 3
```

---

### 10. **Visualisation avancée avec NetworkX et Matplotlib**

Personnaliser l'apparence du graphe pour une meilleure lisibilité.

```python
import networkx as nx
import matplotlib.pyplot as plt

# Créer un graphe
G = nx.Graph()
G.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'C'), ('C', 'D'), ('D', 'E'),
    ('E', 'F'), ('F', 'C')
])

# Assigner des positions en utilisant un layout
pos = nx.spring_layout(G, seed=42)

# Dessiner les nœuds avec différentes tailles et couleurs
node_sizes = [700 if node == 'C' else 300 for node in G.nodes()]
node_colors = ['red' if node == 'C' else 'skyblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)

# Dessiner les arêtes avec des largeurs variables
edge_widths = [2 if (u == 'C' or v == 'C') else 1 for u, v in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_widths)

# Dessiner les étiquettes
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.title("Visualisation de graphe personnalisée")
plt.axis('off')
plt.show()
```

**Sortie :**

Un graphe personnalisé où le nœud 'C' est mis en évidence en rouge avec une taille plus grande, et les arêtes connectées à 'C' ont des lignes plus épaisses.

---

Ces exemples fournissent une compréhension fondamentale de la façon d'utiliser NetworkX pour créer, manipuler et analyser des graphes en Python. Pour une utilisation plus avancée et une documentation détaillée, reportez-vous à la [documentation officielle de NetworkX](https://networkx.org/documentation/stable/).