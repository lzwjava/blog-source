---
audio: false
generated: true
image: false
lang: fr
layout: post
model: google/gemini-3-pro-preview
title: Opérations sur les lignes et modifications du déterminant
translated: true
type: note
---

C'est une excellente question ! Abordons les opérations élémentaires sur les lignes et leur effet sur le déterminant.

## 📐 Atteindre la forme échelonnée (REF)

Vous avez raison, **l'échange de lignes**, **la multiplication d'une ligne par un scalaire** et **l'ajout d'un multiple d'une ligne à une autre** sont les trois opérations élémentaires sur les lignes utilisées pour obtenir la **forme échelonnée (REF)**.

---

## 🛑 Effet des opérations sur les lignes sur le déterminant

Votre affirmation selon laquelle le déterminant d'une matrice **ne change pas** pendant ces opérations est **partiellement incorrecte**. Seule une des trois opérations élémentaires sur les lignes laisse le déterminant inchangé :

### 1. Ajouter un multiple d'une ligne à une autre

* **Opération :** \\(R_i \leftarrow R_i + c R_j\\)
* **Effet sur le Déterminant :** Le déterminant **NE CHANGE PAS**.
    * Si \\(\det(A) = d\\), alors \\(\det(A') = d\\).
    * **Exemple :** \\(\det \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = -2\\). \\(\det \begin{pmatrix} 1 & 2 \\ 3-2(1) & 4-2(2) \end{pmatrix} = \det \begin{pmatrix} 1 & 2 \\ 1 & 0 \end{pmatrix} = -2\\).

### 2. Multiplier une ligne par un scalaire non nul

* **Opération :** \\(R_i \leftarrow c R_i\\) (où \\(c \ne 0\\))
* **Effet sur le Déterminant :** Le déterminant est multiplié par le scalaire \\(c\\).
    * Si \\(\det(A) = d\\), alors \\(\det(A') = c \cdot d\\).
    * **Exemple :** \\(\det \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = -2\\). \\(\det \begin{pmatrix} 1 & 2 \\ 3(2) & 4(2) \end{pmatrix} = \det \begin{pmatrix} 1 & 2 \\ 6 & 8 \end{pmatrix} = 8-12 = -4\\). Ici, \\(c=2\\), et le nouveau déterminant est \\(2 \cdot (-2) = -4\\).

### 3. Échanger deux lignes

* **Opération :** \\(R_i \leftrightarrow R_j\\)
* **Effet sur le Déterminant :** Le déterminant est multiplié par \\(-1\\) (il change de signe).
    * Si \\(\det(A) = d\\), alors \\(\det(A') = -d\\).
    * **Exemple :** \\(\det \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = -2\\). \\(\det \begin{pmatrix} 3 & 4 \\ 1 & 2 \end{pmatrix} = 3(2) - 4(1) = 6-4 = 2\\). Ici, le signe est passé de \\(-2\\) à \\(2\\).

---

## 💡 Tableau récapitulatif

| Opération Élémentaire sur les Lignes | Notation | Effet sur le Déterminant |
| :--- | :--- | :--- |
| **Échange de lignes** | \\(R_i \leftrightarrow R_j\\) | \\(\det(A') = -\det(A)\\) |
| **Multiplication par un scalaire** | \\(R_i \leftarrow c R_i\\) | \\(\det(A') = c \cdot \det(A)\\) |
| **Addition de lignes** | \\(R_i \leftarrow R_i + c R_j\\) | \\(\det(A') = \det(A)\\) |

Si vous utilisez des opérations sur les lignes pour transformer une matrice \\(A\\) en sa forme échelonnée \\(U\\), vous pouvez trouver le déterminant original en gardant une trace des changements :

\\(\\)\det(A) = (-1)^s \cdot \frac{1}{c_1 c_2 \dots c_k} \cdot \det(U)\\(\\)

où \\(s\\) est le nombre d'échanges de lignes et \\(c_1, c_2, \dots, c_k\\) sont les scalaires utilisés dans les multiplications de lignes. Pour une matrice sous forme REF, \\(\det(U)\\) est simplement le produit de ses éléments diagonaux (puisqu'il s'agit d'une matrice triangulaire supérieure).

---

Souhaitez-vous essayer d'utiliser ces opérations sur une matrice spécifique pour trouver son déterminant ?