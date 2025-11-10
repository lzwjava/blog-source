---
audio: false
generated: true
image: false
lang: hant
layout: post
title: DeepSeek V3.1 混合模式詳解
translated: true
type: note
---

以下是 **DeepSeek V3.1 API** 處理其新型混合推理架構（「思考」與「非思考」模式）的方式：

---

### API 變更概述

#### 1. **兩個不同的端點（模式）**

* **`deepseek-chat`** 對應 **非思考模式** — 專為快速回應而優化。
* **`deepseek-reasoner`** 對應 **思考模式** — 專為需要更深思熟慮、多步驟推理的任務而構建。
  這兩個端點現在都基於相同的 V3.1 模型運行，並具有 128K token 的上下文窗口。（[DeepSeek API 文檔][1], [Data Science Dojo][2]）

#### 2. **擴展的上下文支援**

* 兩種模式均支援擴展的 128K token 上下文，這是一項重大升級，允許處理非常長的輸入。（[DeepSeek API 文檔][1], [Hugging Face][3]）

#### 3. **改進的格式與能力**

* 現已支援 **Anthropic API 相容性**，使得將 DeepSeek 與 Anthropic 風格的客戶端庫整合更加容易。（[DeepSeek API 文檔][1]）
* 支援 **嚴格函數呼叫**（測試版），允許通過 API 進行更強大且經過驗證的工具調用。（[DeepSeek API 文檔][1]）

#### 4. **UI 切換與 API 調用**

* 在其網頁 UI 上（「DeepThink」按鈕），用戶可以互動式地切換模式。
* 在 **API** 中，您必須通過將 `model` 參數設置為 `"deepseek-chat"`（非思考模式）或 `"deepseek-reasoner"`（思考模式）來明確選擇模式。（[DeepSeek API 文檔][1]）

#### 5. **其他增強功能**

* 引入了 **更多 API 資源** 和整體更流暢的開發者體驗。（[DeepSeek API 文檔][1]）
* 底層的分詞器和聊天模板已更新，以支援基於模式的行為（例如，適當地插入 `` token）。（[Hugging Face][3]）

---

### 摘要：變更內容 — 無需表格

* **新命名**：

  * `deepseek-chat` → 非思考模式
  * `deepseek-reasoner` → 思考模式

* **共享架構**：兩者都基於相同的 671B 參數模型構建，並具有長達 128K token 的上下文窗口。

* **增強的整合選項**：

  * 支援 Anthropic 風格的 API。
  * 提供嚴格的函數呼叫（測試版），實現更安全、基於模式的工具互動。

* **模板更新**：API 現在在提示中使用特殊 token（``）來區分模式，並革新了聊天模板邏輯。

* **開發者體驗**：平台包含更多資源、更新的文檔以及整體更流暢的整合流程。

---

### 使用範例 (Python/HTTP)

**非思考模式（快速回應）：**

```python
import openai  # 或 DeepSeek 相容的 SDK
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role":"user","content":"講個笑話給我聽。"}],
)
```

**思考模式（深度推理）：**

```python
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role":"user","content":"解釋為什麼天空是藍色的。"}],
)
```

**函數呼叫（嚴格模式，測試版）：**
您可以定義帶有 JSON 模式的函數（工具），讓模型調用它們，接收結構化呼叫，然後執行並回傳結果 — 非常適合構建自主代理。（[DeepSeek API 文檔][1], [Reddit][4], [apidog][5]）

---

如果您需要協助設計工具使用的提示、優化成本或速度，或者想更詳細地探索 Anthropic 相容介面，請告訴我！

[1]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"
[2]: https://datasciencedojo.com/blog/deep-seek-v3-1/?utm_source=chatgpt.com "Deep Seek v3.1: The Next Leap in Open-Source Large ..."
[3]: https://huggingface.co/deepseek-ai/DeepSeek-V3.1?utm_source=chatgpt.com "deepseek-ai/DeepSeek-V3.1"
[4]: https://www.reddit.com/r/LocalLLaMA/comments/1munvj6/the_new_design_in_deepseek_v31/?utm_source=chatgpt.com "The new design in DeepSeek V3.1 : r/LocalLLaMA"
[5]: https://apidog.com/blog/deepseek-v3-1-api/?utm_source=chatgpt.com "How to Use DeepSeek-V3.1 API ?"