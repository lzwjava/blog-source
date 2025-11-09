---
audio: false
date: 2025-09-09
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 設定 LibreChat 中的 OPENAI_REVERSE_PROXY
translated: true
type: note
---

明白了 👍 你正在編輯 LibreChat 的 `.env` 檔案。
這個檔案正是你設定 `OPENAI_REVERSE_PROXY` 的地方。

---

### 1. 變數功能說明

`OPENAI_REVERSE_PROXY` 用於讓 LibreChat 將 OpenAI API 請求透過代理伺服器路由（例如，如果你運行自託管反向代理來添加日誌記錄、快取、區域路由或繞過限制）。

---

### 2. 設定方法

在你的 `.env` 檔案中，只需將其設定為你的反向代理基礎 URL。例如：

```ini
OPENAI_REVERSE_PROXY=https://your-proxy.example.com/v1
```

注意事項：

* URL 應指向模擬 OpenAI `/v1` API 的代理端點。
* 除非你的代理要求，否則請勿包含結尾的 `/`。
* 如果不使用代理，請保持空白（`OPENAI_REVERSE_PROXY=`）。

---

### 3. 應用變更

編輯 `.env` 後，請重啟你的 LibreChat 容器以載入新值：

```bash
docker compose down
docker compose up -d --force-recreate
```

---

### 4. 驗證設定

你可以在運行的容器內檢查：

```bash
docker compose exec librechat env | grep OPENAI_REVERSE_PROXY
```

它應該顯示你設定的值。

---

你已經有反向代理 URL（例如 `https://openrouter.ai/api/v1` 或你自己的 Nginx 實例），還是需要我示範如何為 LibreChat **設定一個**反向代理？