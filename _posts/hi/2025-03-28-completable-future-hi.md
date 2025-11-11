---
audio: false
generated: true
lang: hi
layout: post
title: जावा में कम्प्लीटेबल फ्यूचर
translated: true
type: note
---

एक Java Spring Boot प्रोजेक्ट में, JavaScript के `Promise.all` का कोई सीधा समकक्ष नहीं है, जो कई प्रॉमिसेज के पूरा होने का इंतज़ार करता है और उनके परिणाम प्रदान करता है। हालाँकि, आप `java.util.concurrent` पैकेज से `CompletableFuture` का उपयोग करके, विशेष रूप से `CompletableFuture.allOf` मेथड के साथ, समान कार्यक्षमता प्राप्त कर सकते हैं - एक for लूप में कई टास्क्स को समवर्ती रूप से चलाना और सभी थ्रेड्स के पूरा होने के बाद उनके परिणामों का उपयोग करना। यह दृष्टिकोण एक Spring Boot प्रोजेक्ट के लिए बहुत उपयुक्त है, खासकर जब Spring की अतुल्यकालिक प्रोग्रामिंग सुविधाओं के साथ संयुक्त हो। नीचे, मैं इसे चरण दर चरण समझाऊंगा, जिसमें एक पूर्ण उदाहरण भी शामिल है।

### `CompletableFuture` क्यों?
`CompletableFuture` (Java 8 में पेश किया गया) आपको अतुल्यकालिक ऑपरेशन करने और उनके पूरा होने का प्रबंधन करने की अनुमति देता है। `allOf` मेथड कई `CompletableFuture` इंस्टेंस लेती है और एक नया `CompletableFuture` रिटर्न करती है जो तब पूरा होता है जब दिए गए सभी फ्यूचर्स पूरे हो जाते हैं, जिससे यह आपके परिदृश्य के लिए आदर्श बन जाता है जहाँ आप चाहते हैं:
- For लूप के भीतर टास्क्स को समानांतर में निष्पादित करना।
- सभी टास्क्स के समाप्त होने की प्रतीक्षा करना।
- बाद में परिणामों का उपयोग करना।

### कार्यान्वयन के चरण
Spring Boot प्रोजेक्ट में आप अपने समाधान को इस प्रकार संरचित कर सकते हैं:

1.  **अतुल्यकालिक टास्क्स को परिभाषित करें**
    आपके for लूप का प्रत्येक पुनरावृत्ति एक ऐसे टास्क का प्रतिनिधित्व करता है जो स्वतंत्र रूप से चल सकता है। ये टास्क `CompletableFuture` इंस्टेंस रिटर्न करेंगे, जो उनके अंतिम परिणामों का प्रतिनिधित्व करते हैं।

2.  **फ्यूचर्स को इकट्ठा करें**
    लूप में बनाते समय सभी `CompletableFuture` ऑब्जेक्ट्स को एक सूची में संग्रहीत करें।

3.  **सभी टास्क्स के पूरा होने की प्रतीक्षा करें**
    सभी टास्क्स के समाप्त होने पर एक सिंगल फ्यूचर बनाने के लिए `CompletableFuture.allOf` का उपयोग करें।

4.  **परिणाम प्राप्त करें और उपयोग करें**
    सभी टास्क्स पूरे होने के बाद, प्रत्येक `CompletableFuture` से परिणाम निकालें और उन्हें आवश्यकतानुसार प्रोसेस करें।

5.  **एक्सेप्शन्स को हैंडल करें**
    टास्क निष्पादन के दौरान संभावित त्रुटियों के लिए ध्यान रखें।

### उदाहरण कार्यान्वयन
मान लें कि आपके पास समवर्ती रूप से प्रोसेस करने के लिए आइटम्स की एक सूची है (जैसे, किसी सर्विस को कॉल करना या कुछ कम्प्यूटेशन करना)। यहाँ दो दृष्टिकोण हैं: एक Spring के `@Async` एनोटेशन का उपयोग करते हुए और दूसरा `CompletableFuture.supplyAsync` का उपयोग करते हुए।

#### दृष्टिकोण 1: Spring के साथ `@Async` का उपयोग करना
Spring Boot अतुल्यकालिक रूप से मेथड्स चलाने के लिए `@Async` एनोटेशन प्रदान करता है। आपको अपने एप्लिकेशन में async सपोर्ट सक्षम करने की आवश्यकता होगी।

