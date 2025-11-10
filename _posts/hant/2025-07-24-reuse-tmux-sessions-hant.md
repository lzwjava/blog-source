---
audio: false
generated: true
lang: hant
layout: post
title: 重用現有 tmux 工作階段
translated: true
type: note
---

要重用現有的 tmux 工作階段（例如你案例中的 `1` 或 `8`），你可以在啟動 tmux 時附加到現有工作階段。以下是具體做法：

### 解決方案
1. **列出現有工作階段**：
   執行 `tmux list-sessions`（或 `tmux ls`）查看所有活躍工作階段：
   ```
   tmux list-sessions
   ```
   輸出範例（根據你的案例）：
   ```
   1: 1 windows (created Thu Jul 10 03:03:47 2025)
   8: 1 windows (created Thu Jul 24 02:11:07 2025)
   ```

2. **附加到特定工作階段**：
   與其執行 `tmux`（會建立新工作階段），不如使用 `attach-session`（或 `attach`）指令連接現有工作階段。例如：
   - 要附加到工作階段 `1`：
     ```
     tmux attach-session -t 1
     ```
   - 要附加到工作階段 `8`：
     ```
     tmux attach-session -t 8
     ```

   可將 `attach-session` 簡寫為 `attach`：
   ```
   tmux attach -t 1
   ```

3. **檢查 tmux 是否已在運行**：
   若嘗試附加到不存在的工作階段，tmux 會拋出錯誤。為避免意外建立新工作階段，可在啟動前檢查 tmux 是否正在運行。例如，將以下內容加入 shell 腳本或工作流程：
   ```
   tmux has-session -t 1 && tmux attach -t 1 || tmux new-session -s 1
   ```
   此指令會檢查工作階段 `1` 是否存在：若存在則附加，否則建立名為 `1` 的新工作階段。

4. **提升操作便利性**：
   - **建立別名**：在 shell 配置檔案（如 `~/.zshrc` 或 `~/.bashrc`）中加入別名，始終附加到特定工作階段：
     ```
     alias tmux1='tmux attach -t 1 || tmux new-session -s 1'
     ```
     之後執行 `tmux1` 即可附加到工作階段 `1`（若不存在則自動建立）。
   - **預設工作階段**：若想始終使用特定工作階段（如 `1`），可建立腳本或配置 `.tmux.conf` 實現自動化。

5. **避免建立新工作階段**：
   為避免執行 `tmux` 時預設建立新工作階段，可配置工作流程始終檢查現有工作階段。例如修改 shell 配置：
   ```
   tmux attach -t 1 2>/dev/null || tmux new-session -s 1
   ```
   此指令會嘗試附加到工作階段 `1`（若不存在則抑制錯誤），僅在必要時建立新工作階段。

6. **可選：為工作階段命名提升清晰度**：
   與其依賴數字工作階段 ID（如 `1`, `8`），可為工作階段命名以便管理。例如：
   ```
   tmux new-session -s mywork
   ```
   之後透過以下指令附加：
   ```
   tmux attach -t mywork
   ```

### 問題成因
當不帶參數執行 `tmux` 時，會建立帶有自動遞增 ID（如 `1`, `8`）的新工作階段。為防止工作階段編號持續增加，必須明確使用 `tmux attach -t <工作階段>` 附加到現有工作階段。

### 範例工作流程
要始終使用工作階段 `1`：
1. 執行 `tmux list-sessions` 檢查工作階段 `1` 是否存在
2. 若存在則執行 `tmux attach -t 1`
3. 若不存在則執行 `tmux new-session -s 1`

可在 shell 中自動化此流程：
```bash
if tmux has-session -t 1 2>/dev/null; then
  tmux attach -t 1
else
  tmux new-session -s 1
fi
```

### 注意事項
- 若工作階段已被其他客戶端附加，可能需要先分離該客戶端（`tmux detach`），或使用 `tmux attach -t 1 -d` 強制分離其他客戶端
- 可透過 `tmux kill-session -t <工作階段>`（如 `tmux kill-session -t 8`）清理未使用的工作階段

此方法能確保你重用 `1` 或 `2` 等工作階段，避免工作階段數量持續增加。

[tmux 手冊頁](https://man.openbsd.org/tmux.1)