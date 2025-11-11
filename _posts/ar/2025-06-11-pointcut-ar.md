---
audio: false
generated: true
lang: ar
layout: post
title: فهم تعبيرات نقطة القطع
translated: true
type: note
---

تطلب دليلاً شاملاً حول تعبيرات نقطة القطع في AspectJ، مع التركيز تحديداً على `execution` وكيفية استخدام الأحرف البدلة، ومطابقة أسماء الفئات (بادئة/لاحقة)، وأيضاً حول أنواع النصائح الأخرى مثل `@AfterReturning`. دعنا نفصل هذا الموضوع.

### فهم تعبيرات نقطة القطع في Spring AOP (بناء جملة AspectJ)

يستخدم Spring AOP تعبيرات نقطة القطع من AspectJ لتحديد *أين* يجب تطبيق النصيحة (مثل `@Before`، `@AfterReturning`، إلخ). جوهر سؤالك يدور حول محدد نقطة القطع `execution`، وهو الأكثر استخداماً.

#### محدد نقطة القطع `execution`

يطابق محدد نقطة القطع `execution` عمليات تنفيذ الأساليب. وبناء جملته العام هو:

`execution(modifiers-pattern? ret-type-pattern declaring-type-pattern?name-pattern(param-pattern) throws-pattern?)`

دعنا نحلل المكونات:

* **`modifiers-pattern?`**: اختياري. يطابق معدّلات الأسلوب (مثل `public`، `private`، `protected`).
* **`ret-type-pattern`**: مطلوب. يطابق نوع الإرجاع للأسلوب.
* **`declaring-type-pattern?`**: اختياري. يطابق الاسم المؤهل بالكامل للفئة التي تم فيها تعريف الأسلوب.
* **`name-pattern`**: مطلوب. يطابق اسم الأسلوب.
* **`param-pattern`**: مطلوب. يطابق معاملات الأسلوب.
* **`throws-pattern?`**: اختياري. يطابق الاستثناءات التي يرميها الأسلوب.

#### مثالك: `@Before("execution(* com.example.service.*.*(..))")`

دعنا نحلل المثال المذكور:

* `@Before`: هذا تعليق نصيحة، مما يعني أن الأسلوب المُعلَّق عنه سيعمل *قبل* نقطة الالتحام المطابقة.
* `execution()`: محدد نقطة القطع.
* `*`: يطابق أي نوع إرجاع.
* `com.example.service.*.*`:
    * `com.example.service`: يطابق الحزمة `com.example.service`.
    * `.*`: أول `*` بعد `service` يطابق أي فئة داخل حزمة `com.example.service`.
    * `.`: فاصل بين الحزمة/الفئة والأسلوب.
    * `*`: ثاني `*` يطابق أي اسم أسلوب داخل تلك الفئات.
* `(..)`: يطابق أي عدد من المعاملات (صفر أو أكثر، من أي نوع).

**بالإنجليزية البسيطة:** تطابق نقطة القطع هذه تنفيذ *أي أسلوب* في *أي فئة* داخل حزمة `com.example.service` (وأي حزم فرعية مباشرة لها، إذا كانت هناك فئات مباشرة في `com.example.service`).

---

### الأحرف البدلة في تعبيرات نقطة القطع

الأحرف البدلة ضرورية لإنشاء تعبيرات نقطة قطع مرنة.

* **`*` (علامة نجمية مفردة)**:
    * يطابق أي عنصر مفرد في نمط الاسم (مثل أي نوع إرجاع، أي اسم فئة، أي اسم أسلوب).
    * يطابق أي مقطع مفرد في اسم الحزمة (مثل `com.example.*.service` سيطابق `com.example.foo.service`).
* **`..` (نقطتان مزدوجتان)**:
    * **في أنماط الحزم**: يطابق صفراً أو أكثر من المقاطع في اسم الحزمة.
        * `com.example..service`: يطابق `com.example.service`، `com.example.foo.service`، `com.example.foo.bar.service`، إلخ.
    * **في أنماط المعاملات**: يطابق صفراً أو أكثر من الوسائط من أي نوع.
        * `(..)`: يطابق أي عدد من الوسائط.
        * `(java.lang.String, ..)`: يطابق الأساليب التي تحتوي على `String` كأول وسيطة، متبوعة بأي عدد من الوسائط الأخرى.
        * `(.., java.lang.Long)`: يطابق الأساليب التي تحتوي على أي عدد من الوسائط الأولية، وتنتهي بـ `Long`.

