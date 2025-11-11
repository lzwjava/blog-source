---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग एओपी गाइड
translated: true
type: note
---

## 1. स्प्रिंग AOP का परिचय

स्प्रिंग AOP (एस्पेक्ट-ओरिएंटेड प्रोग्रामिंग) स्प्रिंग फ्रेमवर्क का एक महत्वपूर्ण घटक है जो बिजनेस लॉजिक से अलग क्रॉस-कटिंग कंसर्न्स (जैसे लॉगिंग, सिक्योरिटी, ट्रांजैक्शन मैनेजमेंट) को लागू करने का एक तरीका प्रदान करता है।

### मुख्य अवधारणाएँ:
- **क्रॉस-कटिंग कंसर्न्स**: ऐसी फंक्शनैलिटी जो कई लेयर्स में फैली हो (लॉगिंग, सिक्योरिटी, आदि)
- **एस्पेक्ट**: एक कंसर्न का मॉड्यूलराइजेशन जो कई क्लासेज को क्रॉस करता है
- **जॉइन पॉइंट**: प्रोग्राम एक्सेक्यूशन के दौरान एक पॉइंट (मेथड एक्सेक्यूशन, एक्सेप्शन हैंडलिंग, आदि)
- **एडवाइस**: एक विशेष जॉइन पॉइंट पर एस्पेक्ट द्वारा की गई कार्रवाई
- **पॉइंटकट**: जॉइन पॉइंट्स से मेल खाने वाला प्रिडिकेट
- **वीविंग**: एडवाइज्ड ऑब्जेक्ट बनाने के लिए एस्पेक्ट्स को अन्य एप्लिकेशन टाइप्स से लिंक करना

## 2. स्प्रिंग AOP बनाम AspectJ

| फीचर               | स्प्रिंग AOP | AspectJ |
|-----------------------|-----------|---------|
| इम्प्लीमेंटेशन        | रनटाइम प्रॉक्सीइंग | कम्पाइल-टाइम/लोड-टाइम वीविंग |
| परफॉर्मेंस           | धीमा | तेज़ |
| सपोर्टेड जॉइन पॉइंट्स | केवल मेथड एक्सेक्यूशन | सभी (मेथड, कंस्ट्रक्टर, फील्ड एक्सेस, आदि) |
| कॉम्प्लेक्सिटी            | सरल | अधिक जटिल |
| डिपेंडेंसी            | कोई अतिरिक्त डिपेंडेंसी नहीं | AspectJ कंपाइलर/वीवर की आवश्यकता |

## 3. कोर AOP कंपोनेंट्स

### 3.1 एस्पेक्ट्स
`@Aspect` से एनोटेट की गई एक क्लास जिसमें एडवाइसेज और पॉइंटकट्स होते हैं।

```java
@Aspect
@Component
public class LoggingAspect {
    // एडवाइसेज और पॉइंटकट्स यहाँ जाएंगे
}
```

### 3.2 एडवाइस टाइप्स

1. **बिफोर**: एक जॉइन पॉइंट से पहले एक्सेक्यूट होता है
   ```java
   @Before("execution(* com.example.service.*.*(..))")
   public void beforeAdvice() {
       System.out.println("मेथड एक्सेक्यूशन से पहले");
   }
   ```

2. **आफ्टररिटर्निंग**: एक जॉइन पॉइंट के सामान्य रूप से पूरा होने के बाद एक्सेक्यूट होता है
   ```java
   @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", returning = "result")
   public void afterReturningAdvice(Object result) {
       System.out.println("मेथड ने रिटर्न किया: " + result);
   }
   ```

3. **आफ्टरथ्रोइंग**: एक्सेक्यूट होता है यदि कोई मेथड एक्सेप्शन थ्रो करके एक्जिट करती है
   ```java
   @AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", throwing = "ex")
   public void afterThrowingAdvice(Exception ex) {
       System.out.println("एक्सेप्शन थ्रो हुआ: " + ex.getMessage());
   }
   ```

