---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग एओपी (एस्पेक्ट-ओरिएंटेड प्रोग्रामिंग)
translated: true
type: note
---

स्प्रिंग एओपी (एस्पेक्ट-ओरिएंटेड प्रोग्रामिंग) स्प्रिंग फ्रेमवर्क की एक शक्तिशाली सुविधा है जो आपको लॉगिंग, सुरक्षा, या लेनदेन प्रबंधन जैसी क्रॉस-कटिंग चिंताओं को मॉड्यूलराइज़ करने की अनुमति देती है। मैं आपको एक व्यावहारिक दृष्टिकोण के साथ स्प्रिंग एओपी एपीआई का उपयोग करने की मूल बातें समझाऊंगा।

### 1. **मुख्य अवधारणाओं को समझें**
एपीआई में गोता लगाने से पहले, आपको यह जानना आवश्यक है:
- **एस्पेक्ट**: एक मॉड्यूल जो एक क्रॉस-कटिंग चिंता को समाहित करता है (जैसे, लॉगिंग)।
- **एडवाइस**: एक विशेष बिंदु पर एक एस्पेक्ट द्वारा की गई कार्रवाई (जैसे, किसी मेथड के चलने से "पहले" या "बाद में")।
- **पॉइंटकट**: एक प्रिडिकेट जो परिभाषित करता है कि एडवाइस को कहाँ लागू किया जाना चाहिए (जैसे, विशिष्ट मेथड्स या क्लासेस)।
- **जॉइन पॉइंट**: प्रोग्राम एक्सेक्यूशन में एक बिंदु जहां एक एस्पेक्ट लागू किया जा सकता है (जैसे, मेथड इनवोकेशन)।

स्प्रिंग एओपी प्रॉक्सी-आधारित है, जिसका अर्थ है कि यह एस्पेक्ट्स लागू करने के लिए आपकी बीन्स को प्रॉक्सी के साथ रैप करता है।

### 2. **अपना प्रोजेक्ट सेट अप करें**
स्प्रिंग एओपी का उपयोग करने के लिए, आपको चाहिए:
- एक स्प्रिंग बूट प्रोजेक्ट (या एओपी डिपेंडेंसीज़ के साथ एक स्प्रिंग प्रोजेक्ट)।
- यदि Maven का उपयोग कर रहे हैं तो अपने `pom.xml` में डिपेंडेंसी जोड़ें:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-aop</artifactId>
  </dependency>
  ```
- अपने कॉन्फ़िगरेशन में एओपी सक्षम करें (आमतौर पर स्प्रिंग बूट के साथ स्वचालित, लेकिन आप इसे `@EnableAspectJAutoProxy` के साथ स्पष्ट रूप से सक्षम कर सकते हैं)।

### 3. **एक एस्पेक्ट बनाएँ**
स्प्रिंग एओपी एपीआई का उपयोग करके एक एस्पेक्ट को परिभाषित करने का तरीका यहां बताया गया है:

#### उदाहरण: लॉगिंग एस्पेक्ट
```java
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class LoggingAspect {

    // बिफोर एडवाइस: मेथड एक्सेक्यूशन से पहले चलती है
    @Before("execution(* com.example.myapp.service.*.*(..))")
    public void logBeforeMethod() {
        System.out.println("सर्विस पैकेज में एक मेथड चलने वाली है");
    }

    // आफ्टर एडवाइस: मेथड एक्सेक्यूशन के बाद चलती है
    @After("execution(* com.example.myapp.service.*.*(..))")
    public void logAfterMethod() {
        System.out.println("सर्विस पैकेज में एक मेथड का एक्सेक्यूशन समाप्त हो गया है");
    }
}
```
- `@Aspect`: इस क्लास को एक एस्पेक्ट के रूप में चिह्नित करता है।
- `@Component`: इसे एक स्प्रिंग बीन के रूप में पंजीकृत करता है।
- `execution(* com.example.myapp.service.*.*(..))`: एक पॉइंटकट एक्सप्रेशन जिसका अर्थ है "`service` पैकेज के तहत किसी भी क्लास की किसी भी मेथड को किसी भी रिटर्न टाइप और किसी भी पैरामीटर के साथ।"

### 4. **सामान्य एडवाइस प्रकार**
स्प्रिंग एओपी कई एडवाइस एनोटेशन का समर्थन करता है:
- `@Before`: मिलान किए गए मेथड से पहले चलता है।
- `@After`: मेथड के बाद चलता है (सफलता या विफलता की परवाह किए बिना)।
- `@AfterReturning`: एक मेथड के सफलतापूर्वक लौटने के बाद चलता है।
- `@AfterThrowing`: चलता है यदि मेथड एक एक्सेप्शन फेंकती है।
- `@Around`: मेथड को रैप करता है, जिससे आप एक्सेक्यूशन को नियंत्रित कर सकते हैं (सबसे शक्तिशाली)।

#### उदाहरण: अराउंड एडवाइस
```java
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class PerformanceAspect {

    @Around("execution(* com.example.myapp.service.*.*(..))")
    public Object measureTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object result = joinPoint.proceed(); // मूल मेथड को निष्पादित करें
        long end = System.currentTimeMillis();
        System.out.println("एक्सेक्यूशन समय: " + (end - start) + "ms");
        return result;
    }
}
```
- `ProceedingJoinPoint`: इंटरसेप्ट की जा रही मेथड का प्रतिनिधित्व करता है।
- `proceed()`: मूल मेथड को इनवोक करता है।

### 5. **पॉइंटकट एक्सप्रेशन**
पॉइंटकट्स परिभाषित करते हैं कि एडवाइस कहाँ लागू होती है। सामान्य सिंटैक्स:
- `execution(modifiers? return-type declaring-type? method-name(params) throws?)`
  - उदाहरण: `execution(public String com.example.myapp.service.MyService.get*(..))`
    - `MyService` में "get" से शुरू होने वाली पब्लिक मेथड्स से मेल खाता है जो एक `String` लौटाती हैं।

आप पॉइंटकट्स को संयोजित भी कर सकते हैं:
```java
@Pointcut("execution(* com.example.myapp.service.*.*(..))")
public void serviceMethods() {}

