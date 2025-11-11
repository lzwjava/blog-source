---
audio: false
generated: true
lang: ar
layout: post
title: تزامن الجافا
translated: true
type: note
---

### النقاط الرئيسية
- تساعد الحزمة `java.util.concurrent` في إدارة مهام متعددة في وقت واحد بلغة Java، مما يجعل البرامج أسرع وأكثر استجابة.
- يبدو من المرجح أن استخدام `ExecutorService` هو طريقة شائعة للتعامل مع السلاسل التنفيذية (Threads)، مما يسمح لك بتشغيل المهام في الخلفية.
- تشير الأبحاث إلى أن المجموعات المتزامنة (Concurrent Collections) مثل `ConcurrentHashMap` هي آمنة للاستخدام في بيئات متعددة السلاسل التنفيذية، مما يضمن إمكانية وصول سلاسل تنفيذية متعددة إلى البيانات بأمان.
- تميل الأدلة نحو استخدام أدوات المزامنة مثل `Lock` للحصول على تحكم أفضل في الموارد المشتركة مقارنة بالطرق التقليدية.

### مقدمة عن Java Utility Concurrent
الحزمة `java.util.concurrent` هي جزء من المكتبة القياسية لجافا، مصممة لتبسيط كتابة البرامج التي تشغل مهامًا متعددة في وقت واحد. هذا مفيد لتحسين الأداء، خاصة على أجهزة الكمبيوتر الحديثة التي تحتوي على نوى متعددة.

### استخدام ExecutorService
`ExecutorService` هو أداة رئيسية لإدارة السلاسل التنفيذية. تتيح لك إنشاء مجموعة من السلاسل التنفيذية وإرسال مهام لتشغيلها في الخلفية. على سبيل المثال، يمكنك إعداد مجموعة سلاسل تنفيذية وتشغيل مهام تُرجع نتائج، ثم الانتظار حتى تنتهي.

### المجموعات المتزامنة (Concurrent Collections)
تتضمن هذه الحزمة مجموعات آمنة للاستخدام في بيئات متعددة السلاسل التنفيذية مثل `ConcurrentHashMap`، والتي يمكن لسلاسل تنفيذية متعددة القراءة منها والكتابة إليها دون حدوث تعارضات. يختلف هذا عن المجموعات العادية، التي قد تحتاج إلى مزامنة إضافية.

### أدوات المزامنة
تقدم أدوات مثل `Lock` و `Condition` مرونة أكثر من الكلمة المفتاحية `synchronized`. تساعد في التحكم في الوصول إلى الموارد المشتركة، مما يضمن أن سلسلة تنفيذية واحدة فقط يمكنها تعديل البيانات في كل مرة.

---

### ملاحظة مسح: دليل شامل لاستخدام Java Utility Concurrent

يقدم هذا القسم استكشافًا مفصلاً لحزمة `java.util.concurrent`، مع توسيع النقاط الرئيسية وتقديم دليل شامل للمستخدمين الذين يتطلعون إلى تنفيذ البرمجة المتزامنة في جافا. تم هيكلة المحتوى لمحاكاة مقال احترافي، مع ضمان تضمين جميع التفاصيل ذات الصلة من التحليل الأولي، مع عمق إضافي للفهم التقني.

#### نظرة عامة على التزامن في جافا وحزمة `java.util.concurrent`
يمكن التزامن في جافا من تنفيذ مهام متعددة بالتوازي، مما يعزز أداء التطبيق واستجابته، خاصة على المعالجات متعددة النوى. تعد حزمة `java.util.concurrent`، التي تم تقديمها في جافا 5، مكونًا حاسمًا في المكتبة القياسية لجافا، حيث تقدم مجموعة من الفئات والواجهات لتسهيل البرمجة المتزامنة. تعالج هذه الحزمة تحديات إدارة السلاسل التنفيذية والمزامنة ومشاركة البيانات، والتي كانت تُعالج يدويًا في السابق وغالبًا ما أدت إلى كود معقد وعرضة للأخطاء.

