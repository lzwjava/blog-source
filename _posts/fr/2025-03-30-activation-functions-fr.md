---
audio: false
generated: true
lang: fr
layout: post
title: Fonctions d'activation dans les réseaux de neurones
translated: true
type: note
---

Les fonctions **sigmoid**, **ReLU** et **Leaky ReLU** sont toutes des fonctions d'activation utilisées dans les réseaux de neurones. Chacune d'elles possède des caractéristiques uniques et est adaptée à différentes tâches selon le type de problème à résoudre. Voici une analyse de leurs différences :

### 1. **Sigmoid** :
   - **Formule** :  
     \\[
     \sigma(x) = \frac{1}{1 + e^{-x}}
     \\]
   - **Plage** : (0, 1)
   - **Avantages** :
     - Un gradient doux, ce qui aide à l'optimisation.
     - La sortie est bornée entre 0 et 1, ce qui la rend utile pour les probabilités ou la classification binaire.
   - **Inconvénients** :
     - **Problème de gradient qui s'évanouit** : Pour des valeurs d'entrée très grandes ou très petites, le gradient devient très petit (presque nul), ce qui peut ralentir l'entraînement, en particulier dans les réseaux profonds.
     - Les sorties ne sont pas centrées sur zéro, ce qui peut entraîner des problèmes lorsque les mises à jour du gradient sont dominées par une seule direction.
   - **Cas d'usage** : Souvent utilisée dans la couche de sortie pour les tâches de classification binaire (par exemple, dans la régression logistique).

### 2. **ReLU (Rectified Linear Unit)** :
   - **Formule** :  
     \\[
     f(x) = \max(0, x)
     \\]
   - **Plage** : [0, ∞)
   - **Avantages** :
     - **Rapide et simple** : Facile à calculer et efficace en pratique.
     - Résout le problème du gradient qui s'évanouit en permettant une bonne propagation des gradients.
     - Encourage la parcimonie (de nombreux neurones peuvent devenir inactifs).
   - **Inconvénients** :
     - **Problème du "ReLU mort"** : Les neurones peuvent "mourir" pendant l'entraînement si leur sortie est toujours nulle (c'est-à-dire pour les entrées négatives). Cela peut amener certains neurones à ne plus jamais s'activer.
   - **Cas d'usage** : Très couramment utilisée dans les couches cachées des réseaux profonds, en particulier dans les réseaux de neurones convolutifs et profonds.

### 3. **Leaky ReLU** :
   - **Formule** :  
     \\[
     f(x) = \max(\alpha x, x)
     \\]
     Où \\( \alpha \\) est une petite constante (par exemple, 0,01).
   - **Plage** : (-∞, ∞)
   - **Avantages** :
     - Empêche le **problème du "ReLU mort"** en autorisant une petite pente négative pour les valeurs négatives de \\( x \\).
     - Comme ReLU, elle aide à résoudre le problème du gradient qui s'évanouit et encourage la parcimonie.
   - **Inconvénients** :
     - Peut toujours produire des sorties négatives, mais c'est beaucoup moins problématique qu'avec la ReLU standard.
     - Le choix de \\( \alpha \\) peut être délicat et nécessite parfois un réglage.
   - **Cas d'usage** : Utilisée dans de nombreux modèles de deep learning pour éviter les problèmes liés à ReLU, en particulier dans les réseaux où le problème du "ReLU mort" pourrait survenir.

---

### **Résumé comparatif** :

- **Sigmoid** :  
  Idéale pour les couches de sortie dans les tâches de classification binaire, mais souffre du problème du gradient qui s'évanouit.
  
- **ReLU** :  
  Une bonne fonction d'activation polyvalente pour les couches cachées. Elle accélère l'entraînement et fonctionne bien pour les grands réseaux, mais peut souffrir du problème des neurones morts.

- **Leaky ReLU** :  
  Une modification de ReLU qui résout le problème du "ReLU mort" en autorisant un petit gradient non nul pour les entrées négatives. Elle est largement utilisée pour les modèles plus profonds.

### **En pratique** :
- **Sigmoid** est souvent utilisée lorsque la sortie doit être dans la plage (0, 1), comme dans la couche finale des tâches de classification binaire.
- **ReLU** est souvent le choix par défaut pour les couches cachées en raison de sa simplicité et de sa capacité à bien gérer les gradients qui s'évanouissent.
- **Leaky ReLU** est utilisée à la place de ReLU lorsqu'il y a des inquiétudes concernant la "mort" des neurones pendant l'entraînement.

Chacune de ces fonctions d'activation a sa place en fonction de la structure et des objectifs du réseau de neurones que vous construisez !