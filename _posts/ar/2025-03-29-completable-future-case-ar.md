---
audio: false
generated: true
lang: ar
layout: post
title: تنفيذ التحقق متعدد الخيوط باستخدام كومبليتابلفيوتشر
translated: true
type: note
---

إذا استخدمنا `CompletableFuture` في تطبيق Spring Boot للتحقق متعدد الخيوط، فإنه يوفر طريقة حديثة ومرنة للتعامل مع المهام غير المتزامنة. أدناه، سأشرح كيفية تنفيذ ذلك، وسأسلط الضوء على مزاياه وتحدياته، وسأقدم حلاً كاملاً مخصصًا للتحقق من قواعد متعددة في وقت واحد.

### تنفيذ التحقق متعدد الخيوط باستخدام CompletableFuture

`CompletableFuture` هو جزء من واجهة برمجة التطبيقات (API) للتزامن في Java ويسمح لك بتنفيذ المهام بشكل غير متزامن، وتسلسل العمليات، والتعامل مع النتائج أو الاستثناءات بأناقة. إليك كيف يمكننا استخدامه للتحقق من قواعد متعددة بالتوازي، والتوقف بمجرد فشل إحداها.

#### الخطوة 1: تحديد منطق التحقق

أولاً، لنفترض أن لدينا خدمة تحدد قواعد تحقق فردية. قد تتضمن كل قاعدة الوصول إلى قاعدة بيانات أو منطق معقد، لذا سنستخدم شرح Spring `@Transactional` لإدارة المعاملات بشكل صحيح.

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class RuleValidator {

    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // محاكاة منطق التحقق (مثال: استعلام قاعدة بيانات)
        return performValidation(ruleId);
    }

    private boolean performValidation(int ruleId) {
        // مثال: القواعد ذات الأرقام الزوجية تمر، والفردية تفشل
        return ruleId % 2 == 0;
    }
}
```

#### الخطوة 2: تنفيذ خدمة التحقق باستخدام CompletableFuture

الآن، لننشئ خدمة تشغل قواعد تحقق متعددة في وقت واحد باستخدام `CompletableFuture`. سنستخدم `ExecutorService` لإدارة الخيوط وضمان أنه إذا فشلت أي قاعدة، يمكننا إيقاف معالجة الأخريات.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;

@Service
public class ValidationService {
    private static final Logger log = LoggerFactory.getLogger(ValidationService.class);
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    public boolean validateAllRules() {
        // إنشاء قائمة لحمل جميع الـ futures
        List<CompletableFuture<Boolean>> futures = new ArrayList<>();

        // إرسال 10 قواعد تحقق (على سبيل المثال)
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            CompletableFuture<Boolean> future = CompletableFuture.supplyAsync(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    log.error("Validation failed for rule " + ruleId, e);
                    return false; // معالجة الاستثناءات كفشل
                }
            }, executorService);
            futures.add(future);
        }

        // إنشاء future لتتبع النتيجة الإجمالية
        CompletableFuture<Boolean> resultFuture = new CompletableFuture<>();

        // مراقبة كل future للكشف عن الفشل
        for (CompletableFuture<Boolean> future : futures) {
            future.thenAccept(result -> {
                if (!result && !resultFuture.isDone()) {
                    // تم الكشف عن أول فشل
                    resultFuture.complete(false);
                    // إلغاء المهام المتبقية
                    futures.forEach(f -> {
                        if (!f.isDone()) {
                            f.cancel(true);
                        }
                    });
                }
            });
        }

        // إذا اكتملت جميع الـ futures بنجاح، ضع标记 كـ true
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]))
                .thenRun(() -> {
                    if (!resultFuture.isDone()) {
                        resultFuture.complete(true);
                    }
                });

        try {
            return resultFuture.get(); // حظر حتى تصبح النتيجة متاحة
        } catch (InterruptedException | ExecutionException e) {
            log.error("Error during validation", e);
            return false;
        }
    }
}
```

#### آلية العمل

1. **إرسال المهام**:
   - ننشئ `CompletableFuture` لكل قاعدة باستخدام `supplyAsync()`، والتي تشغل منطق التحقق بشكل غير متزامن.
   - يقوم `executorService` (يتم حقنه عبر Spring) بإدارة مجموعة الخيوط.

2. **الكشف عن الفشل**:
   - يتم مراقبة كل future باستخدام `thenAccept()`. إذا أرجعت أي قاعدة `false`، نكمل `resultFuture` بقيمة `false` ونلغي الـ futures المتبقية.

3. **حالة النجاح**:
   - ينتظر `CompletableFuture.allOf()` حتى تكتمل جميع الـ futures. إذا لم يحدث أي فشل، فإنه يكمل `resultFuture` بقيمة `true`.

4. **استرجاع النتيجة**:
   - نحجب على `resultFuture.get()` للحصول على النتيجة النهائية، مع معالجة أي استثناءات قد تحدث.

### مزايا استخدام CompletableFuture

- **المرونة**: يمكنك تسلسل العمليات (مثل `thenApply`، `thenCompose`) لمعالجة النتائج further إذا لزم الأمر.
- **معالجة الاستثناءات**: تجعل الطرق المدمجة مثل `exceptionally()` أو `handle()` من السهل إدارة الأخطاء.
- **التصميم غير المعيق**: يدعم نمط البرمجة التفاعلية، والذي يمكن توسيعه لسير عمل أكثر تعقيدًا.

### التحديات

- **الإلغاء**: على عكس `ExecutorService` مع `CompletionService` (حيث يمكنك بسهولة الاستفسار عن النتيجة الأولى وإلغاء الأخريات)، يتطلب `CompletableFuture` إلغاءً يدويًا للـ futures الأخرى عند فشل واحدة. وهذا يزيد من التعقيد.
- **التعقيد**: يمكن أن يصبح الكود أصعب في القراءة والصيانة مقارنة بنهج أبقي قائم على الحلقة مع `ExecutorService`.

### مثال الاستخدام

لاستخدام هذا في تطبيق Spring Boot، يمكنك تكوين حبة `ExecutorService`:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // ضبط الحجم حسب الحاجة
    }
}
```

ثم، استدعِ الخدمة من وحدة تحكم أو مكون آخر:

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

### خاتمة

يعد استخدام `CompletableFuture` للتحقق متعدد الخيوط في Spring Boot نهجًا قابلًا للتطبيق، خاصة إذا كنت تقدر طبيعته غير المتزامنة والقابلة للتسلسل. فهو يسمح لك بتشغيل قواعد التحقق في وقت واحد والتعامل مع النتائج بمرونة. ومع ذلك، إذا كان هدفك الأساسي هو البساطة - خاصة للكشف عن الفشل الأول وإلغاء المهام المتبقية - فقد يكون `ExecutorService` التقليدي مع `CompletionService` أسهل في التنفيذ والصيانة. مع `CompletableFuture`، تكتسب القوة والمرونة على حساب منطق إلغاء أكثر تعقيدًا قليلاً.