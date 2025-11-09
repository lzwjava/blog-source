---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Azure Application Insights セットアップガイド
translated: true
type: note
---

## Azure Application Insights とは

Azure Application Insights は、Azure Monitor のアプリケーション パフォーマンス管理 (APM) サービスであり、ライブ Web アプリケーションの監視を支援します。要求、依存関係、トレース、メトリック、ログなどのテレメトリ データを通じて、問題の検出、診断、ユーザー行動の理解のためのツールを提供します。現在は OpenTelemetry によって駆動され、より広範な互換性を実現しています。

## 前提条件
- アクティブな Azure サブスクリプション。
- Azure でリソースを作成する権限 (例: 所有者または共同作成者ロール)。
- アプリケーション コード (.NET、Java、Node.js、Python などをサポート)。

## ステップ 1: Application Insights リソースの作成
1. [Azure portal](https://portal.azure.com) にサインインします。
2. 左上のメニューで **リソースの作成** をクリックします。
3. 「Application Insights」を検索し、結果から **監視 + 管理** の下にあるそれを選択します。
4. 詳細を入力します：
   - **サブスクリプション**: ご利用の Azure サブスクリプションを選択します。
   - **リソース グループ**: 既存のものを選択するか、新しいものを作成します。
   - **名前**: リソースに一意の名前を付けます。
   - **リージョン**: ユーザーやアプリに近いリージョンを選択します。
   - **ワークスペース**: オプションで既存の Log Analytics ワークスペースにリンクします。それ以外の場合は、新しいものが自動的に作成されます。
5. 確認して **作成** をクリックします。デプロイには数分かかります。
6. 作成されたら、リソースの **概要** ページに移動し、**接続文字列** をコピーします (上にホバーしてコピー アイコンをクリック)。これは、アプリがテレメトリ データを送信する場所を識別します。

**ヒント**: 開発、テスト、本番環境では、データが混在しないように別々のリソースを使用してください。

## ステップ 2: アプリケーションのインストルメンテーション
OpenTelemetry サポートを追加して、テレメトリ (要求、例外、メトリックなど) を自動的に収集します。接続文字列は、`APPLICATIONINSIGHTS_CONNECTION_STRING` という名前の環境変数経由で設定することを推奨します (本番環境向け)。

### .NET (ASP.NET Core) の場合
1. NuGet パッケージをインストールします：
   ```
   dotnet add package Azure.Monitor.OpenTelemetry.AspNetCore
   ```
2. `Program.cs` で：
   ```csharp
   using Azure.Monitor.OpenTelemetry.AspNetCore;

   var builder = WebApplication.CreateBuilder(args);
   builder.Services.AddOpenTelemetry().UseAzureMonitor();
   var app = builder.Build();
   app.Run();
   ```
3. 接続文字列で環境変数を設定し、アプリを実行します。

### Java の場合
1. Azure Monitor OpenTelemetry Distro JAR (例: `applicationinsights-agent-3.x.x.jar`) をダウンロードします。
2. 同じディレクトリに設定ファイル `applicationinsights.json` を作成します：
   ```json
   {
     "connectionString": "接続文字列をここに入力"
   }
   ```
3. エージェントを指定してアプリを実行します： `java -javaagent:applicationinsights-agent-3.x.x.jar -jar your-app.jar`.

### Node.js の場合
1. パッケージをインストールします：
   ```
   npm install @azure/monitor-opentelemetry
   ```
2. アプリのエントリ ポイントで設定します：
   ```javascript
   const { AzureMonitorOpenTelemetry } = require('@azure/monitor-opentelemetry');
   const provider = new AzureMonitorOpenTelemetry({
     connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING
   });
   provider.start();
   ```
3. 環境変数を設定し、アプリを開始します。

### Python の場合
1. パッケージをインストールします：
   ```
   pip install azure-monitor-opentelemetry
   ```
2. アプリで：
   ```python
   from azure.monitor.opentelemetry import configure_azure_monitor
   configure_azure_monitor(connection_string="接続文字列をここに入力")
   ```
3. アプリを実行します。

その他の言語または自動インストルメンテーション (例: Azure App Service 向け) については、公式ドキュメントを確認してください。まずローカルでテストしてください。

## ステップ 3: データの表示と分析
1. インストルメント化されたアプリを実行し、何らかのアクティビティ (例: 要求の送信) を生成します。
2. Azure portal で、Application Insights リソースを開きます。
3. **概要** ページを確認します：ライブ メトリック、要求数、応答時間が表示されます (データは約 1～2 分で表示されます)。
4. 機能を探索します：
   - **Live Metrics**: 本番アプリ向けのリアルタイム ストリーム。
   - **失敗**: 例外とトレースを詳細に調査。
   - **パフォーマンス**: 依存関係と低速な要求を分析。
   - **使用状況**: ユーザー セッションとカスタム イベントを追跡。
   - **アラート**: 問題 (例: 高失敗率) に対する通知を設定。
5. **ログ** で Kusto クエリ言語 (KQL) を使用してデータをクエリし、カスタム分析を実行します。

## ベスト プラクティス
- 基本的なテレメトリから始め、必要に応じてカスタム イベント/メトリックを追加します。
- **使用量と推定コスト** ページでコストを監視します (Log Analytics を通じて課金されます)。
- ブラウザーの監視には、Web ページに JavaScript SDK スニペットを追加します。

[Application Insights リソースの作成と構成](https://learn.microsoft.com/en-us/azure/azure-monitor/app/create-workspace-resource)  
[Application Insights で OpenTelemetry を有効にする](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable)  
[Application Insights の概要](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)