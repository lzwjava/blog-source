---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Ghostty：快速跨平台終端模擬器
translated: true
type: note
---

Ghostty 是一款跨平台終端機模擬器，專為追求速度、功能豐富性及 macOS 與 Linux 原生整合而設計（Windows 支援開發中）。其主要採用 **Zig** 建構——這是一種專注於安全性、效能與簡潔性的現代系統程式語言，而非您詢問的 Rust。

### 核心實作細節
- **核心架構**：共享核心（負責終端模擬、渲染及多數邏輯處理）以 Zig 編寫，可實現底層控制與高效能表現，包括透過 Metal（macOS）或 Vulkan/OpenGL（跨平台）進行 GPU 加速。
- **平台專屬層**：為實現原生操作體驗，採用平台專屬工具包構建圖形介面：
  - macOS：使用 Swift/AppKit 處理視窗與使用者介面。
  - Linux：使用 GTK 處理視窗管理。
  - 以 Zig 編寫的共享渲染管線將各平台元件無縫整合。
- **設計亮點功能**：
  - 極速啟動與渲染（例如可無延遲處理大量輸出內容）。
  - 支援連字、表情符號與進階文字排版功能。
  - 可透過 Lua 腳本進行配置，實現功能擴展。
  - 無冗餘設計——在保持極簡風格的同時，內建分頁、搜尋及 OSC 52 剪貼簿整合等核心功能。
- **開發理念**：由 Mitchell Hashimoto（HashiCorp 創辦人）創建，強調正確性與執行效率，捨棄傳統終端機（如 xterm）常見的相容性補丁。專案採用 MIT 許可證開源。

若您有興趣參與開發或進行二次開發，請查閱 GitHub 儲存庫獲取 Zig 程式碼庫與建置說明（需 Zig 0.13+ 版本）。

### 參考資源
- [Ghostty GitHub 儲存庫](https://github.com/ghostty-org/ghostty)
- [Ghostty 介紹（Mitchell Hashimoto 部落格）](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns)
- [Ghostty 1.0 版本發布說明](https://dansasser.me/posts/ghostty-1-0-a-terminal-emulator-built-for-speed-features-and-native-integration/)