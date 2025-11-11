---
audio: false
generated: true
lang: ar
layout: post
title: دليل إلى إيه أو بي الربيع
translated: true
type: note
---

## 1. مقدمة إلى Spring AOP

Spring AOP (البرمجة الموجهة للجانب) هو مكون رئيسي في إطار Spring يوفر طريقة لتنفيذ الاهتمامات المتقاطعة (مثل التسجيل، الأمان، إدارة المعاملات) بشكل منفصل عن منطق الأعمال.

### المفاهيم الأساسية:
- **الاهتمامات المتقاطعة**: وظائف تمتد عبر طبقات متعددة (التسجيل، الأمان، إلخ.)
- **الجانب**: نمطية لاهتمام يقطع عبر فئات متعددة
- **نقطة الاشتراك**: نقطة أثناء تنفيذ البرنامج (تنفيذ الأسلوب، معالجة الاستثناء، إلخ.)
- **النصيحة**: الإجراء الذي يتخذه جانب عند نقطة اشتراك معينة
- **تعبير النقطة**: مسند يطابق نقاط الاشتراك
- **النسج**: ربط الجوانب مع أنواع التطبيقات الأخرى لإنشاء كائن موجه

## 2. Spring AOP مقابل AspectJ

| الميزة               | Spring AOP | AspectJ |
|-----------------------|-----------|---------|
| التنفيذ               | الوكالة أثناء وقت التشغيل | النسج أثناء وقت الترجمة/وقت التحميل |
| الأداء                | أبطأ | أسرع |
| نقاط الاشتراك المدعومة | تنفيذ الأسلوب فقط | الكل (الأسلوب، المُنشئ، الوصول إلى الحقل، إلخ.) |
| التعقيد               | أبسط | أكثر تعقيدًا |
| التبعية               | لا توجد تبعيات إضافية | يتطلب مترجم/نساج AspectJ |

## 3. مكونات AOP الأساسية

### 3.1 الجوانب
فئة معلمة بـ `@Aspect` تحتوي على نصائح وتعبيرات نقطة.

```java
@Aspect
@Component
public class LoggingAspect {
    // سيتم وضع النصائح وتعبيرات النقطة هنا
}
```

### 3.2 أنواع النصائح

1. **Before**: ينفذ قبل نقطة اشتراك
   ```java
   @Before("execution(* com.example.service.*.*(..))")
   public void beforeAdvice() {
       System.out.println("Before method execution");
   }
   ```

2. **AfterReturning**: ينفذ بعد اكتمال نقطة اشتراك بشكل طبيعي
   ```java
   @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", returning = "result")
   public void afterReturningAdvice(Object result) {
       System.out.println("Method returned: " + result);
   }
   ```

3. **AfterThrowing**: ينفذ إذا خرج أسلوب برمي استثناء
   ```java
   @AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", throwing = "ex")
   public void afterThrowingAdvice(Exception ex) {
       System.out.println("Exception thrown: " + ex.getMessage());
   }
   ```

4. **After (Finally)**: ينفذ بعد نقطة اشتراك بغض النظر عن النتيجة
   ```java
   @After("execution(* com.example.service.*.*(..))")
   public void afterAdvice() {
       System.out.println("After method execution (finally)");
   }
   ```

5. **Around**: يلف نقطة اشتراك، أقوى نصيحة
   ```java
   @Around("execution(* com.example.service.*.*(..))")
   public Object aroundAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
       System.out.println("Before proceeding");
       Object result = joinPoint.proceed();
       System.out.println("After proceeding");
       return result;
   }
   ```

### 3.3 تعبيرات النقطة

تحدد تعبيرات النقطة مكان تطبيق النصيحة باستخدام التعبيرات:

- **Execution**: يطابق تنفيذ الأسلوب
  ```java
  @Pointcut("execution(public * com.example.service.*.*(..))")
  public void serviceMethods() {}
  ```

- **Within**: يطابق جميع نقاط الاشتراك داخل أنواع معينة
  ```java
  @Pointcut("within(com.example.service..*)")
  public void inServiceLayer() {}
  ```

- **this**: يطابق beans التي تكون نسخًا من نوع معين
- **target**: يطابق beans التي يمكن تعيينها لنوع معين
- **args**: يطابق الأساليب بأنواع وسيطات محددة
- **@annotation**: يطابق الأساليب بتعليقات توضيحية محددة

### 3.4 دمج تعبيرات النقطة

يمكن دمج تعبيرات النقطة باستخدام العوامل المنطقية:
```java
@Pointcut("execution(* com.example.service.*.*(..)) && !execution(* com.example.service.UserService.*(..))")
public void serviceMethodsExceptUserService() {}
```

## 4. خطوات التنفيذ

