---
audio: false
generated: true
lang: ar
layout: post
title: الخيوط الافتراضية
translated: true
type: note
---

الخيوط الافتراضية (Virtual Threads)، التي أُدخلت في جافا 19 كجزء من Project Loom، تقدم بديلاً خفيف الوزن للخيوط التقليدية (platform threads). تم تصميمها لتحسين قابلية التوسع وكفاءة التطبيقات من خلال تقليل النفقات العامة المرتبطة بإدارة الخيوط.

لاستخدام الخيوط الافتراضية مع Spring، ستحتاج إلى التأكد من أن بيئتك مهيأة لدعم جافا 19 أو إصدار أحدث، حيث أن الخيوط الافتراضية هي ميزة في هذه الإصدارات. إليك دليل عام حول كيفية دمج الخيوط الافتراضية مع تطبيق Spring:

### 1. **إعداد بيئتك**

- **إصدار جافا**: تأكد من استخدامك جافا 19 أو إصدار أحدث. يمكنك التحقق من إصدار جافا باستخدام الأمر `java -version`.
- **إصدار Spring Boot**: تأكد من استخدامك إصدارًا من Spring Boot يدعم جافا 19 أو إصدار أحدث.

### 2. **تمكين الخيوط الافتراضية**

يمكن استخدام الخيوط الافتراضية في تطبيق Spring الخاص بك عن طريق تكوين التطبيق لاستخدامها. إليك كيف يمكنك القيام بذلك:

#### **أ. تكوين خدمة المُنفذ (Executor Service)**

يمكنك تكوين `ExecutorService` لاستخدام الخيوط الافتراضية. يمكن القيام بذلك في فئة التكوين الخاصة بـ Spring:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Configuration
public class VirtualThreadConfig {

    @Bean
    public ExecutorService virtualThreadExecutor() {
        return Executors.newVirtualThreadPerTaskExecutor();
    }
}
```

#### **ب. استخدام الخيوط الافتراضية في خدمتك**

يمكنك بعد ذلك حقن `ExecutorService` هذه في خدمات Spring الخاصة بك واستخدامها لتنفيذ المهام باستخدام الخيوط الافتراضية:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.concurrent.ExecutorService;

@Service
public class MyService {

    private final ExecutorService executorService;

    @Autowired
    public MyService(ExecutorService executorService) {
        this.executorService = executorService;
    }

    public void executeTask() {
        executorService.submit(() -> {
            // منطق المهمة هنا
            System.out.println("Task executed on a virtual thread: " + Thread.currentThread());
        });
    }
}
```

### 3. **اختبار الخيوط الافتراضية**

لاختبار ما إذا كانت الخيوط الافتراضية قيد الاستخدام، يمكنك تسجيل معلومات الخيط. سيكون لأسماء الخيوط الافتراضية ما يشير إلى أنها افتراضية، مثل `VirtualThread[#<id>]`.

### 4. **اعتبارات**

- **التوافق**: تأكد من أن جميع المكتبات والأطر التي تستخدمها متوافقة مع جافا 19 أو إصدار أحدث.
- **الأداء**: تم تصميم الخيوط الافتراضية لتحسين قابلية التوسع، ولكن لا يزال يتعين عليك تحليل أداء تطبيقك للتأكد من أنها توفر فوائد الأداء المتوقعة.
- **عمليات الحجب (Blocking Operations)**: الخيوط الافتراضية مفيدة بشكل خاص للمهام المرتبطة بالإدخال/الإخراج (I/O-bound). تأكد من أن تطبيقك مصمم للاستفادة من هذا.

باتباع هذه الخطوات، يمكنك دمج الخيوط الافتراضية في تطبيق Spring الخاص بك والاستفادة من مزاياها في قابلية التوسع.