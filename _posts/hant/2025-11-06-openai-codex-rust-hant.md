---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 基於 Rust 的 OpenAI Codex 命令行介面
translated: true
type: note
---

### OpenAI Codex CLI 與 Rust

GitHub 儲存庫 [https://github.com/openai/codex](https://github.com/openai/codex) 託管了 OpenAI 的 Codex，這是一個輕量級、實驗性的基於 CLI 的編碼代理，可在您的終端機中本地運行。它通過整合 OpenAI 模型（例如，透過 Responses API，預設為 o4-mini）來協助完成程式碼生成、編輯和除錯等任務。它支援透過 ChatGPT 帳戶或 API 金鑰進行身份驗證，透過 TOML 檔案進行配置，並透過 Model Context Protocol (MCP) 進行擴充。可透過 npm、Homebrew 或適用於 macOS 和 Linux 的直接二進位檔進行安裝。

#### Codex 如何使用 Rust？
Codex 的 CLI 工具已大部分使用 Rust 重寫，目前約佔程式碼庫的 96.7%（其餘部分為 Python、TypeScript 等）。Rust 實現（位於 `codex-rs` 子目錄中）為核心終端介面提供動力，包括：
- **原生二進位檔編譯**：產生用於跨平台分發的獨立可執行檔（macOS Apple Silicon/x86_64、Linux x86_64/arm64），無需外部執行時依賴。
- **安全功能**：使用 Rust 進行 Linux 沙箱處理，以安全地執行和測試生成的程式碼。
- **協定處理**：實現了可擴充的 "wire protocol"，用於 MCP 伺服器和未來的多語言擴充（例如，允許 Python 或 Java 附加元件）。
- **TUI (Terminal UI) 元件**：Rust 處理終端機中的文字選擇、複製/貼上和互動元素。

此轉變始於部分重寫（到 2025 年中約有一半程式碼使用 Rust），並已進展到近乎完全採用，發布標籤如 `rust-v0.2.0`。您可以透過 `npm i -g @openai/codex@native` 安裝原生 Rust 版本。原始的 TypeScript/Node.js 版本仍然可用，但一旦達到功能對等，將被逐步淘汰。

#### Rust 對它有幫助嗎？
是的，Rust 顯著提升了 Codex 作為 CLI 工具的可用性和可靠性。主要好處包括：
- **效能提升**：無垃圾回收執行時意味著更低的記憶體使用量和更快的啟動/執行速度，非常適合 CI/CD 管線或容器等資源受限的環境。
- **簡化分發**：單一靜態二進位檔消除了 "dependency hell"（例如，無需安裝 Node.js v22+、npm 或 nvm），使其更易於部署並減少用戶摩擦。
- **安全性改進**：Rust 的記憶體安全性和原生綁定實現了強大的沙箱處理以執行程式碼，防止在運行不受信任的生成程式碼的工具中出現漏洞。
- **可擴充性和可維護性**：wire protocol 允許與其他語言無縫整合，而 Rust 的生態系統支援快速迭代終端機特定功能，如 TUI。

這些特性使得 Codex 對於在終端機或 IDE（例如 VS Code 整合）中工作的開發人員來說更加穩健。

#### 他們為什麼使用 Rust？
OpenAI 從 TypeScript/Node.js 轉向 Rust，主要是為了解決 JS 生態系統在高效能、安全 CLI 方面的限制：
- **消除依賴**：Node.js 要求（例如特定版本）阻礙了沒有適當設定的用戶；Rust 二進位檔是零依賴且可移植的。
- **更好的程式碼執行安全性**：用於沙箱處理的原生 Rust 綁定已被使用，使得全面轉向對於更安全的本地程式碼測試來說是合乎邏輯的。
- **效能優化**：避免 JS 執行時開銷（例如 GC 暫停）確保了可預測、高效的資源使用——這對於即時處理 AI 生成程式碼的工具至關重要。
- **長期可擴充性**：Rust 實現了更輕鬆的擴充協定，並與 OpenAI 的 "原生" 感覺目標保持一致，與雙重 Node/Rust 程式碼庫相比，減少了維護負擔。

此遷移大約在 2025 年 6 月宣布，並有一個待辦事項清單追蹤任務，如 README 更新和 Homebrew formula 變更。它仍然是實驗性的，因此請期待持續的改進。

**參考資料**  
- [GitHub 儲存庫概覽](https://github.com/openai/codex)  
- [Reddit 上關於 Rust 重寫的討論](https://www.reddit.com/r/rust/comments/1lkdu2m/openai_is_ditching_typescript_to_rebuild_codex/)  
- [Heise 關於安全性與效能轉換的文章](https://www.heise.de/en/news/Security-and-performance-OpenAI-Codex-CLI-switches-from-TypeScript-to-Rust-10425172.html)  
- [SSOJet 部落格關於效率提升的文章](https://ssojet.com/blog/openai-codex-transitions-to-rust-enhancing-efficiency-and-power)