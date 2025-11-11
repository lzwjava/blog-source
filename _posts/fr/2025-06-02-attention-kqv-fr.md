---
audio: false
generated: true
lang: fr
layout: post
title: Mécanisme K, Q, V dans les Transformers
translated: true
type: note
---

Le mécanisme **Clé (K), Requête (Q) et Valeur (V)** est un composant fondamental du mécanisme d'**auto-attention** dans les grands modèles de langage (LLM) basés sur l'architecture Transformer. Ce mécanisme, introduit dans l'article fondateur *"Attention is All You Need"* (Vaswani et al., 2017), permet aux modèles de pondérer l'importance des différents mots d'une séquence lors du traitement ou de la génération de texte. Ci-dessous, je présente une introduction complète sur le fonctionnement du mécanisme **K, Q, V** dans le contexte des Transformers pour LLM, couvrant son intuition, sa formulation mathématique, son implémentation dans l'auto-attention et son rôle dans l'architecture globale.

---

### 1. **Intuition derrière K, Q, V dans l'Auto-Attention**
Le mécanisme d'auto-attention permet à un modèle Transformer de traiter une séquence d'entrée en se concentrant sur les parties pertinentes de la séquence pour chaque mot (ou token). Les composants **K, Q, V** sont les éléments de base de ce processus, permettant au modèle de déterminer dynamiquement quelles parties de l'entrée sont les plus pertinentes les unes par rapport aux autres.

- **Requête (Q) :** Représente la "question" qu'un token pose aux autres tokens de la séquence. Pour chaque token, le vecteur requête encode les informations que le token recherche dans le reste de la séquence.
- **Clé (K) :** Représente la "description" de chaque token dans la séquence. Le vecteur clé encode les informations qu'un token peut fournir aux autres.
- **Valeur (V) :** Représente le contenu réel ou l'information portée par un token. Une fois que le modèle a déterminé quels tokens sont pertinents (via les interactions Q et K), il récupère les vecteurs valeur correspondants pour construire la sortie.

L'interaction entre **Q** et **K** détermine l'attention que chaque token doit porter à tous les autres tokens, et les vecteurs **V** sont ensuite pondérés et combinés sur la base de cette attention pour produire la sortie de chaque token.

Imaginez cela comme une recherche en bibliothèque :
- **Requête** : Votre requête de recherche (par exemple, "apprentissage automatique").
- **Clé** : Les titres ou les métadonnées des livres de la bibliothèque, que vous comparez à votre requête pour trouver les livres pertinents.
- **Valeur** : Le contenu réel des livres que vous récupérez après avoir identifié les pertinents.

---

### 2. **Fonctionnement de K, Q, V dans l'Auto-Attention**
Le mécanisme d'auto-attention calcule une somme pondérée des vecteurs **Valeur**, où les poids sont déterminés par la similarité entre les vecteurs **Requête** et **Clé**. Voici un détail étape par étape du processus :

#### Étape 1 : Représentation de l'Entrée
- L'entrée d'une couche Transformer est une séquence de tokens (par exemple, des mots ou sous-mots), chacun représenté par un vecteur de plongement de haute dimension (par exemple, de dimension \\( d_{\text{model}} = 512 \\)).
- Pour une séquence de \\( n \\) tokens, l'entrée est une matrice \\( X \in \mathbb{R}^{n \times d_{\text{model}}} \\), où chaque ligne est le plongement d'un token.

