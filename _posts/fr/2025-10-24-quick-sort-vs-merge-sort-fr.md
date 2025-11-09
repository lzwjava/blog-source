---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Tri Rapide contre Tri Fusion
translated: true
type: note
---

### Pourquoi le tri rapide semble délicat (et pas le tri fusion)

Tu as raison — implémenter le tri rapide de zéro sans références peut donner l'impression de lutter contre un cochon graissé, tandis que le tri fusion est plus comme plier du linge : méthodique et prévisible. Le flux "diviser, conquérir, combiner" du tri fusion est linéaire et récursif de manière propre, sans surprises à l'étape de fusion. Le tri rapide, en revanche, est *en place* et repose sur une astuce de partitionnement intelligente qui implique d'échanger des éléments autour d'un "pivot" (un point de division choisi). Cela semble chaotique au début parce que le pivot n'est pas fixe — c'est plus comme un arbitre qui se fait déplacer pendant le jeu. Mais une fois que tu saisis l'intuition, c'est élégamment efficace (en moyenne O(n log n), dans le pire cas O(n²) si les pivots sont mauvais).

Laisse-moi te présenter le tri rapide avec une approche naturelle, comme une histoire : imagine que tu tries un tas de livres en désordre sur une étagère par hauteur. Au lieu de diviser le tas en deux, de tout mesurer et de fusionner (c'est le tri fusion), tu choisis un livre comme "référence" (le pivot), puis tu réarranges les autres pour que tous les livres plus courts soient à sa gauche et tous les plus grands à sa droite. Le pivot se retrouve à sa place *finale*, et tu appliques la récursion uniquement sur les sous-tas de gauche et de droite. Pas besoin d'espace supplémentaire — juste des échanges sur l'étagère. C'est comme la cérémonie hollandaise de lever de drapeau "quicksort" (d'où le nom), où tu partitionnes en trois groupes : plus court, référence, plus grand.

### Pourquoi ça marche : La magie du partitionnement

Le tri rapide fonctionne grâce à une **garantie de diviser-pour-régner** : chaque étape de partitionnement place *au moins un élément* (le pivot) dans sa position finale correcte, réduisant le problème d'au moins autant à chaque fois. Dans le meilleur cas, le pivot divise le tableau de manière égale (comme la division en deux du tri fusion), conduisant à une récursion équilibrée. Dans le pire cas (par exemple, un tableau déjà trié avec un mauvais choix de pivot), il dégénère en O(n²) comme le tri à bulles — mais de bons choix de pivot le rendent extrêmement rapide en pratique.

L'idée clé : **le partitionnement impose des invariants**. Après un partitionnement :
- Tout ce qui est à gauche du pivot ≤ pivot.
- Tout ce qui est à droite du pivot ≥ pivot.
- Le pivot est maintenant trié pour toujours — pas besoin d'y toucher à nouveau.

Cela garantit une progression : la profondeur de l'arbre de récursion est au maximum de log n en moyenne, et chaque niveau effectue un travail total de O(n) (balayage et échanges).

### Comment choisir le pivot (et pourquoi il "bouge" pendant les comparaisons)

Le pivot n'est pas sacré — c'est juste n'importe quel élément que tu choisis comme référence. Les mauvais choix (comme toujours le premier élément) peuvent déséquilibrer les choses, voici donc une progression naturelle des stratégies, de la simple à la robuste :

1.  **Naïf : Choisir le premier (ou le dernier) élément.**
    - Facile à coder, mais risqué. Sur un tableau trié `[1,2,3,4,5]`, pivot=1 signifie que la gauche est vide, la droite a 4 éléments — la récursion devient déséquilibrée.
    - Le "mouvement" : Pendant le partitionnement, tu compares tout le reste à cette valeur de pivot, mais tu échanges les éléments *autour* de sa position. Le pivot lui-même est échangé pour se mettre en place au fur et à mesure que les frontières le traversent.

2.  **Mieux : Choisir l'élément du milieu.**
    - On l'échange temporairement à la fin, et on l'utilise comme pivot. Plus équilibré intuitivement (plus proche de la médiane), mais toujours vulnérable aux entrées triées/inversées.

3.  **Le meilleur en pratique : Choisir un élément aléatoire.**
    - On l'échange à la fin, puis on partitionne. L'aléatoire moyenne les mauvais cas, rendant le pire cas improbable (avec une forte probabilité, toujours O(n log n)). C'est ce que la plupart des bibliothèques utilisent.

4.  **Sophistiqué (pour les entretiens) : Médiane de trois.**
    - Choisir la médiane du premier/du milieu/du dernier comme pivot. Rapide à calculer, évite les pièges courants.

Dans le code, on "fixe" souvent le pivot en l'échangeant d'abord à la fin, on partitionne autour de sa *valeur* (pas de sa position), puis on l'échange à l'endroit où il doit être. C'est pourquoi on a l'impression que le pivot "bouge" — il n'est pas statique ; le processus de partitionnement trouve dynamiquement sa place via deux pointeurs (gauche et droite) qui avancent l'un vers l'autre en s'échangeant les éléments qui ne respectent pas la condition.

### Un exemple pratique : Trier [3, 7, 1, 9, 4] avec le dernier élément comme pivot

Parcourons une étape de partitionnement. Tableau : `[3, 7, 1, 9, 4]`. Pivot = dernier = 4. (Nous l'échangerons au besoin.)

- Commencer avec le pointeur gauche à l'index 0 (valeur 3), droite à l'index 3 (valeur 9, car le pivot est à l'index 4).
- Balayer depuis la gauche : 3 < 4 ? Oui, le laisser. Suivant, 7 > 4 ? Oui, mais attends — on l'échange avec le premier >4 depuis la droite.
- En réalité, le partitionnement de Lomuto standard (style à un pointeur simple) :
  1. i = -1 (frontière pour < pivot).
  2. Pour j de 0 à n-2 (ignorer le pivot) :
     - Si arr[j] ≤ pivot (4), échanger arr[++i] avec arr[j]. (Agrandir le côté gauche.)
  3. Finalement, échanger le pivot avec arr[++i] pour le placer.

Étape par étape :
- j=0 : 3 ≤4 ? Oui. i=0, échanger arr[0] avec arr[0] (rien ne change). Tableau : [3,7,1,9,4]
- j=1 : 7 ≤4 ? Non. Ignorer.
- j=2 : 1 ≤4 ? Oui. i=1, échanger arr[1] (7) avec arr[2] (1). Tableau : [3,1,7,9,4]
- j=3 : 9 ≤4 ? Non. Ignorer.
- Fin : Échanger le pivot (4 à l'index 4) avec arr[++i=2] (7). Tableau : [3,1,4,9,7]

Maintenant : À gauche de 4 (index 2) se trouve [3,1] (les deux ≤4, non triés), à droite [9,7] (les deux ≥4, non triés). Pivot=4 est *terminé*. Récursion sur la gauche [3,1] et la droite [9,7].

- Gauche : Pivot=1, se partitionne en [1,3].
- Droite : Pivot=7, se partitionne en [7,9].

Tri complet : [1,3,4,7,9]. Tu vois ? À chaque étape, on verrouille la progression, et les échanges "déplacent" le pivot à sa place.

### Ébauche de pseudocode (pour faciliter l'implémentation)

```
quicksort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quicksort(arr, low, pivot_idx-1)
        quicksort(arr, pivot_idx+1, high)

partition(arr, low, high):  # Style Lomuto, pivot à high
    pivot = arr[high]
    i = low - 1
    for j in low to high-1:
        if arr[j] <= pivot:
            i += 1
            swap arr[i], arr[j]
    swap arr[i+1], arr[high]
    return i+1
```

Le "mouvement" se produit dans ces échanges : les éléments dansent les uns autour des autres jusqu'à ce que le pivot se stabilise. Entraîne-toi sur papier avec 5-6 éléments — une fois que le partitionnement clique, la récursion semble naturelle. Si tu bloques, essaie de l'animer mentalement comme ce tri de livres sur une étagère.

Pour approfondir :
[Visualisation du tri rapide](https://visualgo.net/en/sorting?slide=9)
[Chapitre CLRS sur le tri rapide](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-20.html#%_sec_3.3)