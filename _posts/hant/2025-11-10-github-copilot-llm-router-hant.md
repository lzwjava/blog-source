---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 配置 GitHub Copilot LLM 路由器
translated: true
type: note
---

要在企業環境中設定您的 LLM 路由器，使其專門使用 GitHub Copilot 的 LLM API，請為其添加專用供應商，並調整路由器設定以將所有流量路由至該供應商。

- **新增 GitHub Copilot 供應商**：在 "Providers" 陣列中加入一個新項目，包含適當的 API 基礎 URL、您的 GitHub 個人存取權杖 (PAT) 作為 API 金鑰，以及支援的模型。
- **更新路由器預設值**：將所有路由器欄位（例如 "default"、"think"）更改為僅指向新供應商名稱，確保不呼叫其他供應商。
- **處理企業限制**：使用您企業 GitHub 帳戶的 PAT（需具備必要範圍），如果您的環境因合規性要求需使用代理路由，請利用現有的 "PROXY_URL"。
- **測試與驗證**：更新後，請驗證所有 API 呼叫是否僅導向 Copilot 端點，以符合僅允許 Copilot API 互動的政策。

### 逐步設定說明
1. **產生 GitHub PAT**：登入您的 GitHub 企業帳戶，建立一個個人存取權杖，並授予適當的範圍，例如用於聊天存取的 `copilot` 或用於更廣泛模型推論的 `models:read`。這可確保安全的身份驗證，而不暴露更廣泛的權限。
2. **修改 Providers 陣列**：在您的 config JSON 中的 "Providers" 列表附加一個新物件。將 "name" 設定為描述性名稱（如 "github_copilot"），"api_base_url" 設定為 "https://api.githubcopilot.com/chat/completions"（適用於 Copilot 代理）或 "https://models.github.ai/inference/chat/completions"（適用於一般 GitHub Models 推論），"api_key" 設定為您的 PAT，並列出相容的模型。
3. **調整 Router 部分**：將 "Router" 物件中的所有值替換為您的新供應商名稱（例如 "github_copilot"），以強制專屬使用。這可防止回退到其他供應商（如 OpenRouter）。
4. **企業注意事項**：在受限環境中，請確認您的網路政策允許對 GitHub 網域進行輸出呼叫。如有需要，請更新 "PROXY_URL" 以透過經批准的企業代理進行路由。啟用日誌記錄（"LOG": true）以稽核呼叫並確保合規性。

### 更新後的設定範例
以下為修改後您的設定可能呈現的樣子（請將佔位符替換為您的實際 PAT 和首選端點）：

```json
{
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "",
      "models": [
        "moonshotai/kimi-k2",
        "anthropic/claude-sonnet-4",
        "anthropic/claude-3.5-sonnet",
        "anthropic/claude-3.7-sonnet:thinking",
        "anthropic/claude-opus-4",
        "google/gemini-2.5-flash",
        "google/gemini-2.5-pro",
        "deepseek/deepseek-chat-v3.1",
        "deepseek/deepseek-r1",
        "mistralai/mistral-medium-3.1",
        "qwen/qwen3-coder",
        "openai/gpt-oss-120b",
        "openai/gpt-5",
        "z-ai/glm-4.6",
        "x-ai/grok-code-fast-1",
        "x-ai/grok-4-fast",
        "minimax/minimax-m2",
        "moonshotai/kimi-k2-thinking"
      ],
      "transformer": {
        "use": [
          "openrouter"
        ]
      }
    },
    {
      "name": "github_copilot",
      "api_base_url": "https://api.githubcopilot.com/chat/completions",
      "api_key": "ghp_YourPersonalAccessTokenHere",
      "models": [
        "gpt-4o",
        "gpt-4o-mini",
        "claude-3-5-sonnet-20240620"
      ],
      "transformer": {
        "use": [
          "github_copilot"
        ]
      }
    }
  ],
  "Router": {
    "default": "github_copilot",
    "background": "github_copilot",
    "think": "github_copilot",
    "longContext": "github_copilot",
    "longContextThreshold": 30000,
    "webSearch": "github_copilot"
  }
}
```