**चरण 1: Async सपोर्ट सक्षम करें**
एक कॉन्फ़िगरेशन क्लास या अपनी मुख्य एप्लिकेशन क्लास में `@EnableAsync` एनोटेशन जोड़ें:

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

@SpringBootApplication
@EnableAsync
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

**चरण 2: एक Async मेथड वाली सर्विस को परिभाषित करें**
एक सर्विस बनाएं जिसमें एक मेथड हो जो प्रत्येक आइटम को अतुल्यकालिक रूप से प्रोसेस करती है:

```java
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import java.util.concurrent.CompletableFuture;

@Service
public class MyService {

    @Async
    public CompletableFuture<String> processItem(String item) {
        // कुछ कार्य का अनुकरण करें (जैसे, I/O या कम्प्यूटेशन)
        try {
            Thread.sleep(1000); // 1-सेकंड की देरी
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return CompletableFuture.completedFuture("Interrupted: " + item);
        }
        return CompletableFuture.completedFuture("Processed: " + item);
    }
}
```

**चरण 3: कंट्रोलर या सर्विस में आइटम्स को प्रोसेस करें**
अपने कंट्रोलर या किसी अन्य सर्विस में, टास्क जमा करने और सभी परिणामों की प्रतीक्षा करने के लिए for लूप का उपयोग करें:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.concurrent.CompletableFuture;

@Component
public class ItemProcessor {

    @Autowired
    private MyService myService;

    public List<String> processItems(List<String> items) {
        // सभी फ्यूचर्स को रखने के लिए सूची
        List<CompletableFuture<String>> futures = new ArrayList<>();

        // for लूप में प्रत्येक टास्क जमा करें
        for (String item : items) {
            CompletableFuture<String> future = myService.processItem(item);
            futures.add(future);
        }

        // सभी टास्क्स के पूरा होने की प्रतीक्षा करें
        CompletableFuture<Void> allFutures = CompletableFuture.allOf(
            futures.toArray(new CompletableFuture[0])
        );

        // सभी टास्क्स के पूरे होने तक ब्लॉक करें
        allFutures.join();

        // परिणाम एकत्रित करें
        List<String> results = futures.stream()
            .map(CompletableFuture::join) // प्रत्येक परिणाम प्राप्त करें
            .collect(Collectors.toList());

        return results;
    }
}
```

**उपयोग उदाहरण:**
```java
List<String> items = Arrays.asList("Item1", "Item2", "Item3");
List<String> results = itemProcessor.processItems(items);
System.out.println(results); // प्रिंट करता है: [Processed: Item1, Processed: Item2, Processed: Item3]
```

#### दृष्टिकोण 2: `CompletableFuture.supplyAsync` का उपयोग करना
यदि आप `@Async` का उपयोग नहीं करना चाहते हैं, तो आप एक `Executor` और `CompletableFuture.supplyAsync` के साथ थ्रेड्स को मैन्युअल रूप से प्रबंधित कर सकते हैं।

**चरण 1: एक थ्रेड पूल कॉन्फ़िगर करें**
थ्रेड पूल को नियंत्रित करने के लिए एक `TaskExecutor` बीन को परिभाषित करें:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.core.task.TaskExecutor;

@Configuration
public class AsyncConfig {

    @Bean
    public TaskExecutor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);    // पूल में रखने के लिए थ्रेड्स की संख्या
        executor.setMaxPoolSize(10);    // थ्रेड्स की अधिकतम संख्या
        executor.setQueueCapacity(25);  // लंबित टास्क्स के लिए कतार क्षमता
        executor.initialize();
        return executor;
    }
}
```

**चरण 2: `supplyAsync` के साथ आइटम्स को प्रोसेस करें**
टास्क्स को अतुल्यकालिक रूप से चलाने के लिए एक्सिक्यूटर का उपयोग करें:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.stream.Collectors;
import org.springframework.core.task.TaskExecutor;

@Component
public class ItemProcessor {

    @Autowired
    private TaskExecutor taskExecutor;

    public List<String> processItems(List<String> items) {
        // supplyAsync का उपयोग करके फ्यूचर्स बनाएं
        List<CompletableFuture<String>> futures = items.stream()
            .map(item -> CompletableFuture.supplyAsync(() -> processItem(item), taskExecutor))
            .collect(Collectors.toList());

        // सभी टास्क्स के पूरा होने की प्रतीक्षा करें
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).join();

