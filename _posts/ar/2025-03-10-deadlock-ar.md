---
audio: false
generated: true
lang: ar
layout: post
title: اختناق في سبرينغ بوت
translated: true
type: note
---

دعنا نتعمق في حل مشكلة تَعَطُّل (deadlock) في مشروع Spring Boot عندما تصل طلبات متعددة إلى طريقة bean في وقت واحد. تحدث حالات التَعَطُّل عندما يحجب خيطان أو أكثر بعضهما البعض إلى أجل غير مسمى، غالبًا بسبب التنافس على الموارد المشتركة مثل أقفال قاعدة البيانات، أو الكتل المتزامنة (synchronized blocks)، أو هياكل البيانات الآمنة للخيوط (thread-safe). بما أنك ذكرت أن طريقة bean تتعامل مع العديد من الطلبات، سأفترض أن هذا bean ذو نطاق Singleton (النطاق الافتراضي في Spring) وسأستكشف الأسباب والحلول الشائعة.

أولاً، دعنا نحدد السيناريوهات المحتملة للتَعَطُّل في هذا السياق:
1.  **أقفال قاعدة البيانات**: إذا كانت طريقة bean تتفاعل مع قاعدة بيانات (على سبيل المثال، عبر JPA/Hibernate)، قد تقوم المعاملات المتزامنة (concurrent transactions) بقفل الصفوف أو الجداول بترتيبات متضاربة.
2.  **الكتل المتزامنة (Synchronized Blocks)**: إذا كانت الطريقة تستخدم الكلمة المفتاحية `synchronized` أو الأقفال (مثل `ReentrantLock`)، فإن الترتيب غير الصحيح للأقفال قد يتسبب في انتظار الخيوط لبعضها البعض.
3.  **الموارد المشتركة**: إذا كان الـ bean يعدل موردًا مشتركًا في الذاكرة (مثل متغير static أو مجموعة collection)، قد يؤدي التنافس (contention) إلى تَعَطُّل.
4.  **الاستدعاءات الخارجية**: إذا كانت الطريقة تستدعي خدمات أو واجهات برمجة تطبيقات (APIs) خارجية، فإن التأخيرات أو سلوك الحجب قد يزيد من مشاكل التزامن.

بما أنك لم تشارك كودًا محددًا، سأقدم نهجًا عامًا لتشخيص وإصلاح المشكلة، ثم أقدم مثالًا ملموسًا.

### الخطوة 1: تشخيص التَعَطُّل
-   **تمكين التسجيل (Logging)**: أضف تسجيلًا (على سبيل المثال، SLF4J مع Logback) لتتبع دخول الطريقة، وخروجها، والوصول إلى الموارد. هذا يساعد في تحديد مكان توقف الخيوط.
-   **تفريغ الخيوط (Thread Dump)**: عندما يحدث التَعَطُّل، قم بالتقاط تفريغ للخيوط (مثل استخدام `jstack` أو VisualVM). ابحث عن الخيوط في حالة `BLOCKED` أو `WAITING` وتحقق من آثار المكدس (stack traces) الخاصة بها للكشف عن تنافس الأقفال.
-   **المراقبة**: استخدم أدوات مثل Spring Actuator أو أداة تحليل الأداء (profiler) (مثل YourKit) لمراقبة سلوك الخيوط تحت الحمل.

### الخطوة 2: الإصلاحات الشائعة
إليك كيفية معالجة التَعَطُّل بناءً على الأسباب المحتملة:

#### الحالة 1: تَعَطُّل مرتبط بقاعدة البيانات
إذا كانت طريقة bean تنفذ عمليات على قاعدة البيانات، فإن حالات التَعَطُّل غالبًا ما تنشأ من تعارضات المعاملات (transaction conflicts).
-   **الحل**: حسّن حدود المعاملات (transaction boundaries) وترتيب الحصول على الأقفال.
    -   استخدم `@Transactional` مع مستوى عزل مناسب (مثل `READ_COMMITTED` بدلاً من `SERIALIZABLE` ما لم يكن ضروريًا تمامًا).
    -   تأكد من الترتيب المتسق للوصول إلى الموارد (مثل تحديث الجدول A دائمًا قبل الجدول B).
    -   قلل نطاق المعاملة (transaction scope) بنقل المنطق غير التعاملي (non-transactional logic) خارج `@Transactional`.
-   **مثال**:
    ```java
    @Service
    public class MyService {
        @Autowired
        private MyRepository repo;

        @Transactional
        public void processRequest(Long id1, Long id2) {
            // التأكد من الترتيب المتسق لتجنب التَعَطُّل
            if (id1 < id2) {
                repo.updateEntity(id1);
                repo.updateEntity(id2);
            } else {
                repo.updateEntity(id2);
                repo.updateEntity(id1);
            }
        }
    }
    ```
-   **إضافة مفيدة**: عيّن وقت انتهاء للمعاملة (transaction timeout) (مثل `@Transactional(timeout = 5)`) لإلغاء المعاملات طويلة المدى ومنع الانتظار indefinitely.

