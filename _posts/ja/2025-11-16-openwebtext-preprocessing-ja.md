---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: OpenWebTextデータセット前処理スクリプト
translated: true
type: note
---

### 概要
このPythonスクリプトは、OpenWebTextデータセット（GPT-2のようなモデルのトレーニングに使用されるものと同様のウェブスクレイピングテキストのコーパス）を含む大規模なテキストファイルを処理します。目的は以下の通りです：
- 生テキストを管理可能な「ドキュメント」（テキストのチャンク）に分割する
- Hugging Faceの`Dataset`オブジェクトを作成し、容易な操作を可能にする
- GPT-2のByte Pair Encoding（BPE）トークナイザーをTikTokenから使用してテキストをトークン化する（特殊トークンを無視し、テキスト終了マーカーを追加）
- データセットをトレーニング用（99.95%）と検証用（0.05%）に分割する
- トークン化されたデータをNumPyのメモリマップ配列を使用してコンパクトなバイナリファイル（`train.bin`および`val.bin`）として保存する。これらのファイルは機械学習トレーニング中の効率的な読み込みのために、トークンIDのシーケンス（16ビット整数として）を格納する

このスクリプトは、トークン化にマルチプロセッシングを使用するマルチコアシステムでの効率性を考慮して設計されています。これは、言語モデルトレーニングのための同様の前処理を扱うFlash Attentionリポジトリ（コード内でリンク）のデータローディングモジュールに触発されています。注意：OpenWebTextは巨大（非圧縮で約40GB）ですが、このスクリプトは事前にダウンロード済みのローカル`openwebtext.txt`ファイルを想定しています。出力ファイルははるかに小さくなります：`train.bin`は約17GB（90億トークン）、`val.bin`は約8.5MB（400万トークン）。

スクリプトは開始時にプロキシ設定を表示します（暗黙的なダウンロード中のネットワーク問題のデバッグ用と思われるが、ここでは明示的なダウンロードはない）。デフォルトで8つのワーカープロセスをトークン化に使用します。

### ステップバイステップの詳細

#### 1. インポートと初期設定
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
- **目的**: ファイル操作（`os`、`tarfile`）、プログレスバー（`tqdm`）、数値演算（`numpy`）、トークン化（`tiktoken`）、Hugging Faceユーティリティ（`huggingface_hub`、`datasets`）のためのライブラリをインポート
- **プロキシ表示**: HTTP/HTTPSプロキシの環境変数をログ出力（ネットワーク制限に遭遇した場合に有用。例：トークナイザーモデルのダウンロード時。ただしTikTokenは内部的に処理）
- **ワーカー**: トークン化の並列処理のために`num_proc=8`を設定（CPUコア数の約半分でバランスを取る）。`num_proc_load_dataset`はこれに合わせているが、ここでは使用されない（Hugging Faceからロードする元コードの名残）
- **エンコーダ**: GPT-2 BPEトークナイザー（`enc`）をロード。これはテキストを整数のトークンID（0–50,256範囲）に変換する
- **ロギング**: Hugging Face datasetsのロギングを「info」レベルに設定し、処理中の詳細な出力を可能にする

`if __name__ == '__main__':`ガードは、スクリプトが直接実行されたとき（インポートされていないとき）のみメインロジックが実行されることを保証する

#### 2. テキストファイルの読み込みと分割
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
- **ファイル読み込み**: `openwebtext.txt`（スクリプトと同じディレクトリにあると想定）をUTF-8モードで開き、エンコーディングエラーを無視。全内容を`full_text`に読み込み、空白を除去
- **分割ロジック**: テキストを「ドキュメント」（段落や記事のような論理的なチャンク）に分割しようと試みる：
  - **主要**: 二重改行（`\n\n`）で分割。コーパスでのドキュメント分離に一般的
  - **代替1**: チャンクが1つ以下（例：二重改行なし）の場合、単一改行（`\n`）で分割し、行ベースのテキストに対応
  - **代替2**: まだチャンクが1つ以下の場合（例：単一テキストブロック）、`. `（ピリオド＋スペース）で文に分割し、100文ごとに「ドキュメント」チャンクにグループ化。単一エントリが長くなりすぎるのを防ぐ。完全性のために各チャンクの末尾にピリオドを追加
- **出力**: 空でない、空白を除去したドキュメントを`texts`リストに格納。作成された総数を表示（例：サブセットで10k例）
- **この方法の理由**: OpenWebTextはウェブページの連結であるため、分割により生のダンプではないトレーニング例が作成される。これはBookCorpusのようなデータセットの処理方法を模倣する

#### 3. データセットの作成と分割
```python
    # Create dataset from texts
    dataset = datasets.Dataset.from_dict({'text': texts})

    # create train/val split from the 10k examples
    split_dataset = dataset.train_test_split(test_size=0.0005, seed=2357, shuffle=True)
    split_dataset['val'] = split_dataset.pop('test') # rename the test split to val
```
- **データセット作成**: `texts`リストをHugging Faceの`Dataset`にラップし、単一カラム`'text'`を持つ。これにより、マッピングのような効率的な並列操作が可能になる
- **分割**: `train_test_split`を使用してトレーニング（99.95%）とテスト（0.05%）セットに分割。小さな検証サイズは、巨大なデータセットでは意図的—計算リソースを無駄にせずに評価するのに十分
  - `test_size=0.0005`: 検証用に0.05%（例：100kから約50例）
  - `seed=2357`: 再現性のための固定乱数シード
  - `shuffle=True`: 分割前にランダム化
