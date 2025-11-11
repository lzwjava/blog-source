---
audio: false
generated: true
lang: fr
layout: post
title: Systèmes d'équations et élimination de Gauss
translated: true
type: note
---

Ce tutoriel fournit un guide détaillé sur les **systèmes d'équations**, leur représentation, leurs solutions et la méthode d'**élimination de Gauss** utilisée pour les résoudre.

---

## **1. Systèmes d'Équations : Définition et Représentation**

Un **système d'équations linéaires** est constitué de plusieurs équations linéaires partageant des variables. Un système général avec \\( n \\) variables et \\( m \\) équations peut s'écrire :

\\[
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= b_1 \\\\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= b_2 \\\\
\vdots & \\\\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n &= b_m
\end{aligned}
\\]

où :
- \\( x_1, x_2, \dots, x_n \\) sont les variables inconnues.
- \\( a_{ij} \\) sont les coefficients.
- \\( b_1, b_2, \dots, b_m \\) sont les constantes du côté droit.

### **Représentation Matricielle**

Un système d'équations peut être représenté à l'aide de **matrices** :

\\[
A \mathbf{x} = \mathbf{b}
\\]

où :

- \\( A \\) est la **matrice des coefficients** :

  \\[
  A =
  \begin{bmatrix}
  a_{11} & a_{12} & \dots & a_{1n} \\\\
  a_{21} & a_{22} & \dots & a_{2n} \\\\
  \vdots & \vdots & \ddots & \vdots \\\\
  a_{m1} & a_{m2} & \dots & a_{mn}
  \end{bmatrix}
  \\]

- \\( \mathbf{x} \\) est le **vecteur colonne des variables** :

  \\[
  \mathbf{x} =
  \begin{bmatrix}
  x_1 \\\\
  x_2 \\\\
  \vdots \\\\
  x_n
  \end{bmatrix}
  \\]

- \\( \mathbf{b} \\) est le **vecteur colonne des constantes** :

  \\[
  \mathbf{b} =
  \begin{bmatrix}
  b_1 \\\\
  b_2 \\\\
  \vdots \\\\
  b_m
  \end{bmatrix}
  \\]

La **matrice augmentée** s'écrit :

\\[
[A | \mathbf{b}]
\\]

Exemple :
\\[
\begin{aligned}
2x + 3y &= 8 \\\\
5x - y &= 3
\end{aligned}
\\]

Représentation matricielle :
\\[
\begin{bmatrix}
2 & 3 \\\\
5 & -1
\end{bmatrix}
\begin{bmatrix}
x \\\\
y
\end{bmatrix}
=
\begin{bmatrix}
8 \\\\
3
\end{bmatrix}
\\]

Matrice augmentée :
\\[
\left[
\begin{array}{cc|c}
2 & 3 & 8 \\\\
5 & -1 & 3
\end{array}
\right]
\\]

---

## **2. Méthode d'Élimination de Gauss**

L'élimination de Gauss est une méthode systématique pour résoudre des systèmes d'équations en transformant la matrice augmentée en **forme échelonnée par lignes (REF)** puis en résolvant pour les variables en utilisant la **substitution arrière**.

### **Étapes de l'Élimination de Gauss**
1. **Convertir la matrice augmentée en une forme triangulaire supérieure (forme échelonnée par lignes)** en utilisant des opérations sur les lignes :
   - Échanger des lignes si nécessaire.
   - Multiplier une ligne par une constante non nulle.
   - Ajouter ou soustraire un multiple d'une ligne à une autre.

2. **Substitution arrière** pour trouver la solution.

---

### **Exemple 1 : Résolution d'un Système par Élimination de Gauss**

Résoudre le système :
\\[
\begin{aligned}
2x + y - z &= 3 \\\\
4x - 6y &= 2 \\\\
-2x + 7y + 2z &= 5
\end{aligned}
\\]

#### **Étape 1 : Convertir en Matrice Augmentée**
\\[
\left[
\begin{array}{ccc|c}
2 & 1 & -1 & 3 \\\\
4 & -6 & 0 & 2 \\\\
-2 & 7 & 2 & 5
\end{array}
\right]
\\]

#### **Étape 2 : Rendre le Premier Pivot Égal à 1**
Diviser la ligne 1 par 2 :
\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\\\
4 & -6 & 0 & 2 \\\\
-2 & 7 & 2 & 5
\end{array}
\right]
\\]

#### **Étape 3 : Éliminer la Première Colonne sous le Pivot**
Remplacer la ligne 2 en soustrayant 4 fois la ligne 1 :
Remplacer la ligne 3 en ajoutant 2 fois la ligne 1 :

\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\\\
0 & -8 & 2 & -4 \\\\
0 & 8 & 1 & 8
\end{array}
\right]
\\]

#### **Étape 4 : Rendre le Deuxième Pivot Égal à 1**
Diviser la ligne 2 par -8 :

\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\\\
0 & 1 & -0.25 & 0.5 \\\\
0 & 8 & 1 & 8
\end{array}
\right]
\\]

#### **Étape 5 : Éliminer la Deuxième Colonne sous le Pivot**
Remplacer la ligne 3 en soustrayant 8 fois la ligne 2 :

\\[
\left[
\begin{array}{ccc|c}
1 & 0.5 & -0.5 & 1.5 \\\\
0 & 1 & -0.25 & 0.5 \\\\
0 & 0 & 3 & 4
\end{array}
\right]
\\]

#### **Étape 6 : Substitution Arrière**
Résoudre de bas en haut :
- \\( 3z = 4 \Rightarrow z = \frac{4}{3} \\)
- \\( y - 0.25z = 0.5 \Rightarrow y = 0.5 + 0.25(4/3) = \frac{7}{6} \\)
- \\( x + 0.5y - 0.5z = 1.5 \Rightarrow x = 1.5 - 0.5(7/6) + 0.5(4/3) = \frac{11}{6} \\)

**Solution :**
\\[
x = \frac{11}{6}, \quad y = \frac{7}{6}, \quad z = \frac{4}{3}
\\]

---

## **3. Types de Solutions**
1. **Solution Unique** : Une seule solution pour \\( x_1, x_2, \dots \\).
2. **Infinite de Solutions** : De nombreuses solutions (le système est dépendant).
3. **Aucune Solution** : Système incohérent.

---

## **4. Systèmes Homogènes vs Non Homogènes**
- **Système homogène** : \\( A\mathbf{x} = 0 \\)
  - A toujours au moins la **solution triviale** \\( \mathbf{x} = 0 \\).
  - Peut avoir une infinité de solutions si le déterminant de \\( A \\) est nul.

- **Système non homogène** : \\( A\mathbf{x} = \mathbf{b} \\)
  - Peut avoir **une solution unique, une infinité de solutions ou aucune solution**.

---

## **Conclusion**
- L'élimination de Gauss est une méthode puissante pour résoudre des systèmes.
- Le nombre de solutions dépend du **rang** de la matrice.
- Les systèmes homogènes ont toujours une solution triviale.

Faites-moi savoir si vous avez besoin de plus d'exemples ou d'explications ! 🚀