---
audio: false
generated: true
lang: ar
layout: post
title: التبعيات الدائرية في سبرينغ
translated: true
type: note
---

تحدث التبعيات الدائرية في Spring أو Spring Boot عندما يعتمد حبتان (beans) أو أكثر على بعضهما البعض، بشكل مباشر أو غير مباشر، أثناء التهيئة. هذا يخلق حلقة حيث لا تستطيع آلية حقن التبعية في Spring حل هذه التبعيات لأن كل حبة تتطلب أن تكون الحبة الأخرى مهيأة بالكامل أولاً. تحدث هذه المشكلة عادةً أثناء إنشاء الحبوب في سياق تطبيق Spring (Spring Application Context)، مما يؤدي إلى ظهور استثناء `BeanCurrentlyInCreationException`.

### لماذا تحدث التبعيات الدائرية
تدير Spring الحبوب في حاوية حقن التبعية، ويتم إنشاء الحبوب عادةً بترتيب معين بناءً على تبعياتها. عندما تشير الحبوب إلى بعضها البعض بطريقة دورية (على سبيل المثال، الحبة A تعتمد على الحبة B، والحبة B تعتمد على الحبة A)، لا تستطيع Spring إنشاءها لأنها تتعطل في حلقة لا نهائية أثناء التهيئة. هذا شائع بشكل خاص في التطبيقات المعقدة ذات المكونات المترابطة بشكل وثيق.

من المرجح أن تحدث المشكلة في السيناريوهات التالية:
1.  **حقن المُنشئ (Constructor Injection)**: عندما يتم توصيل الحبوب عبر المُنشئات، يجب على Spring حل التبعيات في وقت التهيئة، مما قد يؤدي إلى مشاكل دورية إذا كانت الحبوب تشير إلى بعضها البعض.
2.  **الحقن عبر الحقول أو الطرق Setter مع التهيئة الفورية (Eager Initialization)**: إذا تم تهيئة الحبوب بشكل فوري (السلوك الافتراضي للحبوب ذات النطاق Singleton)، تحاول Spring حل التبعيات على الفور، مما يكشف عن التبعيات الدائرية.
3.  **علاقات الحبوب المعقدة أو غير المُهيأة بشكل صحيح**: التصميم الضعيف أو عدم وجود فصل للاهتمامات (Separation of Concerns) يمكن أن يؤدي إلى حدوث دورات غير مقصودة.
4.  **الشرح مثل `@Autowired` أو `@Component`**: حقن التبعية التلقائي في المكونات المترابطة بشكل وثيق يمكن أن ينشئ دورات عن غير قصد.

### أمثلة شائعة للتبعيات الدائرية

#### المثال 1: دورة حقن المُنشئ
```java
@Component
public class BeanA {
    private final BeanB beanB;

    @Autowired
    public BeanA(BeanB beanB) {
        this.beanB = beanB;
    }
}

@Component
public class BeanB {
    private final BeanA beanA;

    @Autowired
    public BeanB(BeanA beanA) {
        this.beanA = beanA;
    }
}
```
**المشكلة**: `BeanA` تتطلب `BeanB` في مُنشئها، و `BeanB` تتطلب `BeanA` في مُنشئها. لا تستطيع Spring إنشاء أي من الحبتين لأن كل منهما تعتمد على الأخرى أن تكون مهيأة بالكامل أولاً.

**الخطأ**: `BeanCurrentlyInCreationException: Error creating bean with name 'beanA': Requested bean is currently in creation: Is there an unresolvable circular reference?`

#### المثال 2: دورة الحقن عبر الحقول
```java
@Component
public class BeanA {
    @Autowired
    private BeanB beanB;
}

@Component
public class BeanB {
    @Autowired
    private BeanA beanA;
}
```
**المشكلة**: كل من `BeanA` و `BeanB` تستخدمان `@Autowired` لحقن بعضهما البعض عبر الحقول. على الرغم من أن الحقن عبر الحقول أكثر مرونة من حقن المُنشئ، إلا أن Spring لا تزال تكتشف الدورة أثناء تهيئة الحبة إذا كانت كلاهما من نوع Singleton (النطاق الافتراضي).

