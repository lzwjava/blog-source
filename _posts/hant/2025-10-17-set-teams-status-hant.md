---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 使用 PowerShell 設定 Teams 狀態
translated: true
type: note
---

不，Microsoft Teams 並沒有官方的獨立命令列工具（例如簡單的 `teams --status offline` 可執行檔）來設定您的線上狀態。內建的斜線指令（例如 `/away` 或 `/offline`）僅在 Teams 應用程式介面內有效，無法在終端機中使用。

不過，您可以透過 PowerShell 和 Microsoft Graph API 來實現此功能。這需要安裝 Microsoft Graph PowerShell SDK、使用您的 Microsoft 帳戶進行驗證，並執行 cmdlet 來更新您的狀態。以下是逐步指南：

### 必要條件
1. 安裝 PowerShell（如果尚未安裝；Windows 10+ 已內建）。
2. 以管理員身份開啟 PowerShell 並安裝模組：
   ```
   Install-Module Microsoft.Graph -Scope CurrentUser
   ```

### 設定您的狀態
1. 連線至 Microsoft Graph（這將透過瀏覽器提示驗證）：
   ```
   Connect-MgGraph -Scopes "Presence.ReadWrite"
   ```

2. 執行 cmdlet 來設定狀態。將 `YourUserId` 替換為您的 Microsoft Entra ID（Azure AD）使用者 ID（您可以透過 `Get-MgUser -UserId your.email@domain.com` 取得）。常見的狀態值包括：
   - `Available`
   - `Away`
   - `Busy`
   - `DoNotDisturb`
   - `Offline`（對他人顯示為離線）

   設定為離線的範例：
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Offline"
   ```

   設定為離開的範例：
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Away"
   ```

3. 完成後斷開連線：
   ```
   Disconnect-MgGraph
   ```

### 注意事項
- 這會立即更新您的狀態，但可能會根據您的活動重設（例如閒置時間觸發「離開」狀態）。
- 若要實現自動化（例如在排程上切換狀態的腳本），請將上述指令包裝在 `.ps1` 檔案中，並透過工作排程器執行。
- 如果您也想設定自訂狀態訊息（例如「外出用餐」），請使用 `Set-MgUserPresenceStatusMessage`。
- 這適用於個人使用，但需要適當的權限；管理員可能需要啟用 Graph API 存取。

若要在閒置期間保持「可用」狀態（常見的解決方法），存在模擬活動的腳本（例如每隔幾分鐘切換 Num Lock），但它們並非真正的狀態設定工具。

參考資料：  
[使用 MS Graph PowerShell 管理 Microsoft Teams 中的狀態](https://m365scripts.com/microsoft-teams/manage-presence-status-in-microsoft-teams-using-ms-graph-powershell/)  
[Set-MgUserPresence PowerShell Cmdlet 文件](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users.actions/set-mguserpresence)  
[關於透過 API/命令列設定 Teams 狀態的 Reddit 討論串](https://www.reddit.com/r/teams/comments/1h5wee9/teams_status_with_api_command_line/)