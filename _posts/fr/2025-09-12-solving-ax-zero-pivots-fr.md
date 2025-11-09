---
audio: false
date: 2025-09-12
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Résolution de Ax Égal à Zéro Variables Pivots
translated: true
type: note
---

Cette vidéo est **Leçon 7** du cours **18.06 Linear Algebra* du MIT (Printemps 2005)**, enseigné par **le Professeur Gilbert Strang**. Le sujet est :

### **"Résoudre \\( A\mathbf{x} = \mathbf{0} \\) : Variables Pivots et Solutions Spéciales"**

---

### **Concepts Clés Couverts dans la Leçon :**
1. **Systèmes Homogènes (\\( A\mathbf{x} = \mathbf{0} \\))**
   - Un système d'équations linéaires où le membre de droite est le vecteur zéro.
   - A toujours au moins la **solution triviale** \\( \mathbf{x} = \mathbf{0} \\).
   - S'il y a des **variables libres**, il y a une infinité de solutions.

2. **Variables Pivots vs Variables Libres**
   - **Variables pivots** : Correspondent aux colonnes avec des pivots (premiers coefficients non nuls) dans la **forme échelonnée réduite (RREF)** de \\( A \\).
   - **Variables libres** : Correspondent aux colonnes **sans pivots** (peuvent prendre n'importe quelle valeur).
   - Le nombre de variables libres = nombre de colonnes − rang de \\( A \\).

3. **Solutions Spéciales (Base de l'Espace Nul)**
   - Pour chaque variable libre, on lui attribue la valeur **1** et aux autres **0**, puis on résout pour les variables pivots.
   - Ces solutions forment une **base** pour l'**espace nul** de \\( A \\) (toutes les solutions de \\( A\mathbf{x} = \mathbf{0} \\)).
   - L'espace nul est un **sous-espace vectoriel** de \\( \mathbb{R}^n \\).

4. **Rang et Espace Nul**
   - Si \\( A \\) est une matrice \\( m \times n \\) de rang \\( r \\) :
     - Nombre de variables pivots = \\( r \\).
     - Nombre de variables libres = \\( n - r \\).
     - Dimension de l'espace nul = \\( n - r \\).

5. **Exemple Détaillé**
   - Strang traite un exemple (probablement une matrice avec un rang < nombre de colonnes) pour illustrer :
     - La recherche de la RREF.
     - L'identification des variables pivots et libres.
     - La construction des solutions spéciales.
     - L'expression de la solution générale comme une combinaison linéaire des solutions spéciales.

6. **Interprétation Géométrique**
   - L'espace nul représente tous les vecteurs \\( \mathbf{x} \\) qui sont "annulés" (envoyés sur zéro) lorsqu'ils sont multipliés par \\( A \\).
   - Pour une matrice 3×3 de rang 2, l'espace nul est une **ligne** passant par l'origine.

---

### **Pourquoi Cette Leçon est Importante :**
- Introduit l'**espace nul** (un sous-espace fondamental en algèbre linéaire).
- Fait le lien entre la **réduction de lignes (élimination)** et la structure des solutions.
- Jette les bases pour la compréhension de l'**indépendance linéaire**, des **bases** et de la **dimension** dans les leçons suivantes.
- Essentielle pour résoudre des systèmes, comprendre les transformations et pour des applications comme les **équations différentielles** ou le **machine learning**.

---
### **Où Trouver Plus d'Informations :**
- **Matériel complet du cours** : [MIT OCW 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- **Manuel** : *"Introduction to Linear Algebra"* de Strang (le Chapitre 2 couvre ce sujet).
- **Leçons suivantes** : Les prochaines leçons discutent de la **résolution de \\( A\mathbf{x} = \mathbf{b} \\)** (systèmes non homogènes) et de l'**espace colonne**.

---
### **Résumé en Une Phrase :**
Cette leçon enseigne comment trouver **toutes les solutions** de \\( A\mathbf{x} = \mathbf{0} \\) en identifiant les variables pivots/libres et en construisant une base pour l'espace nul à l'aide de solutions spéciales.