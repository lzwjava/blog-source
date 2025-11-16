---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: OpenWebText 數據集預處理腳本
translated: true
type: note
---

### 概述
這個 Python 腳本用於處理包含 OpenWebText 資料集的大型文字檔案（這是一個類似於訓練 GPT-2 等模型所使用的網路爬取文字語料庫）。其目標是：
- 將原始文字分割成易於管理的「文件」（文字區塊）。
- 建立一個 Hugging Face `Dataset` 物件以便於處理。
- 使用 TikToken 中的 GPT-2 Byte Pair Encoding (BPE) tokenizer 對文字進行標記化（忽略特殊標記並附加文本結束標記）。
- 將資料集分割為訓練集 (99.95%) 和驗證集 (0.05%)。
- 使用 NumPy 的記憶體映射陣列將標記化後的資料儲存為緊湊的二進位檔案（`train.bin` 和 `val.bin`）。這些檔案儲存了標記 ID 的序列（作為 16 位元整數），以便在機器學習訓練期間高效載入。

該腳本專為在多核心系統上高效運行而設計，使用多處理進行標記化。其靈感來自 Flash Attention 儲存庫中的資料載入模組（程式碼中已連結），該模組處理語言模型訓練的類似預處理。注意：OpenWebText 非常龐大（未壓縮約 40GB），但此腳本假設已預先下載本地的 `openwebtext.txt` 檔案。輸出檔案要小得多：`train.bin` 約 17GB（90 億個標記），`val.bin` 約 8.5MB（400 萬個標記）。

腳本在開始時會列印代理設定（可能用於在隱性下載期間除錯網路問題，儘管此處沒有明確的下載）。預設使用 8 個工作程序進行標記化。

### 逐步分解

#### 1. 匯入與初始設定
```python
import os
import tarfile
from tqdm import tqdm
import numpy as np
import tiktoken
from huggingface_hub import hf_hub_download
from datasets import load_dataset # huggingface datasets
import datasets

print("HTTP_PROXY:", os.getenv("HTTP_PROXY"))
print("HTTPS_PROXY:", os.getenv("HTTPS_PROXY"))

# number of workers in .map() call
# good number to use is ~order number of cpu cores // 2
num_proc = 8

# number of workers in load_dataset() call
# best number might be different from num_proc above as it also depends on NW speed.
# it is better than 1 usually though
num_proc_load_dataset = num_proc

enc = tiktoken.get_encoding("gpt2")

datasets.logging.set_verbosity_info()
```
- **目的**：匯入用於檔案處理（`os`、`tarfile`）、進度條（`tqdm`）、數值運算（`numpy`）、標記化（`tiktoken`）和 Hugging Face 工具（`huggingface_hub`、`datasets`）的函式庫。
- **代理列印**：記錄 HTTP/HTTPS 代理的環境變數，如果腳本遇到網路限制（例如，用於下載 tokenizer 模型，儘管 TikToken 在內部處理此問題）時很有用。
- **工作程序**：設定 `num_proc=8` 用於標記化中的並行處理（大約一半的 CPU 核心以達到平衡）。`num_proc_load_dataset` 與其匹配，但在此未使用（來自靈感程式碼的遺留，該程式碼從 Hugging Face 載入）。
- **編碼器**：載入 GPT-2 BPE tokenizer（`enc`）。這會將文字轉換為整數標記 ID（範圍 0–50,256）。
- **日誌記錄**：將 Hugging Face datasets 的日誌級別設定為「info」，以便在處理期間輸出詳細資訊。

`if __name__ == '__main__':` 防護確保主要邏輯僅在腳本直接執行時運行（而非匯入時）。

