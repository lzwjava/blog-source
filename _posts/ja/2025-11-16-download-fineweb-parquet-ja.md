---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 特定のFineWeb Parquetファイルをダウンロード
translated: true
type: note
---

Common Crawlのダンプ（例：CC-MAIN-2013-20）から、15Tトークンもの巨大なFineWeb全体ではなく、いくつかのparquetファイルだけをダウンロードして使用したい場合があります―まったく合理的な選択です！2025年現在、これを実現する最も簡単な方法をご紹介します。

### 方法1: huggingface_hubを使用した直接ダウンロード（推奨、最速）
これにより、必要なparquetファイルのみを全速力（hf-transferを有効にすると〜GB/s）でダウンロードできます。

```bash
# 1. インストール/アップグレード
pip install -U "huggingface_hub[hf_transfer]"

# 2. 高速ダウンロードを有効化（非常に重要！）
export HF_HUB_ENABLE_HF_TRANSFER=1   # Linux/macOS
# またはWindows PowerShellの場合:
# $env:HF_HUB_ENABLE_HF_TRANSFER = "1"

# 3. 必要なparquetファイルのみをダウンロード
huggingface-cli download HuggingFaceFW/fineweb \
    data/CC-MAIN-2013-20/000_00000.parquet \
    data/CC-MAIN-2013-20/000_00001.parquet \
    data/CC-MAIN-2013-20/000_00002.parquet \
    --repo-type dataset --local-dir fineweb-2013-20
```

これで完了です。`fineweb-2013-20/`フォルダに3つの〜2.15GBのparquetファイルが保存されます。

### 方法2: 特定ファイルをダウンロードするワンライナーPythonスクリプト
```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="HuggingFaceFW/fineweb",
    repo_type="dataset",
    allow_patterns=[
        "data/CC-MAIN-2013-20/000_00000.parquet",
        "data/CC-MAIN-2013-20/000_00001.parquet",
        # 必要に応じて追加
    ],
    local_dir="fineweb-2013-20"
)
```

### ローカルでParquetファイルを読み込む方法
```python
import pandas as pd
# または、速度向上とメモリ使用量削減のためにpyarrowを使用
import pyarrow.parquet as pq
import pyarrow.dataset as ds

# 最速の方法（すべてをRAMに読み込まずにストリーミング）
dataset = ds.dataset("fineweb-2013-20/data/CC-MAIN-2013-20/", format="parquet")

for batch in dataset.to_batches(batch_size=1024):
    df = batch.to_pandas()
    for text in df["text"]:
        # トークン化、フィルタリング、jsonlへの書き込みなど、任意の処理を実行
        print(text[:200])  # 例
```

あるいは、pandasを使用して簡単に（数ファイルの場合に適しています）：
```python
df = pd.read_parquet("fineweb-2013-20/data/CC-MAIN-2013-20/000_00000.parquet")
print(df.columns)  # ['text', 'id', 'dump', 'url', 'date', 'file_path', 'language', 'language_score', 'token_count']
print(df.iloc[0]["text"])
```

### CC-MAIN-2013-20の簡単な統計
- 〜207 parquetファイル × 〜2.15 GB ≈ 合計422 GB
- 〜440億トークン（小規模から中規模の実験に適したサイズ）
- Hugging Faceによって既にクリーニング、重複排除、フィルタリング済み

必要なのはこれだけです。必要な数の`_0000XX.parquet`ファイル（シャッフルされています）を選び、それらだけをダウンロードして、すぐにトレーニングやフィルタリングを開始してください。