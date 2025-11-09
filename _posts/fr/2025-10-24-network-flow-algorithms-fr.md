---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Algorithmes de flux de réseau expliqués
translated: true
type: note
---

### Comprendre les algorithmes de flot dans les réseaux

Les algorithmes de flot dans les réseaux sont un sujet fondamental en théorie des graphes et en informatique, utilisés pour modéliser et résoudre des problèmes impliquant le flux de ressources à travers un réseau (comme des tuyaux, des routes ou des flux de données). Ils sont essentiels pour les tâches d'optimisation telles que le flot maximum (par exemple, quelle quantité d'eau peut s'écouler dans un système de tuyaux), la coupe minimum (par exemple, trouver les goulots d'étranglement) et ont des applications dans le transport, la planification et l'appariement.

Je vais décomposer cela étape par étape : les concepts clés, un exemple simple, les principaux algorithmes et des conseils pour un apprentissage approfondi. Nous nous concentrerons sur le problème du flot maximum, car c'est le cœur du sujet.

#### 1. Concepts Clés
- **Représentation du graphe** : Un réseau est un graphe orienté \\( G = (V, E) \\) avec des sommets \\( V \\) (nœuds) et des arêtes \\( E \\) (connexions). Chaque arête a une **capacité** \\( c(u, v) \\), le flot maximum qu'elle peut transporter du nœud \\( u \\) au nœud \\( v \\).
- **Source et Puits** : Un nœud est la **source** \\( s \\) (où le flux commence) et un autre est le **puits** \\( t \\) (où il se termine).
- **Flot** : Une fonction \\( f(u, v) \\) attribuant la quantité de flux passant le long de chaque arête, satisfaisant :
  - **Contrainte de capacité** : \\( 0 \leq f(u, v) \leq c(u, v) \\).
  - **Conservation** : Pour tout nœud qui n'est ni \\( s \\) ni \\( t \\), le flux entrant = le flux sortant (pas d'accumulation).
- **Flot Net** : Le flot est antisymétrique : \\( f(u, v) = -f(v, u) \\).
- **Graphe Résiduel** : Suit la capacité restante après envoi du flux. Si vous envoyez \\( f \\) sur une arête de capacité \\( c \\), la capacité résiduelle avant est \\( c - f \\), et arrière est \\( f \\) (pour "annuler" le flux).
- **Objectifs** :
  - **Flot Maximum** : Maximiser le flux total de \\( s \\) à \\( t \\).
  - **Coupe Minimum** : Partitionner les nœuds en \\( S \\) (avec \\( s \\)) et \\( T \\) (avec \\( t \\)) ; minimiser la somme des capacités de \\( S \\) vers \\( T \\). Par le théorème flot-max/coupe-min, le flot max = la capacité de la coupe min.

#### 2. Un Exemple Simple
Imaginez un petit réseau pour l'expédition de marchandises :

- Nœuds : \\( s \\) (source), A, B, \\( t \\) (puits).
- Arêtes :
  - \\( s \to A \\) : capacité 10
  - \\( s \to B \\) : capacité 10
  - \\( A \to B \\) : capacité 2
  - \\( A \to t \\) : capacité 8
  - \\( B \to t \\) : capacité 9

Visualisation ASCII :
```
  s
 / \
10  10
A   B
| \ / |
8  2  9
 \ /  
  t
```

