---
audio: false
generated: true
lang: ar
layout: post
title: مستقبل مكتمل في جافا
translated: true
type: note
---

في مشروع Java Spring Boot، لا يوجد ما يعادل مباشرةً لـ `Promise.all` في JavaScript، الذي ينتظر اكتمال عدة وعود ويوفر نتائجها. ومع ذلك، يمكنك تحقيق وظيفة مماثلة — تشغيل مهام متعددة في وقت واحد في حلقة for واستخدام نتائجها بعد اكتمال جميع الخيوط — باستخدام `CompletableFuture` من حزمة `java.util.concurrent`، تحديدًا باستخدام طريقة `CompletableFuture.allOf`. هذا النهج مناسب جدًا لمشروع Spring Boot، خاصة عند دمجه مع ميزات البرمجة غير المتزامنة في Spring. أدناه، سأشرح كيفية القيام بذلك خطوة بخطوة، بما في ذلك مثال كامل.

### لماذا `CompletableFuture`؟
`CompletableFuture` (المقدمة في Java 8) تسمح لك بتنفيذ عمليات غير متزامنة وإدارة اكتمالها. تأخذ طريقة `allOf` عدة نماذج من `CompletableFuture` وتُرجع `CompletableFuture` جديدة تنتهي عندما تنتهي جميع الـ Futures المعطاة، مما يجعلها مثالية لسيناريوك حيث تريد:
- تنفيذ مهام بالتوازي داخل حلقة for.
- الانتظار حتى تنتهي جميع المهام.
- استخدام النتائج بعد ذلك.

### خطوات التنفيذ
إليك كيف يمكنك هيكلة الحل الخاص بك في مشروع Spring Boot:

1. **تحديد المهام غير المتزامنة**
   تمثل كل تكرار في حلقة for الخاص بك مهمة يمكنها التشغيل بشكل مستقل. سترجع هذه المهام نماذج `CompletableFuture`، تمثل نتائجها في النهاية.

2. **جمع الـ Futures**
   قم بتخزين جميع كائنات `CompletableFuture` في قائمة أثناء إنشائها في الحلقة.

3. **الانتظار حتى اكتمال جميع المهام**
   استخدم `CompletableFuture.allOf` لدمج الـ Futures في future واحدة تنتهي عندما تنتهي جميع المهام.

4. **استرداد النتائج واستخدامها**
   بعد اكتمال جميع المهام، استخرج النتائج من كل `CompletableFuture` وقم بمعالجتها حسب الحاجة.

5. **معالجة الاستثناءات**
   ضع في الاعتبار الأخطاء المحتملة أثناء تنفيذ المهمة.

### مثال على التنفيذ
لنفترض أن لديك قائمة من العناصر لمعالجتها في وقت واحد (مثل استدعاء خدمة أو إجراء بعض الحسابات). فيما يلي نهجان: أحدهما يستخدم شرح Spring `@Async` والآخر يستخدم `CompletableFuture.supplyAsync`.

#### النهج 1: استخدام `@Async` مع Spring
يوفر Spring Boot شرح `@Async` لتشغيل الأساليب بشكل غير متزامن. ستحتاج إلى تمكين دعم غير المتزامن في تطبيقك.

**الخطوة 1: تمكين دعم غير المتزامن**
أضف شرح `@EnableAsync` إلى فئة التكوين أو فئة التطبيق الرئيسية:

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

@SpringBootApplication
@EnableAsync
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

**الخطوة 2: تحديد خدمة بطريقة غير متزامنة**
أنشئ خدمة تحتوي على طريقة تعالج كل عنصر بشكل غير متزامن:

```java
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import java.util.concurrent.CompletableFuture;

@Service
public class MyService {

    @Async
    public CompletableFuture<String> processItem(String item) {
        // محاكاة بعض العمل (مثل I/O أو حساب)
        try {
            Thread.sleep(1000); // تأخير لمدة ثانية واحدة
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return CompletableFuture.completedFuture("Interrupted: " + item);
        }
        return CompletableFuture.completedFuture("Processed: " + item);
    }
}
```

**الخطوة 3: معالجة العناصر في وحدة تحكم أو خدمة**
في وحدة التحكم أو خدمة أخرى، استخدم حلقة for لإرسال المهام والانتظار لجميع النتائج:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.concurrent.CompletableFuture;

@Component
public class ItemProcessor {

    @Autowired
    private MyService myService;