---

### مطابقة أسماء الفئات

#### 1. مطابقة اسم الفئة باللاحقة

لمطابقة الفئات التي تنتهي بلاحقة محددة، تضع الحرف البدل قبل اللاحقة.

**مثال: مطابقة جميع الفئات التي تنتهي بـ `ServiceImpl`**

```java
@Before("execution(* com.example.service.*ServiceImpl.*(..))")
```

* `*ServiceImpl`: يطابق أي اسم فئة ينتهي بـ `ServiceImpl`.

**مثال: مطابقة جميع الفئات التي تنتهي بـ `Controller` في أي حزمة فرعية لـ `com.example.web`**

```java
@Before("execution(* com.example.web..*Controller.*(..))")
```

* `com.example.web..`: يطابق `com.example.web` وأي من حزمه الفرعية.
* `*Controller`: يطابق أي اسم فئة ينتهي بـ `Controller`.

#### 2. مطابقة اسم الفئة بالبادئة

لمطابقة الفئات التي تبدأ ببادئة محددة، تضع الحرف البدل بعد البادئة.

**مثال: مطابقة جميع الفئات التي تبدأ بـ `User`**

```java
@Before("execution(* com.example.service.User*.*(..))")
```

* `User*`: يطابق أي اسم فئة يبدأ بـ `User`.

**مثال: مطابقة جميع الفئات التي تبدأ بـ `Admin` في حزمة `com.example.admin`**

```java
@Before("execution(* com.example.admin.Admin*.*(..))")
```

#### 3. مطابقة أسماء فئات محددة (مطابقة تامة)

لا حاجة للأحرف البدلة للمطابقة التامة.

**مثال: مطابقة الأساليب في `com.example.service.UserServiceImpl` فقط**

```java
@Before("execution(* com.example.service.UserServiceImpl.*(..))")
```

---

### أنواع مختلفة من محددات نقطة القطع

بينما `execution` هو الأكثر شيوعاً، يوفر AspectJ عدة محددات أخرى لنقطة القطع لتحديد نقاط الالتحام. يمكنك الجمع بينها باستخدام العوامل المنطقية (`and`، `or`، `not` أو `&&`، `||`، `!`).

إليك أهمها:

1.  **`execution()`**: كما نوقش، يطابق تنفيذ الأساليب.
    * مثال: `@Before("execution(* com.example.service.UserService.*(..))")`

2.  **`within()`**: يطابق نقاط الالتحام حيث يكون الكود داخل نوع معين (فئة). غالباً ما يستخدم لتقييد نطاق نقاط القطع الأخرى.
    * مثال: `@Before("within(com.example.service.*) && execution(* *(..))")`
        * هذا يجمع بين `within` و `execution`. يعني "أي تنفيذ أسلوب داخل أي فئة في حزمة `com.example.service`." جزء `execution` هو مجرد حرف بدل لأي أسلوب، حيث أن `within` يتعامل مع مطابقة الفئة.

3.  **`this()`**: يطابق نقاط الالتحام حيث أن الوكيل *نفسه* هو نسخة من النوع المعطى. هذا أقل استخداماً للنصائح البسيطة وأكثر لقضايا الإدخال أو الاستدعاء الذاتي.
    * مثال: `@Around("this(com.example.service.UserService)")`
        * يطابق إذا كان وكيل AOP ينفذ `UserService`.

4.  **`target()`**: يطابق نقاط الالتحام حيث أن *الكائن الهدف* (الكائن الفعلي الذي تتم نصيحته، وليس الوكيل) هو نسخة من النوع المعطى. هذا غالباً ما يكون أكثر بديهية من `this()` عندما تهتم بالتنفيذ الأساسي.
    * مثال: `@Around("target(com.example.service.UserServiceImpl)")`
        * يطابق إذا كان الكائن الهدف هو نسخة من `UserServiceImpl`.

