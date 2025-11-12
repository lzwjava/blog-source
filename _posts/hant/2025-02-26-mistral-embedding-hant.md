---
audio: false
generated: true
lang: hant
layout: post
title: Mistral AI 嵌入技術
translated: true
type: note
---

要使用 Mistral AI 提供嵌入範例，您可以利用其嵌入 API 生成文字語義的數值表示（嵌入）。這些嵌入適用於相似性檢測、聚類分析、分類或搜尋等任務。以下將示範如何為一組句子生成嵌入，並使用 Mistral AI 嵌入端點計算其相似度。此範例基於提供的程式碼結構，但根據文件說明專門針對嵌入功能進行調整：[Mistral AI 嵌入功能](https://docs.mistral.ai/capabilities/embeddings/)。

### 前置準備

執行範例前請確保：
1. **API 金鑰**：有效的 Mistral AI API 金鑰已儲存在 `MISTRAL_API_KEY` 環境變數中
2. **相依套件**：已安裝必要的 Python 套件，可透過以下指令安裝：
   ```bash
   pip install requests numpy
   ```

### 範例程式碼

以下是完整的 Python 腳本，可為三個句子生成嵌入並計算其兩兩相似度：

```python
import os
import requests
import numpy as np

def call_mistral_embeddings_api(texts, model="mistral-embed"):
    """
    呼叫 Mistral AI 嵌入 API 為文字列表生成嵌入向量
    
    參數：
        texts (list)：要嵌入的字串列表
        model (str)：使用的嵌入模型（預設："mistral-embed"）
    
    返回：
        list：嵌入向量列表，若請求失敗則返回 None
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("錯誤：未設定 MISTRAL_API_KEY 環境變數")
        return None
    
    url = "https://api.mistral.ai/v1/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "input": texts
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and "data" in response_json:
            embeddings = [item["embedding"] for item in response_json["data"]]
            return embeddings
        else:
            print(f"Mistral 嵌入 API 錯誤：無效的回應格式：{response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral 嵌入 API 錯誤：{e}")
        if e.response:
            print(f"回應狀態碼：{e.response.status_code}")
            print(f"回應內容：{e.response.text}")
        return None

def calculate_similarity(emb1, emb2):
    """
    使用點積計算兩個嵌入向量的相似度
    
    參數：
        emb1 (list)：第一個嵌入向量
        emb2 (list)：第二個嵌入向量
    
    返回：
        float：相似度分數（點積，對歸一化向量等同於餘弦相似度）
    """
    return np.dot(emb1, emb2)

if __name__ == "__main__":
    # 要嵌入的範例文字
    texts = [
        "I love programming in Python.",
        "Python is a great programming language.",
        "The weather is sunny today."
    ]
    
    # 生成嵌入向量
    embeddings = call_mistral_embeddings_api(texts)
    if embeddings:
        # 顯示嵌入維度
        print(f"嵌入維度：{len(embeddings[0])}")
        
        # 計算兩兩相似度
        sim_12 = calculate_similarity(embeddings[0], embeddings[1])
        sim_13 = calculate_similarity(embeddings[0], embeddings[2])
        sim_23 = calculate_similarity(embeddings[1], embeddings[2])
        
        # 顯示結果
        print(f"\n相似度結果：")
        print(f"文字 1：'{texts[0]}'")
        print(f"文字 2：'{texts[1]}'")
        print(f"文字 3：'{texts[2]}'")
        print(f"\n文字 1 與文字 2 的相似度：{sim_12:.4f}")
        print(f"文字 1 與文字 3 的相似度：{sim_13:.4f}")
        print(f"文字 2 與文字 3 的相似度：{sim_23:.4f}")
```

### 執行方式

1. **設定 API 金鑰**：
   ```bash
   export MISTRAL_API_KEY="your_api_key_here"
   ```

2. **儲存並執行**：
   將腳本儲存（例如存為 `embedding_example.py`）後執行：
   ```bash
   python embedding_example.py
   ```

### 預期輸出

假設 API 呼叫成功，您將看到類似輸出（具體數值取決於返回的嵌入向量）：
```
嵌入維度：1024

相似度結果：
文字 1：'I love programming in Python.'
文字 2：'Python is a great programming language.'
文字 3：'The weather is sunny today.'

文字 1 與文字 2 的相似度：0.9200
文字 1 與文字 3 的相似度：0.6500
文字 2 與文字 3 的相似度：0.6700
```

### 原理說明

- **API 端點**：`call_mistral_embeddings_api` 函數向 `https://api.mistral.ai/v1/embeddings` 發送 POST 請求，傳遞文字列表和 `"mistral-embed"` 模型。API 返回的 JSON 回應在 `"data"` 鍵下包含嵌入向量

- **嵌入向量**：每個嵌入向量是 1024 維向量（根據 Mistral 文件說明），代表輸入文字的語義內容。嵌入向量已歸一化為範數 1

- **相似度計算**：由於嵌入向量已歸一化，兩個嵌入向量的點積（`np.dot`）等於其餘弦相似度。數值越高表示語義相似度越高：
  - **文字 1 與文字 2**：兩者均關於 Python 程式設計，相似度應較高（例如約 0.92）
  - **文字 1 與文字 3**：一個關於程式設計，另一個關於天氣，相似度應較低（例如約 0.65）
  - **文字 2 與文字 3**：類似模式，因主題不同而相似度較低

### 其他應用場景

Mistral AI 的嵌入向量還可應用於以下領域：
- **聚類分析**：使用 K-means 等演算法分組相似文字（需要 `scikit-learn`）：
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=2).fit(np.array(embeddings))
  print(kmeans.labels_)
  ```
- **搜尋**：嵌入查詢並尋找最相似文字：
  ```python
  query = "Tell me about Python."
  query_emb = call_mistral_embeddings_api([query])[0]
  similarities = [calculate_similarity(query_emb, emb) for emb in embeddings]
  most_similar = texts[np.argmax(similarities)]
  print(f"最相似文字：'{most_similar}'")
  ```
- **分類**：將嵌入向量作為機器學習模型的特徵

### 注意事項

- **模型**：`"mistral-embed"` 模型針對嵌入功能進行了優化。請查閱[文件](https://docs.mistral.ai/capabilities/embeddings/)了解更新或其他模型
- **批次處理**：API 可單次呼叫處理多個文字，提升效率
- **進階應用**：如需大規模相似度搜尋，可整合向量資料庫如 Faiss 或 Milvus

此範例提供了使用 Mistral AI 嵌入功能的實務入門指南，透過更改端點和資料格式即可適應提供的聊天完成程式碼結構。