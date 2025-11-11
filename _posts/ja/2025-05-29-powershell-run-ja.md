---
audio: false
generated: true
lang: ja
layout: post
title: 'PowerShell: 現在のターミナルでコマンドを実行'
translated: true
type: note
---

現在のPowerShellターミナルで新しいコマンドプロンプトを開かずに、`mvn`やWebSphereサーバーコマンドを直接実行するには、call演算子（`&`）を使用するか、コマンドを直接呼び出します。この方法により、コマンドが既存のPowerShellセッション内で実行され、出力とエラーが同じターミナルに表示されます。

以下に方法を示します：

1. **コマンドを直接実行**：
   コマンド（例：`mvn`）がシステムのPATHに含まれているか、現在のディレクトリでアクセス可能な場合は、ターミナルで行うようにコマンドを入力します：

   ```powershell
   mvn clean install
   ```

   これにより、`mvn`がPowerShellセッション内で直接実行され、出力は現在のターミナルに表示されます。

2. **Call演算子（`&`）を使用**：
   実行可能ファイルへのパスを指定する必要がある場合や、コマンドが変数に格納されている場合は、call演算子を使用します：

   ```powershell
   & "C:\path\to\maven\bin\mvn.cmd" clean install
   ```

   WebSphereサーバーコマンド（例：`wsadmin`や`startServer`）を実行する場合は、次のように行います：

   ```powershell
   & "C:\path\to\WebSphere\AppServer\bin\startServer.bat" server1
   ```

   `&`演算子により、コマンドが現在のPowerShellセッション内で実行されます。

3. **スペースや変数を含むコマンドの処理**：
   コマンドのパスにスペースが含まれている場合や、変数に格納されている場合は、`&`と引用符で囲んだパスを使用します：

   ```powershell
   $mvnPath = "C:\Program Files\Apache Maven\bin\mvn.cmd"
   & $mvnPath clean install
   ```

4. **環境変数の設定（必要な場合）**：
   `mvn`やWebSphereスクリプトなどの一部のコマンドは、環境変数（例：`JAVA_HOME`や`WAS_HOME`）を必要とする場合があります。コマンド実行前にスクリプト内で設定します：

   ```powershell
   $env:JAVA_HOME = "C:\path\to\jdk"
   $env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
   mvn --version
   ```

   WebSphereの場合：

   ```powershell
   $env:WAS_HOME = "C:\path\to\WebSphere\AppServer"
   & "$env:WAS_HOME\bin\startServer.bat" server1
   ```

5. **出力の取得やエラーの処理**：
   コマンドの出力を取得したり、エラーを処理したりするには、PowerShellの標準的なメカニズムを使用します：

   ```powershell
   try {
       $output = & mvn clean install 2>&1
       Write-Output $output
   } catch {
       Write-Error "Mavenの実行に失敗しました: $_"
   }
   ```

6. **`Start-Process`の回避**：
   `Start-Process`は新しいプロセス（多くの場合、別のウィンドウ）を起動しますが、上記の方法では実行が現在のセッション内に留まります。以下のような`Start-Process`の使用は避けてください：

   ```powershell
   # これにより新しいコマンドプロンプトウィンドウが開きます
   Start-Process -FilePath "mvn" -ArgumentList "clean install"
   ```

   代わりに、直接実行または`&`を使用してください。

### スクリプト例
以下は、現在のターミナルで`mvn`とWebSphereコマンドを実行するサンプルPowerShellスクリプトです：

```powershell
# 必要に応じて環境変数を設定
$env:JAVA_HOME = "C:\Program Files\Java\jdk-11"
$env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH
$env:WAS_HOME = "C:\IBM\WebSphere\AppServer"

# Mavenコマンドを実行
Write-Output "Mavenを実行中..."
& mvn clean install

# WebSphereサーバーコマンドを実行
Write-Output "WebSphereサーバーを起動中..."
& "$env:WAS_HOME\bin\startServer.bat" server1
```

### 注意点
- コマンドラインツール（`mvn`、`startServer.bat`など）がPATHに含まれているか、実行可能ファイルへのフルパスを指定してください。
- コマンドが特定の作業ディレクトリを必要とする場合は、実行前に`Set-Location`（または`cd`）を使用してください：

   ```powershell
   Set-Location "C:\path\to\project"
   & mvn clean install
   ```

- `.bat`や`.cmd`ファイルに依存するコマンド（WebSphereで一般的）の場合、`&`演算子は適切に機能しますが、スクリプトがPowerShellで実行されることを確認してください（`cmd.exe`ではありません）。
- 環境変数やPATHに問題がある場合は、`Get-ChildItem Env:`で確認してください。

この方法により、すべてが現在のPowerShellターミナル内で処理され、新しいウィンドウが開かず、クリーンなワークフローが維持されます。特定のコマンドや設定に問題がある場合は、詳細を共有していただければ、さらに具体的な解決策を提案できます。