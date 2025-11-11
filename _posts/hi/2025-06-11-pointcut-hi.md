---
audio: false
generated: true
lang: hi
layout: post
title: पॉइंटकट एक्सप्रेशन को समझना
translated: true
type: note
---

आप Spring AOP में AspectJ पॉइंटकट एक्सप्रेशन की एक व्यापक गाइड मांग रहे हैं, विशेष रूप से `execution` पर ध्यान केंद्रित करते हुए, और यह कि वाइल्डकार्ड का उपयोग कैसे करें, क्लास नाम मैच करें (उपसर्ग/प्रत्यय), और साथ ही अन्य एडवाइस प्रकारों जैसे `@AfterReturning` के बारे में जानें। आइए इसे समझते हैं।

### Spring AOP में पॉइंटकट एक्सप्रेशन को समझना (AspectJ सिंटैक्स)

Spring AOP यह निर्धारित करने के लिए AspectJ पॉइंटकट एक्सप्रेशन का उपयोग करता है कि *कहां* एक एडवाइस (जैसे `@Before`, `@AfterReturning`, आदि) लागू होनी चाहिए। आपके प्रश्न का मूल `execution` पॉइंटकट डिज़ाइनेटर के इर्द-गिर्द घूमता है, जो सबसे अधिक इस्तेमाल किया जाने वाला है।

#### `execution` पॉइंटकट डिज़ाइनेटर

`execution` पॉइंटकट डिज़ाइनेटर मेथड एक्सिक्यूशन से मेल खाता है। इसका सामान्य सिंटैक्स है:

`execution(modifiers-pattern? ret-type-pattern declaring-type-pattern?name-pattern(param-pattern) throws-pattern?)`

आइए घटकों को तोड़ते हैं:

* **`modifiers-pattern?`**: ऑप्शनल। मेथड मॉडिफायर से मेल खाता है (जैसे, `public`, `private`, `protected`)।
* **`ret-type-pattern`**: आवश्यक। मेथड के रिटर्न टाइप से मेल खाता है।
* **`declaring-type-pattern?`**: ऑप्शनल। फुली क्वालिफाइड क्लास नाम से मेल खाता है जहां मेथड डिक्लेयर की गई है।
* **`name-pattern`**: आवश्यक। मेथड के नाम से मेल खाता है।
* **`param-pattern`**: आवश्यक। मेथड के पैरामीटर्स से मेल खाता है।
* **`throws-pattern?`**: ऑप्शनल। मेथड द्वारा throw किए गए एक्सेप्शन से मेल खाता है।

#### आपका उदाहरण: `@Before("execution(* com.example.service.*.*(..))")`

आइए आपके दिए गए उदाहरण को समझते हैं:

* `@Before`: यह एक एडवाइस एनोटेशन है, जिसका अर्थ है कि एनोटेटेड मेथड मैच किए गए जॉइन पॉइंट से *पहले* चलेगी।
* `execution()`: पॉइंटकट डिज़ाइनेटर।
* `*`: किसी भी रिटर्न टाइप से मेल खाता है।
* `com.example.service.*.*`:
    * `com.example.service`: `com.example.service` पैकेज से मेल खाता है।
    * `.*`: `service` के बाद पहला `*` `com.example.service` पैकेज के भीतर किसी भी क्लास से मेल खाता है।
    * `.`: पैकेज/क्लास और मेथड के बीच सेपरेटर।
    * `*`: दूसरा `*` उन क्लासेज के भीतर किसी भी मेथड नाम से मेल खाता है।
* `(..)`: पैरामीटर्स की किसी भी संख्या से मेल खाता है (शून्य या अधिक, किसी भी प्रकार के)।

**सरल भाषा में:** यह पॉइंटकट `com.example.service` पैकेज के भीतर *किसी भी क्लास* में *किसी भी मेथड* के एक्सिक्यूशन से मेल खाता है।

---

### पॉइंटकट एक्सप्रेशन में वाइल्डकार्ड

वाइल्डकार्ड लचीले पॉइंटकट एक्सप्रेशन बनाने के लिए महत्वपूर्ण हैं।

