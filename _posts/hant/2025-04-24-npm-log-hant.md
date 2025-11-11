---
audio: false
generated: true
lang: hant
layout: post
title: NPM 日誌級別
translated: true
type: note
---

NPM (Node Package Manager) 提供多種日誌級別，用於控制執行 npm 指令時的輸出詳細程度。以下由簡至詳列出各級別：

- **silent**：不顯示任何輸出
- **error**：僅顯示錯誤訊息（預設值）
- **warn**：顯示錯誤與警告
- **notice**：顯示錯誤、警告與通知
- **http**：顯示 HTTP 請求
- **timing**：顯示時間統計資訊
- **info**：顯示一般資訊訊息
- **verbose**：顯示詳細資訊
- **silly**：顯示所有除錯資訊

您可透過 `--loglevel` 參數或 `npm_config_loglevel` 環境變數設定日誌級別：

```bash
npm install --loglevel verbose
```

或透過 npm 配置進行設定：

```bash
npm config set loglevel verbose
```

大多數指令的預設日誌級別為「error」，這意味著除非特別要求更詳細的輸出，否則您只會看到錯誤訊息。