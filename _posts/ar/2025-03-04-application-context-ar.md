---
audio: false
generated: true
lang: ar
layout: post
title: تسجيل الدخول إلى Spring's Application Context
translated: true
---

لاستخدام واجهة `ApplicationContextAware` من Spring للوصول إلى `ApplicationContext` في كائن Java عادي مثل مستهلك Kafka، تحتاج إلى طريقة لتجسيد الفاصلات بين الفاصلات التي يديرها Spring و كائنك العادي. إليك كيفية القيام بذلك:

### النهج العام
تسمح واجهة `ApplicationContextAware` لفاصلة يديرها Spring باستقبال `ApplicationContext` تلقائيًا من Spring. يمكنك استخدام هذا لتجعل السياق متاحًا لفاصلة Java عادية التي لا يديرها Spring (أي ليس فاصلة تم إنشاؤها بواسطة محول Spring).

#### خطوات للوصول إلى ApplicationContext
1. **إنشاء فئة مساعدة يديرها Spring**:
   حدد فئة تفعيل `ApplicationContextAware` وتديرها Spring (مثلًا، مع ملحق `@Component`). ستستقبل هذه الفئة `ApplicationContext` عندما يبدأ تطبيق Spring.

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

   - `@Component` يضمن أن Spring يدير هذه الفاصلة.
   - `setApplicationContext` يتم استدعاؤه من قبل Spring لإدخال `ApplicationContext`.
   - متغير `context` ثابت ومتغير getter يسمح بالوصول من أي مكان.

2. **الوصول إلى السياق في كائن Java العادي**:
   في كائن Java العادي (مثل مستهلك Kafka الذي تم إنشاؤه يدويًا)، استرجع `ApplicationContext` باستخدام فئة المساعدة واستخدمه للحصول على الفاصلات التي يديرها Spring.

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // استخدم الخدمة أو الفاصلات الأخرى حسب الحاجة
       }
   }
   ```

   - يعمل هذا لأن `ApplicationContextProvider` يتم تهيئته من قبل Spring عند بدء التشغيل، مما يجعل السياق متاحًا بشكل ثابت.

3. **البديل: تمرير السياق بشكل صريح**:
   إذا تم إنشاء كائن Java العادي من قبل فاصلة يديرها Spring، يمكنك استدعاء `ApplicationContext` إلى تلك الفاصلة وتمريره إلى الكائن العادي عبر بناء أو متغير setter.

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

   - هذا يجنب المتغيرات الثابتة، مما يجعل التبعية صريحة وتحسين قابلية الاختبار.

### حل خاص بمستهلك Kafka
إذا كنت تعمل مع مستهلك Kafka واستخدام **Spring Kafka**، فإن النهج الموصى به هو دمج المستهلك مباشرة في نظام Spring بدلاً من معالجته ككائن Java عادي.

#### باستخدام `@KafkaListener`
حدد مستهلك Kafka كفاصلة يديرها Spring مع طريقة `@KafkaListener`. هذا يسمح لك باستدعاء `ApplicationContext` أو الفاصلات الأخرى مباشرة.

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
        // استخدم السياق أو someService مباشرة
        SomeService service = context.getBean(SomeService.class); // إذا كان مطلوبًا
        someService.process(message);
    }
}
```

- Spring Kafka يدير دورة حياة المستهلك، بما في ذلك التثبيت والتدوير.
- الاستدعاء يبعد الحاجة إلى استخراج السياق يدويًا في معظم الحالات.

#### مستهلك Kafka يدوي
إذا كنت مضطرًا إلى إنشاء `KafkaConsumer` يدويًا (مثلًا، باستخدام مكتبة عميل Kafka مباشرة)، فافعل ذلك داخل فاصلة يديرها Spring وتمرير `ApplicationContext` إليها، كما هو موضح في النهج الصريح للتمرير أعلاه.

### التوصيات
- **لمستهلكات Kafka**: استخدم `@KafkaListener` من Spring Kafka في فاصلة يديرها Spring كلما أمكن. هذا يستفيد من التكامل بين Spring و Kafka ويبسط الوصول إلى `ApplicationContext` و الفاصلات الأخرى.
- **لكائنات Java العادية**: إما استخدم النهج الثابت `ApplicationContextProvider` أو تمرير `ApplicationContext` بشكل صريح من فاصلة يديرها Spring. يفضل النهج الصريح للتمرير عندما يكون ممكنًا، لأنه يبعد عن الحالة الثابتة ويحسن قابلية الاختبار.

بالتتبع لهذه الطرق، يمكنك استخدام `ApplicationContextAware` بشكل فعال لجعل السياق متاحًا لكائن Java العادي، بما في ذلك مستهلك Kafka، حسب إعدادك الخاص.