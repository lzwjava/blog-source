---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: MSYS2：Windows 上的 Unix 環境
translated: true
type: note
---

MSYS2 是一個專為 Windows 設計的免費開源軟體發行版與建構平台。它直接在 Windows 上提供類 Unix 環境（類似 Linux 或 macOS shell），並配備了 Bash、GCC 編譯器及名為 Pacman 的套件管理器等工具。這讓開發、建構、安裝和執行原生 Windows 應用程式變得更加容易——特別是那些源自 Unix/Linux 生態系統的應用——無需使用完整的虛擬機器或雙重開機設定。

### 主要功能
- **套件管理**：使用 Pacman 從軟體庫安裝數千個預先建置的套件（例如函式庫、Git、Python 或 Vim 等工具）。
- **環境子系統**：包含三個子系統：
  - **MSYS**：用於 POSIX 相容工具。
  - **MinGW-w64**：用於交叉編譯為 Windows 可執行檔（32 位元或 64 位元）。
  - **UCRT64/MINGW64**：具有更佳 Windows 整合度的現代化變體。
- **使用情境**：廣泛應用於 C/C++ 開發、腳本編寫，以及將開源軟體移植到 Windows。常與 VS Code 等 IDE 搭配使用，實現無縫工作流程。

它輕量、積極維護，並可在 Windows 10/11 上運行（舊版透過傳統安裝程式支援 Windows 7）。如果您熱衷程式設計，或需要在 Windows 上進行終端機密集型操作，對許多開發者而言，它是 WSL 的首選替代方案。

[MSYS2 官方網站](https://www.msys2.org/)  
[MSYS2 GitHub 儲存庫](https://github.com/msys2)