4. **आफ्टर (फाइनली)**: आउटकम की परवाह किए बिना एक जॉइन पॉइंट के बाद एक्सेक्यूट होता है
   ```java
   @After("execution(* com.example.service.*.*(..))")
   public void afterAdvice() {
       System.out.println("मेथड एक्सेक्यूशन के बाद (फाइनली)");
   }
   ```

5. **अराउंड**: एक जॉइन पॉइंट को रैप करता है, सबसे शक्तिशाली एडवाइस
   ```java
   @Around("execution(* com.example.service.*.*(..))")
   public Object aroundAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
       System.out.println("प्रोसीडिंग से पहले");
       Object result = joinPoint.proceed();
       System.out.println("प्रोसीडिंग के बाद");
       return result;
   }
   ```

### 3.3 पॉइंटकट एक्सप्रेशन्स

पॉइंटकट्स परिभाषित करते हैं कि एडवाइस कहाँ लागू की जानी चाहिए एक्सप्रेशन्स का उपयोग करके:

- **एक्सेक्यूशन**: मेथड एक्सेक्यूशन से मेल खाता है
  ```java
  @Pointcut("execution(public * com.example.service.*.*(..))")
  public void serviceMethods() {}
  ```

- **विदिन**: कुछ प्रकार के भीतर सभी जॉइन पॉइंट्स से मेल खाता है
  ```java
  @Pointcut("within(com.example.service..*)")
  public void inServiceLayer() {}
  ```

- **दिस**: दिए गए प्रकार के इंस्टेंस वाले बीन्स से मेल खाता है
- **टार्गेट**: दिए गए प्रकार के असाइन करने योग्य बीन्स से मेल खाता है
- **आर्ग्स**: विशिष्ट आर्ग्युमेंट टाइप्स वाली मेथड्स से मेल खाता है
- **@annotation**: विशिष्ट एनोटेशन वाली मेथड्स से मेल खाता है

### 3.4 पॉइंटकट्स को कॉम्बाइन करना

पॉइंटकट्स को लॉजिकल ऑपरेटर्स का उपयोग करके कॉम्बाइन किया जा सकता है:
```java
@Pointcut("execution(* com.example.service.*.*(..)) && !execution(* com.example.service.UserService.*(..))")
public void serviceMethodsExceptUserService() {}
```

## 4. इम्प्लीमेंटेशन स्टेप्स

### 4.1 सेटअप

1. स्प्रिंग AOP डिपेंडेंसी एड करें (यदि स्प्रिंग बूट का उपयोग नहीं कर रहे हैं):
   ```xml
   <dependency>
       <groupId>org.springframework</groupId>
       <artifactId>spring-aop</artifactId>
       <version>${spring.version}</version>
   </dependency>
   <dependency>
       <groupId>org.aspectj</groupId>
       <artifactId>aspectjweaver</artifactId>
       <version>${aspectj.version}</version>
   </dependency>
   ```

2. स्प्रिंग बूट के लिए, बस `spring-boot-starter-aop` इन्क्लूड करें:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-aop</artifactId>
   </dependency>
   ```

3. अपनी कॉन्फ़िगरेशन में AOP को एनेबल करें:
   ```java
   @Configuration
   @EnableAspectJAutoProxy
   public class AppConfig {
   }
   ```

### 4.2 एस्पेक्ट्स बनाना

```java
@Aspect
@Component
public class LoggingAspect {
    
    private final Logger logger = LoggerFactory.getLogger(this.getClass());
    
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        logger.info("प्रवेश कर रहा है: {}.{}() आर्ग्युमेंट्स के साथ = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            Arrays.toString(joinPoint.getArgs()));
    }
    
