---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: AWS CloudWatchログの読み取り
translated: true
type: note
---

### AWS CloudWatch ログの読み取りについて
AWS CloudWatch Logs は、AWS リソース（EC2 インスタンス、Lambda 関数、RDS データベースなど）やアプリケーションからのログファイルを一元化、監視、保存するサービスです。ログを読み取るには、まずログが CloudWatch に送信されていることを確認する必要があります（例：EC2 上の CloudWatch エージェント経由、または他のサービスとの自動連携）。設定が完了すると、AWS マネジメントコンソール、AWS CLI、または SDK を介してプログラムでログを表示できます。

### 前提条件
- **AWS 権限**: IAM ユーザーまたはロールに `logs:DescribeLogGroups`、`logs:DescribeLogStreams`、`logs:GetLogEvents`、`logs:FilterLogEvents` の権限があることを確認してください（`CloudWatchLogsReadOnlyAccess` ポリシーをアタッチします）。
- **ログ設定**: ログは CloudWatch にルーティングされている必要があります。例：
  - EC2 インスタンスに CloudWatch Logs エージェントをインストールする。
  - Lambda や ECS などのサービスでロギングを有効にする。
- **AWS CLI (オプション)**: CLI を使用する場合は、`aws configure` でインストールと設定を行います。

### AWS マネジメントコンソールでのログ表示
1. [AWS マネジメントコンソール](https://console.aws.amazon.com/) にサインインし、CloudWatch サービスを開きます。
2. 左のナビゲーションペインで、**Logs** > **Log groups** を選択します。
3. ログを含むロググループを選択します（例：Lambda ログの場合は `/aws/lambda/my-function`）。
4. ログストリームのリスト（選択したロググループの下）で、特定のストリームを選択します（例：インスタンスや実行ごとに1つ）。
5. ログイベントが読み込まれます。表示をカスタマイズします：
   - **イベントの展開**: イベントの横にある矢印をクリックして展開するか、リストの上にある **Text** ビューに切り替えてプレーンテキストを表示します。
   - **フィルター/検索**: 検索ボックスにフィルターを入力します（例：「ERROR」と入力してエラー行のみを表示）。
   - **時間範囲**: 検索ボックスの横にある時間セレクターをクリックします。**Relative**（例：過去1時間）または **Absolute**（カスタム日付）を選択し、UTC と現地時間を切り替えます。
6. イベントをスクロールして確認するか、必要に応じてダウンロードします。

複数のストリームやグループにわたる高度なクエリには、**CloudWatch Logs Insights**（Logs > Logs Insights の下）を使用します。`fields @timestamp, @message | filter @level = "ERROR" | sort @timestamp desc` のようなクエリを記述して、ログを分析および視覚化します。

### AWS CLI を使用したログの読み取り
これらのコマンドを使用して、ログをプログラムでリストおよび取得します。`my-log-group` などのプレースホルダーは実際の名前に置き換えてください。

1. **ロググループのリスト表示**:
   ```
   aws logs describe-log-groups --log-group-name-prefix my-log-group
   ```
   これにより、ARN、保持期間、保存バイト数などのメタデータが返されます。

2. **グループ内のログストリームのリスト表示**:
   ```
   aws logs describe-log-streams --log-group-name my-log-group --log-stream-name-prefix 2025
   ```
   プレフィックス（例：日付ベースの名前）でストリームをフィルタリングし、作成時刻とサイズを表示します。

3. **ストリームからのログイベントの取得**:
   ```
   aws logs get-log-events --log-group-name my-log-group --log-stream-name my-stream --start-time 1730137600000
   ```
   - `--start-time` および `--end-time`: 時間範囲の Unix タイムスタンプ（ミリ秒）。
   - `--limit`: 返される最大イベント数（デフォルトは 1,000）。
   - 出力には、タイムスタンプ、インジェスト時間、メッセージテキストが含まれます。
   - レスポンスからの `--next-token` を使用してページネーションを行います。

ストリーム全体でのフィルタリング検索には、`filter-log-events` を使用します：
```
aws logs filter-log-events --log-group-name my-log-group --filter-pattern "ERROR" --start-time 1730137600000
```

### ヒントとベストプラクティス
- **保持期間**: ログはデフォルトで無期限に保持されます。コストを管理するためにグループごとに調整します（例：30日）。
- **コスト**: 表示は無料ですが、インジェストと保存には料金がかかります—CloudWatch メトリクスで監視してください。
- **トラブルシューティング**: ログが表示されない場合は、エージェントのインストールまたはサービスのロギングが有効になっていることを確認してください。
- リアルタイム監視には、ログパターンに対するメトリクスフィルターまたはアラームを設定します。

[Working with log groups and log streams - Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)  
[CloudWatch Logs examples using AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli_cloudwatch-logs_code_examples.html)  
[Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)