* **`*` (सिंगल एस्टेरिस्क)**:
    * नाम पैटर्न में किसी एकल एलिमेंट से मेल खाता है (जैसे, कोई भी रिटर्न टाइप, कोई भी क्लास नाम, कोई भी मेथड नाम)।
    * पैकेज नाम में किसी एकल सेगमेंट से मेल खाता है (जैसे, `com.example.*.service`, `com.example.foo.service` से मेल खाएगा)।
* **`..` (डबल डॉट)**:
    * **पैकेज पैटर्न में**: पैकेज नाम में शून्य या अधिक सेगमेंट से मेल खाता है।
        * `com.example..service`: `com.example.service`, `com.example.foo.service`, `com.example.foo.bar.service`, आदि से मेल खाएगा।
    * **पैरामीटर पैटर्न में**: किसी भी प्रकार के शून्य या अधिक आर्गुमेंट से मेल खाता है।
        * `(..)`: आर्गुमेंट की किसी भी संख्या से मेल खाता है।
        * `(java.lang.String, ..)`: पहले आर्गुमेंट के रूप में `String` वाली मेथड से मेल खाता है, जिसके बाद कोई भी संख्या में अन्य आर्गुमेंट हों।
        * `(.., java.lang.Long)`: किसी भी संख्या में शुरुआती आर्गुमेंट वाली मेथड से मेल खाता है, जो `Long` के साथ समाप्त होती है।

---

### क्लास नाम मैच करना

#### 1. प्रत्यय (Suffix) वाले क्लास नाम से मेल खाना

किसी विशिष्ट प्रत्यय वाली क्लासेज से मेल खाने के लिए, आप प्रत्यय से पहले वाइल्डकार्ड लगाते हैं।

**उदाहरण: `ServiceImpl` से समाप्त होने वाली सभी क्लासेज से मेल खाएं**

```java
@Before("execution(* com.example.service.*ServiceImpl.*(..))")
```

* `*ServiceImpl`: किसी भी क्लास नाम से मेल खाता है जो `ServiceImpl` से समाप्त होता है।

**उदाहरण: `com.example.web` के किसी भी सब-पैकेज में `Controller` से समाप्त होने वाली सभी क्लासेज से मेल खाएं**

```java
@Before("execution(* com.example.web..*Controller.*(..))")
```

* `com.example.web..`: `com.example.web` और इसके किसी भी सब-पैकेज से मेल खाता है।
* `*Controller`: `Controller` से समाप्त होने वाले किसी भी क्लास नाम से मेल खाता है।

#### 2. उपसर्ग (Prefix) वाले क्लास नाम से मेल खाना

किसी विशिष्ट उपसर्ग से शुरू होने वाली क्लासेज से मेल खाने के लिए, आप उपसर्ग के बाद वाइल्डकार्ड लगाते हैं।

**उदाहरण: `User` से शुरू होने वाली सभी क्लासेज से मेल खाएं**

```java
@Before("execution(* com.example.service.User*.*(..))")
```

* `User*`: किसी भी क्लास नाम से मेल खाता है जो `User` से शुरू होता है।

**उदाहरण: `com.example.admin` पैकेज में `Admin` से शुरू होने वाली सभी क्लासेज से मेल खाएं**

```java
@Before("execution(* com.example.admin.Admin*.*(..))")
```

#### 3. विशिष्ट क्लास नाम से मेल खाना (सटीक मिलान)

सटीक मिलान के लिए वाइल्डकार्ड की आवश्यकता नहीं है।

**उदाहरण: केवल `com.example.service.UserServiceImpl` में मेथड से मेल खाएं**

```java
@Before("execution(* com.example.service.UserServiceImpl.*(..))")
```

---

### विभिन्न प्रकार के पॉइंटकट डिज़ाइनेटर

हालांकि `execution` सबसे आम है, AspectJ जॉइन पॉइंट्स निर्दिष्ट करने के लिए कई अन्य पॉइंटकट डिज़ाइनेटर प्रदान करता है। आप इन्हें लॉजिकल ऑपरेटर्स (`and`, `or`, `not` या `&&`, `||`, `!`) का उपयोग करके संयोजित कर सकते हैं।

