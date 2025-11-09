---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Verhinderung von Ereignisverlust beim AKS-Skalieren
translated: true
type: note
---

### Wahrscheinliche Ursache für Ereignisverlust

Wenn Ihr Dienst in Azure Kubernetes Service (AKS) von 1 auf 2 Pods hochskaliert, bewältigt der anfängliche Pod die steigende Last alleine, bis der neue Pod bereit ist (typischerweise 1-2 Minuten, abhängig von Ihrer Horizontal Pod Autoscaler (HPA)-Konfiguration). Wenn das Ereignisvolumen während dieses Zeitfensters stark ansteigt, könnte Ihr Event Hubs-Namespace den Eingang drosseln (z.B. aufgrund unzureichender Durchsatzeinheiten), was zu einem Verlust von ~1% führt (ServerBusy-Fehler). Event Hubs bietet eine At-Least-Once-Zustellung, aber ohne ordnungsgemäße Wiederholungsversuche schlagen gedrosselte Sendeversuche stillschweigend fehl oder verlieren Ereignisse.

Das Hochskalieren selbst unterbricht nicht die Verbindung des bestehenden Pods – der Verlust resultiert aus transienter Überlastung, nicht aus Pod-Beendigung.

### Behebung und Konfiguration

Um dies zuverlässig zu handhaben:

1.  **Aktivieren Sie Auto-Inflate im Event Hubs-Namespace**
    Dies skaliert Durchsatzeinheiten (TUs) automatisch hoch, wenn der Eingang Ihre Basislinie überschreitet (z.B. von 1 auf 20 TUs), und verhindert so Drosselung während Lastspitzen wie Skalierungsereignissen.
    - Im Azure-Portal: Gehen Sie zu Ihrem Event Hubs-Namespace > **Einstellungen** > **Skalieren** > Aktivieren Sie **Auto-inflate aktivieren** > Legen Sie die max. TUs fest (z.B. 20) > Speichern.
    - CLI: `az eventhubs namespace update --resource-group <rg> --name <namespace> --enable-auto-inflate true --maximum-throughput-units 20`
    - Kosten: Abgerechnet pro Stunde für das erreichte Maximum; beginnen Sie mit einer Basislinie von 5-10 TUs.
    Dies stellt sicher, dass die Kapazität proaktiv ohne manuelles Eingreifen wächst.

