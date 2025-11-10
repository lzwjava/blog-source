---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 二通りの方法で GloVe ベクトルを読み込む
translated: true
type: note
---

`the`、`to`、`U.S.` のような単語や独自のテキストに対して GloVe ベクトルを取得するには、次の2つの簡単な方法があります：

---

## オプション A — Stanford GloVe をダウンロードして `gensim` で検索する

これが最も一般的な方法で、ダウンロード後は完全にオフラインで動作します。

```python
# 1) ダウンロード & 解凍（初回実行時のみ）
import os, zipfile, urllib.request
url = "https://nlp.stanford.edu/data/glove.6B.zip"
zip_path = "glove.6B.zip"
if not os.path.exists(zip_path):
    urllib.request.urlretrieve(url, zip_path)
with zipfile.ZipFile(zip_path) as zf:
    zf.extract("glove.6B.300d.txt")  # 300次元セット

# 2) GloVe形式 -> word2vecテキスト形式に変換して読み込み
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

glove_path = "glove.6B.300d.txt"
w2v_path   = "glove.6B.300d.w2v.txt"
if not os.path.exists(w2v_path):
    glove2word2vec(glove_path, w2v_path)

vectors = KeyedVectors.load_word2vec_format(w2v_path, binary=False)
print(vectors.vector_size)  # 300

# 3) 単語検索
print(vectors['the'][:5])   # 最初の5次元
print(vectors['to'][:5])

# 注意: glove.6Bの語彙は小文字化されています。
# 'U.S.' -> この語彙では 'u.s.'（存在する場合）。安全策：トークンを小文字化してください。
print(vectors['u.s.'][:5])
```

独自のテキストを埋め込む：

```python
import re, numpy as np

# u.s. のようなトークン内のドットを保持するシンプルなトークナイザ
TOKEN_RE = re.compile(r"[A-Za-z0-9\.\-']+")

def tokenize(text: str):
    return TOKEN_RE.findall(text.lower())

def embed_tokens(tokens, kv: KeyedVectors):
    vecs = [kv[w] for w in tokens if w in kv.key_to_index]
    return np.stack(vecs) if vecs else np.zeros((0, kv.vector_size))

def embed_sentence_avg(text: str, kv: KeyedVectors):
    V = embed_tokens(tokenize(text), kv)
    return V.mean(axis=0) if V.size else np.zeros(kv.vector_size)

# 例
print(embed_sentence_avg("The quick brown fox jumps over the lazy dog.", vectors)[:10])
print(embed_tokens(tokenize("U.S. interest rates rose today."), vectors).shape)  # (n_tokens, 300)
```

**ヒント**

* `glove.6B.300d.txt` はメモリ上で約 1.1 GB を使用します。負荷が高い場合は、代わりに `100d` を試してください。
* 6B セットは**小文字化**されています。テキストは常に小文字化するか、より広範なカバレッジが必要な場合は大規模な **840B** セットを使用してください（実際にはほぼ大文字小文字を区別しません）。
* OOV（語彙外）の単語は何も返しません。スキップするか、サブワードのヒューリスティックにフォールバックできます。

---

## オプション B — `torchtext` に GloVe のダウンロードと提供を任せる

手動でのダウンロード/変換が不要になります。

```python
import torch
from torchtext.vocab import GloVe
import re

glove = GloVe(name="6B", dim=300)  # ~/.vector_cache に自動ダウンロード
stoi = glove.stoi    # 単語 -> インデックス
vecs = glove.vectors # テンソル [vocab, 300]

def get_word_vec(word: str):
    idx = stoi.get(word.lower())
    return vecs[idx] if idx is not None else None

print(get_word_vec("the")[:5])
print(get_word_vec("to")[:5])
print(get_word_vec("U.S.")[:5])     # 多くのビルドでは None になる; "u.s." を試す：
print(get_word_vec("u.s.")[:5])

# 文の埋め込み（平均）
TOKEN_RE = re.compile(r"[A-Za-z0-9\.\-']+")
def embed_sentence_avg(text: str):
    toks = TOKEN_RE.findall(text.lower())
    xs = [get_word_vec(t) for t in toks]
    xs = [x for x in xs if x is not None]
    return torch.stack(xs, dim=0).mean(0) if xs else torch.zeros(glove.dim)

print(embed_sentence_avg("The quick brown fox...")[:10])
```

---

## 特定の行についての質問

以下のような行：

```
the  0.418 0.24968 -0.41242 0.1217 ... 0.34527  # 合計300個の浮動小数点数
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982 0.25344 ... 0.024118
```

は、プレーンテキストの `.txt` ファイルでそのまま見られる形式です：各行は `トークン` とそれに続く `300個` の浮動小数点数で構成されています。`gensim` や `torchtext` を使用すれば、行を自分で解析する必要はありません—これらのライブラリが処理し、直接ベクトルを検索できるようにします。

---

## よくある落とし穴（と解決策）

* **「KeyError: 'U.S.'」** → 6B セットでは `u.s.` を使用するか、より良いカバレッジを持つ大規模なセットを選択し、検索前には常に小文字化してください。
* **メモリ/時間の大量消費** → `300d` の代わりに `100d` や `200d` を使用するか、ファイルをスキャンして必要な単語だけを読み込み、より小さな語彙を構築してください。
* **文/ドキュメントベクトル** → 単語ベクトルの平均または合計を取ります。重み付き平均が必要な場合は、TF-IDF 重みを試してください。

ご希望であれば、具体的なテキスト処理の目的（分類、類似性、クラスタリングなど）を教えてください。GloVe を使用したエンドツーエンドの最小限のパイプラインを概説します。