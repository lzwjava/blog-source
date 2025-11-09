---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 升級克勞德代碼至最新版本
translated: true
type: note
---

要將 Claude Code 從 v2.0.0 升級至最新版本，請根據您的安裝類型選擇以下其中一種方法（所有版本預設支援自動更新，會在下次啟動工具時套用；您可透過設定 `DISABLE_AUTOUPDATER=1` 來停用此功能）：

### 透過 Claude Code 內建指令
在終端機中執行手動更新指令：
```
claude update
```
這會自動套用最新版本。[1][2]

### 透過 npm（若為全域安裝）
若您最初是透過 npm 安裝，請使用以下指令更新：
```
npm update -g @anthropic-ai/claude-code
```
或強制安裝最新版本：
```
npm install -g @anthropic-ai/claude-code@latest
```
[3][4]

### 透過原生二進位檔（Beta 安裝程式）
若為原生安裝，請重新執行安裝程式腳本來取得最新版本：
```
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash -s latest

# Windows PowerShell
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) latest
```
[1]

**驗證步驟：** 升級後，請執行 `claude --version` 檢查版本，確認已更新至當前穩定版本。若遇到問題，請確保 npm 為最新版本（可執行 `npm install -g npm@latest`）。所有設定與配置在更新過程中均會保留。[1][3][4]

引用來源：
[1] https://docs.claude.com/en/docs/claude-code/setup
[2] https://www.reddit.com/r/ClaudeAI/comments/1lvbijz/claude_code_updates_from_version_1045_to_1044/
[3] https://www.reddit.com/r/ClaudeAI/comments/1l8gbfo/dont_forget_to_update_your_claude_cli_it_makes_a/
[4] https://www.claudelog.com/faq/