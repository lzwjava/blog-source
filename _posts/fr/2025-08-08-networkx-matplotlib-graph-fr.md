---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Tutoriel sur les Graphes avec NetworkX et Matplotlib
translated: true
type: note
---

### Installation des bibliothèques
Pour utiliser NetworkX et Matplotlib pour dessiner des diagrammes, installez-les si nécessaire :
- NetworkX : Gère la création et la manipulation de graphes.
- Matplotlib : Fournit des capacités de traçage.

Installation via pip :
```bash
pip install networkx matplotlib
```

Pour un rendu plus rapide, Matplotlib recommande d'installer NumPy (`pip install numpy`).

### Configuration de base et exemple
1. **Importer les bibliothèques** :  
   ```python
   import networkx as nx
   import matplotlib.pyplot as plt
   ```

2. **Créer un graphe** :  
   Utilisez NetworkX pour construire un graphe non orienté simple (vous pouvez le personnaliser avec des graphes orientés, des arêtes pondérées, etc.) :
   ```python
   G = nx.Graph()  # Créer un graphe vide
   G.add_nodes_from([1, 2, 3, 4, 5])  # Ajouter des nœuds (ex. : 5 nœuds)
   G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])  # Ajouter des arêtes (connexions)
   ```

3. **Dessiner et afficher le diagramme** :  
   Utilisez le backend de Matplotlib pour la visualisation :
   ```python
   nx.draw(G, with_labels=True)  # Dessiner le graphe avec les étiquettes des nœuds
   plt.show()  # Afficher le graphique
   ```

Cela produit une disposition circulaire de base du graphe (un cycle avec 5 nœuds).

### Personnalisations avancées
- **Dispositions** : Contrôlez les positions des nœuds (ex. : aléatoire, disposition spring) :
  ```python
  pos = nx.spring_layout(G)  # Disposition force-directed pour des réseaux réalistes
  nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray')
  plt.title("Diagramme de réseau")
  plt.show()
  ```
- **Styles des nœuds et des arêtes** : Personnalisez l'apparence :
  ```python
  nx.draw(G, pos=pos, node_size=500, node_color='red', edge_width=2, font_size=10)
  ```
- **Graphes orientés** : Pour les relations hiérarchiques, utilisez `nx.DiGraph`.
  ```python
  DG = nx.DiGraph()
  DG.add_edges_from([('A', 'B'), ('B', 'C')])
  nx.draw(DG, with_labels=True, arrows=True)
  plt.show()
  ```
- **Sauvegarde du diagramme** : Exportez vers un fichier au lieu d'afficher :
  ```python
  plt.savefig('diagram.png')
  ```

### Conseils et ressources
- Documentation NetworkX (networkx.org) pour les types de graphes comme les arbres ou les grilles.
- Documentation Matplotlib (matplotlib.org) pour l'intégration dans des interfaces graphiques ou des sous-graphiques.
- Pour les grands graphes (>100 nœuds), utilisez `nx.draw_networkx` ou des outils externes comme Graphviz pour de meilleures performances.
- Expérimentez dans un notebook Jupyter pour un traçage interactif. Si des problèmes surviennent, les erreurs courantes proviennent de backends manquants (installez via `pip install pyqt5` ou similaire pour les fenêtres interactives).