        // परिणाम एकत्रित करें
        List<String> results = futures.stream()
            .map(CompletableFuture::join)
            .collect(Collectors.toList());

        return results;
    }

    private String processItem(String item) {
        // कुछ कार्य का अनुकरण करें
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return "Interrupted: " + item;
        }
        return "Processed: " + item;
    }
}
```

### मुख्य बिंदु
- **पूरा होने की प्रतीक्षा**: `CompletableFuture.allOf(...).join()` या `.get()` यह सुनिश्चित करता है कि मुख्य थ्रेड तब तक प्रतीक्षा करता है जब तक सभी टास्क्स समाप्त नहीं हो जाते। चेक्ड एक्सेप्शन्स को हैंडल करने से बचने के लिए `join()` का उपयोग करें; यदि कोई टास्क विफल होता है तो यह `CompletionException` थ्रो करता है।
- **एक्सेप्शन हैंडलिंग**: यदि आपको एक्सेप्शन्स को हैंडल करने की आवश्यकता है तो `.join()` या `.get()` कॉल को ट्राई-कैच ब्लॉक में लपेटें:

```java
try {
    allFutures.get();
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    // इंटरप्शन को हैंडल करें
} catch (ExecutionException e) {
    // टास्क विफलताओं को हैंडल करें
    e.printStackTrace();
}
```

- **थ्रेड पूल कॉन्फ़िगरेशन**: अपने वर्कलोड के आधार पर थ्रेड पूल के आकार को समायोजित करें। I/O-बाउंड टास्क्स (जैसे, डेटाबेस कॉल, API रिक्वेस्ट्स) के लिए, एक बड़ा पूल (जैसे, 5-10 थ्रेड्स) ठीक है। CPU-बाउंड टास्क्स के लिए, CPU कोर की संख्या से मेल खाएं (जैसे, `Runtime.getRuntime().availableProcessors()`)।
- **परिणाम क्रम**: परिणाम इनपुट सूची के क्रम को बनाए रखते हैं क्योंकि फ्यूचर्स लूप के समान क्रम में एकत्र किए जाते हैं।

### कौन सा दृष्टिकोण चुनें?
- **`@Async` का उपयोग करें** यदि आपके टास्क स्वाभाविक रूप से एक Spring सर्विस का हिस्सा हैं और आप चाहते हैं कि Spring थ्रेडिंग का प्रबंधन करे। यह अधिक साफ-सुथरा है और Spring Boot के साथ अच्छी तरह से एकीकृत होता है।
- **`supplyAsync` का उपयोग करें** यदि आपको टास्क निष्पादन पर अधिक नियंत्रण की आवश्यकता है या Spring के async फ्रेमवर्क पर निर्भर नहीं रहना चाहते।

### अंतिम उत्तर
एक Java Spring Boot प्रोजेक्ट में for-loop जॉब के लिए `Promise.all` को दोहराने के लिए, जहाँ आप मल्टीथ्रेडेड निष्पादन के बाद थ्रेड परिणामों का उपयोग करना चाहते हैं, `CompletableFuture` इंस्टेंस की एक सूची के साथ `CompletableFuture.allOf` का उपयोग करें। सादगी के लिए Spring के साथ `@Async` दृष्टिकोण की सिफारिश की जाती है, लेकिन कस्टम एक्सिक्यूटर के साथ `supplyAsync` भी काम करता है। ऊपर दिया गया `@Async` के साथ उदाहरण इसे प्रदर्शित करता है:

- `@Async` मेथड का उपयोग करके for लूप में `CompletableFuture` इंस्टेंस बनाएं।
- सभी टास्क्स की प्रतीक्षा करने के लिए `CompletableFuture.allOf` का उपयोग करें।
- पूरा होने के बाद परिणाम एकत्रित करें और उपयोग करें।

यह सुनिश्चित करता है कि सभी टास्क समवर्ती रूप से चलते हैं, और आप उनके परिणामों को प्रोसेस कर सकते हैं एक बार वे सभी पूरे हो जाएं, जिससे आपकी आवश्यकताओं को प्रभावी ढंग से पूरा किया जाता है।