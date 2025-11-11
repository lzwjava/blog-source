---
audio: false
generated: true
lang: ja
layout: post
title: PowerShellコマンドガイド
translated: true
type: note
---

## PowerShell の概要
PowerShell は、Microsoft が開発したタスク自動化および構成管理フレームワークで、コマンドライン シェルとスクリプト言語で構成されています。.NET Framework（および新しいバージョンでは .NET Core）上に構築されており、管理者が Windows、Linux、macOS システムにわたって複雑なタスクを実行できるようにします。

PowerShell コマンドは、**cmdlet**（「コマンドレット」と発音）として知られ、`動詞-名詞` の命名規則に従います（例: `Get-Process`, `Set-Item`）。このガイドでは、機能別に分類した必須のコマンドレットと、その使用法を示す例を紹介します。

---

## 1. PowerShell の核心概念
コマンドの詳細に入る前に、重要な概念を理解することが不可欠です:
- **Cmdlet**: 特定の機能を実行する軽量なコマンド。
- **パイプライン**: `|` 演算子を使用して、あるコマンドレットの出力を別のコマンドレットへの入力として渡すことを可能にします。
- **モジュール**: PowerShell の機能を拡張するコマンドレット、スクリプト、関数のコレクション。
- **プロバイダー**: データストア（ファイルシステム、レジストリなど）にドライブであるかのようにアクセスするためのインターフェース。
- **オブジェクト**: PowerShell はプレーンテキストではなくオブジェクトを扱うため、構造化されたデータ操作が可能になります。

---

## 2. カテゴリ別 必須コマンドレット

### 2.1 システム情報
これらのコマンドレットは、システム、プロセス、サービスに関する情報を取得します。

| コマンドレット | 説明 | 例 |
|--------|-------------|---------|
| `Get-ComputerInfo` | システムのハードウェアとソフトウェアの詳細を取得します。 | `Get-ComputerInfo | Select-Object WindowsProductName, OsVersion` |
| `Get-Process` | 実行中のプロセスを一覧表示します。 | `Get-Process | Where-Object {$_.CPU -gt 1000}` |
| `Get-Service` | システム上のサービスを表示します。 | `Get-Service | Where-Object {$_.Status -eq "Running"}` |
| `Get-HotFix` | インストール済みの Windows 更新プログラムを一覧表示します。 | `Get-HotFix | Sort-Object InstalledOn -Descending` |

**例**: CPU 使用率でソートされた、すべての実行中プロセスを一覧表示。
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object Name, CPU, Id -First 5
```

### 2.2 ファイルとディレクトリの管理
PowerShell はファイルシステムをプロバイダーとして扱い、ドライブと同様のナビゲーションを可能にします。

| コマンドレット | 説明 | 例 |
|--------|-------------|---------|
| `Get-Item` | ファイルまたはディレクトリを取得します。 | `Get-Item C:\Users\*.txt` |
| `Set-Item` | アイテムのプロパティ（ファイル属性など）を変更します。 | `Set-Item -Path C:\test.txt -Value "New content"` |
| `New-Item` | 新しいファイルまたはディレクトリを作成します。 | `New-Item -Path C:\Docs -Name Report.txt -ItemType File` |
| `Remove-Item` | ファイルまたはディレクトリを削除します。 | `Remove-Item C:\Docs\OldFile.txt` |
| `Copy-Item` | ファイルまたはディレクトリをコピーします。 | `Copy-Item C:\Docs\Report.txt D:\Backup` |
| `Move-Item` | ファイルまたはディレクトリを移動します。 | `Move-Item C:\Docs\Report.txt C:\Archive` |

**例**: ディレクトリとファイルを作成し、別の場所にコピーします。
```powershell
New-Item -Path C:\Temp -Name MyFolder -ItemType Directory
New-Item -Path C:\Temp\MyFolder -Name Test.txt -ItemType File
Copy-Item C:\Temp\MyFolder\Test.txt C:\Backup
```

### 2.3 システム管理
システム設定、サービス、ユーザーを管理するためのコマンドレット。

| コマンドレット | 説明 | 例 |
|--------|-------------|---------|
| `Start-Service` | サービスを開始します。 | `Start-Service -Name "wuauserv"` |
| `Stop-Service` | サービスを停止します。 | `Stop-Service -Name "wuauserv"` |
| `Restart-Computer` | システムを再起動します。 | `Restart-Computer -Force` |
| `Get-EventLog` | イベントログのエントリを取得します。 | `Get-EventLog -LogName System -Newest 10` |
| `Set-ExecutionPolicy` | スクリプト実行ポリシーを設定します。 | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |

**例**: Windows Update サービスの状態をチェックし、停止している場合は開始します。
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Stopped") {
    Start-Service -Name "wuauserv"
}
```

### 2.4 ネットワーク管理
ネットワーク構成と診断のためのコマンドレット。