此設定確保路由器僅與 Copilot API 互動，符合限制僅允許呼叫核准端點的企業政策。

---

在企業環境中，整合 LLM API（如 GitHub Copilot）需要仔細設定以符合安全政策，通常會限制輸出呼叫僅能連線至特定的核准服務。所提供的路由器設定似乎是自訂設定，用於跨供應商路由 LLM 請求，類似於 OpenRouter 或 LiteLLM 等工具，其中 "Providers" 定義了 API 端點和模型，而 "Router" 則決定了回退或特定類別的路由。為了使其專門使用 GitHub Copilot 的 LLM API（確保不呼叫其他外部服務），您需要將 Copilot 納入為供應商，並在所有路由器路徑中強制執行。這種方法適用於企業防火牆或合規規則僅允許 GitHub 託管 API 的情況，利用 Copilot 的 OpenAI 相容介面進行聊天完成。

GitHub Copilot 主要透過兩種途徑提供 LLM 存取：用於建置代理和擴充功能的專用 Copilot LLM 端點，以及用於一般推論的更廣泛 GitHub Models API。專用的 Copilot 端點 `https://api.githubcopilot.com/chat/completions` 專為企業級代理開發而設計，支援採用 OpenAI 聊天完成格式的 POST 請求。身份驗證使用源自 GitHub 個人存取權杖 (PAT) 的 Bearer 權杖，通常透過 `Authorization` 標頭傳遞。例如，範例請求可能包含如 `Authorization: Bearer <your-pat>` 和 `Content-Type: application/json` 的標頭，以及包含 `messages`（使用者/系統提示的陣列）和可選參數（如用於即時回應的 `stream: true`）的請求主體。文件中未明確列出模型，但與 Copilot 的底層供應商（例如 GPT-4 變體和 Claude 模型）保持一致，並對第三方代理實施嚴格的速率限制以防止濫用。

