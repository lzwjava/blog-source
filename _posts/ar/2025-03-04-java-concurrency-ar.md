---
audio: false
generated: true
lang: ar
layout: post
title: التوازي في جاڤا
translated: true
---

### النقاط الرئيسية
- يوفر حزمة `java.util.concurrent` مساعدة في إدارة مهام متعددة في وقت واحد في Java، مما يجعل البرامج أسرع وأكثر استجابة.
- يبدو أن استخدام `ExecutorService` هو طريقة شائعة للتعامل مع الخيوط، مما يسمح لك بتشغيل المهام في الخلفية.
- تشير الأبحاث إلى أن مجموعات البيانات المتزامنة مثل `ConcurrentHashMap` هي آمنة للخيوط، مما يضمن أن يمكن للعديد من الخيوط الوصول إلى البيانات بأمان.
- تشير الأدلة إلى استخدام أدوات التزامن مثل `Lock` للحصول على أفضل التحكم على الموارد المشتركة مقارنة بالأسلوب التقليدي.

### مقدمة إلى Java Utility Concurrent
هي حزمة `java.util.concurrent` جزء من مكتبة Java القياسية، مصممة لتسهيل كتابة البرامج التي تعمل على تنفيذ مهام متعددة في نفس الوقت. وهذا مفيد لتحسين الأداء، خاصة على أجهزة الكمبيوتر الحديثة التي تحتوي على عدة نواة.

### استخدام ExecutorService
`ExecutorService` هو أداة رئيسية لإدارة الخيوط. يسمح لك بإنشاء مجموعة من الخيوط وتقديم المهام للتشغيل في الخلفية. على سبيل المثال، يمكنك إعداد مجموعة خيوط وتشغيل المهام التي تعيد النتائج، ثم الانتظار حتى تنتهي.

### مجموعات البيانات المتزامنة
تضم هذه الحزمة مجموعات بيانات آمنة للخيوط مثل `ConcurrentHashMap`، والتي يمكن للعديد من الخيوط قراءتها وكتابتها دون تعارض. وهذا مختلف عن المجموعات العادية، والتي قد تحتاج إلى تزامن إضافي.

### أدوات التزامن
توفر أدوات مثل `Lock` و `Condition` مرونة أكبر من كلمة `synchronized`. تساعد في التحكم في الوصول إلى الموارد المشتركة، مما يضمن أن يمكن فقط لخط واحد تعديل البيانات في وقت واحد.

---

### ملاحظة الاستطلاع: دليل شامل لاستخدام Java Utility Concurrent

يقدم هذا القسم استكشافًا مفصلًا لحزمة `java.util.concurrent`، ويوسع النقاط الرئيسية ويقدم دليلًا شاملًا للمستخدمين الذين يبحثون عن تنفيذ البرمجة المتزامنة في Java. يتم تنظيم المحتوى على شكل مقالة محترفة، مما يضمن تضمين جميع التفاصيل ذات الصلة من التحليل الأولي، مع عمق إضافي لفهم تقنية.

#### نظرة عامة على التزامن في Java وحزمة `java.util.concurrent`
يسمح التزامن في Java بتشغيل مهام متعددة في نفس الوقت، مما يحسن أداء التطبيقات واستجابتها، خاصة على المعالجات متعددة النواة. تم تقديم حزمة `java.util.concurrent` في Java 5، وهي جزء أساسي من مكتبة Java القياسية، وتوفر مجموعة من الفئات والواجهات لتسهيل البرمجة المتزامنة. تتعامل هذه الحزمة مع تحديات إدارة الخيوط والتزامن ومشاركة البيانات، والتي كانت تُعامل يدويًا سابقًا، مما أدى إلى كود معقد ومخطئ.

تضم الحزمة أدواتًا لتجمعات الخيوط، ومجموعات البيانات المتزامنة، وأدوات التزامن، مما يجعل من السهل تطوير تطبيقات قابلة للتوسيع وفعالة. على سبيل المثال، يمكن أن تستفيد التطبيقات الحديثة مثل خادمات الويب من معالجة عدة طلبات في نفس الوقت، وتوفر هذه الحزمة الأدوات لتحقيق ذلك بشكل فعال.

#### المكونات الرئيسية واستخدامها

##### ExecutorService: إدارة الخيوط بشكل فعال
`ExecutorService` هو واجهة مركزية لإدارة تنفيذ الخيوط، وتوفر واجهة برمجة تطبيقات عالية المستوى لتسليم الخيوط وتنفيد المهام بشكل غير متزامن. تنسخ إنشاء وإدارة الخيوط، مما يسمح للمطورين التركيز على منطق المهام بدلاً من دورة حياة الخيوط.

