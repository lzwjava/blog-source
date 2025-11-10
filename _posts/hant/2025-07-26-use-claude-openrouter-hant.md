---
audio: false
generated: true
lang: hant
layout: post
title: 透過 OpenRouter 使用 Claude
translated: true
type: note
---

### 如何透過 OpenRouter 使用 Claude 模型（中國用戶無需 Anthropic API 存取權限）

作為中國用戶，您可能會因區域封鎖而無法直接存取 Anthropic 的 Claude API。不過，OpenRouter 是一個可靠的替代方案，它作為統一 API 閘道器，可連接多個 AI 供應商，包括 Anthropic 的 Claude 模型。OpenRouter 在中國可正常存取（其網站和 API 端點均未被封鎖），讓您無需直接擁有 Anthropic 帳戶或 API 金鑰即可將請求路由至 Claude。雖然這是按使用量付費的服務（您需要新增付款方式），但註冊是免費的，且支援有限用量的免費層級。

OpenRouter 的 API 與 OpenAI 的格式相容，因此您可以使用熟悉的函式庫，例如 OpenAI Python SDK。以下我將概述入門步驟，並提供在 Python 中使用 Claude 的程式碼範例。

#### 步驟 1：註冊 OpenRouter
1. 造訪 OpenRouter 網站：https://openrouter.ai。
2. 點擊「Sign Up」或「Get Started」（通常位於右上角）。
3. 使用您的電子郵件（或 GitHub/Google 登入，如果可用）建立帳戶。無需使用 VPN，因為該網站在中國可正常運作。
4. 註冊後，如果需要，請驗證您的電子郵件。
5. 前往儀表板並新增付款方式（例如信用卡）為您的帳戶充值。OpenRouter 根據 token 使用量收費，但您可以先存入少量金額。請查看其定價頁面以了解 Claude 模型的詳細資訊。

#### 步驟 2：產生 API 金鑰
1. 在您的 OpenRouter 儀表板中，導覽至「API Keys」或「Keys」部分。
2. 建立一個新的 API 金鑰（它看起來會像一串長字元，例如 `sk-or-v1-...`）。
3. 複製並安全地儲存它——請像對待密碼一樣對待它。您將在程式碼中使用它，而不是 Anthropic 金鑰。

#### 步驟 3：選擇 Claude 模型
OpenRouter 列出了 Anthropic 的 Claude 模型，其 ID 類似於：
- `anthropic/claude-3.5-sonnet`（推薦用於大多數任務；平衡且能力強）。
- `anthropic/claude-3-opus`（功能更強大但更昂貴）。
- 較新版本（例如，如果 2025 年有 Claude 3.7）將在 https://openrouter.ai/models?providers=anthropic 上列出。

您可以瀏覽模型頁面以查看成本、上下文限制和可用性。

#### 步驟 4：設定您的環境
- 如果尚未安裝 Python，請安裝它（推薦版本 3.8+）。
- 安裝 OpenAI 函式庫：在終端機中執行 `pip install openai`。

#### 步驟 5：在程式碼中使用 Claude
使用 OpenAI SDK 並指定 OpenRouter 的基礎 URL（`https://openrouter.ai/api/v1`）。在您的請求中指定 Claude 模型 ID。

以下是一個簡單的 Python 範例，用於與 Claude 3.5 Sonnet 聊天：

```python
from openai import OpenAI

# 使用 OpenRouter 的端點和您的 API 金鑰初始化客戶端
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY_HERE",  # 替換為您的實際金鑰
)

# 向 Claude 發送請求
completion = client.chat.completions.create(
    model="anthropic/claude-3.5-sonnet",  # 使用 Claude 模型 ID
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, what is the capital of China?"}
    ],
    temperature=0.7,  # 可選：調整創造性（0-1）
    max_tokens=150    # 可選：限制回應長度
)

# 列印回應
print(completion.choices[0].message.content)
```

- **說明**：這會向 Claude 發送系統提示和使用者訊息，取得回應並列印出來。請替換 API 金鑰並根據需要調整參數。
- **如果您偏好原始 HTTP 請求**（不使用 OpenAI 函式庫）：

```python
import requests
import json

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer YOUR_OPENROUTER_API_KEY_HERE",
        "Content-Type": "application/json"
    },
    data=json.dumps({
        "model": "anthropic/claude-3.5-sonnet",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, what is the capital of China?"}
        ]
    })
)

# 解析並列印回應
data = response.json()
print(data['choices'][0]['message']['content'])
```

- **提示**：
  - 新增可選的標頭，如 `"HTTP-Referer": "your-site-url"` 和 `"X-Title": "Your App Name"`，以歸屬使用情況（有助於排行榜和潛在的免費額度）。
  - 在您的 OpenRouter 儀表板中監控使用情況，以避免意外成本。
  - 對於串流回應或進階功能（例如工具），請參閱 OpenRouter 的完整文件。
  - 如果遇到速率限制或錯誤，請檢查您的餘額或嘗試不同的模型。

#### 疑難排解
- **API 錯誤**：確保您的金鑰正確且已充值。首先使用便宜的模型進行測試。
- **區域問題**：如果發生任何封鎖（不太可能），請使用 VPN，但 OpenRouter 的設計旨在為支援的模型繞過此類限制。
- **免費替代方案**：對於有限的免費存取，可以探索像 Puter.js 這樣的代理（但它們可能有限制）。

此設定讓您無需直接存取 Anthropic 即可以程式設計方式使用 Claude。如果您需要與特定工具（例如 Cursor IDE 或 Make.com）整合，請搜尋相關教學。

參考資料：  
[OpenRouter 文件](https://openrouter.ai/docs)  
[Anthropic Claude on OpenRouter](https://openrouter.ai/anthropic/claude-3.5-sonnet)  
[在中國使用 OpenRouter](https://medium.com/ai-simplified-in-plain-english/not-re-inventing-the-wheel-in-ai-2ec3e76ae2bd)  
[如何在中國使用 Claude](https://www.comparitech.com/blog/vpn-privacy/how-to-use-claude-in-china/)