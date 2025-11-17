---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: FineWebデータのダウンロードと準備
translated: true
type: note
---

### Parquetファイルのダウンロード

提供されたURLは、FineWebデータセット（CommonCrawlデータのクリーンなサブセット）の特定のParquetファイルを指しています。このファイル（`CC-MAIN-2013-20`ダンプの`000_00000.parquet`）には、約100万行の英語ウェブテキストが含まれており、各行には言語モデルトレーニング用に事前処理済みの`text`カラム（HTML除去、重複排除、Trafilaturaなどのツールによる品質フィルタリング済み）が含まれています。

ダウンロード方法：
- Hugging Face CLIを使用: `huggingface-cli download HuggingFaceFW/fineweb data/CC-MAIN-2013-20/000_00000.parquet --local-dir ./fineweb_data`
- またはPythonの`huggingface_hub`を使用:
  ```python
  from huggingface_hub import hf_hub_download

  file_path = hf_hub_download(
      repo_id="HuggingFaceFW/fineweb",
      filename="data/CC-MAIN-2013-20/000_00000.parquet",
      local_dir="./fineweb_data"
  )
  print(f"Downloaded to: {file_path}")
  ```
これにより、約500MBのファイルがローカルに保存されます（例: `./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet`）。

完全なダンプ（数百ファイル）には、データセットドキュメントで示されているように`snapshot_download`を使用しますが、テストにはこの単一ファイルから始めてください。

### テキストの抽出

FineWebの`text`カラムはトレーニング準備済みのプレーンテキストです—HTMLや生HTMLを解析する必要はありません。効率的に読み込むには`pandas`または`pyarrow`を使用します。方法は以下の通り：

1. **依存関係のインストール**（必要な場合）: `pip install pandas pyarrow datasets`（NanoGPTセットアップで既にあると仮定）。

2. **Parquetファイルの読み込みとテキスト抽出**:
   ```python
   import pandas as pd
   import os

   # ダウンロードしたファイルへのパス
   parquet_path = "./fineweb_data/data/CC-MAIN-2013-20/000_00000.parquet"

   # Parquetファイルの読み込み（大容量ファイルに効率的）
   df = pd.read_parquet(parquet_path, columns=['text'])  # メモリ節約のためtextカラムのみ読み込み

   # すべてのテキストをリストに抽出（メモリ制約がある場合は反復処理）
   texts = df['text'].tolist()  # 約100万文字列のリスト

   # オプション: 基本的なクリーニング（FineWebは既にクリーンだが、空白文字を正規化）
   import re
   def clean_text(text):
       if pd.isna(text):  # nullをスキップ（FineWebでは稀）
           return ''
       text = re.sub(r'\s+', ' ', text.strip())  # 空白文字を圧縮
       return text if len(text) > 10 else ''  # 非常に短いテキストをフィルタリング

   cleaned_texts = [clean_text(t) for t in texts if t]  # フィルタを適用

   print(f"Extracted {len(cleaned_texts)} text samples")
   print("Sample:", cleaned_texts[0][:200] + "...")  # 最初のテキストをプレビュー
   ```

   - **メモリのヒント**: このファイルは約100万行、各テキストは約1-5k文字です。16GB RAMのマシンでは問題なく読み込めます。より大きなダンプには、チャンク読み込みのために`pyarrow`を使用:
     ```python
     import pyarrow.parquet as pq

     table = pq.read_table(parquet_path, columns=['text'])
     texts = table['text'].to_pylist()
     ```

   - **ストリーミング代替案**（完全なダウンロード不要）: `datasets`ライブラリを使用してすべてを読み込まずに反復処理:
     ```python
     from datasets import load_dataset

     # ストリーミングモードで特定のダンプを読み込み
     dataset = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)

     texts = []
     for i, sample in enumerate(dataset):
         if i >= 100000:  # テスト用に制限
             break
         texts.append(sample['text'])

     # 上記のようにクリーニング
     ```

### NanoGPTトレーニングの準備

NanoGPTは、特別なトークン（例: `"<|endoftext|>"`）で区切られた連結ドキュメントを含む単一のテキストファイル（例: `input.txt`）を期待します。抽出したテキストをフォーマットする方法は以下の通り：

```python
# 上記からcleaned_textsを抽出後
with open('input.txt', 'w', encoding='utf-8') as f:
    for text in cleaned_texts:
        f.write(text + "\n<|endoftext|>\n")  # NanoGPTのデフォルト区切り文字

print("Saved to input.txt – ready for NanoGPT!")
```

- **このフォーマットの理由**: NanoGPTの`data.py`スクリプトは`input.txt`を読み込み、トークナイザ（例: GPT-2）でエンコードし、train/val分割を作成します。各ドキュメントは`"<|endoftext|>"`で終了し、ドキュメント間のコンテキスト混入を防ぎます。
- **カスタマイズ**:
  - 長さでフィルタリング: 書き込み前に`if 100 < len(text.split()) < 10000:`を追加して中規模ドキュメントを維持。
  - テスト用サブセット: クイック10kサンプル実行に`cleaned_texts[:10000]`を使用。
  - トレーニングコマンド: `input.txt`の準備ができたら、NanoGPTで`python train.py`を実行（必要に応じて`--dataset=input.txt`を調整）。

この単一ファイルは約5-10Bトークンを提供します—ファインチューニングに最適です。さらに必要であれば、追加のParquetファイルをダウンロードして連結してください。メモリ問題が発生した場合やNanoGPT設定のヘルプが必要な場合は、詳細を共有してください！

**参照**: [FineWeb Dataset Card](https://huggingface.co/datasets/HuggingFaceFW/fineweb)