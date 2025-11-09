---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Azure CLI クイックスタートガイド
translated: true
type: note
---

Azure CLI（コマンドラインインターフェース）は、コマンドラインからAzureリソースを管理するためのクロスプラットフォームツールセットです。Webポータルが不要で、タスクの自動化、デプロイのスクリプト化、Azureサービスとの連携に最適です。Windows、macOS、LinuxでBash、PowerShell、コマンドプロンプトをサポートしています。

## インストール

1. **前提条件**: Python 3.8以降がインストールされていることを確認してください（`python --version`で確認）。

2. **パッケージマネージャーを使用したインストール**（推奨）:
   - **Windows**: Winget（`winget install Microsoft.AzureCLI`）またはChocolatey（`choco install azure-cli`）を使用。
   - **macOS**: Homebrew（`brew install azure-cli`）を使用。
   - **Linux（Ubuntu/Debian）**: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`を実行。
   - **その他のLinux**: RPMまたは公式サイトからの手動ダウンロードを使用。

3. **インストールの確認**: ターミナルを開き、`az --version`を実行。CLIのバージョン（例：2025年後半時点で2.64.0）が表示されます。

詳細なプラットフォーム別の手順については、公式のインストールドキュメントを参照してください。

## 認証

Azure CLIを使用する前に、Azureアカウントにサインインします：

1. **対話型ログイン**: `az login`を実行。Microsoft Entra ID認証のためにブラウザが開きます。プロンプトに従ってサインイン。

2. **サービスプリンシパル（自動化用）**: `az ad sp create-for-rbac --name "MyApp" --role contributor --scopes /subscriptions/{subscription-id}`でサービスプリンシパルを作成。その後、`az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>`を使用。

3. **ログインの確認**: `az account show`を使用してアクティブなサブスクリプションを確認。

4. **ログアウト**: `az logout`。

多要素認証（MFA）がサポートされており、`az account set --subscription <id>`で複数のサブスクリプションを管理できます。

## 基本コマンド

Azure CLIは、`az`コマンドの後にグループ（例：`vm`、`storage`）とサブコマンドを使用します。概要には`az --help`を、詳細には`az <group> --help`を使用。

### 一般的なグローバルオプション
- `--help`または`-h`: ヘルプを表示。
- `--output table/json/yaml`: 出力をフォーマット（デフォルト：table）。
- `--query`: JSON出力をフィルタリングするJMESPathクエリ（例：`--query "[].name"`）。

### 主な例
- **サブスクリプションの一覧表示**: `az account list --output table`
- **リソースグループの取得**: `az group list --output table`
- **リソースグループの作成**: `az group create --name "MyResourceGroup" --location "eastus"`

## 仮想マシン（VM）の管理
Azure CLIはVMのライフサイクル管理に優れています。

1. **VMの作成**:
   ```
   az vm create \
     --resource-group "MyResourceGroup" \
     --name "MyVM" \
     --image Ubuntu2204 \
     --admin-username azureuser \
     --admin-password MyP@ssw0rd123! \
     --location "eastus"
   ```

2. **VMの一覧表示**: `az vm list --output table`

3. **VMの起動/停止**: `az vm start --name "MyVM" --resource-group "MyResourceGroup"` または `az vm stop --name "MyVM" --resource-group "MyResourceGroup"`

4. **VMへのSSH接続**: `az vm ssh "MyVM" --resource-group "MyResourceGroup"`

5. **VMの削除**: `az vm delete --name "MyVM" --resource-group "MyResourceGroup" --yes`

## ストレージアカウントの管理
1. **ストレージアカウントの作成**:
   ```
   az storage account create \
     --name mystorageaccount \
     --resource-group "MyResourceGroup" \
     --location "eastus" \
     --sku Standard_LRS
   ```

2. **Blobのアップロード**: まず、`az storage account keys list --account-name mystorageaccount --resource-group "MyResourceGroup" --query "[0].value -o tsv"`でキーを取得。その後：`az storage blob upload --account-name mystorageaccount --container-name mycontainer --name myfile.txt --file ./myfile.txt --auth-mode key`

## その他の一般的なシナリオ
- **ARMテンプレートのデプロイ**: `az deployment group create --resource-group "MyResourceGroup" --template-file template.json`
- **リソースのクエリ**: `az resource list --resource-group "MyResourceGroup" --output table`
- **CLIの更新**: `az upgrade`
- **拡張機能**: 追加コマンドのために`az extension add --name azure-devops`などの拡張機能をインストール。

スクリプトでは、Bash/PowerShellのループと組み合わせるか、GitHub ActionsなどのCI/CDパイプラインでAzure CLIを使用します。

## ヒントとベストプラクティス
- プレビューには`--dry-run`を使用（サポートされている場合）。
- オートコンプリートを有効化: Bashでは`az completion`を実行。
- エラー処理: 終了コード（成功は0）を確認し、トラブルシューティングには`--debug`を使用。
- セキュリティ: 資格情報のハードコーディングを避け、環境変数またはAzure Key Vaultを使用。

## 参考資料
[Azure CLIのインストール](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)  
[Azure CLIリファレンス](https://learn.microsoft.com/en-us/cli/azure/)  
[Azure CLIクイックスタート](https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli)