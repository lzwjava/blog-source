---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Copilot 企業級模型選項概覽
translated: true
type: note
---

你詢問的是 **Copilot Enterprise** 使用哪種模型，特別是它是否為 GPT-4.1、GPT-4o 或其他模型。以下是截至 **2025 年 9 月** 的最新相關資訊：

---

### Copilot Enterprise 有哪些可用模型？

#### GitHub Copilot Enterprise 與 Copilot Chat

* **預設情況下**，GitHub Copilot Enterprise（以及 Copilot Chat）**運行於 GPT-4o**，提供更快的回應速度和改進的品質。 ([Reddit][1])
* 近期，**GPT-4.1** 已可供使用 — 但管理員必須在 Copilot 設定中透過政策**明確啟用**。啟用後，使用者可以在 VS Code 和 github.com 的模型選擇器中選取 GPT-4.1。 ([The GitHub Blog][2])

#### Visual Studio Copilot

* 截至 **2025 年 6 月**，Visual Studio 的 Copilot **現已使用 GPT-4.1 作為其預設模型**，取代了 GPT-4o。微軟的測試顯示 GPT-4.1 能提供**更快的回應、更高品質的建議和更高的效率**。 ([Visual Studio Magazine][3], [Microsoft Learn][4])

#### Microsoft 365 Copilot (Office 生產力工具)

* 微軟已開始透過新的「**智慧模式 (Smart Mode)**」將 **GPT-5** 整合到更廣泛的 Copilot 生態系統中 — 包括 Microsoft 365 Copilot、GitHub Copilot、Copilot Studio 等 — 該模式會根據需求自動將任務路由到最合適的模型，從而改善推理、上下文保留和互動品質。 ([The Verge][5])
* 此外，微軟宣布整合 Anthropic 的 **Claude Sonnet 4** 用於進階任務，例如簡報設計和試算表自動化，同時在其他功能上仍使用 **GPT-5**（以及其餘基於 GPT 的路由）。 ([New York Post][6])

---

### 總結 — 哪種模型適合 **Copilot Enterprise**？

* **GitHub Copilot Enterprise / Copilot Chat**：

  * 預設：**GPT-4o**
  * 可選：**GPT-4.1**（若由管理員啟用）
* **Visual Studio Copilot**：預設現為 **GPT-4.1**
* **Microsoft 365 Copilot**：利用 **GPT-5 智慧模式**，具有更高性能的路由和能力 — 並且也整合了 **Claude Sonnet 4** 用於特定的企業任務。

---

### 快速概覽（依您偏好，不使用寬表格）：

* **GPT-4o**：GitHub Copilot Enterprise 中的預設模型；以企業聊天中的速度和品質聞名。
* **GPT-4.1**：功能更強大的後繼模型 — 更擅長程式碼、遵循指令和長上下文。若已啟用，可在 GitHub Copilot 中使用，並且現為 Visual Studio Copilot 的預設模型。 ([OpenAI][7])
* **GPT-5**：最新模型，透過智慧模式整合到 M365 Copilot 及所有 Copilot 平台中，用於更智慧的模型選擇。 ([The Verge][5])
* **Claude Sonnet 4**：主要為 Office 任務（如 PowerPoint 和 Excel 自動化）而添加，與 GPT-5 並行。 ([New York Post][6])

---

### 接下來該做什麼？

* 如果您是管理 GitHub Copilot Enterprise 的**管理員**，請檢查您的設定，若您希望使用者利用其性能改進，請**啟用 GPT-4.1**。
* 如果您使用 **Visual Studio Copilot**，您已經預設使用 **GPT-4.1**。
* 對於 **Microsoft 365 Copilot**，您將受益於 **GPT-5 智慧模式**的推出和 **Claude Sonnet 4** 的整合。無需任何操作 — 它已是服務層的一部分。

如果您需要協助配置這些設定或根據您組織的特定環境來選擇模型選項，請告訴我！

[1]: https://www.reddit.com/r/GithubCopilot/comments/1dx2iq1/github_copilot_enterprise_on_gpt4o/?utm_source=chatgpt.com "GitHub Copilot Enterprise on GPT-4o : r/GithubCopilot"
[2]: https://github.blog/changelog/2025-04-14-openai-gpt-4-1-now-available-in-public-preview-for-github-copilot-and-github-models/?utm_source=chatgpt.com "OpenAI GPT-4.1 now available in public preview for GitHub ..."
[3]: https://visualstudiomagazine.com/articles/2025/06/26/new-default-model-for-visual-studio-copilot-so-how-do-you-choose.aspx?utm_source=chatgpt.com "New Default Model for Visual Studio Copilot, So How Do ..."
[4]: https://learn.microsoft.com/en-us/visualstudio/ide/copilot-select-add-models?view=vs-2022&utm_source=chatgpt.com "Using AI models in Copilot Chat - Visual Studio (Windows)"
[5]: https://www.theverge.com/news/753984/microsoft-copilot-gpt-5-model-update?utm_source=chatgpt.com "Microsoft brings GPT-5 to Copilot with new smart mode"
[6]: https://nypost.com/2025/09/10/business/microsoft-to-add-anthropic-ai-models-as-rift-with-openai-grows-report/?utm_source=chatgpt.com "Microsoft to add Anthropic AI models - as rift with OpenAI grows: report"
[7]: https://openai.com/index/gpt-4-1/?utm_source=chatgpt.com "Introducing GPT-4.1 in the API"