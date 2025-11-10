---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Gensim 的 Word2Vec 腳本
translated: true
type: note
---

為您提供一個關於 Word2Vec 的 Python 腳本，我需要先做一些假設，因為「關於 Word2Vec 的腳本」這個範圍相當廣泛。我將提供兩種常見情境：

1.  **使用 `gensim` 進行訓練和基本應用的簡單腳本：** 這是在 Python 中使用 Word2Vec 最常見且實用的方法。
2.  **從零開始的基本概念性實現：** 這更側重於理解核心算法，但由於複雜性和優化問題，在實際應用中較不實用。

根據您的請求，我將優先介紹 `gensim` 方法，因為這是大多數人會使用的方式。

-----

### 使用 `gensim` 的 Word2Vec Python 腳本

此腳本將演示：

  * 準備樣本文本數據。
  * 訓練 Word2Vec 模型。
  * 尋找最相似的詞語。
  * 執行詞語類比。
  * 儲存和載入模型。

**先決條件：**

您需要安裝 `gensim` 函式庫：

```bash
pip install gensim
```

**Python 腳本 (`word2vec_gensim_example.py`):**

```python
import gensim
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
import logging

# 配置日誌記錄以查看訓練進度
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# --- 1. 準備樣本文本數據 ---
# 在實際應用中，您會從檔案載入文本數據。
# 這裡我們使用一個簡單的句子列表。
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

# 預處理句子：分詞並轉換為小寫
# gensim 的 simple_preprocess 對此非常方便
tokenized_sentences = [simple_preprocess(sentence) for sentence in raw_sentences]

print("\n--- 分詞後的句子 ---")
for sentence in tokenized_sentences:
    print(sentence)

# --- 2. 訓練 Word2Vec 模型 ---
# 參數解釋：
#   vector_size: 詞向量的維度。
#   window: 在一個句子中，當前詞與預測詞之間的最大距離。
#   min_count: 忽略總頻率低於此值的所有詞。
#   sg: 訓練算法：0 代表 CBOW，1 代表 Skip-gram。Skip-gram 通常對罕見詞效果更好。
#   workers: 使用多個工作執行緒來訓練模型（= 訓練更快）。
#   epochs: 在語料庫上的迭代次數。
model = Word2Vec(
    sentences=tokenized_sentences,
    vector_size=100,      # 範例：100 維向量
    window=5,             # 上下文窗口為左右各 5 個詞
    min_count=1,          # 包含所有詞（針對此小範例）
    sg=1,                 # 使用 Skip-gram (sg=1)
    workers=4,            # 使用 4 個 CPU 核心進行訓練
    epochs=10             # 訓練 10 個週期
)

print("\n--- 模型訓練完成 ---")

# --- 3. 探索模型 ---

# 獲取特定詞的向量
try:
    word_vector = model.wv['machine']
    print(f"\n'machine' 的向量（前 10 個維度）: {word_vector[:10]}")
    print(f"'machine' 的向量形狀: {word_vector.shape}")
except KeyError:
    print("\n詞彙表中找不到 'machine'。")

# 尋找最相似的詞
print("\n--- 與 'machine' 最相似的詞 ---")
try:
    similar_words = model.wv.most_similar('machine')
    for word, similarity in similar_words:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n詞彙表中找不到 'machine'。")

print("\n--- 與 'dog' 最相似的詞 ---")
try:
    similar_words_dog = model.wv.most_similar('dog')
    for word, similarity in similar_words_dog:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n詞彙表中找不到 'dog'。")


# 執行詞語類比（例如，King - Man + Woman = Queen）
# 在非常小的數據集上可能無法完美運作，但展示了概念。
print("\n--- 詞語類比 (King - Man + Woman = ?) ---")
try:
    result = model.wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
    if result:
        print(f"King - Man + Woman 類似於: {result[0][0]} (相似度: {result[0][1]:.4f})")
    else:
        print("類比沒有結果。詞彙量可能太小。")
except KeyError as e:
    print(f"類比中的一個或多個詞未在詞彙表中找到: {e}")
except Exception as e:
    print(f"類比過程中發生錯誤: {e}")

# 檢查兩個詞之間的相似度
print("\n--- 'machine' 與 'learning' 之間的相似度 ---")
try:
    similarity = model.wv.similarity('machine', 'learning')
    print(f"相似度: {similarity:.4f}")
except KeyError:
    print("一個或兩個詞未在詞彙表中找到。")

print("\n--- 'dog' 與 'cat' 之間的相似度 ---")
try:
    similarity_pets = model.wv.similarity('dog', 'cat')
    print(f"相似度: {similarity_pets:.4f}")
except KeyError:
    print("一個或兩個詞未在詞彙表中找到。")

print("\n--- 'dog' 與 'computer' 之間的相似度 ---")
try:
    similarity_diff = model.wv.similarity('dog', 'computer')
    print(f"相似度: {similarity_diff:.4f}")
except KeyError:
    print("一個或兩個詞未在詞彙表中找到。")

# --- 4. 儲存和載入模型 ---
model_path = "word2vec_model.bin"
model.save(model_path)
print(f"\n模型已儲存至 {model_path}")

# 載回模型
loaded_model = Word2Vec.load(model_path)
print(f"模型已從 {model_path} 載入")

# 驗證載入的模型
print("\n--- 驗證載入的模型（使用載入的模型尋找與 'machine' 最相似的詞）---")
try:
    similar_words_loaded = loaded_model.wv.most_similar('machine')
    for word, similarity in similar_words_loaded:
        print(f"{word}: {similarity:.4f}")
except KeyError:
    print("\n在載入模型的詞彙表中找不到 'machine'。")

print("\n腳本執行完成。")
```

**如何運行腳本：**

1.  將上面的程式碼儲存為 Python 檔案（例如 `word2vec_gensim_example.py`）。
2.  打開您的終端機或命令提示字元。
3.  導航至您儲存檔案的目錄。
4.  使用以下命令運行腳本：`python word2vec_gensim_example.py`

-----

### Word2Vec (`gensim` 實現) 中的關鍵概念

  * **`gensim.models.Word2Vec`**: 用於訓練的主要類別。
  * **`sentences`**: 一個可迭代對象的可迭代對象，外層可迭代對象是語料庫，內層可迭代對象是詞的列表（分詞後的句子）。
  * **`vector_size`**: 詞向量的維度。更高的維度可以捕捉更多細微差別，但需要更多數據和計算。
  * **`window`**: 在一個句子中，當前詞與其周圍詞之間的最大距離。
  * **`min_count`**: 出現次數少於 `min_count` 的詞將被忽略。這有助於過濾掉可能沒有意義嵌入的非常罕見的詞。
  * **`sg` (Skip-gram vs. CBOW)**:
      * `sg=0` (CBOW - 連續詞袋模型): 根據上下文預測當前詞。訓練速度更快。
      * `sg=1` (Skip-gram): 給定當前詞，預測周圍的詞。通常對罕見詞表現更好。
  * **`workers`**: 用於訓練的 CPU 核心數量，可加速過程。
  * **`epochs`**: 算法在整個數據集上迭代的次數。更多的週期可能導致更好的嵌入質量，但也需要更長的時間。
  * **`model.wv`**: 「詞向量」對象 (`KeyedVectors`)，包含訓練好的詞嵌入以及 `most_similar`、`similarity` 等方法。您也可以像 `model.wv['word']` 這樣直接訪問向量。

-----

這個 `gensim` 腳本為使用 Word2Vec 提供了堅實的基礎。對於實際應用，您通常會使用更大的語料庫（例如 Wikipedia、Common Crawl）並調整超參數以獲得最佳性能。