@Before("serviceMethods()")
public void logBeforeService() {
    System.out.println("सर्विस मेथड कॉल की गई");
}
```

### 6. **मेथड विवरण तक पहुंचें**
आप मेथड आर्गुमेंट्स, सिग्नेचर्स, या मेटाडेटा तक पहुंच सकते हैं:
```java
@Before("execution(* com.example.myapp.service.*.*(..))")
public void logMethodDetails(JoinPoint joinPoint) {
    String methodName = joinPoint.getSignature().getName();
    Object[] args = joinPoint.getArgs();
    System.out.println("मेथड " + methodName + " को " + args.length + " आर्गुमेंट्स के साथ कॉल किया गया");
}
```

### 7. **रन और टेस्ट करें**
- कुछ मेथड्स के साथ एक सर्विस क्लास (जैसे, `MyService`) बनाएं।
- अपना स्प्रिंग एप्लिकेशन रन करें।
- एस्पेक्ट स्वचालित रूप से मिलान करने वाली मेथड्स पर लागू हो जाएगा।

#### उदाहरण सर्विस:
```java
@Service
public class MyService {
    public String sayHello(String name) {
        return "Hello, " + name;
    }
}
```

जब आप `myService.sayHello("Alice")` कॉल करेंगे, तो लॉगिंग या परफॉर्मेंस एस्पेक्ट्स काम करने लगेंगे।

### सुझाव
- **परफॉर्मेंस**: एओपी प्रॉक्सी के कारण ओवरहेड जोड़ता है, इसलिए इसका विवेकपूर्ण उपयोग करें।
- **स्कोप**: स्प्रिंग एओपी केवल स्प्रिंग-मैनेज्ड बीन्स पर काम करता है। गैर-स्प्रिंग ऑब्जेक्ट्स के लिए, AspectJ (एक अधिक शक्तिशाली विकल्प) पर विचार करें।
- **डिबगिंग**: देखने के लिए कि प्रॉक्सी कैसे लागू होते हैं, `org.springframework.aop` के लिए डिबग लॉगिंग सक्षम करें।

यदि आपके पास कोई विशिष्ट उपयोग का मामला है या किसी विशेष कार्यान्वयन में सहायता की आवश्यकता है, तो मुझे बताएं, और मैं स्पष्टीकरण को और अधिक अनुकूलित कर दूंगा!