2.  **Konfigurieren Sie den Producer-Client für Wiederholungsversuche und Zuverlässigkeit**
    Verwenden Sie das Azure Event Hubs SDK in Ihrem App-Code, um exponentielle Backoff-Wiederholungsversuche bei transienten Fehlern (Drosselung, Timeouts) zu implementieren. Standardwerte sind oft 3 Wiederholungsversuche mit 60s Timeout – passen Sie diese an Ihre Bedürfnisse an. Bündeln Sie Ereignisse (z.B. 100-500 pro Sendevorgang), um API-Aufrufe zu reduzieren und die Resilienz zu verbessern.
    - **Allgemeine Best Practices**:
        - Setzen Sie max. Wiederholungsversuche: 5-10.
        - Exponentieller Backoff: Beginnen Sie bei 1s, max. Verzögerung 30s.
        - Verbindungs-Timeout: 30-60s.
        - Verwenden Sie idempotente Schlüssel (z.B. UUID pro Ereignis), wenn Duplikate tolerierbar sind (Event Hubs unterstützt dies in Premium/Dedicated-Tarifen).
        - Überwachen Sie via Azure Monitor: Verfolgen Sie die Metriken `IncomingMessages` vs. `ThrottledRequests`.

    - **Beispiel: .NET (Azure.Messaging.EventHubs)**
      ```csharp
      using Azure.Messaging.EventHubs;
      using Azure.Messaging.EventHubs.Producer;

      var connectionString = "<your-connection-string>";
      var eventHubName = "<your-eventhub-name>";

      var clientOptions = new EventHubProducerClientOptions
      {
          Retry = new EventHubsRetryOptions
          {
              TryTimeout = TimeSpan.FromSeconds(60),  // Timeout pro Operation
              MaximumTries = 7,  // Max. Wiederholungsversuche
              Delay = TimeSpan.FromSeconds(2),  // Initialer Backoff
              MaximumDelay = TimeSpan.FromSeconds(30),  // Max. Backoff
              Mode = RetryMode.Exponential  // Backoff-Strategie
          },
          ConnectionOptions = new EventHubConnectionOptions
          {
              TransportType = EventHubsTransportType.AmqpWebSockets  // Für AKS-Netzwerk
          }
      };

      await using var producer = new EventHubProducerClient(connectionString, eventHubName, clientOptions);

      // Batch senden
      using var batch = await producer.CreateBatchAsync(new CreateBatchOptions { PartitionKey = "your-key" });
      batch.TryAdd(new EventData(Encoding.UTF8.GetBytes("event-data")));
      await producer.SendAsync(batch);
      ```
      Dies wiederholt bei ServerBusy-Fehlern und stellt sicher, dass Ereignisse nach dem Skalieren ankommen.

    - **Beispiel: Java (Azure Event Hubs Client)**
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
          .transportType(TransportType.AMQP_WEB_SOCKETS)  // Für AKS
          .buildAsyncClient();

      // Batch senden
      Flux<PartitionInformation> partitions = producer.getPartitionPropertiesFlux();
      // ... Logik zum Senden des Batches mit integrierten Wiederholungsversuchen
      ```
      Das SDK behandelt Wiederholungsversuche bei Fehlern transparent.

    - **Andere Sprachen**: Ähnliche Muster in Python (azure-eventhub), Node.js (verwenden Sie Retry-Options in EventHubProducerClient). Siehe SDK-Dokumentation für Ihren Stack.

3.  **AKS-spezifische Handhabung für Skalierung**
    - **Proaktive Skalierung**: Optimieren Sie den HPA, um früher zu skalieren (z.B. Ziel-CPU 60% vs. 80%), um das Überlastungsfenster zu verringern:
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
              averageUtilization: 60  # Skaliert bei 60% CPU
      ```
      Anwenden mit `kubectl apply -f hpa.yaml`.
    - **Graceful Pod-Verhalten**: Setzen Sie `terminationGracePeriodSeconds: 30` in Ihrer Deployment-YAML, um das Leeren gepufferter Ereignisse bei zukünftigem Herunterskalieren zu ermöglichen (nicht direkt für Hochskalieren, aber gute Praxis).
    - **Netzwerk**: Verwenden Sie WebSockets (AMQP over WebSockets) in den Client-Optionen für eine bessere AKS-Ausgangsbehandlung.
    - **Monitoring**: Aktivieren Sie AKS-Diagnosen für Log Analytics; fragen Sie Pod-Ereignisse während der Skalierung ab (z.B. `KubePodInventory | where TimeGenerated > ago(1h)`).

4.  **Zusätzliche Sicherheitsvorkehrungen**
    - **Zonenredundanter Namespace**: Aktivieren Sie dies bei der Namespace-Erstellung (Standard in unterstützten Regionen) für 99,99% SLA und keinen Verlust während Zonenausfällen.
    - **Partitionen**: Verwenden Sie 4-32 Partitionen basierend auf der Last (z.B. entsprechend der erwarteten parallelen Producer); weisen Sie Partitionsschlüssel für geordnete Gruppierung zu.
    - **Capture-Feature**: Aktivieren Sie Event Hubs Capture in den Blob Storage als Backup für seltene Verluste (Premium-Tarif).
    - **Test**: Simulieren Sie Last mit Tools wie Apache JMeter; überwachen Sie, ob nach der Konfiguration keine Drosselung mehr auftritt.

Dieses Setup sollte den Verlust auf nahezu Null reduzieren. Beginnen Sie mit Auto-Inflate + Client-Wiederholungsversuchen für schnelle Erfolge.

### Referenzen

-   [Zuverlässigkeit in Azure Event Hubs](https://learn.microsoft.com/en-us/azure/reliability/reliability-event-hubs)
-   [Skalieren mit Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-scalability)
-   [Event Hubs .NET SDK Retry-Optionen](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.eventhubs.producer.eventhubproducerclientoptions.retryoptions)
-   [AKS-Skalierungskonzepte](https://learn.microsoft.com/en-us/azure/aks/concepts-scale)