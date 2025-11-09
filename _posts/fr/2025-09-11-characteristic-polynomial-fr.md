---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Polynôme caractéristique en algèbre linéaire
translated: true
type: note
---

### **Introduction complète au polynôme caractéristique en algèbre linéaire**

Le **polynôme caractéristique** est un concept fondamental en **algèbre linéaire** qui joue un rôle crucial dans l'étude des **valeurs propres, vecteurs propres, diagonalisation et propriétés des matrices**. Il fournit un pont entre les **transformations linéaires** et les **équations polynomiales**, nous permettant d'analyser les matrices en termes de leurs propriétés spectrales.

---

## **1. Définition du polynôme caractéristique**
Étant donnée une matrice carrée **\\( n \times n \\)** \\( A \\) sur un corps \\( \mathbb{F} \\) (typiquement \\( \mathbb{R} \\) ou \\( \mathbb{C} \\)), le **polynôme caractéristique** de \\( A \\), noté \\( p_A(\lambda) \\) ou \\( \chi_A(\\lambda) \\), est défini par :

\\[
p_A(\lambda) = \det(\lambda I_n - A)
\\]

où :
- \\( \lambda \\) est une **variable scalaire** (une indéterminée),
- \\( I_n \\) est la **matrice identité \\( n \times n \\)**,
- \\( \det \\) désigne le **déterminant** de la matrice \\( (\lambda I_n - A) \\).

### **Forme explicite**
Pour une matrice \\( n \times n \\) \\( A \\), le polynôme caractéristique est un **polynôme unitaire de degré \\( n \\)** en \\( \lambda \\) :

\\[
p_A(\lambda) = \lambda^n + c_{n-1} \lambda^{n-1} + \dots + c_1 \lambda + c_0
\\]

où les coefficients \\( c_i \\) dépendent des entrées de \\( A \\).

---

## **2. Propriétés clés du polynôme caractéristique**
Le polynôme caractéristique possède plusieurs propriétés importantes qui le rendent utile en algèbre linéaire :

### **(1) Les racines sont les valeurs propres**
Les **racines** de l'équation caractéristique \\( p_A(\lambda) = 0 \\) sont précisément les **valeurs propres** de \\( A \\).

\\[
p_A(\lambda) = 0 \implies \det(\lambda I - A) = 0 \implies \lambda \text{ est une valeur propre de } A.
\\]