| コマンドレット | 説明 | 例 |
|--------|-------------|---------|
| `Test-Connection` | リモートホストに ping を実行します。 | `Test-Connection google.com` |
| `Get-NetAdapter` | ネットワークアダプターを一覧表示します。 | `Get-NetAdapter | Select-Object Name, Status` |
| `Get-NetIPAddress` | IP アドレス構成を取得します。 | `Get-NetIPAddress -AddressFamily IPv4` |
| `Resolve-DnsName` | DNS 名を解決します。 | `Resolve-DnsName www.google.com` |

**例**: サーバーに ping を実行し、その DNS 解決をチェックします。
```powershell
Test-Connection -ComputerName google.com -Count 2
Resolve-DnsName google.com
```

### 2.5 ユーザーとグループ管理
ローカルユーザーとグループを管理するためのコマンドレット。

| コマンドレット | 説明 | 例 |
|--------|-------------|---------|
| `New-LocalUser` | ローカルユーザーアカウントを作成します。 | `New-LocalUser -Name "TestUser" -Password (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force)` |
| `Remove-LocalUser` | ローカルユーザーアカウントを削除します。 | `Remove-LocalUser -Name "TestUser"` |
| `Get-LocalGroup` | ローカルグループを一覧表示します。 | `Get-LocalGroup | Select-Object Name` |
| `Add-LocalGroupMember` | ユーザーをローカルグループに追加します。 | `Add-LocalGroupMember -Group "Administrators" -Member "TestUser"` |

**例**: 新しいローカルユーザーを作成し、Administrators グループに追加します。
```powershell
$password = ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force
New-LocalUser -Name "TestUser" -Password $password -FullName "Test User" -Description "Test account"
Add-LocalGroupMember -Group "Administrators" -Member "TestUser"
```

### 2.6 スクリプトと自動化
PowerShell は自動化のためのスクリプト作成に優れています。

| コマンドレット | 説明 | 例 |
|--------|-------------|---------|
| `Write-Output` | データをパイプラインに出力します。 | `Write-Output "Hello, World!"` |
| `ForEach-Object` | パイプライン内のアイテムをループ処理します。 | `Get-Process | ForEach-Object { $_.Name }` |
| `Where-Object` | 条件に基づいてオブジェクトをフィルタリングします。 | `Get-Service | Where-Object { $_.Status -eq "Running" }` |
| `Invoke-Command` | ローカルまたはリモートコンピューターでコマンドを実行します。 | `Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Process }` |
| `New-ScheduledTask` | スケジュールされたタスクを作成します。 | `New-ScheduledTask -Action (New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\script.ps1") -Trigger (New-ScheduledTaskTrigger -Daily -At "3AM")` |

**例**: 実行中のプロセスをファイルに記録するスクリプトを作成します。
```powershell
$logPath = "C:\Logs\ProcessLog.txt"
Get-Process | Select-Object Name, CPU, StartTime | Export-Csv -Path $logPath -NoTypeInformation
```

### 2.7 モジュール管理
モジュールは PowerShell の機能を拡張します。

| コマンドレット | 説明 | 例 |
|--------|-------------|---------|
| `Get-Module` | 利用可能なモジュールまたはインポートされたモジュールを一覧表示します。 | `Get-Module -ListAvailable` |
| `Import-Module` | モジュールをインポートします。 | `Import-Module ActiveDirectory` |
| `Install-Module` | リポジトリからモジュールをインストールします。 | `Install-Module -Name PSWindowsUpdate -Force` |
| `Find-Module` | リポジトリ内のモジュールを検索します。 | `Find-Module -Name *Azure*` |

**例**: Windows 更新プログラムを管理するために PSWindowsUpdate モジュールをインストールしてインポートします。
```powershell
Install-Module -Name PSWindowsUpdate -Force
Import-Module PSWindowsUpdate
Get-WUList
```

---

## 3. パイプラインの操作
パイプライン (`|`) を使用すると、コマンドレットを連結してデータを順次処理できます。例:
```powershell
Get-Process | Where-Object { $_.WorkingSet64 -gt 100MB } | Sort-Object WorkingSet64 -Descending | Select-Object Name, WorkingSet64 -First 5
```
このコマンドは:
1. すべてのプロセスを取得します。
2. 100MB を超えるメモリを使用しているプロセスをフィルタリングします。
3. メモリ使用量で降順にソートします。
4. 上位 5 つのプロセスを選択し、その名前とメモリ使用量を表示します。

---

## 4. 変数、ループ、条件
PowerShell は自動化のためのスクリプト構文をサポートしています。

### 変数
```powershell
$path = "C:\Logs"
$services = Get-Service
Write-Output "Log path is $path"
```

### ループ
- **ForEach-Object**:
```powershell
Get-Service | ForEach-Object { Write-Output $_.Name }
```
- **For ループ**:
```powershell
for ($i = 1; $i -le 5; $i++) { Write-Output "Iteration $i" }
```

### 条件
```powershell
$service = Get-Service -Name "wuauserv"
if ($service.Status -eq "Running") {
    Write-Output "Windows Update is running."
} else {
    Write-Output "Windows Update is stopped."
}
```

---