تتضمن الحزمة أدوات لمجموعات السلاسل التنفيذية (Thread Pools)، وهياكل البيانات المتزامنة، وأدوات مساعدة للمزامنة، مما يجعل تطوير التطبيقات القابلة للتطوير والفعالة أسهل. على سبيل المثال، تستفيد التطبيقات الحديثة مثل خوادم الويب من معالجة طلبات متعددة في وقت واحد، وتوفر هذه الحزمة الأدوات للقيام بذلك بفعالية.

#### المكونات الرئيسية واستخدامها

##### ExecutorService: إدارة السلاسل التنفيذية بكفاءة
`ExecutorService` هي واجهة مركزية لإدارة تنفيذ السلاسل التنفيذية، توفر واجهة برمجة تطبيقات (API) عالية المستوى للتعامل مع مجموعات السلاسل التنفيذية وتنفيذ المهام غير المتزامن. إنها تجرد عملية إنشاء وإدارة السلاسل التنفيذية، مما يسمح للمطورين بالتركيز على منطق المهمة بدلاً من إدارة دورة حياة السلسلة التنفيذية.

لاستخدام `ExecutorService`، يمكنك إنشاء مجموعة سلاسل تنفيذية باستخدام طرق التصنيع (Factory Methods) من فئة `Executors`، مثل `newFixedThreadPool`، أو `newCachedThreadPool`، أو `newSingleThreadExecutor`. إليك مثالاً يوضح استخدامها:

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class ExecutorServiceExample {
    public static void main(String[] args) {
        // إنشاء مجموعة سلاسل تنفيذية ثابتة بعدد 2 سلسلة تنفيذية
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // إرسال مهام إلى المنفذ (Executor)
        Future<String> future1 = executor.submit(() -> {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "Task 1 completed";
        });

        Future<String> future2 = executor.submit(() -> {
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "Task 2 completed";
        });

        try {
            // انتظار انتهاء المهام والحصول على نتائجها
            System.out.println(future1.get());
            System.out.println(future2.get());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // إيقاف المنفذ
            executor.shutdown();
        }
    }
}
```

يُظهر هذا المثال كيفية إنشاء مجموعة سلاسل تنفيذية، وإرسال مهام تُرجع نتائج عبر `Future`، وضمان الإيقاف المناسب. يسمح لك كائن `Future` بالتحقق مما إذا كانت المهمة قد اكتملت واسترداد نتيجتها، مع معالجة الاستثناءات بشكل مناسب. هذا مفيد بشكل خاص للبرمجة غير المتزامنة، حيث يمكن تشغيل مهام مثل معالجة المعاملات أو معالجة الطلبات بشكل مستقل.

##### المجموعات المتزامنة: هياكل البيانات الآمنة للسلاسل التنفيذية
المجموعات المتزامنة هي تنفيذات آمنة للاستخدام في بيئات متعددة السلاسل التنفيذية للمجموعات القياسية في جافا، مصممة للاستخدام في سياقات متعددة السلاسل التنفيذية. تتضمن الأمثلة `ConcurrentHashMap`، و `ConcurrentSkipListMap`، و `ConcurrentSkipListSet`، و `CopyOnWriteArrayList`، و `CopyOnWriteArraySet`. تلغي هذه المجموعات الحاجة إلى المزامنة الخارجية، مما يقلل من خطر الجمود (Deadlocks) ويحسن الأداء.

على سبيل المثال، `ConcurrentHashMap` هو بديل آمن للاستخدام في بيئات متعددة السلاسل التنفيذية لـ `HashMap`، يسمح لسلاسل تنفيذية متعددة بالقراءة والكتابة في وقت واحد دون حظر. إليك مثال:

```java
import java.util.concurrent.ConcurrentHashMap;