    public List<String> processItems(List<String> items) {
        // قائمة لحمل جميع الـ Futures
        List<CompletableFuture<String>> futures = new ArrayList<>();

        // إرسال كل مهمة في حلقة for
        for (String item : items) {
            CompletableFuture<String> future = myService.processItem(item);
            futures.add(future);
        }

        // الانتظار حتى اكتمال جميع المهام
        CompletableFuture<Void> allFutures = CompletableFuture.allOf(
            futures.toArray(new CompletableFuture[0])
        );

        // حظر حتى تنتهي جميع المهام
        allFutures.join();

        // جمع النتائج
        List<String> results = futures.stream()
            .map(CompletableFuture::join) // الحصول على كل نتيجة
            .collect(Collectors.toList());

        return results;
    }
}
```

**مثال على الاستخدام:**
```java
List<String> items = Arrays.asList("Item1", "Item2", "Item3");
List<String> results = itemProcessor.processItems(items);
System.out.println(results); // يطبع: [Processed: Item1, Processed: Item2, Processed: Item3]
```

#### النهج 2: استخدام `CompletableFuture.supplyAsync`
إذا كنت تفضل عدم استخدام `@Async`، يمكنك إدارة الخيوط يدويًا باستخدام `Executor` و `CompletableFuture.supplyAsync`.

**الخطوة 1: تكوين مجموعة الخيوط**
حدد `TaskExecutor` bean للتحكم في مجموعة الخيوط:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.core.task.TaskExecutor;

@Configuration
public class AsyncConfig {

    @Bean
    public TaskExecutor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);    // عدد الخيوط التي يجب الاحتفاظ بها في المجموعة
        executor.setMaxPoolSize(10);    // الحد الأقصى لعدد الخيوط
        executor.setQueueCapacity(25);  // سعة قائمة الانتظار للمهام المعلقة
        executor.initialize();
        return executor;
    }
}
```

**الخطوة 2: معالجة العناصر باستخدام `supplyAsync`**
استخدم المنفذ لتشغيل المهام بشكل غير متزامن:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.stream.Collectors;
import org.springframework.core.task.TaskExecutor;

@Component
public class ItemProcessor {

    @Autowired
    private TaskExecutor taskExecutor;

    public List<String> processItems(List<String> items) {
        // إنشاء Futures باستخدام supplyAsync
        List<CompletableFuture<String>> futures = items.stream()
            .map(item -> CompletableFuture.supplyAsync(() -> processItem(item), taskExecutor))
            .collect(Collectors.toList());

        // الانتظار حتى اكتمال جميع المهام
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).join();

        // جمع النتائج
        List<String> results = futures.stream()
            .map(CompletableFuture::join)
            .collect(Collectors.toList());

        return results;
    }

    private String processItem(String item) {
        // محاكاة بعض العمل
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return "Interrupted: " + item;
        }
        return "Processed: " + item;
    }
}
```

### النقاط الرئيسية
- **الانتظار حتى الاكتمال**: يضمن `CompletableFuture.allOf(...).join()` أو `.get()` أن الخيط الرئيسي ينتظر حتى تنتهي جميع المهام. استخدم `join()` لتجنب معالجة الاستثناءات المفحوصة؛ فإنه يلقي `CompletionException` إذا فشلت مهمة.
- **معالجة الاستثناءات**: لف استدعاء `.join()` أو `.get()` في كتلة try-catch إذا كنت بحاجة إلى معالجة الاستثناءات:

```java
try {
    allFutures.get();
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    // معالجة المقاطعة
} catch (ExecutionException e) {
    // معالجة فشل المهام
    e.printStackTrace();
}
```

- **تكوين مجموعة الخيوط**: اضبط حجم مجموعة الخيوط بناءً على عبء العمل الخاص بك. للمهام المرتبطة بـ I/O (مثل استدعاءات قاعدة البيانات، طلبات API)، مجموعة أكبر (مثل 5-10 خيوط) جيدة. للمهام المرتبطة بوحدة المعالجة المركزية، طابق عدد نوى وحدة المعالجة المركزية (مثل `Runtime.getRuntime().availableProcessors()`).
- **ترتيب النتيجة**: تحافظ النتائج على ترتيب قائمة الإدخال حيث يتم جمع الـ Futures بنفس ترتيب الحلقة.

### أي نهج تختار؟
- **استخدم `@Async`** إذا كانت مهامك جزءًا طبيعيًا من خدمة Spring وتريد من Spring إدارة الخيوط. إنه أكثر نظافة ويتكامل جيدًا مع Spring Boot.
- **استخدم `supplyAsync`** إذا كنت بحاجة إلى مزيد من التحكم في تنفيذ المهمة أو لا تريد الاعتماد على إطار العمل غير المتزامن لـ Spring.

### الإجابة النهائية
لتكرار `Promise.all` في مشروع Java Spring Boot لوظيفة حلقة for حيث تريد استخدام نتائج الخيوط بعد التنفيذ متعدد الخيوط، استخدم `CompletableFuture.allOf` مع قائمة من نماذج `CompletableFuture`. يوصى بنهج `@Async` مع Spring للبساطة، لكن `supplyAsync` مع منفذ مخصص يعمل أيضًا. يوضح المثال أعلاه مع `@Async` هذا:

- أنشئ نماذج `CompletableFuture` في حلقة for باستخدام طريقة `@Async`.
- استخدم `CompletableFuture.allOf` للانتظار لجميع المهام.
- اجمع النتائج واستخدمها بعد الاكتمال.

هذا يضمن تشغيل جميع المهام في وقت واحد، ويمكنك معالجة نتائجها بمجرد انتهائها جميعًا، مما يلبي متطلباتك بشكل فعال.