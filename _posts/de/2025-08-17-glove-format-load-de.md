---
audio: false
generated: true
image: false
lang: de
layout: post
title: GloVe-Format und Ladeführer
translated: true
type: note
---

GloVe-Vektoren sind reine Textdateien. Jede Zeile besteht aus einem Token, gefolgt von seinen Embedding-Werten, alle durch Leerzeichen getrennt. Es gibt **keine Kopfzeile** (im Gegensatz zu vielen word2vec-Textdateien).

Beispiel (300-d GloVe):

```
the 0.418 0.24968 -0.41242 0.1217 ... 0.34527   # 300 floats insgesamt
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982  0.25344 ... 0.024118
```

Einige praktische Hinweise:

* Gängige Veröffentlichungen:

  * `glove.6B.{50,100,200,300}d.txt` (Wikipedia + Gigaword; \~400k Vokabular, Kleinbuchstaben).
  * `glove.840B.300d.txt` (Common Crawl; \~2.2M Vokabular).
  * `glove.twitter.27B.{25,50,100,200}d.txt` (Twitter; viele Hashtags/Emoticons).
* Token enthalten niemals Leerzeichen (Phrasen verwenden Unterstriche), daher ist ein einfaches `line.split()` ausreichend.
* Floats sind im ASCII-Format; man sieht reguläre Dezimalzahlen und manchmal wissenschaftliche Schreibweise.
* Es gibt keine spezielle `<unk>`-Zeile; die Behandlung unbekannter Wörter (OOV) liegt bei Ihnen.

Ihr Loader

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

entspricht diesem Format. Zwei kleine Verbesserungen, die Sie möglicherweise wünschen:

1. Verwenden Sie float32, um den Speicherbedarf zu halbieren:

```python
vec = np.asarray(line[1:], dtype=np.float32)
```

2. Überspringen Sie versehentliche "Kopfzeilen" oder fehlerhafte Zeilen (manche neu verpackte Dateien fügen eine hinzu):

```python
parts = line.rstrip().split(' ')
if len(parts) < 2: 
    continue
if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
    # sieht aus wie eine word2vec-artige Kopfzeile: "<vocab> <dim>"
    continue
word, *vals = parts
```

### Aufbau einer Embedding-Matrix für Ihren Vokabular

Nachdem Sie ein `dictionary: word -> id` erstellt haben, ordnen Sie die GloVe-Zeilen einer Gewichtsmatrix für Ihr `nn.Embedding` zu:

```python
def build_embedding_matrix(dictionary, glove_path, dim=300, dtype=np.float32):
    _, glove = read_glove_vecs(glove_path)  # wie oben, aber dtype=float32
    V = len(dictionary)
    W = np.random.uniform(-0.05, 0.05, (V, dim)).astype(dtype)
    for w, idx in dictionary.items():
        vec = glove.get(w)
        if vec is not None and vec.shape[0] == dim:
            W[idx] = vec
    return torch.tensor(W)

# Verwendung
# emb_weight = build_embedding_matrix(dictionary, "glove.6B.300d.txt", dim=300)
# model.in_embeddings.weight.data.copy_(emb_weight)
```

### Schneller Vergleich mit word2vec Text/Binär

* **GloVe Text**: keine Kopfzeile, `word float float ...`
* **word2vec Text**: beginnt oft mit `"<vocab> <dim>"` Kopfzeile.
* **word2vec Binär**: Kopfzeile + binäre Floats.

Falls Sie jemals Werkzeuge verwenden müssen, die das word2vec-Format erwarten, konvertieren Sie mit `gensim.scripts.glove2word2vec`.