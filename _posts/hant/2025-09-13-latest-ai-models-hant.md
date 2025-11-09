---
audio: false
date: 2025-09-13
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 最新人工智能模型及其應用
translated: true
type: note
---

以下是我們截至2025年9月中旬對 GPT-5、Gemini 2.5 Pro、GPT-5 mini 及其在 Copilot / 高級模型中的應用現況總結：

---

## GPT-5（OpenAI）

* **發佈日期**：2025年8月7日（[OpenAI][1]）
* **模型簡介**：統一型大型語言模型，具備更強推理能力、更低幻覺率，並在編程、數學、寫作、健康、視覺感知等領域表現提升。內含「GPT-5 pro」版本處理高需求任務（[OpenAI][1]）
* **推理機制**：具備內部分層思考架構（「快速」與「深度推理」模式），用戶可選擇「GPT-5思考模式」或使用「請深入思考」等提示觸發進階推理（[OpenAI][1]）
* **存取層級與限制**：

  * 所有 ChatGPT 用戶（免費與付費）皆可使用（[OpenAI][1]）
  * 免費用戶有使用次數限制，超額後可能切換至輕量版「GPT-5 mini」（[OpenAI][1]）
  * 付費方案（Plus/Pro/Team/Enterprise/EDU）享有更高使用額度；Pro 用戶可使用「GPT-5 pro」（[OpenAI][1]）

---

## Gemini 2.5 Pro（Google）

* **發佈時程**：

  * 實驗版 Gemini 2.5 Pro 於2025年3月25日首度公開（[blog.google][2]）
  * 穩定版（正式發佈）於2025年6月17日推出（[Google Cloud][3]）
* **功能特色**：此為 Gemini 2.5 系列中最先進模型，具備百萬詞元上下文窗口、強化推理與編程能力、多語言支援等特性（[blog.google][2]）

---

## GPT-5 mini

* **定位與時程**：GPT-5 輕量加速版，2025年8月中旬於 GitHub Copilot 開放公開預覽（[The GitHub Blog][4]）
* **應用場景**：適用於 GitHub Copilot Chat（網頁版）、VS Code 插件及 GitHub Mobile（iOS/Android），並將出現於用戶模型選單（[The GitHub Blog][4]）
* **高級請求計費**：在 GitHub Copilot 付費方案中使用 GPT-5 mini **不消耗**「高級請求」額度（[The GitHub Blog][4]）

---

## **Copilot / 高級服務 / Microsoft / GitHub** 應用現況

* **GitHub Copilot**：

  * 所有方案（含免費版）現已支援 GPT-5 mini（[The GitHub Blog][4]）
  * 完整版 GPT-5 僅限付費 Copilot 方案使用（[The GitHub Blog][5]）
  * 模型選單依方案與組織設定提供 GPT-5、GPT-5 mini 等選項（[The GitHub Blog][4]）

* **Microsoft Copilot / Copilot Studio / 365 Copilot**：

  * Microsoft Copilot 產品線支援 GPT-5，例如 Copilot Studio 開發者可選用 GPT-5，系統會自動調度不同變體（對話型 vs 推理型）（[Microsoft Developer][6]）
  * 高級功能通常需付費訂閱，GPT-5 或高規格模型多限付費用戶與企業層級使用（[OpenAI][1]）

---

是否需要進一步了解**效能比較**（GPT-5 vs Gemini 2.5 Pro 等）或**未來傳聞功能**？

[1]: https://openai.com/index/introducing-gpt-5/?utm_source=chatgpt.com "Introducing GPT-5"
[2]: https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/?utm_source=chatgpt.com "Gemini 2.5: Our most intelligent AI model"
[3]: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions?utm_source=chatgpt.com "Model versions and lifecycle | Generative AI on Vertex AI"
[4]: https://github.blog/changelog/2025-08-13-gpt-5-mini-now-available-in-github-copilot-in-public-preview/?utm_source=chatgpt.com "GPT-5 mini now available in GitHub Copilot in public preview"
[5]: https://github.blog/changelog/2025-09-09-openai-gpt-5-and-gpt-5-mini-are-now-generally-available-in-github-copilot/?utm_source=chatgpt.com "OpenAI GPT-5 and GPT-5 mini are now generally available ..."
[6]: https://developer.microsoft.com/blog/gpt-5-for-microsoft-developers?utm_source=chatgpt.com "GPT-5 for Microsoft Developers"