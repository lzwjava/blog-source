---
audio: false
generated: true
image: false
lang: ja
layout: post
title: GloVeフォーマットと読み込みガイド
translated: true
type: note
---

GloVeベクトルはプレーンテキストファイルです。各行は1つのトークンとその埋め込み値が続き、すべてスペースで区切られています。**ヘッダーはありません**（多くのword2vecテキストファイルとは異なります）。

例（300次元GloVe）：

```
the 0.418 0.24968 -0.41242 0.1217 ... 0.34527   # 合計300個のfloat
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982  0.25344 ... 0.024118
```

実用的な注意点：

* 一般的なリリース：

  * `glove.6B.{50,100,200,300}d.txt`（Wikipedia + Gigaword; \~40万語彙、小文字）。
  * `glove.840B.300d.txt`（Common Crawl; \~220万語彙）。
  * `glove.twitter.27B.{25,50,100,200}d.txt`（Twitter; 多数のハッシュタグ/絵文字）。
* トークンにスペースは含まれない（フレーズはアンダースコアを使用）ので、単純な`line.split()`で問題ありません。
* 浮動小数点数はASCII形式です。通常の小数表記と、時には科学技術表記も見られます。
* 特別な`<unk>`行はありません。OOV（語彙外）処理はユーザーに委ねられています。

あなたのローダー

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

はこの形式に一致しています。必要に応じて検討したい2つの小さな改良点：

1. メモリを半分に削減するためにfloat32を使用：

```python
vec = np.asarray(line[1:], dtype=np.float32)
```

2. 誤った「ヘッダー」や不正な行をスキップ（一部の再パッケージ化ファイルでは追加されることがあります）：

```python
parts = line.rstrip().split(' ')
if len(parts) < 2: 
    continue
if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
    # word2vec形式のヘッダーに見える: "<語彙数> <次元数>"
    continue
word, *vals = parts
```

### 語彙に対する埋め込み行列の構築

`dictionary: word -> id`を作成した後、GloVeの行を`nn.Embedding`用の重み行列にマッピングします：

```python
def build_embedding_matrix(dictionary, glove_path, dim=300, dtype=np.float32):
    _, glove = read_glove_vecs(glove_path)  # 上記と同じ、ただしdtype=float32
    V = len(dictionary)
    W = np.random.uniform(-0.05, 0.05, (V, dim)).astype(dtype)
    for w, idx in dictionary.items():
        vec = glove.get(w)
        if vec is not None and vec.shape[0] == dim:
            W[idx] = vec
    return torch.tensor(W)

# 使用例
# emb_weight = build_embedding_matrix(dictionary, "glove.6B.300d.txt", dim=300)
# model.in_embeddings.weight.data.copy_(emb_weight)
```

### word2vecテキスト/バイナリ形式との簡単な比較

* **GloVeテキスト**: ヘッダーなし、`word float float ...`
* **word2vecテキスト**: 多くの場合、`"<語彙数> <次元数>"`ヘッダーで始まる。
* **word2vecバイナリ**: ヘッダー + バイナリ浮動小数点数。

word2vec形式を期待するツールを使用する必要がある場合は、`gensim.scripts.glove2word2vec`で変換してください。