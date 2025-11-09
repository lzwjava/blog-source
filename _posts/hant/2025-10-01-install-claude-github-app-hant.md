---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 安裝 Claude GitHub 應用程式以協作
translated: true
type: note
---

透過在 Claude Code（Anthropic 的人工智慧驅動編碼工具）中使用 `/install-github-app` 指令安裝 Claude GitHub App，可實現與 GitHub 的無縫整合。這讓您能在 GitHub issues 或 pull requests (PR) 的評論中直接標注 @claude，使 Claude 能作為「虛擬隊友」在 GitHub 介面中協助回應反饋、修復錯誤或建議程式碼修改。該指令將引導您完成設定流程，包括使用 Claude Max 訂閱帳號登入及選擇儲存庫。[1][2][3] 此功能將 Claude 從終端工具轉變為您開發工作流程中的活躍參與者，特別適合協作編碼與 CI/CD 管道。[3][4][5][6][7]

參考文獻：
[1] https://github.com/anthropics/claude-code-action
[2] https://www.reddit.com/r/ClaudeAI/comments/1kvabkk/use_claude_github_app_with_your_claude_max_w/
[3] https://github.com/apps/claude
[4] https://www.youtube.com/watch?v=0kJh4KuJ1nY
[5] https://apidog.com/blog/claude-code-github-actions/
[6] https://www.youtube.com/watch?v=FjHtZnjNEBU
[7] https://www.youtube.com/watch?v=L_WFEgry87M