## 5. エラー処理
堅牢なスクリプトのために `Try`、`Catch`、`Finally` を使用します。
```powershell
Try {
    Get-Item -Path C:\NonExistentFile.txt -ErrorAction Stop
}
Catch {
    Write-Output "Error: $($_.Exception.Message)"
}
Finally {
    Write-Output "Operation completed."
}
```

---

## 6. リモート管理
PowerShell は `Invoke-Command` と `Enter-PSSession` を使用したリモート管理をサポートします。

**例**: リモートコンピューターでコマンドを実行します。
```powershell
Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Service | Where-Object { $_.Status -eq "Running" } }
```

**例**: 対話型のリモートセッションを開始します。
```powershell
Enter-PSSession -ComputerName Server01
```

---

## 7. 実用的なスクリプト例
以下は、ディスク容量を監視し、使用率が 80% を超えた場合に警告するサンプルスクリプトです。

```powershell
$disks = Get-Disk
$threshold = 80

foreach ($disk in $disks) {
    $freeSpacePercent = ($disk.FreeSpace / $disk.Size) * 100
    if ($freeSpacePercent -lt (100 - $threshold)) {
        Write-Output "Warning: Disk $($disk.Number) is at $("{0:N2}" -f (100 - $freeSpacePercent))% capacity."
    }
}
```

---

## 8. 効果的な PowerShell 使用法のヒント
- **速度向上のためのエイリアスの使用**: `dir` (`Get-ChildItem`)、`ls` (`Get-ChildItem`)、`gci` (`Get-ChildItem`) などの一般的なエイリアスは、対話型セッションで時間を節約します。
- **Get-Help**: 詳細なドキュメントには `Get-Help <コマンドレット>` を使用します（例: `Get-Help Get-Process -Full`）。
- **Update-Help**: `Update-Help` でヘルプファイルを最新の状態に保ちます。
- **プロファイル**: `$PROFILE` を編集して PowerShell 環境をカスタマイズします（例: `notepad $PROFILE`）。
- **タブ補完**: `Tab` キーを押して、コマンドレット、パラメーター、パスを自動補完します。
- **詳細出力の使用**: コマンドレットに `-Verbose` を追加して、詳細な実行情報を表示します。

---

## 9. 追加リソース
- **公式ドキュメント**: [Microsoft PowerShell Docs](https://docs.microsoft.com/en-us/powershell/)
- **PowerShell Gallery**: モジュール用の [PowerShell Gallery](https://www.powershellgallery.com/)。
- **コミュニティ**: X や Stack Overflow などのフォーラムで、リアルタイムのヒントやスクリプトを確認してください。
- **学習**: *PowerShell in Depth* や *Learn PowerShell in a Month of Lunches* などの書籍。

---

PowerShell は、Microsoft が開発した強力なスクリプト言語およびコマンドライン シェルです。タスクの自動化と構成管理に広く使用されています。以下は `Get-NetTCPConnection` 以外の一般的に使用される PowerShell コマンドの一部です:

1.  **Get-Process**: ローカルコンピューターまたはリモートコンピューターで実行されているプロセスに関する情報を取得します。
2.  **Get-Service**: ローカルコンピューターまたはリモートコンピューターのサービスを取得します。
3.  **Get-EventLog**: アプリケーション、セキュリティ、システムログなどのイベントログからイベントを取得します。
4.  **Get-ChildItem**: 指定された1つ以上の場所にあるアイテムと子アイテムを取得します（コマンドプロンプトの `dir` に類似）。
5.  **Get-Content**: 指定された場所にあるアイテムの内容を取得します（コマンドプロンプトの `type` に類似）。
6.  **Set-ExecutionPolicy**: PowerShell 実行ポリシーのユーザー設定を変更します。
7.  **Invoke-Command**: ローカルおよびリモートコンピューターでコマンドを実行します。
8.  **New-Item**: ファイルやディレクトリなどの新しいアイテムを作成します。
9.  **Remove-Item**: 指定されたアイテムを削除します。
10. **Copy-Item**: アイテムをある場所から別の場所にコピーします。
11. **Move-Item**: アイテムをある場所から別の場所に移動します。
12. **Rename-Item**: PowerShell プロバイダーの名前空間内のアイテムの名前を変更します。
13. **Get-Help**: PowerShell コマンドと概念に関する情報を表示します。
14. **Select-Object**: オブジェクトまたはオブジェクトのセットの指定されたプロパティを選択します。
15. **Where-Object**: プロパティ値に基づいてコレクションからオブジェクトを選択します。
16. **Sort-Object**: プロパティ値でオブジェクトをソートします。
17. **Export-Csv**: オブジェクトを一連の CSV 文字列に変換し、その文字列をファイルに保存します。
18. **Import-Csv**: CSV ファイルをインポートし、オブジェクトに変換します。
19. **Start-Process**: ローカルコンピューターで1つ以上のプロセスを開始します。
20. **Stop-Process**: 1つ以上の実行中のプロセスを停止します。

これらのコマンドは、PowerShell でできることのほんの一例です。この言語は非常に拡張性が高く、複雑なタスクを自動化するためのカスタム コマンドレットやスクリプトを作成できます。