---
audio: true
lang: ar
layout: post
title: تسجيل الخيوط في جاڤا
translated: true
---

دعونا نغوص في موضوع تزامن الخيوط في جافا! عندما يتفاعل عدة خيوط مع الموارد المشتركة (مثل المتغيرات، المجموعات، أو الملفات)، عليك منع حالات السباق - حيث تتداخل الخيوط مع بعضها البعض، مما يؤدي إلى نتائج غير متوقعة. يوفر جافا عدة أدوات لهذا الغرض: `synchronized`، `Lock`، و `Semaphore`. سأشرح كل منها، وأعرض أمثلة، وأقارن بينها حتى يمكنك اختيار الأفضل حسب احتياجاتك.

---

### 1. كلمة `synchronized`
تضمن كلمة `synchronized` أن فقط خيط واحد يمكن أن ينفذ كتلة من الكود أو طريقة في نفس الوقت. إنها أداة التزامن الأبسط، مبنية في قلب جافا.

#### كيفية عملها
- تقفل مراقب كائن (كل كائن جافا لديه مراقب).
- تنتظر الخيوط الأخرى حتى يتم إفراج عن القفل.

#### مثال: عداد مع `synchronized`
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
- بدون `synchronized`، قد يتداخل `count++` (قراءة-تعديل-كتابة)، مما يعطي نتيجة أقل من 2000.
- `synchronized` يقفل `Counter`، مما يضمن تحديثات ذرية.

#### كتلة `synchronized`
يمكنك أيضًا قفل كود محدد بدلاً من طريقة كاملة:
```java
public void increment() {
    synchronized (this) {
        count++;
    }
}
```
- استخدم كائنًا مختلفًا كقفل إذا كنت تريد تحكمًا أكثر دقة:
```java
private final Object lock = new Object();
public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

#### المزايا والعيوب
- **المزايا**: بسيط، مبني، جيد للاستخدام الأساسي.
- **العيوب**: لا يوجد مرونة (مثل عدم القدرة على إيقاف خيط في انتظار)، يظل مقفلًا حتى يتم إفراج عنه.

---

### 2. واجهة `Lock` (java.util.concurrent.locks)
توفر واجهة `Lock` (مثل `ReentrantLock`) أكثر من التحكم من `synchronized`. إنها جزء من حزمة `java.util.concurrent` و تم تقديمها لتحل مشاكل `synchronized`.

#### الميزات الرئيسية
- دعوات `lock()` و `unlock()` صريحة.
- يدعم قفل المحاولة، الأوقات الزمنية، وقفل القابل للإيقاف.
- خيار العدل (الخيوط تنتظر في الترتيب).

#### مثال: عداد مع `ReentrantLock`
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
- `try-finally` يضمن إفراج عن القفل حتى إذا حدث استثناء.

#### الميزات المتقدمة
- **قفل المحاولة**: محاولة غير مقفلة للحصول على القفل:
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
- **الوقت الزمني**: انتظر لفترة محدودة:
```java
if (lock.tryLock(1, TimeUnit.SECONDS)) { ... }
```
- **القابل للإيقاف**: السماح للخيوط في انتظار أن يتم إيقافها:
```java
lock.lockInterruptibly();
```

#### المزايا والعيوب
- **المزايا**: مرن، يدعم الميزات المتقدمة، التحكم الصريح.
- **العيوب**: أكثر تعقيدًا، مطلوب إفراج عن القفل يدويًا (خطر نسيان الإفراج).

---

### 3. `Semaphore`
يسيطر `Semaphore` على الوصول إلى الموارد من خلال الحفاظ على مجموعة من الإذنات. إنه ممتاز للحد من التزامن (مثل أن لا أكثر من 5 خيوط يمكن الوصول إلى الموارد).

#### كيفية عملها
- يحصل الخيوط على الإذنات باستخدام `acquire()`.
- يفرج عن الإذنات باستخدام `release()`.
- إذا لم يكن هناك أي إذنات متاحة، تنتظر الخيوط.

#### مثال: حد من اتصالات قاعدة البيانات
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
- فقط 3 خيوط يمكن "الاتصال" في نفس الوقت؛ تنتظر الخيوط الأخرى حتى يتم إفراج عن الإذن.

#### الميزات المتقدمة
- **العدل**: `new Semaphore(3, true)` يضمن ترتيب FIFO.
- **قفل المحاولة**: `semaphore.tryAcquire()` يحدد دون قفل.

#### المزايا والعيوب
- **المزايا**: مثالي للمجموعات الموارد، نظام الإذنات المرن.
- **العيوب**: أكثر تعقيدًا من `synchronized` أو `Lock`، ليس للاستبعاد المتبادل البسيط.

---

### الجمع مع `ExecutorService`
هكذا تعمل هذه الأدوات مع مجموعة خيوط:
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

### المقارنة
| الميزة            | `synchronized`       | `Lock` (ReentrantLock) | `Semaphore`         |
|--------------------|----------------------|------------------------|---------------------|
| سهولة الاستخدام        | عالية                | متوسطة                | منخفضة                |
| المرونة        | منخفضة                 | عالية                  | متوسطة             |
| الدقة        | طريقة/كتلة        | صريح              | بناءً على الإذن       |
| القابل للإيقاف      | لا                  | نعم                   | نعم                |
| خيار العدل    | لا                  | نعم                   | نعم                |
| حالة الاستخدام           | الاستبعاد المتبادل البسيط | التحكم المتقدم | الحد من الموارد |

---

### متى استخدام ماذا؟
- **`synchronized`**: سريع، استبعاد متبادل بسيط (مثل حماية متغير واحد).
- **`Lock`**: تحتاج إلى قفل المحاولة، الأوقات الزمنية، أو القابل للإيقاف (مثل عمليات العمل المعقدة).
- **`Semaphore`**: الحد من الوصول المتزامن إلى الموارد (مثل مجموعات الإتصالات، الحد من معدل).