    @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", 
                   returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {
        logger.info("बाहर निकल रहा है: {}.{}() रिजल्ट के साथ = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            result);
    }
    
    @Around("@annotation(com.example.annotations.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object proceed = joinPoint.proceed();
        long executionTime = System.currentTimeMillis() - start;
        logger.info("{} {} ms में एक्सेक्यूट हुआ", 
            joinPoint.getSignature(), executionTime);
        return proceed;
    }
}
```

### 4.3 कस्टम एनोटेशन्स

विशिष्ट AOP व्यवहार के लिए मेथड्स को मार्क करने के लिए कस्टम एनोटेशन्स बनाएं:

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

फिर इसे मेथड्स पर उपयोग करें:
```java
@Service
public class UserService {
    
    @LogExecutionTime
    public User getUser(Long id) {
        // इम्प्लीमेंटेशन
    }
}
```

## 5. एडवांस्ड टॉपिक्स

### 5.1 एस्पेक्ट ऑर्डरिंग

`@Order` के साथ एस्पेक्ट एक्सेक्यूशन के ऑर्डर को कंट्रोल करें:
```java
@Aspect
@Component
@Order(1)
public class LoggingAspect {
    // ...
}

@Aspect
@Component
@Order(2)
public class ValidationAspect {
    // ...
}
```

### 5.2 मेथड इनफॉर्मेशन तक पहुँच

एडवाइस मेथड्स में, आप एक्सेस कर सकते हैं:
- `JoinPoint` (बिफोर, आफ्टर, आफ्टररिटर्निंग, आफ्टरथ्रोइंग के लिए)
- `ProceedingJoinPoint` (अराउंड के लिए)

```java
@Before("execution(* com.example.service.*.*(..))")
public void beforeAdvice(JoinPoint joinPoint) {
    String methodName = joinPoint.getSignature().getName();
    String className = joinPoint.getTarget().getClass().getName();
    Object[] args = joinPoint.getArgs();
    // ...
}
```

### 5.3 एक्सेप्शन हैंडलिंग

```java
@AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", 
               throwing = "ex")
