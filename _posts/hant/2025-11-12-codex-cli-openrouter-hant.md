---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 配置 Codex CLI 以使用 OpenRouter
translated: true
type: note
---

### 設定 Codex CLI 配置以使用 OpenRouter

Codex CLI（來自 OpenAI）是一個基於終端機的編碼代理，支援透過配置文件自定義模型供應商，例如 OpenRouter。OpenRouter 提供與 OpenAI 相容的 API，因此您可以透過定義具有適當基礎 URL 的供應商來將請求路由到 OpenRouter。這讓您在使用 Codex 的同時，能夠存取更廣泛的模型（例如來自 Anthropic、Google 或開源供應商的模型）。

配置儲存在 `~/.codex/config.toml` 的 TOML 檔案中（如果不存在，請建立它）。您需要為 OpenRouter 定義一個**模型供應商**部分，然後在特定模型的**設定檔**中引用它。

#### 步驟 1：取得您的 OpenRouter API 金鑰
- 如果尚未註冊，請前往 [openrouter.ai](https://openrouter.ai) 註冊。
- 從您的帳戶儀表板生成一個 API 金鑰。
- 將其設定為環境變數：  
  ```
  export OPENROUTER_API_KEY=您的_api_金鑰_在此
  ```
  將此命令加入您的 shell 設定檔（例如 `~/.bashrc` 或 `~/.zshrc`）以永久儲存。

#### 步驟 2：編輯配置檔案
在編輯器中開啟 `~/.codex/config.toml` 並加入以下部分。這會將基礎 URL 設定為 OpenRouter 的端點 (`https://openrouter.ai/api/v1`)，該端點與 OpenAI 相容（Codex 會自動附加 `/chat/completions`）。

```toml
# 定義 OpenRouter 供應商
[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"  # 從您的環境變數讀取以進行驗證

# 定義使用此供應商的設定檔（範例：使用類似 GPT 的模型）
[profiles.openrouter-gpt]
model_provider = "openrouter"
model = "openai/gpt-4o-mini"  # 替換為任何 OpenRouter 模型 ID，例如 "anthropic/claude-3.5-sonnet"
```

- **關鍵欄位說明**：
  - `base_url`：指向 OpenRouter 的 API 端點。這會覆蓋預設的 OpenAI 基礎 URL。
  - `env_key`：指定用於 Bearer token 驗證標頭的環境變數。
  - `model`：使用 [OpenRouter 模型列表](https://openrouter.ai/models) 中的確切模型 ID。對於編碼任務，可以嘗試 "openai/codex-mini-latest" 或 "meta-llama/llama-3.1-405b-instruct"。
  - 您可以為不同的模型新增多個設定檔（例如，使用 `model = "anthropic/claude-3.5-sonnet"` 的 `[profiles.openrouter-claude]`）。

#### 步驟 3：使用配置
- 如果需要，請安裝 Codex CLI：`npm install -g @openai/codex`（或透過 Homebrew：`brew install codex`）。
- 使用您的設定檔執行 Codex：  
  ```
  codex --profile openrouter-gpt
  ```
  或在配置中設定預設設定檔：  
  ```toml
  [default_profile]
  name = "openrouter-gpt"
  ```
- 測試：執行 `codex` 並給它一個簡單的編碼提示。檢查 OpenRouter 的儀表板以查看使用情況。

#### 疑難排解
- **驗證錯誤**：確保 `OPENROUTER_API_KEY` 已設定並匯出。
- **找不到模型**：在 OpenRouter 上驗證模型 ID — 它區分大小寫並且有前綴（例如 "供應商/模型名稱"）。
- **版本檢查**：使用 Codex CLI v0.13+ 以獲得完整的供應商支援。透過 `npm update -g @openai/codex` 更新。
- **進階路由**：對於 OpenRouter 特定功能，例如成本優化路由，可以在設定檔下加入可選參數，如 `provider = { sort = "price" }`（在較新版本中支援）。

此設定使您的請求與 Codex 的 OpenAI 風格 API 相容，同時利用 OpenRouter 的生態系統。更多詳細資訊，請參閱 [npm 上的 Codex CLI 文件](https://www.npmjs.com/package/@openai/codex) 或 OpenRouter 的 [API 指南](https://openrouter.ai/docs)。如果您使用的是像 Open Codex 這樣的分支，配置類似，但可能具有額外的 Gemini 支援。