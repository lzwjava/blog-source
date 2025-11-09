---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用 nanoGPT 訓練自訂數據集
translated: true
type: note
---

### 使用 nanoGPT 準備和訓練自訂文本數據集

nanoGPT 設計用於輕鬆訓練文本數據，包括自訂數據集。過程包括將文本準備成二進制令牌文件、配置訓練參數，以及運行訓練腳本。下面我將根據代碼庫的示例（例如 Shakespeare 或 OpenWebText）概述步驟。您需要 Python 3.8+ 和 GPU 以進行高效訓練（CPU 也可用但較慢）。

#### 1. 安裝依賴項
首先，設置環境：
```
pip install torch numpy transformers datasets tiktoken wandb tqdm
```
- `torch`：用於 PyTorch（如果使用 GPU，請安裝 CUDA 版本：例如 `pip install torch --index-url https://download.pytorch.org/whl/cu118`）。
- 其他庫處理令牌化、數據加載和日誌記錄。

#### 2. 準備自訂數據集
nanoGPT 期望數據為二進制文件（`train.bin` 和 `val.bin`），其中包含令牌化的整數。您需要編寫一個簡單的準備腳本來處理原始文本。

- **放置文本文件**：將原始文本（例如 `input.txt`）放在 `data/` 下的新文件夾中，例如 `data/my_dataset/`。
  
- **創建準備腳本**：從代碼庫複製並修改示例（例如 `data/shakespeare_char/prepare.py` 用於字符級別，或 `data/openwebtext/prepare.py` 用於 GPT-2 BPE 令牌級別）。
  
  **字符級別令牌化示例**（適用於小型數據集；將每個字符視為一個令牌）：
  ```python
  # 保存為 data/my_dataset/prepare.py
  import os
  import requests
  import numpy as np
  from torch.utils.data import Dataset, random_split

  # 加載文本（替換為您的文件路徑）
  with open('data/my_dataset/input.txt', 'r', encoding='utf-8') as f:
      text = f.read()

  # 編碼為字符
  chars = sorted(list(set(text)))
  vocab_size = len(chars)
  stoi = {ch: i for i, ch in enumerate(chars)}
  itos = {i: ch for i, ch in enumerate(chars)}
  def encode(s): return [stoi[c] for c in s]
  def decode(l): return ''.join([itos[i] for i in l])

  # 令牌化整個文本
  data = torch.tensor(encode(text), dtype=torch.long)

  # 分割為訓練/驗證集（90/10）
  n = int(0.9 * len(data))
  train_data = data[:n]
  val_data = data[n:]

  # 保存為 .bin 文件
  train_data = train_data.numpy()
  val_data = val_data.numpy()
  train_data.tofile('data/my_dataset/train.bin')
  val_data.tofile('data/my_dataset/val.bin')

  # 打印統計信息
  print(f"Length of dataset in characters: {len(data)}")
  print(f"Vocab size: {vocab_size}")
  ```
  運行它：
  ```
  python data/my_dataset/prepare.py
  ```
  這將創建 `train.bin` 和 `val.bin`。

- **GPT-2 BPE 令牌化**（適用於較大數據集；使用子詞）：
  修改 `data/openwebtext/prepare.py`。您需要安裝 `tiktoken`（已在依賴項中）並類似地處理文本，但使用 `tiktoken.get_encoding("gpt2").encode()` 而不是字符編碼。將文本分割為訓練/驗證塊（例如 90/10），然後保存為 NumPy 數組到 `.bin`。

- **提示**：
  - 保持數據集清潔（例如，如果需要，移除特殊字符）。
  - 對於非常大的文件，分塊處理以避免內存問題。
  - 詞彙大小：字符約為 65（Shakespeare）；BPE 約為 50k。

#### 3. 配置訓練
通過複製示例（例如 `config/train_shakespeare_char.py`）創建配置文件到 `config/train_my_dataset.py` 並編輯它。

需要調整的關鍵參數：
```python
# 示例配置片段
out_dir = 'out-my_dataset'  # 檢查點輸出文件夾
dataset = 'my_dataset'      # 與您的數據文件夾名稱匹配
batch_size = 64             # 根據 GPU 內存調整（例如，小型 GPU 為 12）
block_size = 256            # 上下文長度（每個示例的令牌數）
n_layer = 6                 # Transformer 層數
n_head = 6                  # 注意力頭數
n_embd = 384                # 嵌入維度
max_iters = 5000            # 訓練步數
lr = 6e-4                   # 學習率
dropout = 0.2               # 丟棄率
init_from = 'scratch'       # 'scratch' 用於新模型；'gpt2' 加載預訓練模型
```
- 用於微調（從預訓練 GPT-2 開始）：設置 `init_from = 'gpt2'`（或 'gpt2-medium'）。
- 對於 Apple Silicon：添加 `device = 'mps'`。
- 默認每 500 次迭代保存檢查點。

#### 4. 運行訓練
從頭開始訓練或微調：
```
python train.py config/train_my_dataset.py
```
- 對於多 GPU（例如 8 個 GPU）：`torchrun --standalone --nproc_per_node=8 train.py config/train_my_dataset.py`。
- 使用 WandB 監控（記錄損失、樣本；在配置中啟用 `wandb_log = True`）。
- 訓練時間：GPU 上小型模型需幾分鐘；較大模型需幾小時/天。

#### 5. 生成樣本（測試模型）
訓練後，生成文本：
```
python sample.py --out_dir=out-my_dataset --start="您的提示在此"
```
這將加載最新檢查點並生成。

#### 常見問題
- **內存錯誤**：減少 `batch_size` 或 `block_size`。
- **無 GPU**：在命令中添加 `--device=cpu --compile=False`。
- **大型數據集**：使用分佈式訓練進行擴展。

更多詳細信息，請查閱代碼庫的 README 和數據/配置示例。

[nanoGPT GitHub](https://github.com/karpathy/nanoGPT)