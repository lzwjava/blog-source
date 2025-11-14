---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Claude 代碼在 Windows 上使用 Git Bash
translated: true
type: note
---

是的，根據最新動態，Claude Code（Anthropic 推出的 AI 編程工具）在 Windows 系統上確實會觸發 `git-bash.exe` 來執行 shell 指令。該工具經常使用 Git Bash 作為指令執行環境，特別是在未配置 WSL 的原生 Windows 環境中。這可能導致執行指令時彈出終端視窗，且目前存在與確保 Git Bash 正確被檢測及使用相關的已知配置、擴充功能（例如 VS Code 中的擴充）及故障排除步驟。

舉例來說：
- 在原生 Windows 環境中，Claude Code 依賴 Git Bash 來提供類 Unix 兼容性，以處理腳本和指令。
- 若設為預設終端（例如在 VS Code 或 Cursor 等整合工具中），它會啟動 `git-bash.exe` 來執行任務。
- 目前存在已回報的錯誤和處理指南，涉及影響此整合的 Git 安裝路徑問題或路徑中的空格字元。

若您遇到問題，請檢查系統 PATH 環境變數、確保 Git 已正確安裝，並驗證 IDE 中的終端設定檔。

參考資料：  
[Claude Code 原生 Windows Bash 輸出未顯示 - Reddit](https://www.reddit.com/r/ClaudeAI/comments/1m06s2l/claude_code_native_windows_bash_output_not_seen/)  
[錯誤：Claude Code VS Code 擴充功能無法檢測 Git Bash - GitHub](https://github.com/anthropics/claude-code/issues/8674)  
[Claude Code 在 Windows 上的安裝故障排除 - Medium](https://medium.com/%40tomhag_17/troubleshooting-claude-code-installation-on-windows-from-tty-errors-to-success-1f44af03c9f2)  
[在未配置 WSL 的 Windows 上運行 Claude Code - 部落格](https://blog.shukebeta.com/2025/06/25/running-claude-code-on-windows-without-wsl/)  
[AI 代理 Claude 4 即使在預設終端為 Git Bash 時仍於 PowerShell 執行指令 - 論壇](https://forum.cursor.com/t/ai-agent-claude-4-runs-commands-in-powershell-even-when-default-terminal-is-git-bash/137164)  
[2025 年 Windows 安裝 Claude Code 完整指南 - Itecsonline](https://itecsonline.com/post/how-to-install-claude-code-on-windows)  
[錯誤：Claude Code 無法解析含空格的 Git Bash 路徑 - GitHub](https://github.com/anthropics/claude-code/issues/4507)  
[未配置 WSL 的 Windows 安裝 Claude Code 逐步指南 - YouTube](https://www.youtube.com/watch?v=LtnxvLZjxAI)  
[47 個每位 Windows 用戶都應知道的 Claude Code WSL 技巧 - Medium](https://medium.com/%40joe.njenga/47-claude-code-wsl-tricks-every-windows-user-should-know-5d42aaee2d93)  
[Windows 11 安裝 Claude Code 指南：透過 WSL2 設置 - Claude AI](https://claude.ai/public/artifacts/03a4aa0c-67b2-427f-838e-63770900bf1d)