### 4.1 الإعداد

1. إضافة تبعية Spring AOP (إذا لم تكن تستخدم Spring Boot):
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

2. بالنسبة لـ Spring Boot، ما عليك سوى تضمين `spring-boot-starter-aop`:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-aop</artifactId>
   </dependency>
   ```

3. تمكين AOP في التهيئة الخاصة بك:
   ```java
   @Configuration
   @EnableAspectJAutoProxy
   public class AppConfig {
   }
   ```

### 4.2 إنشاء الجوانب

```java
@Aspect
@Component
public class LoggingAspect {
    
    private final Logger logger = LoggerFactory.getLogger(this.getClass());
    
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        logger.info("Entering: {}.{}() with arguments = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            Arrays.toString(joinPoint.getArgs()));
    }
    
    @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", 
                   returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {
        logger.info("Exiting: {}.{}() with result = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            result);
    }
    
    @Around("@annotation(com.example.annotations.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object proceed = joinPoint.proceed();
        long executionTime = System.currentTimeMillis() - start;
        logger.info("{} executed in {} ms", 
            joinPoint.getSignature(), executionTime);
        return proceed;
    }
}
```

### 4.3 التعليقات التوضيحية المخصصة

إنشاء تعليقات توضيحية مخصصة لوضع علامة على الأساليب لسلوك AOP محدد:

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

ثم استخدمها على الأساليب:
```java
@Service
public class UserService {
    
    @LogExecutionTime
    public User getUser(Long id) {
        // implementation
    }
}
```

## 5. مواضيع متقدمة

### 5.1 ترتيب الجوانب

التحكم في ترتيب تنفيذ الجوانب باستخدام `@Order`:
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

### 5.2 الوصول إلى معلومات الأسلوب

في أساليب النصيحة، يمكنك الوصول إلى:
- `JoinPoint` (لـ Before، After، AfterReturning، AfterThrowing)
- `ProceedingJoinPoint` (لـ Around)

```java
@Before("execution(* com.example.service.*.*(..))")
public void beforeAdvice(JoinPoint joinPoint) {
    String methodName = joinPoint.getSignature().getName();
    String className = joinPoint.getTarget().getClass().getName();
    Object[] args = joinPoint.getArgs();
    // ...
}
```

### 5.3 معالجة الاستثناءات

```java
@AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", 
               throwing = "ex")
