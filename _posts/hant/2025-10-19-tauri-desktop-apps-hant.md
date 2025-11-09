---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 桌面應用程式的 Tauri 框架
translated: true
type: note
---

### 什麼是 Rust 中的 Tauri？

Tauri 是一個開源框架，用於構建輕量級、安全且高效的桌面（及流動）應用程式。其後端主要使用 Rust 編寫，負責處理核心邏輯、系統互動及安全性，同時允許您使用任何前端網頁技術（HTML、CSS、JavaScript/TypeScript）。這使其成為希望運用網頁開發技能、又不想承擔傳統工具（如 Electron）額外負擔的開發者的熱門選擇，最終生成的應用程式二進制文件體積大幅縮小（通常低於 10MB）。

#### 主要特性：
- **跨平台支援**：可從單一代碼庫構建適用於 Windows、macOS、Linux、Android 及 iOS 的應用程式。
- **安全導向**：Rust 的記憶體安全特性與 Tauri 的權限模型能最大限度減少漏洞；由於不使用完整瀏覽器引擎，攻擊面更小。
- **前端靈活性**：可與 React、Vue、Svelte 等框架或純 JavaScript 協作——任何能編譯為網頁資源的技術皆可適用。
- **Rust 整合**：後端透過 Rust crates 處理檔案 I/O、網絡通訊或數據庫存取等任務，並可透過安全 API 從前端輕鬆調用。
- **輕量佔用**：相較於其他方案，應用程式運行更快速且資源效率更高，得益於其採用系統原生的 webview。

在 Rust 生態系統中，Tauri 特別吸引人之處在於能夠創建具原生體驗的應用程式，同時不犧牲開發效率。該項目持續積極維護，2.0 版本更進一步強化了流動端支援與性能優化。

欲了解更多詳情，請查閱官方文件或 GitHub 代碼庫。

[官方 Tauri 網站](https://v2.tauri.app/)  
[Tauri GitHub 代碼庫](https://github.com/tauri-apps/tauri)  
[Tauri 維基百科頁面](https://en.wikipedia.org/wiki/Tauri_%28software_framework%29)