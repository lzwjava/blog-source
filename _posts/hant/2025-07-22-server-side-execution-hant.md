---
audio: false
generated: true
lang: hant
layout: post
title: 優化伺服器端執行的AI工具調用
translated: true
type: note
---

是的，傳統聊天機器人中使用工具或函數呼叫的來回互動模式（即 AI 模型生成呼叫、發送至客戶端或其他服務、等待執行、然後接收結果）確實可能導致延遲，尤其是在即時應用中。這通常是由於網路開銷、序列化/反序列化以及需要多次 API 往返造成的。您提出的使用 lambda 函數或設計能接受 Python 程式碼以在伺服器端執行的 API 建議，是減輕此問題的聰明方法——基本上是將計算轉移到伺服器，以最小化客戶端與伺服器之間的互動。我將從概念上分解這一點，討論可行性、潛在實現方式及權衡取捨。

### 為何傳統工具呼叫可能緩慢
在許多 AI 框架中（例如 LangChain、OpenAI 的函數呼叫或 Anthropic 的工具）：
- 模型輸出結構化的工具呼叫（例如包含函數名稱和參數的 JSON）。
- 客戶端（或代理）在本地或透過另一個 API 執行該函數。
- 結果被附加到對話歷史中，並發送回模型進行下一步推理。
這種循環每周期可能增加數秒的延遲，在複雜任務（如數據分析或多步驟推理）中會累積延遲。

### 使用 Lambda 函數或伺服器端程式碼執行
您的想法與「無伺服器」或「沙箱化」執行模型相符，即 AI 生成直接在託管模型的伺服器上運行的程式碼（或類似 lambda 的片段）。這將所有內容保持在同一個環境中，將往返次數減少到可能僅有用戶的一次 API 呼叫。

- **Lambda 函數方法**：像 AWS Lambda、Google Cloud Functions 或 Azure Functions 這樣的服務允許按需執行小型、短暫的 Python 程式碼片段，而無需管理伺服器。在 AI 情境中：
  - 聊天機器人的後端可以封裝 AI 模型（例如透過 OpenAI API）並將 Lambda 整合為工具。
  - 模型生成一個 lambda 表達式或短函數，在伺服器端調用。
  - 優點：可擴展、按使用付費，且啟動快速（冷啟動通常 <100ms）。
  - 缺點：執行時間有限（例如 AWS 上最長 15 分鐘），並且如果任務跨多個調用，則需要處理狀態管理。
  - 範例：AI 代理可以生成一個 lambda 來處理數據（例如 `lambda x: sum(x) if isinstance(x, list) else 0`），將其發送到 Lambda 端點，並內聯獲取結果。

- **設計接受並執行 Python 程式碼的 API**：
  - 是的，這絕對是可行的，並且已經在生產系統中存在。關鍵在於**沙箱化**，以防止安全風險，如任意程式碼執行（例如刪除檔案或進行網路呼叫）。
  - 工作原理：API 端點接收程式碼片段（作為字串），在隔離環境中運行它，捕獲輸出/錯誤，並返回結果。AI 模型可以迭代生成並「呼叫」此程式碼，而無需離開伺服器。
  - 好處：
    - 減少延遲：執行發生在與模型相同的數據中心，通常只需毫秒級時間。
    - 實現複雜任務：如數據處理、數學模擬或檔案處理，無需外部工具。
    - 有狀態會話：某些實現跨呼叫維護類似 REPL 的環境。
  - 安全措施：
    - 使用容器（Docker）、微型虛擬機（Firecracker）或受限的 Python 解釋器（例如 PyPy 沙箱化或受限全域變數）。
    - 限制資源：CPU/時間配額、無網路存取、白名單模組（例如 numpy、pandas，但不能使用 os 或 subprocess）。
    - 像 `restrictedpython` 這樣的函式庫或像 E2B/Firecracker 這樣的工具提供了現成的沙箱。

