---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Aperçu de l'arbre AVL
translated: true
type: note
---

### Qu'est-ce qu'un arbre AVL ?

Un arbre AVL est un type **d'arbre binaire de recherche (ABR) auto-équilibré**, inventé en 1962 par Georgy Adelson-Velsky et Evgenii Landis (d'où le nom). Comme tout ABR, il stocke les données de manière triée : tous les nœuds du sous-arbre gauche sont plus petits que le nœud parent, et tous ceux du sous-arbre droit sont plus grands. La caractéristique principale est qu'il ajuste automatiquement sa structure après des insertions ou des suppressions pour rester équilibré.

### Comment fonctionne-t-il ?

- **Facteur d'équilibre** : Pour chaque nœud, l'arbre calcule un "facteur d'équilibre" comme la hauteur du sous-arbre gauche moins la hauteur du sous-arbre droit. Ce facteur doit toujours être -1, 0 ou +1 (c'est-à-dire que les sous-arbres diffèrent d'au plus un niveau).
- **Rotations pour l'équilibrage** : Si une insertion ou une suppression viole le facteur d'équilibre :
  - **Rotations simples** (gauche ou droite) corrigent les déséquilibres où la violation se trouve dans l'enfant le plus proche.
  - **Rotations doubles** (gauche-droite ou droite-gauche) traitent les cas où elle se trouve dans l'enfant le plus éloigné.
- Ces rotations préservent la propriété ABR tout en rétablissant l'équilibre, et s'exécutent en temps O(1) par opération.

Exemple : Insérer des nœuds dans l'ordre croissant dans un ABR simple en ferait une liste chaînée (déséquilibrée). Dans un arbre AVL, les rotations le maintiennent approximativement équilibré en hauteur, comme dans cet exemple simplifié avant/après :

```
Déséquilibré (après insertions : 1,2,3) :
    2
   /
  1
 /
3  (en réalité, décalé à droite : 1->2->3)

Après rotation :
  2
 / \
1   3
```

### Pourquoi est-il spécial ?

- **Efficacité garantie** : Contrairement aux ABR classiques, qui peuvent atteindre O(n) dans le pire cas (par exemple, décalés comme une liste), les arbres AVL garantissent un temps **O(log n)** en moyenne et dans le pire cas pour la recherche, l'insertion et la suppression. Cela les rend idéaux pour les applications nécessitant des performances constantes, comme les bases de données ou les tables des symboles.
- **Compromis** : Ils sont plus stricts que d'autres arbres équilibrés (par exemple, les arbres rouge-noir, qui permettent un peu plus de déséquilibre pour des insertions/suppressions plus rapides). AVL privilégie la vitesse de recherche sur la vitesse de modification.
- **Espace** : Utilise un champ supplémentaire par nœud pour le suivi de la hauteur/du facteur d'équilibre, mais cela est mineur.

En bref, les arbres AVL sont "spéciaux" pour leur auto-équilibrage rigoureux, transformant des ABR potentiellement chaotiques en structures performantes et fiables avec une complexité logarithmique.

Pour plus de détails : [Arbre AVL sur Wikipédia](https://fr.wikipedia.org/wiki/Arbre_AVL)