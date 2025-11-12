---
audio: false
generated: true
lang: hant
layout: post
title: 深度思考模型
translated: true
type: note
---

此資訊基於來自 https://search.jina.ai 的查詢。

---

以下是深度推理模型及其 API 可用性的詳細分析，旨在提供更深入的理解，並協助您選擇合適的模型以滿足需求：

*   **OpenAI o-series 模型 (o1, o3-mini 等)**：這些模型可透過 Azure OpenAI Service 使用 [^1]，專為複雜推理而設計，在科學、編程和數學領域表現卓越。例如，`o1` 模型具有 200,000 個 token 的上下文視窗，並可透過 `reasoning_effort` 參數調整處理時間以進行微調 [^2]。

    *   **API 存取：** 可透過 Azure OpenAI Service API 並使用 `2024-12-01-preview` API 版本進行存取 [^1]。
    *   **定價：** Azure OpenAI 的定價因模型和使用情況而異。請查閱 Azure OpenAI Service 定價頁面以獲取詳細資訊。
    *   **速率限制：** 速率限制取決於 Azure OpenAI 的服務層級和區域。請參考 Azure OpenAI 文件以了解具體細節。
    *   **支援功能：** 函數呼叫、JSON 模式、可調整的安全設定 [^3]。
    *   **程式碼範例 (Python)：**
        ```python
        from openai import AzureOpenAI
        client = AzureOpenAI(
          azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
          api_key=os.getenv("AZURE_OPENAI_API_KEY"),
          api_version="2024-12-01-preview"
        )
        response = client.chat.completions.create(
            model="o1-new", # 請替換為您的 o1 部署模型名稱。
            messages=[
                {"role": "user", "content": "撰寫我的第一個 Python API 時應該考慮哪些步驟？"},
            ],
            max_completion_tokens = 5000
        )
        print(response.model_dump_json(indent=2))
        ```
*   **DeepSeek R1**：以在推理基準測試中可與 OpenAI 的 o1 匹敵而聞名，DeepSeek 透過其 API 提供 R1 模型 [^4]。該 API 提供對模型生成的思維鏈內容的存取，允許使用者觀察模型的推理過程 [^5]。DeepSeek 還提供了一個具成本效益的 OpenAI 替代方案，其完整的 R1 API 僅以極低成本提供 [^6]。DeepSeek-V3 API 也已推出，其性能可與領先的閉源模型相媲美 [^7]。

    *   **API 存取：** DeepSeek API，相容於 OpenAI API 格式 [^8]。
    *   **定價：** 輸入 token 每百萬個 0.14 美元，輸出 token 每百萬個 0.55 美元 [^9]。
    *   **速率限制：** 請參考 DeepSeek API 文件以了解具體速率限制。
    *   **支援功能：** 聊天完成、聊天前綴完成 (Beta) [^10]。
    *   **程式碼範例 (Python)：**
        ```python
        from openai import OpenAI
        client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")
        messages = [{"role": "user", "content": "9.11 和 9.8，哪個比較大？"}]
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=messages
        )
        print(response.choices[^0].message.content)
        ```
        
*   **Grok (xAI)**：xAI 的 Grok 模型，包括 Grok-3 和 Grok-3 mini，設計上具備強大的推理能力。雖然 Grok-1.5 曾提供給早期測試者使用，但 Grok 3 即將透過 API 推出 [^11]。Grok 3 (Think) 和 Grok 3 mini (Think) 模型使用強化學習來改進其思維鏈過程，從而實現數據高效的高級推理 [^12]。

    *   **API 存取：** Grok 3 API 預計即將發布 [^11]。
    *   **定價：** 定價細節尚未公開。請查閱 xAI 網站以獲取更新。
    *   **速率限制：** 速率限制尚未公開。請查閱 xAI 網站以獲取更新。
    *   **支援功能：** 工具使用、程式碼執行和高級代理功能計劃用於企業版 API [^12]。
*   **Gemini 1.5 Pro**：作為 Google 的模型，Gemini 1.5 Pro 擅長對大量資訊進行推理，並針對多種推理任務進行了優化 [^13]。它是一個多模態模型，提供更強大的推理能力，包括回應中的思考過程 [^14]。Gemini API 為開發者提供了 200 萬個 token 的上下文視窗 [^15]。

    *   **API 存取：** 可透過 Gemini API 使用 [^15]。
    *   **定價：** 請查閱 Google AI Studio 定價頁面以獲取詳細資訊。
    *   **速率限制：** 文字嵌入的速率限制為每分鐘 1,500 個請求 [^16]。請查閱 Google AI Studio 文件以了解其他速率限制。
    *   **支援功能：** 函數呼叫、程式碼執行、可調整的安全設定、JSON 模式 [^17]。

**比較分析：**

