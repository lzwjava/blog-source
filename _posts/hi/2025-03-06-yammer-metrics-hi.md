---
audio: false
generated: true
lang: hi
layout: post
title: जावा में एप्लिकेशन मेट्रिक्स
translated: true
type: note
---

`com.yammer.metrics` लाइब्रेरी, जिसे मूल रूप से Yammer द्वारा विकसित किया गया था, अब **Dropwizard Metrics** लाइब्रेरी का हिस्सा है। यह Java में एप्लिकेशन मेट्रिक्स को इकट्ठा करने और रिपोर्ट करने का एक मजबूत तरीका प्रदान करती है, जो आपको रिक्वेस्ट काउंट, रिस्पॉन्स टाइम और अन्य जैसे पर्फॉर्मेंस पहलुओं की निगरानी करने में मदद करती है। नीचे इसे प्रभावी ढंग से उपयोग करने का एक मार्गदर्शक दिया गया है।

---

### चरण 1: डिपेंडेंसी जोड़ें
चूंकि `com.yammer.metrics` का विकास Dropwizard Metrics में हो गया है, इसलिए आपको Dropwizard Metrics लाइब्रेरी का उपयोग करना चाहिए। यदि आप Maven का उपयोग कर रहे हैं, तो अपनी `pom.xml` में निम्नलिखित डिपेंडेंसी जोड़ें:

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- उपलब्ध नवीनतम संस्करण का उपयोग करें -->
</dependency>
```

आपकी आवश्यकताओं के आधार पर, आप अतिरिक्त मॉड्यूल भी चाह सकते हैं, जैसे कि:
- JVM-संबंधित मेट्रिक्स के लिए `metrics-jvm`।
- HTTP क्लाइंट मेट्रिक्स के लिए `metrics-httpclient`।
- Jersey वेब फ्रेमवर्क के साथ एकीकरण के लिए `metrics-jersey`।

नवीनतम संस्करण और उपलब्ध मॉड्यूल के लिए [Dropwizard Metrics डॉक्यूमेंटेशन](https://metrics.dropwizard.io/) देखें।

---

### चरण 2: एक मेट्रिक रजिस्ट्री बनाएँ
`MetricRegistry` वह केंद्रीय स्थान है जहाँ सभी मेट्रिक्स संग्रहीत होते हैं। आप आमतौर पर अपने एप्लिकेशन के लिए एक इंस्टेंस बनाते हैं:

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
Dropwizard Metrics कई प्रकार के मेट्रिक्स का समर्थन करता है, जिनमें से प्रत्येक अलग-अलग निगरानी आवश्यकताओं के अनुरूप है:

#### **काउंटर**
काउंटर का उपयोग उन मूल्यों को ट्रैक करने के लिए किया जाता है जो बढ़ या घट सकते हैं (जैसे, संसाधित रिक्वेस्ट्स की संख्या)।

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // 1 से बढ़ाएँ
counter.inc(5); // 5 से बढ़ाएँ
counter.dec();  // 1 से घटाएँ
```

#### **गेज**
गेज किसी विशिष्ट क्षण पर किसी मान की एक स्नैपशॉट प्रदान करते हैं (जैसे, वर्तमान कतार का आकार)। आप `Gauge` इंटरफेस को इम्प्लीमेंट करके एक गेज को परिभाषित करते हैं:

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
हिस्टोग्राम मूल्यों के सांख्यिकीय वितरण को ट्रैक करते हैं (जैसे, रिक्वेस्ट आकार):

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // एक मान रिकॉर्ड करें
```

#### **मीटर**
मीटर घटनाओं की दर मापते हैं (जैसे, प्रति सेकंड रिक्वेस्ट):

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // एक घटना रिकॉर्ड करें
```

#### **टाइमर**
टाइमर घटनाओं की दर और अवधि दोनों को मापते हैं (जैसे, रिक्वेस्ट प्रोसेसिंग समय):

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // कुछ कार्य का अनुकरण करें
    Thread.sleep(100);
} finally {
    context.stop(); // अवधि रिकॉर्ड करें
}
```

---

### चरण 4: मेट्रिक्स रिपोर्ट करें
मेट्रिक्स को उपयोगी बनाने के लिए, आपको उन्हें कहीं रिपोर्ट करने की आवश्यकता है। Dropwizard Metrics विभिन्न रिपोर्टरों का समर्थन करता है, जैसे कि कंसोल, JMX, या Graphite। यहाँ एक कंसोल रिपोर्टर का उदाहरण दिया गया है जो हर 10 सेकंड में मेट्रिक्स लॉग करता है:

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // हर 10 सेकंड में रिपोर्ट करें
```

प्रोडक्शन उपयोग के लिए, Graphite जैसी सिस्टम के साथ एकीकरण करने या JMX के माध्यम से मेट्रिक्स एक्सपोज़ करने पर विचार करें।

---

### चरण 5: फ्रेमवर्क के साथ एकीकृत करें (वैकल्पिक)
यदि आप Jersey जैसे वेब फ्रेमवर्क का उपयोग कर रहे हैं, तो आप अपने एंडपॉइंट्स को स्वचालित रूप से इंस्ट्रूमेंट करने के लिए `metrics-jersey` मॉड्यूल का उपयोग कर सकते हैं। इसके अतिरिक्त, `@Timed` या `@Counted` जैसे एनोटेशन मेट्रिक संग्रह को सरल बना सकते हैं:

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

इस सुविधा को सक्षम करने के लिए `metrics-jersey` डिपेंडेंसी जोड़ें और इसे अपने Jersey एप्लिकेशन के साथ कॉन्फ़िगर करें।

---

### सर्वोत्तम अभ्यास
- **नामकरण सम्मेलन**: स्पष्टता के लिए एक पदानुक्रमित नामकरण योजना का उपयोग करें (जैसे, `com.example.myapp.requests.total`)।
- **प्रदर्शन**: मेट्रिक्स की संख्या और आवृत्ति के साथ सावधान रहें, क्योंकि अत्यधिक संग्रह प्रदर्शन को प्रभावित कर सकता है।
- **दस्तावेज़ीकरण**: नवीनतम उदाहरणों और उन्नत सुविधाओं के लिए [Dropwizard Metrics दस्तावेज़ीकरण](https://metrics.dropwizard.io/) देखें।

---

### उदाहरण: सभी को एक साथ रखना
यहाँ कई अवधारणाओं को संयोजित करने वाला एक सरल उदाहरण दिया गया है:

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // एक काउंटर बनाएँ
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // एक टाइमर बनाएँ
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // कार्य का अनुकरण करें
        context.stop();

        // एक कंसोल रिपोर्टर शुरू करें
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // रिपोर्ट देखने के लिए प्रोग्राम को चलते रहने दें
        Thread.sleep(5000);
    }
}
```

यह कोड एक काउंटर और एक टाइमर को ट्रैक करता है, और परिणामों को हर सेकंड कंसोल पर रिपोर्ट करता है।

---

### अंतिम नोट्स
`com.yammer.metrics` लाइब्रेरी का विकास Dropwizard Metrics में हो गया है, इसलिए हमेशा `io.dropwizard.metrics` ग्रुप से नवीनतम संस्करण का उपयोग करें। यदि आप एक नई परियोजना शुरू कर रहे हैं, तो आप Micrometer जैसे आधुनिक विकल्पों का भी पता लगा सकते हैं, लेकिन Dropwizard Metrics कई Java एप्लिकेशन्स के लिए एक ठोस विकल्प बनी हुई है। अधिक जानकारी के लिए, आधिकारिक दस्तावेज़ीकरण देखें!