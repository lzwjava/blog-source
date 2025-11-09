---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 標準ナノGPTトレーニング反復回数
translated: true
type: note
---

nanoGPTのデフォルト設定（例：Shakespeareキャラクターデータセットでの学習）では、モデルは合計**5000イテレーション**実行されます。

これは`config/train_shakespeare_char.py`ファイル内の`max_iters = 5000`によって設定されています。`train.py`を実行する際に、コマンドラインで`--max_iters=<値>`を指定することで上書きできます。

[config/train_shakespeare_char.py](https://huggingface.co/nindanaoto/nanoGPT-BitNet158b/blob/main/config/train_shakespeare_char.py)