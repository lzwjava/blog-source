---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: منع فقدان الأحداث أثناء توسيع نطاق خدمة حاويات Azure
translated: true
type: note
---

### السبب المحتمل لفقدان الأحداث

عندما يتم التوسع التلقائي لخدمتك من 1 إلى 2 وحدة Pod في خدمة Azure Kubernetes (AKS)، تتعامل وحدة الـ Pod الأولى مع الحمل المتزايد بمفردها حتى تصبح وحدة الـ Pod الجديدة جاهزة (عادة 1-2 دقيقة، اعتمادًا على تكوين Horizontal Pod Autoscaler أو HPA). إذا ارتفع حجم الأحداث بشكل مفاجئ خلال هذه الفترة، قد يحد مساحة اسم Event Hubs من دخول البيانات (على سبيل المثال، بسبب عدم كفاية وحدات الإنتاجية)، مما يؤدي إلى فقدان بنسبة ~1% (أخطاء ServerBusy). يوفر Event Hubs تسليمًا "مرة واحدة على الأقل" على أقل تقدير، ولكن بدون إعداد محاولات إعادة محاولة مناسبة، تفشل عمليات الإرسال المحدودة بصمت أو تُفقد الأحداث.

عملية التوسع بحد ذاتها لا تعطل اتصال وحدة الـ Pod الحالية – الفقدان ناتج عن الحمل الزائد العابر، وليس إنهاء وحدة الـ Pod.

### كيفية الإصلاح والتكوين
للتعامل مع هذا بشكل موثوق:

1. **تمكين التوسع التلقائي (Auto-Inflate) على مساحة اسم Event Hubs**
   يؤدي هذا إلى توسيع وحدات الإنتاجية (TUs) تلقائيًا عندما يتجاوز دخول البيانات خط الأساس الخاص بك (على سبيل المثال، من 1 إلى 20 TU)، مما يمنع التقييد أثناء ذروة الحمل مثل أحداث التوسع.
   - في بوابة Azure: انتقل إلى مساحة اسم Event Hubs الخاصة بك > **الإعدادات (Settings)** > **القياس (Scale)** > حدد **تمكين التوسع التلقائي (Enable auto-inflate)** > عيّن الحد الأقصى لـ TUs (على سبيل المثال، 20) > احفظ.
   - CLI: `az eventhubs namespace update --resource-group <rg> --name <namespace> --enable-auto-inflate true --maximum-throughput-units 20`
   - التكلفة: يتم الفوترة لكل ساعة لأقصى قيمة تم الوصول إليها؛ ابدأ بـ 5-10 TUs كخط أساس.
   يضمن هذا نمو السعة بشكل استباقي دون تدخل يدوي.

