---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Charger les vecteurs GloVe de deux manières
translated: true
type: note
---

Vous avez deux méthodes simples pour obtenir les vecteurs GloVe pour des mots comme `the`, `to`, `U.S.` et pour votre propre texte :

---

## Option A — Télécharger Stanford GloVe et effectuer des recherches avec `gensim`

C'est la méthode la plus courante et elle fonctionne entièrement hors ligne une fois téléchargée.

```python
# 1) Télécharger & dézipper (première exécution uniquement)
import os, zipfile, urllib.request
url = "https://nlp.stanford.edu/data/glove.6B.zip"
zip_path = "glove.6B.zip"
if not os.path.exists(zip_path):
    urllib.request.urlretrieve(url, zip_path)
with zipfile.ZipFile(zip_path) as zf:
    zf.extract("glove.6B.300d.txt")  # jeu de données 300-dim

# 2) Convertir le format GloVe -> format texte word2vec et charger
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

glove_path = "glove.6B.300d.txt"
w2v_path   = "glove.6B.300d.w2v.txt"
if not os.path.exists(w2v_path):
    glove2word2vec(glove_path, w2v_path)

vectors = KeyedVectors.load_word2vec_format(w2v_path, binary=False)
print(vectors.vector_size)  # 300

# 3) Recherches de mots uniques
print(vectors['the'][:5])   # 5 premières dimensions
print(vectors['to'][:5])

# NOTE : Le vocabulaire de glove.6B est en minuscules.
# 'U.S.' -> 'u.s.' dans ce vocab (si présent). Plus sûr : mettre vos tokens en minuscules.
print(vectors['u.s.'][:5])
```

Maintenant, intégrez votre propre texte :

```python
import re, numpy as np

# tokeniseur simple qui conserve les points dans les tokens comme u.s.
TOKEN_RE = re.compile(r"[A-Za-z0-9\.\-']+")

def tokenize(text: str):
    return TOKEN_RE.findall(text.lower())

def embed_tokens(tokens, kv: KeyedVectors):
    vecs = [kv[w] for w in tokens if w in kv.key_to_index]
    return np.stack(vecs) if vecs else np.zeros((0, kv.vector_size))

def embed_sentence_avg(text: str, kv: KeyedVectors):
    V = embed_tokens(tokenize(text), kv)
    return V.mean(axis=0) if V.size else np.zeros(kv.vector_size)

# Exemples
print(embed_sentence_avg("The quick brown fox jumps over the lazy dog.", vectors)[:10])
print(embed_tokens(tokenize("U.S. interest rates rose today."), vectors).shape)  # (n_tokens, 300)
```

**Conseils**

* `glove.6B.300d.txt` ≈ 1.1 Go en mémoire. Si c'est trop lourd, essayez `100d` à la place.
* Le jeu de données 6B est en **minuscules** ; mettez toujours votre texte en minuscules, ou utilisez le jeu de données **840B** plus grand si vous avez besoin d'une meilleure couverture (en pratique, il est aussi largement en minuscules).
* Les mots OOV (hors vocabulaire) ne renvoient rien ; vous pouvez les ignorer ou utiliser des heuristiques de sous-mots.

---

## Option B — Laisser `torchtext` télécharger et servir GloVe pour vous

Cela évite le téléchargement et la conversion manuels.

```python
import torch
from torchtext.vocab import GloVe
import re

glove = GloVe(name="6B", dim=300)  # télécharge automatiquement dans ~/.vector_cache
stoi = glove.stoi    # mot -> index
vecs = glove.vectors # tenseur [vocab, 300]

def get_word_vec(word: str):
    idx = stoi.get(word.lower())
    return vecs[idx] if idx is not None else None

print(get_word_vec("the")[:5])
print(get_word_vec("to")[:5])
print(get_word_vec("U.S.")[:5])     # devient None dans beaucoup de builds ; essayez "u.s." :
print(get_word_vec("u.s.")[:5])

# Intégration de phrase (moyenne)
TOKEN_RE = re.compile(r"[A-Za-z0-9\.\-']+")
def embed_sentence_avg(text: str):
    toks = TOKEN_RE.findall(text.lower())
    xs = [get_word_vec(t) for t in toks]
    xs = [x for x in xs if x is not None]
    return torch.stack(xs, dim=0).mean(0) if xs else torch.zeros(glove.dim)

print(embed_sentence_avg("The quick brown fox...")[:10])
```

---

## Ce que vous avez demandé concernant les lignes spécifiques

Ces lignes comme :

```
the  0.418 0.24968 -0.41242 0.1217 ... 0.34527  # 300 floats au total
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982 0.25344 ... 0.024118
```

sont exactement ce que vous verrez dans les fichiers texte `.txt` : chaque ligne est `token` suivi de `300` floats. Avec `gensim` ou `torchtext`, vous n'avez pas besoin d'analyser les lignes vous-même—ils s'en chargent et vous donnent un accès direct aux vecteurs.

---

## Pièges courants (et correctifs)

* **“KeyError: ‘U.S.’”** → Utilisez `u.s.` avec le jeu de données 6B, ou choisissez un jeu de données plus grand avec une meilleure couverture, et mettez toujours en minuscules avant la recherche.
* **Mémoire/temps énorme** → Utilisez `100d` ou `200d` au lieu de `300d`, ou chargez uniquement les mots nécessaires en parcourant le fichier et en construisant un vocabulaire plus petit.
* **Vecteurs de Phrase/Document** → Faites la moyenne ou la somme des vecteurs de mots ; pour une moyenne pondérée, essayez les poids TF-IDF.

Si vous le souhaitez, dites-moi votre objectif exact de traitement de texte (classification, similarité, clustering, etc.) et je vous proposerai un pipeline minimal utilisant GloVe de bout en bout.