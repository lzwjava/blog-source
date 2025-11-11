---
audio: false
generated: true
lang: hi
layout: post
title: एस्पेक्टजे विथ जावा एंड स्प्रिंग बूट
translated: true
type: note
---

## विषय सूची
1. [एस्पेक्ट-ओरिएंटेड प्रोग्रामिंग (AOP) का परिचय](#परिचय-एस्पेक्ट-ओरिएंटेड-प्रोग्रामिंग-aop)
2. [AspectJ अवलोकन](#aspectj-अवलोकन)
3. [Java के साथ AspectJ](#java-के-साथ-aspectj)
4. [Spring Boot के साथ AspectJ](#spring-boot-के-साथ-aspectj)
5. [सामान्य उपयोग के मामले](#सामान्य-उपयोग-के-मामले)
6. [सर्वोत्तम अभ्यास](#सर्वोत्तम-अभ्यास)
7. [प्रदर्शन संबंधी विचार](#प्रदर्शन-संबंधी-विचार)

## एस्पेक्ट-ओरिएंटेड प्रोग्रामिंग (AOP) का परिचय

AOP एक प्रोग्रामिंग प्रतिमान है जो क्रॉस-कटिंग कॉन्सर्न के पृथक्करण द्वारा मॉड्यूलरिटी बढ़ाने का लक्ष्य रखता है। क्रॉस-कटिंग कॉन्सर्न ऐसी कार्यक्षमताएं हैं जो सिस्टम के कई हिस्सों में फैली होती हैं (जैसे लॉगिंग, सुरक्षा, लेन-देन प्रबंधन)।

मुख्य AOP अवधारणाएं:
- **एस्पेक्ट**: एक चिंता का मॉड्यूलराइजेशन जो कई कक्षाओं में फैला हो
- **जॉइन पॉइंट**: प्रोग्राम निष्पादन के दौरान एक बिंदु (मेथड कॉल, फील्ड एक्सेस, आदि)
- **एडवाइस**: किसी विशेष जॉइन पॉइंट पर की गई कार्रवाई
- **पॉइंटकट**: जॉइन पॉइंट से मेल खाने वाला प्रिडिकेट
- **वीविंग**: अन्य एप्लिकेशन प्रकारों के साथ एस्पेक्ट को जोड़ना

## AspectJ अवलोकन

AspectJ Java के लिए सबसे लोकप्रिय और पूर्ण-सुविधाओं वाला AOP कार्यान्वयन है। यह प्रदान करता है:
- एक शक्तिशाली पॉइंटकट भाषा
- विभिन्न वीविंग तंत्र (कंपाइल-टाइम, पोस्ट-कंपाइल, लोड-टाइम)
- Spring AOP द्वारा प्रदान किए गए समर्थन से परे पूर्ण AOP समर्थन

### AspectJ बनाम Spring AOP

| फीचर            | AspectJ | Spring AOP |
|--------------------|---------|------------|
| जॉइन पॉइंट        | मेथड एक्जीक्यूशन, कंस्ट्रक्टर कॉल, फील्ड एक्सेस, आदि | केवल मेथड एक्जीक्यूशन |
| वीविंग            | कंपाइल-टाइम, पोस्ट-कंपाइल, लोड-टाइम | रनटाइम प्रॉक्सीइंग |
| प्रदर्शन        | बेहतर (कोई रनटाइम ओवरहेड नहीं) | थोड़ा धीमा (प्रॉक्सी का उपयोग करता है) |
| जटिलता         | अधिक जटिल | सरल |
| निर्भरताएं       | AspectJ कंपाइलर/वीवर की आवश्यकता होती है | Spring में बिल्ट-इन |

## Java के साथ AspectJ

### सेटअप

1. अपने `pom.xml` (Maven) में AspectJ निर्भरताएं जोड़ें:

```xml
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjrt</artifactId>
    <version>1.9.7</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.7</version>
</dependency>
```

2. कंपाइल-टाइम वीविंग के लिए AspectJ Maven प्लगइन कॉन्फ़िगर करें:

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>aspectj-maven-plugin</artifactId>
    <version>1.14.0</version>
    <configuration>
        <complianceLevel>11</complianceLevel>
        <source>11</source>
        <target>11</target>
        <showWeaveInfo>true</showWeaveInfo>
        <verbose>true</verbose>
        <Xlint>ignore</Xlint>
        <encoding>UTF-8</encoding>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>compile</goal>
                <goal>test-compile</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

### एस्पेक्ट बनाना

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;

@Aspect
public class LoggingAspect {

    // पॉइंटकट परिभाषा
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // एडवाइस
    @Before("serviceMethods()")
    public void logBeforeServiceMethods() {
        System.out.println("एक सर्विस मेथड को निष्पादित किया जाने वाला है");
    }
}
```

### एडवाइस प्रकार

1. **बिफोर**: जॉइन पॉइंट से पहले निष्पादित
2. **आफ्टर**: जॉइन पॉइंट के पूरा होने के बाद निष्पादित (सामान्य रूप से या असाधारण रूप से)
3. **आफ्टररिटर्निंग**: जॉइन पॉइंट के सामान्य रूप से पूरा होने के बाद निष्पादित
4. **आफ्टरथ्रोइंग**: यदि कोई मेथड अपवाद फेंककर बाहर निकलती है तो निष्पादित
5. **अराउंड**: जॉइन पॉइंट को घेरता है (सबसे शक्तिशाली एडवाइस)

### पॉइंटकट एक्सप्रेशन

AspectJ एक समृद्ध पॉइंटकट एक्सप्रेशन भाषा प्रदान करता है:

```java
// पैकेज में मेथड एक्जीक्यूशन
@Pointcut("execution(* com.example.service.*.*(..))")

// क्लास में मेथड एक्जीक्यूशन
@Pointcut("execution(* com.example.service.UserService.*(..))")

// विशिष्ट नाम वाली मेथड
@Pointcut("execution(* *..find*(..))")

// विशिष्ट रिटर्न प्रकार के साथ
@Pointcut("execution(public String com.example..*(..))")

// विशिष्ट पैरामीटर प्रकारों के साथ
@Pointcut("execution(* *.*(String, int))")

// पॉइंटकट को संयोजित करना
@Pointcut("serviceMethods() && findMethods()")
```

## Spring Boot के साथ AspectJ

### सेटअप

1. Spring AOP और AspectJ निर्भरताएं जोड़ें:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.7</version>
</dependency>
```

2. अपने Spring Boot एप्लिकेशन में AspectJ समर्थन सक्षम करें:

```java
@SpringBootApplication
@EnableAspectJAutoProxy
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

### उदाहरण: निष्पादन समय लॉगिंग

```java
@Aspect
@Component
public class ExecutionTimeAspect {

    private static final Logger logger = LoggerFactory.getLogger(ExecutionTimeAspect.class);

    @Around("@annotation(com.example.annotation.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long startTime = System.currentTimeMillis();
        
        Object proceed = joinPoint.proceed();
        
        long executionTime = System.currentTimeMillis() - startTime;
        
        logger.info("{} executed in {} ms", 
            joinPoint.getSignature(), executionTime);
        
        return proceed;
    }
}
```

एक कस्टम एनोटेशन बनाएं:

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

इसे मेथड पर उपयोग करें:

```java
@Service
public class UserService {
    
    @LogExecutionTime
    public List<User> getAllUsers() {
        // implementation
    }
}
```

### उदाहरण: लेन-देन प्रबंधन

```java
@Aspect
@Component
public class TransactionAspect {

    @Autowired
    private PlatformTransactionManager transactionManager;

    @Around("@annotation(com.example.annotation.Transactional)")
    public Object manageTransaction(ProceedingJoinPoint joinPoint) throws Throwable {
        TransactionDefinition def = new DefaultTransactionDefinition();
        TransactionStatus status = transactionManager.getTransaction(def);
        
        try {
            Object result = joinPoint.proceed();
            transactionManager.commit(status);
            return result;
        } catch (Exception e) {
            transactionManager.rollback(status);
            throw e;
        }
    }
}
```

## सामान्य उपयोग के मामले

1. **लॉगिंग**: मेथड प्रवेश/अपवादों का केंद्रीकृत लॉगिंग
2. **प्रदर्शन मॉनिटरिंग**: निष्पादन समय ट्रैक करना
3. **लेन-देन प्रबंधन**: घोषणात्मक लेन-देन सीमाएं
4. **सुरक्षा**: प्राधिकरण जांचें
5. **त्रुटि प्रबंधन**: सुसंगत अपवाद हैंडलिंग
6. **कैशिंग**: स्वचालित मेथड परिणाम कैशिंग
7. **वैलिडेशन**: पैरामीटर वैलिडेशन
8. **ऑडिटिंग**: ट्रैक करें कि किसने क्या और कब किया

## सर्वोत्तम अभ्यास

1. **एस्पेक्ट को केंद्रित रखें**: प्रत्येक एस्पेक्ट को एक चिंता को संभालना चाहिए
2. **सार्थक नामों का उपयोग करें**: स्पष्ट एस्पेक्ट और पॉइंटकट नाम
3. **एस्पेक्ट में बिजनेस लॉजिक से बचें**: एस्पेक्ट को क्रॉस-कटिंग कॉन्सर्न संभालना चाहिए, कोर लॉजिक नहीं
4. **एस्पेक्ट को डॉक्यूमेंट करें**: विशेष रूप से जटिल पॉइंटकट
5. **प्रदर्शन पर विचार करें**: अराउंड एडवाइस प्रदर्शन को प्रभावित कर सकती है
6. **एस्पेक्ट का परीक्षण करें**: एस्पेक्ट को किसी अन्य कोड की तरह परीक्षण की आवश्यकता होती है
7. **एनोटेशन का उपयोग करें**: कस्टम एनोटेशन एस्पेक्ट को अधिक घोषणात्मक बनाते हैं
8. **execution() बनाम @annotation() के साथ सावधान रहें**: जानें कि प्रत्येक का उपयोग कब करना है

## प्रदर्शन संबंधी विचार

1. **कंपाइल-टाइम वीविंग** आम तौर पर सबसे तेज़ विकल्प है
2. **लोड-टाइम वीविंग** क्लास लोडिंग के दौरान कुछ ओवरहेड जोड़ता है
3. **रनटाइम वीविंग** (Spring AOP) में सबसे अधिक ओवरहेड होता है
4. **जटिल पॉइंटकट** प्रदर्शन को प्रभावित कर सकते हैं
5. **अराउंड एडवाइस** अन्य एडवाइस प्रकारों की तुलना में अधिक महंगी है

प्रोडक्शन में अधिकतम प्रदर्शन के लिए:
- जहां संभव हो कंपाइल-टाइम वीविंग का उपयोग करें
- पॉइंटकट को सरल रखें
- अत्यधिक व्यापक पॉइंटकट एक्सप्रेशन से बचें

## निष्कर्ष

AspectJ Java और Spring Boot एप्लिकेशन में क्रॉस-कटिंग कॉन्सर्न को लागू करने का एक शक्तिशाली तरीका प्रदान करता है। जबकि Spring AOP कई मामलों के लिए सरल और पर्याप्त है, AspectJ अधिक क्षमताएं प्रदान करता है जब आपको मेथड इंटरसेप्शन से आगे जाने की आवश्यकता होती है। इस गाइड में बताए गए पैटर्न और सर्वोत्तम अभ्यासों का पालन करके, आप अधिक मॉड्यूलर, रखरखाव योग्य एप्लिकेशन बनाने के लिए AspectJ का प्रभावी ढंग से उपयोग कर सकते हैं।