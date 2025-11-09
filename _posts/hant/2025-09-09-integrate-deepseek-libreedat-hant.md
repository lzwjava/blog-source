---
audio: false
date: 2025-09-09
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 整合 DeepSeek 與 LibreChat 指南
translated: true
type: note
---

以下是讓 **DeepSeek 在 LibreChat 中運作**的最快方法。我將展示兩種選項——使用 **官方 DeepSeek API**（推薦），或透過 **OpenRouter**。

---

## 選項 A — 使用 DeepSeek 官方 API（推薦）

1. **取得 DeepSeek API 金鑰**
   在你的 DeepSeek 帳戶中建立一個，然後記下基礎 URL：
   `https://api.deepseek.com`（或 OpenAI 相容的 `https://api.deepseek.com/v1`）。 ([DeepSeek API 文件][1], [deepseek.apidog.io][2])

2. **在 `librechat.yaml` 中加入 DeepSeek 端點**
   將此內容置於 `endpoints:` → `custom:` 下：

```yaml
- name: deepseek
  apiKey: ${DEEPSEEK_API_KEY}
  baseURL: https://api.deepseek.com/v1
  models:
    default: deepseek-chat
    fetch: true
    list:
      - deepseek-chat        # V3（通用）
      - deepseek-coder       # 程式碼導向
      - deepseek-reasoner    # R1 推理
  titleConvo: true
  dropParams: null
```

LibreChat 附帶 **DeepSeek** 配置指南，並確認模型名稱（`deepseek-chat`、`deepseek-coder`、`deepseek-reasoner`）以及關於 R1 串流其「思考過程」的說明。 ([LibreChat][3])

3. **透過 `.env` 設定 API 金鑰**
   在你的 LibreChat `.env` 檔案中：

```
DEEPSEEK_API_KEY=sk-...
```

LibreChat 透過 `librechat.yaml` + `.env` 支援自訂的 OpenAI 相容供應商。 ([LibreChat][4])

4. **重啟你的堆疊**
   從你的 LibreChat 資料夾執行：

```bash
docker compose down
docker compose up -d --build
```

（需要此步驟以便 API 容器重新載入 `librechat.yaml` 和 `.env`。）如果你的自訂端點沒有出現，請檢查 `api` 容器日誌以尋找配置錯誤。 ([GitHub][5])

---

## 選項 B — 透過 OpenRouter 使用 DeepSeek

如果你已經使用 OpenRouter，只需在 OpenRouter 端點區塊中註冊 DeepSeek 模型。

`librechat.yaml`：

```yaml
- name: openrouter
  apiKey: ${OPENROUTER_KEY}
  baseURL: https://openrouter.ai/api/v1
  models:
    default: deepseek/deepseek-chat
    list:
      - deepseek/deepseek-chat
      - deepseek/deepseek-coder
      - deepseek/deepseek-reasoner
```

LibreChat 文件中有兩個重要注意事項：
• 不要設定 `OPENROUTER_API_KEY` 環境變數名稱（使用不同的名稱如 `OPENROUTER_KEY`），否則你將意外覆蓋 OpenAI 端點。
• OpenRouter 在 LibreChat 的自訂端點清單中是一等公民。 ([LibreChat][6])

OpenRouter 透過 OpenAI 相容介面公開 DeepSeek 模型。 ([OpenRouter][7])

---

## 提示與注意事項

* **R1 / `deepseek-reasoner`**：它可以串流其思維鏈（「思考過程」）。某些 OpenAI 參數可能不適用。如果你看到奇怪的輸出，請先使用 `deepseek-chat` 測試。 ([LibreChat][3])
* **模型獲取**：設定 `fetch: true` 讓 LibreChat 在支援時拉取最新的模型清單；否則將使用你指定的 `list:`。 ([LibreChat][8])
* **這些設定的位置**：`librechat.yaml` 是自訂端點檔案；`.env` 攜帶金鑰和代理設定。 ([LibreChat][8])

如果你需要，可以貼上你當前的 `librechat.yaml`，我會幫你乾淨地加入 DeepSeek（保證沒有表格）。

[1]: https://api-docs.deepseek.com/?utm_source=chatgpt.com "DeepSeek API Docs: Your First API Call"
[2]: https://deepseek.apidog.io/your-first-api-call-835227m0?utm_source=chatgpt.com "DeepSeek API: Your First API Call"
[3]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/deepseek?utm_source=chatgpt.com "Deepseek"
[4]: https://www.librechat.ai/docs/quick_start/custom_endpoints?utm_source=chatgpt.com "Custom Endpoints"
[5]: https://github.com/danny-avila/LibreChat/discussions/2487?utm_source=chatgpt.com "Fix the librechat.yaml file in the main repository. #2487"
[6]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/openrouter?utm_source=chatgpt.com "Openrouter"
[7]: https://openrouter.ai/deepseek/deepseek-v3-base%3Afree/api?utm_source=chatgpt.com "DeepSeek V3 Base – Run with an API"
[8]: https://www.librechat.ai/docs/configuration/librechat_yaml?utm_source=chatgpt.com "librechat.yaml config file"