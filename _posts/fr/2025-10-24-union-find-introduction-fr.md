---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Introduction à l'algorithme Union-Find
translated: true
type: note
---

### Introduction à l'algorithme Union-Find (Union de ensembles disjoints)

L'algorithme **Union-Find** (aussi appelé **Union de ensembles disjoints** ou **DSU**) est une structure de données et un ensemble d'opérations utilisés pour gérer une collection d'ensembles disjoints (groupes d'éléments qui ne se chevauchent pas). Il est efficace pour les problèmes impliquant le regroupement, la fusion ou la vérification de la connectivité, comme dans les algorithmes de graphes ou le clustering.

Opérations clés :
- **Find** : Détermine à quel ensemble un élément appartient (souvent en trouvant la "racine" ou le représentant de l'ensemble).
- **Union** : Fusionne deux ensembles en un seul.

L'algorithme est remarquable grâce à des optimisations comme la **compression de chemin** (aplatir la structure arborescente lors des opérations find) et l'**union par rang/taille** (fusionner les arbres plus petits dans les plus grands pour garder la structure équilibrée). Cela rend le temps quasi O(1) amorti par opération—très rapide pour les grands jeux de données.

#### Structure de données de base
- Un tableau `p[]` (tableau parent) : `p[i]` pointe vers le parent de l'élément `i`. Initialement, chaque élément est son propre parent (`p[i] = i`).
- Optionnel : Un tableau `rank[]` pour l'union par rang afin d'équilibrer les fusions.

#### L'opération Find (avec compression de chemin)
La fonction `find` remonte d'un élément jusqu'à sa racine. La ligne que vous avez mentionnée—`if (p[i] != -1) i = p[i]`—est une étape récursive ou itérative dans ce processus. Elle suit les pointeurs parent jusqu'à atteindre la racine (où `p[root] == root` ou `p[root] == -1` pour une sentinelle).

Voici une implémentation itérative simple en pseudocode :

```
function find(i):
    if p[i] != -1:  # Pas la racine (ou sentinelle)
        i = p[i]     # Aller au parent (c'est votre ligne !)
        return find(i)  # Récursif : continuer jusqu'à la racine
    else:
        return i     # Racine trouvée
```

**Avec compression de chemin complète** (pour optimiser les futures recherches), nous aplatissons le chemin en définissant tous les nœuds directement sur la racine :

```
function find(i):
    if p[i] != i:  # Pas la racine
        p[i] = find(p[i])  # Compresser : définir le parent sur la racine trouvée
    return p[i]
```

- `-1` est souvent utilisé comme sentinelle pour les racines (au lieu de `i` pour l'auto-parenté), surtout dans certaines implémentations pour distinguer les nœuds non initialisés ou invalides.
- Sans compression, des recherches répétées peuvent rendre la structure une longue chaîne (O(n) pire cas). La compression la rend presque plate.

#### L'opération Union
Pour fusionner les ensembles de `x` et `y` :
1. Trouver les racines : `rootX = find(x)`, `rootY = find(y)`.
2. Si `rootX != rootY`, lier l'une à l'autre (par exemple, par rang : attacher le rang plus petit au plus grand).

Pseudocode :
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
            rank[rootX] += 1  # Augmenter le rang pour le nouveau parent
```

#### Comment utiliser l'algorithme
Union-Find est idéal pour les problèmes de connectivité dynamique. Voici un guide étape par étape avec des exemples :

1. **Initialisation** :
   - Créer `p[]` de taille `n` (nombre d'éléments) : `for i in 0 to n-1: p[i] = -1` (ou `i` pour l'auto-parent).
   - Optionnel : `rank[]` tous initialisés à 0 ou 1.

2. **Flux d'utilisation de base** :
   - Pour vérifier si deux éléments sont dans le même ensemble : `if find(a) == find(b)`.
   - Pour fusionner : `union(a, b)`.
   - Traiter les requêtes/fusions dans n'importe quel ordre—c'est dynamique !

3. **Exemple : Détection de composantes connexes dans un graphe**
   Imaginez un graphe avec 5 nœuds (0-4) et des arêtes comme (0-1), (1-2), (3-4).
   ```
   // Init
   p = [-1, -1, -1, -1, -1]
   rank = [0, 0, 0, 0, 0]

   // Union des arêtes
   union(0, 1)  // Fusionne 0 et 1, disons p[0]=-1, p[1]=0
   union(1, 2)  // Fusionne 2 dans {0,1}, p[2]=0
   union(3, 4)  // Fusionne {3,4}, disons p[3]=-1, p[4]=3

   // Requête : 0 et 2 sont-ils connectés ? find(0)=0, find(2)=0 → Oui
   // 2 et 3 sont-ils connectés ? find(2)=0, find(3)=-1 → Non
   ```

4. **Applications réelles** :
   - **Algorithme de Kruskal pour l'arbre couvrant minimal** : Trier les arêtes par poids, unir les arêtes qui ne forment pas de cycle (ignorer si `find(u) == find(v)`).
   - **Amis sur un réseau social** : Unir les amis, trouver les connexions mutuelles.
   - **Segmentation d'image** : Unir les pixels adjacents de couleur similaire.
   - **Détection de cycle dans les graphes non orientés** : Unir les extrémités ; si déjà dans le même ensemble, un cycle existe.

#### Implémentation Python simple
```python
class UnionFind:
    def __init__(self, n):
        self.p = [-1] * n
        self.rank = [0] * n
    
    def find(self, i):
        if self.p[i] != -1 and self.p[i] != i:  # Gère la sentinelle + auto-parent
            self.p[i] = self.find(self.p[i])  # Compression de chemin
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

# Utilisation
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.find(0) == uf.find(2))  # True
```

Cela garde les choses efficaces—essayez avec un plus grand `n` pour voir la vitesse !

Pour plus de détails, consultez [GeeksforGeeks: Union-Find Algorithm](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank-and-path-compression/) ou [CP-Algorithms: DSU](https://cp-algorithms.com/data_structures/disjoint_set_union.html).