#### الحالة 2: الكتل المتزامنة (Synchronized Blocks) أو الأقفال
إذا كانت الطريقة تستخدم أقفالًا صريحة، فقد يحدث التَعَطُّل إذا تم الحصول على الأقفال بترتيبات مختلفة عبر الخيوط.
-   **الحل**: استخدم قفلًا واحدًا أو فرض ترتيبًا ثابتًا للأقفال.
    -   استبدل كتل `synchronized` المتعددة بقفل واحد شامل (coarse-grained lock) إذا كان ذلك ممكنًا.
    -   استخدم `ReentrantLock` مع وقت انتهاء (timeout) لتجنب الحجب indefinitely.
-   **مثال**:
    ```java
    @Service
    public class MyService {
        private final ReentrantLock lock = new ReentrantLock();

        public void processRequest(String resourceA, String resourceB) {
            try {
                if (lock.tryLock(2, TimeUnit.SECONDS)) {
                    // القسم الحرج (Critical section)
                    System.out.println("Processing " + resourceA + " and " + resourceB);
                } else {
                    throw new RuntimeException("Could not acquire lock in time");
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                if (lock.isHeldByCurrentThread()) {
                    lock.unlock();
                }
            }
        }
    }
    ```

#### الحالة 3: الموارد المشتركة في الذاكرة
إذا كان الـ bean يعدل مجموعة (collection) أو متغيرًا مشتركًا، فقد يسبب الوصول المتزامن مشاكل.
-   **الحل**: استخدم بدائل آمنة للخيوط (thread-safe) أو تجنب الحالة المشتركة (shared state).
    -   استبدل `ArrayList` بـ `CopyOnWriteArrayList` أو `Collections.synchronizedList`.
    -   استخدم `ConcurrentHashMap` للخرائط (maps).
    -   الأفضل من ذلك، اجعل الـ bean عديم الحالة (stateless) أو استخدم beans ذات نطاق الطلب (`@Scope("request")`).
-   **مثال**:
    ```java
    @Service
    @Scope("prototype") // تجنب Singleton إذا كان stateful
    public class MyService {
        private final ConcurrentHashMap<String, Integer> cache = new ConcurrentHashMap<>();

        public void processRequest(String key, int value) {
            cache.put(key, value); // آمن للخيوط (Thread-safe)
        }
    }
    ```

#### الحالة 4: حمل تزامن عالٍ
إذا كان التَعَطُّل ناتجًا عن إرباك الـ bean بطلبات كثيرة، فقد يكون تنافس الخيوط (thread contention) هو السبب الجذري.
-   **الحل**: أدخل المعالجة غير المتزامنة (asynchronous processing) أو تحديد معدل الطلبات (rate limiting).
    -   استخدم `@Async` لتفريغ العمل إلى مجموعة خيوط (thread pool).
    -   قم بتكوين مجموعة خيوط باستخدام `TaskExecutor` لإدارة التزامن.
-   **مثال**:
    ```java
    @Service
    public class MyService {
        @Async
        public CompletableFuture<String> processRequest(String input) {
            // محاكاة العمل
            Thread.sleep(1000);
            return CompletableFuture.completedFuture("Done: " + input);
        }
    }

    @Configuration
    @EnableAsync
    public class AsyncConfig {
        @Bean
        public TaskExecutor taskExecutor() {
            ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
            executor.setCorePoolSize(10);
            executor.setMaxPoolSize(50);
            executor.setQueueCapacity(100);
            return executor;
        }
    }
    ```
-   **طريقة الاستخدام**: استدع `processRequest` وتعامل مع الـ `CompletableFuture` في المتحكم (controller).

### الخطوة 3: منع المشاكل المستقبلية
-   **اختبار الحمل**: Simulate high concurrency مع أدوات مثل JMeter أو Gatling لاكتشاف حالات التَعَطُّل مبكرًا.
-   **مراجعة الكود**: ابحث عن الأقفال المتداخلة (nested locks)، أو المعاملات طويلة المدى، أو الحالة القابلة للتعديل المشتركة (shared mutable state).
-   **أوقات الانتهاء (Timeouts)**: عيّن دائمًا أوقات انتهاء للأقفال، أو المعاملات، أو الاستدعاءات الخارجية.

### الأفكار النهائية
بدون رؤية كود الـ bean الخاص بك، افترضت أنه bean من نوع Singleton تحت حمل ثقيل مع احتمال وجود تنافس على قاعدة البيانات أو الأقفال. إذا شاركت المزيد من التفاصيل (مثل كود الطريقة، أو آثار المكدس stack traces، أو الموارد التي يصل إليها)، يمكنني تخصيص الحل بشكل أكبر. في الوقت الحالي، ابدأ بالتشخيص باستخدام تفريغ الخيوط (thread dump) وطبق الإصلاح المناسب - تحسين قاعدة البيانات، أو إدارة الأقفال، أو المعالجة غير المتزامنة. دعني أعرف كيف سارت الأمور