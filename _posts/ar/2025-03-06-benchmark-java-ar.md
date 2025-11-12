---
audio: false
generated: true
lang: ar
layout: post
title: معايير الأداء في جافا
translated: true
type: note
---

أداة Java Microbenchmark Harness (JMH) هي أداة قوية لبناء وتشغيل وتحليل المقاييس الدقيقة (microbenchmarks) في جافا. تتيح للمطورين قياس أداء كودهم بطريقة مضبوطة وقابلة للتكرار. فيما يلي دليل شامل حول كيفية استخدام JMH بفعالية.

---

## 1. إعداد مشروعك

لاستخدام JMH، تحتاج إلى تضمينه في مشروعك. إليك كيفية القيام بذلك باستخدام Maven أو Gradle:

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
أضف هذه الأسطر إلى ملف `build.gradle` الخاص بك:

```groovy
dependencies {
    implementation 'org.openjdk.jmh:jmh-core:1.36'
    annotationProcessor 'org.openjdk.jmh:jmh-generator-annprocess:1.36'
}
```

توفر هذه التبعيات مكتبة JMH الأساسية ومعالج الشرح (annotation processor) اللازم لتوليد كود المقاييس.

---

## 2. اكتب مقياسك (Benchmark)

أنشئ فئة جافا لتحديد المقياس الخاص بك. استخدم شرح `@Benchmark` لتحديد الطرق التي تريد قياسها. إليك مثال بسيط:

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
        // Code to benchmark
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`**: يحدد الطريقة كهدف للمقياس.
- **`@BenchmarkMode`**: يحدد كيفية قياس الأداء (مثل `Mode.AverageTime` لمتوسط وقت التنفيذ).
- **`@OutputTimeUnit`**: يحدد وحدة الوقت للنتائج (مثل `TimeUnit.NANOSECONDS`).

---

## 3. اضبط المقياس (Benchmark)

يمكنك تخصيص المقياس الخاص بك باستخدام شروحات JMH إضافية:

- **`@Warmup`**: يحدد مرحلة الإحماء (مثال: `@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Measurement`**: يهيء مرحلة القياس (مثال: `@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Fork`**: يحدد عدد عمليات JVM الفرعية (forks) المستخدمة (مثال: `@Fork(value = 1)` للتشغيل في نسخة JVM واحدة).
- **`@State`**: يحدد نطاق كائنات الحالة (مثال: `@State(Scope.Thread)` للحالة المحلية للخيط (thread-local state)).

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
        // Code to benchmark
    }
}
```

---

## 4. شغّل المقياس (Benchmark)

لتشغيل المقياس الخاص بك، يمكنك استخدام عداء (runner) JMH. إليك كيفية القيام بذلك باستخدام Maven:

### **أضف إضافة Maven Shade Plugin**
قم بتضمين هذا في ملف `pom.xml` الخاص بك لإنشاء JAR قابل للتنفيذ:

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

### **ابنِ وشغّل**
1. ابنِ ملف JAR: `mvn clean package`
2. شغّل المقياس: `java -jar target/benchmarks.jar`

سيقوم JMH بتنفيذ المقاييس وعرض النتائج في طرفيتك (terminal).

---

## 5. حلل النتائج

يخرج JMH مقاييس الأداء بناءً على تهيئتك. على سبيل المثال:

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode**: وضع المقياس (مثال: `avgt` لمتوسط الوقت).
- **Cnt**: عدد تكرارات القياس.
- **Score**: الأداء المقاس (مثال: متوسط الوقت بالنانوثانية لكل عملية).
- **Error**: هامش الخطأ.
- **Units**: وحدة القياس.

استخدم هذه النتائج لتقييم وتحسين أداء الكود الخاص بك.

---

## 6. ميزات متقدمة

يقدم JMH أدوات إضافية لسيناريوهات أكثر تعقيدًا:

### **المعاملات (Parameterization)**
اختبر الكود الخاص بك بمدخلات مختلفة باستخدام `@Param`:

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // Code to benchmark
        }
    }
}
```

### **الثقوب السوداء (Blackholes)**
امنع JVM من تحسين النتائج غير المستخدمة باستخدام `Blackhole`:

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // يمنع إزالة الكود الميت (dead code elimination)
}
```

---

## 7. أفضل الممارسات

- **قم بإحماء JVM**: قم دائمًا بتضمين مرحلة إحماء لضمان قيام مترجم JIT بتحسين الكود الخاص بك قبل القياس.
- **اختر الوضع المناسب**: استخدم `Mode.AverageTime` لقياس زمن الوصول (latency)، و `Mode.Throughput` لعدد العمليات في الثانية، إلخ.
- **تحكم في البيئة**: شغّل المقاييس على نظام مستقر لتجنب التداخل من العمليات الأخرى.
- **تجنب التحسينات غير المرغوب فيها**: استخدم الثقوب السوداء أو ميزات JMH الأخرى لمنع JVM من إزالة الكود.

---

باتباع هذه الخطوات، يمكنك استخدام `org.openjdk.jmh` لقياس وتحسين أداء كود جافا الخاص بك بدقة. سواء كنت تختبر عمليات بسيطة أو خوارزميات معقدة، يوفر JMH الأدوات التي تحتاجها لإجراء مقاييس موثوقة.