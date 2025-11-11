---
audio: false
generated: true
lang: ar
layout: post
title: فهم خدمة المنفذ ومنفذ تجمع الخيوط
translated: true
type: note
---

ضبط معلمات `ExecutorService` في جافا يتضمن تكوين مجموعة الخيوط لتحسين الأداء بناءً على موارد نظامك (مثل معالج 8 نوى) وطبيعة مهامك (مثل المهام المرتبطة بالمعالج أو المرتبطة بالإدخال/الإخراج). أدناه، سأشرح كيفية تكوين `ExecutorService` لمعالج 8 نوى، مع التركيز على التطبيقات الشائعة مثل `ThreadPoolExecutor`، وسأقدم أمثلة عملية مخصصة لحالة استخدامك.

---

### فهم ExecutorService و ThreadPoolExecutor

يتم تنفيذ واجهة `ExecutorService` عادةً بواسطة فئات مثل `ThreadPoolExecutor`، والتي تتيح تحكمًا دقيقًا في معلمات مجموعة الخيوط. عند تكوينها لمعالج 8 نوى، تحتاج إلى مراعاة:
- **حجم المجموعة الأساسي (Core Pool Size)**: عدد الخيوط التي تبقى نشطة حتى عندما تكون خاملة.
- **الحد الأقصى لحجم المجموعة (Maximum Pool Size)**: أقصى عدد مسموح به من الخيوط في المجموعة.
- **سعة قائمة الانتظار (Queue Capacity)**: حجم قائمة انتظار المهام لحجز المهام قبل تنفيذها.
- **استراتيجية إنشاء الخيوط (Thread Creation Strategy)**: كيفية إنشاء الخيوط وإدارتها.
- **نوع المهمة (Task Type)**: ما إذا كانت المهام مرتبطة بالمعالج (مثل العمليات الحسابية) أو مرتبطة بالإدخال/الإخراج (مثل استدعاءات قاعدة البيانات).

بالنسبة لمعالج 8 نوى، يعتمد التكوين الأمثل على ما إذا كانت مهامك كثيفة الاستخدام للمعالج أو كثيفة الاستخدام للإدخال/الإخراج (مثل الوصول إلى قاعدة البيانات في سيناريو التحقق الخاص بك).

---

### المعلمات الرئيسية لـ ThreadPoolExecutor

إليك كيفية إعداد `ThreadPoolExecutor`:

```java
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    corePoolSize,      // عدد الخيوط التي تبقى نشطة
    maximumPoolSize,   // أقصى عدد مسموح به من الخيوط
    keepAliveTime,     // مدة بقاء الخيوط الخاملة نشطة (مثل 60L)
    TimeUnit.SECONDS,  // الوحدة الزمنية لـ keepAliveTime
    workQueue,         // قائمة الانتظار لحجز المهام (مثل new LinkedBlockingQueue<>())
    threadFactory,     // اختياري: تخصيص أسماء أو أولوية للخيوط
    rejectionHandler   // الإجراء عند امتلاء قائمة الانتظار ووصول عدد الخيوط للحد الأقصى
);
```

#### تفصيل المعلمات
1. **`corePoolSize`**:
   - الحد الأدنى لعدد الخيوط التي تبقى نشطة دائمًا.
   - للمهام المرتبطة بالمعالج: اضبطه على عدد النوى (مثل 8).
   - للمهام المرتبطة بالإدخال/الإخراج: يمكن أن يكون أعلى (مثل 16 أو أكثر)، حيث قد تقضي الخيوط وقتًا في الانتظار.

2. **`maximumPoolSize`**:
   - أقصى عدد من الخيوط المسموح به في حالة امتلاء قائمة الانتظار.
   - للمهام المرتبطة بالمعالج: غالبًا ما يكون مساويًا لـ `corePoolSize` (مثل 8).
   - للمهام المرتبطة بالإدخال/الإخراج: أعلى للتعامل مع الأحمال المفاجئة (مثل 20 أو 50).

3. **`keepAliveTime`**:
   - المدة التي تبقى فيها الخيوط الخاملة الزائدة (أكثر من `corePoolSize`) نشطة قبل إنهائها.
   - مثال: `60L` ثانية هو الإعداد الافتراضي الشائع.

4. **`workQueue`**:
   - قائمة انتظار للمهام التي تنتظر التنفيذ:
     - `LinkedBlockingQueue`: قائمة انتظار غير محدودة (افتراضي في كثير من الحالات).
     - `ArrayBlockingQueue`: قائمة انتظار محدودة (مثل `new ArrayBlockingQueue<>(100)`).
     - `SynchronousQueue`: لا توجد قائمة انتظار؛ يتم تسليم المهام مباشرة إلى الخيوط (مستخدم في `Executors.newCachedThreadPool()`).

5. **`threadFactory`** (اختياري):
   - يخصص إنشاء الخيوط (مثل تسمية الخيوط لأغراض التصحيح).
   - الافتراضي: `Executors.defaultThreadFactory()`.

6. **`rejectionHandler`** (اختياري):
   - السياسة عند تجاوز المهام لـ `maximumPoolSize` وسعة قائمة الانتظار:
     - `AbortPolicy` (افتراضي): يطلق استثناء `RejectedExecutionException`.
     - `CallerRunsPolicy`: ينفذ المهمة في الخيط الذي قام بالاستدعاء.
     - `DiscardPolicy`: يتجاهل المهمة بصمت.

---

### التكوين لمعالج 8 نوى