#### المثال 3: تبعية دائرية غير مباشرة
```java
@Component
public class BeanA {
    @Autowired
    private BeanB beanB;
}

@Component
public class BeanB {
    @Autowired
    private BeanC beanC;
}

@Component
public class BeanC {
    @Autowired
    private BeanA beanA;
}
```
**المشكلة**: `BeanA` تعتمد على `BeanB`، و `BeanB` تعتمد على `BeanC`، و `BeanC` تعتمد على `BeanA`، مشكلة دورة. هذه التبعية غير المباشرة يصعب ملاحظتها ولكنها تسبب نفس المشكلة.

#### المثال 4: فئات `@Configuration` ذات مراجع دائرية
```java
@Configuration
public class ConfigA {
    @Autowired
    private ConfigB configB;

    @Bean
    public ServiceA serviceA() {
        return new ServiceA(configB);
    }
}

@Configuration
public class ConfigB {
    @Autowired
    private ConfigA configA;

    @Bean
    public ServiceB serviceB() {
        return new ServiceB(configA);
    }
}
```
**المشكلة**: فئتي التهيئة `ConfigA` و `ConfigB` تعتمدان على بعضهما البعض، مما يخلق دورة عندما تحاول Spring تهيئة الحبوب المعرفة في هذه الفئات.

### الأسباب الشائعة في Spring Boot
-   **التهيئة التلقائية (Auto-Configuration)**: يمكن لتهيئة Spring Boot التلقائية أن تقدم أحيانًا تبعيات تؤدي إلى دورات، خاصة عندما تتفاعل الحبوب المخصصة مع الحبوب المُهيأة تلقائيًا.
-   **مسح المكونات (Component Scanning)**: الإفراط في استخدام `@ComponentScan` أو الحزم غير المُهيأة بشكل صحيح يمكن أن يلتقط حبوبًا غير مقصودة، مما يؤدي إلى تبعيات دائرية.
-   **التصميم المترابط بشكل وثيق**: منطق الأعمال الذي يربط الخدمات والمستودعات وأجهزة التحكم بشكل وثيق يمكن أن ينشئ دورات عن غير قصد.
-   **إساءة استخدام نطاق Prototype**: بينما يمكن للحبوب ذات نطاق Prototype أن تتجنب التبعيات الدائرية في بعض الأحيان، فإن الجمع بينها وبين حبوب Singleton بطريقة دورية يمكن أن يسبب مشاكل.

### كيفية حل التبعيات الدائرية
1.  **استخدام شرح `@Lazy`**:
    - علق أحد التبعيات بـ `@Lazy` لتأخير تهيئتها حتى الحاجة الفعلية لها.
    ```java
    @Component
    public class BeanA {
        @Autowired
        @Lazy
        private BeanB beanB;
    }
    ```
    هذا يكسر الدورة بالسماح لـ `BeanA` أن تُهيأ جزئيًا قبل حل `BeanB`.

2.  **التحول إلى الحقن عبر طرق Setter أو الحقول**:
    - بدلاً من حقن المُنشئ، استخدم الحقن عبر طرق Setter أو الحقول لإحدى الحبوب للسماح لـ Spring بتهيئة الحبة أولاً ثم حقن التبعيات لاحقًا.
    ```java
    @Component
    public class BeanA {
        private BeanB beanB;

        @Autowired
        public void setBeanB(BeanB beanB) {
            this.beanB = beanB;
        }
    }
    ```

