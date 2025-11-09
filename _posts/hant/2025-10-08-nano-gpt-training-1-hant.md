---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 預設 nanoGPT 訓練迭代次數
translated: true
type: note
---

在 nanoGPT 的預設配置中（例如使用莎士比亞字元資料集進行訓練），模型總共會執行 **5000 次迭代**。

此設定由 `config/train_shakespeare_char.py` 檔案中的 `max_iters = 5000` 所定義。您可以在執行 `train.py` 時透過命令列參數 `--max_iters=<數值>` 來覆寫此設定。

[config/train_shakespeare_char.py](https://huggingface.co/nindanaoto/nanoGPT-BitNet158b/blob/main/config/train_shakespeare_char.py)