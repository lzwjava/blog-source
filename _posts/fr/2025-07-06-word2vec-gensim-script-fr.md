---
audio: false
generated: true
lang: fr
layout: post
title: Script Word2Vec avec Gensim
translated: true
type: note
---

Pour vous fournir un script Python pour Word2Vec, je dois faire quelques hypothèses sur ce que vous recherchez, car "un script sur Word2Vec" peut être assez large. Je vais fournir deux scénarios courants :

1.  **Un script simple utilisant `gensim` pour l'entraînement et l'utilisation de base :** C'est la manière la plus courante et pratique d'utiliser Word2Vec en Python.
2.  **Une implémentation conceptuelle très basique à partir de zéro :** Celle-ci est plus pour comprendre les algorithmes de base, mais moins pratique pour une utilisation réelle en raison de la complexité et des besoins en optimisation.

Compte tenu de votre demande, je vais privilégier l'approche `gensim` car c'est ce que la plupart des gens utilisent.

-----

### Script Python pour Word2Vec utilisant `gensim`

Ce script va démontrer :

  * La préparation de données textuelles d'exemple.
  * L'entraînement d'un modèle Word2Vec.
  * La recherche des mots les plus similaires.
  * L'exécution d'analogies de mots.
  * La sauvegarde et le chargement du modèle.

**Prérequis :**

Vous devez installer la bibliothèque `gensim` :

```bash
pip install gensim
```

**Script Python (`word2vec_gensim_example.py`) :**

```python
import gensim
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import logging

# Configurer la journalisation pour voir la progression de l'entraînement
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# --- 1. Préparer les données textuelles d'exemple ---
# Dans un scénario réel, vous chargeriez vos données textuelles à partir de fichiers.
# Ici, nous utilisons une simple liste de phrases.
raw_sentences = [
    "I love natural language processing.",
    "Word embeddings are a fascinating topic.",
    "Machine learning revolutionizes many industries.",
    "Deep learning is a subset of machine learning.",
    "Natural language processing uses various techniques.",
    "Computers understand human language better with word vectors.",
    "The quick brown fox jumps over the lazy dog.",
    "Dog and cat are common pets.",
    "King is to Queen as Man is to Woman."
]

# Prétraiter les phrases : tokeniser et convertir en minuscules
# simple_preprocess de gensim est pratique pour cela
tokenized_sentences = [simple_preprocess(sentence) for sentence in raw_sentences]

print("\n--- Phrases Tokenisées ---")
for sentence in tokenized_sentences:
    print(sentence)

# --- 2. Entraîner le modèle Word2Vec ---
# Paramètres expliqués :
#   vector_size : Dimensionnalité des vecteurs de mots.
#   window : Distance maximale entre le mot courant et le mot prédit dans une phrase.
#   min_count : Ignore tous les mots dont la fréquence totale est inférieure à cette valeur.
#   sg : Algorithme d'entraînement : 0 pour CBOW, 1 pour Skip-gram. Skip-gram est généralement meilleur pour les mots rares.
#   workers : Utilise ce nombre de threads de travail pour entraîner le modèle (= entraînement plus rapide).
#   epochs : Nombre d'itérations (époques) sur le corpus.
model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=100,      # Exemple : vecteurs de 100 dimensions
    window=5,             # Fenêtre contextuelle de 5 mots de chaque côté
    min_count=1,          # Inclure tous les mots (pour ce petit exemple)
    sg=1,                 # Utiliser Skip-gram (sg=1)
    workers=4,            # Utiliser 4 cœurs CPU pour l'entraînement
    epochs=10             # Entraîner pendant 10 époques
)

print("\n--- Entraînement du modèle terminé ---")

# --- 3. Explorer le modèle ---

# Obtenir le vecteur pour un mot spécifique
try:
    word_vector = model.wv['machine']
    print(f"\nVecteur pour 'machine' (10 premières dimensions) : {word_vector[:10]}")
    print(f"Forme du vecteur pour 'machine' : {word_vector.shape}")
except KeyError:
    print("\n'machine' non trouvé dans le vocabulaire.")

# Trouver les mots les plus similaires
print("\n--- Mots les plus similaires à 'machine' ---")
try:
    similar_words = model.wv.most_similar('machine')
    for word, similarity in similar_words:
        print(f"{word} : {similarity:.4f}")
except KeyError:
    print("\n'machine' non trouvé dans le vocabulaire.")

print("\n--- Mots les plus similaires à 'dog' ---")
try:
    similar_words_dog = model.wv.most_similar('dog')
    for word, similarity in similar_words_dog:
        print(f"{word} : {similarity:.4f}")
except KeyError:
    print("\n'dog' non trouvé dans le vocabulaire.")


# Effectuer des analogies de mots (ex: King - Man + Woman = Queen)
# Cela peut ne pas fonctionner parfaitement avec de très petits jeux de données, mais démontre le concept.
print("\n--- Analogies de mots (King - Man + Woman = ?) ---")
try:
    result = model.wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
    if result:
        print(f"King - Man + Woman est similaire à : {result[0][0]} (similarité : {result[0][1]:.4f})")
    else:
        print("Aucun résultat pour l'analogie. Le vocabulaire est peut-être trop petit.")
except KeyError as e:
    print(f"Un ou plusieurs mots pour l'analogie non trouvés dans le vocabulaire : {e}")
except Exception as e:
    print(f"Une erreur est survenue lors de l'analogie : {e}")

# Vérifier la similarité entre deux mots
print("\n--- Similarité entre 'machine' et 'learning' ---")
try:
    similarity = model.wv.similarity('machine', 'learning')
    print(f"Similarité : {similarity:.4f}")
except KeyError:
    print("Un ou les deux mots non trouvés dans le vocabulaire.")

print("\n--- Similarité entre 'dog' et 'cat' ---")
try:
    similarity_pets = model.wv.similarity('dog', 'cat')
    print(f"Similarité : {similarity_pets:.4f}")
except KeyError:
    print("Un ou les deux mots non trouvés dans le vocabulaire.")

print("\n--- Similarité entre 'dog' et 'computer' ---")
try:
    similarity_diff = model.wv.similarity('dog', 'computer')
    print(f"Similarité : {similarity_diff:.4f}")
except KeyError:
    print("Un ou les deux mots non trouvés dans le vocabulaire.")

# --- 4. Sauvegarder et Charger le Modèle ---
model_path = "word2vec_model.bin"
model.save(model_path)
print(f"\nModèle sauvegardé dans {model_path}")

# Charger le modèle
loaded_model = Word2Vec.load(model_path)
print(f"Modèle chargé depuis {model_path}")

# Vérifier le modèle chargé
print("\n--- Vérifier le Modèle Chargé (Mots les plus similaires à 'machine' en utilisant le modèle chargé) ---")
try:
    similar_words_loaded = loaded_model.wv.most_similar('machine')
    for word, similarity in similar_words_loaded:
        print(f"{word} : {similarity:.4f}")
except KeyError:
    print("\n'machine' non trouvé dans le vocabulaire du modèle chargé.")

print("\nExécution du script terminée.")
```

