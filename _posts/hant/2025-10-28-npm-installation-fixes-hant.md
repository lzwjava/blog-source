---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: npm 安裝錯誤修正
translated: true
type: note
---

### 理解錯誤原因

這是在全域更新（或安裝）`@anthropic-ai/claude-code` 套件時發生的 npm 安裝失敗。關鍵問題出現在「reify」階段，npm 嘗試在安裝新版本前「retire」（備份）現有的套件目錄。具體來說：

- npm 正嘗試將 `/usr/lib/node_modules/@anthropic-ai/claude-code` 重新命名為一個臨時備份目錄，例如 `/usr/lib/node_modules/@anthropic-ai/.claude-code-ZjqcDZyQ`。
- 此操作失敗並出現 `ENOTEMPTY: directory not empty`（錯誤代碼 -39），這通常發生在以下情況：
  - 來源目錄包含被鎖定、正在使用或具有權限問題的檔案/子目錄。
  - 存在損壞的符號連結、開啟的檔案控制代碼（例如來自正在執行的 `claude` 程序）或 Linux 上的檔案系統異常。
  - 少數情況下，npm 內部的 move-file 邏輯遇到競爭條件。

你的環境設定：
- Node：v22.18.0
- npm：v11.6.1
- 作業系統：Linux 6.14.0-29-generic（可能是 Ubuntu/Debian）
- 以 root 權限執行（根據日誌路徑 `/root/.npm/_logs/`），因此權限不是根本原因。
- 工作目錄：`/home/lzwjava/projects/blog-source`（但這是全域安裝，所以無關緊要）。

該套件似乎是 Anthropic 的 Claude Code 工具（用於 AI 編碼輔助的 CLI），第 73 行顯示了 `@img/sharp-libvips-linux-x64` 的依賴項不匹配警告，但這與崩潰無關。

### 快速解決方法（請按順序嘗試）

1. **停止任何執行中的程序**：
   - 終止任何 `claude` CLI 或相關程序：`pkill claude`（或使用 `ps aux | grep claude` 查找 PID，然後執行 `kill <PID>`）。
   - 關閉正在使用該套件的終端機/IDE。

2. **手動清理目錄**：
   - 移除現有的套件和二進位檔：
     ```
     sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code
     sudo rm -f /usr/bin/claude
     ```
   - 這將繞過 npm 的備份步驟。然後重新嘗試安裝：
     ```
     sudo npm install -g @anthropic-ai/claude-code
     ```

3. **清除 npm 快取並重試**：
   - 執行：
     ```
     sudo npm cache clean --force
     sudo npm install -g @anthropic-ai/claude-code
     ```
   - 如果問題持續，請加入 `--no-optional` 以跳過可選依賴項（例如 Sharp 影像庫）。

4. **替代方案：使用 npx 或避免全域安裝**：
   - 如果不需要全域安裝，請在專案中本地安裝：`npm install @anthropic-ai/claude-code`（然後透過 `npx claude` 執行）。
   - 或使用 Yarn：`sudo yarn global add @anthropic-ai/claude-code`（Yarn 有時處理移動的方式不同）。

5. **如果問題仍然存在**：
   - 檢查檔案系統問題：`ls -la /usr/lib/node_modules/@anthropic-ai/`（查找異常的符號連結或鎖定）。
   - 暫時降級 npm：`sudo npm install -g npm@10`（v11 版本偶爾有 reify 錯誤；之後可還原）。
   - 完整日誌：檢查 `/root/.npm/_logs/2025-10-27T16_10_10_534Z-debug-0.log` 以獲取更多線索。

這應該能解決問題 — 在 Linux 上，npm 全域套件在重新命名時可能較不穩定。如果你提供執行的確切指令或更多日誌內容，我可以進一步完善建議。