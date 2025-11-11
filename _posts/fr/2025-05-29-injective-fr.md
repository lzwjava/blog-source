---
audio: false
generated: true
lang: fr
layout: post
title: Fonctions injectives
translated: true
type: note
---

En mathématiques, le terme « injective » fait référence à une fonction ou une application entre deux ensembles où des éléments distincts du premier ensemble sont appliqués sur des éléments distincts du second ensemble. En d'autres termes, deux éléments différents du domaine (le premier ensemble) ne sont jamais appliqués sur le même élément du codomaine (le second ensemble).

Cette propriété est également connue sous le nom de « un-à-un ». Si une fonction \\( f \\) est injective, alors pour deux éléments quelconques \\( x \\) et \\( y \\) du domaine, si \\( f(x) = f(y) \\), alors nécessairement \\( x = y \\). Cela garantit que chaque élément du codomaine est l'image d'au plus un élément du domaine.

---

Pour comprendre pourquoi une transformation linéaire \\( T \\) est injective si son noyau ne contient que le vecteur nul, décomposons les définitions et les implications :

1. **Noyau d'une transformation** : Le noyau d'une transformation linéaire \\( T: V \rightarrow W \\) (noté \\( \ker(T) \\)) est l'ensemble de tous les vecteurs de \\( V \\) qui sont appliqués sur le vecteur nul de \\( W \\). Mathématiquement, \\( \ker(T) = \{ v \in V \mid T(v) = 0 \} \\).

2. **Transformation injective** : Une transformation linéaire \\( T \\) est injective (ou un-à-un) si des vecteurs différents dans \\( V \\) sont appliqués sur des vecteurs différents dans \\( W \\). Autrement dit, si \\( T(u) = T(v) \\), alors \\( u = v \\).

Maintenant, connectons ces deux concepts :

- Supposons que \\( \ker(T) = \{0\} \\). Cela signifie que le seul vecteur de \\( V \\) qui est appliqué sur le vecteur nul de \\( W \\) est le vecteur nul lui-même.

- Pour montrer que \\( T \\) est injective, supposons que \\( T(u) = T(v) \\). Par la linéarité de \\( T \\), nous avons \\( T(u) - T(v) = T(u - v) = 0 \\).

- Puisque \\( \ker(T) = \{0\} \\), \\( T(u - v) = 0 \\) implique que \\( u - v = 0 \\), ce qui signifie que \\( u = v \\).

Ainsi, si \\( \ker(T) = \{0\} \\), la transformation \\( T \\) est injective. En effet, la seule solution de \\( T(v) = 0 \\) est \\( v = 0 \\), ce qui garantit qu'aucun couple de vecteurs distincts dans \\( V \\) n'est appliqué sur le même vecteur dans \\( W \\).

---

L'équation \\( T(u) - T(v) = T(u - v) \\) est une conséquence de la propriété de linéarité d'une transformation linéaire \\( T \\). Décomposons pourquoi cela est vrai :

1. **Linéarité de \\( T \\)** : Une transformation linéaire \\( T \\) satisfait deux propriétés clés pour tous vecteurs \\( u \\) et \\( v \\) de l'espace vectoriel et tout scalaire \\( c \\) :
   - **Additivité** : \\( T(u + v) = T(u) + T(v) \\)
   - **Homogénéité** : \\( T(cu) = cT(u) \\)

2. **Dérivation de \\( T(u) - T(v) = T(u - v) \\)** :
   - En utilisant la propriété d'additivité, nous pouvons exprimer \\( T(u - v) \\) comme \\( T(u + (-v)) \\), ce qui est égal à \\( T(u) + T(-v) \\).
   - Par la propriété d'homogénéité, \\( T(-v) = -T(v) \\).
   - Par conséquent, \\( T(u - v) = T(u) + (-T(v)) = T(u) - T(v) \\).

Ainsi, \\( T(u) - T(v) = T(u - v) \\) est un résultat direct de la linéarité de \\( T \\). Cette propriété est fondamentale en algèbre linéaire et est fréquemment utilisée dans les démonstrations et les dérivations impliquant des transformations linéaires.