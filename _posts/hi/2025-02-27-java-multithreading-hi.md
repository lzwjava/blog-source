---
audio: false
generated: true
lang: hi
layout: post
title: जावा मल्टीथ्रेडिंग
translated: true
type: note
---

आइए Java मल्टीथ्रेडिंग और `Executor` फ्रेमवर्क के प्रभावी उपयोग में गहराई से उतरते हैं। मल्टीथ्रेडिंग आपके प्रोग्राम को एक साथ कई कार्य चलाने की अनुमति देती है, जिससे I/O-बाउंड या CPU-गहन ऑपरेशन्स के प्रदर्शन में सुधार होता है। `Executor` फ्रेमवर्क लो-लेवल थ्रेड निर्माण और हैंडलिंग को अमूर्त बनाकर थ्रेड प्रबंधन को सरल बनाता है। मैं आपको पहले बेसिक्स दिखाऊंगा, फिर `Executor` और संबंधित टूल्स के उपयोग का तरीका बताऊंगा।

---

### 1. Java में मल्टीथ्रेडिंग की मूल बातें
Java थ्रेड बनाने के दो प्राथमिक तरीके प्रदान करती है:
- **`Thread` क्लास को एक्सटेंड करें**:

```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start(); // थ्रेड शुरू करता है
    }
}
```

- **`Runnable` इंटरफेस को इम्प्लीमेंट करें**:

```java
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Runnable running: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start();
    }
}
```

- थ्रेड लॉन्च करने के लिए `start()` को कॉल करें (`run()` नहीं)—`run()` कोड को केवल मौजूदा थ्रेड में चलाता है।

---

### 2. `Executor` का उपयोग क्यों करें?
मैन्युअल रूप से थ्रेड बनाना सरल मामलों के लिए काम करता है, लेकिन कई कार्यों को प्रबंधित करने के लिए यह अक्षम है (जैसे, थ्रेड ओवरहेड, संसाधन समाप्ति)। `Executor` फ्रेमवर्क (Java 5 में `java.util.concurrent` के तहत पेश किया गया) एक थ्रेड पूल और टास्क मैनेजमेंट सिस्टम प्रदान करता है, जो मल्टीथ्रेडिंग को साफ़ और अधिक स्केलेबल बनाता है।

---

### 3. `ExecutorService` का उपयोग
`ExecutorService` इंटरफेस (`Executor` का एक सबइंटरफेस) मुख्य टूल है। इसे उपयोग करने का तरीका यहां बताया गया है:

#### चरण 1: एक ExecutorService बनाएँ
थ्रेड पूल बनाने के लिए `Executors` यूटिलिटी क्लास का उपयोग करें:
```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        // 4 थ्रेड्स वाला फिक्स्ड थ्रेड पूल
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // टास्क सबमिट करें
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                System.out.println("Task executed by: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000); // कार्य का अनुकरण करें
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        // एक्जीक्यूटर को शट डाउन करें
        executor.shutdown(); // नए टास्क को रोकता है, मौजूदा टास्क के खत्म होने का इंतजार करता है
    }
}
```
- `newFixedThreadPool(4)` 4 थ्रेड्स वाला एक पूल बनाता है। अतिरिक्त टास्क एक कतार में इंतजार करते हैं।
- `submit()` `Runnable` या `Callable` टास्क स्वीकार करता है (`Callable` एक परिणाम लौटाता है)।

#### सामान्य Executor प्रकार
- `Executors.newSingleThreadExecutor()`: एक थ्रेड, टास्क को क्रमिक रूप से प्रोसेस करता है।
- `Executors.newCachedThreadPool()`: आवश्यकतानुसार थ्रेड बनाता है, निष्क्रिय थ्रेड्स का पुन: उपयोग करता है (छोटे समय वाले टास्क के लिए अच्छा)।
- `Executors.newScheduledThreadPool(n)`: विलंब या आवधिकता के साथ टास्क शेड्यूल करने के लिए।

---

### 4. `Callable` और `Future` के साथ परिणामों को हैंडल करना
यदि आपको टास्क के परिणाम चाहिए, तो `Runnable` के बजाय `Callable` का उपयोग करें:
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // एक Callable टास्क सबमिट करें
        Future<Integer> future = executor.submit(() -> {
            Thread.sleep(1000);
            return 42;
        });

        // टास्क के चलते समय अन्य कार्य करें
        System.out.println("Task submitted...");

        // परिणाम प्राप्त करें (पूरा होने तक ब्लॉक करता है)
        Integer result = future.get();
        System.out.println("Result: " + result);

        executor.shutdown();
    }
}
```
- `Future.get()` परिणाम प्राप्त करता है, यदि टास्क पूरा नहीं हुआ है तो ब्लॉक करता है।
- बिना ब्लॉक किए पूर्णता की जांच के लिए `future.isDone()` का उपयोग करें।

---

### 5. एडवांस्ड: थ्रेड पूल ट्यूनिंग
रियल-वर्ल्ड ऐप्स के लिए, आप एक कस्टम `ThreadPoolExecutor` चाह सकते हैं:
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // कस्टम थ्रेड पूल: 2-4 थ्रेड्स, 10 की कतार क्षमता
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2, // कोर पूल आकार
            4, // अधिकतम पूल आकार
            60L, // निष्क्रिय थ्रेड टाइमआउट
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(10) // टास्क कतार
        );

        for (int i = 0; i < 15; i++) {
            executor.execute(() -> {
                System.out.println("Task by: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        executor.shutdown();
    }
}
```
- कोर आकार (2): न्यूनतम थ्रेड जीवित रखे जाते हैं।
- अधिकतम आकार (4): यदि कतार भरी हुई है तो अधिकतम थ्रेड।
- कतार: सभी थ्रेड्स व्यस्त होने पर टास्क रखती है।

---

### 6. सर्वोत्तम अभ्यास
- **उचित रूप से शटडाउन करें**: संसाधन लीक से बचने के लिए हमेशा `shutdown()` या `shutdownNow()` को कॉल करें।
- **इंटरप्शन को हैंडल करें**: लूप्स में `Thread.currentThread().isInterrupted()` की जांच करें।
- **ओवरलोडिंग से बचें**: बहुत अधिक थ्रेड प्रदर्शन को खराब कर सकते हैं—CPU कोर के आधार पर पूल आकार को ट्यून करें (जैसे, `Runtime.getRuntime().availableProcessors()`)।
- **`ExecutorService` के साथ `try-finally` का उपयोग करें**:
```java
ExecutorService executor = Executors.newFixedThreadPool(4);
try {
    // टास्क सबमिट करें
} finally {
    executor.shutdown();
}
```

---

### Log4j के साथ उदाहरण (सबको एक साथ जोड़ना)
मल्टीथ्रेडिंग को आपके पिछले Log4j प्रश्न के साथ जोड़ना:
```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import java.util.concurrent.*;

public class Main {
    private static final Logger logger = LogManager.getLogger(Main.class);

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (int i = 0; i < 5; i++) {
            final int taskId = i;
            executor.submit(() -> {
                logger.info("Task {} started by {}", taskId, Thread.currentThread().getName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    logger.error("Task {} interrupted", taskId, e);
                    Thread.currentThread().interrupt();
                }
                logger.info("Task {} completed", taskId);
            });
        }

        executor.shutdown();
    }
}
```
पहले वाले `log4j2.xml` के साथ, यह टास्क प्रगति को कंसोल और फाइल में लॉग करता है।