#### 2. 讀取與分割文字檔案
```python
if __name__ == '__main__':
    # Read the local openwebtext.txt file
    txt_file = os.path.join(os.path.dirname(__file__), 'openwebtext.txt')
    print(f"Reading from local file: {txt_file}")

    # Read the text content
    texts = []
    with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
        # Read the entire file
        full_text = f.read().strip()

        # Try to split into documents by double newlines first
        documents = full_text.split('\n\n')

        # If we only got one document, split by single newlines
        if len(documents) <= 1:
            documents = full_text.split('\n')

        # If we still only have one document, split by period followed by space
        if len(documents) <= 1:
            # Split on period followed by space, then join back sentences
            sentences = full_text.split('. ')
            # Group sentences into chunks of ~100 sentences per document
            chunk_size = 100
            for i in range(0, len(sentences), chunk_size):
                chunk = '. '.join(sentences[i:i+chunk_size])
                if chunk.strip():
                    texts.append(chunk.strip() + '.')
        else:
            # Process documents from double/single newline splits
            for doc in documents:
                doc = doc.strip()
                if doc:  # Only add non-empty documents
                    texts.append(doc)

        print(f"Created {len(texts)} documents from the text file")
```
- **檔案讀取**：以 UTF-8 模式開啟 `openwebtext.txt`（假設與腳本位於同一目錄），忽略編碼錯誤。將整個內容讀入 `full_text` 並去除空白字元。
- **分割邏輯**：嘗試將文字分割為「文件」（邏輯區塊，如段落或文章）：
  - **主要**：以雙換行符（`\n\n`）分割，這在語料庫中分隔文件很常見。
  - **後備 1**：如果分割後只有 ≤1 個區塊（例如，沒有雙換行符），則以單換行符（`\n`）分割以處理基於行的文字。
  - **後備 2**：如果仍然只有 ≤1 個區塊（例如，單個文字塊），則以 `. `（句點 + 空格）分割成句子，然後將每 100 個句子分組為一個「文件」區塊。這可以防止單個條目過長。為了完整性，在每個區塊的末尾添加一個句點。
- **輸出**：將非空、去除空白字元的文件儲存在 `texts` 列表中。列印建立的總數（例如，子集為 10k 個範例）。
- **為何如此？** OpenWebText 是網頁的串接，因此分割後建立的訓練範例不僅僅是原始傾印。這模仿了 BookCorpus 等資料集的處理方式。

#### 3. 建立與分割資料集
```python
    # Create dataset from texts
    dataset = datasets.Dataset.from_dict({'text': texts})

    # create train/val split from the 10k examples
    split_dataset = dataset.train_test_split(test_size=0.0005, seed=2357, shuffle=True)
    split_dataset['val'] = split_dataset.pop('test') # rename the test split to val
```
- **資料集建立**：將 `texts` 列表包裝成 Hugging Face `Dataset`，其中包含單一欄位 `'text'`。這使得像映射這樣的並行操作變得高效。
- **分割**：使用 `train_test_split` 將其分為訓練集 (99.95%) 和測試集 (0.05%)。小的驗證集大小是針對龐大資料集有意為之的——足以進行評估而不浪費計算資源。
  - `test_size=0.0005`：0.05% 用於驗證（例如，從 100k 中約 50 個範例）。
  - `seed=2357`：固定的隨機種子以確保可重現性。
  - `shuffle=True`：在分割前進行隨機化。
- **重新命名**：彈出 `'test'` 並重新命名為 `'val'`。現在 `split_dataset` 是一個包含 `'train'` 和 `'val'` 鍵的字典，每個鍵都是一個 `Dataset` 物件。

#### 4. 標記化函數
```python
    # we now want to tokenize the dataset. first define the encoding function (gpt2 bpe)
    def process(example):
        ids = enc.encode_ordinary(example['text']) # encode_ordinary ignores any special tokens
        ids.append(enc.eot_token) # add the end of text token, e.g. 50256 for gpt2 bpe
        # note: I think eot should be prepended not appended... hmm. it's called "eot" though...
        out = {'ids': ids, 'len': len(ids)}
        return out
```
- **目的**：將文字轉換為模型輸入的標記 ID。
- **`encode_ordinary`**：將文字字串標記化為整數列表（GPT-2 詞彙表）。忽略文字中的任何非標準標記。
- **附加 EOT**：在末尾添加文本結束標記（GPT-2 的 ID 為 50256）。這在訓練期間標示序列邊界。（註解指出可能存在前置與附加的爭論，但在像 GPT 這樣的因果 LM 設定中，附加是常見的。）
- **輸出**：返回一個包含 `'ids'`（標記 ID 列表）和 `'len'`（序列長度，用於後續求和）的字典。

#### 5. 應用標記化
```python
    # tokenize the dataset
    tokenized = split_dataset.map(
        process,
        remove_columns=['text'],
        desc="tokenizing the splits",
        num_proc=num_proc,
    )
```
- **映射**：使用並行工作程序（`num_proc=8`）將 `process` 應用於訓練/驗證資料集中的每個範例。
- **`remove_columns=['text']`**：丟棄原始文字以節省記憶體（現在我們只需要標記）。
- **進度**：透過 `desc` 顯示進度條。由於需要編碼，此步驟對於大型資料集可能需要一些時間。

