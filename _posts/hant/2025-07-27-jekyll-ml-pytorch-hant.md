---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 強化Jekyll部落格與PyTorch整合
translated: true
type: note
---

### 使用 PyTorch 透過 ML/AI 改進您的 Jekyll 部落格

由於您正在運行 Jekyll 部落格（一個靜態網站生成器），整合 ML/AI 功能（例如推薦或分類）需要一些創意。Jekyll 生成靜態 HTML，因此動態元素（例如即時推薦）可能需要客戶端 JavaScript 或在建置過程中透過 Jekyll 外掛或腳本進行預計算。您提到要避免使用 LLM API 並專注於使用 PyTorch 建立自己的神經網絡——這很好，因為這使得所有內容都在本地且可自訂。我將概述一些實用想法，重點放在 PyTorch 的實作上。這些假設您可以存取基本函式庫，如 NumPy（用於資料處理），並且能夠手動處理文字預處理或使用簡單的分詞（因為您的設定中未提及進階的 NLP 函式庫，如 Hugging Face，但如有需要，可以在本地添加）。

您可能會建立 Python 腳本（例如在 `scripts/` 目錄中），這些腳本在 Jekyll 的建置過程中運行（透過 Makefile 鉤子或部署時的 GitHub Actions）。例如，處理 `_posts/` 中的 Markdown 文章，生成 JSON 資料，並透過 Liquid 模板將其注入到您的網站中。

#### 1. 使用 PyTorch 分類器進行文章分類
透過訓練一個簡單的神經網絡分類器，自動對文章進行分類（例如分為「ML」、「Notes」、「Latex」等主題）。這屬於監督式學習：您需要手動標記一部分文章作為訓練資料。如果沒有標籤，可以先從非監督式聚類開始（見下文）。

**步驟：**
- **資料準備：** 解析 `_posts/` 中的 Markdown 檔案。提取文字內容（跳過 frontmatter）。建立資料集：(文字, 標籤) 對的列表。最初使用 CSV 或列表來處理約 50-100 個標記範例。
- **預處理：** 對文字進行分詞（簡單的空格/空白分割），建立詞彙表，轉換為數字索引。使用 one-hot 編碼或基本嵌入。
- **模型：** 在 PyTorch 中使用一個基本的前饋神經網絡進行多類別分類。
- **訓練：** 在本地機器上訓練。使用交叉熵損失和 Adam 優化器。
- **整合：** 在建置過程中運行腳本以分類所有文章，生成 `categories.json` 檔案，並在 Jekyll 中使用它來標記頁面或建立分類索引。

**PyTorch 程式碼片段範例（在類似 `scripts/categorize_posts.py` 的腳本中）：**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import os
from collections import Counter

# 步驟 1: 載入並預處理資料（簡化版）
def load_posts(posts_dir='_posts'):
    texts = []
    labels = []  # 假設手動標籤: 0=ML, 1=Notes, 等等
    for file in os.listdir(posts_dir):
        if file.endswith('.md'):
            with open(os.path.join(posts_dir, file), 'r') as f:
                content = f.read().split('---')[2].strip()  # 跳過 frontmatter
                texts.append(content)
                # 佔位符：從字典或 CSV 載入標籤
                labels.append(0)  # 替換為實際標籤
    return texts, labels

texts, labels = load_posts()
# 建立詞彙表（前 1000 個單詞）
all_words = ' '.join(texts).lower().split()
vocab = {word: idx for idx, word in enumerate(Counter(all_words).most_common(1000))}
vocab_size = len(vocab)

# 將文字轉換為向量（詞袋模型）
def text_to_vec(text):
    vec = np.zeros(vocab_size)
    for word in text.lower().split():
        if word in vocab:
            vec[vocab[word]] += 1
    return vec

X = np.array([text_to_vec(t) for t in texts])
y = torch.tensor(labels, dtype=torch.long)

# 步驟 2: 定義模型
class Classifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, num_classes)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = Classifier(vocab_size, num_classes=3)  # 調整 num_classes

