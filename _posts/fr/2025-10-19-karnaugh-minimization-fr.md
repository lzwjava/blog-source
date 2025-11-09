---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Exemple de minimisation par la table de Karnaugh
translated: true
type: note
---

### Exemple d'utilisation de la table de Karnaugh : Minimisation d'une fonction booléenne à 3 variables

Parcourons un exemple pratique d'utilisation d'une table de K pour simplifier une expression booléenne. Nous utiliserons une fonction à 3 variables (A, B, C) où la sortie est 1 pour les mintermes m(1, 2, 4, 7). Cela signifie :

- f(A, B, C) = A'B'C + A'BC' + AB'C' + ABC

L'objectif est de minimiser cela en le moins de termes (et de littéraux) possible, ce qui réduit le nombre de portes logiques dans un circuit.

#### Étape 1 : Construire la table de K
Une table de K à 3 variables est une grille 2x4 (ou 4x2, mais nous utiliserons les lignes pour AB et les colonnes pour C). Les lignes sont étiquetées dans l'ordre du code Gray (00, 01, 11, 10) pour garantir que les cellules adjacentes ne diffèrent que d'un seul bit. Placez des 1 dans les cellules correspondant aux mintermes :

| AB \ C | 0     | 1     |
|--------|-------|-------|
| **00** | 0     | 1 (m1) |
| **01** | 1 (m2) | 0     |
| **11** | 0     | 1 (m7) |
| **10** | 1 (m4) | 0     |

(Ici, m1 = A'B'C, m2 = A'BC', m4 = AB'C', m7 = ABC.)

#### Étape 2 : Grouper les 1 adjacents
La clé de la minimisation est de trouver les groupes les plus grands possibles (rectangles ou carrés) de 1 qui sont adjacents (y compris les bords qui se rejoignent, comme un tore). Chaque groupe doit avoir une taille qui est une puissance de 2 (1, 2, 4, 8, etc.). Les groupes peuvent se chevaucher.