يمكنك إنشاء مجموعة خيوط باستخدام طرق مصنع من فئة `Executors` مثل `newFixedThreadPool` و `newCachedThreadPool` و `newSingleThreadExecutor`. إليك مثال يوضح استخدامه:

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class ExecutorServiceExample {
    public static void main(String[] args) {
        // إنشاء مجموعة خيوط ثابتة تحتوي على 2 خيوط
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // تقديم المهام إلى المحرّك
        Future<String> future1 = executor.submit(() -> {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "تم إكمال المهمة 1";
        });

        Future<String> future2 = executor.submit(() -> {
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "تم إكمال المهمة 2";
        });

        try {
            // الانتظار حتى تنتهي المهام وتحصل على نتائجها
            System.out.println(future1.get());
            System.out.println(future2.get());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // إيقاف المحرّك
            executor.shutdown();
        }
    }
}
```

يوضح هذا المثال كيفية إنشاء مجموعة خيوط، تقديم المهام التي تعيد النتائج عبر `Future`، وضمن إيقاف المحرّك بشكل صحيح. يسمح لك `Future` بالتحقق من إكمال المهمة وتحصل على نتيجةها، مع معالجة الاستثناءات بشكل مناسب. وهذا مفيد في البرمجة غير المتزامنة، حيث يمكن أن تعمل المهام مثل معالجة المعاملات أو معالجة الطلبات بشكل مستقل.

##### مجموعات البيانات المتزامنة: بنية البيانات آمنة للخيوط
هي مجموعات بيانات آمنة للخيوط، مصممة للاستخدام في سياق الخيوط المتعددة. وتشمل الأمثلة `ConcurrentHashMap` و `ConcurrentSkipListMap` و `ConcurrentSkipListSet` و `CopyOnWriteArrayList` و `CopyOnWriteArraySet`. هذه المجموعات تخلص من الحاجة إلى تزامن خارجي، مما يقلل من خطر حدوث تعادلات وتحسن الأداء.

على سبيل المثال، `ConcurrentHashMap` هو بديل آمن للخيوط لـ `HashMap`، يسمح لعدة خيوط قراءتها وكتابتها في نفس الوقت دون تعارض. إليك مثال:

```java
import java.util.concurrent.ConcurrentHashMap;

