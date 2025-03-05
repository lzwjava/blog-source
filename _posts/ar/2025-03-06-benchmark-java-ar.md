---
audio: false
generated: true
lang: ar
layout: post
title: 'Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java


  Benchmarking in Java'
translated: true
---

الهيكل الأساسي لمقياس الأداء الميكرو (JMH) هو أداة قوية لبناء، تشغيل، وتحليل مقياس الأداء الميكرو في جاڤا. يسمح للمطورين بمقاس أداء كودهم بطريقة مضبوطة ومكررة. أدناه دليل شامل على كيفية استخدام JMH بشكل فعال.

---

## 1. إعداد مشروعك

لاستخدام JMH، عليك تضمينه في مشروعك. إليك كيفية القيام بذلك باستخدام Maven أو Gradle:

### **Maven**
أضف التبعيات التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.openjdk.jmh</groupId>
    <artifactId>jmh-core</artifactId>
    <version>1.36</version>
</dependency>
<dependency>
    <groupId>org.openjdk.jmh</groupId>
    <artifactId>jmh-generator-annprocess</artifactId>
    <version>1.36</version>
    <scope>provided</scope>
</dependency>
```

### **Gradle**
أضف هذه السطور إلى ملف `build.gradle` الخاص بك:

```groovy
dependencies {
    implementation 'org.openjdk.jmh:jmh-core:1.36'
    annotationProcessor 'org.openjdk.jmh:jmh-generator-annprocess:1.36'
}
```

توفر هذه التبعيات مكتبة JMH الأساسية ومعالج التعليقات اللازمة لتوليد كود المقياس.

---

## 2. كتابة مقياسك

إنشاء فئة جاڤا لتحديد مقياسك. استخدم تعليق `@Benchmark` لتحديد الطرق التي تريد قياسها. إليك مثال بسيط:

```java
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import java.util.concurrent.TimeUnit;

public class MyBenchmark {

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    @OutputTimeUnit(TimeUnit.NANOSECONDS)
    public void testMethod() {
        // كود المقياس
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`**: يحدد الطريقة كهدف للمقياس.
- **`@BenchmarkMode`**: يحدد كيفية قياس الأداء (مثل `Mode.AverageTime` لمتوسط الوقت التنفيذ).
- **`@OutputTimeUnit`**: يحدد وحدة الوقت للنتائج (مثل `TimeUnit.NANOSECONDS`).

---

## 3. تهيئة المقياس

يمكنك تخصيص مقياسك باستخدام تعليقات JMH الإضافية:

- **`@Warmup`**: يحدد المرحلة التمهيدية (مثل `@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Measurement`**: يحدد المرحلة القياسية (مثل `@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Fork`**: يحدد عدد عمليات التفرع JVM (مثل `@Fork(value = 1)` لتشغيل في حالة JVM واحدة).
- **`@State`**: يحدد نطاق كائنات الحالة (مثل `@State(Scope.Thread)` للحالة المحلية للخط).

مثال مع التهيئة:

```java
@State(Scope.Thread)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
public class MyBenchmark {
    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    @OutputTimeUnit(TimeUnit.SECONDS)
    public void testMethod() {
        // كود المقياس
    }
}
```

---

## 4. تشغيل المقياس

لإجراء مقياسك، يمكنك استخدام مشغل JMH. إليك كيفية القيام بذلك باستخدام Maven:

### **إضافة مشغل Maven Shade**
أضف هذا إلى ملف `pom.xml` الخاص بك لإنشاء ملف JAR قابل للتنفيذ:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-shade-plugin</artifactId>
            <version>3.2.4</version>
            <executions>
                <execution>
                    <phase>package</phase>
                    <goals>
                        <goal>shade</goal>
                    </goals>
                    <configuration>
                        <finalName>benchmarks</finalName>
                        <transformers>
                            <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                <mainClass>org.openjdk.jmh.Main</mainClass>
                            </transformer>
                        </transformers>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

### **بناء و تشغيل**
1. بناء الملف JAR: `mvn clean package`
2. تشغيل المقياس: `java -jar target/benchmarks.jar`

سيقوم JMH بتنفيذ المقياسات ويظهر النتائج في شاشة المخرج.

---

## 5. تحليل النتائج

يخرج JMH مقاييس الأداء بناءً على تهيئةك. على سبيل المثال:

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode**: نمط المقياس (مثل `avgt` لمتوسط الوقت).
- **Cnt**: عدد تكرار القياس.
- **Score**: الأداء المقاس (مثل متوسط الوقت في النانو ثانية لكل عملية).
- **Error**: هامش الخطأ.
- **Units**: وحدة القياس.

استخدم هذه النتائج لتقييم وتحسين أداء كودك.

---

## 6. الميزات المتقدمة

يقدم JMH أدوات إضافية لمواقف أكثر تعقيدًا:

### **التعليمات**
اختبر كودك مع مدخلات مختلفة باستخدام `@Param`:

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // كود المقياس
        }
    }
}
```

### **الفراغات السوداء**
منع JVM من تحسين الكود غير المستخدم باستخدام `Blackhole`:

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // يمنع إزالة الكود الميت
}
```

---

## 7. أفضل الممارسات

- **تسخين JVM**: دائمًا تضمين مرحلة التسخين لضمان أن يOptimize JIT Compiler كودك قبل القياس.
- **اختيار النمط الصحيح**: استخدم `Mode.AverageTime` للاتساق، `Mode.Throughput` لعملية الثانية، إلخ.
- **تحكم في البيئة**: قم بتنفيذ المقياسات على نظام مستقر لتجنب التدخل من العمليات الأخرى.
- **تجنب تحسينات**: استخدم الفراغات السوداء أو ميزات JMH الأخرى لمنع JVM من إزالة الكود.

---

بالتتبع لهذه الخطوات، يمكنك استخدام `org.openjdk.jmh` لمقاس وتحسين أداء كودك جاڤا بشكل دقيق. سواء كنت تستخدمن مقياسات بسيطة أو خوارزميات معقدة، يوفر JMH الأدوات التي تحتاجها لمقياس الأداء الموثوق.