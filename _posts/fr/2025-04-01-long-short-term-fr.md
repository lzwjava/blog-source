---
audio: false
generated: true
lang: fr
layout: post
title: Réseaux à mémoire à long court terme
translated: true
type: note
---

Les réseaux de mémoire à long terme (LSTM) sont un type d'architecture de réseau neuronal récurrent conçue spécifiquement pour résoudre le problème du gradient qui disparaît et permettre l'apprentissage de dépendances à long terme dans les données séquentielles. Ils y parviennent grâce à une structure interne plus sophistiquée appelée **cellule LSTM**.

Voici une explication du fonctionnement d'une cellule LSTM :

**Idée centrale : L'état de la cellule**

Le concept central d'un LSTM est l'**état de la cellule** (souvent noté 'C<sub>t</sub>'). Considérez l'état de la cellule comme un tapis roulant qui traverse toute la séquence. Il transporte les informations pertinentes pour l'historique à long terme de la séquence. Les informations peuvent être ajoutées à ou supprimées de l'état de la cellule au fur et à mesure de son flux dans le réseau via des structures appelées **portes**.

**Les portes**

Les cellules LSTM ont trois portes principales qui régulent le flux d'informations :

1.  **Porte d'oubli :** Cette porte décide quelles informations de l'état de cellule précédent doivent être supprimées.
    * Elle reçoit l'état caché précédent (h<sub>t-1</sub>) et l'entrée actuelle (x<sub>t</sub>).
    * Ceux-ci sont transmis à une couche de réseau neuronal suivie d'une **fonction d'activation sigmoïde**.
    * La fonction sigmoïde produit des valeurs comprises entre 0 et 1. Une valeur proche de 0 signifie "oublier complètement cette information", tandis qu'une valeur proche de 1 signifie "conserver complètement cette information".
    * Mathématiquement, la sortie de la porte d'oubli (f<sub>t</sub>) est calculée comme suit :
        ```
        f_t = σ(W_f * [h_{t-1}, x_t] + b_f)
        ```
        où :
        * σ est la fonction sigmoïde.
        * W<sub>f</sub> est la matrice de poids pour la porte d'oubli.
        * [h<sub>t-1</sub>, x_t] est la concaténation de l'état caché précédent et de l'entrée actuelle.
        * b<sub>f</sub> est le vecteur de biais pour la porte d'oubli.

2.  **Porte d'entrée :** Cette porte décide quelles nouvelles informations de l'entrée actuelle doivent être ajoutées à l'état de la cellule. Ce processus implique deux étapes :
    * **Couche de la porte d'entrée :** Une couche sigmoïde décide quelles valeurs nous allons mettre à jour.
        ```
        i_t = σ(W_i * [h_{t-1}, x_t] + b_i)
        ```
        où :
        * σ est la fonction sigmoïde.
        * W<sub>i</sub> est la matrice de poids pour la porte d'entrée.
        * [h<sub>t-1</sub>, x_t] est la concaténation de l'état caché précédent et de l'entrée actuelle.
        * b<sub>i</sub> est le vecteur de biais pour la porte d'entrée.
    * **Couche des valeurs candidates :** Une couche tanh crée un vecteur de nouvelles valeurs candidates (état de cellule candidat, noté 'C̃<sub>t</sub>') qui pourraient être ajoutées à l'état de la cellule. La fonction tanh produit des valeurs entre -1 et 1, ce qui aide à réguler le réseau.
        ```
        C̃_t = tanh(W_C * [h_{t-1}, x_t] + b_C)
        ```
        où :
        * tanh est la fonction tangente hyperbolique.
        * W<sub>C</sub> est la matrice de poids pour l'état de cellule candidat.
        * [h<sub>t-1</sub>, x_t] est la concaténation de l'état caché précédent et de l'entrée actuelle.
        * b<sub>C</sub> est le vecteur de biais pour l'état de cellule candidat.

3.  **Porte de sortie :** Cette porte décide quelles informations de l'état de cellule actuel doivent être sorties en tant qu'état caché pour le pas de temps actuel.
    * Elle reçoit l'état caché précédent (h<sub>t-1</sub>) et l'entrée actuelle (x<sub>t</sub>).
    * Ceux-ci sont transmis à une couche de réseau neuronal suivie d'une **fonction d'activation sigmoïde** pour déterminer quelles parties de l'état de cellule doivent être sorties.
        ```
        o_t = σ(W_o * [h_{t-1}, x_t] + b_o)
        ```
        où :
        * σ est la fonction sigmoïde.
        * W<sub>o</sub> est la matrice de poids pour la porte de sortie.
        * [h<sub>t-1</sub>, x_t] est la concaténation de l'état caché précédent et de l'entrée actuelle.
        * b<sub>o</sub> est le vecteur de biais pour la porte de sortie.
    * L'état de la cellule est ensuite passé à travers une **fonction tanh** pour ramener les valeurs entre -1 et 1.
    * Enfin, la sortie de la porte sigmoïde est multipliée élément par élément par la sortie de la fonction tanh appliquée à l'état de la cellule. Cela devient le nouvel état caché (h<sub>t</sub>) qui est transmis au pas de temps suivant et peut également être utilisé pour faire des prédictions.
        ```
        h_t = o_t * tanh(C_t)
        ```

**Mise à jour de l'état de la cellule**

L'état de la cellule est mis à jour en fonction des décisions prises par les portes d'oubli et d'entrée :

```
C_t = f_t * C_{t-1} + i_t * C̃_t
```

* La porte d'oubli (f<sub>t</sub>) détermine la quantité de l'état de cellule précédent (C<sub>t-1</sub>) à conserver. Si f<sub>t</sub> est proche de 0, l'information est principalement oubliée. Si elle est proche de 1, l'information est principalement conservée.
* La porte d'entrée (i<sub>t</sub>) détermine la quantité des nouvelles valeurs candidates (C̃<sub>t</sub>) qui doit être ajoutée à l'état de la cellule. Si i<sub>t</sub> est proche de 0, la nouvelle information est principalement ignorée. Si elle est proche de 1, la nouvelle information est principalement ajoutée.

**Comment les LSTM résolvent le problème du gradient qui disparaît :**

La clé de la capacité des LSTM à gérer les dépendances à long terme réside dans l'état de la cellule et les mécanismes de gating. L'état de la cellule agit comme une voie directe pour que l'information circule sur de nombreux pas de temps sans être multipliée de manière répétée par des poids, ce qui est la cause principale des gradients qui disparaissent dans les RNN traditionnels.

Les portes permettent au LSTM d'apprendre quand stocker, accéder et oublier des informations dans l'état de la cellule. Ce mécanisme de mémoire sélective permet au réseau de conserver les informations pertinentes sur de longues séquences et de les utiliser lorsque cela est nécessaire, atténuant efficacement le problème du gradient qui disparaît et permettant l'apprentissage de dépendances à long terme.

En essence, les LSTM offrent un moyen pour le réseau de maintenir une "mémoire" sur de longues périodes, ce qui les rend très efficaces pour les tâches impliquant des données séquentielles avec des dépendances à long terme.