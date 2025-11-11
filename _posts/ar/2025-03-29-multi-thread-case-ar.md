---
audio: false
generated: true
lang: ar
layout: post
title: حالة متعددة الخيوط
translated: true
type: note
---

لتعامل مع التحقق متعدد الخيوط في مشروع Java Spring Boot مع 10 قواعد، حيث قد تصل بعض القواعد إلى قاعدة البيانات وتريد إلغاء الآخرين بمجرد فشل واحدة لتجنب إهدار الوقت، يمكنك استخدام أدوات التزامن في Java بالاشتراك مع ميزات Spring. إليك حلاً كاملاً وفعالاً:

### نظرة عامة على النهج
- **تشغيل عمليات التحقق بشكل متزامن**: استخدم خيوطًا متعددة لتنفيذ قواعد التحقق العشرة بالتوازي، مما يسرع العملية عندما تمر جميع القواعد بنجاح.
- **الإلغاء عند الفشل**: أوقف عمليات التحقق المتبقية بمجرد فشل أي قاعدة، لتقليل العمل غير الضروري.
- **الاستفادة من Spring**: استخدم حقن التبعية وإدارة المعاملات في Spring للقواعد التي تصل إلى قاعدة البيانات.

أفضل طريقة لتحقيق ذلك هي استخدام `ExecutorService` مقترنًا بـ `CompletionService`. يسمح لك `CompletionService` بمعالجة نتائج المهام عند اكتمالها، مما يتيح الكشف الفوري عن الفشل وإلغاء المهام المعلقة.

---

### الحل خطوة بخطوة

#### 1. تعريف قواعد التحقق
يجب أن تكون كل قاعدة من القواعد العشرة مهمة تحقق مستقلة. قد تتضمن بعض القواعد الوصول إلى قاعدة البيانات، لذا قم بتغليفها في خدمة ذات طرق معاملاتية.

```java
@Service
public class RuleValidator {
    // مثال: قاعدة تصل إلى قاعدة البيانات
    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // محاكاة تحقق القاعدة، مثل استعلام قاعدة البيانات
        // إرجاع true إذا نجحت القاعدة، false إذا فشلت
        return performValidation(ruleId); // التنفيذ يعتمد على منطقك
    }

    private boolean performValidation(int ruleId) {
        // استبدل بمنطق التحقق الفعلي
        return ruleId % 2 == 0; // مثال: القواعد ذات الأرقام الزوجية تمر
    }
}
```

- استخدم `@Transactional(readOnly = true)` للقواعد التي تقرأ فقط من قاعدة البيانات، لضمان تشغيل كل منها في سياق معاملتها الخاص بطريقة آمنة للخيوط.

#### 2. تكوين ExecutorService
حدد مجموعة خيوط لإدارة التنفيذ المتزامن لمهام التحقق. في Spring، يمكنك إنشاؤها كـ bean:

```java
@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // 10 خيوط لـ 10 قواعد
    }
}
```

- اضبط حجم مجموعة الخيوط بناءً على إمكانيات نظامك (مثل نوى المعالج، حدود اتصال قاعدة البيانات).