- **名前変更**: `'test'`をポップし、`'val'`に名前変更。これで`split_dataset`は`'train'`と`'val'`キーを持つ辞書となり、それぞれが`Dataset`オブジェクト

#### 4. トークン化関数
```python
    # we now want to tokenize the dataset. first define the encoding function (gpt2 bpe)
    def process(example):
        ids = enc.encode_ordinary(example['text']) # encode_ordinary ignores any special tokens
        ids.append(enc.eot_token) # add the end of text token, e.g. 50256 for gpt2 bpe
        # note: I think eot should be prepended not appended... hmm. it's called "eot" though...
        out = {'ids': ids, 'len': len(ids)}
        return out
```
- **目的**: モデル入力のためにテキストをトークンIDに変換
- **`encode_ordinary`**: テキスト文字列を整数のリスト（GPT-2語彙）にトークン化。テキスト内の非標準トークンを無視
- **EOT追加**: 末尾にテキスト終了トークン（GPT-2ではID 50256）を追加。これはトレーニング中のシーケンス境界を示す（コメントでは先頭追加と末尾追加の議論に言及しているが、GPTのような因果的LM設定では末尾追加が一般的）
- **出力**: `'ids'`（トークンIDのリスト）と`'len'`（後で合計するためのシーケンス長）を持つ辞書を返す

#### 5. トークン化の適用
```python
    # tokenize the dataset
    tokenized = split_dataset.map(
        process,
        remove_columns=['text'],
        desc="tokenizing the splits",
        num_proc=num_proc,
    )
```
- **マッピング**: 並列ワーカー（`num_proc=8`）を使用して、トレーニング/検証データセットのすべての例に`process`を適用
- **`remove_columns=['text']`**: 元のテキストを削除しメモリを節約（トークンのみが必要）
- **進捗**: `desc`でプログレスバーを表示。エンコーディングのため、大規模データセットではこのステップに時間がかかる可能性がある

#### 6. トークン化データのバイナリファイルへの保存
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
- **分割ループ**: `'train'`と`'val'`について、`'len'`フィールドを合計して総トークン数（`arr_len`）を計算
- **メモリマップ配列**: NumPyメモリマップファイル（`train.bin`または`val.bin`）をuint16整数の書き込み可能な配列として作成（GPT-2の最大トークン値50,256に適合。int32より約50%スペース節約）。形状は1次元：`(total_tokens,)`
- **効率のためのバッチ処理**: すべてを一度にRAMにロードするのを避けるため、データセットを最大1024シャード（`total_batches`）に分割。小さなデータセット（<1024例）の場合、正確な数を使用
  - **`shard`**: データセットを連続したバッチに分割（ここではシャッフルなし）
  - **`with_format('numpy')`**: 高速な連結のためにバッチをNumPy配列に変換
- **書き込み**: 各バッチからトークンIDを連結し、`idx`から始まるメモリマップ配列に順次コピー。`tqdm`で進捗を追跡
- **`flush()`**: すべてのデータがディスクに書き込まれることを保証
- **バイナリ/メモリマップの理由**: これらのファイルは巨大だがストリーミング可能。トレーニング中、`np.memmap('train.bin', dtype=np.uint16, mode='r')`でメモリにすべてをロードせずに読み込める

#### 7. 出力と使用法に関するコメント
```python
    # train.bin is ~17GB, val.bin ~8.5MB
    # train has ~9B tokens (9,035,582,198)
    # val has ~4M tokens (4,434,897)

    # to read the bin files later, e.g. with numpy:
    # m = np.memmap('train.bin', dtype=np.uint16, mode='r')
```
- これらは完全なOpenWebTextの例示サイズ（ローカルファイルは異なる可能性がある）
- **読み取りのヒント**: 読み取り専用アクセスにメモリマップを使用。トレーニングループでは、フラット配列からランダムな開始インデックスをサンプリングし、固定長シーケンス（例：1024トークン）を読み取ることができる

### 潜在的な問題と注意点
- **メモリ使用量**: 非常に大きなファイル（40GB以上）の場合、完全な`openwebtext.txt`をRAMに読み込むと失敗する可能性がある。必要に応じてストリーミング読み込みを検討
- **EOT配置**: コメントではEOTの末尾追加と先頭追加について疑問を呈している。実際には、自己回帰モデルでは末尾追加が機能する（コンテンツの後に終了を示す）
- **カスタマイズ**: ローカルファイルを想定。元のコードはHugging Faceからダウンロードするが、このバージョンはローカルで読み取る（高速、認証不要）
- **依存関係**: `tiktoken`、`datasets`、`numpy`、`tqdm`が必要。不足している場合はpipでインストール
- **スケーラビリティ**: 実際のOpenWebTextでは、64GB以上のRAMと高速ストレージ（SSD）を搭載したマシンで実行。10k例の分割は、サブセット用であることを示唆

このスクリプトは生テキストをGPTのような言語モデルのトレーニング準備が整った形式に変換し、最適化します。変更（例：異なるトークナイザーやチャンクサイズ）に関する質問があれば、お知らせください！