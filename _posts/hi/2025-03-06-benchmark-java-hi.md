---
audio: false
generated: true
lang: hi
layout: post
title: जावा में बेंचमार्किंग
translated: true
type: note
---

Java Microbenchmark Harness (JMH) Java में माइक्रोबेंचमार्क बनाने, चलाने और विश्लेषण करने के लिए एक शक्तिशाली टूल है। यह डेवलपर्स को उनके कोड के प्रदर्शन को नियंत्रित और दोहराए जाने योग्य तरीके से मापने की अनुमति देता है। नीचे JMH का प्रभावी ढंग से उपयोग करने का एक व्यापक गाइड दिया गया है।

---

## 1. अपना प्रोजेक्ट सेट अप करें

JMH का उपयोग करने के लिए, आपको इसे अपने प्रोजेक्ट में शामिल करना होगा। यहां बताया गया है कि इसे Maven या Gradle के साथ कैसे करें:

### **Maven**
अपनी `pom.xml` में निम्नलिखित डिपेंडेंसीज़ जोड़ें:

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
अपने `build.gradle` में ये लाइनें जोड़ें:

```groovy
dependencies {
    implementation 'org.openjdk.jmh:jmh-core:1.36'
    annotationProcessor 'org.openjdk.jmh:jmh-generator-annprocess:1.36'
}
```

ये डिपेंडेंसीज़ JMH कोर लाइब्रेरी और बेंचमार्क कोड जनरेट करने के लिए आवश्यक एनोटेशन प्रोसेसर प्रदान करती हैं।

---

## 2. अपना बेंचमार्क लिखें

अपना बेंचमार्क परिभाषित करने के लिए एक Java क्लास बनाएं। जिन मेथड्स को आप मापना चाहते हैं, उन्हें चिह्नित करने के लिए `@Benchmark` एनोटेशन का उपयोग करें। यहां एक सरल उदाहरण दिया गया है:

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
        // बेंचमार्क के लिए कोड
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`**: मेथड को बेंचमार्क टार्गेट के रूप में चिह्नित करता है।
- **`@BenchmarkMode`**: प्रदर्शन को कैसे मापना है, यह निर्दिष्ट करता है (जैसे, औसत निष्पादन समय के लिए `Mode.AverageTime`)।
- **`@OutputTimeUnit`**: परिणामों के लिए समय की इकाई सेट करता है (जैसे, `TimeUnit.NANOSECONDS`)।

---

## 3. बेंचमार्क कॉन्फ़िगर करें

आप अतिरिक्त JMH एनोटेशन्स का उपयोग करके अपने बेंचमार्क को कस्टमाइज़ कर सकते हैं:

- **`@Warmup`**: वार्म-अप फेज़ को परिभाषित करता है (जैसे, `@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`)।
- **`@Measurement`**: मापन फेज़ को कॉन्फ़िगर करता है (जैसे, `@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`)।
- **`@Fork`**: उपयोग करने के लिए JVM फोर्क्स की संख्या निर्दिष्ट करता है (जैसे, एक JVM इंस्टेंस में चलाने के लिए `@Fork(value = 1)`)।
- **`@State`**: स्टेट ऑब्जेक्ट्स के स्कोप को परिभाषित करता है (जैसे, थ्रेड-लोकल स्टेट के लिए `@State(Scope.Thread)`)।

कॉन्फ़िगरेशन के साथ उदाहरण:

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
        // बेंचमार्क के लिए कोड
    }
}
```

---

## 4. बेंचमार्क चलाएं

अपना बेंचमार्क निष्पादित करने के लिए, आप JMH रनर का उपयोग कर सकते हैं। यहां बताया गया है कि इसे Maven के साथ कैसे करें:

### **Maven Shade Plugin जोड़ें**
एक एक्ज़ीक्यूटेबल JAR बनाने के लिए इसे अपनी `pom.xml` में शामिल करें:

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

### **बिल्ड और रन करें**
1. JAR बनाएं: `mvn clean package`
2. बेंचमार्क चलाएं: `java -jar target/benchmarks.jar`

JMH बेंचमार्क्स निष्पादित करेगा और परिणाम आपके टर्मिनल में प्रदर्शित करेगा।

---

## 5. परिणामों का विश्लेषण करें

JMH आपके कॉन्फ़िगरेशन के आधार पर प्रदर्शन मेट्रिक्स आउटपुट करता है। उदाहरण के लिए:

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode**: बेंचमार्क मोड (जैसे, औसत समय के लिए `avgt`)।
- **Cnt**: मापन पुनरावृत्तियों की संख्या।
- **Score**: मापा गया प्रदर्शन (जैसे, प्रति ऑपरेशन औसत समय नैनोसेकंड में)।
- **Error**: त्रुटि का मार्जिन।
- **Units**: माप की इकाई।

अपने कोड के प्रदर्शन का मूल्यांकन और अनुकूलन करने के लिए इन परिणामों का उपयोग करें।

---

## 6. उन्नत सुविधाएँ

JMH अधिक जटिल परिदृश्यों के लिए अतिरिक्त टूल्स प्रदान करता है:

### **पैरामीटराइजेशन**
`@Param` का उपयोग करके अपने कोड को विभिन्न इनपुट्स के साथ टेस्ट करें:

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // बेंचमार्क के लिए कोड
        }
    }
}
```

### **ब्लैकहोल**
`Blackhole` का उपयोग करके JVM को अनुपयोगी परिणामों को ऑप्टिमाइज़ करने से रोकें:

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // डेड कोड एलिमिनेशन को रोकता है
}
```

---

## 7. सर्वोत्तम अभ्यास

- **JVM को वार्म अप करें**: मापन से पहले यह सुनिश्चित करने के लिए कि JIT कंपाइलर आपके कोड को ऑप्टिमाइज़ करता है, हमेशा एक वार्म-अप फेज़ शामिल करें।
- **सही मोड चुनें**: विलंबता के लिए `Mode.AverageTime`, प्रति सेकंड ऑपरेशन्स के लिए `Mode.Throughput`, आदि का उपयोग करें।
- **वातावरण को नियंत्रित करें**: अन्य प्रक्रियाओं के हस्तक्षेप से बचने के लिए बेंचमार्क्स को एक स्थिर सिस्टम पर चलाएं।
- **ऑप्टिमाइज़ेशन से बचें**: JVM को कोड को एलिमिनेट करने से रोकने के लिए ब्लैकहोल या अन्य JMH सुविधाओं का उपयोग करें।

---

इन चरणों का पालन करके, आप अपने Java कोड के प्रदर्शन को सटीक रूप से मापने और सुधारने के लिए `org.openjdk.jmh` का उपयोग कर सकते हैं। चाहे आप सरल ऑपरेशन्स टेस्ट कर रहे हों या जटिल एल्गोरिदम, JMH विश्वसनीय बेंचमार्किंग के लिए आपको आवश्यक टूल्स प्रदान करता है।