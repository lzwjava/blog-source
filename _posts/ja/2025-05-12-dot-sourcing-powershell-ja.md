---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: ドットソーシングPowerShellスクリプト
translated: true
type: note
---

### .ps1 ファイルでの PowerShell 関数のドットソーシング

ドットソーシング（`.` 演算子を使用）は、PowerShell スクリプト（.ps1 ファイル）を現在のセッションのメモリに読み込み、その関数と変数をスクリプトのトップレベルコードを実行せずに利用できるようにします。モジュールや再利用可能なコードをインポートする際に便利です。

#### 基本構文
PowerShell セッションで次のコマンドを実行します：
```
. Path\To\YourScript.ps1
```
- `Path\To\YourScript.ps1` を実際のファイルパスに置き換えてください（信頼性のために絶対パスを使用することを推奨）。
- 例：`. C:\Scripts\MyFunctions.ps1` – これにより、そのファイルから関数がセッションに読み込まれます。

#### 仕組み
- スクリプト内で定義された関数が、現在のセッションで呼び出し可能になります。
- 変数もインポートされますが、ローカルスコープでない場合に限ります。
- 本番スクリプトではドットソーシングを避け、より良い整理のためにモジュールを使用してください。
- ヒント：パスにスペースが含まれる場合は、引用符で囲んでください：`. "C:\My Scripts\Functions.ps1"`

よくある問題：スクリプトに構文エラーがある場合、ドットソーシングはエラーで失敗します。コマンドプロンプトから `PowerShell -Command ". .\YourScript.ps1"` を実行してテストしてください。

### PowerShell 実行ポリシーの使用

実行ポリシーは、PowerShell が実行できるスクリプトを制限するセキュリティ設定で、悪意のあるコードの実行を防ぎます。これらはスコープごと（例：マシン全体、ユーザー固有）に設定されます。

#### 現在のポリシーの確認
PowerShell で次を実行：
```
Get-ExecutionPolicy
```
- 出力例：`Restricted`（すべてのスクリプトをブロック）、`AllSigned`（署名済みスクリプトのみ）、`RemoteSigned`（リモートスクリプトは署名済み、ローカルは許可）、または `Unrestricted`。

#### ポリシーの設定または変更
`Set-ExecutionPolicy` を使用（マシンレベルの変更には管理者権限が必要）：
- ローカルで作成されたスクリプトを許可する例：`Set-ExecutionPolicy RemoteSigned`
- プロンプトなしで強制：`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force`
- スコープ指定：`Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser`（自分のユーザーアカウントにのみ影響）。

#### 一般的なポリシー
- `Restricted`：デフォルト。すべてのスクリプトの実行をブロック。
- `AllSigned`：デジタル署名を要求（安全だが不便）。
- `RemoteSigned`：セキュリティと利便性のバランス—ローカルスクリプトは許可、リモートは署名済みのみ。
- `Unrestricted`：すべてのスクリプトを実行（危険。注意して使用）。
- `Bypass`：完全な無制限。自動化用。

ヒント：ポリシーはコンソールセッションに適用されますが、設定されない限り ISE や VS Code には適用されません。`Write-Host "Hello"` のようなサンプルスクリプトを実行して変更をテストしてください。詳細は、Microsoft のドキュメント `help about_Execution_Policies` を参照してください。企業環境では、グループポリシーがローカル設定を上書きする可能性があります。