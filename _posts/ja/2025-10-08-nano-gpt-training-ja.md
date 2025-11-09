---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: カスタムデータセットを用いたnanoGPTトレーニング
translated: true
type: note
---

### カスタムテキストデータセットをnanoGPTで準備・トレーニングする方法

nanoGPTは、カスタムデータセットを含むテキストデータのトレーニングを簡単に行えるように設計されています。このプロセスでは、テキストをバイナリトークンファイルに準備し、トレーニングパラメータを設定し、トレーニングスクリプトを実行する必要があります。以下では、リポジトリの例（ShakespeareやOpenWebTextなど）に基づいて手順を説明します。効率的なトレーニングにはPython 3.8+とGPUが必要です（CPUでも動作しますが遅くなります）。

#### 1. 依存関係のインストール
まず、環境をセットアップします：
```
pip install torch numpy transformers datasets tiktoken wandb tqdm
```
- `torch`: PyTorch用（GPUを使用する場合はCUDA付きでインストール：例 `pip install torch --index-url https://download.pytorch.org/whl/cu118`）。
- その他はトークン化、データローディング、ロギングを処理します。

#### 2. カスタムデータセットの準備
nanoGPTは、トークン化された整数を含むバイナリファイル（`train.bin` と `val.bin`）としてデータを期待します。生のテキストを処理するための簡単な準備スクリプトを作成する必要があります。

- **テキストファイルの配置**: 生のテキスト（例：`input.txt`）を `data/` の下の新しいフォルダ（例：`data/my_dataset/`）に配置します。
  
- **準備スクリプトの作成**: リポジトリから例（文字レベルの場合は `data/shakespeare_char/prepare.py`、GPT-2 BPEトークンレベルの場合は `data/openwebtext/prepare.py`）をコピーして適応させます。
  
  **文字レベルトークン化の例**（小規模データセット向け；各文字をトークンとして扱う）：
  ```python
  # data/my_dataset/prepare.py として保存
  import os
  import requests
  import numpy as np
  from torch.utils.data import Dataset, random_split

  # テキストを読み込む（ファイルパスを置き換えてください）
  with open('data/my_dataset/input.txt', 'r', encoding='utf-8') as f:
      text = f.read()

  # 文字としてエンコード
  chars = sorted(list(set(text)))
  vocab_size = len(chars)
  stoi = {ch: i for i, ch in enumerate(chars)}
  itos = {i: ch for i, ch in enumerate(chars)}
  def encode(s): return [stoi[c] for c in s]
  def decode(l): return ''.join([itos[i] for i in l])

  # テキスト全体をトークン化
  data = torch.tensor(encode(text), dtype=torch.long)

  # トレーニング/検証に分割（90/10）
  n = int(0.9 * len(data))
  train_data = data[:n]
  val_data = data[n:]

  # .binファイルとして保存
  train_data = train_data.numpy()
  val_data = val_data.numpy()
  train_data.tofile('data/my_dataset/train.bin')
  val_data.tofile('data/my_dataset/val.bin')

  # 統計情報を表示
  print(f"データセットの文字数: {len(data)}")
  print(f"語彙サイズ: {vocab_size}")
  ```
  実行：
  ```
  python data/my_dataset/prepare.py
  ```
  これで `train.bin` と `val.bin` が作成されます。

- **GPT-2 BPEトークン化の場合**（大規模データセット向け；サブワードを使用）：
  `data/openwebtext/prepare.py` を適応させます。`tiktoken` をインストールし（依存関係に既に含まれています）、文字エンコーディングの代わりに `tiktoken.get_encoding("gpt2").encode()` を使用してテキストを同様に処理します。テキストをトレーニング/検証チャンク（例：90/10）に分割し、NumPy配列として `.bin` に保存します。

- **ヒント**：
  - データセットをクリーンに保つ（必要に応じて特殊文字を削除するなど）。
  - 非常に大きなファイルの場合、メモリの問題を避けるためにチャンクで処理する。
  - 語彙サイズ：文字の場合〜65（Shakespeare）；BPEの場合〜50k。

#### 3. トレーニングの設定
例（例：`config/train_shakespeare_char.py`）をコピーして `config/train_my_dataset.py` を作成し、編集します。

調整する主要なパラメータ：
```python
# 設定スニペットの例
out_dir = 'out-my_dataset'  # チェックポイント用の出力フォルダ
dataset = 'my_dataset'      # データフォルダ名に一致
batch_size = 64             # GPUメモリに基づいて調整（例：小規模GPUの場合は12）
block_size = 256            # コンテキスト長（例あたりのトークン数）
n_layer = 6                 # Transformerレイヤー数
n_head = 6                  # アテンションヘッド数
n_embd = 384                # 埋め込み次元数
max_iters = 5000            # トレーニングステップ数
lr = 6e-4                   # 学習率
dropout = 0.2               # ドロップアウト率
init_from = 'scratch'       # 新規モデルの場合は'scratch'；事前学習済みを読み込む場合は'gpt2'
```
- ファインチューニングの場合（事前学習済みGPT-2から開始）：`init_from = 'gpt2'`（または 'gpt2-medium'）を設定。
- Apple Siliconの場合：`device = 'mps'` を追加。
- デフォルトで500イテレーションごとにチェックポイントを保存。

#### 4. トレーニングの実行
スクラッチまたはファインチューニングからトレーニング：
```
python train.py config/train_my_dataset.py
```
- マルチGPUの場合（例：8 GPU）：`torchrun --standalone --nproc_per_node=8 train.py config/train_my_dataset.py`。
- WandBで監視（損失、サンプルをログ；設定で `wandb_log = True` にして有効化）。
- トレーニング時間：GPU上の小さなモデルで数分；大規模なモデルで数時間/数日。

#### 5. サンプル生成（モデルのテスト）
トレーニング後、テキストをサンプリング：
```
python sample.py --out_dir=out-my_dataset --start="あなたのプロンプトここに"
```
これにより最新のチェックポイントが読み込まれ、生成が行われます。

#### 一般的な問題
- **メモリエラー**: `batch_size` または `block_size` を減らす。
- **GPUがない場合**: コマンドに `--device=cpu --compile=False` を追加。
- **大規模データセット**: スケーリングには分散トレーニングを使用。

詳細については、リポジトリのREADMEおよびデータ/設定の例を確認してください。

[nanoGPT GitHub](https://github.com/karpathy/nanoGPT)