यहां सबसे महत्वपूर्ण हैं:

1.  **`execution()`**: जैसा चर्चा हुई, मेथड एक्सिक्यूशन से मेल खाता है।
    * उदाहरण: `@Before("execution(* com.example.service.UserService.*(..))")`

2.  **`within()`**: उन जॉइन पॉइंट्स से मेल खाता है जहां कोड एक निश्चित प्रकार (क्लास) के भीतर है। इसका उपयोग अक्सर अन्य पॉइंटकट्स के स्कोप को सीमित करने के लिए किया जाता है।
    * उदाहरण: `@Before("within(com.example.service.*) && execution(* *(..))")`
        * यह `within` और `execution` को संयोजित करता है। इसका अर्थ है "`com.example.service` पैकेज के भीतर किसी भी क्लास में कोई भी मेथड एक्सिक्यूशन।" `execution` भाग तब किसी भी मेथड के लिए सिर्फ एक वाइल्डकार्ड है, क्योंकि `within` क्लास मैचिंग को संभालता है।

3.  **`this()`**: उन जॉइंट पॉइंट्स से मेल खाता है जहां प्रॉक्सी *स्वयं* दिए गए प्रकार का एक इंस्टेंस है। यह सरल एडवाइस के लिए कम इस्तेमाल किया जाता है और अधिक इंट्रोडक्शन या सेल्फ-इनवोकेशन इश्यूज के लिए।
    * उदाहरण: `@Around("this(com.example.service.UserService)")`
        * मैच करता है यदि AOP प्रॉक्सी `UserService` को इम्प्लीमेंट करता है।

4.  **`target()`**: उन जॉइन पॉइंट्स से मेल खाता है जहां *टार्गेट ऑब्जेक्ट* (वास्तव में एडवाइस किया जा रहा ऑब्जेक्ट, प्रॉक्सी नहीं) दिए गए प्रकार का एक इंस्टेंस है। जब आप अंतर्निहित इम्प्लीमेंटेशन की परवाह करते हैं तो यह अक्सर `this()` से अधिक सहज होता है।
    * उदाहरण: `@Around("target(com.example.service.UserServiceImpl)")`
        * मैच करता है यदि टार्गेट ऑब्जेक्ट `UserServiceImpl` का एक इंस्टेंस है।

5.  **`args()`**: उन जॉइन पॉइंट्स से मेल खाता है जहां आर्गुमेंट एक निश्चित प्रकार के होते हैं या एक निश्चित पैटर्न से मेल खाते हैं।
    * उदाहरण: `@Before("execution(* com.example.service.*.*(String, ..))")`
        * उन मेथड से मेल खाता है जहां पहला आर्गुमेंट एक `String` है।
    * उदाहरण: `@Before("args(java.lang.String, int)")`
        * उन मेथड से मेल खाता है जो ठीक एक `String` और उसके बाद एक `int` लेती हैं।
    * उदाहरण: `@Before("args(name, age)")` जहां `name` और `age` को तब एडवाइस मेथड पैरामीटर्स से बाइंड किया जा सकता है।

6.  **`bean()`**: (Spring-विशिष्ट) विशिष्ट नामों या नाम पैटर्न वाले Spring beans पर निष्पादित मेथड से मेल खाता है।
    * उदाहरण: `@Before("bean(userService) && execution(* *(..))")`
        * "userService" नाम के Spring bean पर किसी भी मेथड एक्सिक्यूशन से मेल खाता है।
    * उदाहरण: `@Before("bean(*Service) && execution(* *(..))")`
        * उन Spring beans पर किसी भी मेथड एक्सिक्यूशन से मेल खाता है जिनके नाम "Service" से समाप्त होते हैं।

