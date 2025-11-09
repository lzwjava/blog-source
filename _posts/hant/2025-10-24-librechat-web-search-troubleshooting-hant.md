---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: LibreChat 網頁搜尋故障排除
translated: true
type: note
---

讓我們仔細排查這個問題——當 **在 LibreChat 中網路搜尋無法運作**，即使已添加 **Firecrawl**、**SerpApi** 和 **Jina API** 金鑰後，問題幾乎總是以下之一：配置錯誤、缺少後端啟用標誌，或是使用者介面誤解。

以下是清晰的分步說明（無表格，僅解釋）：

---

### 1. **檢查後端配置中是否啟用了「網路搜尋」**

開啟你的 LibreChat 伺服器配置檔案（通常是 `.env` 或 `api/config.yaml`，取決於你的設定），並確認你有類似以下的設定：

```
# 適用於 .env
SEARCH_ENABLED=true
```

或者，如果使用 YAML：

```yaml
features:
  search: true
```

如果 `SEARCH_ENABLED` 或 `search` 未明確設定為 `true`，使用者介面按鈕可能會顯示但實際上不會執行搜尋。

---

### 2. **確認 API 金鑰命名正確**

每個供應商都需要特定的環境變數名稱。例如：

* 對於 **SerpApi**：

  ```
  SERPAPI_API_KEY=your_key_here
  ```
* 對於 **Firecrawl**：

  ```
  FIRECRAWL_API_KEY=your_key_here
  ```
* 對於 **Jina**：

  ```
  JINA_API_KEY=your_key_here
  ```

同時請確保這些金鑰已在執行 `backend` 程序的相同環境中匯出或載入。

檢查方法：

```bash
echo $SERPAPI_API_KEY
```

如果返回空白，表示你的後端無法讀取它。

---

### 3. **編輯金鑰後重新啟動 LibreChat**

LibreChat 不會熱重載環境變數。請執行：

```bash
docker compose down
docker compose up -d
```

（或者，如果你未使用 Docker，請再次執行 `npm run start`）。

---

### 4. **驗證 LibreChat 實際使用的搜尋供應商**

LibreChat 會根據配置順序選擇一個預設的網路搜尋後端。

例如，如果你希望它使用 SerpApi，你必須指定：

```
SEARCH_PROVIDER=serpapi
```

或者，如果你想使用 Jina：

```
SEARCH_PROVIDER=jina
```

如果你只設定了金鑰但未定義要使用的供應商，LibreChat 可能會預設為無供應商。

---

### 5. **查看後端日誌**

執行：

```bash
docker logs librechat-backend
```

或

```bash
npm run start:debug
```

尋找類似以下的訊息：

```
[Search] SerpApi key missing or invalid
```

或

```
Search provider not configured
```

這些是最佳線索。

---

### 6. **直接測試 API**

以確保你的金鑰確實有效：

**SerpApi 測試：**

```bash
curl "https://serpapi.com/search.json?q=chatgpt&api_key=YOUR_KEY"
```

**Firecrawl 測試：**

```bash
curl "https://api.firecrawl.dev/v1/search?q=chatgpt" -H "Authorization: Bearer YOUR_KEY"
```

**Jina 測試：**

```bash
curl "https://r.jina.ai/chatgpt" -H "Authorization: Bearer YOUR_KEY"
```

如果這些測試失敗，表示金鑰本身無效或已達速率限制。

---

### 7. **前端版本不匹配**

如果你最近更新了 LibreChat（特別是從 v0.7 之前版本到 v0.8+ 版本），前端 `網路搜尋` 切換開關可能存在，但你的後端版本尚未支援整合的 Firecrawl/Jina 搜尋模組。
請執行：

```bash
git pull
```

並重新建置：

```bash
docker compose build --no-cache
docker compose up -d
```

---

### 8. **最終檢查——從網頁使用者介面確認**

開啟使用者介面，前往 **設定 → 功能**，並確認：

* 「網路搜尋」切換開關為開啟狀態
* 你選擇的供應商已列出（SerpApi、Firecrawl 或 Jina）

如果顯示 *「無可用供應商」*，表示後端未讀取到你的金鑰。

---

如果你願意，可以貼上你的相關 `.env` 內容（金鑰部分請遮罩），我將準確指出哪一行缺失或命名錯誤。

你想讓我看看那個片段嗎？