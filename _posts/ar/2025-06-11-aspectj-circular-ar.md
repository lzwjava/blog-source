---
audio: false
generated: true
lang: ar
layout: post
title: حل التبعيات الدائرية باستخدام AspectJ
translated: true
type: note
---

تظهر التبعيات الدائرية في سيناريوك لأن `BlogConfig` و`BlogCore` و`BlogWeb` تشير إلى بعضها البعض، مما يخلق حلقة تبعية. بالإضافة إلى ذلك، قد يؤدي `LoggingAspect` الخاص بـ AspectJ في `BlogCore` (أو ربما `BlogWeb`) إلى تفاقم المشكلة إذا تم تطبيقه على طرق عبر الوحدات، بما في ذلك `BlogConfig` الذي يعتمد على `BlogCore`. دعنا نحلل المشكلة ونقدم حلاً لحل التبعية الدائرية مع الحفاظ على وظائف AspectJ سليمة.

### تحليل المشكلة
1. **تبعيات الوحدات**:
   - `BlogCore` تعتمد على `BlogConfig`.
   - `BlogWeb` تعتمد على كل من `BlogCore` و`BlogConfig`.
   - `BlogConfig` تعتمد على `BlogCore` (هذا يخلق التبعية الدائرية: `BlogCore` ↔ `BlogConfig`).
   - قد يؤدي اعتماد `BlogWeb` على كلا الوحدتين إلى سحب التبعية الدائرية.

2. **AspectJ LoggingAspect**:
   - يستخدم `LoggingAspect` في `BlogCore` (أو `BlogWeb`) نقطة قطع واسعة (`execution(* *(..))`)، والتي تنطبق على جميع عمليات تنفيذ الأساليب في سياق التطبيق، بما في ذلك الأساليب في `BlogConfig` و`BlogCore` و`BlogWeb`.
   - إذا كان `LoggingAspect` في `BlogCore` وينسج في `BlogConfig`، و`BlogConfig` تعتمد على `BlogCore`، فقد تعقد عملية نسج AspectJ التبعية الدائرية أثناء التهيئة.

3. **تأثير التبعية الدائرية**:
   - في نظام بناء مثل Maven أو Gradle، يمكن أن تسبب التبعيات الدائرية بين الوحدات مشاكل في الترجمة أو وقت التشغيل (مثل `BeanCurrentlyInCreationException` في Spring، أو مشاكل في تحميل الفئات).
   - قد يفشل نسج AspectJ في وقت الترجمة أو وقت التحميل أو ينتج سلوكًا غير متوقع إذا كانت الفئات من `BlogConfig` و`BlogCore` مترابطة ولم يتم تهيئتها بالكامل.

### الحل
لحل التبعية الدائرية وضمان عمل `LoggingAspect` الخاص بـ AspectJ بشكل صحيح، اتبع هذه الخطوات:

#### 1. كسر التبعية الدائرية
المشكلة الأساسية هي تبعية `BlogCore` ↔ `BlogConfig`. لإصلاح هذا، قم باستخراج الوظائف أو التكوين المشترك الذي يتسبب في اعتماد `BlogConfig` على `BlogCore` إلى وحدة جديدة أو أعد هيكلة التبعيات.

**الخيار أ: تقديم وحدة جديدة (`BlogCommon`)**
- أنشئ وحدة جديدة، `BlogCommon`، لحفظ الواجهات أو التكوينات أو الأدوات المساعدة التي يحتاجها كل من `BlogCore` و`BlogConfig`.
- انقل الأجزاء من `BlogCore` التي تعتمد عليها `BlogConfig` (مثل الواجهات، الثوابت، أو الخدمات المشتركة) إلى `BlogCommon`.
- قم بتحديث التبعيات:
  - `BlogConfig` تعتمد على `BlogCommon`.
  - `BlogCore` تعتمد على `BlogCommon` و`BlogConfig`.
  - `BlogWeb` تعتمد على `BlogCore` و`BlogConfig`.

**مثال على هيكل التبعية**:
```
BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
```

**التنفيذ**:
- في `BlogCommon`، حدد الواجهات أو المكونات المشتركة. على سبيل المثال:
  ```java
  // وحدة BlogCommon
  public interface BlogService {
      void performAction();
  }
  ```
