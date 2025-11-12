---
audio: false
generated: true
lang: fr
layout: post
title: Processus de Gram-Schmidt
translated: true
type: note
---

Le **processus de Gram-Schmidt** est une méthode en algèbre linéaire utilisée pour convertir un ensemble de vecteurs linéairement indépendants en un ensemble orthonormal de vecteurs qui engendrent le même sous-espace. Ceci est particulièrement utile dans diverses applications telles que la décomposition QR, la résolution de problèmes des moindres carrés et la simplification des calculs dans les espaces vectoriels.

### **Concepts Clés**

- **Vecteurs Linéairement Indépendants** : Vecteurs qui ne peuvent pas être exprimés comme une combinaison linéaire les uns des autres.
- **Vecteurs Orthogonaux** : Vecteurs qui sont perpendiculaires les uns aux autres, ce qui signifie que leur produit scalaire est nul.
- **Ensemble Orthonormal** : Un ensemble de vecteurs qui sont à la fois orthogonaux et de norme unitaire (norme égale à 1).

### **Objectif du Processus de Gram-Schmidt**

- **Orthogonalisation** : Transformer un ensemble de vecteurs en un ensemble où chaque vecteur est orthogonal aux autres.
- **Normalisation** : Ajuster la longueur de chaque vecteur pour en faire un vecteur unitaire.
- **Simplification** : Faciliter les calculs dans les projections, les décompositions et les transformations au sein des espaces vectoriels.

### **Le Processus Expliqué**

Étant donné un ensemble de vecteurs linéairement indépendants \\( \{ \mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \} \\) dans un espace préhilbertien (comme \\( \mathbb{R}^n \\)), le processus de Gram-Schmidt construit un ensemble orthonormal \\( \{ \mathbf{q}_1, \mathbf{q}_2, \ldots, \mathbf{q}_n \} \\) en suivant ces étapes :

1. **Initialiser le Premier Vecteur** :
   \\[
   \mathbf{u}_1 = \mathbf{v}_1
   \\]
   Normaliser pour obtenir :
   \\[
   \mathbf{q}_1 = \frac{\mathbf{u}_1}{\| \mathbf{u}_1 \|}
   \\]

2. **Orthogonalisation et Normalisation Itératives** pour \\( k = 2 \\) à \\( n \\) :
   - **Orthogonaliser** :
     \\[
     \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} \text{proj}_{\mathbf{q}_j} \mathbf{v}_k
     \\]
     où la projection \\( \text{proj}_{\mathbf{q}_j} \mathbf{v}_k \\) est calculée comme :
     \\[
     \text{proj}_{\mathbf{q}_j} \mathbf{v}_k = (\mathbf{v}_k \cdot \mathbf{q}_j) \mathbf{q}_j
     \\]
   - **Normaliser** :
     \\[
     \mathbf{q}_k = \frac{\mathbf{u}_k}{\| \mathbf{u}_k \|}
     \\]

### **Étapes Détaillées**

1. **Calculer \\( \mathbf{u}_1 \\) et \\( \mathbf{q}_1 \\)** :
   - \\( \mathbf{u}_1 = \mathbf{v}_1 \\)
   - \\( \mathbf{q}_1 = \frac{\mathbf{u}_1}{\| \mathbf{u}_1 \|} \\)

2. **Pour chaque vecteur suivant \\( \mathbf{v}_k \\)** :
   - **Soustraire les projections sur tous les \\( \mathbf{q}_j \\) précédents** :
     \\[
     \mathbf{u}_k = \mathbf{v}_k - \sum_{j=1}^{k-1} (\mathbf{v}_k \cdot \mathbf{q}_j) \mathbf{q}_j
     \\]
   - **Normaliser \\( \mathbf{u}_k \\) pour obtenir \\( \mathbf{q}_k \\)** :
     \\[
     \mathbf{q}_k = \frac{\mathbf{u}_k}{\| \mathbf{u}_k \|}
     \\]

### **Exemple**

Appliquons le processus de Gram-Schmidt aux vecteurs \\( \mathbf{v}_1 = [1, 1] \\) et \\( \mathbf{v}_2 = [1, 0] \\) dans \\( \mathbb{R}^2 \\).

1. **Premier Vecteur** :
   - \\( \mathbf{u}_1 = \mathbf{v}_1 = [1, 1] \\)
   - Normaliser :
     \\[
     \| \mathbf{u}_1 \| = \sqrt{1^2 + 1^2} = \sqrt{2}
     \\]
     \\[
     \mathbf{q}_1 = \frac{[1, 1]}{\sqrt{2}} = \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right]
     \\]

2. **Deuxième Vecteur** :
   - Calculer la projection de \\( \mathbf{v}_2 \\) sur \\( \mathbf{q}_1 \\) :
     \\[
     \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = (\mathbf{v}_2 \cdot \mathbf{q}_1) \mathbf{q}_1
     \\]
     \\[
     \mathbf{v}_2 \cdot \mathbf{q}_1 = [1, 0] \cdot \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right] = \frac{1}{\sqrt{2}}
     \\]
     \\[
     \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = \frac{1}{\sqrt{2}} \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right] = \left[ \frac{1}{2}, \frac{1}{2} \right]
     \\]
   - Soustraire la projection :
     \\[
     \mathbf{u}_2 = \mathbf{v}_2 - \text{proj}_{\mathbf{q}_1} \mathbf{v}_2 = [1, 0] - \left[ \frac{1}{2}, \frac{1}{2} \right] = \left[ \frac{1}{2}, -\frac{1}{2} \right]
     \\]
   - Normaliser \\( \mathbf{u}_2 \\) :
     \\[
     \| \mathbf{u}_2 \| = \sqrt{\left( \frac{1}{2} \right)^2 + \left( -\frac{1}{2} \right)^2} = \frac{1}{\sqrt{2}}
     \\]
     \\[
     \mathbf{q}_2 = \frac{\left[ \frac{1}{2}, -\frac{1}{2} \right]}{\frac{1}{\sqrt{2}}} = \left[ \frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right]
     \\]

### **Résultat**

L'ensemble orthonormal est :
\\[
\mathbf{q}_1 = \left[ \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right], \quad \mathbf{q}_2 = \left[ \frac{\sqrt{2}}{2}, -\frac{\sqrt{2}}{2} \right]
\\]

Ces vecteurs sont orthogonaux (\\( \mathbf{q}_1 \cdot \mathbf{q}_2 = 0 \\)) et de norme unitaire (\\( \| \mathbf{q}_1 \| = \| \mathbf{q}_2 \| = 1 \\)).

### **Applications**

- **Décomposition QR** : Décomposer une matrice en une matrice orthogonale \\( Q \\) et une matrice triangulaire supérieure \\( R \\).
- **Problèmes des Moindres Carrés** : Trouver la solution d'approximation optimale pour des systèmes surdéterminés.
- **Méthodes Numériques** : Améliorer la stabilité et l'efficacité des algorithmes de calcul.

### **Résumé**

Le processus de Gram-Schmidt est une méthode systématique pour orthonormaliser un ensemble de vecteurs dans un espace préhilbertien, garantissant que le nouvel ensemble est plus facile à manipuler tout en préservant l'espace engendré par les vecteurs originaux. Il est fondamental en algèbre linéaire et a de vastes applications en mathématiques, en physique et en ingénierie.