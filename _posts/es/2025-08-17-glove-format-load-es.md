---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Formato y Carga de GloVe
translated: true
type: note
---

Los vectores GloVe son archivos de texto plano. Cada línea es un token seguido de sus valores de embedding, todos separados por espacios. **No hay cabecera** (a diferencia de muchos archivos de texto word2vec).

Ejemplo (GloVe 300-d):

```
the 0.418 0.24968 -0.41242 0.1217 ... 0.34527   # 300 floats en total
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982  0.25344 ... 0.024118
```

Algunas notas prácticas:

* Lanzamientos comunes:

  * `glove.6B.{50,100,200,300}d.txt` (Wikipedia + Gigaword; \~400k vocabulario, minúsculas).
  * `glove.840B.300d.txt` (Common Crawl; \~2.2M vocabulario).
  * `glove.twitter.27B.{25,50,100,200}d.txt` (Twitter; muchos hashtags/emoticonos).
* Los tokens nunca contienen espacios (las frases usan guiones bajos), por lo que un simple `line.split()` es suficiente.
* Los floats están en ASCII; verás decimales regulares y a veces notación científica.
* No hay una fila especial `<unk>`; el manejo de OOV depende de ti.

Tu cargador

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

coincide con ese formato. Dos pequeñas mejoras que podrías querer:

1. Usar float32 para reducir la memoria a la mitad:

```python
vec = np.asarray(line[1:], dtype=np.float32)
```

2. Omitir "cabeceras" accidentales o líneas incorrectas (algunos archivos reempaquetados añaden una):

```python
parts = line.rstrip().split(' ')
if len(parts) < 2: 
    continue
if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
    # parece una cabecera al estilo word2vec: "<vocab> <dim>"
    continue
word, *vals = parts
```

### Construyendo una matriz de embedding para tu vocabulario

Después de crear tu `dictionary: word -> id`, asigna las filas de GloVe a una matriz de pesos para tu `nn.Embedding`:

```python
def build_embedding_matrix(dictionary, glove_path, dim=300, dtype=np.float32):
    _, glove = read_glove_vecs(glove_path)  # como arriba, pero dtype=float32
    V = len(dictionary)
    W = np.random.uniform(-0.05, 0.05, (V, dim)).astype(dtype)
    for w, idx in dictionary.items():
        vec = glove.get(w)
        if vec is not None and vec.shape[0] == dim:
            W[idx] = vec
    return torch.tensor(W)

# uso
# emb_weight = build_embedding_matrix(dictionary, "glove.6B.300d.txt", dim=300)
# model.in_embeddings.weight.data.copy_(emb_weight)
```

### Contraste rápido con word2vec texto/binario

* **GloVe texto**: sin cabecera, `word float float ...`
* **word2vec texto**: a menudo comienza con una cabecera `"<vocab> <dim>"`.
* **word2vec binario**: cabecera + floats binarios.

Si alguna vez necesitas usar herramientas que esperan el formato word2vec, convierte con `gensim.scripts.glove2word2vec`.