#### Étape 2 : Transformations Linéaires pour Générer K, Q, V
- Pour chaque token, trois vecteurs sont calculés : **Requête (Q)**, **Clé (K)**, et **Valeur (V)**. Ils sont obtenus en appliquant des transformations linéaires apprises aux plongements d'entrée :
  \\[
  Q = X W_Q, \quad K = X W_K, \quad V = X W_V
  \\]
  - \\( W_Q, W_K, W_V \in \mathbb{R}^{d_{\text{model}} \times d_k} \\) sont des matrices de poids appris.
  - Typiquement, \\( d_k = d_v \\), et elles sont souvent définies à \\( d_{\text{model}} / h \\) (où \\( h \\) est le nombre de têtes d'attention, expliqué plus tard).
  - Le résultat est :
    - \\( Q \in \mathbb{R}^{n \times d_k} \\) : Matrice Requête pour tous les tokens.
    - \\( K \in \mathbb{R}^{n \times d_k} \\) : Matrice Clé pour tous les tokens.
    - \\( V \in \mathbb{R}^{n \times d_v} \\) : Matrice Valeur pour tous les tokens.

#### Étape 3 : Calcul des Scores d'Attention
- Le mécanisme d'attention calcule combien chaque token doit prêter attention à tous les autres tokens en calculant le **produit scalaire** entre le vecteur requête d'un token et les vecteurs clé de tous les tokens :
  \\[
  \text{Scores d'Attention} = Q K^T
  \\]
  - Cela produit une matrice \\( \in \mathbb{R}^{n \times n} \\), où chaque entrée \\( (i, j) \\) représente la similarité non normalisée entre la requête du token \\( i \\) et la clé du token \\( j \\).
- Pour stabiliser les gradients et éviter les valeurs importantes, les scores sont mis à l'échelle par la racine carrée de la dimension des clés :
  \\[
  \text{Scores Mis à l'Échelle} = \frac{Q K^T}{\sqrt{d_k}}
  \\]
  - C'est ce qu'on appelle l'**attention à produit scalaire mis à l'échelle**.

#### Étape 4 : Application de Softmax pour Obtenir les Poids d'Attention
- Les scores mis à l'échelle sont passés dans une fonction **softmax** pour les convertir en probabilités (poids d'attention) dont la somme est égale à 1 pour chaque token :
  \\[
  \text{Poids d'Attention} = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right)
  \\]
  - Le résultat est une matrice \\( \in \mathbb{R}^{n \times n} \\), où chaque ligne représente la distribution d'attention d'un token sur tous les tokens de la séquence.
  - Des poids d'attention élevés indiquent que les tokens correspondants sont très pertinents les uns pour les autres.

#### Étape 5 : Calcul de la Sortie
- Les poids d'attention sont utilisés pour calculer une somme pondérée des vecteurs **Valeur** :
  \\[
  \text{Sortie de l'Attention} = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V
  \\]
  - La sortie est une matrice \\( \in \mathbb{R}^{n \times d_v} \\), où chaque ligne est une nouvelle représentation d'un token, incorporant des informations de tous les autres tokens en fonction de leur pertinence.

#### Étape 6 : Attention Multi-Têtes
- En pratique, les Transformers utilisent une **attention multi-têtes**, où le processus ci-dessus est exécuté plusieurs fois en parallèle (avec des \\( W_Q, W_K, W_V \\) différents) pour capturer différents types de relations :
  - L'entrée est divisée en \\( h \\) têtes, chacune avec des vecteurs \\( Q, K, V \\) plus petits de dimension \\( d_k = d_{\text{model}} / h \\).
  - Chaque tête calcule sa propre sortie d'attention.
  - Les sorties de toutes les têtes sont concaténées et passées through une transformation linéaire finale :
    \\[
    \text{MultiHead}(Q, K, V) = \text{Concat}(\text{tête}_1, \text{tête}_2, \dots, \text{tête}_h) W_O
    \\]
    où \\( W_O \in \mathbb{R}^{h \cdot d_v \times d_{\text{model}}} \\) est une matrice de projection de sortie apprise.

---

### 3. **Rôle de K, Q, V dans les LLM de type Transformer**
Le mécanisme **K, Q, V** est utilisé dans différentes parties de l'architecture Transformer, selon le type d'attention :

- **Auto-Attention dans l'Encodeur (par exemple, BERT) :**
  - Tous les tokens prêtent attention à tous les autres tokens de la séquence d'entrée (attention bidirectionnelle).
  - \\( Q, K, V \\) sont tous dérivés de la même séquence d'entrée \\( X \\).
  - Cela permet au modèle de capturer le contexte des tokens précédents et suivants, ce qui est utile pour des tâches comme la classification de texte ou la réponse aux questions.

- **Auto-Attention dans le Décodeur (par exemple, GPT) :**
  - Dans les modèles autorégressifs comme GPT, le décodeur utilise une **auto-attention masquée** pour éviter de prêter attention aux tokens futurs (puisque le modèle génère du texte séquentiellement).
  - Le masque assure que pour chaque token \\( i \\), les scores d'attention pour les tokens \\( j > i \\) sont fixés à \\(-\infty\\) avant le softmax, leur donnant effectivement un poids nul.
  - \\( Q, K, V \\) sont toujours dérivés de la séquence d'entrée, mais l'attention est causale (ne prête attention qu'aux tokens précédents).

- **Attention Croisée dans les Modèles Encodeur-Décodeur (par exemple, T5) :**
  - Dans les architectures encodeur-décodeur, le décodeur utilise l'attention croisée pour prêter attention à la sortie de l'encodeur.
  - Ici, \\( Q \\) est dérivé de l'entrée du décodeur, tandis que \\( K \\) et \\( V \\) proviennent de la sortie de l'encodeur, permettant au décodeur de se concentrer sur les parties pertinentes de la séquence d'entrée lors de la génération de la sortie.

---

### 4. **Pourquoi K, Q, V Fonctionnent si Bien**
Le mécanisme **K, Q, V** est puissant pour plusieurs raisons :
- **Contextualisation Dynamique** : Il permet à chaque token de collecter des informations d'autres tokens en fonction de leur contenu, plutôt que de s'appuyer sur des motifs fixes (par exemple, comme dans les RNN ou les CNN).
- **Parallélisation** : Contrairement aux réseaux de neurones récurrents, l'auto-attention traite tous les tokens simultanément, la rendant très efficace sur le matériel moderne comme les GPU.
- **Flexibilité** : L'attention multi-têtes permet au modèle de capturer des relations diverses (par exemple, syntaxiques, sémantiques) en apprenant différentes projections pour \\( Q, K, V \\).
- **Évolutivité** : Le mécanisme s'adapte bien aux longues séquences (bien que le coût computationnel croisse quadratiquement avec la longueur de la séquence, atténué par des techniques comme l'attention clairsemée ou les Transformers efficaces).

---

### 5. **Résumé Mathématique**
La formule de l'attention à produit scalaire mis à l'échelle est :
\\[
\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V
\\]
Pour l'attention multi-têtes :
\\[
\text{MultiHead}(Q, K, V) = \text{Concat}(\text{tête}_1, \dots, \text{tête}_h) W_O
\\]
où :
\\[
\text{tête}_i = \text{Attention}(Q W_{Q_i}, K W_{K_i}, V W_{V_i})
\\]

---

### 6. **Exemple Pratique**
Prenons la phrase : *"Le chat s'est assis sur le tapis."*
- **Entrée** : Chaque mot est converti en un vecteur de plongement (par exemple, via une couche de plongement de mots).
- **Calcul de Q, K, V** : Pour chaque token, le modèle calcule les vecteurs requête, clé et valeur en utilisant des poids appris.
- **Scores d'Attention** : Pour le mot "chat", le vecteur requête pourrait attribuer des scores d'attention élevés à "assis" et "tapis" car ils sont contextuellement pertinents, tout en donnant des scores plus faibles à "le".
- **Sortie** : Le mécanisme d'attention produit une nouvelle représentation pour "chat" qui incorpore des informations de "assis" et "tapis", pondérées par leurs scores d'attention.

---

### 7. **Extensions et Optimisations**
- **Attention Efficace** : Pour gérer les longues séquences, des variantes comme Performer, Linformer ou Longformer réduisent la complexité computationnelle de l'attention.
- **Encodages Positionnels** : Puisque l'auto-attention est permutation-invariante, les Transformers ajoutent des encodages positionnels aux plongements d'entrée pour capturer l'ordre des mots, ce qui influence indirectement \\( Q, K, V \\).
- **Empilement de Couches** : Les Transformers empilent plusieurs couches d'auto-attention, permettant à \\( Q, K, V \\) d'opérer sur des représentations de plus en plus abstraites.

---

### 8. **Conclusion**
Le mécanisme **K, Q, V** est au cœur de l'auto-attention du Transformer, permettant aux LLM de modéliser efficacement des relations complexes dans le texte. En calculant des scores d'attention basés sur des requêtes et des clés, et en agrégeant des informations à partir de vecteurs valeur, les Transformers atteignent des performances de pointe dans des tâches comme la modélisation du langage, la traduction, et plus encore. Comprendre ce mécanisme est essentiel pour saisir comment les LLM modernes traitent et génèrent un texte semblable à celui d'un humain.

Si vous souhaitez approfondir un aspect spécifique (par exemple, l'attention multi-têtes, l'implémentation en code, ou les applications dans des modèles spécifiques), faites-le moi savoir !