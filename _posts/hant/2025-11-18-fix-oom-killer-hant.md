---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 FineWeb 指令碼中的記憶體終結程式
translated: true
type: note
---

出現「Killed」訊息而沒有 Python 追蹤記錄，意味著 Linux OOM（記憶體不足）終結程式終止了該進程。這發生在 `data/fineweb/prepare.py` 腳本中，因為它試圖在進行標記化之前，一次性將整個約 15 GB 的合併文字檔案（`train_fineweb.txt`）載入到 RAM 中，可能是透過類似 `open(...).read()` 的方式。

儘管 FineWeb-Edu 是為串流處理而設計的（官方下載器使用 Hugging Face `datasets` 並以約 1 億個標記為一個分片進行處理，從不將所有資料載入記憶體），但 nanoGPT 的 fineweb 資料夾有一個自訂的本機檔案路徑，對於大型檔案來說記憶體效率不高。

### 快速解決方案（選擇一種）

1. **最佳且推薦：使用官方的串流 FineWeb-Edu 下載器，而非您的本機檔案**  
   完全不要使用 nanoGPT 的 `data/fineweb/prepare.py`。  
   使用 Karpathy 專為 FineWeb-Edu 10B 標記（或更大版本）編寫的新腳本：

   ```bash
   # 從 nanoGPT 根目錄（或任何位置）
   wget https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py
   python fineweb.py
   ```

   這會使用 `datasets.load_dataset(..., streaming=True)` 和多進程處理，以串流方式下載並標記化 FineWeb-Edu sample-10BT（100 億個標記，原始資料約 15-20 GB）。它從不將整個資料集載入 RAM，並在類似 `edu_fineweb10B/` 的資料夾中產生 nanoGPT 預期的完全相同 `.bin` 分片。  
   它在具有 32-64 GB RAM（或甚至更少，如果您在腳本中減少 `num_proc_load_dataset` 和 `num_proc`）的機器上運行良好。

   對於完整的 100B 或 1T 版本，只需將 `remote_name = "sample-10BT"` 更改為 `"100BT"` 或您需要的任何版本。

2. **如果您真的想保留您的 10 個本機 parquet → txt 檔案**  
   修改 `data/fineweb/prepare.py`，使其以區塊方式處理文字，而不是一次性載入全部：

   打開腳本並將大的 `with open(local_file, 'r', encoding='utf-8') as f: data = f.read()` 區塊替換為類似以下的內容：

   ```python
   from tqdm import tqdm
   import tiktoken
   enc = tiktoken.get_encoding("gpt2")

   chunk_size = 1_000_000  # 每個區塊的字元數，可根據需要調整
   tokens = []
   with open(local_file, "r", encoding="utf-8") as f:
       while True:
           chunk = f.read(chunk_size)
           if not chunk:
               break
           tokens.extend(enc.encode_ordinary(chunk))  # 或 enc.encode(chunk)
           print(f"Tokenized so far: {len(tokens)/1e6:.1f}M tokens")
   tokens = np.array(tokens, dtype=np.uint16)
   ```

   這即使對於您的 15 GB 檔案，也能將峰值 RAM 控制在約 10-15 GB 以下。

3. **硬體解決方法（臨時方案，不理想）**  
   - 增加大量交換空間（例如，64-128 GB 的交換檔案）。一旦開始使用交換空間，速度會非常慢，但可能會完成。  
     ```bash
     sudo fallocate -l 64G /swapfile
     sudo chmod 600 /swapfile
     sudo mkswap /swapfile
     sudo swapon /swapfile
     ```
   - 在具有 ≥64 GB RAM 的機器/實例上運行（例如，AWS r6i.4xlarge 或更大規格）。

### 總結
直接運行 build-nanogpt 中的官方 `fineweb.py` — 這是最乾淨的解決方案，也是現在大家處理 FineWeb 時普遍使用的方法。問題在於您合併的 15 GB txt 檔案，而不是 FineWeb 本身。

[官方 FineWeb-Edu 下載器腳本](https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py)  
[FineWeb-Edu 資料集頁面](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)