#### 6. 將標記化資料儲存為二進位檔案
```python
    # concatenate all the ids in each dataset into one large file we can use for training
    for split, dset in tokenized.items():
        arr_len = np.sum(dset['len'], dtype=np.uint64)
        filename = os.path.join(os.path.dirname(__file__), f'{split}.bin')
        dtype = np.uint16 # (can do since enc.max_token_value == 50256 is < 2**16)
        arr = np.memmap(filename, dtype=dtype, mode='w+', shape=(arr_len,))

        # Use adaptive batch size based on dataset size
        total_batches = min(1024, len(dset))
        if total_batches < 1024:
            print(f"Using {total_batches} batches for {split} dataset (size: {len(dset)})")

        idx = 0
        for batch_idx in tqdm(range(total_batches), desc=f'writing {filename}'):
            # Only process if this batch index is valid for the dataset size
            if batch_idx < len(dset):
                # Batch together samples for faster write
                batch = dset.shard(num_shards=total_batches, index=batch_idx, contiguous=True).with_format('numpy')
                arr_batch = np.concatenate(batch['ids'])
                # Write into mmap
                arr[idx : idx + len(arr_batch)] = arr_batch
                idx += len(arr_batch)
        arr.flush()
```
- **循環遍歷分割**：對於 `'train'` 和 `'val'`，透過加總 `'len'` 欄位計算總標記數（`arr_len`）。
- **記憶體映射陣列**：建立一個 NumPy memmap 檔案（`train.bin` 或 `val.bin`）作為 uint16 整數的可寫入陣列（適合 GPT-2 的 50,256 最大標記值；比 int32 節省約 50% 空間）。形狀為一維：`(total_tokens,)`。
- **批次處理以提高效率**：將資料集分割為最多 1024 個分片（`total_batches`），以避免一次將所有內容載入 RAM。對於小型資料集（<1024 個範例），使用確切數量。
  - **`shard`**：將資料集分割為連續的批次（此處不進行洗牌）。
  - **`with_format('numpy')`**：將批次轉換為 NumPy 陣列以進行快速串接。
- **寫入**：將每個批次的標記 ID 串接起來，並從 `idx` 開始依序複製到 memmap 陣列中。使用 `tqdm` 追蹤進度。
- **`flush()`**：確保所有資料寫入磁碟。
- **為何使用二進位/memmap？** 這些檔案很大但可串流處理。在訓練期間，您可以使用 `np.memmap('train.bin', dtype=np.uint16, mode='r')` 載入它們，而無需將所有內容載入記憶體。

#### 7. 關於輸出與使用的註釋
```python
    # train.bin is ~17GB, val.bin ~8.5MB
    # train has ~9B tokens (9,035,582,198)
    # val has ~4M tokens (4,434,897)

    # to read the bin files later, e.g. with numpy:
    # m = np.memmap('train.bin', dtype=np.uint16, mode='r')
```
- 這些是完整 OpenWebText 的範例大小（您的本地檔案可能不同）。
- **讀取提示**：使用 memmap 進行唯讀存取。在訓練循環中，您可以從平坦陣列中取樣隨機起始索引並讀取固定長度的序列（例如，1024 個標記）。

### 潛在問題與注意事項
- **記憶體使用**：對於非常大的檔案（40GB+），將完整的 `openwebtext.txt` 讀入 RAM 可能會失敗。如果需要，請考慮串流讀取。
- **EOT 放置**：註解質疑附加與前置 EOT；在實踐中，附加適用於自回歸模型（它在內容之後標記結束）。
- **自訂**：假設有一個本地檔案；靈感程式碼從 Hugging Face 下載，但此版本從本地讀取（更快，無需驗證）。
- **相依性**：需要 `tiktoken`、`datasets`、`numpy`、`tqdm`。如果缺少，請透過 pip 安裝。
- **可擴展性**：對於真實的 OpenWebText，請在具有 64GB+ RAM 和快速儲存（SSD）的機器上運行。10k 範例分割表明這可能用於子集。

此腳本將原始文字轉換為訓練就緒的格式，並針對像 GPT 這樣的語言模型進行了最佳化。如果您對修改它有疑問（例如，不同的 tokenizer 或區塊大小），請告訴我！