---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 使用 Homebrew 升級 Ollama
translated: true
type: note
---

要使用 Homebrew 在 macOS 上將 Ollama 升級至最新版本（截至 2025 年 7 月為 v0.10.0），請按照以下步驟操作：

1. 更新 Homebrew 的配方，確保其知曉最新的可用版本：
   ```
   brew update
   ```

2. 特別升級 Ollama：
   ```
   brew upgrade ollama
   ```

3. 透過檢查版本來驗證升級：
   ```
   ollama --version
   ```

如果您將 Ollama 作為背景服務運行，請在升級後重新啟動它：
```
brew services restart ollama
```

或者，如果您手動運行它，請停止任何現有進程，並使用您偏好的指令重新啟動（例如，從安裝輸出中的注意事項）：
```
OLLAMA_FLASH_ATTENTION="1" OLLAMA_KV_CACHE_TYPE="q8_0" /opt/homebrew/opt/ollama/bin/ollama serve
```

除了這個標準流程外，無需其他特殊的升級說明。

[Ollama 版本發布](https://github.com/ollama/ollama/releases)