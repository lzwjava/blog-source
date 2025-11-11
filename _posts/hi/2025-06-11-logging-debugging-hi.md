---
audio: false
generated: true
lang: hi
layout: post
title: जावा डिबगिंग और लॉगिंग तकनीकें
translated: true
type: note
---

Java में हर एक स्टेटमेंट के एक्सेक्यूट होने पर हर वेरिएबल और स्टेट को ऑटोमैटिक लॉग करने के लिए कोई बिल्ट-इन फ्लैग नहीं है, क्योंकि इससे बहुत अधिक मात्रा में आउटपुट जनरेट होगा और परफॉर्मेंस पर काफी प्रभाव पड़ेगा। हालाँकि, आप विभिन्न टूल्स, तकनीकों और कॉन्फ़िगरेशन का उपयोग करके वेरिएबल्स और प्रोग्राम स्टेट की डिटेल्ड डीबगिंग और लॉगिंग प्राप्त कर सकते हैं। नीचे, मैं Java में इसे पूरा करने के सबसे करीबी तरीकों की रूपरेखा दूंगा, जिसमें डीबगिंग फ्लैग्स, टूल्स और कस्टम सॉल्यूशन शामिल हैं।

---

### 1. **डीबगर के साथ JVM डीबगिंग फ्लैग्स का उपयोग**
Java वर्चुअल मशीन (JVM) Java डीबग वायर प्रोटोकॉल (JDWP) के माध्यम से डीबगिंग को सपोर्ट करती है। आप विशिष्ट JVM फ्लैग्स पास करके डीबगिंग को एनेबल कर सकते हैं, जो आपको वेरिएबल्स, स्टैक ट्रेस और प्रोग्राम स्टेट को स्टेप-बाय-स्टेप मॉनिटर करने के लिए एक डीबगर (जैसे IntelliJ IDEA, Eclipse, या Visual Studio Code) अटैच करने की अनुमति देते हैं।

#### JVM डीबगिंग कैसे एनेबल करें
अपने Java एप्लिकेशन को निम्नलिखित JVM ऑप्शन्स के साथ शुरू करें:
```bash
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 MyApp
```

- **मुख्य फ्लैग्स**:
  - `-agentlib:jdwp`: डीबगिंग के लिए JDWP एजेंट को एनेबल करता है।
  - `transport=dt_socket`: डीबगर कम्युनिकेशन के लिए सॉकेट ट्रांसपोर्ट का उपयोग करता है।
  - `server=y`: JVM एक सर्वर के रूप में कार्य करता है, एक डीबगर के कनेक्ट होने की प्रतीक्षा करता है।
  - `suspend=y`: डीबगर के अटैच होने तक JVM को पॉज़ कर देता है (बिना प्रतीक्षा किए रन करने के लिए `suspend=n` का उपयोग करें)।
  - `address=*:5005`: डीबगर कनेक्शन के लिए पोर्ट (उदाहरण के लिए, 5005) निर्दिष्ट करता है।

#### डीबगर के साथ उपयोग
1. **डीबगर अटैच करें**: IntelliJ IDEA, Eclipse, या Visual Studio Code जैसे IDE का उपयोग करके निर्दिष्ट पोर्ट (उदाहरण के लिए, 5005) पर JVM से कनेक्ट करें।
2. **ब्रेकपॉइंट्स सेट करें**: अपने कोड में उन स्थानों पर ब्रेकपॉइंट्स रखें जहाँ आप वेरिएबल्स और स्टेट का निरीक्षण करना चाहते हैं।
3. **कोड के माध्यम से स्टेप करें**: डीबगर आपको प्रत्येक स्टेटमेंट के माध्यम से स्टेप करने, वेरिएबल वैल्यूज़ का निरीक्षण करने, एक्सप्रेशन्स का मूल्यांकन करने और रियल-टाइम में कॉल स्टैक देखने की अनुमति देते हैं।

