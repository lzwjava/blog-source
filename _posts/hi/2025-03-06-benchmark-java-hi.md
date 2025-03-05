---
audio: false
generated: true
lang: hi
layout: post
title: Java में बेंचमार्किंग
translated: true
---

Java Microbenchmark Harness (JMH) एक शक्तिशाली औजार है जो Java में माइक्रोबेंचमार्क्स को बनाना, चलाना और विश्लेषित करना संभव बनाता है। यह डेवलपर्स को अपने कोड की प्रदर्शन को एक नियंत्रित और दोहराने योग्य तरीके से मापने की अनुमति देता है। नीचे JMH का उपयोग करने के लिए एक व्यापक मार्गदर्शन दिया गया है।

---

## 1. आपका प्रोजेक्ट सेट अप करें

JMH का उपयोग करने के लिए, आपको इसे अपने प्रोजेक्ट में शामिल करना होगा। यहां इसे Maven या Gradle के साथ कैसे करना है:

### **Maven**
निम्नलिखित निर्भरताओं को अपने `pom.xml` में जोड़ें:

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
निम्नलिखित पंक्तियाँ अपने `build.gradle` में जोड़ें:

```groovy
dependencies {
    implementation 'org.openjdk.jmh:jmh-core:1.36'
    annotationProcessor 'org.openjdk.jmh:jmh-generator-annprocess:1.36'
}
```

ये निर्भरताएं JMH कोर लाइब्रेरी और बेंचमार्क कोड को जनरेट करने के लिए आवश्यक एनोटेशन प्रोसेसर प्रदान करते हैं।

---

## 2. आपका बेंचमार्क लिखें

एक Java क्लास बनाएं ताकि आपका बेंचमार्क परिभाषित हो सके। `@Benchmark` एनोटेशन का उपयोग करके, आप मापने के लिए चाहे हुए विधियों को चिह्नित करें। यहां एक सरल उदाहरण है:

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
        // बेंचमार्क करने के लिए कोड
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`**: विधि को बेंचमार्क लक्ष्य के रूप में चिह्नित करता है।
- **`@BenchmarkMode`**: प्रदर्शन को कैसे मापना है (उदाहरण के लिए, `Mode.AverageTime` औसत कार्यनिरत समय के लिए).
- **`@OutputTimeUnit`**: परिणामों के लिए समय इकाई सेट करता है (उदाहरण के लिए, `TimeUnit.NANOSECONDS`).

---

## 3. बेंचमार्क को कॉन्फ़िगर करें

आपका बेंचमार्क को अतिरिक्त JMH एनोटेशन का उपयोग करके अनुकूलित कर सकते हैं:

- **`@Warmup`**: गर्मीकरण चरण को परिभाषित करता है (उदाहरण के लिए, `@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Measurement`**: मापन चरण को कॉन्फ़िगर करता है (उदाहरण के लिए, `@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Fork`**: कितने JVM फॉर्क्स का उपयोग करना है, यह निर्धारित करता है (उदाहरण के लिए, `@Fork(value = 1)` एक JVM इंस्टेंस में चलाने के लिए).
- **`@State`**: स्टेट ऑब्जेक्ट्स की स्कोप को परिभाषित करता है (उदाहरण के लिए, `@State(Scope.Thread)` थ्रेड-लोकल स्टेट के लिए).

कोन्फ़िगरेशन के साथ उदाहरण:

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
        // बेंचमार्क करने के लिए कोड
    }
}
```

---

## 4. बेंचमार्क चलाएं

अपना बेंचमार्क चलाने के लिए, आप JMH रनर का उपयोग कर सकते हैं। यहां इसे Maven के साथ कैसे करना है:

### **Maven Shade प्लगइन जोड़ें**
इसे अपने `pom.xml` में शामिल करें ताकि एक एक्सीक्यूटेबल JAR बनाया जा सके:

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

### **बिल्ड और चलाएं**
1. JAR बनाएं: `mvn clean package`
2. बेंचमार्क चलाएं: `java -jar target/benchmarks.jar`

JMH बेंचमार्क्स को चलाएगा और परिणामों को आपकी टर्मिनल पर प्रदर्शित करेगा।

---

## 5. परिणामों का विश्लेषण करें

JMH आपके कॉन्फ़िगरेशन के आधार पर प्रदर्शन मेट्रिक्स का आउटपुट देता है। उदाहरण के लिए:

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode**: बेंचमार्क मोड (उदाहरण के लिए, `avgt` औसत समय के लिए).
- **Cnt**: मापन इटरेशन की संख्या.
- **Score**: मापा गया प्रदर्शन (उदाहरण के लिए, औसत समय नैनोसेकंड प्रति ऑपरेशन में).
- **Error**: त्रुटि का मार्जिन.
- **Units**: मापन इकाई.

इन परिणामों का उपयोग करके, आप अपने कोड की प्रदर्शन की मूल्यांकन और अनुकूलन कर सकते हैं।

---

## 6. उन्नत विशेषताएं

JMH अधिक जटिल परिस्थितियों के लिए अतिरिक्त औजार प्रदान करता है:

### **परामिटराइजेशन**
अपने कोड को विभिन्न इनपुट्स के साथ टेस्ट करने के लिए `@Param` का उपयोग करें:

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // बेंचमार्क करने के लिए कोड
        }
    }
}
```

### **ब्लैकहोल्स**
JVM को अनुपयोगी परिणामों को ऑप्टिमाइज़ करने से रोकने के लिए `Blackhole` का उपयोग करें:

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // मृत कोड हटाने को रोकता है
}
```

---

## 7. सर्वश्रेष्ठ अभ्यास

- **JVM को गर्म करें**: हमेशा गर्मीकरण चरण शामिल करें ताकि JIT कॉम्पाइलर आपका कोड मापने से पहले ऑप्टिमाइज़ कर सके।
- **सही मोड चुनें**: `Mode.AverageTime` लैटेंसी के लिए, `Mode.Throughput` सेकंड प्रति ऑपरेशन के लिए, आदि का उपयोग करें।
- **पर्यावरण को नियंत्रित करें**: बेंचमार्क्स को एक स्थिर प्रणाली पर चलाएं ताकि अन्य प्रक्रियाओं से हस्तक्षेप से बचा जा सके।
- **ऑप्टिमाइज़ेशन से बचें**: ब्लैकहोल्स या अन्य JMH विशेषताओं का उपयोग करके JVM को कोड को हटाने से रोकें।

---

इन चरणों का पालन करके, आप `org.openjdk.jmh` का उपयोग करके अपने Java कोड की प्रदर्शन को सही और विश्वसनीय तरीके से माप और सुधार सकते हैं। चाहे आप सरल ऑपरेशन या जटिल एल्गोरिथम टेस्ट कर रहे हों, JMH आपको विश्वसनीय बेंचमार्किंग के लिए आवश्यक औजार प्रदान करता है।