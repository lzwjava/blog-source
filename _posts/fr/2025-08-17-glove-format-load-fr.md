---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide du format GloVe et de son chargement
translated: true
type: note
---

Les vecteurs GloVe sont des fichiers en texte brut. Chaque ligne correspond à un token suivi de ses valeurs d'embedding, le tout séparé par des espaces. Il n'y a **aucun en-tête** (contrairement à de nombreux fichiers word2vec en texte).

Exemple (GloVe 300-d) :

```
the 0.418 0.24968 -0.41242 0.1217 ... 0.34527   # 300 floats au total
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982  0.25344 ... 0.024118
```

Quelques notes pratiques :

* Versions courantes :

  * `glove.6B.{50,100,200,300}d.txt` (Wikipedia + Gigaword ; \~400k vocab, minuscules).
  * `glove.840B.300d.txt` (Common Crawl ; \~2.2M vocab).
  * `glove.twitter.27B.{25,50,100,200}d.txt` (Twitter ; beaucoup de hashtags/émoticônes).
* Les tokens ne contiennent jamais d'espaces (les phrases utilisent des underscores), donc un simple `line.split()` convient.
* Les floats sont en ASCII ; vous verrez des décimales régulières et parfois la notation scientifique.
* Il n'y a pas de ligne spéciale `<unk>` ; la gestion des mots hors vocabulaire vous revient.

Votre loader

```python
def read_glove_vecs(glove_file):
    with open(glove_file, 'r', encoding='utf-8') as f:
        words = set()
        word_to_vec_map = {}
        for line in f:
            line = line.strip().split()
            curr_word = line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)
    return words, word_to_vec_map
```

correspond à ce format. Deux petites améliorations possibles :

1. Utilisez float32 pour réduire la mémoire de moitié :

```python
vec = np.asarray(line[1:], dtype=np.float32)
```

2. Ignorez les "en-têtes" accidentels ou les mauvaises lignes (certains fichiers repackagés en ajoutent un) :

```python
parts = line.rstrip().split(' ')
if len(parts) < 2: 
    continue
if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
    # ressemble à un en-tête de style word2vec : "<vocab> <dim>"
    continue
word, *vals = parts
```

### Construction d'une matrice d'embedding pour votre vocabulaire

Après avoir créé votre `dictionary: word -> id`, mappez les lignes GloVe dans une matrice de poids pour votre `nn.Embedding` :

```python
def build_embedding_matrix(dictionary, glove_path, dim=300, dtype=np.float32):
    _, glove = read_glove_vecs(glove_path)  # comme ci-dessus, mais dtype=float32
    V = len(dictionary)
    W = np.random.uniform(-0.05, 0.05, (V, dim)).astype(dtype)
    for w, idx in dictionary.items():
        vec = glove.get(w)
        if vec is not None and vec.shape[0] == dim:
            W[idx] = vec
    return torch.tensor(W)

# utilisation
# emb_weight = build_embedding_matrix(dictionary, "glove.6B.300d.txt", dim=300)
# model.in_embeddings.weight.data.copy_(emb_weight)
```

### Comparaison rapide avec word2vec texte/binaire

* **GloVe texte** : pas d'en-tête, `word float float ...`
* **word2vec texte** : commence souvent par un en-tête `"<vocab> <dim>"`.
* **word2vec binaire** : en-tête + floats binaires.

Si vous avez besoin d'utiliser des outils attendant le format word2vec, convertissez avec `gensim.scripts.glove2word2vec`.