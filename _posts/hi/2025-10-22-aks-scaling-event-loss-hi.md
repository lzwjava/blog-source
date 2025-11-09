---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: एकेएस स्केलिंग के दौरान ईवेंट लॉस को रोकना
translated: true
type: note
---

### इवेंट हानि का संभावित कारण
जब आपकी सेवा Azure Kubernetes Service (AKS) में 1 से 2 पॉड्स तक ऑटो-स्केल करती है, तो प्रारंभिक पॉड नए पॉड के तैयार होने तक (आमतौर पर 1-2 मिनट, आपके Horizontal Pod Autoscaler (HPA) कॉन्फ़िगरेशन पर निर्भर करता है) बढ़ते लोड को अकेले संभालता है। यदि इस समयावधि के दौरान इवेंट वॉल्यूम में अचानक वृद्धि होती है, तो आपके Event Hubs नेमस्पेस में इनग्रेस थ्रॉटल हो सकती है (जैसे, अपर्याप्त थ्रूपुट यूनिट्स के कारण), जिससे ~1% हानि (ServerBusy errors) हो सकती है। Event Hubs कम-से-कम-एकबार डिलीवरी प्रदान करता है, लेकिन उचित रिट्राइज़ के बिना, थ्रॉटल किए गए सेण्ड विफल हो जाते हैं या इवेंट्स ड्रॉप हो जाते हैं।

स्केलिंग अप स्वयं मौजूदा पॉड के कनेक्शन को बाधित नहीं करती—हानि अस्थायी ओवरलोड से उत्पन्न होती है, पॉड समाप्ति से नहीं।

### कैसे ठीक करें और कॉन्फ़िगर करें
इसे विश्वसनीय रूप से संभालने के लिए:

1. **Event Hubs नेमस्पेस पर ऑटो-इन्फ्लेट सक्षम करें**  
   यह आपके बेसलाइन से अधिक इनग्रेस होने पर थ्रूपुट यूनिट्स (TUs) को स्वचालित रूप से स्केल कर देता है (जैसे, 1 से 20 TUs), स्केलिंग इवेंट्स जैसे लोड स्पाइक्स के दौरान थ्रॉटलिंग को रोकता है।  
   - Azure पोर्टल में: अपने Event Hubs नेमस्पेस पर जाएं > **सेटिंग्स** > **स्केल** > **Enable auto-inflate** चेक करें > अधिकतम TUs सेट करें (जैसे, 20) > सेव करें।  
   - CLI: `az eventhubs namespace update --resource-group <rg> --name <namespace> --enable-auto-inflate true --maximum-throughput-units 20`  
   - लागत: प्रति घंटे प्राप्त अधिकतम के लिए बिल किया जाता है; 5-10 TUs बेसलाइन से शुरू करें।  
   यह सुनिश्चित करता है कि क्षमता मैन्युअल हस्तक्षेप के बिना सक्रिय रूप से बढ़े।