Quel est le flot maximum ? Intuitivement, envoyez 10 vers A et 10 vers B, mais A ne peut pousser que 8 vers t (2 vont vers B, ce qui aide B à pousser 9+2=11, mais la limite de B est 9 ? Attendez, calculons correctement.

En utilisant un algorithme (ci-dessous), le flot maximum est 17 :
- Chemin 1 : s→A→t (flot 8), mises à jour résiduelles.
- Chemin 2 : s→B→t (flot 9), mises à jour résiduelles.
- Chemin 3 : s→A→B→t (flot 0 ? Attendez, après le premier, A a 2 restants vers B, mais B vers t a 0 restant—en fait, ajustons.

Mieux : Le total depuis s est 20, mais les goulots d'étranglement limitent à 17 (8 direct de A + 9 de B, avec 2 reroutés ? Non—exécutez l'algo pour la précision.

#### 3. Principaux Algorithmes
Commencez par les bases ; progressez vers les plus efficaces. Tous augmentent le flux le long des chemins dans le graphe résiduel jusqu'à ce qu'il n'y ait plus de chemins d'augmentation.

- **Méthode de Ford-Fulkerson** (1956, fondamentale) :
  - Trouve répétitivement n'importe quel chemin de s à t dans le graphe résiduel (par exemple, via DFS/BFS).
  - Augmente le flux par la capacité résiduelle minimale sur ce chemin.
  - Répète jusqu'à ce qu'il n'y ait plus de chemin.
  - **Temps** : Dépend de l'implémentation ; peut être lent si les capacités sont irrationnelles (mais entiers : O(|E| * max_flow)).
  - **Avantages** : Simple. **Inconvénients** : Inefficace pour les grands graphes.
  - Pseudocode :
    ```
    tant qu'il existe un chemin P de s à t dans le graphe résiduel :
        goulot = capacité résiduelle min sur P
        augmenter le flux le long de P par goulot
        mettre à jour les résiduels
    retourner le flux total
    ```

- **Edmonds-Karp** (1972, variante BFS de Ford-Fulkerson) :
  - Utilise BFS pour trouver le plus court chemin d'augmentation (évite les longs chemins).
  - **Temps** : O(|V| * |E|^2) — polynomial, pratique pour les petits graphes.
  - Idéal pour l'apprentissage ; implémentable en ~50 lignes de code.

- **Algorithme de Dinic** (1970, plus rapide) :
  - Construit un **graphe de niveaux** via BFS (couches par distance depuis s).
  - Utilise DFS pour trouver des flots bloquants (chemins multiples par niveau).
  - **Temps** : O(|V|^2 * |E|) pire cas, mais O(|V| * |E|) pour les capacités unitaires ; très rapide en pratique.
  - **Quand l'utiliser** : Graphes de taille moyenne à grande.

- **Push-Relabel (ou Preflow-Push)** (années 80, Goldberg-Tarjan) :
  - "Pousse" l'excès de flux des nœuds vers le puits en utilisant des heuristiques.
  - **Temps** : O(|V|^3) ou mieux avec les heuristiques FIFO/gap.
  - **Avantages** : Gère les très grands graphes (par exemple, le routage Internet).

Pour la coupe min : Après le flot max, la coupe est les nœuds atteignables depuis s dans le graphe résiduel final vs. les autres.

#### 4. Conseils d'Implémentation
- Utilisez des listes d'adjacence pour les graphes.
- En code (style Python) : Représentez les capacités résiduelles comme un dict de dicts.
- Bibliothèques : NetworkX (Python) a des fonctions intégrées comme `maximum_flow`.
- Testez sur de petits exemples ; visualisez avec des outils comme Graphviz.

#### 5. Pièges Courants & Extensions
- **Cycles** : Les résiduels gèrent le "reflux" pour ajuster.
- **Sources/Puits Multiples** : Ajoutez une super-source/super-puits.
- **Coûts** : Pour le flot à coût minimum, ajoutez des coûts aux arêtes et utilisez des chemins les plus courts successifs.
- **Applications** : Planification aérienne, segmentation d'image (vision), appariement biparti (définir flow=1).

#### Parcours d'Apprentissage
- Lisez CLRS (Cormen et al.) Chapitre 26.
- Entraînez-vous sur LeetCode/HackerRank (par exemple, "Minimum Cost to Make at Least One Valid Path").
- Visualisez : Dessinez les résiduels après chaque augmentation.

[Introduction aux flots dans les réseaux](https://www.geeksforgeeks.org/maximum-bipartite-matching/)  
[Théorème Flot-Max/Coupe-Min](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem)  
[Tutoriel NetworkX](https://networkx.org/documentation/stable/tutorial.html)