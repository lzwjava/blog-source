---
audio: false
generated: true
image: false
lang: hant
layout: post
title: GloVe 格式與載入指南
translated: true
type: note
---

GloVe 向量是純文字檔案。每行包含一個詞元及其嵌入值，以空格分隔。檔案**沒有標頭行**（這點與許多 word2vec 文字檔案不同）。

範例（300 維 GloVe）：

```
the 0.418 0.24968 -0.41242 0.1217 ... 0.34527   # 共 300 個浮點數
to   0.68047 -0.039263 -0.67412 0.056051 ... -0.067549
U.S. 0.3459  0.21513  -0.09982  0.244 ... 0.024118
```

實務注意事項：

* 常見發布版本：
  * `glove.6B.{50,100,200,300}d.txt`（維基百科 + Gigaword；約 40 萬詞彙，全小寫）
  * `glove.840B.300d.txt`（Common Crawl；約 220 萬詞彙）
  * `glove.twitter.27B.{25,50,100,200}d.txt`（Twitter；含大量主題標籤/表情符號）
* 詞元不包含空格（片語使用底線連接），因此直接使用 `line.split()` 即可
* 浮點數為 ASCII 格式；會看到常規小數與科學記號表示法
* 沒有特殊的 `<unk>` 列；未登錄詞處理需自行實現

您的載入函式

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

符合此格式。兩個可考慮的升級項目：

1. 使用 float32 節省一半記憶體：

```python
vec = np.asarray(line[1:], dtype=np.float32)
```

2. 跳過意外出現的「標頭」或錯誤行（部分重新封裝的檔案會添加標頭）：

```python
parts = line.rstrip().split(' ')
if len(parts) < 2: 
    continue
if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
    # 看似 word2vec 風格標頭："<詞彙量> <維度>"
    continue
word, *vals = parts
```

### 為您的詞彙表建立嵌入矩陣

建立 `dictionary: 詞語 -> 編號` 後，將 GloVe 行映射到 `nn.Embedding` 的權重矩陣：

```python
def build_embedding_matrix(dictionary, glove_path, dim=300, dtype=np.float32):
    _, glove = read_glove_vecs(glove_path)  # 如前所述，但 dtype=float32
    V = len(dictionary)
    W = np.random.uniform(-0.05, 0.05, (V, dim)).astype(dtype)
    for w, idx in dictionary.items():
        vec = glove.get(w)
        if vec is not None and vec.shape[0] == dim:
            W[idx] = vec
    return torch.tensor(W)

# 使用方式
# emb_weight = build_embedding_matrix(dictionary, "glove.6B.300d.txt", dim=300)
# model.in_embeddings.weight.data.copy_(emb_weight)
```

### 與 word2vec 文字/二進位格式快速對比

* **GloVe 文字**：無標頭，格式為 `詞語 浮點數 浮點數 ...`
* **word2vec 文字**：通常以 `"<詞彙量> <維度>"` 標頭開頭
* **word2vec 二進位**：標頭 + 二進位浮點數

若需使用預期 word2vec 格式的工具，可透過 `gensim.scripts.glove2word2vec` 進行轉換。