- في `BlogCore`، نفذ الواجهة:
  ```java
  // وحدة BlogCore
  public class BlogCoreService implements BlogService {
      public void performAction() { /* logic */ }
  }
  ```
- في `BlogConfig`، استخدم الواجهة من `BlogCommon`:
  ```java
  // وحدة BlogConfig
  import com.example.blogcommon.BlogService;
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- في `BlogWeb`، استخدم كلا الوحدتين حسب الحاجة.

هذا يلغي التبعية الدائرية من خلال ضمان أن `BlogConfig` لم تعد تعتمد مباشرة على `BlogCore`.

**الخيار ب: انعكاس التحكم (IoC) مع حقن التبعية**
- إذا كنت تستخدم إطار عمل مثل Spring، أعد هيكلة `BlogConfig` لتعتمد على التجريدات (الواجهات) المحددة في `BlogCore` بدلاً من الفئات الملموسة.
- استخدم حقن التبعية لتوفير تنفيذ `BlogCore` لـ `BlogConfig` في وقت التشغيل، مما يتجنب تبعية دائرية في وقت الترجمة.
- مثال:
  ```java
  // وحدة BlogCore
  public interface BlogService {
      void performAction();
  }
  @Component
  public class BlogCoreService implements BlogService {
      public void performAction() { /* logic */ }
  }

  // وحدة BlogConfig
  @Configuration
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- يحل حاوية IoC الخاصة بـ Spring التبعية في وقت التشغيل، مما يكسر التبعية الدائرية في وقت الترجمة.

#### 2. ضبط تكوين AspectJ
قد تنطبق نقطة القطع الواسعة لـ `LoggingAspect` (`execution(* *(..))`) على جميع الوحدات، بما في ذلك `BlogConfig`، مما قد يعقد التهيئة. لجعل الناحية أكثر قابلية للإدارة وتجنب مشاكل النسج:

- **ضيق نقطة القطع**: قم بتقييد الناحية لحزم أو وحدات محددة لتجنب تطبيقها على `BlogConfig` أو كود البنية التحتية الآخر.
  ```java
  import org.aspectj.lang.JoinPoint;
  import org.aspectj.lang.annotation.After;
  import org.aspectj.lang.annotation.Aspect;
  import java.util.Arrays;

  @Aspect
  public class LoggingAspect {
      @After("execution(* com.example.blogcore..*(..)) || execution(* com.example.blogweb..*(..))")
      public void logAfter(JoinPoint joinPoint) {
          System.out.println("Method executed: " + joinPoint.getSignature());
          System.out.println("Arguments: " + Arrays.toString(joinPoint.getArgs()));
      }
  }
  ```
  تنطبق نقطة القطع هذه فقط على الأساليب في `BlogCore` (`com.example.blogcore`) و`BlogWeb` (`com.example.blogweb`)، باستثناء `BlogConfig`.

- **انقل الناحية إلى وحدة منفصلة**: لتجنب مشاكل النسج أثناء تهيئة الوحدة، ضع `LoggingAspect` في وحدة جديدة (مثل `BlogAspects`) تعتمد على `BlogCore` و`BlogWeb` ولكن ليس على `BlogConfig`.
  - هيكل التبعية:
    ```
    BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
                       ↑          ↑
                       └─ BlogAspects ─┘
    ```
  - قم بتحديث تكوين البناء (مثل Maven/Gradle) لضمان نسج `BlogAspects` بعد `BlogCore` و`BlogWeb`.

- **استخدم النسج في وقت التحميل (LTW)**: إذا تسبب النسج في وقت الترجمة في مشاكل بسبب التبعيات الدائرية، انتقل إلى النسج في وقت التحميل مع AspectJ. قم بتكوين LTW في تطبيقك (عبر `@EnableLoadTimeWeaving` الخاص بـ Spring أو ملف `aop.xml`) لتأجيل تطبيق الناحية حتى وقت التشغيل، بعد تحميل الفئات.

#### 3. تحديث تكوين البناء
تأكد من أن أداة البناء الخاصة بك (Maven، Gradle، إلخ) تعكس هيكل الوحدة الجديد وتحل التبعيات بشكل صحيح.