2. **रिट्राइज़ और विश्वसनीयता के लिए प्रोड्यूसर क्लाइंट कॉन्फ़िगर करें**  
   अस्थायी errors (थ्रॉटलिंग, टाइमआउट) पर एक्सपोनेंशियल बैकऑफ रिट्राइज़ लागू करने के लिए अपने ऐप कोड में Azure Event Hubs SDK का उपयोग करें। डिफॉल्ट अक्सर 60s टाइमआउट के साथ 3 रिट्राइज़ होते हैं—अपनी आवश्यकताओं के लिए ट्यून करें। API कॉल्स कम करने और लचीलापन बेहतर करने के लिए इवेंट्स को बैच करें (जैसे, 100-500 प्रति सेण्ड)।  
   - **सामान्य सर्वोत्तम अभ्यास**:  
     - अधिकतम रिट्राइज़ सेट करें: 5-10.  
     - एक्सपोनेंशियल बैकऑफ: 1s से शुरू करें, अधिकतम विलंब 30s.  
     - कनेक्शन टाइमआउट: 30-60s.  
     - यदि डुप्लिकेट्स सहनीय हैं तो अचल कुंजियों का उपयोग करें (जैसे, प्रति इवेंट UUID) (Event Hubs Premium/Dedicated टियर में इसका समर्थन करता है)।  
     - Azure Monitor के माध्यम से मॉनिटर करें: `IncomingMessages` बनाम `ThrottledRequests` मेट्रिक्स ट्रैक करें।  

   - **उदाहरण: .NET (Azure.Messaging.EventHubs)**  
     ```csharp
     using Azure.Messaging.EventHubs;
     using Azure.Messaging.EventHubs.Producer;

     var connectionString = "<your-connection-string>";
     var eventHubName = "<your-eventhub-name>";

     var clientOptions = new EventHubProducerClientOptions
     {
         Retry = new EventHubsRetryOptions
         {
             TryTimeout = TimeSpan.FromSeconds(60),  // प्रति-ऑपरेशन टाइमआउट
             MaximumTries = 7,  // अधिकतम रिट्राइज़
             Delay = TimeSpan.FromSeconds(2),  // प्रारंभिक बैकऑफ
             MaximumDelay = TimeSpan.FromSeconds(30),  // अधिकतम बैकऑफ
             Mode = RetryMode.Exponential  // बैकऑफ रणनीति
         },
         ConnectionOptions = new EventHubConnectionOptions
         {
             TransportType = EventHubsTransportType.AmqpWebSockets  // AKS नेटवर्किंग के लिए
         }
     };

     await using var producer = new EventHubProducerClient(connectionString, eventHubName, clientOptions);

     // बैच भेजें
     using var batch = await producer.CreateBatchAsync(new CreateBatchOptions { PartitionKey = "your-key" });
     batch.TryAdd(new EventData(Encoding.UTF8.GetBytes("event-data")));
     await producer.SendAsync(batch);
     ```  
     यह ServerBusy पर रिट्राइज़ करता है, यह सुनिश्चित करता है कि इवेंट्स पोस्ट-स्केल पहुंच जाएं।

   - **उदाहरण: Java (Azure Event Hubs Client)**  
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
         .transportType(TransportType.AMQP_WEB_SOCKETS)  // AKS के लिए
         .buildAsyncClient();

     // बैच भेजें
     Flux<PartitionInformation> partitions = producer.getPartitionPropertiesFlux();
     // ... रिट्राइज़ बिल्ट-इन के साथ बैच भेजने के लिए लॉजिक
     ```  
     SDK errors पर पारदर्शी रूप से रिट्राइज़ संभालता है।

   - **अन्य भाषाएं**: Python (azure-eventhub), Node.js (EventHubProducerClient में रिट्राइ विकल्पों का उपयोग करें) में समान पैटर्न। अपने स्टैक के लिए SDK डॉक्स देखें।

3. **स्केलिंग के लिए AKS-विशिष्ट हैंडलिंग**  
   - **सक्रिय स्केलिंग**: ओवरलोड विंडो को कम करने के लिए HPA को पहले स्केल करने के लिए ट्यून करें (जैसे, लक्ष्य CPU 60% बनाम 80%):  
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
             averageUtilization: 60  # 60% CPU पर स्केल करें
     ```  
     `kubectl apply -f hpa.yaml` के साथ लागू करें।  
   - **सहज पॉड व्यवहार**: भविष्य की स्केल-डाउन पर बफर किए गए इवेंट्स को फ्लश करने की अनुमति देने के लिए अपने Deployment YAML में `terminationGracePeriodSeconds: 30` सेट करें (सीधे अप के लिए नहीं, लेकिन अच्छा अभ्यास)।  
   - **नेटवर्किंग**: बेहतर AKS एग्रेस हैंडलिंग के लिए क्लाइंट विकल्पों में WebSockets (AMQP over WebSockets) का उपयोग करें।  
   - **मॉनिटरिंग**: लॉग एनालिटिक्स में AKS डायग्नोस्टिक्स सक्षम करें; स्केल के दौरान पॉड इवेंट्स के लिए क्वेरी करें (जैसे, `KubePodInventory | where TimeGenerated > ago(1h)`).

4. **अतिरिक्त सुरक्षा उपाय**  
   - **ज़ोन-रिडंडेंट नेमस्पेस**: नेमस्पेस निर्माण में सक्षम करें (समर्थित क्षेत्रों में डिफॉल्ट) 99.99% SLA और ज़ोन विफलताओं के दौरान कोई हानि नहीं के लिए।  
   - **पार्टीशन्स**: लोड के आधार पर 4-32 पार्टीशन्स का उपयोग करें (जैसे, अपेक्षित समानांतर प्रोड्यूसर्स से मेल खाएं); ऑर्डरड ग्रुपिंग के लिए पार्टीशन कुंजियाँ निर्दिष्ट करें।  
   - **कैप्चर फीचर**: किसी भी दुर्लभ हानि के लिए बैकअप के रूप में Blob Storage में Event Hubs Capture सक्षम करें (Premium टियर)।  
   - **टेस्ट**: Apache JMeter जैसे टूल्स के साथ लोड सिम्युलेट करें; पोस्ट-कॉन्फ़िग शून्य थ्रॉटलिंग के लिए मॉनिटर करें।

यह सेटअप हानि को लगभग-शून्य तक गिरा देगा। त्वरित सफलताओं के लिए ऑटो-इन्फ्लेट + क्लाइंट रिट्राइज़ से शुरुआत करें।

### संदर्भ
- [Azure Event Hubs में विश्वसनीयता](https://learn.microsoft.com/en-us/azure/reliability/reliability-event-hubs)  
- [Event Hubs के साथ स्केलिंग](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-scalability)  
- [Event Hubs .NET SDK रिट्राइ विकल्प](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.eventhubs.producer.eventhubproducerclientoptions.retryoptions)  
- [AKS स्केलिंग अवधारणाएँ](https://learn.microsoft.com/en-us/azure/aks/concepts-scale)