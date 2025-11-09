---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Définition de l'adjointe et relation avec le cofacteur
translated: true
type: note
---

### Clarification de la définition de l'adjointe (et sa relation avec les cofacteurs)

Vous êtes globalement sur la bonne voie concernant la construction de l'adjointe via les cofacteurs, mais il y a une petite correction importante à apporter à votre description. La matrice adjointe (souvent notée `adj(A)`) n'est pas construite en multipliant l'élément original `a(i,j)` par le déterminant signé du "reste" (la sous-matrice après suppression de la ligne i et de la colonne j). À la place :

- Le **cofacteur** `C_ij` de l'élément `a(i,j)` est défini comme `C_ij = (-1)^{i+j} * det(M_ij)`, où `M_ij` est la sous-matrice obtenue en supprimant la ligne i et la colonne j de A. Ceci est purement le **mineur signé** — il n'y a pas de multiplication par `a(i,j)` lui-même.
- La **matrice des cofacteurs** C a ces `C_ij` comme éléments.
- L'**adjointe** est la **transposée** de la matrice des cofacteurs : `adj(A) = C^T`. Ainsi, l'élément en position (i,j) de `adj(A)` est en réalité `C_ji` (le cofacteur avec les indices inversés).

Cette structure de mineurs signés provient du développement de Laplace pour le calcul des déterminants (nous en reparlerons plus bas). Votre description ressemble un peu à la formule du déterminant elle-même : `det(A) = somme sur j de a(i,j) * C_ij` (le long de n'importe quelle ligne i), qui elle, *implique* bien une multiplication par `a(i,j)`. Mais l'adjointe omet cette multiplication — c'est simplement la collection de ces mineurs signés, transposée, pour permettre de jolies identités algébriques.

Prenons un exemple rapide 2x2 pour illustrer (disons A = [[a, b], [c, d]]) :
- Cofacteurs : C_11 = (-1)^{1+1} det([d]) = d ; C_12 = (-1)^{1+2} det([c]) = -c ; C_21 = (-1)^{2+1} det([b]) = -b ; C_22 = (-1)^{2+2} det([a]) = a.
- Matrice des cofacteurs C = [[d, -c], [-b, a]].
- Adjointe adj(A) = C^T = [[d, -b], [-c, a]].
- Remarquez qu'il n'y a pas de multiplicateurs a, b, c, d originaux dans les cofacteurs — tout repose sur les sous-matrices "restantes".

Oui, c'est exactement ainsi que l'on calcule l'adjointe : pour chaque position, supprimer la ligne/colonne, prendre le det du reste, appliquer le signe `(-1)^{i+j}`, assembler pour former C, puis transposer pour obtenir adj(A). C'est récursif (les mineurs impliquent des matrices plus petites), donc pour les grandes matrices n x n, c'est très coûteux en calcul — c'est pourquoi on utilise souvent l'élimination de Gauss pour les inverses en pratique.

### Pourquoi a-t-on besoin de l'Adjointe ? (C'est plus qu'une simple étape intermédiaire)

Vous avez parfaitement raison de penser que cela ressemble à une "présentation intermédiaire" pour l'inversion matricielle — et dans un sens computationnel, c'est le cas ! La formule clé est `A^{-1} = (1 / det(A)) * adj(A)`, en supposant que det(A) ≠ 0. Cela donne directement l'inverse en utilisant uniquement des déterminants de sous-matrices, sans avoir besoin d'opérations sur les lignes. Mais ce n'est pas *qu'une* étape intermédiaire ; voici pourquoi elle est utile et nécessaire :

1. **Formule d'Inversion Matricielle** : Pour les petites matrices ou le calcul symbolique (par exemple, dans les preuves ou l'arithmétique exacte), c'est une manière propre et explicite d'exprimer l'inverse. Cela met en lumière comment l'inverse se "décompose" en cofacteurs mis à l'échelle.

2. **Perspectives Théoriques** : L'identité `A * adj(A) = adj(A) * A = det(A) * I` (où I est la matrice identité) révèle une structure profonde. Elle montre que toute matrice commute avec son adjointe à un scalaire près, et elle est le fondement de la compréhension des matrices singulières (det(A)=0 implique A adj(A)=0, donc les noyaux s'alignent).