7.  **`@annotation()`**: उन जॉइन पॉइंट्स से मेल खाता है जहां टार्गेट मेथड (या `within` के लिए क्लास) एक विशिष्ट एनोटेशन के साथ एनोटेटेड है।
    * उदाहरण: `@Before("@annotation(com.example.annotation.Loggable)")`
        * किसी भी मेथड से मेल खाता है जो `@Loggable` से एनोटेटेड है।
    * उदाहरण: `@Before("execution(* *(..)) && @annotation(org.springframework.transaction.annotation.Transactional)")`
        * किसी भी मेथड एक्सिक्यूशन से मेल खाता है जो `@Transactional` से एनोटेटेड है।

8.  **`@within()`**: उन जॉइन पॉइंट्स से मेल खाता है जहां डिक्लेयरिंग टाइप (क्लास) एक विशिष्ट एनोटेशन के साथ एनोटेटेड है।
    * उदाहरण: `@Before("@within(org.springframework.stereotype.Service) && execution(* *(..))")`
        * किसी भी मेथड एक्सिक्यूशन से मेल खाता है जो `@Service` से एनोटेटेड क्लास के भीतर है।

9.  **`@target()`**: उन जॉइन पॉइंट्स से मेल खाता है जहां टार्गेट ऑब्जेक्ट की क्लास के पास दिया गया एनोटेशन है।
    * उदाहरण: `@Around("@target(com.example.annotation.Auditable)")`

10. **`@args()`**: उन जॉइन पॉइंट्स से मेल खाता है जहां मेथड को पास किए गए वास्तविक आर्गुमेंट के रनटाइम टाइप के पास दिए गए प्रकार का एनोटेशन है।
    * उदाहरण: `@Before("@args(com.example.annotation.ValidInput)")`

---

### एडवाइस प्रकार (एनोटेशन)

आपने `@AfterReturning` और "कोई अन्य जिसे हम एनोटेशन में उपयोग कर सकते हैं" का उल्लेख किया। Spring AOP कई एडवाइस प्रकार प्रदान करता है, जिनमें से प्रत्येक जॉइन पॉइंट के लाइफसाइकल में एक अलग बिंदु पर निष्पादित होता है:

1.  **`@Before`**:
    * मैच की गई मेथड एक्सिक्यूशन से *पहले* निष्पादित होता है।
    * उदाहरण: सर्विस मेथड चलने से पहले रिक्वेस्ट डिटेल्स लॉग करना।
    * मेथड को निष्पादित होने से रोक नहीं सकता या उसके रिटर्न वैल्यू को बदल नहीं सकता।

2.  **`@AfterReturning`**:
    * मैच की गई मेथड के *सफलतापूर्वक* रिटर्न करने के *बाद* निष्पादित होता है (बिना एक्सेप्शन throw किए)।
    * मेथड के रिटर्न वैल्यू तक पहुंच सकता है।
    * सिंटैक्स: `@AfterReturning(pointcut="yourPointcut()", returning="result")`
    * उदाहरण:
        ```java
        @AfterReturning(pointcut="execution(* com.example.service.UserService.getUserById(..))", returning="user")
        public void logUserRetrieval(Object user) {
            System.out.println("User retrieved: " + user);
        }
        ```
        *नोट: `returning` एट्रिब्यूट नाम (इस मामले में `user`) एडवाइस मेथड में पैरामीटर नाम से मेल खाना चाहिए।*

3.  **`@AfterThrowing`**:
    * मैच की गई मेथड के एक्सेप्शन throw करने के *बाद* निष्पादित होता है।
    * throw किए गए एक्सेप्शन तक पहुंच सकता है।
    * सिंटैक्स: `@AfterThrowing(pointcut="yourPointcut()", throwing="ex")`
    * उदाहरण:
        ```java
        @AfterThrowing(pointcut="execution(* com.example.service.*.*(..))", throwing="ex")
        public void logException(Exception ex) {
            System.err.println("Exception occurred: " + ex.getMessage());
        }
        ```
        *नोट: `throwing` एट्रिब्यूट नाम (इस मामले में `ex`) एडवाइस मेथड में पैरामीटर नाम से मेल खाना चाहिए।*

