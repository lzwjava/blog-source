---
audio: false
generated: true
lang: ar
layout: post
title: الوصول إلى سياق تطبيق سبرينغ
translated: true
type: note
---

لاستخدام واجهة `ApplicationContextAware` الخاصة بـ Spring للوصول إلى `ApplicationContext` في كائن Java عادي، مثل مستهلك Kafka، تحتاج إلى طريقة لربط حبوب (beans) التي تديرها Spring بكائنك العادي. إليك كيف يمكنك القيام بذلك:

### النهج العام
تسمح واجهة `ApplicationContextAware` لحبة (bean) تديرها Spring باستقبال `ApplicationContext` تلقائيًا من Spring. يمكنك استخدام هذا لجعل السياق متاحًا لكائن Java عادي لا تديره Spring (أي ليس حبة (bean) تم إنشاؤها بواسطة حاوية Spring).

#### خطوات الوصول إلى ApplicationContext
1. **إنشاء فئة مساعدة تديرها Spring**:
   عرّف فئة تنفذ `ApplicationContextAware` وتديرها Spring (على سبيل المثال، مع شرح `@Component`). ستستقبل هذه الفئة `ApplicationContext` عندما يبدأ تطبيق Spring.

   ```java
   import org.springframework.context.ApplicationContext;
   import org.springframework.context.ApplicationContextAware;
   import org.springframework.stereotype.Component;

   @Component
   public class ApplicationContextProvider implements ApplicationContextAware {
       private static ApplicationContext context;

       @Override
       public void setApplicationContext(ApplicationContext applicationContext) {
           context = applicationContext;
       }

       public static ApplicationContext getApplicationContext() {
           return context;
       }
   }
   ```

   - `@Component` تضمن أن Spring تدير هذه الحبة (bean).
   - يتم استدعاء `setApplicationContext` من قبل Spring لحقن `ApplicationContext`.
   - يسمح المتغير الساكن `context` وطريقة الاسترجاع (getter) بالوصول من أي مكان.

2. **الوصول إلى السياق في كائن Java العادي الخاص بك**:
   في كائن Java العادي الخاص بك (على سبيل المثال، مستهلك Kafka تم إنشاؤه يدويًا)، استرجع `ApplicationContext` باستخدام فئة المساعد واستخدمه للحصول على الحبوب (beans) التي تديرها Spring.

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // استخدم الخدمة أو الحبوب الأخرى حسب الحاجة
       }
   }
   ```

   - يعمل هذا لأن `ApplicationContextProvider` يتم تهيئته بواسطة Spring عند بدء التشغيل، مما يجعل السياق متاحًا بشكل ساكن.

3. **بديل: تمرير السياق بشكل صريح**:
   إذا كان كائن Java العادي الخاص بك يتم إنشاؤه بواسطة حبة (bean) تديرها Spring، فيمكنك حقن `ApplicationContext` تلقائيًا (autowire) في تلك الحبة وتمريره إلى الكائن العادي عبر المُنشئ (constructor) أو setter.

   ```java
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.context.ApplicationContext;
   import org.springframework.stereotype.Component;

   @Component
   public class KafkaConsumerCreator {
       @Autowired
       private ApplicationContext context;

       public MyKafkaConsumer createConsumer() {
           return new MyKafkaConsumer(context);
       }
   }

   public class MyKafkaConsumer {
       private final ApplicationContext context;

       public MyKafkaConsumer(ApplicationContext context) {
           this.context = context;
       }

       public void processMessage() {
           SomeService service = context.getBean(SomeService.class);
           // استخدم الخدمة
       }
   }
   ```

   - يتجنب هذا المتغيرات الساكنة، مما يجعل التبعية صريحة ويحسن قابلية الاختبار.

### حل خاص بمستهلك Kafka
إذا كنت تعمل مع مستهلك Kafka وتستخدم **Spring Kafka**، فإن النهج الموصى به هو دمج المستهلك مباشرة في نظام Spring البيئي بدلاً من التعامل معه ككائن Java عادي.

#### استخدام `@KafkaListener`
عرّف مستهلك Kafka الخاص بك كحبة (bean) تديرها Spring مع طريقة `@KafkaListener`. هذا يسمح لك بحقن `ApplicationContext` أو الحبوب الأخرى تلقائيًا (autowire) مباشرة.

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class MyKafkaConsumer {
    @Autowired
    private ApplicationContext context;

    @Autowired
    private SomeService someService;

    @KafkaListener(topics = "my-topic")
    public void consume(String message) {
        // استخدم context أو someService مباشرة
        SomeService service = context.getBean(SomeService.class); // إذا لزم الأمر
        someService.process(message);
    }
}
```

- تدير Spring Kafka دورة حياة المستهلك، بما في ذلك الخيوط (threading) والاستطلاع (polling).
- يلغي الحقن التلقائي (Autowiring) الحاجة إلى جلب السياق يدويًا في معظم الحالات.

#### مستهلك Kafka يدوي
إذا كان يجب عليك إنشاء `KafkaConsumer` يدويًا (على سبيل المثال، باستخدام مكتبة عميل Kafka مباشرة)، فافعل ذلك داخل حبة (bean) تديرها Spring ومرر `ApplicationContext` إليها، كما هو موضح في نهج التمرير الصريح أعلاه.

### التوصيات
- **لمستهلكي Kafka**: استخدم `@KafkaListener` الخاص بـ Spring Kafka في حبة (bean) تديرها Spring حيثما أمكن. هذا يستفيد من تكامل Spring مع Kafka ويبسط الوصول إلى `ApplicationContext` والحبوب الأخرى.
- **لكائنات Java العادية العامة**: إما استخدم نهج `ApplicationContextProvider` الساكن أو مرر `ApplicationContext` بشكل صريح من حبة (bean) تديرها Spring. يُفضل طريقة التمرير الصريح عندما تكون ممكنة، لأنها تتجنب الحالة الساكنة (static state) وتحسن قابلية الاختبار.

باتباع هذه الطرق، يمكنك استخدام `ApplicationContextAware` بشكل فعال لجعل سياق Spring متاحًا لكائن Java العادي الخاص بك، بما في ذلك مستهلك Kafka، اعتمادًا على إعدادك المحدد.