---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 頂級 macOS 終端機模擬器替代方案
translated: true
type: note
---

除了 iTerm2 和 Ghostty 之外，macOS 上流行的終端模擬器還包含多款開源及專有選項，能滿足效能、功能與自訂化等不同需求。以下清單基於近期推薦與評比，聚焦於 macOS 相容應用程式。

### 熱門替代方案
- **Alacritty**：具 GPU 加速的高速終端機，支援自訂主題與 Vim 式編輯。輕量高效，專為純粹編碼需求設計。[1] [1][2]
- **Kitty**：以 GPU 加速聞名，具分頁視窗、分割畫面及桌面通知等現代功能。支援擴充套件，適合需要高效處理大型工作流程的進階用戶。[1] [2][3][4]
- **WezTerm**：跨平台終端機，具序列多工處理、圖形化選取與 Lua 腳本編寫等進階功能。適合需要精細配置與高效多工處理的使用者。[1][5]
- **Warp**：現代化終端機，內建 AI 協作功能如「Warptime」會議分享與自動補全。介面對團隊友善，但獨特操作介面需時間適應。[1] [3][4][5]
- **Hyper**：基於網頁技術開發，可透過外掛與主題擴充功能。適合想用 CSS 與 JavaScript 自訂介面的開發者，但需注意資源消耗較高。[4][5]
- **Tabby**：多功能終端機，支援 SSH/Telnet 連線、多語言主題與分割視窗。適合遠端工作或日常基礎使用，並提供憑證加密選項。[6]（Reddit 討論指出 Tabby 雖存在潛在錯誤，仍被視為可行替代方案）
- **CoreShell**：專注 SSH 與 SFTP 連線，具智能認證與工作階段管理功能。最適合需安全遠端連線的場景，而非本地終端作業。[3] [4]
- **Commander One**：內建終端機的檔案管理員，提供雙窗瀏覽與快速指令功能。較偏向圖形化介面操作，適合需同時處理檔案與終端指令的使用者。[5]

這些選項均為免費或提供免費版本，社群支援程度各異。macOS 原生終端機應用程式始終是基礎選擇，但對進階用戶而言，Ghostty 與 iTerm2 仍是比較基準的首選。若需要 AI 整合或 GPU 加速等特定功能，可優先考慮 Warp 或 Alacritty；若重視自訂性，請查閱各專案的 GitHub 頁面確認 macOS 相容性。[3]（2025 年更新指南）

安裝多數終端機可透過 Homebrew（例如 `brew install --cask kitty`）或官方網站下載。建議根據自身工作模式選擇初始套件，因更換終端機需重新配置設定。各應用程式功能迭代迅速，請查閱官方發布說明以獲取最新版本。

引用來源：
[1] https://www.youtube.com/watch?v=WxzYtdIcHnQ
[2] https://erlangforums.com/t/which-terminal-emulator-do-you-use-poll/4368
[3] https://setapp.com/how-to/terminal-alternatives-for-mac?srsltid=AfmBOorowizKiascb9JBZSccPQ7V_EMpI2oWZYKGgoMihcje_nKWgc-q
[4] https://www.zdnet.com/article/6-macos-terminal-apps-that-are-much-better-than-apples-default-and-theyre-free/
[5] https://thenewstack.io/the-best-macos-terminal-emulation-programs-for-developers/
[6] https://www.reddit.com/r/MacOS/comments/1hvujf0/best_terminal_for_macos/