3.  **إعادة هيكلة الكود لكسر الدورة**:
    - قدم واجهة أو مكونًا وسيطًا لفصل الحبوب.
    - مثال: استخرج تبعية مشتركة إلى حبة ثالثة أو استخدم طبقة خدمة للتوسط في التفاعلات.
    ```java
    public interface Service {
        void performAction();
    }

    @Component
    public class BeanA implements Service {
        @Autowired
        private BeanB beanB;

        public void performAction() {
            // Logic
        }
    }

    @Component
    public class BeanB {
        @Autowired
        private Service service; // تعتمد على الواجهة، وليس على BeanA مباشرة
    }
    ```

4.  **استخدام شرح `@DependsOn`**:
    - تحكم بشكل صريح في ترتيب تهيئة الحبوب لتجنب الدورات في حالات محددة.
    ```java
    @Component
    @DependsOn("beanB")
    public class BeanA {
        @Autowired
        private BeanB beanB;
    }
    ```

5.  **تمكين الوكائل (Proxying) باستخدام `@EnableAspectJAutoProxy`**:
    - تأكد من أن Spring تستخدم الوكائل (CGLIB أو JDK dynamic proxies) لمعالجة التبعيات، مما يمكنه حل بعض مشاكل الدورية عن طريق حقن وكيل بدلاً من الحبة الفعلية.

6.  **إعادة تقييم التصميم**:
    - غالبًا ما تشير التبعيات الدائرية إلى عيب في التصميم. فكر في إعادة الهيكلة للالتزام بمبدأ المسؤولية الواحدة (Single Responsibility Principle) أو مقلوب التبعيات (Dependency Inversion Principle).

### كيفية تصحيح التبعيات الدائرية
-   **تحقق من Stack Trace**: سيشير Stack Trace الخاص باستثناء `BeanCurrentlyInCreationException` إلى الحبوب المشاركة في الدورة.
-   **تفعيل تسجيل Debug**: عيّن `spring.main.lazy-initialization=true` أو فعّل تسجيل Debug لـ `org.springframework` لرؤية تفاصيل إنشاء الحبوب.
-   **استخدم الأدوات**: يمكن للأدوات مثل Spring Boot Actuator أو إضافات IDEs (مثل Spring Tools Suite) تصور تبعيات الحبوب.

### منع التبعيات الدائرية
-   **اتبع أفضل الممارسات**: استخدم أنماط حقن التبعية مثل الواجهات أو التجريدات لتقليل الترابط الوثيق.
-   **نمطية الكود**: قسّم التطبيقات الكبيرة إلى وحدات أصغر مترابطة بشكل مرن.
-   **اختبر مبكرًا**: شغّل اختبارات التكامل لاكتشاف التبعيات الدائرية أثناء التطوير.
-   **حدد مسح المكونات**: كن محددًا مع `@ComponentScan` لتجنب التقاط حبوب غير ضرورية.

### متى تكون التبعيات الدائرية أقل احتمالًا
-   **نطاق Prototype**: يتم إنشاء الحبوب ذات نطاق Prototype عند الطلب، مما يقلل من احتمالية الدورية (ولكن لا يلغيها تمامًا).
-   **التهيئة المتأخرة (Lazy Initialization)**: تمكين التهيئة المتأخرة العامة (`spring.main.lazy-initialization=true`) يمكن أن يؤجل إنشاء الحبوب، على الرغم من أنه قد يخفي المشكلة فقط.

### خاتمة
تنشأ التبعيات الدائرية في Spring/Spring Boot من الترابط الوثيق بين الحبوب، وغالبًا ما تتفاقم بسبب حقن المُنشئ أو التهيئات المعقدة. تشمل الحلول الشائعة استخدام `@Lazy`، أو التحول إلى الحقن عبر طرق Setter/الحقول، أو إعادة هيكلة الكود لكسر الدورة. من خلال فهم السبب الجذري وتطبيق أفضل الممارسات، يمكنك منع أو حل هذه المشاكل بشكل فعال. إذا واجهت تبعية دائرية محددة، شارك الكود ذو الصلة أو تفاصيل الخطأ، ويمكنني المساعدة في تحليلها further!