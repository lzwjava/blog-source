---
audio: false
generated: true
lang: fr
layout: post
title: Déterminant d'une matrice
translated: true
type: note
---

Si le **déterminant de la matrice \\( A \\) est nul**, le système **peut** avoir une infinité de solutions car cela indique que la matrice est **singulière** (non inversible), ce qui signifie que ses lignes ou colonnes sont linéairement dépendantes. Explorons pourquoi cela conduit à une infinité de solutions.

---

## **1. Déterminant et Rang**
- Le **déterminant d'une matrice carrée \\( A \\)** nous indique si la matrice est inversible.
  - Si \\( \det(A) \neq 0 \\), la matrice est **inversible** et le système a une **solution unique**.
  - Si \\( \det(A) = 0 \\), la matrice est **singulière** (non inversible), ce qui signifie que le système n'a **aucune solution ou une infinité de solutions**.

- Le **rang** d'une matrice est le nombre de **lignes** ou de **colonnes linéairement indépendantes**.
  - Si le nombre de lignes non nulles (le rang) est **inférieur au nombre de variables**, nous obtenons des **variables libres**, conduisant à une **infinité de solutions**.

---

## **2. Pourquoi une infinité de solutions ?**
### **Cas : Système homogène \\( A\mathbf{x} = 0 \\)**
- Un système homogène a toujours la **solution triviale** \\( \mathbf{x} = 0 \\).
- Si \\( \det(A) = 0 \\), cela signifie qu'au moins une ligne dépend d'une autre.
- Cela signifie qu'il existe au moins **une variable libre**, permettant un nombre infini de solutions.

**Exemple :**  
\\[
\begin{aligned}
x + y + z &= 0 \\
2x + 2y + 2z &= 0
\end{aligned}
\\]
- La deuxième équation est simplement le **double** de la première → **une seule équation indépendante**.
- Nous avons **trois variables mais une seule équation indépendante**, donc nous avons des **variables libres** → une infinité de solutions.

---

### **Cas : Système non homogène \\( A\mathbf{x} = \mathbf{b} \\)**
- Si \\( \det(A) = 0 \\), le système est **soit incohérent (aucune solution) soit a une infinité de solutions**.
- Le système a une **infinité de solutions** lorsque le nombre d'équations indépendantes est **inférieur au nombre de variables**.

**Exemple :**  
\\[
\begin{aligned}
x + y + z &= 5 \\
2x + 2y + 2z &= 10
\end{aligned}
\\]
- La deuxième équation est simplement le **double** de la première.
- Une équation indépendante avec **trois variables** → **une infinité de solutions** (forme de solution paramétrique).

---

## **Conclusion**
- Si \\( \det(A) = 0 \\), au moins une ligne est dépendante, ce qui signifie que nous avons des **variables libres**.
- Les variables libres permettent un **nombre infini de solutions** à la fois dans les cas homogènes et certains cas non homogènes.
- Si \\( A \\) est singulière et que le système est incohérent (par exemple, des équations contradictoires comme \\( x + y = 2 \\) et \\( x + y = 3 \\)), il n'y a **aucune solution** au lieu d'une infinité de solutions.

N'hésitez pas à demander des clarifications supplémentaires ! 🚀