5.  **`args()`**: يطابق نقاط الالتحام حيث تكون الوسائط من نوع معين أو تطابق نمطاً معيناً.
    * مثال: `@Before("execution(* com.example.service.*.*(String, ..))")`
        * يطابق الأساليب حيث الوسيطة الأولى هي `String`.
    * مثال: `@Before("args(java.lang.String, int)")`
        * يطابق الأساليب التي تأخذ بالضبط `String` متبوعة بـ `int`.
    * مثال: `@Before("args(name, age)")` حيث يمكن بعد ذلك ربط `name` و `age` بمعاملات أسلوب النصيحة.

6.  **`bean()`**: (خاص بـ Spring) يطابق الأساليب المنفذة على Spring beans بأسماء أو أنماط أسماء محددة.
    * مثال: `@Before("bean(userService) && execution(* *(..))")`
        * يطابق أي تنفيذ أسلوب على Spring bean بالاسم "userService".
    * مثال: `@Before("bean(*Service) && execution(* *(..))")`
        * يطابق أي تنفيذ أسلوب على Spring beans التي تنتهي أسماؤها بـ "Service".

7.  **`@annotation()`**: يطابق نقاط الالتحام حيث يكون الأسلوب الهدف (أو الفئة لـ `within`) مُعلَّقاً عليه بتعليق محدد.
    * مثال: `@Before("@annotation(com.example.annotation.Loggable)")`
        * يطابق أي أسلوب مُعلَّق عليه بـ `@Loggable`.
    * مثال: `@Before("execution(* *(..)) && @annotation(org.springframework.transaction.annotation.Transactional)")`
        * يطابق أي تنفيذ أسلوب مُعلَّق عليه بـ `@Transactional`.

8.  **`@within()`**: يطابق نقاط الالتحام حيث أن نوع التصريح (الفئة) مُعلَّق عليه بتعليق محدد.
    * مثال: `@Before("@within(org.springframework.stereotype.Service) && execution(* *(..))")`
        * يطابق أي تنفيذ أسلوب داخل فئة مُعلَّق عليها بـ `@Service`.

9.  **`@target()`**: يطابق نقاط الالتحام حيث أن فئة الكائن الهدف تحتوي على التعليق المعطى.
    * مثال: `@Around("@target(com.example.annotation.Auditable)")`

10. **`@args()`**: يطابق نقاط الالتحام حيث أن نوع وقت التشغيل للوسائط الفعلية الممررة إلى الأسلوب يحتوي على تعليقات من النوع/الأنواع المعطاة.
    * مثال: `@Before("@args(com.example.annotation.ValidInput)")`

---

### أنواع النصائح (التعليقات)

لقد ذكرت `@AfterReturning` و "أي نوع آخر يمكننا استخدامه في التعليقات". يوفر Spring AOP عدة أنواع من النصائح، كل منها ينفذ في نقطة مختلفة في دورة حياة نقطة الالتحام:

1.  **`@Before`**:
    * ينفذ *قبل* تنفيذ الأسلوب المطابق.
    * مثال: تسجيل تفاصيل الطلب قبل تشغيل أسلوب الخدمة.
    * لا يمكنه منع الأسلوب من التنفيذ أو تغيير قيمته المرجعة.

2.  **`@AfterReturning`**:
    * ينفذ *بعد* أن يعيد الأسلوب المطابق القيمة *بنجاح* (دون رمي استثناء).
    * يمكنه الوصول إلى القيمة المرجعة للأسلوب.
    * بناء الجملة: `@AfterReturning(pointcut="yourPointcut()", returning="result")`
    * مثال:
        ```java
        @AfterReturning(pointcut="execution(* com.example.service.UserService.getUserById(..))", returning="user")
        public void logUserRetrieval(Object user) {
            System.out.println("User retrieved: " + user);
        }
        ```
        *ملاحظة: يجب أن يطابق اسم سمة `returning` (`user` في هذا المثال) اسم المعامل في أسلوب النصيحة.*

