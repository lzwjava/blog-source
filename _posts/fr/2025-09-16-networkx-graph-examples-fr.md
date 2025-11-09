---
audio: false
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Exemples de Création et d'Analyse de Graphes avec NetworkX
translated: true
type: note
---

NetworkX est une bibliothèque Python puissante pour créer, analyser et visualiser des réseaux complexes. Voici plusieurs exemples démontrant ses capacités :

## 1. Création et Visualisation de Graphe de Base

```python
import networkx as nx
import matplotlib.pyplot as plt

# Créer un graphe vide
G = nx.Graph()

# Ajouter des nœuds
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from(range(4, 7))

# Ajouter des arêtes
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4), (4, 5), (5, 6), (6, 1)])

# Visualiser le graphe
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
```

## 2. Exemple de Graphe Orienté

```python
# Créer un graphe orienté
D = nx.DiGraph()

# Ajouter des arêtes (ajoute automatiquement les nœuds)
D.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Dessiner avec différentes couleurs de nœuds
pos = nx.spring_layout(D)
nx.draw(D, pos, with_labels=True, node_color='lightgreen',
        edge_color='red', node_size=1000, arrowsize=20)
plt.show()
```

## 3. Exemple d'Analyse de Graphe

```python
# Créer un graphe
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# Propriétés de base du graphe
print("Nombre de nœuds :", G.number_of_nodes())
print("Nombre d'arêtes :", G.number_of_edges())
print("Nœuds :", G.nodes())
print("Arêtes :", G.edges())
print("Degré du nœud 2 :", G.degree(2))
print("Voisins du nœud 2 :", list(G.neighbors(2)))
print("Le graphe est-il connecté ?", nx.is_connected(G))
print("Plus court chemin de 1 à 5 :", nx.shortest_path(G, 1, 5))
```

## 4. Exemple de Graphe Pondéré

```python
# Créer un graphe pondéré
G = nx.Graph()

# Ajouter des arêtes pondérées
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=1)
G.add_edge('C', 'D', weight=5)

# Dessiner avec les étiquettes d'arêtes montrant les poids
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightcoral')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
```

## 5. Exemple d'Analyse de Réseau Social

```python
# Créer un graphe de réseau social
social = nx.Graph()

# Ajouter des personnes et leurs connexions
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
social.add_nodes_from(people)

connections = [('Alice', 'Bob'), ('Alice', 'Charlie'),
               ('Bob', 'Charlie'), ('Bob', 'David'),
               ('Charlie', 'Eve'), ('David', 'Eve')]
social.add_edges_from(connections)

# Calculer les mesures de centralité
degree_centrality = nx.degree_centrality(social)
betweenness_centrality = nx.betweenness_centrality(social)
closeness_centrality = nx.closeness_centrality(social)

print("Centralité de degré :", degree_centrality)
print("Centralité d'intermédiarité :", betweenness_centrality)
print("Centralité de proximité :", closeness_centrality)

# Visualiser
nx.draw(social, with_labels=True, node_color='lightgreen', node_size=2000)
plt.show()
```

## 6. Génération de Graphe Aléatoire

```python
# Créer un graphe aléatoire d'Erdős–Rényi
random_graph = nx.erdos_renyi_graph(10, 0.3)  # 10 nœuds, probabilité d'arête de 30%

# Visualiser
nx.draw(random_graph, with_labels=True, node_color='skyblue')
plt.show()
```

## 7. Exemple d'Algorithmes de Graphe

```python
# Créer un graphe
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

# Trouver tous les chemins simples entre deux nœuds
print("Tous les chemins de 1 à 6 :", list(nx.all_simple_paths(G, 1, 6)))

# Arbre couvrant minimal
T = nx.minimum_spanning_tree(G)
print("Arêtes dans l'ACM :", T.edges())

# Détection de communautés (nécessite le package python-louvain)
# pip install python-louvain
try:
    import community as community_louvain
    partition = community_louvain.best_partition(G)
    print("Partition des communautés :", partition)
except ImportError:
    print("Installez python-louvain pour la détection de communautés")
```

Ces exemples couvrent la création de base de graphes, la visualisation, l'analyse et quelques algorithmes courants. NetworkX fournit de nombreuses autres fonctionnalités pour travailler avec des réseaux complexes.