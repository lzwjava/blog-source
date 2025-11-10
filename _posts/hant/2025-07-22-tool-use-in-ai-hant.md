---
audio: false
generated: true
lang: hant
layout: post
title: 應用程式介面中的人工智能工具使用詳解
translated: true
type: note
---

### 什麼是 AI API 中的工具使用？

工具使用，常被稱為「工具呼叫」或「函數呼叫」，是 AI API 中的一項功能，允許大型語言模型與外部工具、函數或 API 進行互動。模型不再僅依賴其內部知識生成回應，而是可以決定呼叫預先定義的函數來獲取即時數據、執行計算或觸發操作。這使得 AI 在查詢天氣、搜索資料庫或與其他服務整合等任務上更加動態和實用。

其流程通常如下：
- 你以 JSON 格式定義工具（函數），包括描述和參數。
- 模型分析用戶的查詢，並在需要時輸出一個「工具呼叫」，包含函數名稱和參數。
- 你的應用程式執行該函數並將結果回傳給模型。
- 模型然後生成最終回應，並將工具的輸出結果整合其中。

這通常受到 OpenAI 的函數呼叫 API 的啟發，許多供應商如 Mistral 和 DeepSeek 都支援相容的實現方式。

### Mistral 還是 DeepSeek 用於工具使用？

Mistral AI 和 DeepSeek AI 都在其 API 中支援工具呼叫，使它們適合用於構建需要外部整合的代理或應用程式。以下是基於現有資訊的快速比較：

- **對工具使用的支援**：
  - 兩者都遵循與 OpenAI API 相似的結構，允許通過 JSON 模式輕鬆整合工具。
  - Mistral 在其多個模型（如 Mistral Large 和 Medium）中支援此功能，並提供基於代理的工作流程選項。
  - DeepSeek 主要通過其 "deepseek-chat" 模型支援，並與 OpenAI 的 SDK 完全相容。

- **優點和缺點**：
  - **Mistral**：在通用任務上更為多才多藝，在某些基準測試中推理速度更快，並且更適合歐洲的數據隱私需求。它在快速回應方面表現出色，並具有強大的多語言能力。然而，它可能更昂貴（例如，輸入/輸出成本比 DeepSeek 高）。
  - **DeepSeek**：成本顯著更低（在某些比較中成本可低至 28 倍），在數學、編程和推理任務上表現強勁。它非常適合預算有限的用戶或高用量場景。缺點包括在非技術任務中可能性能較慢，並且對多模態功能的強調較少。
  - **如何選擇？** 如果成本是優先考量，並且你的使用案例涉及編程/數學與工具結合，請選擇 DeepSeek。對於更廣泛的應用、更快的回應速度或企業級功能（如代理），Mistral 是更好的選擇。兩者都對開源友好且性能良好，但請根據你的具體需求進行測試。

最終，對於工具使用而言，沒有一個是絕對「更好」的——它們都運作良好。DeepSeek 在成本節省方面可能略勝一籌，而 Mistral 則提供更成熟的代理整合。

### 如何使用工具使用

要使用工具呼叫，你需要從相應的供應商處獲取 API 金鑰（在 mistral.ai 註冊 Mistral 或在 platform.deepseek.com 註冊 DeepSeek）。兩者都使用與 OpenAI 相似的 Python SDK。以下是一個簡單的天氣查詢工具的分步示例。

#### 使用 Mistral AI 進行工具使用
Mistral 的 API 通過其 `MistralClient` 在聊天完成中支援工具呼叫。使用 `pip install mistralai` 安裝 SDK。

**Python 代碼示例**（改編自官方和社群來源）：
```python
from mistralai import Mistral

# 使用你的 API 金鑰初始化客戶端
api_key = "YOUR_MISTRAL_API_KEY"
model = "mistral-large-latest"  # 支援工具呼叫
client = Mistral(api_key=api_key)

# 定義工具（函數）
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather for a location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The city, e.g., San Francisco"}
                },
                "required": ["location"]
            }
        }
    }
]

# 用戶訊息
messages = [{"role": "user", "content": "What's the weather in Hangzhou?"}]

# 第一次 API 呼叫：模型決定是否需要工具
response = client.chat.complete(
    model=model,
    messages=messages,
    tools=tools,
    tool_choice="auto"  # 自動決定工具使用
)

# 檢查工具呼叫
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    # 將模型的回應附加到訊息中
    messages.append(response.choices[0].message)
    
    # 模擬執行工具（在真實代碼中，呼叫實際的 API）
    tool_call = tool_calls[0]
    if tool_call.function.name == "get_weather":
        location = eval(tool_call.function.arguments)["location"]
        weather_result = "24°C and sunny"  # 替換為真實的函數呼叫
        
        # 附加工具結果
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": tool_call.function.name,
            "content": weather_result
        })
    
    # 第二次 API 呼叫：模型生成最終回應
    final_response = client.chat.complete(model=model, messages=messages)
    print(final_response.choices[0].message.content)
else:
    print(response.choices[0].message.content)
```

此代碼發送查詢，檢查工具呼叫，執行它（此處為模擬），並獲取最終答案。對於基於代理的設置，請使用 Mistral 的測試版代理 API 來處理更複雜的工作流程。

#### 使用 DeepSeek AI 進行工具使用
DeepSeek 的 API 與 OpenAI 相容，因此你可以使用 OpenAI Python SDK。使用 `pip install openai` 安裝。

**Python 代碼示例**（來自官方文檔）：
```python
from openai import OpenAI

# 使用 DeepSeek 基礎 URL 和 API 金鑰初始化客戶端
client = OpenAI(
    api_key="YOUR_DEEPSEEK_API_KEY",
    base_url="https://api.deepseek.com"
)

# 定義工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a location, the user should supply a location first",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"]
            },
        }
    },
]

# 發送訊息的函數
def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",  # 支援工具呼叫
        messages=messages,
        tools=tools
    )
    return response.choices[0].message

# 用戶訊息
messages = [{"role": "user", "content": "How's the weather in Hangzhou?"}]
message = send_messages(messages)
print(f"User>\t {messages[0]['content']}")

# 處理工具呼叫
tool = message.tool_calls[0]
messages.append(message)

# 模擬工具執行（替換為真實函數）
messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})

# 獲取最終回應
message = send_messages(messages)
print(f"Model>\t {message.content}")
```

這遵循相同的流程：查詢 → 工具呼叫 → 執行 → 最終回應。DeepSeek 限制了上下文長度，因此請保持訊息簡潔。

對於進階使用，請檢查速率限制、成本和模型特定文檔。在沙盒環境中進行測試以處理無效參數等錯誤。

### 參考資料
- [Mistral AI 函數呼叫文檔](https://docs.mistral.ai/agents/function_calling/)
- [DeepSeek API 函數呼叫指南](https://api-docs.deepseek.com/guides/function_calling)
- [Mistral AI 函數呼叫示例與代碼](https://medium.com/@jcrsch/mistral-ai-function-calling-a-simple-example-with-code-72f3a762550f)
- [DeepSeek vs. Mistral：全面的 AI 模型比較](https://medium.com/ai-tools-tips-and-news/deepseek-vs-mistral-a-comprehensive-ai-models-comparison-f7d7b86f4b28)
- [Mistral Large vs DeepSeek-V3 比較](https://docsbot.ai/models/compare/mistral-large-2/deepseek-v3)