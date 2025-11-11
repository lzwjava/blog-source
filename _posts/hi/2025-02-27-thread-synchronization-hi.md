---
audio: false
generated: true
lang: hi
layout: post
title: जावा में थ्रेड सिंक्रोनाइज़ेशन
translated: true
type: note
---

आइए Java में thread synchronization के बारे में जानें! जब कई threads साझा संसाधनों (जैसे variables, collections, या files) तक पहुंचते हैं, तो आपको race conditions को रोकने की आवश्यकता होती है—जहां threads एक-दूसरे के साथ हस्तक्षेप करते हैं, जिससे अप्रत्याशित परिणाम सामने आते हैं। Java इसके लिए कई टूल प्रदान करता है: `synchronized`, `Lock`, और `Semaphore`। मैं प्रत्येक को समझाऊंगा, उदाहरण दिखाऊंगा, और उनकी तुलना करूंगा ताकि आप अपनी आवश्यकताओं के लिए सही चुन सकें।

---

### 1. `synchronized` कीवर्ड
`synchronized` कीवर्ड सुनिश्चित करता है कि एक समय में केवल एक thread कोड के एक ब्लॉक या method को execute कर सकता है। यह Java के core में बना सबसे सरल synchronization टूल है।

#### यह कैसे काम करता है
- किसी object के monitor को लॉक करता है (हर Java object का एक monitor होता है)।
- अन्य threads तब तक प्रतीक्षा करते हैं जब तक लॉक release नहीं हो जाता।

#### उदाहरण: `synchronized` के साथ काउंटर
```java
class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        };

        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Final count: " + counter.getCount()); // हमेशा 2000
    }
}
```
- `synchronized` के बिना, `count++` (read-modify-write) ओवरलैप हो सकता है, जिससे परिणाम 2000 से कम मिल सकता है।
- `synchronized` `Counter` instance को लॉक कर देता है, जिससे atomic updates सुनिश्चित होते हैं।

#### Synchronized ब्लॉक
आप पूरी method के बजाय specific code को भी लॉक कर सकते हैं:
```java
public void increment() {
    synchronized (this) {
        count++;
    }
}
```
- बेहतर नियंत्रण के लिए एक अलग object को लॉक के रूप में उपयोग करें:
```java
private final Object lock = new Object();
public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

#### फायदे और नुकसान
- **फायदे**: सरल, built-in, basic use के लिए अच्छा।
- **नुकसान**: लचीलापन नहीं (जैसे, प्रतीक्षारत thread को interrupt नहीं कर सकते), release होने तक block करता है।

---

### 2. `Lock` इंटरफेस (java.util.concurrent.locks)
`Lock` इंटरफेस (जैसे, `ReentrantLock`) `synchronized` की तुलना में अधिक नियंत्रण प्रदान करता है। यह `java.util.concurrent` पैकेज का हिस्सा है और इसे `synchronized` की सीमाओं को दूर करने के लिए पेश किया गया था।

#### मुख्य विशेषताएं
- स्पष्ट `lock()` और `unlock()` कॉल।
- try-locks, timeouts, और interruptible locking का समर्थन करता है।
- Fairness विकल्प (threads क्रम में प्रतीक्षा करते हैं)।

#### उदाहरण: `ReentrantLock` के साथ काउंटर
```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class Counter {
    private int count = 0;
    private final Lock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock(); // हमेशा finally में unlock करें
        }
    }

    public int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        };

        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Final count: " + counter.getCount()); // हमेशा 2000
    }
}
```
- `try-finally` सुनिश्चित करता है कि exception आने पर भी lock release हो जाए।

#### उन्नत विशेषताएं
- **Try Lock**: लॉक प्राप्त करने का non-blocking प्रयास:
```java
if (lock.tryLock()) {
    try {
        count++;
    } finally {
        lock.unlock();
    }
} else {
    System.out.println("Couldn’t acquire lock");
}
```
- **Timeout**: सीमित समय के लिए प्रतीक्षा करें:
```java
if (lock.tryLock(1, TimeUnit.SECONDS)) { ... }
```
- **Interruptible**: प्रतीक्षारत threads को interrupt होने की अनुमति दें:
```java
lock.lockInterruptibly();
```

#### फायदे और नुकसान
- **फायदे**: लचीला, उन्नत विशेषताओं का समर्थन, स्पष्ट नियंत्रण।
- **नुकसान**: अधिक verbose, manual unlock आवश्यक (भूलने का जोखिम)।

---

### 3. `Semaphore`
एक `Semaphore` permits के एक सेट को बनाए रखकर किसी संसाधन तक पहुंच को नियंत्रित करता है। यह concurrency को सीमित करने (जैसे, अधिकतम 5 threads किसी संसाधन तक पहुंच सकते हैं) के लिए बहुत अच्छा है।

#### यह कैसे काम करता है
- Thread `acquire()` के साथ permits प्राप्त करते हैं।
- `release()` के साथ permits जारी करते हैं।
- यदि कोई permit उपलब्ध नहीं है, तो threads प्रतीक्षा करते हैं।

#### उदाहरण: डेटाबेस कनेक्शन सीमित करना
```java
import java.util.concurrent.Semaphore;

