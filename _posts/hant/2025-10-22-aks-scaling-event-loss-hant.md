---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 防止 AKS 擴展期間事件流失
translated: true
type: note
---

### 事件遺失的可能原因
當您的服務在 Azure Kubernetes Service (AKS) 中從 1 個 Pod 自動擴展至 2 個 Pod 時，初始 Pod 會單獨處理增加的負載，直到新 Pod 準備就緒（通常需要 1-2 分鐘，具體取決於您的 Horizontal Pod Autoscaler (HPA) 配置）。如果在此時間窗口內事件量激增，您的 Event Hubs 命名空間可能會限制輸入（例如，由於吞吐量單位不足），導致約 1% 的遺失（ServerBusy 錯誤）。Event Hubs 提供至少一次傳遞，但若沒有適當的重試機制，受限制的傳送會靜默失敗或丟棄事件。

擴展本身不會中斷現有 Pod 的連線——遺失源於瞬時過載，而非 Pod 終止。

### 修復與配置方法
為可靠處理此情況：

1. **在 Event Hubs 命名空間上啟用自動擴充**  
   這會在輸入超過基準時自動擴展吞吐量單位（TUs）（例如從 1 到 20 TUs），防止在擴展事件等負載激增期間發生限制。  
   - 在 Azure 入口網站中：前往您的 Event Hubs 命名空間 > **設定** > **擴展** > 勾選 **啟用自動擴充** > 設定最大 TUs（例如 20）> 儲存。  
   - CLI：`az eventhubs namespace update --resource-group <rg> --name <namespace> --enable-auto-inflate true --maximum-throughput-units 20`  
   - 成本：按達到的小時最大值計費；建議從 5-10 TUs 基準開始。  
   這可確保容量主動增長，無需手動干預。

2. **配置生產者客戶端以實現重試與可靠性**  
   在應用程式碼中使用 Azure Event Hubs SDK 來對瞬態錯誤（限制、逾時）實作指數退避重試。預設通常為 3 次重試與 60 秒逾時——請根據需求調整。批次處理事件（例如每次傳送 100-500 個）以減少 API 呼叫並提高韌性。  
   - **一般最佳實踐**：  
     - 設定最大重試次數：5-10。  
     - 指數退避：從 1 秒開始，最大延遲 30 秒。  
     - 連線逾時：30-60 秒。  
     - 若可容忍重複事件，請使用冪等鍵（例如每個事件的 UUID）（Event Hubs 在 Premium/Dedicated 層級支援此功能）。  
     - 透過 Azure Monitor 監控：追蹤 `IncomingMessages` 與 `ThrottledRequests` 指標。  

   - **範例：.NET (Azure.Messaging.EventHubs)**  
     ```csharp
     using Azure.Messaging.EventHubs;
     using Azure.Messaging.EventHubs.Producer;

     var connectionString = "<your-connection-string>";
     var eventHubName = "<your-eventhub-name>";

     var clientOptions = new EventHubProducerClientOptions
     {
         Retry = new EventHubsRetryOptions
         {
             TryTimeout = TimeSpan.FromSeconds(60),  // 每次操作逾時
             MaximumTries = 7,  // 最大重試次數
             Delay = TimeSpan.FromSeconds(2),  // 初始退避
             MaximumDelay = TimeSpan.FromSeconds(30),  // 最大退避
             Mode = RetryMode.Exponential  // 退避策略
         },
         ConnectionOptions = new EventHubConnectionOptions
         {
             TransportType = EventHubsTransportType.AmqpWebSockets  // 用於 AKS 網路
         }
     };

     await using var producer = new EventHubProducerClient(connectionString, eventHubName, clientOptions);

     // 傳送批次
     using var batch = await producer.CreateBatchAsync(new CreateBatchOptions { PartitionKey = "your-key" });
     batch.TryAdd(new EventData(Encoding.UTF8.GetBytes("event-data")));
     await producer.SendAsync(batch);
     ```  
     這會在 ServerBusy 時重試，確保事件在擴展後成功送達。

   - **範例：Java (Azure Event Hubs Client)**  
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
         .transportType(TransportType.AMQP_WEB_SOCKETS)  // 用於 AKS
         .buildAsyncClient();

     // 傳送批次
     Flux<PartitionInformation> partitions = producer.getPartitionPropertiesFlux();
     // ... 用於傳送批次並內建重試的邏輯
     ```  
     SDK 會在錯誤時透明處理重試。

   - **其他語言**：Python (azure-eventhub)、Node.js（在 EventHubProducerClient 中使用重試選項）有類似模式。請參閱您所用技術堆疊的 SDK 文件。

3. **針對擴展的 AKS 特定處理**  
   - **主動擴展**：調整 HPA 以更早擴展（例如，目標 CPU 60% 對比 80%）以減少過載窗口：  
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
             averageUtilization: 60  # 在 60% CPU 時擴展
     ```  
     使用 `kubectl apply -f hpa.yaml` 套用。  
   - **優雅的 Pod 行為**：在您的 Deployment YAML 中設定 `terminationGracePeriodSeconds: 30`，以允許緩衝事件在未來縮減時刷新（不直接用於擴展，但為良好實踐）。  
   - **網路**：在客戶端選項中使用 WebSockets（AMQP over WebSockets）以獲得更好的 AKS 輸出處理。  
   - **監控**：啟用 AKS 診斷至 Log Analytics；查詢擴展期間的 Pod 事件（例如 `KubePodInventory | where TimeGenerated > ago(1h)`）。

4. **其他防護措施**  
   - **區域冗余命名空間**：在命名空間建立時啟用（在支援區域中預設啟用），以實現 99.99% SLA 且在區域故障期間無遺失。  
   - **分割區**：根據負載使用 4-32 個分割區（例如，匹配預期的平行生產者）；分配分割區鍵以進行有序分組。  
   - **擷取功能**：啟用 Event Hubs Capture 至 Blob Storage 作為任何罕見遺失的備份（Premium 層級）。  
   - **測試**：使用 Apache JMeter 等工具模擬負載；監控配置後是否達到零限制。

此設定應能將遺失降至接近零。從自動擴充 + 客戶端重試開始以快速見效。

### 參考資料
- [Azure Event Hubs 中的可靠性](https://learn.microsoft.com/en-us/azure/reliability/reliability-event-hubs)  
- [使用 Event Hubs 進行擴展](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-scalability)  
- [Event Hubs .NET SDK 重試選項](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.eventhubs.producer.eventhubproducerclientoptions.retryoptions)  
- [AKS 擴展概念](https://learn.microsoft.com/en-us/azure/aks/concepts-scale)