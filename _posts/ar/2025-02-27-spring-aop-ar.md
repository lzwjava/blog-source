---
audio: false
generated: true
lang: ar
layout: post
title: برمجة النواحي في الربيع
translated: true
type: note
---

Spring AOP (البرمجة الموجهة نحو الجوانب) هي ميزة قوية في إطار عمل Spring تتيح لك نمطية الاهتمامات المتقاطعة مثل التسجيل والأمان أو إدارة المعاملات. سأرشدك خلال أساسيات استخدام واجهات برمجة تطبيقات Spring AOP بطريقة عملية.

### 1. **فهم المفاهيم الأساسية**
قبل الخوض في واجهات برمجة التطبيقات، إليك ما تحتاج إلى معرفته:
- **الجانب (Aspect)**: وحدة نمطية تغلف اهتمامًا متقاطعًا (مثل التسجيل).
- **النصيحة (Advice)**: الإجراء الذي يتخذه الجانب عند نقطة معينة (مثل "قبل" أو "بعد" تشغيل طريقة).
- **تعبير نقطة القطع (Pointcut)**: مسند يحدد مكان تطبيق النصيحة (مثل طرق أو فئات محددة).
- **نقطة الربط (Join Point)**: نقطة في تنفيذ البرنامج حيث يمكن تطبيق جانب (مثل استدعاء طريقة).

يعتمد Spring AOP على الوكيل (proxy)، مما يعني أنه يلف حبوبك (beans) بوكلاء لتطبيق الجوانب.

### 2. **إعداد مشروعك**
لاستخدام Spring AOP، ستحتاج إلى:
- مشروع Spring Boot (أو مشروع Spring مع تبعيات AOP).
- أضف التبعية في ملف `pom.xml` الخاص بك إذا كنت تستخدم Maven:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-aop</artifactId>
  </dependency>
  ```
- قم بتمكين AOP في التهيئة الخاصة بك (عادةً ما يكون تلقائيًا مع Spring Boot، ولكن يمكنك تمكينه صراحةً باستخدام `@EnableAspectJAutoProxy`).

### 3. **إنشاء جانب**
إليك كيفية تعريف جانب باستخدام واجهات برمجة تطبيقات Spring AOP:

#### مثال: جانب التسجيل
```java
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class LoggingAspect {

    // نصيحة Before: تعمل قبل تنفيذ الطريقة
    @Before("execution(* com.example.myapp.service.*.*(..))")
    public void logBeforeMethod() {
        System.out.println("A method in the service package is about to be executed");
    }

    // نصيحة After: تعمل بعد تنفيذ الطريقة
    @After("execution(* com.example.myapp.service.*.*(..))")
    public void logAfterMethod() {
        System.out.println("A method in the service package has finished executing");
    }
}
```
- `@Aspect`: يحدد هذا الفصل على أنه جانب.
- `@Component`: يسجله كـ Spring bean.
- `execution(* com.example.myapp.service.*.*(..))`: تعبير نقطة قطع يعني "أي طريقة في أي فصل ضمن حزمة `service` مع أي نوع إرجاع وأي معاملات."

### 4. **أنواع النصائح الشائعة**
يدعم Spring AOP عدة تعريفات للنصائح:
- `@Before`: تعمل قبل تنفيذ الطريقة المطابقة.
- `@After`: تعمل بعد التنفيذ (بغض النظر عن النجاح أو الفشل).
- `@AfterReturning`: تعمل بعد إرجاع الطريقة بنجاح.
- `@AfterThrowing`: تعمل إذا ألقت الطريقة استثناءً.
- `@Around`: تغلف الطريقة، مما يسمح لك بالتحكم في التنفيذ (الأقوى).

#### مثال: نصيحة Around
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
        Object result = joinPoint.proceed(); // تنفيذ الطريقة الأصلية
        long end = System.currentTimeMillis();
        System.out.println("Execution time: " + (end - start) + "ms");
        return result;
    }
}
```
- `ProceedingJoinPoint`: يمثل الطريقة التي يتم اعتراضها.
- `proceed()`: يستدعي الطريقة الأصلية.

### 5. **تعبيرات نقطة القطع**
تحدد نقاط القطع مكان تطبيق النصيحة. الصيغة الشائعة:
- `execution(modifiers? return-type declaring-type? method-name(params) throws?)`
  - مثال: `execution(public String com.example.myapp.service.MyService.get*(..))`
    - تطابق الطرق العامة التي تبدأ بـ "get" في `MyService` وتُرجع `String`.

يمكنك أيضًا دمج نقاط القطع:
```java
@Pointcut("execution(* com.example.myapp.service.*.*(..))")
public void serviceMethods() {}

@Before("serviceMethods()")
public void logBeforeService() {
    System.out.println("Service method called");
}
```

### 6. **الوصول إلى تفاصيل الطريقة**
يمكنك الوصول إلى معاملات الطريقة أو التوقيعات أو البيانات الوصفية:
```java
@Before("execution(* com.example.myapp.service.*.*(..))")
public void logMethodDetails(JoinPoint joinPoint) {
    String methodName = joinPoint.getSignature().getName();
    Object[] args = joinPoint.getArgs();
    System.out.println("Method " + methodName + " called with " + args.length + " arguments");
}
```

### 7. **التشغيل والاختبار**
- أنشئ فصل خدمة (مثل `MyService`) يحتوي على بعض الطرق.
- شغّل تطبيق Spring الخاص بك.
- سيتم تطبيق الجانب تلقائيًا على الطرق المطابقة.

#### مثال على الخدمة:
```java
@Service
public class MyService {
    public String sayHello(String name) {
        return "Hello, " + name;
    }
}
```

عند استدعاء `myService.sayHello("Alice")`، سيتم تفعيل جوانب التسجيل أو الأداء.

### نصائح
- **الأداء**: تضيف AOP حملًا إضافيًا بسبب الوكلاء، لذا استخدمها بحكمة.
- **النطاق**: يعمل Spring AOP على حبوب Spring المدارة فقط. بالنسبة للكائنات غير التابعة لـ Spring، فكر في استخدام AspectJ (بديل أكثر قوة).
- **تصحيح الأخطاء**: قم بتمكين تسجيل التصحيح (debug logging) لـ `org.springframework.aop` لترى كيف يتم تطبيق الوكلاء.

إذا كان لديك حالة استخدام محددة أو تحتاج إلى مساعدة في تنفيذ معين، فأخبرني وسأقوم بتخصيص الشرح بشكل أكبر!