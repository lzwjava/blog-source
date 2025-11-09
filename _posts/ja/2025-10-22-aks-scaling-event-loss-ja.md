---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: AKSスケーリング時のイベント損失防止
translated: true
type: note
---

### イベント損失の可能性が高い原因
Azure Kubernetes Service (AKS) でサービスが1から2ポッドに自動スケールする際、新しいポッドが準備完了するまで（通常1-2分、HPAの設定に依存）、既存の単一ポッドが増加する負荷を単独で処理します。この時間帯にイベント量が急増すると、Event Hubs 名前空間がイングレスをスロットル（例：スループットユニット不足）し、約1%の損失（ServerBusy エラー）が発生する可能性があります。Event Hubs は少なくとも1回の配信を保証しますが、適切なリトライがない場合、スロットルされた送信はサイレントに失敗するか、イベントがドロップされます。

スケールアップ自体は既存ポッドの接続を切断しません。損失はポッド終了ではなく、一時的な過負荷に起因します。

### 修正と構成方法
この問題を確実に処理するには：

1. **Event Hubs 名前空間で Auto-Inflate を有効化**  
   これは、ベースライン（例：1 TUから20 TU）を超えるイングレス発生時にスループットユニット (TU) を自動スケールし、スケールイベント時のような負荷急増時のスロットリングを防止します。  
   - Azure Portal: Event Hubs 名前空間 > **設定** > **スケール** > **Auto-inflate を有効にする** をチェック > 最大 TU（例：20）を設定 > 保存。  
   - CLI: `az eventhubs namespace update --resource-group <rg> --name <namespace> --enable-auto-inflate true --maximum-throughput-units 20`  
   - コスト: 到達した最大値に対して時間単位で課金。ベースラインは5-10 TUから開始。  
   これにより、手動介入なしで容量が事前に拡張されます。

2. **プロデューサークライアントのリトライと信頼性のための構成**  
   アプリコードで Azure Event Hubs SDK を使用し、一時的なエラー（スロットリング、タイムアウト）に対して指数バックオフリトライを実装します。デフォルトは多くの場合、60秒タイムアウトで3回リトライ。必要に応じて調整します。イベントをバッチ処理（例：送信あたり100-500イベント）して API 呼び出しを減らし、回復性を向上させます。  
   - **一般的なベストプラクティス**:  
     - 最大リトライ回数: 5-10。  
     - 指数バックオフ: 1秒から開始、最大遅延30秒。  
     - 接続タイムアウト: 30-60秒。  
     - 重複が許容される場合は冪等キーを使用（例：イベントごとに UUID）。Event Hubs は Premium/Dedicated 階層でこれをサポート。  
     - Azure Monitor で監視: `IncomingMessages` と `ThrottledRequests` メトリクスを追跡。  

   - **例: .NET (Azure.Messaging.EventHubs)**  
     ```csharp
     using Azure.Messaging.EventHubs;
     using Azure.Messaging.EventHubs.Producer;

     var connectionString = "<your-connection-string>";
     var eventHubName = "<your-eventhub-name>";

     var clientOptions = new EventHubProducerClientOptions
     {
         Retry = new EventHubsRetryOptions
         {
             TryTimeout = TimeSpan.FromSeconds(60),  // 操作ごとのタイムアウト
             MaximumTries = 7,  // 最大リトライ回数
             Delay = TimeSpan.FromSeconds(2),  // 初期バックオフ
             MaximumDelay = TimeSpan.FromSeconds(30),  // 最大バックオフ
             Mode = RetryMode.Exponential  // バックオフ戦略
         },
         ConnectionOptions = new EventHubConnectionOptions
         {
             TransportType = EventHubsTransportType.AmqpWebSockets  // AKS ネットワーキング用
         }
     };

     await using var producer = new EventHubProducerClient(connectionString, eventHubName, clientOptions);

     // バッチ送信
     using var batch = await producer.CreateBatchAsync(new CreateBatchOptions { PartitionKey = "your-key" });
     batch.TryAdd(new EventData(Encoding.UTF8.GetBytes("event-data")));
     await producer.SendAsync(batch);
     ```  
     これは ServerBusy 時にリトライし、スケール後もイベントが確実に送信されます。

   - **例: Java (Azure Event Hubs Client)**  
     ```java
     import com.azure.messaging.eventhubs.EventHubProducerAsyncClient;
     import com.azure.messaging.eventhubs.EventHubProducerClientBuilder;
     import com.azure.messaging.eventhubs.models.CreateBatchOptions;
     import com.azure.messaging.eventhubs.models.EventHubProducerAsyncClientBuilder;
     import com.azure.core.amqp.AmqpRetryOptions;

     String connectionString = "<your-connection-string>";
     String eventHubName = "<your-eventhub-name>";

     AmqpRetryOptions retryOptions = new AmqpRetryOptions()
         .setMaxRetries(7)
         .setInitialDelay(Duration.ofSeconds(2))
         .setMaxDelay(Duration.ofSeconds(30))
         .setTryTimeout(Duration.ofSeconds(60));

     EventHubProducerAsyncClient producer = new EventHubProducerClientBuilder()
         .connectionString(connectionString, eventHubName)
         .retryOptions(retryOptions)
         .transportType(TransportType.AMQP_WEB_SOCKETS)  // AKS 用
         .buildAsyncClient();

     // バッチ送信
     Flux<PartitionInformation> partitions = producer.getPartitionPropertiesFlux();
     // ... リトライが組み込まれたバッチ送信ロジック
     ```  
     SDK はエラー時に透過的にリトライを処理します。

   - **その他の言語**: Python (azure-eventhub)、Node.js (EventHubProducerClient のリトライオプション使用) でも同様のパターン。使用スタックの SDK ドキュメントを参照。

