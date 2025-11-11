---
audio: false
generated: true
lang: hi
layout: post
title: एग्ज़ीक्यूटर सर्विस और थ्रेड पूल एग्ज़ीक्यूटर की समझ
translated: true
type: note
---

Java में `ExecutorService` के लिए पैरामीटर सेट करने में आपके सिस्टम के संसाधनों (जैसे 8-कोर CPU) और आपके टास्क्स की प्रकृति (उदाहरण के लिए, CPU-बाउंड या I/O-बाउंड) के आधार पर परफॉर्मेंस को ऑप्टिमाइज़ करने के लिए इसके थ्रेड पूल को कॉन्फ़िगर करना शामिल है। नीचे, मैं 8-कोर CPU के लिए `ExecutorService` को कॉन्फ़िगर करने का तरीका समझाऊंगा, जिसमें `ThreadPoolExecutor` जैसे कॉमन इम्प्लीमेंटेशन पर फोकस किया गया है, और आपके यूज़ केस के अनुरूप प्रैक्टिकल उदाहरण दिए जाएंगे।

---

### ExecutorService और ThreadPoolExecutor को समझना

`ExecutorService` इंटरफेस को आमतौर पर `ThreadPoolExecutor` जैसी क्लासेस द्वारा इम्प्लीमेंट किया जाता है, जो थ्रेड पूल पैरामीटर पर फाइन-ग्रेन्ड कंट्रोल की अनुमति देता है। इसे 8-कोर CPU के लिए कॉन्फ़िगर करते समय, आपको निम्नलिखित बातों पर विचार करने की आवश्यकता है:
- **कोर पूल साइज़**: आइडल होने पर भी जीवित रखने के लिए थ्रेड्स की संख्या।
- **मैक्सिमम पूल साइज़**: पूल में अनुमत थ्रेड्स की अधिकतम संख्या।
- **क्यू कैपेसिटी**: निष्पादित होने से पहले टास्क्स को होल्ड करने के लिए टास्क क्यू का आकार।
- **थ्रेड क्रिएशन स्ट्रैटेजी**: थ्रेड्स कैसे बनाए और मैनेज किए जाते हैं।
- **टास्क प्रकार**: चाहे टास्क CPU-बाउंड हों (जैसे, कम्प्यूटेशन) या I/O-बाउंड (जैसे, डेटाबेस कॉल)।

8-कोर CPU के लिए, इष्टतम कॉन्फ़िगरेशन इस बात पर निर्भर करता है कि आपके टास्क CPU-इंटेंसिव हैं या I/O-इंटेंसिव (जैसे आपके वैलिडेशन सिनेरियो में डेटाबेस एक्सेस)।

---

### ThreadPoolExecutor के लिए मुख्य पैरामीटर

यहां बताया गया है कि आप `ThreadPoolExecutor` को कैसे सेट अप कर सकते हैं:

```java
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    corePoolSize,      // जीवित रखने के लिए थ्रेड्स की संख्या
    maximumPoolSize,   // अनुमत थ्रेड्स की अधिकतम संख्या
    keepAliveTime,     // आइडल थ्रेड्स को जीवित रखने का समय (जैसे, 60L)
    TimeUnit.SECONDS,  // keepAliveTime की यूनिट
    workQueue,         // टास्क्स को होल्ड करने के लिए क्यू (जैसे, new LinkedBlockingQueue<>())
    threadFactory,     // वैकल्पिक: कस्टम थ्रेड नेमिंग या प्रायोरिटी
    rejectionHandler   // क्यू भर जाने और मैक्स थ्रेड्स पहुंच जाने पर क्या करें
);
```

#### पैरामीटर ब्रेकडाउन
1. **`corePoolSize`**:
   - हमेशा जीवित रखे जाने वाले थ्रेड्स की न्यूनतम संख्या।
   - CPU-बाउंड टास्क्स के लिए: कोर की संख्या के बराबर सेट करें (जैसे, 8)।
   - I/O-बाउंड टास्क्स के लिए: यह अधिक हो सकता है (जैसे, 16 या अधिक), क्योंकि थ्रेड्स प्रतीक्षा करने में समय बिता सकते हैं।

2. **`maximumPoolSize`**:
   - यदि क्यू भर जाती है तो अनुमत अधिकतम थ्रेड्स।
   - CPU-बाउंड के लिए: अक्सर `corePoolSize` के समान (जैसे, 8)।
   - I/O-बाउंड के लिए: बर्स्ट को हैंडल करने के लिए अधिक (जैसे, 20 या 50)।