4.  **`@After` (finally एडवाइस)**:
    * मैच की गई मेथड के पूरा होने के *बाद* निष्पादित होता है, भले ही वह सफलतापूर्वक रिटर्न हुई हो या एक्सेप्शन throw किया हो।
    * एक `finally` ब्लॉक के समान।
    * उदाहरण: मेथड आउटकम की परवाह किए बिना रिसोर्सेज रिलीज़ करना।
    * ```java
        @After("execution(* com.example.service.OrderService.placeOrder(..))")
        public void cleanupOrderProcess() {
            System.out.println("Order process completed (cleanup)");
        }
        ```

5.  **`@Around`**:
    * सबसे शक्तिशाली और लचीला एडवाइस प्रकार।
    * मैच की गई मेथड एक्सिक्यूशन के *चारों ओर* निष्पादित होता है।
    * आप वास्तविक मेथड को `ProceedingJoinPoint.proceed()` का उपयोग करके इनवोक करने के लिए जिम्मेदार हैं।
    * मेथड के आर्गुमेंट और रिटर्न वैल्यू का निरीक्षण, संशोधन, या यहां तक कि दमन कर सकता है।
    * एडवाइस्ड मेथड द्वारा throw किए गए एक्सेप्शन को पकड़ और हैंडल कर सकता है।
    * उदाहरण: परफॉर्मेंस मॉनिटरिंग, ट्रांजैक्शन मैनेजमेंट, कैशिंग।
    * ```java
        import org.aspectj.lang.ProceedingJoinPoint;
        import org.aspectj.lang.annotation.Around;
        import org.aspectj.lang.annotation.Aspect;

        @Aspect
        public class PerformanceMonitorAspect {

            @Around("execution(* com.example.service.*.*(..))")
            public Object profile(ProceedingJoinPoint joinPoint) throws Throwable {
                long start = System.currentTimeMillis();
                Object result = joinPoint.proceed(); // ओरिजिनल मेथड को निष्पादित करें
                long end = System.currentTimeMillis();
                System.out.println(joinPoint.getSignature().getName() + " executed in " + (end - start) + "ms");
                return result;
            }
        }
        ```

### पुन: प्रयोज्य पॉइंटकट्स को परिभाषित करना

बेहतर पठनीयता और पुन: प्रयोज्यता के लिए, आप `@Pointcut` का उपयोग करके नामित पॉइंटकट्स को परिभाषित कर सकते हैं।

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.AfterReturning;

@Aspect
public class MyServiceAspect {

    // com.example.service पैकेज में सभी मेथड के लिए एक पॉइंटकट परिभाषित करें
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // उन मेथड के लिए एक पॉइंटकट परिभाषित करें जो एक User ऑब्जेक्ट रिटर्न करती हैं
    @Pointcut("execution(com.example.model.User com.example.service.*.*(..))")
    public void returnsUser() {}

    // परिभाषित पॉइंटकट का उपयोग करना
    @Before("serviceMethods()")
    public void logBeforeServiceCall() {
        System.out.println("Before service method execution.");
    }

    // लॉजिकल AND के साथ पॉइंटकट्स को संयोजित करना
    @AfterReturning(pointcut="serviceMethods() && returnsUser()", returning="user")
    public void logUserReturned(Object user) {
        System.out.println("Service method returned user: " + user);
    }

    // आप आर्गुमेंट के साथ भी पॉइंटकट्स परिभाषित कर सकते हैं
    @Pointcut("execution(* com.example.repository.*.save(..)) && args(entity)")
    public void repositorySave(Object entity) {}

    @Before("repositorySave(entity)")
    public void logEntityBeforeSave(Object entity) {
        System.out.println("Saving entity: " + entity);
    }
}
```

यह व्यापक गाइड Spring AOP में पॉइंटकट एक्सप्रेशन, वाइल्डकार्ड उपयोग, क्लास नाम मैचिंग, और विभिन्न एडवाइस प्रकारों के मूल सिद्धांतों को कवर करती है। इन अवधारणाओं में महारत हासिल करने से आपको यह नियंत्रित करने की अनुमति मिलेगी कि आपकी क्रॉस-कटिंग कंसर्न कहां और कब लागू होती हैं।