| 功能特點          | OpenAI o-series | DeepSeek R1       | Grok (xAI)        | Gemini 1.5 Pro    |
| :---------------- | :-------------- | :---------------- | :---------------- | :---------------- |
| 性能表現          | STEM 領域強勁   | 匹配/超越 o1-mini | 推理能力強勁      | 整體表現強勁      |
| API 存取          | Azure OpenAI    | DeepSeek API      | 即將推出          | Gemini API        |
| 成本              | 視情況而定      | 成本效益高        | 尚未公布          | 請查閱 Google AI Studio |
| 上下文視窗        | 20 萬個 token   | 6.4 萬個 token    | 100 萬個 token    | 200 萬個 token    |
| 預期使用案例      | 複雜任務        | 數學、編程        | 廣泛推理          | 數據分析          |

**限制：**

*   **OpenAI o-series：** 預設可能不會產生 Markdown 格式 [^1]。
*   **DeepSeek R1：** 對於非英語/中文查詢，性能可能會下降 [^18]。
*   **Grok (xAI)：** API 尚未發布；關於具體功能的資訊有限。
*   **Gemini 1.5 Pro：** 實驗模型不適用於生產環境 [^19]。

[^1]: Azure OpenAI o 系列模型旨在以更高的專注度和能力處理推理和解決問題的任務 [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^2]: 推理模型將推理 token 作為完成 token 的一部分，詳細資訊請參閱模型回應 [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^3]: 支援 JSON 模式 [ai.google.dev](https://ai.google.dev/models/gemini)

[^4]: 我們的 API 讓使用者能夠存取 deepseek reasoner 生成的 CoT 內容，使他們能夠查看、顯示和提煉這些內容 [searchenginejournal.com](https://www.searchenginejournal.com/googles-ai-search-is-improving-but-still-lags-behind-human-quality-results/508459/)

[^5]: 以極低的成本和更高的性能，DeepSeek 提供其完整的 R1 API，與 OpenAI 相比僅需極小部分的成本 [seo-kueche.de](https://www.seo-kueche.de/blog/google-stellt-gemini-vor-das-kann-der-neue-ki-chatbot/)

[^6]: 全系列模型均經過高精度微調，指令遵循強化，對於複雜語言理解、深度推理、文本生成，均有優秀的結果表現 [cloud.baidu.com](https://cloud.baidu.com/doc/wenxinworkshop/s/jlil5u56k)

[^7]: xAI Grok 3 API 將在未來幾週內推出 [t.me](https://t.me/s/GPT4Telegram)

[^8]: 今天我們宣布推出兩個 Beta 版推理模型：Grok 3 Think 和 Grok 3 mini Think [x.ai](https://x.ai/blog/grok-3)

[^9]: Gemini 1.5 Pro 是一個中等規模的多模態模型，針對多種推理任務進行了優化 [ai.google.dev](https://ai.google.dev/models/gemini)

[^10]: 提供更強大的推理能力，並在回應中包含思考過程 [youtube.com](https://www.youtube.com/watch?v=YQAydVlHV7c)

[^11]: 輸入 token 限制為 2,097,152 [ai.google.dev](https://ai.google.dev/models/gemini)

[^12]: 關閉推理功能時，Grok 3 會提供即時的高品質回應 [x.ai](https://x.ai/blog/grok-3)

[^13]: Gemini 1.5 Pro 是一個中等規模的多模態模型，針對多種推理任務進行了優化。1.5 Pro 能夠一次處理大量數據 [ai.google.dev](https://ai.google.dev/models/gemini)

[^14]: 預設情況下，o3 mini 和 o1 模型不會嘗試產生包含 Markdown 格式的輸出 [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/reasoning)

[^15]: DeepSeek R1 針對英語和中文進行了優化，但對於其他語言的查詢，其性能可能會下降 [datacamp.com](https://datacamp.com/blog/deepseek-r1)

[^16]: 該 API 提供定義於條款中的預覽版實驗模型，意味著這些模型不適用於生產環境 [ai.google.dev](https://ai.google.dev/models/gemini)

[^17]: API 存取自訂 AI 開發對於開發者 xAI 計劃發布 Grok 3 的 API 存取權限，允許開發者整合其 [medium.com](https://medium.com/@gerardnico/a-timeline-to-grok-3-the-race-to-catch-up-54e0c0d1886c)

[^18]: 我們介紹 DeepSeek R1，它在 RL 之前引入了冷啟動數據。DeepSeek R1 在數學、編程和...方面實現了與 OpenAI o1 相當的性能 [api-docs.deepseek.com](https://api-docs.deepseek.com/guides/reasoning_model)

[^19]: Gemini 1.5 Pro 是一個中等規模的多模態模型，針對多種推理任務進行了優化 [ai.google.dev](https://ai.google.dev/models/gemini)