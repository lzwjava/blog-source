---
audio: false
generated: true
lang: fr
layout: post
title: Similarité Cosinus
translated: true
type: note
---

La similarité cosinus est une métrique largement utilisée en machine learning pour mesurer la similarité entre deux vecteurs dans un espace de haute dimension. Elle est particulièrement populaire dans des domaines comme le traitement du langage naturel (NLP), la recherche d'information et les systèmes de recommandation en raison de sa capacité à capturer l'orientation (ou l'angle) entre les vecteurs, plutôt que leur magnitude. Cela la rend robuste pour comparer des objets comme des documents texte, des préférences utilisateur ou des embeddings, où la direction du vecteur importe plus que sa longueur.

### Qu'est-ce que la similarité cosinus ?

La similarité cosinus quantifie à quel point deux vecteurs sont similaires en calculant le cosinus de l'angle entre eux. Mathématiquement, elle est définie comme :

\\[
\text{Similarité Cosinus} = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|}
\\]

Où :
- \\( A \\) et \\( B \\) sont deux vecteurs (par exemple, représentant des documents, des embeddings ou des ensembles de caractéristiques).
- \\( A \cdot B \\) est le produit scalaire des vecteurs, calculé comme \\( \sum_{i=1}^n A_i B_i \\).
- \\( \|A\| \\) et \\( \|B\| \\) sont les normes euclidiennes (magnitudes) des vecteurs \\( A \\) et \\( B \\), calculées respectivement comme \\( \sqrt{\sum_{i=1}^n A_i^2} \\) et \\( \sqrt{\sum_{i=1}^n B_i^2} \\).
- \\( \theta \\) est l'angle entre les vecteurs.

Le résultat varie entre :
- **1** : Les vecteurs sont identiques en direction (angle = 0°).
- **0** : Les vecteurs sont orthogonaux (angle = 90°), indiquant aucune similarité.
- **-1** : Les vecteurs sont opposés (angle = 180°), indiquant une dissimilarité maximale.

### Propriétés clés

1. **Plage** : Les valeurs de similarité cosinus se situent entre -1 et 1, ce qui les rend faciles à interpréter.
2. **Indépendance de la magnitude** : Puisque les vecteurs sont normalisés par leurs magnitudes, la similarité cosinus se concentre sur la direction, et non sur la longueur. Ceci est utile pour comparer des documents de longueurs différentes ou des embeddings avec des échelles variables.
3. **Caractéristiques non négatives** : Dans de nombreuses applications (par exemple, les données texte avec des fréquences de termes), les vecteurs ont des composantes non négatives, donc la similarité varie généralement entre 0 et 1.
4. **Efficacité computationnelle** : Les calculs du produit scalaire et de la norme sont simples, ce qui rend la similarité cosinus efficace sur le plan computationnel pour les données de haute dimension.

### Comment elle est utilisée en Machine Learning

La similarité cosinus est appliquée à diverses tâches de machine learning en raison de sa polyvalence :

1. **Analyse de texte et NLP** :
   - **Similarité de documents** : Dans des tâches comme le clustering ou les moteurs de recherche, les documents sont représentés comme des vecteurs (par exemple, TF-IDF ou des embeddings comme Word2Vec, GloVe ou BERT). La similarité cosinus mesure à quel point deux documents sont similaires en fonction de leur contenu.
   - **Analyse de sentiment** : Comparaison des vecteurs de sentiment d'extraits de texte.
   - **Détection de plagiat** : Identification des similarités entre les textes en comparant leurs représentations vectorielles.

2. **Systèmes de recommandation** :
   - La similarité cosinus est utilisée pour comparer des profils d'utilisateurs ou d'articles (par exemple, dans le filtrage collaboratif). Par exemple, elle peut mesurer à quel point les préférences de deux utilisateurs sont similaires en fonction de leurs évaluations ou comportements.
   - Elle est efficace dans le filtrage basé sur le contenu, où les articles (par exemple, films, produits) sont représentés comme des vecteurs de caractéristiques.

3. **Traitement d'images et audio** :
   - En vision par ordinateur, la similarité cosinus compare les vecteurs de caractéristiques extraits d'images (par exemple, à partir de CNN) pour mesurer la similarité visuelle.
   - En traitement audio, elle est utilisée pour comparer des spectrogrammes ou des embeddings d'extraits sonores.

4. **Clustering et Classification** :
   - Dans les algorithmes de clustering (par exemple, K-means avec des données texte), la similarité cosinus sert de métrique de distance pour regrouper des éléments similaires.
   - Dans les tâches de classification, elle est utilisée pour comparer les vecteurs d'entrée aux prototypes de classe.

5. **Détection d'anomalies** :
   - La similarité cosinus peut identifier les valeurs aberrantes en comparant les points de données à un centroïde ou à un motif attendu. Une faible similarité indique des anomalies potentielles.