class ConnectionPool {
    private final Semaphore semaphore = new Semaphore(3); // अधिकतम 3 कनेक्शन

    public void connect() {
        try {
            semaphore.acquire();
            System.out.println(Thread.currentThread().getName() + " connected");
            Thread.sleep(1000); // कार्य का अनुकरण
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            semaphore.release();
            System.out.println(Thread.currentThread().getName() + " disconnected");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        ConnectionPool pool = new ConnectionPool();
        Runnable task = () -> pool.connect();

        Thread[] threads = new Thread[10];
        for (int i = 0; i < 10; i++) {
            threads[i] = new Thread(task, "Thread-" + i);
            threads[i].start();
        }
    }
}
```
- एक समय में केवल 3 threads "connect" कर सकते हैं; अन्य तब तक प्रतीक्षा करते हैं जब तक कोई permit release नहीं हो जाती।

#### उन्नत विशेषताएं
- **Fairness**: `new Semaphore(3, true)` FIFO क्रम सुनिश्चित करता है।
- **Try Acquire**: `semaphore.tryAcquire()` बिना block किए जांच करता है।

#### फायदे और नुकसान
- **फायदे**: संसाधन पूल के लिए आदर्श, लचीली permit प्रणाली।
- **नुकसान**: `synchronized` या `Lock` की तुलना में अधिक जटिल, सरल mutual exclusion के लिए नहीं।

---

### `ExecutorService` के साथ संयोजन
यहां बताया गया है कि ये टूल thread pool के साथ कैसे काम करते हैं:
```java
import java.util.concurrent.*;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class SharedResource {
    private int value = 0;
    private final Lock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try {
            value++;
        } finally {
            lock.unlock();
        }
    }

    public int getValue() {
        return value;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        SharedResource resource = new SharedResource();
        ExecutorService executor = Executors.newFixedThreadPool(4);

        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                for (int j = 0; j < 100; j++) {
                    resource.increment();
                }
            });
        }

        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
        System.out.println("Final value: " + resource.getValue()); // हमेशा 1000
    }
}
```

---

### तुलना

| विशेषता            | `synchronized`       | `Lock` (ReentrantLock) | `Semaphore`         |
|--------------------|----------------------|------------------------|---------------------|
| उपयोग में आसानी    | उच्च                | मध्यम                | निम्न                |
| लचीलापन           | निम्न                 | उच्च                  | मध्यम             |
| सूक्ष्मता          | method/block        | स्पष्ट              | permit-आधारित       |
| Interruptible      | नहीं                  | हाँ                   | हाँ                |
| Fairness विकल्प    | नहीं                  | हाँ                   | हाँ                |
| उपयोग का मामला     | सरल mutual exclusion | उन्नत नियंत्रण | संसाधन सीमित करना |

---

### क्या कब उपयोग करें?
- **`synchronized`**: त्वरित, सरल mutual exclusion (जैसे, एकल variable की सुरक्षा)।
- **`Lock`**: try-locks, timeouts, या interruptibility की आवश्यकता होने पर (जैसे, जटिल वर्कफ़्लो)।
- **`Semaphore`**: किसी संसाधन तक concurrent access सीमित करना (जैसे, connection pools, rate limiting)।