**Comment exécuter le script :**

1.  Sauvegardez le code ci-dessus dans un fichier Python (par exemple, `word2vec_gensim_example.py`).
2.  Ouvrez votre terminal ou invite de commande.
3.  Naviguez jusqu'au répertoire où vous avez sauvegardé le fichier.
4.  Exécutez le script en utilisant : `python word2vec_gensim_example.py`

-----

### Concepts Clés dans Word2Vec (implémentation `gensim`)

  * **`gensim.models.Word2Vec`** : La classe principale pour l'entraînement.
  * **`sentences`** : Un itérable d'itérables, où l'itérable externe est le corpus et les itérables internes sont des listes de mots (phrases tokenisées).
  * **`vector_size`** : Le nombre de dimensions pour les vecteurs de mots. Des dimensions plus élevées peuvent capturer plus de nuances mais nécessitent plus de données et de calcul.
  * **`window`** : La distance maximale entre le mot courant et les mots qui l'entourent dans une phrase.
  * **`min_count`** : Les mots qui apparaissent moins de fois que `min_count` sont ignorés. Cela aide à filtrer les mots très rares qui pourraient ne pas avoir d'embeddings significatifs.
  * **`sg` (Skip-gram vs. CBOW)** :
      * `sg=0` (CBOW - Continuous Bag of Words) : Prédit le mot courant en fonction de son contexte. Plus rapide à entraîner.
      * `sg=1` (Skip-gram) : Prédit les mots environnants étant donné le mot courant. Généralement plus performant pour les mots rares.
  * **`workers`** : Nombre de cœurs CPU à utiliser pour l'entraînement, accélérant le processus.
  * **`epochs`** : Nombre de fois que l'algorithme itère sur l'ensemble du jeu de données. Plus d'époques peuvent conduire à des embeddings de meilleure qualité mais prennent aussi plus de temps.
  * **`model.wv`** : L'objet "word vectors" (`KeyedVectors`) qui contient les embeddings de mots entraînés et des méthodes comme `most_similar`, `similarity`, etc. Vous pouvez également accéder aux vecteurs directement comme `model.wv['word']`.

-----

Ce script `gensim` fournit une base solide pour travailler avec Word2Vec. Pour des applications réelles, vous utiliseriez typiquement un corpus beaucoup plus grand (par exemple, Wikipedia, Common Crawl) et ajusteriez les hyperparamètres pour une performance optimale.