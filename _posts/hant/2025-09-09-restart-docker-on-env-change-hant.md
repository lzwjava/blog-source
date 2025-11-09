---
audio: false
date: 2025-09-09
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 環境變更後重啟 Docker 容器
translated: true
type: note
---

當你更改 `.env` 檔案時，Docker 不會自動重新載入那些環境變數。你需要重啟容器，讓它們讀取新的數值。對於你的 LibreChat 設定，可以這樣操作：

1. 確保你位於 `docker-compose.yml` 檔案所在的相同目錄。
2. 執行：

```bash
docker compose down
docker compose up -d
```

這將會停止並移除正在運行的容器，然後使用新的 `.env` 數值重新建立它們。

---

### 替代方案：僅重新啟動

如果你不想完全拆除所有內容，可以透過重建來強制容器讀取新的環境變數：

```bash
docker compose up -d --force-recreate
```

或者如果你也更改了 Dockerfile 或依賴項，請加上 `--build`：

```bash
docker compose up -d --build
```

---

✅ 簡而言之：

* 編輯 `.env` 後，請務必**重新建立**容器（使用 `down` + `up` 或 `up --force-recreate`）。
* 單純使用 `docker compose restart` 不會重新載入新的環境變數值，它只會使用舊的數值重新啟動。

你是否還需要我示範如何**驗證**你的 LibreChat 容器正在使用新的環境變數值（例如使用 `docker inspect` 或 `docker exec env`）？