public void handleException(JoinPoint joinPoint, Exception ex) {
    // एक्सेप्शन लॉग करें, अलर्ट भेजें, आदि
}
```

### 5.4 प्रॉक्सीइंग मैकेनिज्म्स

स्प्रिंग AOP दो प्रकार के प्रॉक्सीज का उपयोग करता है:
- **JDK डायनामिक प्रॉक्सी**: इंटरफेस के लिए डिफॉल्ट
- **CGLIB प्रॉक्सी**: जब कोई इंटरफेस उपलब्ध नहीं होता है तो उपयोग किया जाता है (`proxyTargetClass=true` के साथ फोर्स किया जा सकता है)

## 6. बेस्ट प्रैक्टिसेज

1. **एस्पेक्ट्स को फोकस्ड रखें**: प्रत्येक एस्पेक्ट को एक विशिष्ट क्रॉस-कटिंग कंसर्न को हैंडल करना चाहिए
2. **मीनिंगफुल पॉइंटकट नेम्स का उपयोग करें**: कोड को अधिक रीडेबल बनाता है
3. **एस्पेक्ट्स में महंगे ऑपरेशन्स से बचें**: वे प्रत्येक मैच किए गए जॉइन पॉइंट के लिए रन करते हैं
4. **अराउंड एडवाइस के साथ सावधान रहें**: जानबूझकर एक्सेक्यूशन को रोकने के अलावा हमेशा `proceed()` को कॉल करें
5. **एस्पेक्ट्स को अच्छी तरह से टेस्ट करें**: वे आपकी एप्लिकेशन के कई हिस्सों को प्रभावित करते हैं
6. **एस्पेक्ट्स को डॉक्युमेंट करें**: खासकर यदि वे व्यवहार को महत्वपूर्ण रूप से मॉडिफाई करते हैं
7. **परफॉर्मेंस पर विचार करें**: कॉम्प्लेक्स पॉइंटकट्स या कई एस्पेक्ट्स परफॉर्मेंस को प्रभावित कर सकते हैं

## 7. कॉमन यूज केसेज

1. **लॉगिंग**: मेथड एंट्री/एग्जिट, पैरामीटर्स, रिटर्न वैल्यूज
2. **परफॉर्मेंस मॉनिटरिंग**: एक्सेक्यूशन टाइम मापना
3. **ट्रांजैक्शन मैनेजमेंट**: (हालांकि आमतौर पर स्प्रिंग के `@Transactional` द्वारा हैंडल किया जाता है)
4. **सिक्योरिटी**: अथॉराइजेशन चेक्स
5. **वैलिडेशन**: पैरामीटर वैलिडेशन
6. **एरर हैंडलिंग**: कंसिस्टेंट एक्सेप्शन हैंडलिंग
7. **कैशिंग**: मेथड रिजल्ट कैशिंग
8. **ऑडिटिंग**: ट्रैक करें कि किसने कब और क्या कॉल किया

## 8. लिमिटेशन्स

1. केवल स्प्रिंग-मैनेज्ड बीन्स के साथ काम करता है
2. केवल मेथड एक्सेक्यूशन जॉइन पॉइंट्स सपोर्टेड हैं
3. फाइनल क्लासेज या मेथड्स को एडवाइस नहीं कर सकता
4. सेल्फ-इनवोकेशन (एक क्लास के भीतर मेथड उसी क्लास की दूसरी मेथड को कॉल करना) प्रॉक्सी को बायपास करता है
5. AspectJ की तुलना में सीमित पॉइंटकट एक्सप्रेशन्स

## 9. ट्रबलशूटिंग

**इश्यू**: एडवाइस एक्सेक्यूट नहीं हो रही है
- चेक करें कि क्या बीन स्प्रिंग-मैनेज्ड है
- वेरीफाई करें कि पॉइंटकट एक्सप्रेशन इंटेंडेड मेथड्स से मेल खाता है
- सुनिश्चित करें कि `@EnableAspectJAutoProxy` मौजूद है

**इश्यू**: अराउंड एडवाइस प्रोसीड नहीं कर रही है
- सुनिश्चित करें कि `ProceedingJoinPoint` पर `proceed()` को कॉल करें

**इश्यू**: इनकरेक्ट प्रॉक्सी टाइप
- CGLIB को फोर्स करने के लिए `@EnableAspectJAutoProxy(proxyTargetClass=true)` का उपयोग करें

## 10. कंक्लूजन

स्प्रिंग AOP आपकी एप्लिकेशन में क्रॉस-कटिंग कंसर्न्स को लागू करने का एक शक्तिशाली yet सरल तरीका प्रदान करता है। हालांकि इसमें पूर्ण AspectJ की तुलना में कुछ सीमाएँ हैं, यह स्प्रिंग के साथ सीमलेसली इंटीग्रेट होता है और अधिकांश कॉमन यूज केसेज को कवर करता है। इस गाइड में बताए गए पैटर्न और बेस्ट प्रैक्टिसेज का पालन करके, आप क्रॉस-कटिंग कंसर्न्स को प्रभावी ढंग से मॉड्यूलराइज कर सकते हैं और अपने बिजनेस लॉजिक को क्लीन और फोकस्ड रख सकते हैं।

---

हालांकि स्प्रिंग AOP, AspectJ की वीविंग कैपेबिलिटीज का उपयोग नहीं करता है (इसके बजाय यह प्रॉक्सी-बेस्ड AOP का उपयोग करता है), फिर भी आपको कई महत्वपूर्ण कारणों से `aspectjweaver` डिपेंडेंसी की आवश्यकता होती है:

### 1. **AspectJ एनोटेशन सपोर्ट**
स्प्रिंग AOP, AspectJ के **एनोटेशन्स** (जैसे `@Aspect`, `@Pointcut`, `@Before`, `@After`, आदि) का उपयोग एस्पेक्ट्स और एडवाइसेज को परिभाषित करने के लिए करता है। ये एनोटेशन्स `aspectjweaver` लाइब्रेरी से आते हैं।

- इसके बिना, आपको `@Aspect` या अन्य AOP एनोटेशन्स का उपयोग करते समय कम्पाइलेशन एरर्स मिलेंगे।

### 2. **पॉइंटकट एक्सप्रेशन लैंग्वेज**
स्प्रिंग AOP, AspectJ की **पॉइंटकट एक्सप्रेशन लैंग्वेज** उधार लेता है ताकि यह परिभाषित किया जा सके कि एडवाइस कहाँ लागू की जानी चाहिए (जैसे, `execution(* com.example.service.*.*(..))`).

- `aspectjweaver` इन एक्सप्रेशन्स के लिए पार्सर और मैचिंग लॉजिक प्रदान करता है।

### 3. **अतिरिक्त जॉइन पॉइंट्स के लिए सपोर्ट (सीमित)**
जबकि स्प्रिंग AOP केवल **मेथड एक्सेक्यूशन** जॉइन पॉइंट्स को सपोर्ट करता है (AspectJ के विपरीत, जो कंस्ट्रक्टर्स, फील्ड एक्सेस, आदि को सपोर्ट करता है), फिर भी यह AspectJ की अंडरलाइंग पॉइंटकट मैचिंग मैकेनिज्म पर निर्भर करता है।

### 4. **लोड-टाइम वीविंग (ऑप्शनल)**
यदि आप स्प्रिंग AOP के साथ **लोड-टाइम वीविंग (LTW)** का उपयोग करने का निर्णय लेते हैं (जो दुर्लभ है लेकिन संभव है), तो `aspectjweaver` आवश्यक है। LTW प्रॉक्सीज का उपयोग करने के बजाय क्लास-लोडिंग टाइम पर एस्पेक्ट्स को वीव करने की अनुमति देता है।

```java
@EnableLoadTimeWeaving
public class AppConfig { ... }
```

### 5. **@EnableAspectJAutoProxy के साथ कम्पैटिबिलिटी**
जब आप `@EnableAspectJAutoProxy` का उपयोग करते हैं, स्प्रिंग आंतरिक रूप से AOP एनोटेशन्स को प्रोसेस करने के लिए AspectJ के इन्फ्रास्ट्रक्चर का उपयोग करता है, भले ही यह पूर्ण AspectJ वीविंग नहीं करता है।

---

### **क्या आपको हमेशा इसकी आवश्यकता होती है?**
- **यदि स्प्रिंग बूट (`spring-boot-starter-aop`) का उपयोग कर रहे हैं**: नहीं, क्योंकि यह ट्रांजिटिवली `aspectjweaver` को इन्क्लूड करता है।
- **यदि प्लेन स्प्रिंग AOP का उपयोग कर रहे हैं**: हाँ, आपको इसे एक्सप्लिसिटली इन्क्लूड करना होगा।

### **अल्टरनेटिव्स?**
- यदि आप **पूर्ण AspectJ** (कम्पाइल-टाइम या लोड-टाइम वीविंग) का उपयोग कर रहे थे, तो आपको `aspectjrt` और `aspectjtools` की भी आवश्यकता होगी।
- लेकिन **स्प्रिंग AOP** के लिए, केवल `aspectjweaver` पर्याप्त है।

### **कंक्लूजन**
स्प्रिंग AOP **प्रॉक्सी-बेस्ड** है, लेकिन यह **AspectJ के एनोटेशन्स और पॉइंटकट सिंटैक्स को रीयूज करता है**, यही कारण है कि `aspectjweaver` आवश्यक है। यह स्प्रिंग के प्रॉक्सी एप्रोच और AspectJ के अधिक शक्तिशाली AOP मॉडल के बीच की खाई को पाटता है।