### **(2) Degré et coefficient dominant**
- Le polynôme caractéristique est toujours **unitaire** (le coefficient de \\( \lambda^n \\) est 1).
- Le **degré** de \\( p_A(\lambda) \\) est égal à la **taille de la matrice \\( A \\)** (c'est-à-dire \\( n \\) pour une matrice \\( n \times n \\)).

### **(3) Théorème de Cayley-Hamilton**
Un résultat remarquable stipule que **toute matrice vérifie sa propre équation caractéristique** :

\\[
p_A(A) = A^n + c_{n-1} A^{n-1} + \dots + c_1 A + c_0 I = 0
\\]

Ce théorème est utile pour calculer les **puissances de matrices, les inverses et les fonctions de matrices**.

### **(4) Invariance par similitude**
Si deux matrices \\( A \\) et \\( B \\) sont **semblables** (c'est-à-dire \\( B = P^{-1}AP \\) pour une matrice inversible \\( P \\)), alors elles ont le **même polynôme caractéristique** :

\\[
p_A(\lambda) = p_B(\lambda)
\\]

Cela signifie que le polynôme caractéristique est un **invariant de similitude**.

### **(5) Relations avec la trace et le déterminant**
- Le **coefficient de \\( \lambda^{n-1} \\)** est \\( -\text{tr}(A) \\) (l'opposé de la **trace** de \\( A \\)).
- Le **terme constant \\( c_0 \\)** est \\( (-1)^n \det(A) \\).

Par exemple, pour une matrice \\( 2 \times 2 \\) :
\\[
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \quad p_A(\lambda) = \lambda^2 - (a + d)\lambda + (ad - bc)
\\]
Ici, \\( \text{tr}(A) = a + d \\) et \\( \det(A) = ad - bc \\).

### **(6) Multiplicité des valeurs propres**
- La **multiplicité algébrique** d'une valeur propre \\( \lambda \\) est sa **multiplicité en tant que racine** de \\( p_A(\lambda) \\).
- La **multiplicité géométrique** est la dimension du **sous-espace propre** \\( \ker(\lambda I - A) \\).

Pour qu'une matrice soit **diagonalisable**, la multiplicité géométrique doit être égale à la multiplicité algébrique pour chaque valeur propre.

---

## **3. Calcul du polynôme caractéristique**
Le polynôme caractéristique peut être calculé de plusieurs manières :

### **(1) Développement direct (pour les petites matrices)**
Pour une matrice \\( 2 \times 2 \\) :
\\[
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \quad \lambda I - A = \begin{pmatrix} \lambda - a & -b \\ -c & \lambda - d \end{pmatrix}
\\]
\\[
p_A(\lambda) = (\lambda - a)(\lambda - d) - bc = \lambda^2 - (a + d)\lambda + (ad - bc)
\\]

Pour une matrice \\( 3 \times 3 \\), le calcul devient plus complexe mais suit le même principe de développement du déterminant.

### **(2) Utilisation du développement de Laplace (pour les matrices plus grandes)**
Pour les matrices plus grandes, le déterminant est calculé en utilisant le **développement par cofacteurs** le long d'une ligne ou d'une colonne.

### **(3) Exploitation des structures matricielles spéciales**
- **Matrices triangulaires** : Le polynôme caractéristique est le produit des éléments diagonaux moins \\( \lambda \\) :
  \\[
  p_A(\lambda) = \prod_{i=1}^n (a_{ii} - \lambda)
  \\]
- **Matrices diagonales** : Similaire aux matrices triangulaires.
- **Matrices compagnons** : Le polynôme caractéristique correspond au polynôme définissant la matrice.

### **(4) Méthodes numériques (pour les grandes matrices)**
Pour les très grandes matrices, le calcul exact est impraticable et des **méthodes numériques** (par exemple, l'algorithme QR) sont utilisées pour approximer les valeurs propres.

---

## **4. Applications du polynôme caractéristique**
Le polynôme caractéristique est utilisé dans divers domaines de l'algèbre linéaire et au-delà :

### **(1) Analyse des valeurs propres et vecteurs propres**
- Résoudre \\( p_A(\lambda) = 0 \\) donne les valeurs propres.
- Les sous-espaces propres sont trouvés en résolvant \\( (\lambda I - A)\mathbf{v} = 0 \\).

### **(2) Diagonalisation et forme de Jordan**
- Une matrice est **diagonalisable** si son polynôme caractéristique n'a **pas de racines multiples** (sur \\( \mathbb{C} \\)) et que la multiplicité géométrique est égale à la multiplicité algébrique pour chaque valeur propre.
- La **forme canonique de Jordan** est déterminée par la structure du polynôme caractéristique.

### **(3) Fonctions de matrices et équations différentielles**
- Utilisé pour calculer les **exponentielles de matrices** \\( e^{At} \\) (important dans les **systèmes d'équations différentielles**).
- Aide à résoudre les **relations de récurrence** et les **systèmes dynamiques**.

### **(4) Analyse de stabilité (Théorie du contrôle)**
- En **théorie du contrôle**, les valeurs propres (racines de \\( p_A(\lambda) \\)) déterminent la **stabilité** d'un système.
- Un système est **asymptotiquement stable** si toutes les valeurs propres ont des **parties réelles négatives**.

### **(5) Théorie des graphes (Matrice d'adjacence)**
- Le polynôme caractéristique de la **matrice d'adjacence d'un graphe** fournit des informations sur les **spectres de graphes**, la **connexité** et les **couplages**.

### **(6) Mécanique quantique**
- En mécanique quantique, les valeurs propres de la **matrice hamiltonienne** (niveaux d'énergie) sont trouvées via son polynôme caractéristique.

---

## **5. Exemples de calculs**
### **Exemple 1 : Matrice \\( 2 \times 2 \\)**
Soit :
\\[
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
\\]
Calculons \\( \lambda I - A \\) :
\\[
\lambda I - A = \begin{pmatrix} \lambda - 1 & -2 \\ -3 & \lambda - 4 \end{pmatrix}
\\]
Le polynôme caractéristique est :
\\[
p_A(\lambda) = (\lambda - 1)(\lambda - 4) - (-2)(-3) = \lambda^2 - 5\lambda + 4 - 6 = \lambda^2 - 5\lambda - 2
\\]
**Valeurs propres** : Résoudre \\( \lambda^2 - 5\lambda - 2 = 0 \\) :
\\[
\lambda = \frac{5 \pm \sqrt{25 + 8}}{2} = \frac{5 \pm \sqrt{33}}{2}
\\]

### **Exemple 2 : Matrice triangulaire**
Soit :
\\[
A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 3 \end{pmatrix}
\\]
Le polynôme caractéristique est :
\\[
p_A(\lambda) = (2 - \lambda)^2 (3 - \lambda)
\\]
**Valeurs propres** : \\( \lambda = 2 \\) (multiplicité algébrique 2), \\( \lambda = 3 \\) (multiplicité 1).

---

## **6. Limitations et considérations**
- **Complexité computationnelle** : Pour les grandes matrices, calculer le polynôme caractéristique est **NP-difficile** en général.
- **Instabilité numérique** : Le calcul direct peut être **mal conditionné** pour l'arithmétique à virgule flottante.
- **Matrices non diagonalisables** : Si le polynôme caractéristique a des **racines multiples**, la matrice peut ne pas être diagonalisable (des blocs de Jordan apparaissent).
- **Dépendance au corps** : La factorisation de \\( p_A(\lambda) \\) dépend du **corps de base** (par exemple, certains polynômes se factorisent sur \\( \mathbb{C} \\) mais pas sur \\( \mathbb{R} \\)).

---

## **7. Généralisations et concepts associés**
- **Polynôme minimal** : Le **polynôme unitaire de plus petit degré** tel que \\( m_A(A) = 0 \\). Il divise le polynôme caractéristique.
- **Polynômes annulateurs** : Tout polynôme \\( q(\lambda) \\) tel que \\( q(A) = 0 \\).
- **Équation séculaire** : En physique, le polynôme caractéristique apparaît dans la **théorie des perturbations**.
- **Matrice résultante** : Utilisée dans la **recherche de racines de polynômes** et la **théorie de l'élimination**.

---

## **8. Conclusion**
Le **polynôme caractéristique** est un **outil puissant** en algèbre linéaire qui relie la **théorie des matrices, les équations polynomiales et les problèmes de valeurs propres**. Il est essentiel pour :
- La **diagonalisation** et la **forme normale de Jordan**,
- L'**analyse de stabilité** dans les systèmes dynamiques,
- Le **calcul des fonctions de matrices** (exponentielles, logarithmes),
- La **résolution de relations de récurrence linéaires** et d'**équations différentielles**.

Bien que son calcul puisse être difficile pour les grandes matrices, son importance théorique ne peut être surestimée, ce qui en fait une **pierre angulaire de l'algèbre linéaire avancée et des mathématiques appliquées**.

---
Souhaitez-vous approfondir un aspect spécifique, tel que les **méthodes de calcul, les applications en physique ou le théorème de Cayley-Hamilton** ?