#### आपको क्या मिलता है
- प्रत्येक ब्रेकपॉइंट पर वेरिएबल्स का निरीक्षण करें।
- प्रोग्राम स्टेट (जैसे लोकल वेरिएबल्स, इंस्टेंस फ़ील्ड्स, स्टैक फ़्रेम) की निगरानी करें।
- एक्सेक्यूशन को ट्रेस करने के लिए मेथड कॉल्स में स्टेप इन, ओवर, या आउट करें।

#### सीमाएँ
- ब्रेकपॉइंट्स और स्टेपिंग के मैनुअल सेटअप की आवश्यकता होती है।
- जब तक आप वॉचेस या लॉग पॉइंट्स को एक्सप्लिसिटली कॉन्फ़िगर नहीं करते, तब तक हर स्टेटमेंट के लिए हर वेरिएबल की ऑटोमैटिक लॉगिंग नहीं होती।

---

### 2. **फ्रेमवर्क्स के साथ लॉगिंग (जैसे, SLF4J, Log4j, या Java Logging)**
वेरिएबल वैल्यूज़ और प्रोग्राम स्टेट को लॉग करने के लिए, आप SLF4J के साथ Logback, Log4j, या Java के बिल्ट-इन `java.util.logging` जैसे लॉगिंग फ्रेमवर्क का उपयोग कर सकते हैं। हालाँकि, वेरिएबल वैल्यूज़ और स्टेट को कैप्चर करने के लिए इन्हें अपने कोड में मैन्युअली लॉग स्टेटमेंट्स जोड़ने की आवश्यकता होती है।

#### SLF4J और Logback के साथ उदाहरण
1. **डिपेंडेंसीज जोड़ें** (उदाहरण के लिए, Maven के लिए):

```xml
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.4.11</version>
</dependency>
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
    <version>2.0.9</version>
</dependency>
```

2. **Logback कॉन्फ़िगर करें** (`logback.xml`):

```xml
<configuration>
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    <root level="DEBUG">
        <appender-ref ref="CONSOLE" />
    </root>
</configuration>
```

3. **कोड में लॉगिंग जोड़ें**:

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MyApp {
    private static final Logger logger = LoggerFactory.getLogger(MyApp.class);

    public static void main(String[] args) {
        int x = 10;
        String message = "Hello";
        logger.debug("Variable x: {}, message: {}", x, message);
        x++;
        logger.debug("After increment, x: {}", x);
    }
}
```

#### आउटपुट
```
2025-06-06 20:50:00 DEBUG MyApp - Variable x: 10, message: Hello
2025-06-06 20:50:00 DEBUG MyApp - After increment, x: 11
```

#### नोट्स
- **फायदे**: आप वांछित बिंदुओं पर विशिष्ट वेरिएबल्स और स्टेट्स को कस्टमाइज़ेबल फॉर्मेट के साथ लॉग कर सकते हैं।
- **नुकसान**: हर उस वेरिएबल या स्टेट को ट्रैक करने के लिए जिसे आप चाहते हैं, उसके लिए लॉग स्टेटमेंट्स के मैनुअल जोड़ की आवश्यकता होती है। कोड इंस्ट्रुमेंटेशन के बिना हर वेरिएबल को ऑटोमैटिक लॉग करना अव्यावहारिक है।

---

### 3. **टूल्स के साथ बाइटकोड इंस्ट्रुमेंटेशन (जैसे, Java Agents, Byte Buddy, या AspectJ)**
सोर्स कोड को मॉडिफ़ाई किए बिना हर वेरिएबल और स्टेट को ऑटोमैटिकली लॉग करने के लिए, आप रनटाइम या कंपाइल टाइम पर लॉगिंग लॉजिक इंजेक्ट करने के लिए बाइटकोड इंस्ट्रुमेंटेशन का उपयोग कर सकते हैं। यह तरीका हर स्टेटमेंट की ऑटोमैटिक लॉगिंग के आपके अनुरोध के सबसे करीब है।

#### विकल्प 1: Byte Buddy के साथ Java एजेंट
Byte Buddy एक लाइब्रेरी है जो आपको मेथड कॉल्स को इंटरसेप्ट करने और वेरिएबल स्टेट्स को डायनामिकली लॉग करने के लिए एक Java एजेंट बनाने की अनुमति देती है।

1. **Byte Buddy डिपेंडेंसी जोड़ें** (Maven):

```xml
<dependency>
    <groupId>net.bytebuddy</groupId>
    <artifactId>byte-buddy</artifactId>
    <version>1.14.9</version>
