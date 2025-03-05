---
audio: false
generated: true
lang: hi
layout: post
title: Java में Application Metrics
translated: true
---

`com.yammer.metrics` लाइब्रेरी, जो मूल रूप से Yammer द्वारा विकसित की गई थी, अब **Dropwizard Metrics** लाइब्रेरी का हिस्सा है। यह Java में एप्लिकेशन मेट्रिक्स को इकट्ठा करने और रिपोर्ट करने का एक मजबूत तरीका प्रदान करता है, जिससे आप प्रदर्शन पहलुओं जैसे कि रिक्वेस्ट काउंट, रिस्पॉन्स टाइम, और अधिक को मॉनिटर कर सकते हैं। नीचे इसका उपयोग करने का एक गाइड दिया गया है।

---

### चरण 1: डिपेंडेंसी जोड़ें
`com.yammer.metrics` Dropwizard Metrics में विकसित हो गई है, इसलिए आपको Dropwizard Metrics लाइब्रेरी का उपयोग करना चाहिए। अगर आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` में निम्नलिखित डिपेंडेंसी जोड़ें:

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- उपलब्ध सबसे नया संस्करण का उपयोग करें -->
</dependency>
```

अपने आवश्यकताओं के अनुसार, आपको अतिरिक्त मॉड्यूलों की भी आवश्यकता हो सकती है, जैसे:
- `metrics-jvm` JVM संबंधी मेट्रिक्स के लिए।
- `metrics-httpclient` HTTP क्लाइंट मेट्रिक्स के लिए।
- `metrics-jersey` Jersey वेब फ्रेमवर्क के साथ एकीकरण के लिए।

[Dropwizard Metrics दस्तावेज़](https://metrics.dropwizard.io/) के लिए सबसे नया संस्करण और उपलब्ध मॉड्यूल्स की जांच करें।

---

### चरण 2: मेट्रिक्स रजिस्ट्री बनाएं
`MetricRegistry` वह स्थान है जहां सभी मेट्रिक्स संग्रहीत होते हैं। आप आमतौर पर अपने एप्लिकेशन के लिए एक इंस्टेंस बनाते हैं:

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### चरण 3: विभिन्न प्रकार के मेट्रिक्स का उपयोग करें
Dropwizard Metrics विभिन्न प्रकार के मेट्रिक्स का समर्थन करता है, प्रत्येक अलग-अलग मॉनिटरिंग आवश्यकताओं के लिए उपयुक्त है:

#### **काउंटर्स**
काउंटर्स उन मानों को ट्रैक करने के लिए उपयोग किए जाते हैं जो बढ़ सकते हैं या घट सकते हैं (उदाहरण के लिए, प्रोसेस किए गए रिक्वेस्ट की संख्या):

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // 1 से बढ़ाएं
counter.inc(5); // 5 से बढ़ाएं
counter.dec();  // 1 से घटाएं
```

#### **गेज**
गेज एक विशेष क्षण में एक मान की एक स्नैपशॉट प्रदान करते हैं (उदाहरण के लिए, वर्तमान क्यू साइज)। आप एक गेज को `Gauge` इंटरफेस को लागू करके परिभाषित करते हैं:

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // अपने लॉजिक से बदलें
    }
});
```

#### **हिस्टोग्राम**
हिस्टोग्राम मानों की सांख्यिकीय वितरण को ट्रैक करते हैं (उदाहरण के लिए, रिक्वेस्ट साइज):

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // एक मान रिकॉर्ड करें
```

#### **मीटर**
मीटर घटनाओं की दर को मापते हैं (उदाहरण के लिए, प्रति सेकंड रिक्वेस्ट):

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // एक घटना रिकॉर्ड करें
```

#### **टाइमर्स**
टाइमर्स घटनाओं की दर और अवधि दोनों को मापते हैं (उदाहरण के लिए, रिक्वेस्ट प्रोसेसिंग समय):

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // कुछ काम सिमुलेट करें
    Thread.sleep(100);
} finally {
    context.stop(); // अवधि रिकॉर्ड करें
}
```

---

### चरण 4: मेट्रिक्स रिपोर्ट करें
मेट्रिक्स को उपयोगी बनाने के लिए, आपको उन्हें कहीं रिपोर्ट करना होगा। Dropwizard Metrics विभिन्न रिपोर्टरों का समर्थन करता है, जैसे कि कंसोल, JMX, या ग्राफाइट। यहां एक कंसोल रिपोर्टर का उदाहरण है जो हर 10 सेकंड में मेट्रिक्स लॉग करता है:

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // हर 10 सेकंड में रिपोर्ट करें
```

उत्पादन उपयोग के लिए, ग्राफाइट के साथ एकीकरण करने या JMX के माध्यम से मेट्रिक्स को प्रदर्शित करने की सोचें।

---

### चरण 5: फ्रेमवर्क के साथ एकीकरण (वैकल्पिक)
अगर आप Jersey जैसे वेब फ्रेमवर्क का उपयोग कर रहे हैं, तो आप `metrics-jersey` मॉड्यूल का उपयोग कर सकते हैं अपने एंडपॉइंट्स को स्वचालित रूप से इंस्ट्रुमेंट करने के लिए। अतिरिक्त रूप से, एनोटेशन जैसे `@Timed` या `@Counted` मेट्रिक्स संग्रहण को सरल बना सकते हैं:

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

`metrics-jersey` डिपेंडेंसी जोड़ें और इसे अपने Jersey एप्लिकेशन के साथ सेटअप करें इस सुविधा को सक्षम करने के लिए।

---

### बेस्ट प्रैक्टिस
- **नामकरण संवेदनशीलता**: स्पष्टता के लिए एक हाइरार्किकल नामकरण योजना का उपयोग करें (उदाहरण के लिए, `com.example.myapp.requests.total`).
- **प्रदर्शन**: मेट्रिक्स की संख्या और आवृत्ति के साथ सावधान रहें, क्योंकि अत्यधिक संग्रहण प्रदर्शन पर प्रभाव डाल सकता है।
- **दस्तावेज़**: [Dropwizard Metrics दस्तावेज़](https://metrics.dropwizard.io/) के लिए सबसे नए उदाहरणों और उन्नत विशेषताओं के लिए संदर्भ करें।

---

### उदाहरण: सब कुछ एक साथ
यहाँ कई अवधारणाओं को संयोजित करने का एक सरल उदाहरण है:

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // एक काउंटर बनाएं
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // एक टाइमर बनाएं
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // काम सिमुलेट करें
        context.stop();

        // एक कंसोल रिपोर्टर शुरू करें
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // रिपोर्ट देखने के लिए प्रोग्राम चलने दें
        Thread.sleep(5000);
    }
}
```

यह कोड एक काउंटर और एक टाइमर को ट्रैक करता है, और हर सेकंड में कंसोल पर परिणाम रिपोर्ट करता है।

---

### अंतिम टिप्पणियाँ
`com.yammer.metrics` लाइब्रेरी Dropwizard Metrics में विकसित हो गई है, इसलिए हमेशा `io.dropwizard.metrics` ग्रुप से सबसे नया संस्करण का उपयोग करें। अगर आप एक नया प्रोजेक्ट शुरू कर रहे हैं, तो आप आधुनिक विकल्पों जैसे Micrometer का भी पता लगाने की सोच सकते हैं, लेकिन Dropwizard Metrics कई Java एप्लिकेशनों के लिए एक मजबूत विकल्प बना रहता है। अधिक विवरण के लिए, आधिकारिक दस्तावेज़ देखें!