---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Prevención de Pérdida de Eventos Durante el Escalado de AKS
translated: true
type: note
---

### Causa probable de la pérdida de eventos
Cuando tu servicio se escala automáticamente de 1 a 2 pods en Azure Kubernetes Service (AKS), el pod inicial maneja la carga creciente solo hasta que el nuevo pod está listo (normalmente 1-2 minutos, dependiendo de tu configuración de Horizontal Pod Autoscaler - HPA). Si el volumen de eventos aumenta repentinamente durante esta ventana, tu namespace de Event Hubs puede limitar la entrada (por ejemplo, debido a unidades de rendimiento insuficientes), lo que lleva a una pérdida de ~1% (errores ServerBusy). Event Hubs ofrece entrega al-menos-una-vez, pero sin reintentos adecuados, los envíos limitados fallan silenciosamente o descartan eventos.

El escalado en sí mismo no interrumpe la conexión del pod existente; la pérdida se debe a una sobrecarga transitoria, no a la terminación del pod.

### Cómo solucionarlo y configurarlo
Para manejar esto de forma confiable:

1. **Habilitar Auto-Inflate en el Namespace de Event Hubs**
   Esto escala automáticamente las unidades de rendimiento (TUs) cuando la entrada excede tu línea base (por ejemplo, de 1 a 20 TUs), evitando la limitación durante picos de carga como eventos de escalado.
   - En Azure Portal: Ve a tu namespace de Event Hubs > **Configuración** > **Escala** > Marca **Habilitar auto-inflate** > Establece TUs máximas (ej. 20) > Guardar.
   - CLI: `az eventhubs namespace update --resource-group <rg> --name <namespace> --enable-auto-inflate true --maximum-throughput-units 20`
   - Costo: Facturado por hora por el máximo alcanzado; comienza con una línea base de 5-10 TUs.
   Esto asegura que la capacidad crezca de forma proactiva sin intervención manual.

2. **Configurar el Cliente Productor para Reintentos y Confiabilidad**
   Usa el SDK de Azure Event Hubs en tu código de aplicación para implementar reintentos de retroceso exponencial en errores transitorios (limitación, tiempos de espera agotados). Los valores predeterminados suelen ser 3 reintentos con un tiempo de espera de 60s—ajústalos según tus necesidades. Agrupa eventos (ej. 100-500 por envío) para reducir las llamadas a la API y mejorar la resiliencia.
   - **Mejores Prácticas Generales**:
     - Establecer reintentos máximos: 5-10.
     - Retroceso exponencial: Comenzar en 1s, retraso máximo 30s.
     - Tiempo de espera de conexión: 30-60s.
     - Usar claves idempotentes (ej. UUID por evento) si los duplicados son tolerables (Event Hubs soporta esto en niveles Premium/Dedicados).
     - Monitorear mediante Azure Monitor: Rastrear métricas `IncomingMessages` vs. `ThrottledRequests`.

   - **Ejemplo: .NET (Azure.Messaging.EventHubs)**
     ```csharp
     using Azure.Messaging.EventHubs;
     using Azure.Messaging.EventHubs.Producer;

     var connectionString = "<your-connection-string>";
     var eventHubName = "<your-eventhub-name>";

     var clientOptions = new EventHubProducerClientOptions
     {
         Retry = new EventHubsRetryOptions
         {
             TryTimeout = TimeSpan.FromSeconds(60),  // Tiempo de espera por operación
             MaximumTries = 7,  // Reintentos máximos
             Delay = TimeSpan.FromSeconds(2),  // Retroceso inicial
             MaximumDelay = TimeSpan.FromSeconds(30),  // Retroceso máximo
             Mode = RetryMode.Exponential  // Estrategia de retroceso
         },
         ConnectionOptions = new EventHubConnectionOptions
         {
             TransportType = EventHubsTransportType.AmqpWebSockets  // Para redes de AKS
         }
     };

     await using var producer = new EventHubProducerClient(connectionString, eventHubName, clientOptions);

     // Enviar lote
     using var batch = await producer.CreateBatchAsync(new CreateBatchOptions { PartitionKey = "your-key" });
     batch.TryAdd(new EventData(Encoding.UTF8.GetBytes("event-data")));
     await producer.SendAsync(batch);
     ```
     Esto reintenta en ServerBusy, asegurando que los eventos lleguen después del escalado.

   - **Ejemplo: Java (Azure Event Hubs Client)**
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
         .transportType(TransportType.AMQP_WEB_SOCKETS)  // Para AKS
         .buildAsyncClient();

     // Enviar lote
     Flux<PartitionInformation> partitions = producer.getPartitionPropertiesFlux();
     // ... lógica para enviar lote con reintentos incorporados
     ```
     El SDK maneja los reintentos de forma transparente en errores.

   - **Otros Lenguajes**: Patrones similares en Python (azure-eventhub), Node.js (usar opciones de reintento en EventHubProducerClient). Consulta la documentación del SDK para tu stack.

3. **Manejo Específico de AKS para Escalado**
   - **Escalado Proactivo**: Ajusta HPA para escalar antes (ej. CPU objetivo 60% vs. 80%) para reducir la ventana de sobrecarga:
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
             averageUtilization: 60  # Escalar al 60% de CPU
     ```
     Aplicar con `kubectl apply -f hpa.yaml`.
   - **Comportamiento Elegante del Pod**: Establece `terminationGracePeriodSeconds: 30` en tu YAML de Deployment para permitir que los eventos en búfer se envíen en futuros escalados hacia abajo (no directamente para el escalado hacia arriba, pero es una buena práctica).
   - **Redes**: Usa WebSockets (AMQP sobre WebSockets) en las opciones del cliente para un mejor manejo de la salida de AKS.
   - **Monitoreo**: Habilita diagnósticos de AKS en Log Analytics; consulta eventos de pods durante el escalado (ej. `KubePodInventory | where TimeGenerated > ago(1h)`).

4. **Salvaguardas Adicionales**
   - **Namespace con Redundancia de Zona**: Habilítalo en la creación del namespace (predeterminado en regiones admitidas) para un SLA del 99.99% y sin pérdidas durante fallos de zona.
   - **Particiones**: Usa 4-32 particiones según la carga (ej. que coincida con los productores paralelos esperados); asigna claves de partición para agrupación ordenada.
   - **Función Capture**: Habilita Event Hubs Capture en Blob Storage como respaldo para cualquier pérdida rara (nivel Premium).
   - **Pruebas**: Simula carga con herramientas como Apache JMeter; monitorea para cero limitación después de la configuración.

Esta configuración debería reducir la pérdida a casi cero. Comienza con auto-inflate + reintentos del cliente para mejoras rápidas.

### Referencias
- [Confiabilidad en Azure Event Hubs](https://learn.microsoft.com/en-us/azure/reliability/reliability-event-hubs)
- [Escalado con Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-scalability)
- [Opciones de Reintento del SDK .NET para Event Hubs](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.eventhubs.producer.eventhubproducerclientoptions.retryoptions)
- [Conceptos de Escalado de AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-scale)