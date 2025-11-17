---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用 nvidia-smi 監控 GPU 使用情況
translated: true
type: note
---

要使用 `nvidia-smi` 監看 GPU 使用率隨時間的變化，您只需要使用循環標誌：

**基礎實時更新**

```
nvidia-smi -l 1
```

這會每秒更新一次。您可以將 `1` 替換為任意秒數間隔。

**如需更詳細的統計數據（每個進程的使用情況）**

```
nvidia-smi pmon -s um -d 1
```

這會每秒顯示每個進程的 GPU 使用率（`u`）和記憶體（`m`）。

**如需重複顯示完整 GPU 統計數據**

```
nvidia-smi --query-gpu=timestamp,utilization.gpu,utilization.memory,memory.used,memory.total --format=csv -l 1
```

這會每秒輸出一行包含使用率和記憶體資訊的精簡數據。

如果您需要將輸出記錄到檔案或需要自訂格式，請告訴我。