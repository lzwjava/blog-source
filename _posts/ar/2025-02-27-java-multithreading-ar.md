---
audio: false
generated: true
lang: ar
layout: post
title: برمجة الخيوط المتعددة في جافا
translated: true
type: note
---

دعنا نتعمق في تعدد المسارات (multithreading) في جافا وكيفية استخدام إطار عمل `Executor` بشكل فعال. يسمح تعدد المسارات لبرنامجك بتشغيل مهام متعددة في وقت واحد، مما يحسن الأداء في العمليات المكثفة للإدخال/الإخراج (I/O-bound) أو العمليات المكثفة لوحدة المعالجة المركزية (CPU-intensive). يبسط إطار عمل `Executor` إدارة المسارات من خلال تجريد إنشاء المسارات ومعالجتها على المستوى المنخفض. سأرشدك خلال الأساسيات، ثم سأريك كيفية استخدام `Executor` والأدوات المرتبطة به.

---

### 1. أساسيات تعدد المسارات في جافا
توفر جافا طريقتين أساسيتين لإنشاء مسارات:
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
        thread.start(); // يبدأ المسار
    }
}
```

- **تنفيذ واجهة `Runnable`**:

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

- استدعِ `start()` (وليس `run()`) لبدء المسار — `run()` ينفذ الكود فقط في المسار الحالي.

---

### 2. لماذا نستخدم `Executor`؟
إنشاء المسارات يدويًا يعمل في الحالات البسيطة، لكنه غير فعال لإدارة العديد من المهام (مثل عبء المسار، استنزاف الموارد). يوفر إطار عمل `Executor` (الذي تم تقديمه في جافا 5 تحت `java.util.concurrent`) مجموعة مسارات (thread pool) ونظام إدارة للمهام، مما يجعل تعدد المسارات أكثر نظافة وقابلية للتوسع.

---

### 3. استخدام `ExecutorService`
واجهة `ExecutorService` (واجهة فرعية لـ `Executor`) هي الأداة الأساسية. إليك كيفية استخدامها:

#### الخطوة 1: إنشاء ExecutorService
استخدم فئة الأداة المساعدة `Executors` لإنشاء مجموعة مسارات:
```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        // مجموعة مسارات ثابتة تحتوي على 4 مسارات
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // إرسال المهام
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                System.out.println("Task executed by: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000); // محاكاة العمل
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        // إيقاف المنفذ
        executor.shutdown(); // يمنع المهام الجديدة، وينتظر انتهاء المهام الحالية
    }
}
```
- `newFixedThreadPool(4)` ينشئ مجموعة تحتوي على 4 مسارات. تنتظر المهام الزائدة في قائمة انتظار.
- `submit()` تقبل مهام `Runnable` أو `Callable` (ترجع `Callable` نتيجة).

#### أنواع المنفذين الشائعة
- `Executors.newSingleThreadExecutor()`: مسار واحد، يعالج المهام بالتسلسل.
- `Executors.newCachedThreadPool()`: ينشئ مسارات حسب الحاجة، ويعيد استخدام المسارات الخاملة (جيد للمهام قصيرة العمر).
- `Executors.newScheduledThreadPool(n)`: لجدولة المهام مع تأخيرات أو دورية.

---

### 4. التعامل مع النتائج باستخدام `Callable` و `Future`
إذا كنت بحاجة إلى نتائج المهمة، استخدم `Callable` بدلاً من `Runnable`:
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // إرسال مهمة Callable
        Future<Integer> future = executor.submit(() -> {
            Thread.sleep(1000);
            return 42;
        });

        // القيام بعمل آخر أثناء تشغيل المهمة
        System.out.println("Task submitted...");

        // الحصول على النتيجة (يحجب حتى الانتهاء)
        Integer result = future.get();
        System.out.println("Result: " + result);

        executor.shutdown();
    }
}
```
- `Future.get()` يسترجع النتيجة، ويحجب إذا لم تكن المهمة قد انتهت.
- استخدم `future.isDone()` للتحقق من الاكتمال بدون حجب.

---

### 5. متقدم: ضبط مجموعة المسارات (Thread Pool Tuning)
لتطبيقات العالم الحقيقي، قد ترغب في `ThreadPoolExecutor` مخصص:
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // مجموعة مسارات مخصصة: 2-4 مسارات، سعة قائمة الانتظار 10
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2, // حجم المجموعة الأساسي
            4, // الحد الأقصى لحجم المجموعة
            60L, // وقت انتهاء المسار الخامل
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(10) // قائمة انتظار المهام
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
- الحجم الأساسي (2): الحد الأدنى للمسارات التي تبقى نشطة.
- الحد الأقصى للحجم (4): الحد الأقصى للمسارات إذا كانت قائمة الانتظار ممتلئة.
- قائمة الانتظار: تحتفظ بالمهام عندما تكون جميع المسارات مشغولة.

---

### 6. أفضل الممارسات
- **الإيقاف بشكل صحيح**: استدعِ دائمًا `shutdown()` أو `shutdownNow()` لتجنب تسرب الموارد.
- **معالجة المقاطعات**: تحقق من `Thread.currentThread().isInterrupted()` في الحلقات.
- **تجنب التحميل الزائد**: يمكن لعدد كبير جدًا من المسارات أن يقلل الأداء — اضبط حجم المجموعة بناءً على نوى وحدة المعالجة المركزية (مثل `Runtime.getRuntime().availableProcessors()`).
- **استخدم `try-finally` مع `ExecutorService`**:
```java
ExecutorService executor = Executors.newFixedThreadPool(4);
try {
    // إرسال المهام
} finally {
    executor.shutdown();
}
```

---

### مثال مع Log4j (ربط كل شيء معًا)
الجمع بين تعدد المسارات وسؤالك السابق عن Log4j:
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
مع ملف `log4j2.xml` من السابق، يقوم هذا بتسجيل تقدم المهمة إلى وحدة التحكم والملف.