3. **Règle de Cramer pour les Systèmes Linéaires** : Pour résoudre Ax = b, le i-ème élément de la solution est `x_i = det(A_i) / det(A)`, où A_i est la matrice A dont la colonne i est remplacée par b. Mais det(A_i) se développe via des cofacteurs impliquant les éléments de b — utilisant essentiellement l'adjointe en arrière-plan pour un calcul efficace sans inversion complète.

4. **Développements des Déterminants** : Les cofacteurs permettent le développement de Laplace (votre idée de "det(rest)"), qui est crucial pour calculer det(A) en le décomposant en problèmes plus petits. Historiquement, cela a rendu les déterminants traitables avant l'ère des ordinateurs.

5. **Applications Plus Larges** : En géométrie projective, en infographie (transformations), et même en physique (par exemple, matrices d'impédance), les adjointes apparaissent pour gérer les singularités ou dériver des inverses dans des anneaux au-delà des réels (comme les polynômes).

En bref, bien que la réduction des lignes soit plus rapide pour le calcul numérique, l'adjointe fournit une voie "analytique" qui est élégante pour la théorie, l'enseignement et les cas où l'on a besoin de formules explicites. C'est comme le "pourquoi" derrière l'inverse, pas seulement un moyen d'arriver à une fin.

### Comment l'Adjointe a-t-elle été inventée ? (Un peu d'histoire)

L'adjointe n'est pas née d'un seul "moment eurêka" — c'est un développement naturel des travaux des XVIIIe et XIXe siècles sur les déterminants et les équations linéaires, à une époque où les matrices n'étaient pas encore formalisées (le terme "matrice" est apparu en 1850). Aucun inventeur unique n'est crédité, mais voici la piste :

- **Racines dans les Déterminants (Fin des années 1600–1700)** : Les déterminants sont apparus de la résolution de systèmes linéaires (par exemple, Leibniz en 1693 pour les cas 2x2). Dans les années 1700, des mathématiciens comme Cramer (1750) utilisaient des développements par mineurs pour les solutions, touchant implicitement aux cofacteurs.

- **Concepts Précoces d'« Adjoint » (Années 1760–1800)** : Joseph-Louis Lagrange a forgé le terme "équations adjointes" vers 1766 pour les équations différentielles, où un opérateur "adjoint" reflète l'original (comme la transposée pour les matrices). Arthur Cayley (années 1840–50) a étendu cela aux "formes linéaires adjointes" dans ses travaux sur les matrices. Maxime Bôcher a formalisé la "matrice adjointe" au début des années 1900, mais l'idée centrale est antérieure.

- **L'Idée Clé de Gauss (1801)** : Carl Friedrich Gauss, dans ses *Disquisitiones Arithmeticae*, a défini un "adjoint" pour les formes quadratiques (par exemple, ax² + 2bxy + cy²). Il a construit une forme compagne dont les coefficients sont essentiellement les mineurs signés 2x2 de la matrice symétrique représentant l'original — précisément l'adjointe (à des conventions de signe près). C'était pour la théorie des nombres (formes quadratiques binaires), mais cela anticipe directement la définition moderne. Le travail de Gauss a rendu la construction systématique.

- **Formalisation (À partir du milieu du XIXe siècle)** : Alors que la théorie des matrices se solidifiait (Cayley, Sylvester, Kronecker), le développement par cofacteurs (de Laplace, 1772) a fusionné avec ces idées. Dans les années 1850–60, la formule complète de l'inverse `A^{-1} = adj(A)/det(A)` est apparue dans les textes, avec "adjointe" (du latin "adjugare", atteler ensemble) soulignant son rôle de liaison dans l'inversion.

L'"invention" est probablement issue de la détection de motifs : en développant les déterminants, les mathématiciens ont remarqué que les collections de cofacteurs "inversent" la matrice lorsqu'elles sont mises à l'échelle. Ce fut moins un éclair de génie et plus une évolution organique de la résolution manuelle d'équations. Les textes modernes (par exemple, *Introduction to Linear Algebra* de Strang) l'enseignent encore de cette manière pour l'intuition.

Si vous souhaitez des exemples en code (par exemple, Python via NumPy/SymPy pour en calculer une) ou une exploration plus approfondie de la construction de Gauss, dites-le !

[Adjugate matrix - Wikipedia](https://en.wikipedia.org/wiki/Adjugate_matrix)  
[First usage of "adjoint" - History of Science and Mathematics Stack Exchange](https://hsm.stackexchange.com/questions/5908/what-is-the-first-usage-of-the-term-adjoint-and-why-was-this-word-chosen)