**مثال Maven**:
```xml
<!-- BlogCommon/pom.xml -->
<dependencies>
    <!-- لا توجد تبعيات -->
</dependencies>

<!-- BlogConfig/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCommon</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogCore/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCommon</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogConfig</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogWeb/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCore</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogConfig</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogAspects/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCore</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogWeb</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>org.aspectj</groupId>
        <artifactId>aspectjrt</artifactId>
        <version>1.10.20</version>
    </dependency>
</dependencies>
<build>
    <plugins>
        <plugin>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectj-maven-plugin</artifactId>
            <version>1.15.0</version>
            <executions>
                <execution>
                    <goals>
                        <goal>compile</goal>
                        <goal>test-compile</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

**مثال Gradle**:
```groovy
// BlogCommon/build.gradle
dependencies {
    // لا توجد تبعيات
}

// BlogConfig/build.gradle
dependencies {
    implementation project(':BlogCommon')
}

// BlogCore/build.gradle
dependencies {
    implementation project(':BlogCommon')
    implementation project(':BlogConfig')
}

// BlogWeb/build.gradle
dependencies {
    implementation project(':BlogCore')
    implementation project(':BlogConfig')
}

// BlogAspects/build.gradle
plugins {
    id 'dev.aspectj' version '0.2.0'
}
dependencies {
    implementation project(':BlogCore')
    implementation project(':BlogWeb')
    implementation 'org.aspectj:aspectjrt:1.10.20'
}
aspectj {
    sourceSets {
        main {
            java.srcDirs = ['src/main/java']
        }
    }
}
```

#### 4. اختبر التطبيق
- تحقق من حل التبعية الدائرية عن طريق بناء وتشغيل التطبيق.
- تأكد من أن `LoggingAspect` يسجل عمليات تنفيذ الأساليب في `BlogCore` و`BlogWeb` ولكن ليس في `BlogConfig` (ما لم يكن ذلك مرغوبًا فيه صراحة).
- إذا كنت تستخدم Spring، تحقق من وجود `BeanCurrentlyInCreationException` أو أخطاء مماثلة أثناء تهيئة السياق.
- اختبر نسج AspectJ للتأكد من ظهور السجلات للأساليب الصحيحة.

#### 5. نصائح إضافية
- **استخدم أداة تحليل التبعية**: استخدم أدوات مثل `mvn dependency:tree` في Maven أو مهمة `dependencies` في Gradل للكشف عن أي تبعيات دائرية متبقية.
- **فكر في دقة الناحية**: إذا كان التسجيل مطلوبًا فقط لخدمات محددة، قم بتنقية نقطة القطع بشكل أكبر لاستهداف فئات أو أساليب محددة (مثل `execution(* com.example.blogcore.service.*.*(..))`).
- **تجنب استخدام AspectJ لوحدات التكوين**: بشكل عام، تجنب تطبيق النواحي على كود التكوين أو البنية التحتية (مثل `BlogConfig`) لتقليل التعقيد.

### هيكل التبعية النهائي
بعد إعادة الهيكلة:
```
BlogCommon → BlogConfig → BlogCore → BlogWeb
   ↑                        ↑
   └────── BlogAspects ─────┘
```

### لماذا هذا الحل يعمل
- **كسر الحلقة**: نقل التبعيات المشتركة إلى `BlogCommon` أو استخدام IoC يضمن أن `BlogConfig` لا تعتمد على `BlogCore`، مما يلغي التبعية الدائرية.
- **عزل النواحي**: وضع `LoggingAspect` في وحدة منفصلة (`BlogAspects`) أو تضييق نقطة قطعه يمنع مشاكل النسج ويبقي منطق الناحية مستقلاً عن سلسلة التبعية.
- **تكوين البناء**: يضمن إعداد أداة البناء الصحيحة ترجمة الوحدات ونسجها بالترتيب الصحيح.

يحافظ هذا النهج على وظيفة تسجيل AspectJ الخاصة بك مع ضمان هيكل وحدة نظيف وسهل الصيانة. إذا كان لديك تفاصيل إضافية حول إعدادك (مثل استخدام Spring، فئات محددة تسبب الدورة)، يمكنني تحسين الحل بشكل أكبر!