</dependency>
<dependency>
    <groupId>net.bytebuddy</groupId>
    <artifactId>byte-buddy-agent</artifactId>
    <version>1.14.9</version>
</dependency>
```

2. **एक Java एजेंट बनाएँ**:

```java
import net.bytebuddy.agent.builder.AgentBuilder;
import net.bytebuddy.description.type.TypeDescription;
import net.bytebuddy.dynamic.DynamicType;
import net.bytebuddy.implementation.MethodDelegation;
import net.bytebuddy.matcher.ElementMatchers;
import java.lang.instrument.Instrumentation;

public class LoggingAgent {
    public static void premain(String args, Instrumentation inst) {
        new AgentBuilder.Default()
            .type(ElementMatchers.any())
            .transform((builder, type, classLoader, module) -> 
                builder.method(ElementMatchers.any())
                       .intercept(MethodDelegation.to(LoggingInterceptor.class)))
            .installOn(inst);
    }
}
```

3. **एक इंटरसेप्टर बनाएँ**:

```java
import net.bytebuddy.implementation.bind.annotation.AllArguments;
import net.bytebuddy.implementation.bind.annotation.Origin;
import net.bytebuddy.implementation.bind.annotation.RuntimeType;

import java.lang.reflect.Method;
import java.util.Arrays;

public class LoggingInterceptor {
    @RuntimeType
    public static Object intercept(@Origin Method method, @AllArguments Object[] args) throws Exception {
        System.out.println("Executing: " + method.getName() + " with args: " + Arrays.toString(args));
        // मूल मेथड कॉल के साथ आगे बढ़ें
        return method.invoke(null, args);
    }
}
```

4. **एजेंट के साथ रन करें**:
```bash
java -javaagent:logging-agent.jar -cp . MyApp
```

#### नोट्स
- **फायदे**: मेथड कॉल्स, पैरामीटर्स और संभावित रूप से स्टैक या बाइटकोड का निरीक्षण करके वेरिएबल स्टेट्स को ऑटोमैटिकली लॉग कर सकता है।
- **नुकसान**: हर स्टेटमेंट के लिए हर वेरिएबल को लॉग करने के लिए कॉम्प्लेक्स बाइटकोड एनालिसिस की आवश्यकता होती है, जो धीमी और व्यापक रूप से लागू करने में मुश्किल हो सकती है। लोकल वेरिएबल्स को कैप्चर करने के लिए आपको एजेंट को और कस्टमाइज़ करने की आवश्यकता हो सकती है।

#### विकल्प 2: एस्पेक्ट-ओरिएंटेड प्रोग्रामिंग के लिए AspectJ
AspectJ आपको ऐसे एस्पेक्ट्स को परिभाषित करने की अनुमति देता है जो कोड एक्सेक्यूशन को इंटरसेप्ट करते हैं और वेरिएबल स्टेट्स को लॉग करते हैं।

1. **AspectJ डिपेंडेंसी जोड़ें** (Maven):

```xml
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjrt</artifactId>
    <version>1.9.22</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.22</version>
</dependency>
```

2. **एक एस्पेक्ट परिभाषित करें**:

```java
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;