# 步驟 3: 訓練
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()
X_tensor = torch.tensor(X, dtype=torch.float32)

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X_tensor)
    loss = loss_fn(outputs, y)
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# 步驟 4: 對新文章進行推論
def classify_post(text):
    vec = torch.tensor(text_to_vec(text), dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        pred = model(vec).argmax(1).item()
    return pred  # 映射回分類名稱

# 儲存模型: torch.save(model.state_dict(), 'classifier.pth')
# 在建置腳本中：分類所有文章並寫入 JSON
```

**改進：** 為了提高準確性，可以使用詞嵌入（在 PyTorch 中訓練一個簡單的 Embedding 層）或添加更多層。如果沒有標籤，可以切換到聚類（例如，在嵌入上使用 KMeans——見下一節）。在您的 Makefile 中運行此腳本：`jekyll build && python scripts/categorize_posts.py`。

#### 2. 使用 PyTorch 嵌入的推薦系統
向讀者推薦相似文章（例如「您可能還喜歡...」）。使用基於內容的推薦：學習每篇文章的嵌入，然後計算相似度（餘弦距離）。不需要用戶資料——僅需文章內容。

**步驟：**
- **資料：** 與上述相同——從文章中提取文字。
- **模型：** 在 PyTorch 中訓練一個自動編碼器，將文字壓縮為低維嵌入（例如 64 維向量）。
- **訓練：** 最小化重建損失以學習有意義的表示。
- **推薦：** 對於給定文章，在嵌入空間中找到最近鄰居。
- **整合：** 在建置過程中預計算嵌入，儲存在 JSON 中。在網站上使用 JS 顯示推薦（或使用 Liquid 生成靜態列表）。

**PyTorch 程式碼片段範例（在 `scripts/recommend_posts.py` 中）：**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# 重複使用上述的 load_posts 和 text_to_vec

texts, _ = load_posts()  # 忽略標籤
X = np.array([text_to_vec(t) for t in texts])
X_tensor = torch.tensor(X, dtype=torch.float32)

# 自動編碼器模型
class Autoencoder(nn.Module):
    def __init__(self, input_size, embedding_size=64):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.ReLU(),
            nn.Linear(256, embedding_size)
        )
        self.decoder = nn.Sequential(
            nn.Linear(embedding_size, 256),
            nn.ReLU(),
            nn.Linear(256, input_size)
        )
    
    def forward(self, x):
        emb = self.encoder(x)
        return self.decoder(emb)

model = Autoencoder(vocab_size)
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

for epoch in range(200):
    optimizer.zero_grad()
    reconstructed = model(X_tensor)
    loss = loss_fn(reconstructed, X_tensor)
    loss.backward()
    optimizer.step()
    if epoch % 20 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# 獲取嵌入
with torch.no_grad():
    embeddings = model.encoder(X_tensor).numpy()

# 推薦：對於文章 i，找到前 3 個相似文章
similarities = cosine_similarity(embeddings)
for i in range(len(texts)):
    rec_indices = similarities[i].argsort()[-4:-1][::-1]  # 前 3 個（排除自身）
    print(f'Recs for post {i}: {rec_indices}')

# 將嵌入儲存為 JSON 供 Jekyll 使用
import json
with open('embeddings.json', 'w') as f:
    json.dump({'embeddings': embeddings.tolist(), 'posts': [f'post_{i}' for i in range(len(texts))]}, f)
```

**改進：** 使用變分自動編碼器以獲得更好的嵌入。如果您有用戶瀏覽資料（透過分析），可以在 PyTorch 中添加協同過濾與矩陣分解模型。客戶端：在 JS 中載入 JSON 並即時計算相似度以實現個性化。

#### 3. 其他使用 PyTorch 的想法
- **用於自動標記的非監督式聚類：** 如果標記繁瑣，可以使用嵌入（來自上述自動編碼器）+ KMeans 聚類將文章分組到主題中。使用 PyTorch 進行嵌入，使用 NumPy/SciPy 進行聚類。
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=5)
  clusters = kmeans.fit_predict(embeddings)
  # 根據聚類分配標籤
  ```
  整合：透過腳本在 frontmatter 中生成標籤。

- **語義搜尋增強：** 以類似的方式嵌入查詢和文章，然後使用餘弦相似度進行搜尋欄。預計算文章嵌入；使用 JS 進行查詢嵌入（但由於 PyTorch 是 Python，可以將模型匯出為 ONNX 以透過 ONNX.js 在 JS 中進行推論，或保持搜尋為靜態）。

- **文章摘要：** 在配對的（全文, 手動摘要）資料上訓練一個 seq2seq 模型（在 PyTorch 中使用 RNN/LSTM）。在沒有大型資料集的情況下具有挑戰性，但可以從您的文章開始小規模嘗試。用於生成摘錄。

**一般提示：**
- **可擴展性：** 對於小型部落格，在 CPU 上訓練；PyTorch 可以很好地處理。使用 `torch.save` 儲存模型並載入進行推論。
- **建置整合：** 添加到 Makefile：`train: python scripts/train_models.py` 然後 `build: jekyll build && python scripts/generate_features.py`。
- **限制：** 沒有進階 NLP（例如 transformers），結果是基礎的——考慮在本地添加 `torchtext` 或手動 GloVe 嵌入。在您的 `ml/` 或 `notes/` 目錄上進行測試。
- **部署：** 如果在 GitHub Pages 上，在 CI 中運行腳本。對於動態內容，考慮添加一個輕量級的 Flask 後端，但這會偏離靜態 Jekyll。

如果您分享更多細節（例如文章數量、主題），我可以進一步完善這些內容！