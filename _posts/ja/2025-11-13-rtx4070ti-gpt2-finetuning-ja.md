---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: RTX 4070 Ti GPT-2 ファインチューニングガイド
translated: true
type: note
---

## 環境構築

トレーニングを開始する前に、NVIDIA RTX 4070 Tiが正しくセットアップされていることを確認してください。このGPUは12GBのVRAMを搭載しており、ファインチューニング中のGPT-2 Small（1.24億パラメータ）には十分以上の容量です。OpenWebTextのような大規模なデータセットでのスクラッチからのトレーニングは、時間と計算リソースの要件から、単一のコンシューマー向けGPUでは非現実的です（数週間から数ヶ月かかります）。代わりに、特定のタスク向けに事前学習済みモデルを独自のデータセットでファインチューニングすることに集中してください。

### 1. NVIDIAドライバとCUDAのインストール
- 公式NVIDIAウェブサイトからRTX 4070 Ti用の最新のNVIDIAドライバをダウンロードしてインストールしてください。完全な互換性のために、バージョン535以上であることを確認してください。
- CUDA Toolkitをインストールしてください。RTX 4070 Ti（コンピュート能力8.9）はCUDA 12.xをサポートしています。CUDA 12.4を推奨します：
  - NVIDIA CUDA Toolkitアーカイブからダウンロードします。
  - お使いのOS（Windows/Linux）用のインストールガイドに従ってください。
- 使用するCUDAバージョンに一致するcuDNN（CUDA Deep Neural Network library）をインストールしてください（例：CUDA 12.4用のcuDNN 8.9）。
- インストールを確認します：
  ```
  nvidia-smi  # GPUとCUDAバージョンが表示されるはず
  nvcc --version  # CUDAのインストールを確認
  ```

### 2. Python環境のセットアップ
- Python 3.10または3.11を使用してください。管理を容易にするためにAnacondaまたはMiniconda経由でインストールします。
- 仮想環境を作成します：
  ```
  conda create -n gpt2-train python=3.10
  conda activate gpt2-train
  ```

### 3. 必要なライブラリのインストール
- CUDAサポート付きのPyTorchをインストールします。CUDA 12.4の場合：
  ```
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
  ```
  確認：
  ```
  python -c "import torch; print(torch.cuda.is_available())"  # Trueが返るはず
  ```
- Hugging Faceのライブラリなどをインストールします：
  ```
  pip install transformers datasets accelerate sentencepiece pandas tqdm
  ```

## データセットの準備
- テキストデータセットを選択または準備します（例：1行に1サンプルが含まれる.txtファイル、または'text'カラムを持つCSVファイル）。
- 例えば、Hugging Face Datasetsから公開データセットを使用します：
  ```python
  from datasets import load_dataset
  dataset = load_dataset("bookcorpus")  # またはカスタムデータセット: load_dataset("text", data_files="your_data.txt")
  ```
- 必要に応じてトレーニング/テストに分割します：
  ```python
  dataset = dataset["train"].train_test_split(test_size=0.1)
  ```

## GPT-2 Smallのファインチューニング
シンプルさのためにHugging Face Transformersライブラリを使用します。以下は、因果言語モデリング（次のトークンの予測）のための完全なスクリプトです。

### スクリプト例
これを`train_gpt2.py`として保存し、`python train_gpt2.py`で実行します。

```python
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

# トークナイザーとモデル（GPT-2 Small）の読み込み
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token  # パディングトークンを設定
model = GPT2LMHeadModel.from_pretrained("gpt2")

# データセットの読み込みと前処理（独自のデータセットに置き換えてください）
dataset = load_dataset("bookcorpus")
dataset = dataset["train"].train_test_split(test_size=0.1)

def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, max_length=512, padding="max_length")

tokenized_dataset = dataset.map(preprocess, batched=True, remove_columns=["text"])

# 言語モデリング用のデータコレーター
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# トレーニング引数（単一GPU用に最適化）
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",
    evaluation_strategy="epoch",
    learning_rate=5e-5,
    per_device_train_batch_size=4,  # VRAMに基づいて調整。OOMを避けるために低く始める
    per_device_eval_batch_size=4,
    num_train_epochs=3,  # 必要に応じて調整
    weight_decay=0.01,
    fp16=True,  # 混合精度でトレーニングを高速化しVRAM使用量を削減
    gradient_accumulation_steps=4,  # 実効バッチサイズ = batch_size * accumulation_steps
    save_steps=1000,
    logging_steps=500,
    report_to="none",  # または追跡用に "wandb"
)

# トレーナー
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    data_collator=data_collator,
)

# トレーニング
trainer.train()

# モデルの保存
trainer.save_model("./gpt2-finetuned")
```

### トレーニングの実行
- 別のターミナルで`nvidia-smi`を使用してGPU使用率を監視します。
- メモリ不足（OOM）エラーが発生した場合：
  - `per_device_train_batch_size`を2または1に減らします。
  - 実効バッチサイズを維持するために`gradient_accumulation_steps`を増やします。
  - より小さいmax_length（例：512の代わりに256）を使用します。
- トレーニング時間：4070 Tiでは、中規模のデータセット（例：10万サンプル）で、バッチサイズに応じてエポックあたり1〜5時間を想定します。

## 評価と推論
トレーニング後：
```python
from transformers import pipeline

generator = pipeline("text-generation", model="./gpt2-finetuned", device=0)  # GPU用にdevice=0
output = generator("Your prompt here", max_length=50, num_return_sequences=1)
print(output)
```

- パープレキシティを評価します（低いほど良い）：
  ```python
  import math
  eval_results = trainer.evaluate()
  perplexity = math.exp(eval_results["eval_loss"])
  print(f"Perplexity: {perplexity}")
  ```

## ヒントとトラブルシューティング
- VRAMを節約しトレーニングを高速化するために混合精度（`fp16=True`）を使用します。
- スクラッチからのトレーニング（非推奨）の場合：カスタムトランスフォーマーアーキテクチャ（例：NanoGPTまたは類似のリポジトリ経由）を実装し、大規模なデータセットを使用しますが、非常に長い実行時間を想定してください。
- より大きなデータセットの場合、複数のGPUがある場合は分散トレーニングを使用しますが、それは単一の4070 Tiを超えます。
- 一般的な問題：PyTorchがGPUを検出しない場合、ドライバ/CUDAを再インストールしてください。他のプロセスがGPUを使用していないことを確認してください。

## 参考文献
- [Fine-Tuning GPT-2: A Practical Guide](https://mr-amit.medium.com/fine-tuning-gpt-2-a-practical-guide-2805b4af738b)
- [Training GPT-2 From Scratch: A Step-by-Step Guide](https://youssefh.substack.com/p/training-gpt-2-from-scratch-a-step)
- [How To Train Your Own GenAI Model](https://developer.squareup.com/blog/how-to-train-your-own-genai-model/)
- [How To Make Custom AI-Generated Text With GPT-2](https://minimaxir.com/2019/09/howto-gpt2/)
- [RTX 4070 CUDA version](https://www.reddit.com/r/pytorch/comments/1kwb5fh/rtx_4070_cuda_version/)
- [Geforce RTX 4070 Ti Super CUDA support for Deep Learning](https://forums.developer.nvidia.com/t/geforce-rtx-4070-ti-super-cuda-support-for-deep-learning/282154)
- [CUDA compatibility with RTX 4070](https://forums.developer.nvidia.com/t/cuda-compatibility-with-rtx-4070/287989)