---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: RTX 4070 Ti GPT-2 微調指南
translated: true
type: note
---

## 設定您的環境

在開始訓練之前，請確保您的 NVIDIA RTX 4070 Ti 已正確設定。此 GPU 擁有 12GB 的 VRAM，對於微調 GPT-2 Small（1.24 億參數）來說綽綽有餘。在單一消費級 GPU 上從零開始訓練大型數據集（如 OpenWebText）由於時間和計算資源的要求，是不切實際的——這將耗費數週甚至數月時間。因此，建議專注於針對特定任務，在預訓練模型的基礎上使用您自己的數據集進行微調。

### 1. 安裝 NVIDIA 驅動程式和 CUDA
- 從 NVIDIA 官方網站下載並安裝適用於您 RTX 4070 Ti 的最新驅動程式。確保版本為 535 或更高，以獲得完全相容性。
- 安裝 CUDA Toolkit。RTX 4070 Ti（計算能力 8.9）支援 CUDA 12.x。推薦使用 CUDA 12.4：
  - 從 NVIDIA CUDA Toolkit 檔案庫下載。
  - 按照適用於您作業系統（Windows/Linux）的安裝指南進行操作。
- 安裝與您 CUDA 版本匹配的 cuDNN（例如，CUDA 12.4 對應 cuDNN 8.9）。
- 驗證安裝：
  ```
  nvidia-smi  # 應顯示您的 GPU 和 CUDA 版本
  nvcc --version  # 確認 CUDA 安裝
  ```

### 2. 設定 Python 環境
- 使用 Python 3.10 或 3.11。建議透過 Anaconda 或 Miniconda 安裝以便管理。
- 建立虛擬環境：
  ```
  conda create -n gpt2-train python=3.10
  conda activate gpt2-train
  ```

### 3. 安裝必要的程式庫
- 安裝支援 CUDA 的 PyTorch。對於 CUDA 12.4：
  ```
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
  ```
  驗證：
  ```
  python -c "import torch; print(torch.cuda.is_available())"  # 應返回 True
  ```
- 安裝 Hugging Face 程式庫及其他：
  ```
  pip install transformers datasets accelerate sentencepiece pandas tqdm
  ```

## 準備您的數據集
- 選擇或準備一個文字數據集（例如，一個每行一個樣本的 .txt 檔案，或包含 'text' 欄位的 CSV 檔案）。
- 例如，使用 Hugging Face Datasets 上的公開數據集：
  ```python
  from datasets import load_dataset
  dataset = load_dataset("bookcorpus")  # 或您的自訂數據集：load_dataset("text", data_files="your_data.txt")
  ```
- 如有需要，分割為訓練/測試集：
  ```python
  dataset = dataset["train"].train_test_split(test_size=0.1)
  ```

## 微調 GPT-2 Small
使用 Hugging Face Transformers 程式庫以簡化流程。以下是一個用於因果語言建模（預測下一個 token）的完整腳本範例。

### 腳本範例
將此儲存為 `train_gpt2.py` 並使用 `python train_gpt2.py` 執行。

```python
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

# 載入 tokenizer 和模型 (GPT-2 Small)
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token  # 設定填充 token
model = GPT2LMHeadModel.from_pretrained("gpt2")

# 載入並預處理數據集（請替換為您的數據集）
dataset = load_dataset("bookcorpus")
dataset = dataset["train"].train_test_split(test_size=0.1)

def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, max_length=512, padding="max_length")

tokenized_dataset = dataset.map(preprocess, batched=True, remove_columns=["text"])

# 用於語言建模的資料整理器
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# 訓練參數（針對單一 GPU 優化）
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",
    evaluation_strategy="epoch",
    learning_rate=5e-5,
    per_device_train_batch_size=4,  # 根據 VRAM 調整；從較低值開始以避免記憶體不足
    per_device_eval_batch_size=4,
    num_train_epochs=3,  # 根據需要調整
    weight_decay=0.01,
    fp16=True,  # 混合精度訓練，可加快速度並減少 VRAM 使用
    gradient_accumulation_steps=4,  # 有效批次大小 = batch_size * accumulation_steps
    save_steps=1000,
    logging_steps=500,
    report_to="none",  # 或使用 "wandb" 進行追蹤
)

# 訓練器
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    data_collator=data_collator,
)

# 開始訓練
trainer.train()

# 儲存模型
trainer.save_model("./gpt2-finetuned")
```

### 執行訓練
- 在另一個終端機中使用 `nvidia-smi` 監控 GPU 使用情況。
- 如果遇到記憶體不足錯誤：
  - 將 `per_device_train_batch_size` 減少到 2 或 1。
  - 增加 `gradient_accumulation_steps` 以維持有效批次大小。
  - 使用較小的 max_length（例如，256 而不是 512）。
- 訓練時間：在 4070 Ti 上，對於中型數據集（例如 10 萬個樣本），根據批次大小，每個 epoch 預計需要 1-5 小時。

## 評估與推論
訓練完成後：
```python
from transformers import pipeline

generator = pipeline("text-generation", model="./gpt2-finetuned", device=0)  # device=0 表示使用 GPU
output = generator("您的提示文字", max_length=50, num_return_sequences=1)
print(output)
```

- 評估困惑度（越低越好）：
  ```python
  import math
  eval_results = trainer.evaluate()
  perplexity = math.exp(eval_results["eval_loss"])
  print(f"Perplexity: {perplexity}")
  ```

## 提示與疑難排解
- 使用混合精度（`fp16=True`）以節省 VRAM 並加速訓練。
- 如果非要從頭開始訓練（不推薦）：實現自訂的 transformer 架構（例如透過 NanoGPT 或類似專案）並使用大型數據集，但請預期運行時間會非常長。
- 對於較大的數據集，如果您擁有多個 GPU，可以使用分散式訓練，但這超出了單一 4070 Ti 的範圍。
- 常見問題：如果 PyTorch 無法偵測到 GPU，請重新安裝驅動程式/CUDA。並確保沒有其他程序正在使用 GPU。

## 參考資料
- [Fine-Tuning GPT-2: A Practical Guide](https://mr-amit.medium.com/fine-tuning-gpt-2-a-practical-guide-2805b4af738b)
- [Training GPT-2 From Scratch: A Step-by-Step Guide](https://youssefh.substack.com/p/training-gpt-2-from-scratch-a-step)
- [How To Train Your Own GenAI Model](https://developer.squareup.com/blog/how-to-train-your-own-genai-model/)
- [How To Make Custom AI-Generated Text With GPT-2](https://minimaxir.com/2019/09/howto-gpt2/)
- [RTX 4070 CUDA version](https://www.reddit.com/r/pytorch/comments/1kwb5fh/rtx_4070_cuda_version/)
- [Geforce RTX 4070 Ti Super CUDA support for Deep Learning](https://forums.developer.nvidia.com/t/geforce-rtx-4070-ti-super-cuda-support-for-deep-learning/282154)
- [CUDA compatibility with RTX 4070](https://forums.developer.nvidia.com/t/cuda-compatibility-with-rtx-4070/287989)