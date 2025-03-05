---
audio: true
generated: true
lang: ar
layout: post
title: مؤشرات التطبيقات في جاڤا
translated: true
---

المكتبة `com.yammer.metrics`، التي تم تطويرها أصلاً من قبل Yammer، هي الآن جزء من مكتبة **Dropwizard Metrics**. تقدم طريقة قوية لتجميع وتقرير ميزات التطبيق في Java، مما يساعدك على مراقبة جوانب الأداء مثل عدد الطلبات، وقت الاستجابة، وغيرها. أدناه دليل على كيفية استخدامها بشكل فعال.

---

### الخطوة 1: إضافة التبعية
منذ أن تطور `com.yammer.metrics` إلى Dropwizard Metrics، يجب عليك استخدام مكتبة Dropwizard Metrics. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- استخدم أحدث الإصدار المتاح -->
</dependency>
```

حسب احتياجاتك، قد ترغب أيضًا في إضافة وحدات إضافية مثل:
- `metrics-jvm` لميزات JVM.
- `metrics-httpclient` لميزات عميل HTTP.
- `metrics-jersey` لتكامل مع إطار عمل Jersey.

تحقق من [توثيق Dropwizard Metrics](https://metrics.dropwizard.io/) للحصول على أحدث الإصدار والموحدات المتاحة.

---

### الخطوة 2: إنشاء سجل مقياس
`MetricRegistry` هو المكان المركزي حيث يتم تخزين جميع المقياسات. عادةً ما تخلق نسخة واحدة من التطبيق:

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### الخطوة 3: استخدام أنواع مختلفة من المقياسات
Dropwizard Metrics يدعم عدة أنواع من المقياسات، كل منها مناسب لمتطلبات المراقبة المختلفة:

#### **المعدلات**
المعدلات تستخدم لتتبع القيم التي يمكن أن تزيد أو تنقص (مثل عدد الطلبات المعالجة).

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // زيادة بمقدار 1
counter.inc(5); // زيادة بمقدار 5
counter.dec();  // نقص بمقدار 1
```

#### **المقياسات**
المقياسات تقدم صورة فورية للقيمة في لحظة معينة (مثل حجم الطابور الحالي). يمكنك تعريف مقياس من خلال تنفيذ واجهة `Gauge`:

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // استبدل ببياناتك
    }
});
```

#### **التوزيعات**
التوزيعات تتبع توزيع القيم الإحصائي (مثل أحجام الطلبات):

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // تسجيل قيمة
```

#### **المقاييس**
المقاييس تقيس معدل الأحداث (مثل الطلبات في الثانية):

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // تسجيل حدث
```

#### **المقاييس الزمنية**
المقاييس الزمنية تقيس كل من معدل ووقت الأحداث (مثل وقت معالجة الطلب):

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // تقمص بعض العمل
    Thread.sleep(100);
} finally {
    context.stop(); // تسجيل الوقت
}
```

---

### الخطوة 4: تقرير المقياسات
لجعل المقياسات مفيدة، تحتاج إلى تقريرها في مكان ما. Dropwizard Metrics يدعم عدة مراسلين مثل الشاشة، JMX، أو Graphite. voici مثال على مراسل الشاشة الذي يوثق المقياسات كل 10 ثوان:

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // تقرير كل 10 ثوان
```

للاستخدام الإنتاجي، فكر في التكامل مع أنظمة مثل Graphite أو عرض المقياسات عبر JMX.

---

### الخطوة 5: التكامل مع الإطارات (اختياري)
إذا كنت تستخدم إطار عمل ويب مثل Jersey، يمكنك استخدام وحدة `metrics-jersey` لتسجيل تلقائي لنقاط النهاية الخاصة بك. بالإضافة إلى ذلك، يمكن أن تسهل علامات مثل `@Timed` أو `@Counted` جمع المقياسات:

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

أضف التبعية `metrics-jersey` واصفها مع تطبيق Jersey الخاص بك لتفعيل هذه الميزة.

---

### أفضل الممارسات
- **قواعد التسمية**: استخدم نظام تسمية هرمي للوضوح (مثل `com.example.myapp.requests.total`).
- **الأداء**: كن حذرًا من عدد وتكرار المقياسات، حيث يمكن أن تؤثر التجميع الزائد على الأداء.
- **التوثيق**: راجع [توثيق Dropwizard Metrics](https://metrics.dropwizard.io/) للحصول على أمثلة حديثة وميزات متقدمة.

---

### مثال: جمع كل شيء
هنا مثال بسيط يجمع بين عدة مفاهيم:

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // إنشاء مقياس
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // إنشاء مقياس زمني
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // تقمص العمل
        context.stop();

        // بدء مراسل الشاشة
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // الحفاظ على تشغيل البرنامج لرؤية التقارير
        Thread.sleep(5000);
    }
}
```

هذا الكود يتبع مقياس ومقياس زمني، ويبلغ عن النتائج إلى الشاشة كل ثانية.

---

### الملاحظات النهائية
المكتبة `com.yammer.metrics` تطورت إلى Dropwizard Metrics، لذا استخدم دائمًا أحدث الإصدار من مجموعة `io.dropwizard.metrics`. إذا كنت تبدأ مشروعًا جديدًا، قد ترغب أيضًا في استكشاف بدائل حديثة مثل Micrometer، ولكن Dropwizard Metrics يبقى خيارًا قويًا لعديد من تطبيقات Java. للحصول على مزيد من التفاصيل، راجع الوثائق الرسمية!