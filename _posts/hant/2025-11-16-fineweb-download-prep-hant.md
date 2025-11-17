---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: FineWeb 數據下載與準備
translated: true
type: note
---

### 下載 Parquet 檔案

您提供的 URL 指向 FineWeb 資料集（CommonCrawl 資料的清理子集）中的特定 Parquet 檔案。此檔案（來自 `CC-MAIN-2013-20` 轉儲的 `000_00000.parquet`）包含約 100 萬行英文網路文字，每行都包含一個已為語言模型訓練預處理的 `text` 欄位（已去除 HTML、去重複化，並透過 Trafilatura 等工具進行品質過濾）。

下載方式：
- 使用 Hugging Face CLI：`huggingface-cli download HuggingFaceFW/fineweb data/CC-MAIN-2013-20/000_00000.parquet --local-dir ./fineweb_data`
- 或透過 Python 使用 `huggingface_hub`：
  ```python
  from huggingface_hub import hf_hub_download

  file_path = hf_hub_download(
      repo_id="HuggingFaceFW/fineweb",
      filename="data/CC-MAIN-2013-20/000_00000.parquet",
      local_dir="./fineweb_data"
  )
  print(f"下載至：{file_path}")
  ```
這會將約 500MB 的檔案儲存至本地（例如 `./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet`）。

對於完整轉儲（數百個檔案），請使用資料集文件中所示的 `snapshot_download`，但建議先從此單一檔案開始測試。

### 提取文字

FineWeb 的 `text` 欄位是可直接用於訓練的純文字，無需解析 HTML 或原始 HTML。使用 `pandas` 或 `pyarrow` 可高效載入。方法如下：

1. **安裝依賴項**（如有需要）：`pip install pandas pyarrow datasets`（假設您已為 NanoGPT 設定安裝了這些套件）。

2. **載入 Parquet 檔案並提取文字**：
   ```python
   import pandas as pd
   import os

   # 下載檔案的路徑
   parquet_path = "./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet"

   # 載入 Parquet 檔案（對大檔案效率高）
   df = pd.read_parquet(parquet_path, columns=['text'])  # 僅載入 text 欄位以節省記憶體

   # 將所有文字提取到列表中（若記憶體有限可迭代處理）
   texts = df['text'].tolist()  # 約 100 萬字串的列表

   # 可選：基礎清理（FineWeb 已清理過，但可標準化空白字元）
   import re
   def clean_text(text):
       if pd.isna(text):  # 跳過空值（在 FineWeb 中罕見）
           return ''
       text = re.sub(r'\s+', ' ', text.strip())  # 合併空白字元
       return text if len(text) > 10 else ''  # 過濾極短文字

   cleaned_texts = [clean_text(t) for t in texts if t]  # 套用過濾器

   print(f"已提取 {len(cleaned_texts)} 個文字樣本")
   print("範例：", cleaned_texts[0][:200] + "...")  # 預覽第一個文字
   ```

   - **記憶體提示**：此檔案約有 100 萬行，每行文字約 1-5k 字元。在 16GB RAM 的機器上可順利載入。對於更大的轉儲，請使用 `pyarrow` 進行分塊讀取：
     ```python
     import pyarrow.parquet as pq

     table = pq.read_table(parquet_path, columns=['text'])
     texts = table['text'].to_pylist()
     ```

   - **串流替代方案**（無需完整下載）：使用 `datasets` 函式庫進行迭代而無需載入全部資料：
     ```python
     from datasets import load_dataset

     # 以串流模式載入特定轉儲
     dataset = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)

     texts = []
     for i, sample in enumerate(dataset):
         if i >= 100000:  # 為測試設定限制
             break
         texts.append(sample['text'])

     # 如上所述進行清理
     ```

### 準備 NanoGPT 訓練

NanoGPT 預期單一文字檔案（例如 `input.txt`），其中包含以特殊符號分隔的串接文件（如 `"<|endoftext|>"`）。以下是格式化提取文字的方法：

```python
# 從上述步驟提取 cleaned_texts 後
with open('input.txt', 'w', encoding='utf-8') as f:
    for text in cleaned_texts:
        f.write(text + "\n<|endoftext|>\n")  # NanoGPT 的預設分隔符

print("已儲存至 input.txt – 準備好供 NanoGPT 使用！")
```

- **為何採用此格式？** NanoGPT 的 `data.py` 腳本將讀取 `input.txt`，使用您的 tokenizer（例如 GPT-2）進行編碼，並建立訓練/驗證分割。每個文件以 `"<|endoftext|>"` 結尾，以避免跨文件上下文污染。
- **自訂選項**：
  - 依長度過濾：在寫入前加入 `if 100 < len(text.split()) < 10000:` 以保留中等長度的文件。
  - 測試子集：使用 `cleaned_texts[:10000]` 進行快速的 1 萬樣本測試。
  - 訓練指令：當 `input.txt` 準備好後，在 NanoGPT 中執行 `python train.py`（如有需要，調整 `--dataset=input.txt`）。

此單一檔案提供約 50-100 億個 token，非常適合微調。如需更多資料，請下載其他 Parquet 檔案並進行串接。若遇到記憶體問題或需要 NanoGPT 配置協助，請提供詳細資訊！

**參考**：[FineWeb 資料集卡片](https://huggingface.co/datasets/HuggingFaceFW/fineweb)