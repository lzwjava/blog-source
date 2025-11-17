---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: NVIDIA SMIによるGPU使用率の監視
translated: true
type: note
---

GPUの使用状況を時間経過で監視するには、`nvidia-smi`のループフラグを使用するだけです：

**基本的なライブ更新**

```
nvidia-smi -l 1
```

これは1秒ごとに更新されます。`1`は任意の秒数の間隔に置き換えられます。

**より詳細な統計（プロセスごとの使用状況）が必要な場合**

```
nvidia-smi pmon -s um -d 1
```

これはプロセスごとのGPU使用率（`u`）とメモリ使用量（`m`）を毎秒表示します。

**完全なGPU統計を繰り返し表示したい場合**

```
nvidia-smi --query-gpu=timestamp,utilization.gpu,utilization.memory,memory.used,memory.total --format=csv -l 1
```

これは使用率とメモリ情報を含むコンパクトな行を毎秒出力します。

出力をファイルに記録したい場合やカスタムフォーマットが必要な場合はお知らせください。