- **Groupe 1** : Les deux 1 de la colonne de gauche (m2 et m4) forment une paire verticale. Ils partagent A'B'C' ? Attendez non — en analysant les bits : m2 (010) et m4 (100) ne diffèrent que par A et B, mais dans le code Gray, les lignes 01 et 10 sont adjacentes. Ce groupe couvre le changement de A, donc c'est B'C' (A est indifférent).
- **Groupe 2** : Les deux 1 de la colonne de droite (m1 et m7) forment une paire verticale qui se rejoint (les lignes 00 et 11 ne sont pas directement adjacentes, attendez — en fait pour cette table, un meilleur groupement : remarquez que m1 (001) et m2 (010) sont horizontalement adjacents en ligne 00-01 ? Attendez, corrigeons.

Attendez, re-tracé pour plus de clarté — en fait, les groupements optimaux pour cette fonction :

- Paire horizontale : m1 (ligne00 col1) et m2 (ligne01 col0) ? Non, pas adjacents.
Groupement standard pour ces mintermes :
- Quad ? Non. Paires :
  - m1 et m2 ? m1=001, m2=010 — diffèrent de deux bits, pas adjacents.
  Mieux : m2 (010) et m4 (100) — diffèrent par A et B ? 010 et 100 diffèrent par A (0 à 1) et B (1 à 0), deux bits — pas adjacents.

J'ai choisi un mauvais exemple — laissez-moi en choisir un meilleur avec des groupes clairs pour illustrer.

**Exemple révisé pour plus de clarté** : Utilisons f(A, B, C) = Σ m(0, 1, 2, 4, 5, 6) = A'B'C' + A'B'C + A'BC' + AB'C' + AB'C + ABC'

Table de K :

| AB \ C | 0     | 1     |
|--------|-------|-------|
| **00** | 1 (m0) | 1 (m1) |
| **01** | 1 (m2) | 0 (m3) |
| **11** | 1 (m6) | 0 (m7) |
| **10** | 1 (m4) | 1 (m5) |

Mintermes : 0(000),1(001),2(010),4(100),5(101),6(110)—oui m3(011)=0, m7(111)=0.

Donc le tableau :

| AB \ C | 0     | 1     |
|--------|-------|-------|
| **00** | 1     | 1     |
| **01** | 1     | 0     |
| **11** | 1     | 0     |
| **10** | 1     | 1     |

#### Étape 3 : Identifier les groupes
Maintenant, groupez les 1 :

- **Grand groupe (4 x 1)** : Toute la colonne de gauche (C=0) : m0, m2, m6, m4. Ce sont toutes les cellules où C=0, et AB varie — toutes adjacentes dans une colonne (les lignes se rejoignent). Cela couvre **C'** (puisque C est 0, A et B sont indifférents).
- **Groupe paire (2 x 1)** : En haut à droite (m0 et m1 ? m0 col0, m1 col1 — paire horizontale en ligne 00 : A'B' (C indifférent).
- Mais m1 (001) n'est pas encore couvert ? Attendez, ligne du haut : m0 et m1 sont horizontalement adjacents, couvrant A'B' (C varie).
- Aussi, en bas à droite m5 (101 col1 ligne10) — mais pour couvrir m1 et m5 ? Ils sont en col1, lignes 00 et 10, qui sont adjacentes (les bords se rejoignent), donc paire verticale en col1 : m1 et m5, couvrant AC (attendez, bits : 001 et 101 = A indifférent, B=0, C=1 ? 001 B=0 C=1, 101 A=1 B=0 C=1—oui B'C.

Pour minimiser, nous choisissons des groupes non chevauchants ou une couverture minimale qui couvre tous les 1 avec les tailles les plus grandes.

Optimal :
- Groupe 1 : 4 cellules verticales en col0 : couvre C' (tous les 1 là : m0,m2,m4,m6 → terme : C')
- Groupe 2 : 2 cellules horizontales en ligne00 : m0 et m1 → A'B'
- Groupe 3 : 2 cellules verticales qui se rejoignent en col1 lignes10 et 00 ? Attendez, les lignes 00 et 10 sont adjacentes pour col1 : m1(001) et m5(101) → ne diffèrent que par A, donc B'C (A indifférent).

m5 est couvert, m1 est couvert.

Note : m0 est à la fois dans le groupe1 et le groupe2, mais c'est OK — les chevauchements sont autorisés.

#### Étape 4 : Dériver l'expression minimisée
Chaque groupe devient un terme produit (ET des littéraux communs) :
- Groupe 1 (C') : **C'**
- Groupe 2 (A'B') : **A' B'**
- Groupe 3 (B' C) : **B' C**

Donc, SOP minimisée (Somme de Produits) : f = C' + A'B' + B'C

Vérifiez : Cela a 3 termes (contre 6 originaux), moins de littéraux (4 contre 12), circuit plus simple (en gros 3 portes ET/OU).

Vous pouvez le représenter sur une table de vérité pour confirmer qu'il correspond aux 1 originaux.

#### Pourquoi cela minimise-t-il ?
- **Règle d'adjacence** : Les groupes uniquement là où les variables changent d'un bit, garantissant que le terme ignore cette variable (indifférent = - dans la table).
- **Les plus grands d'abord** : Des groupes plus grands = moins de variables dans le terme = plus simple.
- **Couvrir tous les 1** : Aucun 1 n'est laissé de côté ; les 0 doivent rester à 0 (ne pas les grouper).
- Pour plus de variables (table de K à 4 var est 4x4), même processus, mais plus difficile visuellement.

Cet exemple montre comment les tables de K transforment une somme de mintermes en une forme compacte rapidement sans manipulation algébrique. Pour 4+ variables, utilisez un logiciel, mais pratiquer avec des exemples à 2-3 variables construit l'intuition.

[Digital Logic Design Basics](https://www.allaboutcircuits.com/textbook/digital/chpt-7/karnaugh-mapping/)