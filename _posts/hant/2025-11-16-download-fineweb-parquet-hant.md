---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 下載特定 FineWeb Parquet 檔案
translated: true
type: note
---

你只想從某個 Common Crawl 資料集（例如 CC-MAIN-2013-20）下載使用幾個 parquet 檔案，而不是整個 15T token 的 FineWeb 巨無霸——這完全合理！以下是 2025 年最簡單的實現方法。

### 方法一：使用 huggingface_hub 直接下載（推薦，速度最快）
這方法僅以全速下載你所需的 parquet 檔案（若啟用 hf-transfer 可達 ~GB/s）。

```bash
# 1. 安裝/升級
pip install -U "huggingface_hub[hf_transfer]"

# 2. 啟用快速下載（非常重要！）
export HF_HUB_ENABLE_HF_TRANSFER=1   # Linux/macOS
# 或在 Windows PowerShell：
# $env:HF_HUB_ENABLE_HF_TRANSFER = "1"

# 3. 僅下載你需要的幾個 parquet 檔案
huggingface-cli download HuggingFaceFW/fineweb \
    data/CC-MAIN-2013-20/000_00000.parquet \
    data/CC-MAIN-2013-20/000_00001.parquet \
    data/CC-MAIN-2013-20/000_00002.parquet \
    --repo-type dataset --local-dir fineweb-2013-20
```

完成！你現在可以在 `fineweb-2013-20/` 資料夾中找到三個約 2.15 GB 的 parquet 檔案。

### 方法二：單行 Python 腳本下載指定檔案
```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="HuggingFaceFW/fineweb",
    repo_type="dataset",
    allow_patterns=[
        "data/CC-MAIN-2013-20/000_00000.parquet",
        "data/CC-MAIN-2013-20/000_00001.parquet",
        # 可在此添加更多檔案
    ],
    local_dir="fineweb-2013-20"
)
```

### 如何本地讀取 Parquet 檔案
```python
import pandas as pd
# 或使用 pyarrow 提升速度並降低記憶體使用
import pyarrow.parquet as pq
import pyarrow.dataset as ds

# 最快方式（無需將所有資料載入記憶體即可串流處理）
dataset = ds.dataset("fineweb-2013-20/data/CC-MAIN-2013-20/", format="parquet")

for batch in dataset.to_batches(batch_size=1024):
    df = batch.to_pandas()
    for text in df["text"]:
        # 可進行任意操作：分詞、過濾、寫入 jsonl 等
        print(text[:200])  # 範例
```

或直接使用 pandas（適用於少量檔案）：
```python
df = pd.read_parquet("fineweb-2013-20/data/CC-MAIN-2013-20/000_00000.parquet")
print(df.columns)  # ['text', 'id', 'dump', 'url', 'date', 'file_path', 'language', 'language_score', 'token_count']
print(df.iloc[0]["text"])
```

### CC-MAIN-2013-20 快速統計
- 約 207 個 parquet 檔案 × 約 2.15 GB ≈ 總計 422 GB
- 約 440 億個 token（適合中小型實驗）
- 已由 Hugging Face 完成清理、去重和過濾

這就是你所需的一切。只需選擇任意數量的 `_0000XX.parquet` 檔案（檔案已隨機洗牌），下載選定的檔案，即可立即開始訓練或過濾。