public void handleException(JoinPoint joinPoint, Exception ex) {
    // تسجيل الاستثناء، إرسال تنبيه، إلخ.
}
```

### 5.4 آليات الوكالة

يستخدم Spring AOP نوعين من الوكلاء:
- **JDK Dynamic Proxy**: الافتراضي للواجهات
- **CGLIB Proxy**: يستخدم عندما لا تكون هناك واجهة متاحة (يمكن فرضه بـ `proxyTargetClass=true`)

## 6. أفضل الممارسات

1. **حافظ على تركيز الجوانب**: يجب أن يعالج كل جانب اهتمامًا متقاطعًا محددًا واحدًا
2. **استخدم أسماء تعبيرات نقطة ذات معنى**: يجعل الكود أكثر قابلية للقراءة
3. **تجنب العمليات المكلفة في الجوانب**: تعمل لكل نقطة اشتراك مطابقة
4. **كن حذرًا مع نصيحة Around**: استدع دائمًا `proceed()` ما لم تكن تمنع التنفيذ عمدًا
5. **اختبر الجوانب بدقة**: تؤثر على أجزاء متعددة من تطبيقك
6. **وثق الجوانب**: خاصة إذا كانت تعدل السلوك بشكل كبير
7. **ضع في الاعتبار الأداء**: تعبيرات النقطة المعقدة أو الجوانب الكثيرة يمكن أن تؤثر على الأداء

## 7. حالات الاستخدام الشائعة

1. **التسجيل**: دخول/خروج الأسلوب، المعاملات، قيم الإرجاع
2. **مراقبة الأداء**: قياس وقت التنفيذ
3. **إدارة المعاملات**: (على الرغم من معالجتها عادةً بواسطة `@Transactional` في Spring)
4. **الأمان**: فحوصات التفويض
5. **التحقق من الصحة**: التحقق من صحة المعاملات
6. **معالجة الأخطاء**: معالجة استثناءات متسقة
7. **التخزين المؤقت**: تخزين نتائج الأسلوب مؤقتًا
8. **التدقيق**: تتبع من استدعى ماذا ومتى

## 8. القيود

1. يعمل فقط مع beans المدارة بواسطة Spring
2. يتم دعم نقاط اشتراك تنفيذ الأسلوب فقط
3. لا يمكن توجيه الفئات أو الأساليب النهائية
4. النداء الذاتي (أسلوب داخل فئة يستدعي أسلوبًا آخر من نفس الفئة) يتجاوز الوكيل
5. تعبيرات نقطة محدودة مقارنة بـ AspectJ

## 9. استكشاف الأخطاء وإصلاحها

**المشكلة**: النصيحة لا تنفذ
- تحقق مما إذا كان bean مدارًا بواسطة Spring
- تحقق من تطابق تعبير النقطة مع الأساليب المقصودة
- تأكد من وجود `@EnableAspectJAutoProxy`

**المشكلة**: نصيحة Around لا تستمر
- تأكد من استدعاء `proceed()` على `ProceedingJoinPoint`

**المشكلة**: نوع الوكيل غير صحيح
- استخدم `@EnableAspectJAutoProxy(proxyTargetClass=true)` لإجبار CGLIB

## 10. الخلاصة

يوفر Spring AOP طريقة قوية لكن بسيطة لتنفيذ الاهتمامات المتقاطعة في تطبيقك. بينما لديه بعض القيود مقارنة بـ AspectJ الكامل، فإنه يتكامل بسلاسة مع Spring ويغطي معظم حالات الاستخدام الشائعة. باتباع الأنماط وأفضل الممارسات الموضحة في هذا الدليل، يمكنك نمذجة الاهتمامات المتقاطعة بشكل فعال والحفاظ على منطق أعمالك نظيفًا ومركزًا.

---

على الرغم من أن Spring AOP لا يستخدم إمكانيات النسج في AspectJ (بدلاً من ذلك يستخدم AOP القائم على الوكيل)، لا تزال بحاجة إلى تبعية `aspectjweaver` لعدة أسباب مهمة:

### 1. **دعم تعليقات AspectJ التوضيحية**
يستخدم Spring AOP **التعليقات التوضيحية** الخاصة بـ AspectJ (مثل `@Aspect`، `@Pointcut`، `@Before`، `@After`، إلخ.) لتعريف الجوانب والنصائح. تأتي هذه التعليقات التوضيحية من مكتبة `aspectjweaver`.

- بدونها، ستحصل على أخطاء ترجمة عند استخدام `@Aspect` أو تعليقات AOP أخرى.

### 2. **لغة تعبير النقطة**
يقترض Spring AOP **لغة تعبير النقطة** الخاصة بـ AspectJ لتعريف مكان تطبيق النصيحة (مثل `execution(* com.example.service.*.*(..))`).

- يوفر `aspectjweaver` المحلل ومنطق المطابقة لهذه التعبيرات.

### 3. **دعم نقاط اشتراك إضافية (محدود)**
بينما يدعم Spring AOP فقط نقاط اشتراك **تنفيذ الأسلوب** (على عكس AspectJ، الذي يدعم المنشئين، الوصول إلى الحقل، إلخ.)، فإنه لا يزال يعتمد على آلية مطابقة النقطة الأساسية في AspectJ.

### 4. **النسج أثناء وقت التحميل (اختياري)**
إذا قررت استخدام **النسج أثناء وقت التحميل (LTW)** مع Spring AOP (وهو نادر لكن ممكن)، فإن `aspectjweaver` مطلوب. يسمح LTW بنسج الجوانب أثناء وقت تحميل الفصل بدلاً من استخدام الوكلاء.

```java
@EnableLoadTimeWeaving
public class AppConfig { ... }
```

### 5. **التوافق مع @EnableAspectJAutoProxy**
عندما تستخدم `@EnableAspectJAutoProxy`، يستخدم Spring داخليًا البنية التحتية لـ AspectJ لمعالجة تعليقات AOP التوضيحية، حتى لو لم يقم بنسج AspectJ كامل.

---

### **هل تحتاجه دائمًا؟**
- **إذا كنت تستخدم Spring Boot (`spring-boot-starter-aop`)**: لا، لأنه يتضمن `aspectjweaver` بشكل انتقالي.
- **إذا كنت تستخدم Spring AOP عادي**: نعم، يجب عليك تضمينه بشكل صريح.

### **البدائل؟**
- إذا كنت تستخدم **AspectJ كامل** (نسج أثناء وقت الترجمة أو وقت التحميل)، فستحتاج إلى `aspectjrt` و `aspectjtools` أيضًا.
- لكن بالنسبة لـ **Spring AOP**، فإن `aspectjweaver` وحده كافٍ.

### **الخلاصة**
Spring AOP **قائم على الوكيل**، لكنه **يعيد استخدام تعليقات AspectJ التوضيحية وبناء جملة النقطة**، ولهذا السبب `aspectjweaver` مطلوب. يعمل كجسر بين نهج الوكيل في Spring والنموذج الأقوى لـ AOP في AspectJ.