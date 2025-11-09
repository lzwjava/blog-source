---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: PowerShell による Teams ステータスの設定
translated: true
type: note
---

いいえ、Microsoft Teamsには、プレゼンスステータスを設定するための公式のスタンドアロンなコマンドラインユーティリティ（シンプルな `teams --status offline` のような実行ファイル）はありません。組み込みのスラッシュコマンド（例: `/away` や `/offline`）は、ターミナルからではなく、Teamsアプリのインターフェース内でのみ機能します。

しかし、PowerShellとMicrosoft Graph APIを使用して、コマンドラインからこれを実現することができます。これには、Microsoft Graph PowerShell SDKのインストール、Microsoftアカウントでの認証、およびプレゼンスを更新するためのコマンドレットの実行が必要です。以下にステップバイステップのガイドを示します：

### 前提条件
1. PowerShellをインストール（まだ利用できない場合。Windows 10以降には組み込まれています）。
2. 管理者としてPowerShellを開き、モジュールをインストール：
   ```
   Install-Module Microsoft.Graph -Scope CurrentUser
   ```

### ステータスの設定
1. Microsoft Graphに接続（ブラウザー経由の認証が求められます）：
   ```
   Connect-MgGraph -Scopes "Presence.ReadWrite"
   ```

2. ステータスを設定するコマンドレットを実行します。`YourUserId` は、あなたのMicrosoft Entra ID（Azure AD）ユーザーIDに置き換えてください（`Get-MgUser -UserId your.email@domain.com` で取得可能）。一般的なステータス値は次のとおりです：
   - `Available`
   - `Away`
   - `Busy`
   - `DoNotDisturb`
   - `Offline` (他のユーザーにはオフラインとして表示されます)

   オフラインに設定する例：
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Offline"
   ```

   離席中に設定する例：
   ```
   Set-MgUserPresence -UserId "YourUserId" -Presence "Away"
   ```

3. 完了したら切断します：
   ```
   Disconnect-MgGraph
   ```

### 注意点
- これはあなたのプレゼンスを即座に更新しますが、あなたのアクティビティ（例：アイドル時間が「離席中」をトリガーする）に基づいてリセットされる可能性があります。
- 自動化（例：スケジュールに基づいてステータスを切り替えるスクリプト）の場合、上記を `.ps1` ファイルにラップし、タスクスケジューラ経由で実行します。
- カスタムステータスメッセージ（例：「ランチ中」）も設定したい場合は、`Set-MgUserPresenceStatusMessage` を使用します。
- これは個人利用で機能しますが、適切な権限が必要です。管理者はGraph APIアクセスを有効にする必要があるかもしれません。

アイドル期間中にステータスを「利用可能」に保つための一般的な回避策として、アクティビティをシミュレートするスクリプト（例：数分ごとにNum Lockを切り替える）が存在しますが、これらは真のステータス設定ツールではありません。

参考文献：  
[Manage Presence Status in Microsoft Teams Using MS Graph PowerShell](https://m365scripts.com/microsoft-teams/manage-presence-status-in-microsoft-teams-using-ms-graph-powershell/)  
[Set-MgUserPresence PowerShell Cmdlet Docs](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users.actions/set-mguserpresence)  
[Reddit Thread on Teams Status via API/CLI](https://www.reddit.com/r/teams/comments/1h5wee9/teams_status_with_api_command_line/)