3.  **`@AfterThrowing`**:
    * ينفذ *بعد* أن يرمي الأسلوب المطابق استثناءً.
    * يمكنه الوصول إلى الاستثناء المرمي.
    * بناء الجملة: `@AfterThrowing(pointcut="yourPointcut()", throwing="ex")`
    * مثال:
        ```java
        @AfterThrowing(pointcut="execution(* com.example.service.*.*(..))", throwing="ex")
        public void logException(Exception ex) {
            System.err.println("Exception occurred: " + ex.getMessage());
        }
        ```
        *ملاحظة: يجب أن يطابق اسم سمة `throwing` (`ex` في هذا المثال) اسم المعامل في أسلوب النصيحة.*

4.  **`@After` (نصيحة finally)**:
    * ينفذ *بعد* اكتمال الأسلوب المطابق، بغض النظر عما إذا كان قد أعاد بنجاح أو رمى استثناءً.
    * مشابه لكتلة `finally`.
    * مثال: تحرير الموارد، بغض النظر عن نتيجة الأسلوب.
    * ```java
        @After("execution(* com.example.service.OrderService.placeOrder(..))")
        public void cleanupOrderProcess() {
            System.out.println("Order process completed (cleanup)");
        }
        ```

5.  **`@Around`**:
    * أقوى أنواع النصائح وأكثرها مرونة.
    * ينفذ *حول* تنفيذ الأسلوب المطابق.
    * أنت مسؤول عن استدعاء الأسلوب الفعلي باستخدام `ProceedingJoinPoint.proceed()`.
    * يمكنه فحص، تعديل، أو حتى قمع وسائط الأسلوب وقيمته المرجعة.
    * يمكنه التقاط ومعالجة الاستثناءات التي يرميها الأسلوب المُنصَح.
    * مثال: مراقبة الأداء، إدارة المعاملات، التخزين المؤقت.
    * ```java
        import org.aspectj.lang.ProceedingJoinPoint;
        import org.aspectj.lang.annotation.Around;
        import org.aspectj.lang.annotation.Aspect;

        @Aspect
        public class PerformanceMonitorAspect {

            @Around("execution(* com.example.service.*.*(..))")
            public Object profile(ProceedingJoinPoint joinPoint) throws Throwable {
                long start = System.currentTimeMillis();
                Object result = joinPoint.proceed(); // تنفيذ الأسلوب الأصلي
                long end = System.currentTimeMillis();
                System.out.println(joinPoint.getSignature().getName() + " executed in " + (end - start) + "ms");
                return result;
            }
        }
        ```

### تعريف نقاط القطع القابلة لإعادة الاستخدام

لتحسين إمكانية القراءة وإعادة الاستخدام، يمكنك تعريف نقاط قطع مسماة باستخدام `@Pointcut`.

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.AfterReturning;

@Aspect
public class MyServiceAspect {

    // تعريف نقطة قطع لجميع الأساليب في حزمة com.example.service
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // تعريف نقطة قطع للأساليب التي ترجع كائن User
    @Pointcut("execution(com.example.model.User com.example.service.*.*(..))")
    public void returnsUser() {}

    // استخدام نقطة القطع المعرفة
    @Before("serviceMethods()")
    public void logBeforeServiceCall() {
        System.out.println("Before service method execution.");
    }

    // الجمع بين نقاط القطع باستخدام AND منطقي
    @AfterReturning(pointcut="serviceMethods() && returnsUser()", returning="user")
    public void logUserReturned(Object user) {
        System.out.println("Service method returned user: " + user);
    }

    // يمكنك أيضاً تعريف نقاط قطع بوسائط
    @Pointcut("execution(* com.example.repository.*.save(..)) && args(entity)")
    public void repositorySave(Object entity) {}

    @Before("repositorySave(entity)")
    public void logEntityBeforeSave(Object entity) {
        System.out.println("Saving entity: " + entity);
    }
}
```

يغطي هذا الدليل الشامل الأساسيات حول تعبيرات نقطة القطع، واستخدام الأحرف البدلة، ومطابقة أسماء الفئات، وأنواع النصائح المختلفة في Spring AOP. سيسمح لك إتقان هذه المفاهيم بالتحكم بدقة في مكان وزمان تطبيق اهتماماتك المتقاطعة.