#### السيناريو 1: المهام المرتبطة بالمعالج (CPU-Bound)
إذا كانت مهامك كثيفة الاستخدام للمعالج (مثل العمليات الحسابية المعقدة)، فأنت تريد مطابقة عدد الخيوط مع نوى المعالج لتعظيم الإنتاجية دون إثقال النظام.

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createCpuBoundExecutor() {
        int corePoolSize = 8; // يطابق 8 نوى
        int maximumPoolSize = 8;
        long keepAliveTime = 60L; // 60 ثانية

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(), // قائمة انتظار غير محدودة
            Executors.defaultThreadFactory(),
            new ThreadPoolExecutor.AbortPolicy()
        );
    }
}
```

- **السبب**: 8 خيوط تستخدم بالكامل نوى المعالج الثمانية. إضافة المزيد من الخيوط سيسبب عبئًا إضافيًا due to تبديل السياق، مما يقلل الأداء.

#### السيناريو 2: المهام المرتبطة بالإدخال/الإخراج (مثل التحقق من قاعدة البيانات)
لحالة التحقق الخاصة بك مع الوصول إلى قاعدة البيانات، تكون المهام مرتبطة بالإدخال/الإخراج - حيث تقضي الخيوط وقتًا في انتظار ردود قاعدة البيانات. يمكنك استخدام خيوط أكثر من النوى لإبقاء المعالج مشغولاً بينما تنتظر بعض الخيوط.

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createIoBoundExecutor() {
        int corePoolSize = 16; // ضعف عدد النوى تقريبًا للمهام المرتبطة بالإدخال/الإخراج
        int maximumPoolSize = 20; // السماح بسعة إضافية للذروات
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100), // قائمة انتظار محدودة للتحكم في الذاكرة
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(), // تسمية مخصصة
            new ThreadPoolExecutor.CallerRunsPolicy() // الرجوع إلى الخيط المستدع في حالة الحمل الزائد
        );
    }
}
```

- **السبب**:
  - `corePoolSize = 16`: قاعدة شائعة للمهام المرتبطة بالإدخال/الإخراج هي `N * 2` (حيث `N` هو عدد نوى المعالج)، ولكن يمكنك ضبط هذا بناءً على حدود اتصال قاعدة البيانات وأوقات انتظار المهام.
  - `maximumPoolSize = 20`: يسمح بخيوط إضافية لأحمال الذروة.
  - `ArrayBlockingQueue(100)`: يمنع النمو غير المحدود للمهام في قائمة الانتظار، متجنبًا مشاكل الذاكرة.
  - `CallerRunsPolicy`: يضمن تدهور النظام بشكل متحكم تحت الحمل الزائد عن طريق تشغيل المهام في الخيط المستدع.

#### التكامل مع Spring Boot
في تطبيق Spring Boot، عرّف `ExecutorService` كـ bean:

```java
import com.google.common.util.concurrent.ThreadFactoryBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.*;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        int corePoolSize = 16; // افتراض مهام مرتبطة بالإدخال/الإخراج للتحقق
        int maximumPoolSize = 20;
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100),
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(),
            new ThreadPoolExecutor.CallerRunsPolicy()
        );
    }
}
```

- **ملاحظة**: أضف Guava (`com.google.guava:guava`) إلى التبعيات الخاصة بك لاستخدام `ThreadFactoryBuilder`، أو استخدم `Executors.defaultThreadFactory()` إذا كنت لا تحتاج إلى تسمية مخصصة.

#### استخدامه في خدمة التحقق الخاصة بك
حقنه واستخدمه كما هو موضح في الأمثلة السابقة:

```java
@Service
public class ValidationService {
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    // الاستخدام في منطق CompletableFuture أو ExecutorService كما هو موضح سابقًا
}
```

---

### نصائح للضبط لمعالج 8 نوى

1. **قياس الأداء**:
   - استخدم أدوات التحليل (مثل VisualVM) لمراقبة استخدام الخيوط وضبط `corePoolSize` و `maximumPoolSize`.

2. **حدود قاعدة البيانات**:
   - إذا كانت القواعد تصل إلى قاعدة بيانات، فتأكد من أن حجم مجموعة الخيوط لا يتجاوز حجم مجموعة الاتصالات الخاصة بك (مثل `maximumPoolSize` في HikariCP). قم بتنسيق هذه الإعدادات.

3. **الحساب الديناميكي**:
   - استخدم `Runtime.getRuntime().availableProcessors()` لضبط حجم المجموعة الأساسي ديناميكيًا:
     ```java
     int cores = Runtime.getRuntime().availableProcessors(); // سيعيد 8 على معالج 8 نوى
     int corePoolSize = cores * 2; // للمهام المرتبطة بالإدخال/الإخراج
     ```

4. **بدء الخيوط مسبقًا**:
   - استدعِ `executor.prestartAllCoreThreads()` لتهيئة جميع الخيوط الأساسية مقدمًا، متجنبًا الإنشاء الكسول.

---

### الخلاصة

لمعالج 8 نوى يشغل مهامًا مرتبطة بالإدخال/الإخراج مثل قواعد التحقق الخاصة بك مع الوصول إلى قاعدة البيانات:
- استخدم `ThreadPoolExecutor` مع `corePoolSize = 16`، و `maximumPoolSize = 20`، وقائمة انتظار محدودة (مثل `ArrayBlockingQueue(100)`).
- قم بدمجه كـ bean في Spring لحقن التبعيات.
- اضبط بناءً على نتائج التحليل وقيود قاعدة البيانات.

هذا الإعداد يوازن بين التوازي، استخدام الموارد، واستقرار النظام، مما يجعله مناسبًا لحالة استخدامك. أعلمني إذا كنت بحاجة إلى مساعدة في دمج هذا في مشروعك المحدد!