3. **スケーリングのための AKS 固有の処理**  
   - ** proactive スケーリング**: 過負荷期間を短縮するため、HPA を早めにスケールするよう調整（例：CPU 80% ではなく 60% をターゲット）:  
     ```yaml
     apiVersion: autoscaling/v2
     kind: HorizontalPodAutoscaler
     metadata:
       name: your-app-hpa
     spec:
       scaleTargetRef:
         apiVersion: apps/v1
         kind: Deployment
         name: your-app
       minReplicas: 1
       maxReplicas: 10
       metrics:
       - type: Resource
         resource:
           name: cpu
           target:
             type: Utilization
             averageUtilization: 60  # CPU 60% でスケール
     ```  
     `kubectl apply -f hpa.yaml` で適用。  
   - **Graceful Pod 動作**: 将来のスケールダウン時にバッファリングされたイベントがフラッシュされるよう、Deployment YAML で `terminationGracePeriodSeconds: 30` を設定（スケールアップ直接向けではないが、良い習慣）。  
   - **ネットワーキング**: AKS エグレスの処理を改善するため、クライアントオプションで WebSockets (AMQP over WebSockets) を使用。  
   - **監視**: AKS 診断を Log Analytics に有効化。スケール時のポッドイベントをクエリ（例: `KubePodInventory | where TimeGenerated > ago(1h)`）。

4. **追加の保護策**  
   - **ゾーン冗長名前空間**: 名前空間作成時に有効化（サポートリージョンではデフォルト）。99.99% SLA を提供し、ゾーン障害時の損失を防止。  
   - **パーティション**: 負荷に基づき4-32パーティションを使用（例：想定並列プロデューサー数に合わせる）。順序付けグループ化のためパーティションキーを割り当て。  
   - **Capture 機能**: 稀な損失のバックアップとして、Event Hubs Capture を Blob Storage に有効化（Premium 階層）。  
   - **テスト**: Apache JMeter などのツールで負荷をシミュレート。構成後にスロットリングがゼロであることを監視。

このセットアップにより、損失をほぼゼロに削減できます。まずは Auto-inflate + クライアントリトライから始めて、迅速な改善を図ります。

### 参考資料
- [Reliability in Azure Event Hubs](https://learn.microsoft.com/en-us/azure/reliability/reliability-event-hubs)  
- [Scaling with Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-scalability)  
- [Event Hubs .NET SDK Retry Options](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.eventhubs.producer.eventhubproducerclientoptions.retryoptions)  
- [AKS Scaling Concepts](https://learn.microsoft.com/en-us/azure/aks/concepts-scale)