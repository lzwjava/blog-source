---
audio: true
lang: hi
layout: post
title: Thread Synchronization in Java का अनुवाद
translated: true
---

चलिए, जावा में थ्रेड सिंक्रोनाइजेशन में डाइव करें! जब कई थ्रेड शेयर्ड रिसोर्सेस (जैसे वेरिएबल्स, कलेक्शंस, या फाइल्स) को एक साथ एक्सेस करते हैं, तो आपको रेस कंडीशन को रोकने की जरूरत होती है—जहां थ्रेड एक दूसरे के साथ हस्तक्षेप करते हैं, जिससे अप्रत्याशित परिणाम निकलते हैं। जावा कई टूल्स प्रदान करता है: `synchronized`, `Lock`, और `Semaphore`. मैं प्रत्येक को समझाऊंगा, उदाहरण दिखाऊंगा, और उन्हें तुलना करूंगा ताकि आप अपने जरूरतों के लिए सही चुन सकें।

---

### 1. `synchronized` Keyword
`synchronized` Keyword एक बार में केवल एक थ्रेड को कोड ब्लॉक या मेथड को एक्सेक्यूट करने की सुनिश्चित करता है। यह जावा के कोर में बिल्ट-इन सिंक्रोनाइजेशन टूल है।

#### कैसे काम करता है
- एक ऑब्जेक्ट के मॉनिटर को लॉक करता है (हर जावा ऑब्जेक्ट के पास एक होता है)।
- अन्य थ्रेड लॉक रिलीज़ होने तक इंतजार करते हैं।

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

        System.out.println("Final count: " + counter.getCount()); // Always 2000
    }
}
```
- बिना `synchronized` के, `count++` (रीड-मॉडिफाई-राइट) ओवरलैप हो सकता है, जिससे 2000 से कम परिणाम निकल सकता है।
- `synchronized` `Counter` इंस्टेंस को लॉक करता है, जिससे एटॉमिक अपडेट सुनिश्चित होते हैं।

#### सिंक्रोनाइज्ड ब्लॉक
आप एक पूरी मेथड के बजाय खास कोड को लॉक भी कर सकते हैं:
```java
public void increment() {
    synchronized (this) {
        count++;
    }
}
```
- अगर आप फाइनर कंट्रोल चाहते हैं, तो अलग ऑब्जेक्ट को लॉक के रूप में उपयोग करें:
```java
private final Object lock = new Object();
public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

#### फायदे और नुकसान
- **फायदे**: सरल, बिल्ट-इन, बेसिक उपयोग के लिए अच्छा।
- **नुकसान**: कोई फ्लेक्सिबिलिटी नहीं (जैसे कि इंतजार कर रहे थ्रेड को इंटररप्ट नहीं कर सकते), रिलीज़ होने तक ब्लॉक होता है।

---

### 2. `Lock` Interface (java.util.concurrent.locks)
`Lock` इंटरफेस (जैसे कि `ReentrantLock`) `synchronized` से अधिक कंट्रोल प्रदान करता है। यह `java.util.concurrent` पैकेज का हिस्सा है और `synchronized` की सीमाओं को दूर करने के लिए पेश किया गया था।

