---
audio: false
generated: true
lang: fr
layout: post
title: Algorithme de recherche A* (A-star)
translated: true
type: note
---

L'algorithme de recherche **A* (A-star)** est un algorithme populaire de recherche de chemin et de parcours de graphes utilisé en informatique et en intelligence artificielle. Il est largement utilisé pour trouver le chemin le plus court d'un point de départ (ou nœud) à une cible (ou objectif) dans un graphe, tout en explorant efficacement les chemins possibles.

A* combine des éléments de **l'algorithme de Dijkstra** (qui garantit le chemin le plus court) et de la **recherche best-first gloutonne** (qui tente de trouver l'objectif le plus rapidement possible). La caractéristique clé de A* est qu'il utilise à la fois le coût réel pour atteindre un nœud (depuis le nœud de départ) et une heuristique qui estime le coût de ce nœud à l'objectif.

### Fonctionnement de A* :
1. **Commencer avec une liste ouverte** : La liste ouverte contient les nœuds qui restent à explorer. Initialement, seul le nœud de départ se trouve dans cette liste.
2. **Calculer les scores** : Chaque nœud de la liste ouverte se voit attribuer un score basé sur deux facteurs :
   - **g(n)** : Le coût pour atteindre le nœud actuel depuis le nœud de départ.
   - **h(n)** : Une estimation heuristique du coût pour atteindre l'objectif depuis le nœud actuel (celle-ci est spécifique au domaine, comme la distance en ligne droite ou la distance euclidienne).
   - **f(n) = g(n) + h(n)** : Le coût total estimé, utilisé pour prioriser les nœuds. Les nœuds avec le f(n) le plus faible sont explorés en premier.
3. **Développer le nœud le plus prometteur** : Le nœud avec le score f(n) le plus faible est choisi pour l'exploration. Il est déplacé vers une "liste fermée" des nœuds déjà explorés.
4. **Vérifier les voisins** : L'algorithme examine les voisins du nœud actuel. Si un voisin n'a pas été visité ou peut être atteint avec un coût inférieur, il est ajouté à la liste ouverte.
5. **Répéter** jusqu'à ce que l'objectif soit atteint ou que la liste ouverte soit vide (indiquant qu'aucun chemin n'existe).

### Composants clés :
- **g(n)** : Le coût réel depuis le nœud de départ jusqu'au nœud actuel.
- **h(n)** : L'estimation heuristique depuis le nœud actuel jusqu'à l'objectif (peut varier selon le problème).
- **f(n) = g(n) + h(n)** : Le coût total qui priorise les nœuds pour l'exploration.

### Heuristiques :
La fonction heuristique est essentielle pour l'efficacité de A*. Une heuristique courante pour la recherche de chemin basée sur une grille est la **distance de Manhattan** (somme des distances horizontales et verticales) ou la **distance euclidienne** (distance en ligne droite) pour les espaces continus.

### Exemples d'utilisation :
- **Systèmes de navigation** (GPS)
- **Jeux vidéo et IA** (recherche de chemin pour les personnages ou agents)
- **Robotique** (pour planifier des chemins efficaces)

En résumé, A* est un algorithme très efficace car il explore systématiquement les chemins en se basant à la fois sur le coût connu et sur le coût futur estimé, garantissant qu'il trouve la solution optimale lorsque cela est possible.