2. **تكوين عميل المُنتِج (Producer Client) للمحاولات الإعادة والموثوقية**
   استخدم Azure Event Hubs SDK في كود التطبيق الخاص بك لتنفيذ محاولات إعادة backoff أُسية عند حدوث أخطاء عابرة (التقييد، انتهاء المهلة). الإعدادات الافتراضية غالبًا ما تكون 3 محاولات إعادة مع انتهاء مهلة 60 ثانية – اضبطها حسب احتياجاتك. جمّع الأحداث (على سبيل المثال، 100-500 لكل إرسال) لتقليل استدعاءات API وتحسين المرونة.
   - **أفضل الممارسات العامة**:
     - عيّن الحد الأقصى للمحاولات: 5-10.
     - backoff أُسي: ابدأ من 1 ثانية، أقصى تأخير 30 ثانية.
     - انتهاء مهلة الاتصال: 30-60 ثانية.
     - استخدم مفاتيح عدمية (idempotent) (على سبيل المثال، UUID لكل حدث) إذا كان تكرار الأحداث مقبولاً (يدعم Event Hubs هذا في مستويات Premium/Mdedicated).
     - راقب عبر Azure Monitor: تتبع مقاييس `IncomingMessages` مقابل `ThrottledRequests`.

   - **مثال: .NET (Azure.Messaging.EventHubs)**
     ```csharp
     using Azure.Messaging.EventHubs;
     using Azure.Messaging.EventHubs.Producer;

     var connectionString = "<your-connection-string>";
     var eventHubName = "<your-eventhub-name>";

     var clientOptions = new EventHubProducerClientOptions
     {
         Retry = new EventHubsRetryOptions
         {
             TryTimeout = TimeSpan.FromSeconds(60),  // انتهاء مهلة لكل عملية
             MaximumTries = 7,  // الحد الأقصى للمحاولات
             Delay = TimeSpan.FromSeconds(2),  // backoff ابتدائي
             MaximumDelay = TimeSpan.FromSeconds(30),  // أقصى backoff
             Mode = RetryMode.Exponential  // إستراتيجية backoff
         },
         ConnectionOptions = new EventHubConnectionOptions
         {
             TransportType = EventHubsTransportType.AmqpWebSockets  // لشبكات AKS
         }
     };

     await using var producer = new EventHubProducerClient(connectionString, eventHubName, clientOptions);

     // إرسال الدُفعة
     using var batch = await producer.CreateBatchAsync(new CreateBatchOptions { PartitionKey = "your-key" });
     batch.TryAdd(new EventData(Encoding.UTF8.GetBytes("event-data")));
     await producer.SendAsync(batch);
     ```
     يعيد هذا المحاولة عند حدوث ServerBusy، مما يضمن وصول الأحداث بعد التوسع.

   - **مثال: Java (Azure Event Hubs Client)**
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
         .transportType(TransportType.AMQP_WEB_SOCKETS)  // لـ AKS
         .buildAsyncClient();

     // إرسال الدُفعة
     Flux<PartitionInformation> partitions = producer.getPartitionPropertiesFlux();
     // ... منطق إرسال الدُفعة مع محاولات الإعادة المضمنة
     ```
     يتعامل الـ SDK مع محاولات الإعادة تلقائيًا عند حدوث الأخطاء.

   - **لغات أخرى**: أنماط مشابهة في Python (azure-eventhub)، Node.js (استخدم خيارات إعادة المحاولة في EventHubProducerClient). راجع وثائق الـ SDK الخاصة بمكدّمك التقني.

3. **معالجة محددة لـ AKS للتوسع**
   - **التوسع الاستباقي**: اضبط HPA للتوسع مبكرًا (على سبيل المثال، استهدف استخدام وحدة المعالجة المركزية 60% مقابل 80%) لتقليل نافذة الحمل الزائد:
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
             averageUtilization: 60  # التوسع عند 60% استخدام لوحدة المعالجة المركزية
     ```
     طبق باستخدام `kubectl apply -f hpa.yaml`.
   - **سلوك الـ Pod الأنيق**: عيّن `terminationGracePeriodSeconds: 30` في YAML النشر (Deployment) الخاص بك للسماح للأحداث المخزنة مؤقتًا بالتفريغ أثناء عمليات التصغير المستقبلية (ليس للتوسع المباشر، لكنها ممارسة جيدة).
   - **الشبكات**: استخدم WebSockets (AMQP over WebSockets) في خيارات العميل لتحسين التعامل مع خروج بيانات AKS.
   - **المراقبة**: مكّن تشخيصات AKS في Log Analytics؛ استعلم عن أحداث الـ Pod أثناء التوسع (على سبيل المثال، `KubePodInventory | where TimeGenerated > ago(1h)`).

4. **ضمانات إضافية**
   - **مساحة اسم مقاومة لمنطقة الفشل (Zone-Redundant Namespace)**: مكّن ذلك أثناء إنشاء مساحة الاسم (افتراضي في المناطق المدعومة) للحصول على 99.99% SLA وعدم فقدان البيانات أثناء أعطال المنطقة.
   - **أقسام (Partitions)**: استخدم 4-32 قسمًا بناءً على الحمل (على سبيل المثال، لتتناسب مع المُنتِجين المتوازيين المتوقعين); عيّن مفاتيح الأقسام للتجميع المرتب.
   - **ميزة الالتقاط (Capture Feature)**: مكّن Event Hubs Capture إلى Blob Storage كنسخة احتياطية لأي فقدان نادر (مستوى Premium).
   - **الاختبار**: Simulate الحمل باستخدام أدوات مثل Apache JMeter; راقب للتأكد من عدم وجود تقييد بعد التكوين.

يجب أن يقلل هذا الإعداد الفقدان إلى接近 الصفر. ابدأ بـ auto-inflate + محاولات إعادة العميل لتحقيق نتائج سريعة.

### المراجع
- [الموثوقية في Azure Event Hubs](https://learn.microsoft.com/en-us/azure/reliability/reliability-event-hubs)
- [التوسع باستخدام Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-scalability)
- [خيارات إعادة المحاولة في Event Hubs .NET SDK](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.eventhubs.producer.eventhubproducerclientoptions.retryoptions)
- [مفاهيم توسيع نطاق AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-scale)