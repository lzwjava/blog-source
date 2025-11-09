---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Décomposition par racine carrée pour les requêtes d'intervalle
translated: true
type: note
---

### Décomposition par Racine Carrée

La décomposition par racine carrée (souvent abrégée en √-décomposition) est une technique en informatique et en programmation compétitive utilisée pour optimiser les requêtes et les mises à jour sur des plages de grands tableaux ou structures de données. Elle est particulièrement utile lorsque vous devez répondre efficacement à des requêtes comme "trouver la somme/max/min des éléments dans un sous-tableau", sans avoir recours à des structures plus complexes comme les arbres de segments ou les arbres de Fenwick, qui peuvent être plus difficiles à implémenter.

#### Pourquoi l'utiliser ?
- **Compromis sur la Complexité Temporelle** : Pour un tableau de taille \\( n \\), les requêtes naïves sur une plage prennent \\( O(n) \\) temps par requête. La décomposition par racine carrée réduit cela à \\( O(\sqrt{n}) \\) par requête et mise à jour, ce qui est un bon équilibre pour de nombreux problèmes où \\( n \\) peut aller jusqu'à \\( 10^5 \\) ou \\( 10^6 \\).
- **Simplicité** : Elle est plus facile à coder et à déboguer que les structures de données avancées.
- **Applications** : Courante dans les problèmes impliquant des requêtes de somme sur une plage, des requêtes de minimum sur une plage (RMQ), ou du comptage de fréquence dans des fenêtres glissantes.

#### Comment ça marche
1. **Diviser en Blocs** : Divisez le tableau en blocs de taille \\( \sqrt{n} \\) (arrondie à l'inférieur). Si \\( n = 100 \\), la taille de bloc \\( b = 10 \\), vous obtenez donc 10 blocs.
   - Chaque bloc stocke une information précalculée (par exemple, la somme des éléments dans ce bloc pour les requêtes de somme).
   
2. **Interroger une Plage [L, R]** :
   - **Blocs Complets** : Pour les blocs entièrement contenus dans [L, R], récupérez simplement la valeur précalculée en \\( O(1) \\) par bloc. Au maximum \\( O(\sqrt{n}) \\) blocs complets.
   - **Blocs Partiels** : Pour les bords (blocs partiels gauche et droit), parcourez manuellement les éléments individuels, ce qui prend un total de \\( O(\sqrt{n}) \\) temps (puisque chaque bloc partiel a une taille de \\( \sqrt{n} \\)).
   - Total : \\( O(\sqrt{n}) \\).

3. **Mises à Jour** : Lors de la mise à jour d'un élément, recalculez la valeur précalculée pour son bloc en \\( O(\sqrt{n}) \\) temps (en refaisant la somme du bloc).

#### Exemple Simple : Requête de Somme sur une Plage
Supposons que nous ayons un tableau `A = [1, 3, 2, 4, 5]` et \\( n=5 \\), donc la taille de bloc \\( b = \sqrt{5} \approx 2 \\). Blocs :
- Bloc 0 : [1, 3] → somme = 4
- Bloc 1 : [2, 4] → somme = 6
- Bloc 2 : [5] → somme = 5 (le dernier bloc peut être plus petit)

Requête de somme de l'index 1 à 4 (base 0 : éléments 3,2,4,5) :
- Partiel gauche : Index 1 (dans le Bloc 0) → ajouter 3
- Bloc Complet 1 : Ajouter 6
- Partiel droit : Index 4 (dans le Bloc 2) → ajouter 5
- Total : 3 + 6 + 5 = 14

Pour l'implémenter en code (pseudocode Python) :
```python
import math

class SqrtDecomp:
    def __init__(self, arr):
        self.n = len(arr)
        self.b = int(math.sqrt(self.n))
        self.arr = arr[:]
        self.block_sums = [0] * ((self.n + self.b - 1) // self.b)
        self._build()
    
    def _build(self):
        for i in range(self.n):
            block_id = i // self.b
            self.block_sums[block_id] += self.arr[i]
    
    def update(self, idx, val):
        diff = val - self.arr[idx]
        self.arr[idx] = val
        block_id = idx // self.b
        self.block_sums[block_id] += diff
    
    def query(self, left, right):
        res = 0
        l_block, r_block = left // self.b, right // self.b
        
        if l_block == r_block:
            for i in range(left, right + 1):
                res += self.arr[i]
        else:
            # Partiel gauche
            for i in range(left, (l_block + 1) * self.b):
                res += self.arr[i]
            # Blocs complets
            for blk in range(l_block + 1, r_block):
                res += self.block_sums[blk]
            # Partiel droit
            for i in range(r_block * self.b, right + 1):
                res += self.arr[i]
        return res
```

Ceci est une version basique—adaptez-la pour min/max en stockant min/max par bloc au lieu des sommes.

Pour approfondir, consultez des ressources comme [GeeksforGeeks sur la Décomposition par Racine Carrée](https://www.geeksforgeeks.org/sqrt-decomposition-algorithm-square-root-decomposition-technique-set-1-introduction/) ou [CP-Algorithms](https://cp-algorithms.com/data_structures/sqrt_decomposition.html).