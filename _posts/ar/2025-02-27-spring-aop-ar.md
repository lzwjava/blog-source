---
audio: false
generated: true
lang: ar
layout: post
title: Spring AOP (برمجة التوجه إلى الجوانب)
translated: true
---

Spring AOP (Aspect-Oriented Programming) هو ميزة قوية في إطار عمل Spring التي تسمح لك بتقسيم القضايا المتقاطعة مثل التسجيل، الأمن، أو إدارة المعاملات. سأرشدك عبر أساسيات استخدام APIs Spring AOP باستخدام نهج عملي.

### 1. **فهم المفاهيم الرئيسية**
قبل الغوص في APIs، إليك ما تحتاج إلى معرفته:
- **Aspect**: وحدة تحوي قضية متقاطعة (مثل التسجيل).
- **Advice**: الإجراء الذي يتخذه الجانب في نقطة معينة (مثل "قبل" أو "بعد" تنفيذ طريقة).
- **Pointcut**: شرط يحدد أين يجب تطبيق النصيحة (مثل طرق أو فئات محددة).
- **Join Point**: نقطة في تنفيذ البرنامج حيث يمكن تطبيق الجانب (مثل استدعاء طريقة).

Spring AOP مبني على الوكالة، مما يعني أنه يلف الكائنات الخاصة بك بالوكالات لتطبيق جوانبها.

### 2. **إعداد مشروعك**
لاستخدام Spring AOP، ستحتاج إلى:
- مشروع Spring Boot (أو مشروع Spring مع اعتمادات AOP).
- أضف الاعتماد في `pom.xml` إذا كنت تستخدم Maven:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-aop</artifactId>
  </dependency>
  ```
- تمكين AOP في تكوينك (عادة ما يكون تلقائيًا مع Spring Boot، ولكن يمكنك تمكينه بشكل صريح باستخدام `@EnableAspectJAutoProxy`).

### 3. **إنشاء جانب**
هكذا يمكنك تعريف جانب باستخدام APIs Spring AOP:

#### مثال: جانب التسجيل
```java
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class LoggingAspect {

    // نصيحة قبل: يعمل قبل تنفيذ الطريقة
    @Before("execution(* com.example.myapp.service.*.*(..))")
    public void logBeforeMethod() {
        System.out.println("سيتم تنفيذ طريقة في حزمة الخدمة قريبًا");
    }

    // نصيحة بعد: يعمل بعد تنفيذ الطريقة
    @After("execution(* com.example.myapp.service.*.*(..))")
    public void logAfterMethod() {
        System.out.println("انتهى تنفيذ طريقة في حزمة الخدمة");
    }
}
```
- `@Aspect`: يحدد هذه الفئة كجانب.
- `@Component`: يسجلها ككيان Spring.
- `execution(* com.example.myapp.service.*.*(..))`: تعبير نقطة يحدد "أي طريقة في أي فئة تحت حزمة `service` مع أي نوع عودة و أي متغيرات."

### 4. **أنواع النصائح الشائعة**
يقدم Spring AOP عدة أنواع من نصائح التسمية:
- `@Before`: يعمل قبل تنفيذ الطريقة المتطابقة.
- `@After`: يعمل بعد (بغض النظر عن النجاح أو الفشل).
- `@AfterReturning`: يعمل بعد عودة الطريقة بنجاح.
- `@AfterThrowing`: يعمل إذا ألقت الطريقة استثناء.
- `@Around`: يلف الطريقة، مما يسمح لك بتحكم في التنفيذ (أقوى).

#### مثال: نصيحة حول
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
        Object result = joinPoint.proceed(); // تنفيذ الطريقة
        long end = System.currentTimeMillis();
        System.out.println("وقت التنفيذ: " + (end - start) + "ms");
        return result;
    }
}
```
- `ProceedingJoinPoint`: يمثل الطريقة التي يتم اعتراضها.
- `proceed()`: يستدعي الطريقة الأصلية.

### 5. **عبارات نقطة**
تعريف النقاط حيث يتم تطبيق النصيحة. الصيغة الشائعة:
- `execution(modifiers? return-type declaring-type? method-name(params) throws?)`
  - مثال: `execution(public String com.example.myapp.service.MyService.get*(..))`
    - يتطابق مع الطرق العامة التي تبدأ بـ "get" في `MyService` والتي تعود إلى `String`.

يمكنك أيضًا دمج النقاط:
```java
@Pointcut("execution(* com.example.myapp.service.*.*(..))")
public void serviceMethods() {}

@Before("serviceMethods()")
public void logBeforeService() {
    System.out.println("تم استدعاء طريقة الخدمة");
}
```

### 6. **الوصول إلى تفاصيل الطريقة**
يمكنك الوصول إلى متغيرات الطريقة، التوقيعات، أو البيانات:
```java
@Before("execution(* com.example.myapp.service.*.*(..))")
public void logMethodDetails(JoinPoint joinPoint) {
    String methodName = joinPoint.getSignature().getName();
    Object[] args = joinPoint.getArgs();
    System.out.println("تم استدعاء طريقة " + methodName + " مع " + args.length + " متغيرات");
}
```

### 7. **العمل والتجربة**
- إنشاء فئة خدمة (مثل `MyService`) مع بعض الطرق.
- تشغيل تطبيق Spring الخاص بك.
- سيتم تطبيق الجانب تلقائيًا على الطرق المتطابقة.

#### مثال خدمة:
```java
@Service
public class MyService {
    public String sayHello(String name) {
        return "مرحبًا، " + name;
    }
}
```

عندما تستدعي `myService.sayHello("Alice")`، سيتم تنشيط جوانب التسجيل أو الأداء.

### نصائح
- **الأداء**: يضيف AOP عبءًا بسبب الوكالات، لذا استخدمه بحكمة.
- **المنطقة**: يعمل Spring AOP على الكائنات التي يديرها Spring فقط. بالنسبة للأشياء التي لا تديرها Spring، فكر في AspectJ (بديل أقوى).
- **التشخيص**: تمكين تسجيل التشخيص لـ `org.springframework.aop` لرؤية كيفية تطبيق الوكالات.

إذا كان لديك حالة استخدام محددة أو تحتاج إلى مساعدة في تنفيذ معين، أخبرني وسأعدل التفسير بشكل أكبر!