### 實際範例與實現
多個 AI 平台已經在不同程度上支持此功能：
- **OpenAI 的 Assistants API 與 Code Interpreter**：允許模型在 OpenAI 伺服器上的沙箱化環境中編寫和運行 Python 程式碼。模型可以上傳檔案、執行程式碼並迭代結果——全部在伺服器端完成。無需客戶端執行。
- **Google 的 Gemini API 程式碼執行**：提供內建的 Python 沙箱，模型可以在其中迭代生成和運行程式碼，從輸出中學習，無需外部呼叫。
- **自訂解決方案**：
  - **E2B Sandbox**：用於創建基於雲端的沙箱與 Jupyter 核心的 SDK/API。AI 代理可以安全地發送程式碼運行，非常適合數據分析工具。
  - **Modal Sandboxes**：一個用於在隔離環境中運行 AI 生成程式碼的平台，常用於 LLM 代理。
  - **SandboxAI（開源）**：專門用於在沙箱中執行 AI 生成的 Python 程式碼的運行時環境。
  - 對於 DIY：構建一個 FastAPI 或 Flask 伺服器，透過 POST 接受程式碼，在受限命名空間中使用 `exec()`，或為每個請求啟動一個 Docker 容器。

在程式碼方面，一個簡單的 API 端點可能如下所示（用於說明的偽代碼）：

```python
from fastapi import FastAPI
import restrictedpython  # 用於安全執行

app = FastAPI()

@app.post("/execute")
def execute_code(code: str):
    safe_globals = {"__builtins__": restrictedpython.safe_builtins}  # 受限環境
    try:
        result = {}
        exec(code, safe_globals, result)  # 執行程式碼
        return {"output": result.get("output")}
    except Exception as e:
        return {"error": str(e)}
```

將此與您的聊天機器人整合：AI 根據用戶輸入生成程式碼，內部呼叫端點，並整合結果。

### 潛在缺點與最佳實踐
- **安全風險**：任意程式碼執行是危險的——務必使用沙箱。如果處理不受信任的用戶，請避免使用。
- **成本與可擴展性**：伺服器端執行使用更多計算資源；使用像 New Relic 這樣的工具進行監控以優化。
- **除錯**：如果處理不當，生成程式碼中的錯誤可能會循環。
- **優化的替代方案**：
  - 批次工具呼叫：將多個功能分組到一次伺服器往返中。
  - 串流：使用在並行執行工具時串流回應的 API。
  - 如果延遲容忍度高，可在客戶端執行：用於非敏感任務。
- 如果從頭開始構建，可以從像 LangChain 或 Vercel 的 AI SDK 這樣的框架開始，它們支持自訂工具，並且可以配置為伺服器端運行。

這種方法可以使聊天機器人更快、功能更強大，特別是在計算任務方面。如果您正在實施此方法，可以考慮從 OpenAI 或 Gemini 的內建功能開始，以快速取得成效。

[為 AI 生成的程式碼執行構建沙箱環境](https://anukriti-ranjan.medium.com/building-a-sandboxed-environment-for-ai-generated-code-execution-e1351301268a)  
[substratusai/sandboxai: 在隔離沙箱中運行 AI 生成的程式碼](https://github.com/substratusai/sandboxai)  
[使用 TS 和 GPT-4o 透過沙箱化程式碼執行構建 AI 數據分析師 - E2B](https://e2b.dev/blog/build-ai-data-analyst-with-sandboxed-code-execution-using-typescript-and-gpt-4o)  
[程式碼執行 | Gemini API](https://ai.google.dev/gemini-api/docs/code-execution)  
[Assistants Code Interpreter - OpenAI API](https://platform.openai.com/docs/assistants/tools/code-interpreter)  
[Modal Sandboxes](https://modal.com/use-cases/sandboxes)  
[使用 New Relic AI 監控優化 AI 聊天機器人性能](https://newrelic.com/blog/how-to-relic/optimizing-ai-chatbot-performance)