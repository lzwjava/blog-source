---
audio: false
generated: true
lang: ar
layout: post
title: مزامنة الخيوط في جافا
translated: true
type: note
---

لنغوص في مزامنة الخيوط (Thread Synchronization) في جافا! عندما تصل عدة خيوط إلى موارد مشتركة (مثل المتغيرات، المجموعات، أو الملفات)، تحتاج إلى منع حالات السباق (Race Conditions) - حيث تتداخل الخيوط مع بعضها البعض، مما يؤدي إلى نتائج غير متوقعة. تقدم جافا عدة أدوات لهذا الغرض: `synchronized`، و `Lock`، و `Semaphore`. سأشرح كل أداة، وأعرض أمثلة عليها، وأقارن بينها حتى تتمكن من اختيار الأداة المناسبة لاحتياجاتك.

---

### 1. الكلمة المفتاحية `synchronized`
تضمن الكلمة المفتاحية `synchronized` أن يقوم خيط واحد فقط بتنفيذ كتلة كود أو طريقة في كل مرة. إنها أداة المزامنة الأبسط، وهي مدمجة في نواة جافا.

#### آلية العمل
- تقوم بقفل مراقب (monitor) الكائن (كل كائن في جافا لديه واحد).
- تنتظر الخيوط الأخرى حتى يتم تحرير القفل.

#### مثال: عداد باستخدام `synchronized`
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
- بدون `synchronized`، يمكن أن تتداخل عملية `count++` (قراءة-تعديل-كتابة)، مما يعطي نتيجة أقل من 2000.
- `synchronized` تقفل نسخة الكائن `Counter`، مما يضمن تحديثات ذرية.

#### كتلة متزامنة (Synchronized Block)
يمكنك أيضًا قفل جزء محدد من الكود بدلاً من الطريقة بأكملها:
```java
public void increment() {
    synchronized (this) {
        count++;
    }
}
```
- استخدم كائنًا مختلفًا كقفل إذا أردت تحكمًا أدق:
```java
private final Object lock = new Object();
public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

#### الإيجابيات والسلبيات
- **الإيجابيات**: بسيطة، مدمجة في اللغة، جيدة للاستخدامات الأساسية.
- **سلبيات**: لا مرونة (مثلًا، لا يمكن مقاطعة خيط في حالة انتظار)، تمنع التنفيذ حتى يتم التحرير.

---

### 2. واجهة `Lock` (java.util.concurrent.locks)
توفر واجهة `Lock` (مثل `ReentrantLock`) تحكمًا أكبر من `synchronized`. إنها جزء من حزمة `java.util.concurrent` وتم تقديمها لمعالجة قيود `synchronized`.

#### الميزات الرئيسية
- استدعاءات صريحة `lock()` و `unlock()`.
- تدعم محاولة القفل (try-locks)، المهلات، وقفلاً يمكن مقاطعته.
- خيار الإنصاف (Fairness) (تنتظر الخيوط بالترتيب).

#### مثال: عداد باستخدام `ReentrantLock`
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
            lock.unlock(); // Always unlock in finally
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
- يضمن `try-finally` تحرير القفل حتى في حالة حدوث استثناء.

#### ميزات متقدمة
- **محاولة القفل (Try Lock)**: محاولة غير عاطلة (non-blocking) للحصول على القفل:
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
- **المهلة (Timeout)**: الانتظار لفترة محدودة:
```java
if (lock.tryLock(1, TimeUnit.SECONDS)) { ... }
```
- **قابل للمقاطعة (Interruptible)**: السماح لمقاطعة الخيوط المنتظرة:
```java
lock.lockInterruptibly();
```

#### الإيجابيات والسلبيات
- **الإيجابيات**: مرنة، تدعم الميزات المتقدمة، تحكم صريح.
- **سلبيات**: أكثر تفصيلاً، يتطلب تحريرًا يدويًا للقفل (خطر النسيان).

---

### 3. `Semaphore`
يتحكم `Semaphore` في الوصول إلى مورد من خلال الحفاظ على مجموعة من التصاريح (permits). إنه رائع للحد من التزامن (مثلًا، حد أقصى 5 خيوط يمكنها الوصول إلى مورد).

#### آلية العمل
- تحصل الخيوط على التصاريح باستخدام `acquire()`.
- تطلق التصاريح باستخدام `release()`.
- إذا لم تكن هناك تصاريح متاحة، تنتظر الخيوط.

#### مثال: تحديد عدد اتصالات قاعدة البيانات
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
- يمكن لـ 3 خيوط فقط "الاتصال" في نفس الوقت؛ بينما تنتظر الخيوط الأخرى حتى يتم تحرير تصريح.

#### ميزات متقدمة
- **الإنصاف (Fairness)**: `new Semaphore(3, true)` يضمن ترتيب الأولوية FIFO.
- **محاولة الاكتساب (Try Acquire)**: `semaphore.tryAcquire()` للتحقق بدون عرقلة.

#### الإيجابيات والسلبيات
- **الإيجابيات**: مثالي لمجموعات الموارد، نظام تصاريح مرن.
- **سلبيات**: أكثر تعقيدًا من `synchronized` أو `Lock`، ليس للإقصاء المتبادل البسيط.

---

### الدمج مع `ExecutorService`
إليك كيف تعمل هذه الأدوات مع مجموعة خيوط (thread pool):
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

### مقارنة

| الميزة            | `synchronized`       | `Lock` (ReentrantLock) | `Semaphore`         |
|--------------------|----------------------|------------------------|---------------------|
| سهولة الاستخدام   | عالية                | متوسطة                 | منخفضة             |
| المرونة           | منخفضة               | عالية                  | متوسطة             |
| الدقة             | طريقة/كتلة          | صريح                   | قائم على التصاريح  |
| قابل للمقاطعة     | لا                   | نعم                    | نعم                |
| خيار الإنصاف      | لا                   | نعم                    | نعم                |
| حالة الاستخدام    | الإقصاء المتبادل البسيط | التحكم المتقدم        | تحديد الموارد     |

---

### متى تستخدم ماذا؟
- **`synchronized`**: للإقصاء المتبادل السريع والبسيط (مثل حماية متغير واحد).
- **`Lock`**: عندما تحتاج إلى محاولة قفل، مهلات، أو قابلية المقاطعة (مثل سير العمل المعقد).
- **`Semaphore`**: للحد من الوصول المتزامن إلى مورد (مثل مجموعات الاتصال، تحديد معدل الوصول).