或者，位於 `https://models.github.ai/inference/chat/completions` 的 GitHub Models API 提供了更通用的推論服務，允許僅使用 GitHub 憑證存取模型目錄。這非常適合原型設計和整合到 GitHub Actions 等工作流程中。身份驗證需要具有 `models:read` 範圍的 PAT，可透過您的 GitHub 設定 (https://github.com/settings/tokens) 建立。在企業設定中，這可以擴展到組織層級的權杖，或透過在工作流程 YAML 檔案中添加 `permissions: models: read` 在 CI/CD 管道中使用。可用模型包括業界標準，如 `openai/gpt-4o`、`openai/gpt-4o-mini`、`anthropic/claude-3-5-sonnet-20240620`、Meta 的 Llama 3.1 系列和 Mistral 變體，所有這些都可以透過相同的 OpenAI 相容 API 格式呼叫。這種相容性使其易於整合到您的路由器設定中，而無需對下游程式碼進行重大更改。

對於企業特定設定，GitHub Copilot Enterprise 增強了標準 Copilot 的功能，提供了全組織範圍的控制項（例如基於您的程式碼庫進行微調的模型），但 API 存取遵循相同的模式。網路管理至關重要：您可以設定基於訂閱的路由，以確保 Copilot 流量使用核准的路徑，這要求使用者將其 IDE 擴充功能（例如 VS Code）更新至支援此功能的最低版本。如果您的環境強制要求使用代理，請將設定中的 "PROXY_URL" 更新為指向您的企業代理伺服器，並考慮使用自訂憑證進行 SSL 檢查。像 LiteLLM 這樣的工具可以作為進一步控制的中介代理 — 透過 `pip install litellm[proxy]` 安裝，在 YAML 設定中定義模型，在本地端口啟動伺服器，並將 Copilot 請求重新導向通過它以進行日誌記錄、速率限制和回退處理。然而，在您的情況下，由於目標是專屬使用，請避免在路由器中設定回退，以符合「僅允許呼叫 Copilot」的政策。

要在您的設定中實作此功能，首先附加一個新的供應商物件。根據您的使用案例選擇端點：如果是建置擴充功能，請使用 Copilot 代理端點；如果是一般 LLM 路由，請使用 GitHub Models。列出與您現有模型重疊的模型（例如 Claude 和 GPT 變體）以保持相容性。然後，覆寫所有 "Router" 欄位，使其僅參考此新供應商，消除逗號或回退（如 ",minimax/minimax-m2"）。啟用日誌記錄以監控合規性，並透過模擬請求進行測試，以驗證是否未觸及未經授權的端點。如果與 VS Code 或其他 IDE 整合，請調整設定（如 `github.copilot.advanced.debug.overrideProxyUrl`）以在需要時透過您設定的代理進行路由。

以下是兩個主要 GitHub LLM API 選項的比較表，以幫助您決定在供應商設定中使用哪個端點：

| 方面                  | GitHub Copilot LLM API (用於代理)                  | GitHub Models API                                   |
|-------------------------|-----------------------------------------------------|-----------------------------------------------------|
| 端點                | https://api.githubcopilot.com/chat/completions      | https://models.github.ai/inference/chat/completions |
| 主要用途             | 建置 Copilot 擴充功能和代理              | 一般原型設計、推論和工作流程       |
| 身份驗證          | Bearer PAT (透過 Authorization 標頭)               | 具有 models:read 範圍的 PAT                          |
| 支援的模型        | 隱含式 (例如 GPT-4、Claude 變體)             | 明確目錄：gpt-4o、claude-3-5-sonnet、Llama 3.1 等。 |
| 企業功能     | 對第三方的速率限制；與 Copilot Enterprise 整合 | 可在 GitHub Actions 中使用；支援自帶金鑰 |
| 速率限制/配額      | 對非 GitHub 代理嚴格                        | 用於原型設計的免費層級；可為企業擴展  |
| 相容性           | OpenAI 聊天格式                                  | OpenAI 相容；易於路由器整合          |

此表突顯了為什麼 GitHub Models 可能更適合廣泛的路由器使用，因為它提供了更明確的模型選擇和企業工作流程整合。

潛在挑戰包括權杖過期（PAT 通常有效期為 30-90 天），因此請在企業指令碼中自動化續訂。如果您的環境使用 GitHub Enterprise Cloud，請在組織層級啟用 Copilot 以實現無縫存取。對於進階設定，請探索在 GitHub Models 中自帶 API 金鑰 (BYOK)，以便在停留在 GitHub 生態系統內的同時，透過首選供應商進行路由。請始終優先參考主要的 GitHub 文件以獲取最新的範圍和端點，因為功能發展迅速。如果直接 API 呼叫因網路限制而失敗，請考慮使用 GitHub 的代理設定選項或與 Azure 整合以進行混合企業部署。

總而言之，此設定將您的路由器轉變為一個專屬 Copilot 的系統，既符合企業政策，又保持了程式碼相關或一般 LLM 任務的功能性。

**主要參考文獻：**
- [Using GitHub Copilot's LLM for your agent](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/use-copilot-extensions/build-a-copilot-agent/use-copilots-llm)
- [Quickstart for GitHub Models](https://docs.github.com/en/github-models/quickstart)
- [GitHub Copilot | liteLLM](https://docs.litellm.ai/docs/tutorials/github_copilot_integration)
- [Managing GitHub Copilot access to your enterprise's network](https://docs.github.com/enterprise-cloud%40latest/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-access/manage-network-access)
- [Configuring network settings for GitHub Copilot](https://docs.github.com/copilot/configuring-github-copilot/configuring-network-settings-for-github-copilot)
- [Prototyping with AI models](https://docs.github.com/github-models/prototyping-with-ai-models)
- [Using your own API keys in GitHub Models](https://docs.github.com/en/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)