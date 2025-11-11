---
audio: false
generated: true
lang: ar
layout: post
title: أسبكت جي مع جافا وسبرينغ بوت
translated: true
type: note
---

## جدول المحتويات
1. [مقدمة في البرمجة الموجهة بالجوانب (AOP)](#مقدمة-في-البرمجة-الموجهة-بالجوانب-aop)
2. [نظرة عامة على AspectJ](#نظرة-عامة-على-aspectj)
3. [AspectJ مع Java](#aspectj-مع-java)
4. [AspectJ مع Spring Boot](#aspectj-مع-spring-boot)
5. [حالات الاستخدام الشائعة](#حالات-الاستخدام-الشائعة)
6. [أفضل الممارسات](#أفضل-الممارسات)
7. [اعتبارات الأداء](#اعتبارات-الأداء)

## مقدمة في البرمجة الموجهة بالجوانب (AOP)

AOP هو نموذج برمجة يهدف إلى زيادة الوحدوية من خلال السماح بفصل الاهتمامات المتقاطعة. الاهتمامات المتقاطعة هي الوظائفية التي تمتد عبر أجزاء متعددة من النظام (مثل التسجيل، الأمان، إدارة المعاملات).

مفاهيم AOP الرئيسية:
- **الجانب (Aspect)**: تجزئة لاهتمام يقطع عبر فئات متعددة
- **نقطة الالتحام (Join point)**: نقطة أثناء تنفيذ البرنامج (استدعاء دالة، الوصول إلى حقل، إلخ)
- **النصيحة (Advice)**: الإجراء المتخذ عند نقطة الالتحام معينة
- **تعبير نقطة القطع (Pointcut)**: مسند يطابق نقاط الالتحام
- **النسج (Weaving)**: ربط الجوانب مع أنواع التطبيقات الأخرى

## نظرة عامة على AspectJ

AspectJ هو تنفيذ AOP الأكثر شيوعًا والأكثر اكتمالًا لـ Java. يوفر:
- لغة نقطة قطع قوية
- آليات نسج مختلفة (نسج وقت الترجمة، بعد الترجمة، وقت التحميل)
- دعم AOP كامل يتجاوز ما توفره Spring AOP

### AspectJ مقابل Spring AOP

| الميزة            | AspectJ | Spring AOP |
|--------------------|---------|------------|
| نقاط الالتحام        | تنفيذ الأسلوب، استدعاءات المُنشئ، الوصول إلى الحقول، إلخ. | تنفيذ الأسلوب فقط |
| النسج            | وقت الترجمة، بعد الترجمة، وقت التحميل | إنشاء وكيل وقت التشغيل |
| الأداء        | أفضل (لا توجد تكلفة إضافية وقت التشغيل) | أبطأ قليلاً (يستخدم وكلاء) |
| التعقيد         | أكثر تعقيدًا | أبسط |
| التبعيات       | يتطلب مترجم/ناسج AspectJ | مضمن في Spring |

## AspectJ مع Java

### الإعداد

1. أضف تبعيات AspectJ إلى ملف `pom.xml` (Maven):

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

2. قم بتكوين إضافة AspectJ لـ Maven للنسج في وقت الترجمة:

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

### إنشاء الجوانب

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;

@Aspect
public class LoggingAspect {

    // تعريف نقطة القطع
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // النصيحة
    @Before("serviceMethods()")
    public void logBeforeServiceMethods() {
        System.out.println("A service method is about to be executed");
    }
}
```

### أنواع النصائح

1. **Before**: تُنفذ قبل نقطة الالتحام
2. **After**: تُنفذ بعد اكتمال نقطة الالتحام (بشكل طبيعي أو استثنائي)
3. **AfterReturning**: تُنفذ بعد اكتمال نقطة الالتحام بشكل طبيعي
4. **AfterThrowing**: تُنفذ إذا خرجت الدالة برمي استثناء
5. **Around**: تحيط بنقطة الالتحام (أقوى أنواع النصائح)

### تعبيرات نقطة القطع

يوفر AspectJ لغة تعبيرات نقطة قطع غنية:

```java
// تنفيذ دالة في حزمة
@Pointcut("execution(* com.example.service.*.*(..))")

// تنفيذ دالة في فئة
@Pointcut("execution(* com.example.service.UserService.*(..))")

// دالة باسم محدد
@Pointcut("execution(* *..find*(..))")

// بنوع إرجاع محدد
@Pointcut("execution(public String com.example..*(..))")

// بأنواع معاملات محددة
@Pointcut("execution(* *.*(String, int))")

// دمج تعبيرات نقطة القطع
@Pointcut("serviceMethods() && findMethods()")
```

## AspectJ مع Spring Boot

### الإعداد

1. أضف تبعيات Spring AOP و AspectJ:

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

2. فعّل دعم AspectJ في تطبيق Spring Boot الخاص بك:

```java
@SpringBootApplication
@EnableAspectJAutoProxy
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

### مثال: تسجيل وقت التنفيذ

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

أنشئ شرحًا مخصصًا:

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

استخدمه على الدوال:

```java
@Service
public class UserService {
    
    @LogExecutionTime
    public List<User> getAllUsers() {
        // implementation
    }
}
```

### مثال: إدارة المعاملات

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

## حالات الاستخدام الشائعة

1. **التسجيل**: تسجيل مركزي لدخول وخروج الدوال والاستثناءات
2. **مراقبة الأداء**: تتبع أوقات التنفيذ
3. **إدارة المعاملات**: حدود معاملات تصريحية
4. **الأمان**: فحوصات التفويض
5. **معالجة الأخطاء**: معالجة استثناءات متسقة
6. **التخزين المؤقت**: التخزين المؤقت التلقائي لنتائج الدوال
7. **التحقق**: التحقق من المعاملات
8. **التدقيق**: تتبع من فعل ماذا ومتى

## أفضل الممارسات

1. **اجعل الجوانب مركزة**: يجب أن يعالج كل جانب اهتمامًا واحدًا
2. **استخدم أسماء ذات معنى**: أسماء جوانب ونقاط قطع واضحة
3. **تجنب منطق الأعمال في الجوانب**: يجب أن تعالج الجوانب الاهتمامات المتقاطعة، وليس المنطق الأساسي
4. **وثق الجوانب**: خاصة تعبيرات نقطة القطع المعقدة
5. **ضع في الاعتبار الأداء**: النصيحة Around يمكن أن تؤثر على الأداء
6. **اختبر الجوانب**: الجوانب تحتاج إلى اختبار مثل أي كود آخر
7. **استخدم الشروح**: الشروح المخصصة تجعل الجوانب أكثر تصريحية
8. **كن حذرًا مع execution() مقابل @annotation()**: اعرف متى تستخدم كل منها

## اعتبارات الأداء

1. **نسج وقت الترجمة** هو عمومًا الخيار الأسرع
2. **نسج وقت التحميل** يضيف بعض الحمل الإضافي أثناء تحميل الفئات
3. **نسج وقت التشغيل** (Spring AOP) له أكبر حمل إضافي
4. **تعبيرات نقطة القطع المعقدة** يمكن أن تؤثر على الأداء
5. **النصيحة Around** أكثر تكلفة من أنواع النصائح الأخرى

لأقصى أداء في الإنتاج:
- استخدم نسج وقت الترجمة حيثما أمكن
- حافظ على بساطة تعبيرات نقطة القطع
- تجنب تعبيرات نقطة القطع الواسعة جدًا

## خاتمة

يوفر AspectJ طريقة قوية لتنفيذ الاهتمامات المتقاطعة في تطبيقات Java و Spring Boot. بينما Spring AOP أبسط وكافٍ للعديد من الحالات، يقدم AspectJ إمكانيات أكثر عندما تحتاج إلى تجاوز اعتراض الدوال. باتباع الأنماط وأفضل الممارسات الموضحة في هذا الدليل، يمكنك استخدام AspectJ بشكل فعال لإنشاء تطبيقات أكثر وحدوية وقابلية للصيانة.