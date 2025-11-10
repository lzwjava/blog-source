---
audio: false
generated: true
lang: hant
layout: post
title: 更新Claude代碼命令行界面
translated: true
type: note
---

嗨！看來你正在使用 Anthropic 的 Claude Code CLI 工具。根據你貼出的輸出內容，它似乎已經嘗試自動更新到 1.0.61 版本，但如果更新未成功或你需要手動更新，以下是操作方法：

要更新 Claude Code CLI：
- 開啟你的終端機
- 執行指令：`claude update`
這個內建指令應該會獲取並安裝最新版本

如果更新失敗（例如因權限或網絡問題），你可以嘗試透過 npm 重新安裝（假設你已安裝 Node.js 和 npm）：
- 執行：`npm install -g @anthropic-ai/claude-code`

更新後，你可能需要重新登入，執行 `claude /login`（有時是 `claude login`，取決於版本）。如果你仍然看到錯誤，請檢查網絡連接、確保 API 金鑰有效，或參考官方疑難排解文件。

如需更多指令詳情，你可以執行 `claude --help` 查看更新版本中的選項。

[CLI 參考 - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/cli-reference)  
[如何專業地設置和使用 Claude CLI 工具](https://medium.com/@riccardo.bernardi.advisor/unlocking-claude-pros-power-how-to-set-up-and-use-the-claude-cli-tool-like-a-pro-against-github-d29f8f682a03)  
[GitHub - anthropics/claude-code](https://github.com/anthropics/claude-code)  
[Claude Code 概覽 - Anthropic API](https://docs.anthropic.com/en/docs/claude-code/overview)