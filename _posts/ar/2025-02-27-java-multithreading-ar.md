---
audio: false
lang: ar
layout: post
title: Java Multithreading
translated: true
---

دعونا نغوص في المتعدد التسلسل في جاڤا وكيفية استخدام إطار `Executor` بشكل فعال. يسمح المتعدد التسلسل لبرنامجك بتشغيل عدة مهام بشكل متزامن، مما يحسن الأداء للعمليات المعتمدة على الإدخال/الخروج أو المعتمدة على وحدة المعالجة المركزية. يوفر إطار `Executor` تسيير الخيوط بشكل أبسط من خلال إخفاء إنشاء الخيوط وتسييرها على مستوى منخفض. سأرشدك عبر الأساسيات، ثم سأريك كيفية استخدام `Executor` والأدوات ذات الصلة.

---

### 1. أساسيات المتعدد التسلسل في جاڤا
يوفر جاڤا طريقتين رئيسيتين لإنشاء الخيوط:
- **توسيع فئة `Thread`**:
```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start(); // يبدأ الخيط
    }
}
```
- **تطبيق واجهة `Runnable`**:
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
- استدعاء `start()` (لا `run()`) لإطلاق الخيط—`run()` فقط ينفذ الكود في الخيط الحالي.

---

### 2. لماذا استخدام `Executor`؟
إنشاء الخيوط يدويًا يعمل في الحالات البسيطة، ولكن هو غير فعال في إدارة العديد من المهام (مثل: تكلفة الخيط، استنفاد الموارد). يوفر إطار `Executor` (مقدمة في جاڤا 5 تحت `java.util.concurrent`) مجموعة خيوط ومجموعة إدارة المهام، مما يجعل المتعدد التسلسل أكثر نظافة وأكثر قابلية للتوسيع.

---

### 3. استخدام `ExecutorService`
هي الواجهة `ExecutorService` (واجهة فرعية من `Executor`) هي الأداة الأساسية. إليك كيفية استخدامها:

#### الخطوة 1: إنشاء `ExecutorService`
استخدم فئة `Executors` المساعدة لإنشاء مجموعة خيوط:
```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        // مجموعة خيوط ثابتة مع 4 خيوط
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // تقديم المهام
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                System.out.println("Task executed by: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000); // تقمص العمل
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        // إيقاف تشغيل `executor`
        executor.shutdown(); // يمنع المهام الجديدة، ينتظر انتهاء المهام الحالية
    }
}
```
- `newFixedThreadPool(4)` يخلق مجموعة مع 4 خيوط. المهام الزائدة تنتظر في قائمة الانتظار.
- `submit()` يقبل المهام `Runnable` أو `Callable` (`Callable` يعيد نتيجة).

#### أنواع `Executor` الشائعة
- `Executors.newSingleThreadExecutor()`: خيط واحد، يعالج المهام بشكل تسلسلي.
- `Executors.newCachedThreadPool()`: يخلق الخيوط حسب الحاجة، يعيد استخدام الخيوط الفارغة (جيد للمهام قصيرة العمر).
- `Executors.newScheduledThreadPool(n)`: لتدبير المهام مع تأخير أو دورية.

---

### 4. معالجة النتائج مع `Callable` و `Future`
إذا كنت تحتاج إلى نتائج المهام، استخدم `Callable` بدلاً من `Runnable`:
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // تقديم مهمة `Callable`
        Future<Integer> future = executor.submit(() -> {
            Thread.sleep(1000);
            return 42;
        });

        // القيام بعمل آخر أثناء تنفيذ المهمة
        System.out.println("Task submitted...");

        // الحصول على النتيجة (يتوقف حتى تنتهي المهمة)
        Integer result = future.get();
        System.out.println("Result: " + result);

        executor.shutdown();
    }
}
```
- `Future.get()` يحصل على النتيجة، يتوقف إذا لم تنتهي المهمة.
- استخدم `future.isDone()` لتحقق من الانتهاء دون توقف.

---

### 5. متقدم: ضبط مجموعة الخيوط
للتطبيقات الحقيقية، قد ترغب في مجموعة `ThreadPoolExecutor` مخصصة:
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // مجموعة خيوط مخصصة: 2-4 خيوط، سعة قائمة الانتظار 10
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2, // حجم مجموعة النواة
            4, // حجم مجموعة القصوى
            60L, // وقت انتظار الخيط الفارغ
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(10) // قائمة المهام
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
- حجم النواة (2): عدد الخيوط التي يتم الاحتفاظ بها على قيد الحياة.
- حجم القصوى (4): عدد الخيوط القصوى إذا كانت القائمة ممتلئة.
- القائمة: تحتفظ بالمهام عندما تكون جميع الخيوط مشغولة.

---

### 6. أفضل الممارسات
- **إيقاف التشغيل بشكل صحيح**: دائمًا استدعاء `shutdown()` أو `shutdownNow()` لمنع تسرب الموارد.
- **معالجة التقطيعات**: تحقق من `Thread.currentThread().isInterrupted()` في الدوال.
- **تجنب التحميل الزائد**: الكثير من الخيوط يمكن أن يضر بالأداء—ضبط حجم المجموعة بناءً على وحدات المعالجة المركزية (مثل: `Runtime.getRuntime().availableProcessors()`).
- **استخدام `try-finally` مع `ExecutorService`**:
```java
ExecutorService executor = Executors.newFixedThreadPool(4);
try {
    // تقديم المهام
} finally {
    executor.shutdown();
}
```

---

### مثال مع Log4j (ربطها معًا)
مزج المتعدد التسلسل مع سؤالك السابق حول Log4j:
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
مع `log4j2.xml` من السابق، هذا يسجل تقدم المهمة إلى الشاشة والملف.