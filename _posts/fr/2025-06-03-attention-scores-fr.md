---
audio: false
generated: true
lang: fr
layout: post
title: Stabilisation des scores d'attention dans les transformeurs
translated: true
type: note
---

La division par la racine carrée de la dimension des clés, \\(\sqrt{d_k}\\), dans le mécanisme d'attention à produit scalaire mis à l'échelle (comme dans la formule \\(\text{Scores mis à l'échelle} = \frac{Q K^T}{\sqrt{d_k}}\\)) est un choix délibéré pour stabiliser les gradients et éviter les valeurs importantes, particulièrement dans le contexte des transformers. Voici pourquoi \\(\sqrt{d_k}\\) est utilisé au lieu de simplement \\(d_k\\) :

1.  **Variance du Produit Scalaire** :
    - Le produit scalaire \\( Q K^T \\) calcule la similarité entre les vecteurs de requête (\\( Q \\)) et de clé (\\( K \\)), où chaque vecteur a une dimension \\( d_k \\). Si les éléments de \\( Q \\) et \\( K \\) sont supposés indépendants et ont une moyenne de 0 et une variance de 1 (ce qui est courant après une initialisation ou une normalisation), le produit scalaire \\( Q_i \cdot K_j \\) (pour une seule paire de vecteurs requête et clé) a une variance de \\( d_k \\). Ceci parce que la variance de la somme de \\( d_k \\) produits indépendants de deux variables normales standard s'accroît linéairement avec \\( d_k \\).
    - Sans mise à l'échelle, la magnitude de \\( Q K^T \\) augmente avec \\( d_k \\), conduisant à des valeurs très importantes pour de grandes valeurs de \\( d_k \\) (courant dans les transformers, où \\( d_k \\) peut être 64, 128, ou plus). Des valeurs importantes dans les scores d'attention peuvent causer des problèmes lorsqu'elles sont passées à travers la fonction softmax.

2.  **Stabilité du Softmax** :
    - Les scores d'attention \\( \frac{Q K^T}{\sqrt{d_k}} \\) sont introduits dans un softmax pour calculer les poids d'attention. Si les scores sont trop importants (comme ils le seraient sans mise à l'échelle ou avec une mise à l'chelle insuffisante), la fonction softmax peut produire des distributions très pointues, où un élément domine (approchant 1) et les autres sont proches de 0. Cela conduit à un vanishing gradient pour la plupart des éléments, rendant l'apprentissage du modèle difficile.
    - Diviser par \\(\sqrt{d_k}\\) assure que la variance des scores mis à l'échelle est approximativement de 1, maintenant les scores dans une plage où la fonction softmax se comporte bien, produisant des poids d'attention plus équilibrés et des gradients stables.

3.  **Pourquoi pas \\( d_k \\) ?** :
    - Diviser par \\( d_k \\) au lieu de \\(\sqrt{d_k}\\) sur-mettrait à l'échelle le produit scalaire, réduisant la variance des scores à \\( \frac{1}{d_k} \\). Pour de grandes valeurs de \\( d_k \\), cela rendrait les scores très petits, amenant le softmax à produire des distributions presque uniformes (car de petites entrées dans un softmax donnent des sorties proches de \\( \frac{1}{n} \\)). Cela diluerait la capacité du mécanisme d'attention à se concentrer sur les clés pertinentes, car les différences entre les scores seraient diminuées.
    - Une sur-mise à l'échelle avec \\( d_k \\) pourrait aussi conduire à une instabilité numérique dans certains cas, car des valeurs très petites pourraient être plus difficiles à gérer avec précision en arithmétique à virgule flottante.

4.  **Pourquoi \\(\sqrt{d_k}\\) ?** :
    - Diviser par \\(\sqrt{d_k}\\) normalise la variance du produit scalaire à approximativement 1, car \\( \text{Var}\left(\frac{Q K^T}{\sqrt{d_k}}\right) = \frac{\text{Var}(Q K^T)}{d_k} = \frac{d_k}{d_k} = 1 \\). Cela maintient les scores dans une plage raisonnable, assurant que le softmax produit des poids d'attention significatifs sans être excessivement pointus ou uniformes.
    - La racine carrée découle naturellement de la propriété mathématique de la variance du produit scalaire. Elle trouve un équilibre entre la prévention des valeurs explosives (qui se produiraient sans mise à l'échelle) et l'évitement d'une suppression excessive des scores (qui se produirait avec \\( d_k \\)).

5.  **Efficacité Empirique** :
    - Le choix de \\(\sqrt{d_k}\\) a été introduit dans l'article original du Transformer ("Attention is All You Need" par Vaswani et al., 2017) et a été validé empiriquement à travers de nombreux modèles basés sur les transformers. Il fonctionne bien en pratique pour un large éventail de valeurs de \\( d_k \\), assurant un entraînement stable et de bonnes performances.

En résumé, diviser par \\(\sqrt{d_k}\\) est un choix mathématiquement motivé qui stabilise la variance des scores d'attention, assure que le softmax opère dans un régime bien comporté, et évite les problèmes de gradients explosives ou de vanishing gradient. Diviser par \\( d_k \\) réduirait excessivement les scores, conduisant à des poids d'attention moins discriminants et potentiellement nuisant aux performances du modèle.