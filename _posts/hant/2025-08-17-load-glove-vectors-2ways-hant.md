---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 載入 GloVe 向量兩種方法
translated: true
type: note
---

你有兩種簡單方法可以獲取像 `the`、`to`、`U.S.` 這類詞語的 GloVe 向量，以及處理你自己的文本：

---

## 選項 A — 下載 Stanford GloVe 並使用 `gensim` 查詢

這是最常用的方法，下載後可完全離線運作。

```python
# 1) 下載並解壓（僅首次執行時需要）
import os, zipfile, urllib.request
url = "https://nlp.stanford.edu/data/glove.6B.zip"
zip_path = "glove.6B.zip"
if not os.path.exists(zip_path):
    urllib.request.urlretrieve(url, zip_path)
with zipfile.ZipFile(zip_path) as zf:
    zf.extract("glove.6B.300d.txt")  # 300 維度數據集

# 2) 將 GloVe 格式轉換為 word2vec 文本格式並載入
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

glove_path = "glove.6B.300d.txt"
w2v_path   = "glove.6B.300d.w2v.txt"
if not os.path.exists(w2v_path):
    glove2word2vec(glove_path, w2v_path)

vectors = KeyedVectors.load_word2vec_format(w2v_path, binary=False)
print(vectors.vector_size)  # 300

# 3) 單詞查詢
print(vectors['the'][:5])   # 前 5 個維度
print(vectors['to'][:5])

# 注意：glove.6B 詞彙表為全小寫
# 'U.S.' 在此詞彙表中會變成 'u.s.'（如果存在）。更安全做法：將你的詞元轉為小寫
print(vectors['u.s.'][:5])
```

現在為你的文本生成嵌入向量：

```python
import re, numpy as np

# 簡單的分詞器，保留如 u.s. 中的點號
TOKEN_RE = re.compile(r"[A-Za-z0-9\.\-']+")

def tokenize(text: str):
    return TOKEN_RE.findall(text.lower())

def embed_tokens(tokens, kv: KeyedVectors):
    vecs = [kv[w] for w in tokens if w in kv.key_to_index]
    return np.stack(vecs) if vecs else np.zeros((0, kv.vector_size))

def embed_sentence_avg(text: str, kv: KeyedVectors):
    V = embed_tokens(tokenize(text), kv)
    return V.mean(axis=0) if V.size else np.zeros(kv.vector_size)

# 範例
print(embed_sentence_avg("The quick brown fox jumps over the lazy dog.", vectors)[:10])
print(embed_tokens(tokenize("U.S. interest rates rose today."), vectors).shape)  # (n_tokens, 300)
```

**提示**

* `glove.6B.300d.txt` 約佔用 1.1 GB 記憶體。若負擔過重，可改用 `100d` 版本
* 6B 數據集為**全小寫**；請始終將文本轉為小寫，或使用更大的 **840B** 數據集以獲得更好覆蓋率（實際使用中仍主要為無大小寫區分）
* 遇到詞彙表外（OOV）詞語將不返回結果；你可選擇跳過或使用子詞啟發式方法處理

---

## 選項 B — 讓 `torchtext` 自動下載並提供 GloVe

此方法無需手動下載/轉換。

```python
import torch
from torchtext.vocab import GloVe
import re

glove = GloVe(name="6B", dim=300)  # 自動下載至 ~/.vector_cache
stoi = glove.stoi    # 單詞 -> 索引
vecs = glove.vectors # 張量 [詞彙量, 300]

def get_word_vec(word: str):
    idx = stoi.get(word.lower())
    return vecs[idx] if idx is not None else None

print(get_word_vec("the")[:5])
print(get_word_vec("to")[:5])
print(get_word_vec("U.S.")[:5])     # 在多數版本中會變成 None；請嘗試 "u.s."：
print(get_word_vec("u.s.")[:5])

# 句子嵌入（平均法）
TOKEN_RE = re.compile(r"[A-Za-z0-9\.\-']+")
def embed_sentence_avg(text: str):
    toks = TOKEN_RE.findall(text.lower())
    xs = [get_word_vec(t) for t in toks]
    xs = [x for x in xs if x is not None]
    return torch.stack(xs, dim=0).mean(0) if xs else torch.zeros(glove.dim)

print(embed_sentence_avg("The quick brown fox...")[:10])
```

---

## 關於特定行的說明

你提到的那些行如：

```
the  0.418 0.24968 -0.41242 0.1217 ... 0.34527  # 共 300 個浮點數
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982 0.25344 ... 0.024118
```

正是你在純文字 `.txt` 檔案中會看到的格式：每行包含一個`詞元`後接`300`個浮點數。使用 `gensim` 或 `torchtext` 時，你無需自行解析這些行——它們會自動處理並提供直接的向量查詢功能。

---

## 常見問題（及解決方法）

* **「KeyError: 'U.S.'」** → 使用 6B 數據集時請改用 `u.s.`，或選用覆蓋率更高的更大數據集，並在查詢前始終轉為小寫
* **記憶體/時間消耗過大** → 改用 `100d` 或 `200d` 版本替代 `300d`，或透過掃描檔案並建立較小詞彙表來僅載入所需詞語
* **句子/文件向量** → 對詞向量進行平均或加總處理；如需加權平均，可嘗試 TF-IDF 加權

如果你需要，請告訴我你的具體文本處理目標（分類、相似度、聚類等），我會使用 GloVe 為你繪製一個端到端的最小化流程圖。