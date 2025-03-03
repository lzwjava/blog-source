---
audio: false
generated: true
lang: ar
layout: post
title: تسجيل الدخول إلى Spring's ApplicationContext
translated: true
---

لاستخدام واجهة `ApplicationContextAware` من Spring للوصول إلى `ApplicationContext` في كائن Java عادي مثل مستهلك Kafka، تحتاج إلى طريقة لتجسيد beans التي يديرها Spring مع كائنك العادي. إليك كيفية القيام بذلك:

### النهج العام
تسمح واجهة `ApplicationContextAware` لbean يديره Spring باستقبال `ApplicationContext` تلقائيًا من Spring. يمكنك استخدام هذا لتجعل السياق متاحًا لكائن Java عادي لا يديره Spring (أي ليس beanًا تم إنشاؤه بواسطة محرك Spring).

#### خطوات للوصول إلى ApplicationContext
1. **إنشاء فئة مساعدة يديرها Spring**:
   حدد فئة تنفذ `ApplicationContextAware` وتديرها Spring (مثلًا مع Annotation `@Component`). ستتلقى هذه الفئة `ApplicationContext` عندما يبدأ تطبيق Spring.

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

   - `@Component` يضمن أن Spring يدير هذا bean.
   - `setApplicationContext` يتم استدعاؤه من Spring لإدخال `ApplicationContext`.
   - متغير `context` ثابت ومتغير getter يسمح بالوصول من أي مكان.

2. **الوصول إلى السياق في كائنك Java العادي**:
   في كائنك Java العادي (مثل مستهلك Kafka يتم إنشاؤه يدويًا)، استرجع `ApplicationContext` باستخدام فئة المساعدة واستخدمه للحصول على beans يديرها Spring.

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // استخدم الخدمة أو beans الأخرى حسب الحاجة
       }
   }
   ```

   - هذا يعمل لأن `ApplicationContextProvider` يتم تهيئته من Spring عند البدء، مما يجعل السياق متاحًا بشكل ثابت.

3. **البديل: تمرير السياق بشكل صريح**:
   إذا كان كائنك Java العادي يتم إنشاؤه من bean يديره Spring، يمكنك استدعاء `ApplicationContext` إلى ذلك bean وتمريره إلى الكائن العادي عبر بناء أو setter.

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

   - هذا يجنب المتغيرات الثابتة، مما يجعل التبعية صريحة ويحسن قابلية الاختبار.

### حل خاص بمستهلك Kafka
إذا كنت تعمل مع مستهلك Kafka وتستخدم **Spring Kafka**، فإن النهج الموصى به هو دمج المستهلك مباشرة في نظام Spring بدلاً من معالجته ككائن Java عادي.

#### استخدام `@KafkaListener`
حدد مستهلك Kafka كbean يديره Spring مع طريقة `@KafkaListener`. هذا يسمح لك باستدعاء `ApplicationContext` أو beans أخرى مباشرة.

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
        SomeService service = context.getBean(SomeService.class); // إذا كان مطلوبًا
        someService.process(message);
    }
}
```

- Spring Kafka يدير دورة حياة المستهلك، بما في ذلك التثبيت والتدوير.
- الاستدعاء يبعد الحاجة إلى استخراج السياق يدويًا في معظم الحالات.

#### مستهلك Kafka يدوي
إذا كنت مضطرًا إلى إنشاء `KafkaConsumer` يدويًا (مثلًا باستخدام مكتبة عملاء Kafka مباشرة)، فافعل ذلك داخل bean يديره Spring وتمرير `ApplicationContext` إليه، كما هو موضح في النهج الصريح للتمرير أعلاه.

### توصيات
- **لمستهلكات Kafka**: استخدم `@KafkaListener` من Spring Kafka في bean يديره Spring كلما أمكن. هذا يستفيد من التكامل بين Spring وKafka ويبسط الوصول إلى `ApplicationContext` وbeans الأخرى.
- **لكائنات Java العادية**: إما استخدم النهج الثابت `ApplicationContextProvider` أو تمرير `ApplicationContext` بشكل صريح من bean يديره Spring. يفضل النهج الصريح للتمرير عندما يكون ممكنًا، لأنه يبعد المتغيرات الثابتة ويحسن قابلية الاختبار.

بالتتبع لهذه الطرق، يمكنك استخدام `ApplicationContextAware` بشكل فعال لجعل السياق متاحًا لكائنك Java العادي، بما في ذلك مستهلك Kafka، حسب إعدادك الخاص.