#### 3. تنفيذ التحقق متعدد الخيوط
أنشئ خدمة تنظم عملية التحقق باستخدام `CompletionService`:

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

    public boolean validateAllRules() {
        // الخطوة 1: إنشاء مهام التحقق
        List<Callable<Boolean>> tasks = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            tasks.add(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    // معالجة الاستثناءات (مثل أخطاء قاعدة البيانات) كفشل
                    log.error("Validation failed for rule " + ruleId, e);
                    return false;
                }
            });
        }

        // الخطوة 2: إعداد CompletionService وإرسال المهام
        CompletionService<Boolean> completionService = new ExecutorCompletionService<>(executorService);
        List<Future<Boolean>> futures = new ArrayList<>();
        for (Callable<Boolean> task : tasks) {
            futures.add(completionService.submit(task));
        }

        // الخطوة 3: معالجة النتائج عند اكتمالها
        boolean hasFailed = false;
        for (int i = 0; i < 10; i++) {
            try {
                Future<Boolean> completed = completionService.take(); // يحجب حتى اكتمال المهمة التالية
                boolean result = completed.get();
                if (!result) {
                    hasFailed = true;
                    break; // التوقف عن الفحص بمجرد العثور على فشل
                }
            } catch (InterruptedException | ExecutionException e) {
                log.error("Error during validation", e);
                hasFailed = true;
                break;
            }
        }

        // الخطوة 4: إلغاء المهام المتبقية إذا حدث فشل
        if (hasFailed) {
            for (Future<Boolean> future : futures) {
                if (!future.isDone()) {
                    future.cancel(true); // مقاطعة المهام قيد التشغيل
                }
            }
            return false; // فشل التحقق
        }

        return true; // جميع القواعد نجحت
    }
}
```

#### آلية العمل
- **إنشاء المهام**: يتم تغليف كل قاعدة تحقق في `Callable<Boolean>` تُرجع `true` إذا نجحت القاعدة و`false` إذا فشلت. يتم التقاط الاستثناءات ومعاملتها كفشل.
- **التنفيذ المتزامن**: يتم إرسال المهام إلى `CompletionService`، الذي يشغلها بالتوازي باستخدام مجموعة الخيوط. يتم جمع الـ Futures لتتبع حالة المهمة.
- **معالجة النتائج**: `completionService.take()` تسترجع نتيجة المهمة التالية المكتملة. إذا كانت أي نتيجة `false`، تنكسر الحلقة، ويتم تعيين `hasFailed`.
- **الإلغاء**: عند الفشل، يتم إلغاء جميع المهام غير المنتهية باستخدام `future.cancel(true)`، والذي يحاول مقاطعة الخيوط قيد التشغيل.
- **النتيجة**: تُرجع `false` إذا فشلت أي قاعدة، و`true` إذا نجحت جميعها.

---

### الاعتبارات الرئيسية
- **الوصول إلى قاعدة البيانات**: نظرًا لأن القواعد قد تصل إلى قاعدة البيانات، فإن `@Transactional` تضمن عمليات آمنة للخيوط. تعمل كل مهمة في معاملتها الخاصة، وهو أمر مناسب للتحققات المستقلة.
- **إلغاء المهام**: إلغاء `Future` يقاطع الخيط، ولكن استعلامات قاعدة البيانات الجارية قد لا تتوقف فورًا. ومع ذلك، هذا يمنع المزيد من المعالجة ويسمح للخيط الرئيسي بالمتابعة.
- **معالجة الاستثناءات**: يتم التقاط الاستثناءات (مثل أخطاء قاعدة البيانات) داخل المهام ومعاملتها كفشل، مما يضمن سلوكًا قويًا.
- **حجم مجموعة الخيوط**: تم تعيينه إلى 10 للبساطة (خيط واحد لكل قاعدة)، لكن قم بالتحسين بناءً على احتياجات تطبيقك وموارده.

---

### لماذا هذا هو النهج الأفضل
- **الكفاءة**: تعمل عمليات التحقق بشكل متزامن، مما يقلل الوقت الإجمالي عند نجاح الجميع.
- **الإنهاء المبكر**: يسمح `CompletionService` بالكشف الفوري عن الفشل، ويوقف الإلغاء العمل غير الضروري.
- **البساطة**: يستفيد من أدوات التزامن القياسية في Java ويتكامل بسلاسة مع Spring Boot.
- **القابلية للتوسع**: يمكن توسعته بسهولة لقواعد أكثر عن طريق ضبط مجموعة الخيوط وقائمة المهام.

تم النظر في نهج بديلة مثل `CompletableFuture` أو استطلاع نتائج `Future` مع مهلات زمنية، لكن `CompletionService` أكثر بساطة لحالة الاستخدام هذه، حيث يتعامل بكفاءة مع النتائج بترتيب اكتمالها ويدعم الإلغاء.

---

### مثال للاستخدام
قم بحقن واستدعاء الخدمة في وحدة التحكم أو المنطق التجاري الخاص بك:

```java
@RestController
public class ValidationController {
    private final ValidationService validationService;

    @Autowired
    public ValidationController(ValidationService validationService) {
        this.validationService = validationService;
    }

    @GetMapping("/validate")
    public ResponseEntity<String> validate() {
        boolean result = validationService.validateAllRules();
        return ResponseEntity.ok(result ? "All rules passed" : "Validation failed");
    }
}
```

يلبي هذا الحل متطلباتك: يشغل 10 قواعد تحقق بالتوازي، ويلغي المهام المتبقية عند فشل واحدة، ويتجنب إهدار الوقت، كل ذلك مع التكامل النظيف مع Spring Boot.