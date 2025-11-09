---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Structures de Données Efficaces pour les Requêtes par Intervalle
translated: true
type: note
---

### Arbres de Segments et Arbres de Fenwick : Aperçu

Les Arbres de Segments et les Arbres de Fenwick (aussi appelés Binary Indexed Trees) sont deux structures de données efficaces utilisées en programmation compétitive et dans les algorithmes pour gérer les requêtes de plage et les mises à jour sur des tableaux. Ils permettent des opérations comme les requêtes de somme sur une plage ou les mises à jour ponctuelles en temps logarithmique, ce qui est beaucoup plus rapide que les approches naïves en O(n) pour les grands jeux de données.

#### Arbres de Segments
Un **Arbre de Segments** est une structure basée sur un arbre binaire qui représente un tableau en le divisant en segments (intervalles). Chaque nœud de l'arbre correspond à une plage du tableau :
- Les nœuds feuilles représentent des éléments individuels.
- Les nœuds parents représentent l'union des plages de leurs enfants (par exemple, la somme, le min, le max des sous-plages).
- L'arbre est construit récursivement, avec une hauteur typique de O(log n) pour un tableau de taille n.

**Opérations Clés :**
- **Construction :** Temps O(n) pour construire l'arbre.
- **Mise à jour :** Modifier un seul élément et propager les changements vers le haut de l'arbre en O(log n).
- **Requête :** Calculer un agrégat (par exemple, la somme) sur une plage en parcourant les nœuds pertinents en O(log n).

**Cas d'Usage :** Requêtes de somme/min/max sur une plage, comptage de fréquence, ou toute opération associative. Il est plus flexible mais utilise un espace O(4n).

**Exemple Simple (Somme de Plage) :**
Imaginez un tableau [1, 3, 5, 7]. L'arbre de segments pourrait ressembler à :
- Racine : somme de [1-7] = 16
- Enfant gauche : somme de [1-3] = 4
- Enfant droit : somme de [5-7] = 12
- Et ainsi de suite, jusqu'aux feuilles.

#### Arbres de Fenwick
Un **Arbre de Fenwick** (introduit par Peter Fenwick en 1994) est une structure basée sur un tableau, plus compacte, pour les sommes de préfixe et les opérations similaires. Il utilise des opérations bit à bit pour indexer les éléments efficacement, en suivant les sommes cumulées de manière astucieuse :
- Chaque index stocke la somme d'une plage se terminant à cet index.
- Les mises à jour et les requêtes utilisent la manipulation des bits de poids faible (par exemple, `index & -index` pour trouver le bit le moins significatif).

**Opérations Clés :**
- **Construction :** O(n log n) ou optimisé en O(n).
- **Mise à jour :** Ajouter/soustraire une valeur à un index en O(log n).
- **Requête :** Obtenir la somme de préfixe jusqu'à un index en O(log n) ; somme de plage via les différences de préfixe.

**Cas d'Usage :** Similaires aux arbres de segments mais optimisés pour les sommes de préfixe 1D, les statistiques d'ordre, ou les comptes d'inversion. Il utilise un espace O(n), ce qui le rend plus léger.

**Exemple Simple (Somme de Plage) :**
Pour le tableau [1, 3, 5, 7], le tableau de Fenwick pourrait être [1, 4, 5, 16] (ajustements cumulatifs). Pour requêter la somme[1-3] : prefix(3) - prefix(0) = 9.

#### Comparaison

| Aspect          | Arbre de Segments              | Arbre de Fenwick               |
|-----------------|--------------------------------|--------------------------------|
| **Espace**      | O(4n)                          | O(n)                           |
| **Temps de Construction** | O(n)                       | O(n log n)                     |
| **Flexibilité** | Prend en charge tout agrégat de plage | Idéal pour les sommes de préfixe/mises à jour |
| **Complexité**  | Code légèrement plus complexe  | Implémentation plus simple     |

Les deux sont des incontournables en algorithmes (par exemple, sur LeetCode ou Codeforces). Si vous les implémentez, commencez par Fenwick pour sa simplicité !

Pour aller plus loin :  
[Segment Tree Tutorial - GeeksforGeeks](https://www.geeksforgeeks.org/segment-tree-data-structure/)  
[Fenwick Tree Explained - CP-Algorithms](https://cp-algorithms.com/data_structures/fenwick.html)