3. **`keepAliveTime`**:
   - अतिरिक्त आइडल थ्रेड्स (`corePoolSize` से परे) को समाप्त होने से पहले कितने समय तक जीवित रखा जाता है।
   - उदाहरण: `60L` सेकंड एक सामान्य डिफॉल्ट है।

4. **`workQueue`**:
   - निष्पादित होने की प्रतीक्षा कर रहे टास्क्स के लिए क्यू:
     - `LinkedBlockingQueue`: अनबाउंडेड क्यू (कई मामलों में डिफॉल्ट)।
     - `ArrayBlockingQueue`: बाउंडेड क्यू (जैसे, `new ArrayBlockingQueue<>(100)`)।
     - `SynchronousQueue`: कोई क्यू नहीं; टास्क्स सीधे थ्रेड्स को सौंपे जाते हैं (`Executors.newCachedThreadPool()` में उपयोग किया जाता है)।

5. **`threadFactory`** (वैकल्पिक):
   - थ्रेड क्रिएशन को कस्टमाइज़ करता है (जैसे, डीबगिंग के लिए थ्रेड्स को नाम देना)।
   - डिफॉल्ट: `Executors.defaultThreadFactory()`।

6. **`rejectionHandler`** (वैकल्पिक):
   - जब टास्क `maximumPoolSize` और क्यू कैपेसिटी से अधिक हो जाते हैं तो पॉलिसी:
     - `AbortPolicy` (डिफॉल्ट): `RejectedExecutionException` थ्रो करता है।
     - `CallerRunsPolicy`: टास्क को कॉलिंग थ्रेड में रन करता है।
     - `DiscardPolicy`: टास्क को चुपचाप डिसकार्ड कर देता है।

---

### 8-कोर CPU के लिए कॉन्फ़िगर करना

#### सिनेरियो 1: CPU-बाउंड टास्क्स
यदि आपके टास्क CPU-इंटेंसिव हैं (जैसे, भारी कम्प्यूटेशन), तो आप सिस्टम को ओवरलोड किए बिना थ्रूपुट को अधिकतम करने के लिए थ्रेड काउंट को CPU कोर से मैच करना चाहते हैं।

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createCpuBoundExecutor() {
        int corePoolSize = 8; // 8 कोर से मेल खाता है
        int maximumPoolSize = 8;
        long keepAliveTime = 60L; // 60 सेकंड

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(), // अनबाउंडेड क्यू
            Executors.defaultThreadFactory(),
            new ThreadPoolExecutor.AbortPolicy()
        );
    }
}
```

- **क्यों**: 8 थ्रेड्स 8 कोर का पूरी तरह से उपयोग करते हैं। अधिक थ्रेड्स जोड़ने से कॉन्टेक्स्ट स्विचिंग ओवरहेड होगा, जिससे परफॉर्मेंस कम हो जाएगी।

#### सिनेरियो 2: I/O-बाउंड टास्क्स (जैसे, डेटाबेस वैलिडेशन)
डेटाबेस एक्सेस वाले आपके वैलिडेशन सिनेरियो के लिए, टास्क I/O-बाउंड होते हैं—थ्रेड्स डेटाबेस प्रतिक्रियाओं की प्रतीक्षा करने में समय बिताते हैं। आप कुछ थ्रेड्स के प्रतीक्षा करते समय CPU को व्यस्त रखने के लिए कोर से अधिक थ्रेड्स का उपयोग कर सकते हैं।

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createIoBoundExecutor() {
        int corePoolSize = 16; // I/O-बाउंड टास्क्स के लिए कोर का 2x
        int maximumPoolSize = 20; // कुछ बर्स्ट कैपेसिटी की अनुमति दें
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100), // मेमोरी को सीमित करने के लिए बाउंडेड क्यू
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(), // कस्टम नेमिंग
            new ThreadPoolExecutor.CallerRunsPolicy() // अतिभारित होने पर कॉलर पर फॉलबैक
        );
    }
}
```