#### मुख्य विशेषताएं
- स्पष्ट `lock()` और `unlock()` कॉल्स।
- ट्राई-लॉक, टाइमआउट, और इंटररप्टेबल लॉकिंग का समर्थन।
- फेयरनेस ऑप्शन (थ्रेड फिफो क्रम में इंतजार करते हैं)।

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
            lock.unlock(); // हमेशा फाइनली में अनलॉक करें
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

        System.out.println("Final count: " + counter.getCount()); // Always 2000
    }
}
```
- `try-finally` सुनिश्चित करता है कि लॉक रिलीज़ होता है चाहे कोई भी एक्सेप्शन हो।

#### एडवांस्ड फीचर्स
- **ट्राई लॉक**: ब्लॉकिंग के बिना लॉक प्राप्त करने का प्रयास:
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
- **टाइमआउट**: सीमित समय के लिए इंतजार करें:
```java
if (lock.tryLock(1, TimeUnit.SECONDS)) { ... }
```
- **इंटररप्टेबल**: इंतजार कर रहे थ्रेड को इंटररप्ट करने की अनुमति:
```java
lock.lockInterruptibly();
```

#### फायदे और नुकसान
- **फायदे**: फ्लेक्सिबल, एडवांस्ड फीचर्स का समर्थन, स्पष्ट कंट्रोल।
- **नुकसान**: अधिक वर्बोज, अनलॉक करने की आवश्यकता (भूलने का खतरा)।

---

### 3. `Semaphore`
एक `Semaphore` एक रिसोर्स को कंट्रोल करता है एक सेट ऑफ पर्मिट्स को बनाए रखते हुए। यह एक रिसोर्स तक एक्सेस को सीमित करने के लिए अच्छा है (जैसे कि 5 थ्रेड एक रिसोर्स तक एक्सेस कर सकते हैं)।

#### कैसे काम करता है
- थ्रेड `acquire()` के साथ पर्मिट्स प्राप्त करते हैं।
- `release()` के साथ पर्मिट्स रिलीज़ करते हैं।
- अगर कोई पर्मिट्स उपलब्ध नहीं हैं, तो थ्रेड इंतजार करते हैं।

#### उदाहरण: डेटाबेस कनेक्शंस सीमित करना
```java
import java.util.concurrent.Semaphore;

class ConnectionPool {
    private final Semaphore semaphore = new Semaphore(3); // Max 3 connections

    public void connect() {
        try {
            semaphore.acquire();
            System.out.println(Thread.currentThread().getName() + " connected");
            Thread.sleep(1000); // Simulate work
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
- केवल 3 थ्रेड एक साथ "कनेक्ट" कर सकते हैं; अन्य इंतजार करते हैं जब तक कि एक पर्मिट रिलीज़ नहीं होता।

#### एडवांस्ड फीचर्स
- **फेयरनेस**: `new Semaphore(3, true)` फिफो क्रम सुनिश्चित करता है।
- **ट्राई अक्वायर**: `semaphore.tryAcquire()` ब्लॉकिंग के बिना चेक करता है।

#### फायदे और नुकसान
- **फायदे**: रिसोर्स पूल के लिए आदर्श, फ्लेक्सिबल पर्मिट सिस्टम।
- **नुकसान**: `synchronized` या `Lock` से अधिक जटिल, सरल म्यूचुअल एक्सक्लूजन के लिए नहीं।

---

### `ExecutorService` के साथ संयोजन
यहां ये टूल्स एक थ्रेड पूल के साथ कैसे काम करते हैं:
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
        System.out.println("Final value: " + resource.getValue()); // Always 1000
    }
}
```

---

### तुलना
| Feature            | `synchronized`       | `Lock` (ReentrantLock) | `Semaphore`         |
|--------------------|----------------------|------------------------|---------------------|
| Ease of Use        | High                | Medium                | Low                |
| Flexibility        | Low                 | High                  | Medium             |
| Granularity        | Method/block        | Explicit              | Permit-based       |
| Interruptible      | No                  | Yes                   | Yes                |
| Fairness Option    | No                  | Yes                   | Yes                |
| Use Case           | Simple mutual exclusion | Advanced control | Resource limiting |

---

### कब क्या उपयोग करें?
- **`synchronized`**: तेज़, सरल म्यूचुअल एक्सक्लूजन (जैसे कि एक वेरिएबल को संरक्षित करना)।
- **`Lock`**: ट्राई-लॉक, टाइमआउट, या इंटररप्टेबिलिटी की जरूरत (जैसे कि जटिल वर्कफ्लो)।
- **`Semaphore`**: एक रिसोर्स तक एक्सेस को सीमित करना (जैसे कि कनेक्शन पूल, रेट लिमिटिंग)।