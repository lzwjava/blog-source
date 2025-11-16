---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: nanoGPT 詞彙元數據檔案
translated: true
type: note
---

在 **nanoGPT** (https://github.com/karpathy/nanoGPT) 中，**meta.pkl** 檔案是一個可選的 pickle 檔案，用於儲存資料集的詞彙表與編碼元數據。當您使用自訂文字資料集（非預設的 OpenWebText 或莎士比亞字元級資料集）進行訓練時，便會使用此檔案。

### meta.pkl 通常包含的內容
這是一個包含以下鍵值的字典（範例）：

```python
{
    'vocab_size': 50257,       # 詞彙表大小
    'itos': {0: 'A', 1: 'B', ...},  # 整數 → 字串（符記）
    'stoi': {'A': 0, 'B': 1, ...},  # 字串 → 整數（符記）
    'encoder': ...,            # 編碼函數
    'decoder': ...,            # 解碼函數
}
```

### nanoGPT 載入或建立 meta.pkl 的時機

1. 訓練期間 (`train.py`)：
   - 若 `data/your_dataset/meta.pkl` 已存在 → 直接載入該詞彙表
   - 若檔案**不存在** → nanoGPT 會從資料集文字建立新詞彙表（通常使用 SentencePiece、tiktoken 或簡單的字元級詞彙表），並儲存為 `meta.pkl` 供後續使用

2. 取樣/推論期間 (`sample.py`)：
   - 當出現提示訊息  
     `未找到 meta.pkl，預設使用 GPT-2 編碼...`  
     表示 nanoGPT 在資料目錄中找不到 meta.pkl 檔案
   - 此時系統會回溯至預設的 GPT-2 BPE 分詞器（與 OpenAI GPT-2 相同），詞彙表大小為 50257。這就是為什麼您的 29.94M 參數模型（這是最小 GPT-2 124M 配置，但有時會錯誤顯示）即使在沒有 meta.pkl 的情況下，也能在 OpenWebText 或類似資料集上正常運作

### 簡要總結：

| 情境                               | meta.pkl 作用                                           |
|------------------------------------|---------------------------------------------------------|
| 使用**自訂資料集**訓練時            | 儲存自訂詞彙表以確保編碼/解碼一致性                     |
| 使用 OpenWebText/莎士比亞訓練時     | 無需使用 → nanoGPT 直接採用預設 GPT-2 分詞器            |
| `sample.py` 找不到 meta.pkl 時      | 回溯至 GPT-2 分詞器（即您所見的情況）                   |

若您訓練自訂資料集並希望保持可重現的分詞處理（或使用不同詞彙表大小），nanoGPT 會在首次訓練運行時自動建立 meta.pkl。此後系統將重複使用該檔案，您也不會再看到「預設使用 GPT-2 編碼」的警告訊息。