- **क्यों**:
  - `corePoolSize = 16`: I/O-बाउंड टास्क्स के लिए एक सामान्य ह्युरिस्टिक `N * 2` है (जहां `N` CPU कोर है), लेकिन आप इसे डेटाबेस कनेक्शन लिमिट और टास्क वेट टाइम के आधार पर ट्यून कर सकते हैं।
  - `maximumPoolSize = 20`: पीक लोड के लिए अतिरिक्त थ्रेड्स की अनुमति देता है।
  - `ArrayBlockingQueue(100)`: क्यू किए गए टास्क्स की अनबाउंडेड ग्रोथ को रोकता है, जिससे मेमोरी इश्यूज से बचा जा सके।
  - `CallerRunsPolicy`: यह सुनिश्चित करता है कि सिस्टम कॉलर के थ्रेड में टास्क चलाकर ओवरलोड के तहत सहजता से डिग्रेड हो।

#### Spring Boot इंटीग्रेशन
Spring Boot एप्लिकेशन में, `ExecutorService` को एक बीन के रूप में परिभाषित करें:

```java
import com.google.common.util.concurrent.ThreadFactoryBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.*;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        int corePoolSize = 16; // वैलिडेशन के लिए I/O-बाउंड धारणा
        int maximumPoolSize = 20;
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100),
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(),
            new ThreadPoolExecutor.CallerRunsPolicy()
        );
    }
}
```

- **नोट**: `ThreadFactoryBuilder` के लिए Guava (`com.google.guava:guava`) को अपनी डिपेंडेंसीज में जोड़ें, या यदि आपको कस्टम नेमिंग की आवश्यकता नहीं है तो `Executors.defaultThreadFactory()` का उपयोग करें।

#### अपने वैलिडेशन सर्विस में इसका उपयोग करना
इसे इंजेक्ट करें और उपयोग करें जैसा कि आपके पिछले उदाहरणों में दिखाया गया है:

```java
@Service
public class ValidationService {
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    // CompletableFuture या ExecutorService लॉजिक में उपयोग करें जैसा पहले दिखाया गया है
}
```

---

### 8-कोर CPU के लिए ट्यूनिंग टिप्स

1. **परफॉर्मेंस मापें**:
   - थ्रेड यूसेज को मॉनिटर करने और `corePoolSize` और `maximumPoolSize` को एडजस्ट करने के लिए प्रोफाइलिंग टूल्स (जैसे, VisualVM) का उपयोग करें।

2. **डेटाबेस लिमिट्स**:
   - यदि नियम डेटाबेस को एक्सेस करते हैं, तो सुनिश्चित करें कि थ्रेड पूल साइज़ आपके कनेक्शन पूल साइज़ (जैसे, HikariCP का `maximumPoolSize`) से अधिक न हो। इन सेटिंग्स को समन्वयित करें।

3. **डायनामिक कैलकुलेशन**:
   - कोर पूल साइज़ को डायनामिक रूप से सेट करने के लिए `Runtime.getRuntime().availableProcessors()` का उपयोग करें:
     ```java
     int cores = Runtime.getRuntime().availableProcessors(); // 8-कोर CPU पर 8 रिटर्न करता है
     int corePoolSize = cores * 2; // I/O-बाउंड टास्क्स के लिए
     ```

4. **प्री-स्टार्ट थ्रेड्स**:
   - सभी कोर थ्रेड्स को प्री-अपफ्रंट इनिशियलाइज़ करने के लिए `executor.prestartAllCoreThreads()` को कॉल करें, जिससे लेज़ी क्रिएशन से बचा जा सके।

---

### निष्कर्ष

डेटाबेस एक्सेस वाले आपके वैलिडेशन नियमों जैसे I/O-बाउंड टास्क्स चलाने वाले 8-कोर CPU के लिए:
- `ThreadPoolExecutor` का उपयोग करें जिसमें `corePoolSize = 16`, `maximumPoolSize = 20`, और एक बाउंडेड क्यू (जैसे, `ArrayBlockingQueue(100)`) हो।
- डिपेंडेंसी इंजेक्शन के लिए इसे एक Spring बीन के रूप में इंटीग्रेट करें।
- प्रोफाइलिंग और डेटाबेस कंस्ट्रेंट्स के आधार पर एडजस्ट करें।

यह सेटअप आपके यूज़ केस के लिए उपयुक्त, समानांतरता, संसाधन उपयोग और सिस्टम स्थिरता को संतुलित करता है। यदि आपको इसे अपने विशिष्ट प्रोजेक्ट में इंटीग्रेट करने में सहायता की आवश्यकता हो तो मुझे बताएं!