@Aspect
public class LoggingAspect {
    @After("execution(* *(..))")
    public void logAfter(JoinPoint joinPoint) {
        System.out.println("Method executed: " + joinPoint.getSignature());
        System.out.println("Arguments: " + Arrays.toString(joinPoint.getArgs()));
    }
}
```

3. **AspectJ के साथ रन करें**:
एजेंट जोड़कर AspectJ वीवर का उपयोग करें:
```bash
java -javaagent:aspectjweaver.jar -cp . MyApp
```

#### नोट्स
- **फायदे**: मेथड एक्सेक्यूशन और आर्ग्युमेंट्स को ऑटोमैटिकली लॉग कर सकता है।
- **नुकसान**: हर लोकल वेरिएबल और स्टेट को कैप्चर करने के लिए एडवांस्ड पॉइंटकट्स की आवश्यकता होती है और सोर्स कोड मॉडिफ़िकेशन या रनटाइम वीविंग की आवश्यकता हो सकती है।

---

### 4. **IDE-स्पेसिफिक डीबगिंग फीचर्स का उपयोग**
आधुनिक IDE जैसे IntelliJ IDEA, Eclipse, या Visual Studio Code एडवांस्ड डीबगिंग फीचर्स प्रदान करते हैं जो आपके वांछित व्यवहार का अनुकरण कर सकते हैं:

- **लॉग पॉइंट्स**: IntelliJ IDEA और Eclipse आपको "लॉग पॉइंट्स" (या "ट्रेसपॉइंट्स") सेट करने की अनुमति देते हैं जो एक्सेक्यूशन को पॉज़ किए बिना वेरिएबल वैल्यूज़ प्रिंट करते हैं।
- **वेरिएबल वॉचेस**: आप विशिष्ट वेरिएबल्स को वॉच कर सकते हैं और प्रत्येक स्टेप पर उनके मान लॉग कर सकते हैं।
- **कंडीशनल ब्रेकपॉइंट्स**: ऐसे ब्रेकपॉइंट्स सेट करें जो कुछ शर्तों के पूरा होने पर वेरिएबल्स को लॉग करते हैं।

#### IntelliJ IDEA में उदाहरण
1. एक ब्रेकपॉइंट सेट करें।
2. ब्रेकपॉइंट पर राइट-क्लिक करें, "More" या "Edit Breakpoint" चुनें।
3. वेरिएबल वैल्यूज़ या एक्सप्रेशन्स (जैसे, `System.out.println("x = " + x)`) प्रिंट करने के लिए "Evaluate and Log" को एनेबल करें।
4. प्रत्येक स्टेटमेंट पर स्टेट लॉग करने के लिए कोड के माध्यम से स्टेप करें।

#### नोट्स
- **फायदे**: गैर-आक्रामक और विशिष्ट वेरिएबल्स या मेथड्स के लिए सेट अप करने में आसान।
- **नुकसान**: पूरी तरह से ऑटोमैटिक नहीं; आपको यह निर्दिष्ट करने की आवश्यकता है कि क्या लॉग करना है।

---

### 5. **कस्टम कोड इंस्ट्रुमेंटेशन**
पूर्ण नियंत्रण के लिए, आप हर वेरिएबल और स्टेटमेंट के लिए लॉगिंग स्टेटमेंट्स डालने के लिए अपने Java सोर्स कोड या बाइटकोड को पार्स और मॉडिफ़ाई करने के लिए एक टूल लिख सकते हैं। **ASM** या **Javassist** जैसे टूल बाइटकोड मैनिपुलेशन में मदद कर सकते हैं, लेकिन यह जटिल है और आमतौर पर एडवांस्ड यूज़ केस के लिए उपयोग किया जाता है।

#### उदाहरण वर्कफ़्लो
1. ASM जैसी लाइब्रेरी का उपयोग करके Java सोर्स कोड या बाइटकोड को पार्स करें।
2. सभी लोकल वेरिएबल्स और स्टेटमेंट्स की पहचान करें।
3. प्रत्येक स्टेटमेंट से पहले या बाद में लॉगिंग कॉल्स (जैसे, `System.out.println("Variable x = " + x)`) डालें।
4. मॉडिफ़ाइड कोड को कंपाइल और रन करें।

यह तरीका जटिलता और परफॉर्मेंस ओवरहेड के कारण बड़ी प्रोजेक्ट्स के लिए शायद ही कभी व्यावहारिक होता है।

---

### 6. **ट्रेसिंग और प्रोफाइलिंग के लिए मौजूदा टूल्स**
कई टूल बिना आपके कोड को मॉडिफ़ाई किए प्रोग्राम एक्सेक्यूशन को ट्रेस और लॉग करने में मदद कर सकते हैं:

- **Java Flight Recorder (JFR)**:
  - JVM फ्लैग्स के साथ JFR को एनेबल करें:
    ```bash
    java -XX:StartFlightRecording=settings=profile,dumponexit=true,filename=recording.jfr MyApp
    ```
  - मेथड कॉल्स, स्टैक ट्रेस और इवेंट्स को देखने के लिए JDK मिशन कंट्रोल का उपयोग करके रिकॉर्डिंग्स का विश्लेषण करें।
  - **सीमाएँ**: हर वेरिएबल को लॉग नहीं करता है लेकिन डिटेल्ड एक्सेक्यूशन ट्रेस प्रदान करता है।

- **VisualVM**:
  - एक प्रोफाइलिंग टूल जो मेथड कॉल्स, मेमोरी यूसेज और CPU एक्टिविटी की निगरानी कर सकता है।
  - विशिष्ट वेरिएबल्स या स्टेट्स को लॉग करने के लिए VisualVM-MBeans प्लगइन के साथ उपयोग करें।
  - **सीमाएँ**: वेरिएबल्स को लॉग करने के लिए मैनुअल कॉन्फ़िगरेशन की आवश्यकता होती है।

- **BTrace**:
  - Java के लिए एक डायनामिक ट्रेसिंग टूल जो आपको एक चल रहे JVM में ट्रेसिंग लॉजिक इंजेक्ट करने की अनुमति देता है।
  - उदाहरण स्क्रिप्ट:

    ```java
    import com.sun.btrace.annotations.*;
    import static com.sun.btrace.BTraceUtils.*;

    @BTrace
    public class TraceVariables {
        @OnMethod(clazz = "MyApp", method = "main")
        public static void trace(@ProbeMethodName String methodName, @AllLocals Object[] locals) {
            println("Method: " + methodName + ", Locals: " + Arrays.toString(locals));
        }
    }
    ```
  - **सीमाएँ**: सावधानीपूर्वक स्क्रिप्टिंग की आवश्यकता होती है और आसानी से सभी लोकल वेरिएबल्स को कैप्चर नहीं कर सकता।

---

### सिफारिश
कोई एकल JVM फ्लैग नहीं है जो हर स्टेटमेंट के लिए हर वेरिएबल और स्टेट को ऑटोमैटिकली लॉग करता है, क्योंकि यह परफॉर्मेंस और आउटपुट वॉल्यूम के कारण अव्यावहारिक होगा। इसके बजाय, अपनी आवश्यकताओं के आधार पर निम्नलिखित पर विचार करें:

- **डेवलपमेंट के लिए**: फाइन-ग्रेन्ड कंट्रोल के लिए ब्रेकपॉइंट्स और लॉग पॉइंट्स के साथ एक डीबगर (जैसे IntelliJ IDEA) का उपयोग करें।
- **ऑटोमेटेड लॉगिंग के लिए**: मैनुअल लॉग स्टेटमेंट्स के साथ एक लॉगिंग फ्रेमवर्क (SLF4J/Logback) या मेथड-लेवल लॉगिंग के लिए AspectJ का उपयोग करें।
- **एडवांस्ड यूज़ केस के लिए**: डायनामिक ट्रेसिंग के लिए Byte Buddy के साथ एक Java एजेंट इम्प्लीमेंट करें या BTrace का उपयोग करें।
- **प्रोडक्शन मॉनिटरिंग के लिए**: बिना कोड बदलाव के प्रोफाइलिंग के लिए Java Flight Recorder या VisualVM का उपयोग करें।

यदि आप विशिष्ट वेरिएबल्स या मेथड्स को ऑटोमैटिकली लॉग करना चाहते हैं, तो मैं आपको एक Java एजेंट या AspectJ कॉन्फ़िगरेशन सेट अप करने में मदद कर सकता हूँ। वैकल्पिक रूप से, यदि आपके पास कोई विशिष्ट कोड स्निपेट है, तो मैं आपको दिखा सकता हूँ कि लॉगिंग कैसे जोड़ें या इसे प्रभावी ढंग से डीबग करें। मुझे अपनी प्राथमिकताएं या बाधाएं बताएं!