### Exemple : Similarité cosinus dans l'analyse de texte

Supposons que nous ayons deux documents représentés comme des vecteurs TF-IDF :
- Document 1 : \\( A = [2, 1, 0, 3] \\) (par exemple, fréquences de mots pour quatre termes).
- Document 2 : \\( B = [1, 1, 1, 0] \\).

**Étape 1 : Calculer le produit scalaire** :
\\[
A \cdot B = (2 \cdot 1) + (1 \cdot 1) + (0 \cdot 1) + (3 \cdot 0) = 2 + 1 + 0 + 0 = 3
\\]

**Étape 2 : Calculer les normes** :
\\[
\|A\| = \sqrt{2^2 + 1^2 + 0^2 + 3^2} = \sqrt{4 + 1 + 0 + 9} = \sqrt{14} \approx 3.742
\\]
\\[
\|B\| = \sqrt{1^2 + 1^2 + 1^2 + 0^2} = \sqrt{1 + 1 + 1 + 0} = \sqrt{3} \approx 1.732
\\]

**Étape 3 : Calculer la similarité cosinus** :
\\[
\cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|} = \frac{3}{3.742 \cdot 1.732} \approx \frac{3}{6.483} \approx 0.462
\\]

La similarité cosinus est d'environ 0,462, indiquant une similarité modérée entre les documents.

### Avantages de la similarité cosinus

- **Invariance à l'échelle** : Elle n'est pas affectée par la magnitude des vecteurs, ce qui la rend idéale pour les données texte où la longueur des documents varie.
- **Gère les données de haute dimension** : Efficace dans les espaces de haute dimension et clairsemés (par exemple, les données texte avec des milliers de caractéristiques).
- **Interprétation intuitive** : La valeur du cosinus est directement liée à l'angle, fournissant une mesure claire de la similarité.

### Limitations

- **Ignore la magnitude** : Dans certains cas, les différences de magnitude sont importantes (par exemple, lors de la comparaison de quantités absolues).
- **Suppose des relations linéaires** : La similarité cosinus suppose que la similarité est mieux capturée par la distance angulaire, ce qui n'est pas toujours vrai.
- **Sensibilité aux données clairsemées** : Dans les vecteurs très clairsemés, la similarité cosinus peut être moins discriminante, car de nombreuses dimensions contribuent peu au produit scalaire.

### Similarité cosinus vs autres métriques

- **Distance euclidienne** : Mesure la distance en ligne droite et est sensible à la magnitude, contrairement à la similarité cosinus. Le cosinus est préféré lorsque la direction importe plus que les différences absolues.
- **Similarité de Jaccard** : Utilisée pour les ensembles (par exemple, données binaires), se concentrant sur les éléments partagés plutôt que sur l'orientation des vecteurs.
- **Corrélation de Pearson** : Mesure la corrélation linéaire, en tenant compte des données centrées sur la moyenne, tandis que la similarité cosinus fonctionne sur des vecteurs bruts.

### Implémentation pratique

La similarité cosinus est implémentée dans de nombreuses bibliothèques de machine learning :
- **Python** : `scikit-learn` fournit `cosine_similarity` dans `sklearn.metrics.pairwise`.
  ```python
  from sklearn.metrics.pairwise import cosine_similarity
  import numpy as np

  A = np.array([[2, 1, 0, 3]])
  B = np.array([[1, 1, 1, 0]])
  similarity = cosine_similarity(A, B)
  print(similarity)  # Output: [[0.46225063]]
  ```
- **TensorFlow/PyTorch** : Utilisé pour comparer des embeddings dans les modèles de deep learning.
- **Spark** : Pour les calculs de similarité distribués à grande échelle.

### Applications avancées

1. **Word Embeddings** : La similarité cosinus est la norme pour comparer les embeddings de mots ou de phrases (par exemple, BERT, Sentence-BERT) afin de mesurer la similarité sémantique.
2. **Modèles basés sur les graphes** : Utilisée dans la similarité des nœuds pour les réseaux de neurones de graphes.
3. **Recherche personnalisée** : Les moteurs de recherche comme Elasticsearch utilisent la similarité cosinus pour classer les documents par pertinence par rapport à une requête.

### Conclusion

La similarité cosinus est une métrique puissante, intuitive et efficace sur le plan computationnel pour mesurer la similarité en machine learning. Son accent sur l'orientation des vecteurs la rend idéale pour le texte, les embeddings et les systèmes de recommandation, bien qu'elle soit moins adaptée aux tâches où la magnitude est importante. En comprenant ses forces et ses limites, les praticiens peuvent l'appliquer efficacement à diverses applications, du NLP à la vision par ordinateur. Si vous souhaitez une exploration plus approfondie d'un cas d'utilisation ou d'une implémentation spécifique, faites-le moi savoir !