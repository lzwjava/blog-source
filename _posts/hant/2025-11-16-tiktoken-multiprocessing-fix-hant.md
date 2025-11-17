---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 Tiktoken 多進程 Pickle 錯誤
translated: true
type: note
---

你在使用 `datasets.map(..., num_proc>1)` 搭配自定義分詞器（例如 nanoGPT 的 FineWeb 腳本中使用的 Tiktoken 編碼器）時遇到的錯誤非常常見 —— 分詞器會加載 BPE 文件（`cl100k_base.tiktoken` 或類似文件），而這個文件句柄在 Linux 上（基於 fork 的多進程處理）**無法被 pickle** 並傳送到子進程。

子進程會立即崩潰 → 出現「其中一個子進程意外終止」的錯誤。

### 快速修復（99% 情況下有效）

編輯 `data/fineweb/prepare.py`，強制分詞化過程僅在**主進程**中運行：

```python
# 在大約第 80-85 行，找到 .map() 調用並將 num_proc=8 改為 num_proc=1

tokenized = raw_datasets.map(
    tokenize,
    num_proc=1,               # ← 修改這一行（或直接刪除該參數）
    desc="tokenizing the splits",
)
```

這樣速度會較慢（單核運行），但能穩定運行。在 FineWeb-10B 上，根據你的 CPU/硬盤速度，大約需要 30-60 分鐘。

### 更好的修復方法（保持多進程處理，速度仍快）

讓分詞器在工作進程內部延遲加載，而不是在全局範圍內加載。

將當前的分詞器創建代碼（大約第 40-50 行）替換為以下模式：

```python
import tiktoken

# 刪除全局的 encoder = tiktoken.get_encoding("cl100k_base")

def get_encoder():
    """在每個子進程中延遲加載分詞器"""
    return tiktoken.get_encoding("cl100k_base")

def tokenize(example):
    enc = get_encoder()                                   # ← 每個進程獨立加載
    ids = enc.encode_ordinary(example["text"])
    ids.append(enc.eot_token)  # 或按照腳本原有的操作
    return {"ids": ids, "len": len(ids)}
```

然後保持 `num_proc=8`（或任意數字）。這樣每個工作進程在 fork 後會加載自己的 .tiktoken 文件副本 → 沒有 pickle 問題。

### 更快的替代方案（推薦用於重複運行）

預先從 Hugging Face 下載 10B/100B 的 FineWeb-Edu 分片，並使用 Karpathy 更新的腳本，該腳本直接處理 parquet/arrow 文件，而不是巨大的 .txt 文件：

```bash
# 速度更快且完全避免此錯誤
python data/fineweb/prepare_fineweb.py --version 10B
# 或 100B
```

新腳本（約 2024 年添加）使用官方的 HF 數據集，並且對多進程處理是安全的。

### 總結

| 解決方案                          | 速度       | 複雜度       | 推薦程度         |
|-----------------------------------|------------|--------------|------------------|
| `num_proc=1`                      | 慢         | 1 行代碼修改 | 快速修復         |
| 在 tokenize() 內部使用延遲加載編碼器 | 快         | 小幅度修改   | 最適合 .txt 文件 |
| 使用新的 prepare_fineweb.py 腳本  | 最快       | 新命令       | 推薦使用         |

選擇其中一種方法，你就能立即解決這個錯誤。告訴我你選擇了哪種方式，如果需要，我會提供確切的修補代碼！