public class ConcurrentHashMapExample {
    public static void main(String[] args) {
        ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();

        map.put("apple", 1);
        map.put("banana", 2);

        // يمكن لسلاسل تنفيذية متعددة القراءة من هذه الخريطة والكتابة إليها بأمان
        Thread t1 = new Thread(() -> {
            map.put("cherry", 3);
        });

        Thread t2 = new Thread(() -> {
            System.out.println(map.get("apple"));
        });

        t1.start();
        t2.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

يوضح هذا المثال كيف يمكن الوصول إلى `ConcurrentHashMap` بواسطة سلاسل تنفيذية متعددة دون مزامنة إضافية، مما يجعله مثاليًا للسيناريوهات التي تكون فيها عمليات القراءة والكتابة المتزامنة متكررة، كما في أنظمة التخزين المؤقت (Caching).

##### أدوات المزامنة: ما بعد `synchronized`
تتضمن الحزمة أدوات مزامنة مثل `Lock`، و `ReentrantLock`، و `Condition`، و `CountDownLatch`، و `Semaphore`، و `Phaser`، والتي تقدم مرونة أكثر من الكلمة المفتاحية `synchronized`. هذه الأدوات ضرورية لتنسيق وصول السلاسل التنفيذية إلى الموارد المشتركة وإدارة سيناريوهات المزامنة المعقدة.

على سبيل المثال، يوفر `ReentrantLock` آلية قفل أكثر مرونة، تسمح بتحكم أدق في عمليات القفل والفتح. إليك مثال:

```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LockExample {
    private final Lock lock = new ReentrantLock();

    public void doSomething() {
        lock.lock();
        try {
            // قسم حرج
            System.out.println("Doing something");
        } finally {
            lock.unlock();
        }
    }

    public static void main(String[] args) {
        LockExample example = new LockExample();

        Thread t1 = new Thread(() -> example.doSomething());
        Thread t2 = new Thread(() -> example.doSomething());

        t1.start();
        t2.start();
    }
}
```

يُظهر هذا المثال كيف يمكن استخدام `Lock` لمزامنة الوصول إلى قسم حرج، مما يضمن تنفيذ سلسلة تنفيذية واحدة فقط له في كل مرة. على عكس `synchronized`، يسمح `Lock` بميزات أكثر تقدمًا، مثل الأقفال المؤقتة والأقفال القابلة للمقاطعة، وهي مفيدة في السيناريوهات التي تتطلب معالجة المهلة أو المقاطعة.

تشمل الأدوات الأخرى:
- **CountDownLatch**: أداة مزامنة تسمح لواحدة أو أكثر من السلاسل التنفيذية بالانتظار حتى تكتمل مجموعة من العمليات في سلاسل تنفيذية أخرى. على سبيل المثال، يمكن استخدامها لضمان انتهاء جميع السلاسل التنفيذية العاملة قبل المتابعة.
- **Semaphore**: يتحكم في الوصول إلى مورد مشترك من خلال الحفاظ على عدد التصاريح المتاحة، مفيد للحد من عدد السلاسل التنفيذية التي تصل إلى مورد ما، مثل اتصالات قاعدة البيانات.
- **Phaser**: حاجز قابل لإعادة الاستخدام لتنسيق السلاسل التنفيذية في مراحل، مناسب للتطبيقات ذات مراحل التنفيذ المتعددة، مثل الخوارزميات التكرارية.

#### أدوات إضافية وأفضل الممارسات
تتضمن الحزمة أيضًا فئات ذرية (Atomic) مثل `AtomicInteger`، و `AtomicLong`، و `AtomicReference`، والتي توفر عمليات ذرية للمتغيرات، مما يضمن السلامة للسلاسل التنفيذية دون استخدام أقفال. على سبيل المثال:

```java
import java.util.concurrent.atomic.AtomicInteger;

public class AtomicIntegerExample {
    private AtomicInteger count = new AtomicInteger(0);

    public void increment() {
        count.incrementAndGet();
    }

    public int getCount() {
        return count.get();
    }

    public static void main(String[] args) throws InterruptedException {
        AtomicIntegerExample example = new AtomicIntegerExample();

        Thread t1 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                example.increment();
            }
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 1000; i++) {
                example.increment();
            }
        });

        t1.start();
        t2.start();

        t1.join();
        t2.join();

        System.out.println("Final count: " + example.getCount());
    }
}
```

يُظهر هذا المثال كيف يمكن لـ `AtomicInteger` زيادة عداد بأمان من سلاسل تنفيذية متعددة، متجنبًا ظروف السباق (Race Conditions) دون مزامنة صريحة.

تشمل أفضل الممارسات:
- قم دائمًا بإيقاف `ExecutorService` باستخدام `shutdown()` أو `shutdownNow()` لمنع تسرب الموارد.
- استخدم المجموعات المتزامنة بدلاً من المجموعات المتزامنة (Synchronized Collections) للحصول على أداء أفضل في السيناريوهات التي تهيمن عليها عمليات القراءة.
- تعامل مع الاستثناءات في المهام المرسلة إلى `ExecutorService` باستخدام `Future.get()`، والتي يمكن أن تطرح `ExecutionException`.

#### التحليل المقارن: النهج التقليدية مقابل النهج المتزامنة
لتسليط الضوء على الفوائد، ضع في اعتبارك الفرق بين استخدام البرمجة متعددة السلاسل التنفيذية التقليدية وحزمة `java.util.concurrent`. غالبًا ما تتضمن النهج التقليدية إنشاء مثيلات `Thread` يدويًا وإدارة المزامنة، مما يمكن أن يؤدي إلى كود متكرر (Boilerplate) وأخطاء مثل الجمود (Deadlocks). في المقابل، توفر الحزمة تجريدات عالية المستوى، مما يقلل التعقيد ويحسن قابلية الصيانة.

على سبيل المثال، تتطلب مزامنة `HashMap` يدويًا لفها بـ `Collections.synchronizedMap`، وهو ما يمكن أن يؤدي仍然 إلى مشاكل تنافس (Contention). ومع ذلك، يستخدم `ConcurrentHashMap` قفلًا دقيق الحبيبات (Fine-grained Locking)، مما يسمح بعمليات القراءة والكتابة المتزامنة، وهي تفصيلة غير متوقعة لأولئك المعتادين على طرق المزامنة التقليدية.

#### موارد لمزيد من التعلم
لأولئك الذين يتطلعون إلى تعميق فهمهم، تتوفر عدة موارد:
- تقدم [Oracle Java Tutorials on Concurrency](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html) الرسمية وثائق مفصلة وأمثلة.
- تقدم [Baeldung's Overview of java.util.concurrent](https://www.baeldung.com/java-util-concurrent) أدلة عملية ومقتطفات كود.
- يتضمن [Jenkov's Java Concurrency Utilities](https://jenkov.com/tutorials/java-util-concurrent/index.html) سلسلة من البرامج التعليمية التي تغطي كل مكون بعمق.

تضمن هذه الموارد، المحدثة اعتبارًا من مارس 2025، حصول المستخدمين على معلومات حديثة لتنفيذ البرمجة المتزامنة في جافا.

#### جدول: مقارنة الفئات الرئيسية في `java.util.concurrent`

| الفئة/الواجهة        | الغرض                                      | حالة استخدام مثال                  |
|------------------------|----------------------------------------------|--------------------------------------|
| `ExecutorService`      | يدير مجموعة السلاسل التنفيذية وتنفيذ المهام | تشغيل طلبات HTTP متعددة             |
| `ConcurrentHashMap`    | خريطة تجزئة آمنة للسلاسل التنفيذية          | تخزين البيانات مؤقتًا في تطبيق ويب  |
| `ReentrantLock`        | آلية قفل مرنة                                | حماية الأقسام الحرجة                |
| `CountDownLatch`       | الانتظار حتى اكتمال عمليات متعددة           | ضمان انتهاء جميع السلاسل التنفيذية من الإعداد |
| `Semaphore`            | يتحكم في الوصول إلى الموارد المشتركة         | الحد من مجموعة اتصالات قاعدة البيانات |

يلخص هذا الجدول الاستخدامات الأساسية، مما يساعد في اختيار الأداة المناسبة لاحتياجات التزامن المحددة.

في الختام، تعد حزمة `java.util.concurrent` ضرورية لتطوير جافا الحديث، حيث تقدم أدوات قوية للبرمجة المتزامنة. من خلال الاستفادة من هذه الأدوات، يمكن للمطورين بناء تطبيقات فعالة وقابلة للتطوير، معالجة متطلبات بيئات الحوسبة المعاصرة.

#### الاقتباسات الرئيسية
- [Oracle Java Tutorials Concurrency Summary](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html)
- [Baeldung java.util.concurrent Overview](https://www.baeldung.com/java-util-concurrent)
- [Jenkov Java Concurrency Utilities Index](https://jenkov.com/tutorials/java-util-concurrent/index.html)