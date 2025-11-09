---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comprendre l'algorithme de plus court chemin de Dijkstra
translated: true
type: note
---

### Comprendre l'algorithme du plus court chemin de Dijkstra

L'algorithme de Dijkstra est une méthode fondamentale pour trouver le plus court chemin entre les nœuds d'un graphe où les arêtes ont des poids non négatifs (comme des distances ou des coûts). Il porte le nom d'Edsger W. Dijkstra et est largement utilisé dans la navigation GPS, le routage réseau, et plus encore. L'idée clé : il explore le graphe de manière gloutonne, choisissant toujours le nœud non visité le plus proche et mettant à jour les chemins à partir de là, comme un effet de propagation à partir du point de départ.

#### Prérequis Rapides
- **Bases des Graphes** : Imaginez un graphe comme une carte de villes (nœuds) reliées par des routes (arêtes) avec des longueurs (poids). Nous supposons que les poids sont positifs—pas de distances négatives !
- **Orientation** : Fonctionne pour les graphes orientés et non orientés, mais les exemples ici utilisent des graphes non orientés pour plus de simplicité.
- **Plus Court Chemin** : Le chemin avec le poids total minimal de la source à la cible.

Si les graphes sont nouveaux pour vous, imaginez un réseau social : des personnes (nœuds), des amitiés avec des scores de "force" (poids).

#### Comment ça marche : Intuition étape par étape
Dijkstra construit le plus court chemin de manière incrémentielle, en utilisant une **file de priorité** (comme une liste de tâches triée par urgence—ici, par la distance connue la plus courte actuelle). Il ne revisite jamais les nœuds une fois fixés, ce qui le rend efficace.

1. **Initialisation** :
   - Choisissez un nœud de départ (source). Fixez sa distance à 0.
   - Fixez la distance de tous les autres nœuds à l'infini (∞).
   - Suivez le "chemin vers" chaque nœud (initialement aucun).

2. **Tant qu'il y a des nœuds non visités** :
   - Choisissez le nœud non visité avec la distance actuelle la plus petite (depuis la file de priorité).
   - "Fixez-le" : Marquez-le comme visité. Cette distance est finale—grâce aux poids non négatifs, aucun chemin plus court ne peut être trouvé plus tard.
   - Pour chaque voisin de ce nœud :
     - Calculez la nouvelle distance potentielle : (distance du nœud fixé) + (poids de l'arête vers le voisin).
     - Si cela est plus court que la distance actuelle du voisin, mettez-la à jour et notez que le chemin passe par le nœud fixé.
   - Répétez jusqu'à ce que tous les nœuds soient visités ou que la cible soit fixée.

L'algorithme s'arrête plus tôt si vous ne vous intéressez qu'à un seul nœud cible.

**Pourquoi ça marche** : C'est comme un parcours en largeur mais pondéré—étendant toujours la frontière la moins coûteuse en premier. La preuve repose sur le fait qu'une fois qu'un nœud est fixé, sa distance ne peut pas s'améliorer (propriété de choix glouton).

#### Exemple Simple
Imaginez un graphe avec 4 villes : A (départ), B, C, D. Arêtes et poids :

- A → B : 4
- A → C : 2
- B → C : 1
- B → D : 5
- C → D : 8

Visualisation ASCII :
```
   4
A ----- B
 \     / \
  2   1   5
  \   /     |
   C ------- D
     8
```

Exécution de Dijkstra depuis A :

- **Départ** : dist[A]=0, dist[B]=∞, dist[C]=∞, dist[D]=∞. File : A.
- **Fixer A** (dist=0).
  - Mettre à jour B : 0+4=4
  - Mettre à jour C : 0+2=2
  - File : C(2), B(4)
- **Fixer C** (dist=2).
  - Mettre à jour D : 2+8=10
  - File : B(4), D(10)
- **Fixer B** (dist=4).
  - Mettre à jour C : 4+1=5 (mais 2<5, pas de changement)
  - Mettre à jour D : 4+5=9 (9<10, mise à jour à 9)
  - File : D(9)
- **Fixer D** (dist=9).

Distances finales : A=0, B=4, C=2, D=9.  
Chemin vers D : A → B → D (total 9, plus court que A → C → D=10).

Vous pouvez retracer les chemins en utilisant un tableau de "nœud précédent".

#### Pseudocode
Voici un aperçu d'implémentation simple (de type Python) :

```python
import heapq  # Pour la file de priorité

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    pq = [(0, start)]  # (distance, nœud)
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        if current_dist > distances[current]:
            continue  # Entrée obsolète
        
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruire le chemin vers la cible (par exemple, 'D')
    path = []
    node = 'D'
    while node is not None:
        path.append(node)
        node = previous[node]
    return path[::-1], distances['D']  # Inverser pour obtenir du début à la fin
```

- `graph` : Dictionnaire de dictionnaires, par exemple, `{'A': {'B':4, 'C':2}, ...}`
- Complexité Temporelle : O((V+E) log V) avec un tas binaire (V=sommets, E=arêtes). Excellent pour les graphes peu denses.

#### Conseils pour Approfondir la Compréhension
- **Visualisez** : Dessinez votre graphe sur papier, simulez les étapes avec un tableau des distances/visites.
- **Pièges Courants** : Échoue avec des poids négatifs (utilisez Bellman-Ford à la place). Suppose un graphe connexe.
- **Pratiquez** : Essayez sur de petits graphes, puis codez-le pour un jeu de données de carte.
- **Variantes** : A* ajoute des heuristiques pour des recherches plus rapides (par exemple, dans les jeux).

Cela devrait faire tilt—commencez par l'exemple, exécutez-le mentalement plusieurs fois !

[Wikipedia : Algorithme de Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)  
[GeeksforGeeks : Explication Visuelle](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)