---
audio: false
lang: hi
layout: post
title: Java Multithreading का उपयोग
translated: true
---

चलिए, Java multithreading और `Executor` framework का उपयोग करने के बारे में गहराई से जानते हैं। Multithreading आपके प्रोग्राम को कई टास्क को एक साथ चलाने की अनुमति देता है, जिससे I/O-बाउंड या CPU-इंटेंसिव ऑपरेशंस के लिए प्रदर्शन में सुधार होता है। `Executor` framework ने थ्रेड प्रबंधन को सरल बनाया है, जो निम्न स्तर के थ्रेड निर्माण और हैंडलिंग को छिपा देता है। मैं आपको बेसिक्स के बारे में बताता हूँ, फिर आपको दिखाता हूँ कि `Executor` और संबंधित उपकरणों का उपयोग कैसे करें।

---

### 1. Java में Multithreading के Basics
Java दो प्राथमिक तरीकों से थ्रेड बनाता है:
- **Thread class को extend करें**:
```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start(); // थ्रेड को शुरू करें
    }
}
```
- **Runnable interface को implement करें**:
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
- थ्रेड को शुरू करने के लिए `start()` (नहीं `run()`) को कॉल करें—`run()` केवल वर्तमान थ्रेड में कोड को चलाता है।

---

### 2. `Executor` का उपयोग क्यों करें?
थ्रेड को मैनुअल रूप से बनाना सरल मामलों के लिए काम करता है, लेकिन कई टास्कों को प्रबंधित करने के लिए असमर्थ है (उदाहरण के लिए, थ्रेड ओवरहेड, संसाधन की कमी)। `Executor` framework (Java 5 में `java.util.concurrent` के तहत पेश किया गया) एक थ्रेड पूल और टास्क प्रबंधन प्रणाली प्रदान करता है, जिससे multithreading साफ और अधिक विस्तारशील बन जाता है।

---

### 3. `ExecutorService` का उपयोग
`ExecutorService` interface (एक `Executor` subinterface) go-to tool है। यहाँ इसका उपयोग करने का तरीका है:

#### Step 1: एक ExecutorService बनाएं
`Executors` utility class का उपयोग करके एक थ्रेड पूल बनाएं:
```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        // 4 थ्रेडों वाला फिक्स्ड थ्रेड पूल
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // टास्क सबमिट करें
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                System.out.println("Task executed by: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000); // काम का सिमुलेशन
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        // Executor को बंद करें
        executor.shutdown(); // नए टास्कों को रोकता है, मौजूदा टास्कों को पूरा होने तक इंतजार करता है
    }
}
```
- `newFixedThreadPool(4)` 4 थ्रेडों वाला पूल बनाता है। अतिरिक्त टास्क क्यू में इंतजार करते हैं।
- `submit()` `Runnable` या `Callable` टास्कों को स्वीकार करता है (`Callable` परिणाम देता है).

#### Common Executor Types
- `Executors.newSingleThreadExecutor()`: एक थ्रेड, टास्कों को क्रमिक रूप से प्रोसेस करता है।
- `Executors.newCachedThreadPool()`: आवश्यकता के अनुसार थ्रेड बनाता है, खाली थ्रेडों को पुनः उपयोग करता है (छोटे समय के लिए अच्छे हैं).
- `Executors.newScheduledThreadPool(n)`: टास्कों को समय के साथ या आवृत्ति के साथ शेड्यूल करने के लिए।

---

### 4. `Callable` और `Future` के साथ परिणामों का प्रबंधन
अगर आपको टास्क परिणाम चाहिए, तो `Callable` का उपयोग `Runnable` के बजाय करें:
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

        // टास्क चलने के दौरान अन्य काम करें
        System.out.println("Task submitted...");

        // परिणाम प्राप्त करें (टास्क पूरा होने तक ब्लॉक करता है)
        Integer result = future.get();
        System.out.println("Result: " + result);

        executor.shutdown();
    }
}
```
- `Future.get()` परिणाम प्राप्त करता है, टास्क पूरा होने तक ब्लॉक करता है।
- `future.isDone()` को उपयोग करके ब्लॉक किए बिना पूरा होने की जांच करें।

---

### 5. उन्नत: थ्रेड पूल ट्यूनिंग
वास्तविक दुनिया के एप्लिकेशन के लिए, आपको एक कस्टम `ThreadPoolExecutor` चाहिये हो सकता है:
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // कस्टम थ्रेड पूल: 2-4 थ्रेड, क्यू क्षमता 10
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2, // Core pool size
            4, // Max pool size
            60L, // Idle thread timeout
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(10) // Task queue
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
- Core size (2): जीवित रखे जाने वाले न्यूनतम थ्रेड।
- Max size (4): क्यू भरा हुआ हो तो अधिकतम थ्रेड।
- क्यू: जब सभी थ्रेड व्यस्त हैं तो टास्कों को रखता है।

---

### 6. बेस्ट प्रैक्टिस
- **सही बंद करें**: संसाधन लीक को रोकने के लिए हमेशा `shutdown()` या `shutdownNow()` को कॉल करें।
- **विच्छेदन का प्रबंधन करें**: लूप में `Thread.currentThread().isInterrupted()` की जांच करें।
- **ओवरलोड से बचें**: बहुत सारे थ्रेड प्रदर्शन को खराब कर सकते हैं—थ्रेड पूल आकार को CPU कोरों के आधार पर ट्यून करें (उदाहरण के लिए, `Runtime.getRuntime().availableProcessors()`).
- `ExecutorService` के साथ `try-finally` का उपयोग करें:
```java
ExecutorService executor = Executors.newFixedThreadPool(4);
try {
    // टास्क सबमिट करें
} finally {
    executor.shutdown();
}
```

---

### Log4j के साथ उदाहरण (सबको जोड़ना)
पहले Log4j सवाल के साथ multithreading को जोड़ना:
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
पहले `log4j2.xml` के साथ, यह टास्क प्रगति को कंसोल और फाइल में लॉग करता है।