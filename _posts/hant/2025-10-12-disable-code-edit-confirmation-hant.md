---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 停用 Claude 代碼編輯確認彈出視窗
translated: true
type: note
---

要停用 Claude Code 中的編輯確認彈出視窗（讓它直接對檔案進行編輯，例如 `sync_githook.py` 而不需詢問），您需要在 `settings.json` 檔案中配置權限設定。這就是您所指的「Claude Code JSON」—它是 Claude Code 用於用戶級配置的主要設定檔案。

### 設定步驟

1. **尋找或建立檔案**：
   - 檔案位於 `~/.claude/settings.json`（在 macOS/Linux 上）或 `%USERPROFILE%\.claude\settings.json`（在 Windows 上）。`.claude` 資料夾是隱藏的，請使用終端機或檔案總管前往該位置。
   - 如果檔案或資料夾不存在，請建立它們。您可以透過在 Claude Code 的互動式 REPL 中執行 `/config` 指令來完成此操作（它會引導您開啟設定介面）。

2. **編輯 JSON**：
   - 在任何文字編輯器（例如 VS Code）中開啟 `settings.json`。
   - 新增或更新 `permissions` 部分以自動核准編輯。以下是一個簡單的配置，用於停用所有編輯操作的提示：

     ```json:disable-run
     {
       "permissions": {
         "defaultMode": "acceptEdits",
         "allow": [
           "Edit(*)",
           "Write(*)",
           "MultiEdit(*)"
         ],
         "ask": []
       }
     }
     ```

     - **此配置的作用**：
       - `"defaultMode": "acceptEdits"`：將全域預設設定為無需提示直接接受編輯。
       - `"allow"`：預先核准特定工具，如 `Edit`（用於單一檔案編輯）、`Write`（用於寫入內容）和 `MultiEdit`（用於批次變更）對任何檔案（`*` 萬用字元）的操作。
       - `"ask": []`：確保除非在其他地方明確拒絕，否則不會有任何操作觸發提示。
     - 儲存檔案。變更將在您下一次 Claude Code 工作階段中立即生效。

3. **測試**：
   - 重新啟動 Claude Code 或重新載入工作階段。
   - 要求它編輯一個檔案（例如「編輯 sync_githook.py 以新增註解」）。它應該會直接套用變更而不顯示彈出視窗。
   - 如果您需要專案特定的設定（例如僅針對此儲存庫），請在您的專案根目錄中建立 `.claude/settings.json`。

4. **可選調整**：
   - 如需更精細的控制（例如僅允許在特定目錄中編輯）：將 `"Edit(*)"` 更改為 `"Edit(./src/**)"`。
   - 如果提示仍然出現，請在 REPL 中執行 `/allowed-tools` 以檢查當前規則，或使用 `/config` 透過 UI 進行調整。
   - 為了安全起見，避免使用過於寬泛的 `allow` 規則—從簡單的設定開始，再逐步擴展。

這應該能讓您的工作流程更快且不受干擾。如果您處於企業設定中，請與管理員確認，因為受管理的政策可能會覆蓋用戶設定。

[Claude Code 設定文件](https://docs.claude.com/en/docs/claude-code/settings)  
[停用 Claude Code 權限提示指南](https://www.arsturn.com/blog/how-to-disable-claude-code-permission-prompts)