public class ConcurrentHashMapExample {
    public static void main(String[] args) {
        ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();

        map.put("apple", 1);
        map.put("banana", 2);

        // يمكن لعدة خيوط الوصول إلى هذه الخريطة بشكل آمن
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

يوضح هذا المثال كيفية الوصول إلى `ConcurrentHashMap` من قبل عدة خيوط دون تزامن إضافي، مما يجعله مناسبًا للسيناريوهات التي تكون فيها عمليات القراءة والكتابة المتزامنة شائعة، مثل في أنظمة التخزين المؤقت.

##### أدوات التزامن: ما وراء `synchronized`
تضم الحزمة أدوات التزامن مثل `Lock` و `ReentrantLock` و `Condition` و `CountDownLatch` و `Semaphore` و `Phaser`، وتوفر مرونة أكبر من كلمة `synchronized`. هذه الأدوات أساسية لتنسيق الوصول إلى الموارد المشتركة وإدارة سيناريوهات التزامن المعقدة.

على سبيل المثال، `ReentrantLock` يوفر آلية قفل أكثر مرونة، مما يسمح بالتحكم الدقيق في عمليات القفل والفتح. إليك مثال:

```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LockExample {
    private final Lock lock = new ReentrantLock();

    public void doSomething() {
        lock.lock();
        try {
            // قسم حرج
            System.out.println("إجراء شيء ما");
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

يوضح هذا المثال كيفية استخدام `Lock` لتزامن الوصول إلى قسم حرج، مما يضمن أن يمكن فقط لخط واحد تنفيذه في وقت واحد. خلافًا لـ `synchronized`، `Lock` يسمح بخصائص متقدمة مثل القفلات الموقتة والقفلات القابلة للقطع، والتي مفيدة في السيناريوهات التي تتطلب معالجة الوقت أو قطع.

تضم الأدوات الأخرى:
- **CountDownLatch**: مساعدة للتزامن تسمح لخط أو أكثر بالانتظار حتى تنتهي مجموعة من العمليات في خيوط أخرى. على سبيل المثال، يمكن استخدامها لضمان أن جميع خيوط العمال قد انتهت قبل الاستمرار.
- **Semaphore**: يسيطر على الوصول إلى الموارد المشتركة من خلال الحفاظ على عدد الترخيصات المتاحة، مفيدًا في تحديد عدد الخيوط التي يمكن أن تفتح الموارد، مثل اتصالات قاعدة البيانات.
- **Phaser**: حاجز قابل لإعادة الاستخدام لتنسيق الخيوط في المراحل، مناسبًا للتطبيقات التي تحتوي على عدة مراحل من التنفيذ، مثل الخوارزميات التكرارية.

#### أدوات إضافية وأفضل الممارسات
تضم الحزمة أيضًا فئات ذرية مثل `AtomicInteger` و `AtomicLong` و `AtomicReference`، والتي توفر عمليات ذرية للمتغيرات، مما يضمن أمان الخيوط بدون قفل. على سبيل المثال:

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

        System.out.println("العدد النهائي: " + example.getCount());
    }
}
```

يوضح هذا المثال كيفية زيادة `AtomicInteger` بشكل آمن من عدة خيوط، مما يجنب حالات السباق دون تزامن صريح.

أفضل الممارسات تشمل:
- دائمًا إيقاف `ExecutorService` باستخدام `shutdown()` أو `shutdownNow()` لمنع تسرب الموارد.
- استخدام مجموعات البيانات المتزامنة بدلاً من المجموعات المتزامنة للحصول على أداء أفضل في السيناريوهات التي تكون فيها القراءة شائعة.
- معالجة الاستثناءات في المهام المقدمة إلى `ExecutorService` باستخدام `Future.get()`، والتي يمكن أن تثير `ExecutionException`.

#### تحليل مقارنة: تقنيات تقليدية مقابل تقنيات متزامنة
للتأكيد على الفوائد، فلتفكر في الفرق بين استخدام تقنيات الخيوط التقليدية وحزمة `java.util.concurrent`. غالبًا ما تتضمن تقنيات تقليدية إنشاء `Thread` يدويًا وإدارة التزامن، مما يمكن أن يؤدي إلى كود مكرر ومخطئ مثل تعادلات. في المقابل، توفر الحزمة تقنيات عالية المستوى، مما يقلل من التعقيد ويحسن الصيانة.

على سبيل المثال، يتطلب تزامن `HashMap` يدويًا غلقه مع `Collections.synchronizedMap`، والذي يمكن أن يؤدي إلى مشاكل التنافس. `ConcurrentHashMap`، على العكس من ذلك، يستخدم قفل دقيق، مما يسمح بالقراءة والكتابة المتزامنة، وهو تفصيل غير متوقع لمن اعتاد على تقنيات التزامن التقليدية.

#### الموارد للتعلم الإضافي
للمستفيدين من عمق فهمهم، هناك موارد متاحة:
- [دروس Oracle Java الرسمية حول التزامن](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html) توفر توثيقًا مفصلًا ومثالات.
- [مقدمة Baeldung لـ java.util.concurrent](https://www.baeldung.com/java-util-concurrent) تقدم دليلات عملية وقطع كود.
- [مقالات Jenkov حول أدوات التزامن في Java](https://jenkov.com/tutorials/java-util-concurrent/index.html) تتضمن سلسلة من الدروس التي تغطي كل مكون في العمق.

تضمن هذه الموارد، الحالية حتى مارس 2025، أن يكون للمستخدمين الوصول إلى معلومات حديثة لتنفيذ البرمجة المتزامنة في Java.

#### جدول: مقارنة الفئات الرئيسية في `java.util.concurrent`

| فئة/واجهة        | الغرض                                      | مثال على الاستخدام                     |
|------------------------|----------------------------------------------|--------------------------------------|
| `ExecutorService`      | يدير مجموعة الخيوط وتنفيد المهام       | تشغيل عدة طلبات HTTP       |
| `ConcurrentHashMap`    | خريطة هاش آمنة للخيوط                         | تخزين البيانات المؤقت في تطبيق الويب    |
| `ReentrantLock`        | آلية قفل مرنة                   | حماية الأقسام الحرج         |
| `CountDownLatch`       | الانتظار حتى تنتهي عدة عمليات     | التأكد من انتهاء جميع الخيوط من الإعداد    |
| `Semaphore`            | يسيطر على الوصول إلى الموارد المشتركة          | تحديد حجم مجموعة اتصالات قاعدة البيانات    |

يقدم هذا الجدول ملخصًا للأغراض الرئيسية، مما يساعد في اختيار الأداة المناسبة لحاجات التزامن الخاصة بك.

في الختام، حزمة `java.util.concurrent` أساسية للتنمية الحديثة في Java، وتوفر أدوات قوية للبرمجة المتزامنة. من خلال استغلال هذه الأدوات، يمكن للمطورين بناء تطبيقات فعالة ومتسقة، معالجًا متطلبات بيئات الحوسبة الحديثة.

#### الإشارات الرئيسية
- [دروس Oracle Java الرسمية حول التزامن](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/package-summary.html)
- [مقدمة Baeldung لـ java.util.concurrent](https://www.baeldung.com/java-util-concurrent)
- [مقالات Jenkov حول أدوات التزامن في Java](https://jenkov.com/tutorials/java-util-concurrent/index.html)