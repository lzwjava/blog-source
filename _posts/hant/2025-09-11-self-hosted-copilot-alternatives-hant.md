---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 自託管本地副駕駛替代方案
translated: true
type: note
---

你在尋找開源工具來本地自託管「類Copilot」體驗——這些工具可以自行運行（使用自己的token或模型），或許還能整合到VS Code或其他IDE中。這裡沒有表格，只有清晰簡潔的說明。以下是最知名的選項：

---

### **Tabby**

一個用Rust編寫的自託管AI編程助手。它是開源的，無需外部服務，並提供OpenAPI風格的接口——使得與本地IDE和基礎設施的整合變得直接。它甚至支援消費級GPU和編輯器整合，包括Vim/Neovim。（[GitHub][1], [Software Recommendations Stack Exchange][2]）

---

### **FauxPilot**

一個開源項目，設計為GitHub Copilot的本地託管替代方案。它利用Salesforce的CodeGen模型，通過NVIDIA的Triton Inference Server（和FasterTransformer）運行。可通過Docker部署，與類Copilot客戶端兼容，並在擁有高性能GPU時表現最佳。（[GitHub][3]）

---

### **Privy**

另一個MIT許可的開源工具，可在本地運行。它提供類似GitHub Copilot的實時代碼補全和聊天功能。它可以與LLM運行時（如Ollama、llama.cpp或llamafile）整合，並根據你的硬體支援流行的編程模型（如CodeLlama變體）。（[GitHub][4]）

---

### **GPT4All、Continue、LocalPilot** *（及類似工具）*

在Tabby和FauxPilot之外，還有幾個自託管工具被提及；這些工具提供注重本地隱私的編程輔助。雖然它們不一定那麼完善，但在硬體限制或特定工作流程需求下，它們是可行的選擇。（[Virtualization Howto][5]）

---

### **Ollama（與Docker結合）**

本身不是完整的Copilot替代品，而是一個強大的開源工具，用於本地運行LLM。你可以通過Docker使用Ollama託管模型（如Phi-2），然後通過LLM擴展（例如Hugging Face的`llm-vscode`）連接到VS Code。這讓你可以與本地模型聊天或獲得編程協助。（[Tommaso Colella][6], [Reddit][7]）

---

### **社群熱議**

來自Reddit的討論：

* 「使用Ollama AI在docker伺服器上免費自託管你自己的『Copilot』」——強調Ollama的有效性及其與VS Code的整合。（[Reddit][7]）
* 「Tabby（現在）是最受歡迎的『開源與本地』工具」——指出其日益增長的採用率。（[Reddit][8]）

---

### **總結建議**

* **如果你想要一個完善的開源Copilot替代品：** 從**Tabby**開始。
* **如果你想要更接近Copilot基礎設施的東西（且擁有強大的GPU）：** 試試**FauxPilot**。
* **如果你想要代碼補全+聊天功能，並在模型/運行時上具有靈活性：** 嘗試**Privy**。
* **想要完全控制端點和模型？** 將**Ollama**與你自己的LLM配對，然後使用標準LLM接口連接。

---

### **你的後續步驟**

1. **評估硬體：** FauxPilot和Privy可能需要不錯的GPU；Tabby更輕量。
2. **選擇一個運行時/框架：**

   * **Tabby**：全面的優秀選擇，支援編輯器。
   * **FauxPilot**：類Copilot，使用Docker和Triton。
   * **Privy**：靈活、模型無關的設定。
   * **Ollama + LLM**：純DIY——如果你習慣自己構建端點，這會很棒。
3. **連接到你的IDE：** VS Code（或其他IDE）支援通過本地端點使用這些工具，就像Copilot一樣。

如果你需要任何特定工具的入門幫助或設定步驟，請告訴我！

[1]: https://github.com/TabbyML/tabby?utm_source=chatgpt.com "TabbyML/tabby: Self-hosted AI coding assistant"
[2]: https://softwarerecs.stackexchange.com/questions/90507/foss-alternative-to-github-copilot?utm_source=chatgpt.com "FOSS alternative to GitHub Copilot?"
[3]: https://github.com/fauxpilot/fauxpilot?utm_source=chatgpt.com "FauxPilot - an open-source alternative to ..."
[4]: https://github.com/srikanth235/privy?utm_source=chatgpt.com "srikanth235/privy: An open-source alternative to ..."
[5]: https://www.virtualizationhowto.com/2025/05/best-self-hosted-github-copilot-ai-coding-alternatives/?utm_source=chatgpt.com "Best Self-hosted GitHub Copilot AI Coding Alternatives"
[6]: https://gioleppe.github.io/posts/diy-copilot-phi/?utm_source=chatgpt.com "DIY self-hosted Copilot using Phi-2 and Ollama"
[7]: https://www.reddit.com/r/vscode/comments/1by7njo/self_host_your_own_copilot_for_free_with_ollama/?utm_source=chatgpt.com "Self host your own \"Copilot\" for FREE with Ollama AI on a ..."
[8]: https://www.reddit.com/r/LocalLLaMA/comments/12m8fnm/best_local_equivalent_of_github_copilot/?utm_source=chatgpt.com "Best local equivalent of GitHub Copilot? : r/LocalLLaMA"