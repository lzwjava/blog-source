---
audio: false
generated: true
lang: ar
layout: post
title: مقاييس التطبيقات في جافا
translated: true
type: note
---

مكتبة `com.yammer.metrics`، التي تم تطويرها أصلاً بواسطة Yammer، أصبحت الآن جزءًا من مكتبة **Dropwizard Metrics**. توفر طريقة قوية لجمع وإعداد تقارير مقاييس التطبيقات في Java، مما يساعدك على مراقبة جوانب الأداء مثل عدد الطلبات وأوقات الاستجابة والمزيد. فيما يلي دليل حول كيفية استخدامها بفعالية.

---

### الخطوة 1: إضافة التبعية
نظرًا لأن `com.yammer.metrics` تطورت إلى Dropwizard Metrics، يجب عليك استخدام مكتبة Dropwizard Metrics. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- استخدم أحدث إصدار متاح -->
</dependency>
```

اعتمادًا على احتياجاتك، قد ترغب أيضًا في وحدات إضافية، مثل:
- `metrics-jvm` للمقاييس المتعلقة بـ JVM.
- `metrics-httpclient` لمقاييس عميل HTTP.
- `metrics-jersey` للتكامل مع إطار عمل Jersey.

تحقق من [توثيق Dropwizard Metrics](https://metrics.dropwizard.io/) للحصول على أحدث إصدار والوحدات المتاحة.

---

### الخطوة 2: إنشاء سجل المقاييس
`MetricRegistry` هو المكان المركزي الذي يتم فيه تخزين جميع المقاييس. عادةً ما تقوم بإنشاء مثيل واحد لتطبيقك:

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### الخطوة 3: استخدام أنواع مختلفة من المقاييس
يدعم Dropwizard Metrics عدة أنواع من المقاييس، كل منها مناسب لاحتياجات مراقبة مختلفة:

#### **العدادات**
تُستخدم العدادات لتتبع القيم التي يمكن أن تزيد أو تنقص (مثل عدد الطلبات المعالجة).

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // زيادة بمقدار 1
counter.inc(5); // زيادة بمقدار 5
counter.dec();  // إنقاص بمقدار 1
```

#### **المقاييس**
توفر المقاييس لقطة لقيمة في لحظة محددة (مثل الحجم الحالي للطابور). يمكنك تعريف مقياس عن طريق تنفيذ واجهة `Gauge`:

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // استبدل هذا بمنطقك الخاص
    }
});
```

#### **الرسوم البيانية**
تتعقب الرسوم البيانية التوزيع الإحصائي للقيم (مثل أحجام الطلبات):

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // تسجيل قيمة
```

#### **المقاييس**
تقيس المقاييس معدل الأحداث (مثل الطلبات في الثانية):

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // تسجيل حدث
```

#### **الموقتات**
تقيس الموقتات كلًا من معدل ومدة الأحداث (مثل وقت معالجة الطلب):

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // محاكاة بعض العمل
    Thread.sleep(100);
} finally {
    context.stop(); // تسجيل المدة
}
```

---

### الخطوة 4: إعداد تقارير المقاييس
لجعل المقاييس مفيدة، تحتاج إلى إعداد تقارير بها في مكان ما. يدعم Dropwizard Metrics عدة أنواع من برامج الإبلاغ، مثل وحدة التحكم أو JMX أو Graphite. إليك مثال على برنامج إبلاغ عبر وحدة التحكم يسجل المقاييس كل 10 ثوانٍ:

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // الإبلاغ كل 10 ثوانٍ
```

للاستخدام في بيئة الإنتاج، فكر في التكامل مع أنظمة مثل Graphite أو عرض المقاييس عبر JMX.

---

### الخطوة 5: التكامل مع الأطر (اختياري)
إذا كنت تستخدم إطار عمل ويب مثل Jersey، فيمكنك استخدام وحدة `metrics-jersey` لأتمتة أدوات نقاط النهاية الخاصة بك تلقائيًا. بالإضافة إلى ذلك، يمكن للتعليقات التوضيحية مثل `@Timed` أو `@Counted` تبسيط جمع المقاييس:

```java
import com.codahale.metrics.annotation.Timed;

@Path("/example")
public class ExampleResource {
    @GET
    @Timed
    public String getExample() {
        return "Hello, world!";
    }
}
```

أضف تبعية `metrics-jersey` وقم بتكوينها مع تطبيق Jersey الخاص بك لتمكين هذه الميزة.

---

### أفضل الممارسات
- **اتفاقيات التسمية**: استخدم مخطط تسمية هرمي للوضوح (مثال: `com.example.myapp.requests.total`).
- **الأداء**: كن حذرًا بشأن عدد وتكرار المقاييس، حيث أن الجمع المفرط يمكن أن يؤثر على الأداء.
- **التوثيق**: راجع [توثيق Dropwizard Metrics](https://metrics.dropwizard.io/) للحصول على أمثلة محدثة وميزات متقدمة.

---

### مثال: جمع كل شيء معًا
إليك مثالًا بسيطًا يجمع بين عدة مفاهيم:

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // إنشاء عداد
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // إنشاء مؤقت
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // محاكاة العمل
        context.stop();

        // بدء برنامج إبلاغ عبر وحدة التحكم
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // إبقاء البرنامج قيد التشغيل لرؤية التقارير
        Thread.sleep(5000);
    }
}
```

يتعقب هذا الكود عدادًا ومؤقتًا، ويُعد تقارير بالنتائج إلى وحدة التحكم كل ثانية.

---

### ملاحظات ختامية
لقد تطورت مكتبة `com.yammer.metrics` إلى Dropwizard Metrics، لذا استخدم دائمًا أحدث إصدار من مجموعة `io.dropwizard.metrics`. إذا كنت تبدأ مشروعًا جديدًا، يمكنك أيضًا استكشاف بدائل حديثة مثل Micrometer، ولكن Dropwizard Metrics تظل خيارًا قويًا للعديد من تطبيقات Java. لمزيد من التفاصيل، تحقق من التوثيق الرسمي!