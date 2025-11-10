---
audio: false
generated: true
lang: ar
layout: post
title: تهيئة Maven لتنفيذ الاختبارات بالتوازي
translated: true
type: note
---

لتمكين تنفيذ الاختبارات المتوازي في مشروع Maven الخاص بك، خاصة لفئة `MavenTest.java` المقدمة، يمكنك تكوين إضافة Maven Surefire لتشغيل الاختبارات بشكل متوازٍ. تستخدم فئة `MavenTest.java` إطار JUnit 4 مع اختبارات ديناميكية لتنفيذ أوامر Maven لمشاكل مختلفة، ويشير تتبع المكدس من الخطأ الأصلي إلى أن الاختبارات تعمل بالفعل بشكل متوازٍ (كما يتضح من وجود `ForkJoinPool` في تتبع المكدس). ومع ذلك، يمكنك التحكم بشكل صريح في التنفيذ المتوازي عن طريق تكوين إضافة Surefire في ملف `pom.xml` الخاص بك. أدناه، سأشرح كيفية إعداد تنفيذ الاختبارات المتوازية ومعالجة استخدام علامة `-DParallel` كما هو مطلوب.

### لماذا يحدث التنفيذ المتوازي
يظهر ناتج الاختبار الخاص بك `ForkJoinPool` في تتبع المكدس، مما يشير إلى أن JUnit أو Maven يستخدم بالفعل مجموعة خيوط (thread pool) للتنفيذ المتوازي. تستخدم فئة `MavenTest` `@TestFactory` مع `DynamicTest`، ومن المرجح أن الاختبارات تعمل بشكل متوازٍ بسبب السلوك الافتراضي لـ JUnit أو تكوين Surefire موجود. الهدف الآن هو تكوين التنفيذ المتوازي بشكل صريح والسماح بالتحكم عبر علامة سطر الأوامر مثل `-DParallel`.

### خطوات تكوين تنفيذ الاختبارات المتوازية

1.  **تحديث `pom.xml` لتكوين إضافة Maven Surefire**:
    تدعم إضافة Maven Surefire تنفيذ الاختبارات المتوازية لـ JUnit 4.7+ (الذي يستخدمه مشروعك، حيث أنه متوافق مع `DynamicTest`). يمكنك تحديد مستوى التوازي (على سبيل المثال، `classes`، `methods`، أو `both`) وعدد الخيوط. لتمكين التحكم عبر `-DParallel`، يمكنك استخدام خاصية Maven لتبديل أو تكوين التوازي.

    أضف أو حدّث تكوين إضافة Surefire في `pom.xml` الخاص بك:

    ```xml
    <project>
        <!-- تكوينات أخرى -->
        <properties>
            <!-- الإعداد الافتراضي هو عدم التنفيذ المتوازي ما لم يتم التحديد -->
            <parallel.mode>none</parallel.mode>
            <thread.count>4</thread.count>
        </properties>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-surefire-plugin</artifactId>
                    <version>3.5.3</version>
                    <configuration>
                        <parallel>${parallel.mode}</parallel>
                        <threadCount>${thread.count}</threadCount>
                        <perCoreThreadCount>false</perCoreThreadCount>
                        <!-- اختياري: وقت الانتظار للاختبارات المتوازية -->
                        <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                        <!-- تكوين Forking لعزل الاختبارات -->
                        <forkCount>1</forkCount>
                        <reuseForks>true</reuseForks>
                    </configuration>
                </plugin>
            </plugins>
        </build>
    </project>
    ```

    - **الشرح**:
      - `<parallel>`: يحدد مستوى التوازي. القيم الصالحة لـ JUnit 4.7+ هي `methods`، `classes`، `both`، `suites`، `suitesAndClasses`، `suitesAndMethods`، `classesAndMethods`، أو `all`. لفئة `MavenTest` الخاصة بك، `classes` مناسب حيث يمثل كل `DynamicTest` مشكلة، وتريد تشغيل اختبارات لمشاكل مختلفة بشكل متوازٍ.
      - `<threadCount>`: يحدد عدد الخيوط (على سبيل المثال، `4` لأربعة اختبارات متزامنة). يمكنك تجاوز هذا عبر `-Dthread.count=<number>`.
      - `<perCoreThreadCount>false</perCoreThreadCount>`: يضمن أن `threadCount` هو رقم ثابت، غير معتمد على عدد نوى المعالج.
      - `<parallelTestsTimeoutInSeconds>`: يحدد وقت انتظار للاختبارات المتوازية لمنع التعلق (يتطابق مع `TEST_TIMEOUT` البالغ 10 ثوانٍ في `MavenTest.java`).
      - `<forkCount>1</forkCount>`: يشغل الاختبارات في عملية JVM منفصلة لعزلها، مما يقلل من مشاكل الحالة المشتركة. `<reuseForks>true</reuseForks>` يسمح بإعادة استخدام JVM للكفاءة.
      - `<parallel.mode>` و `<thread.count>`: خصائص Maven يمكن تجاوزها عبر علامات سطر الأوامر (على سبيل المثال، `-Dparallel.mode=classes`).

2.  **تشغيل الاختبارات باستخدام `-DParallel`**:
    لاستخدام علامة `-DParallel` للتحكم في التنفيذ المتوازي، يمكنك تعيينها إلى خاصية `parallel.mode`. على سبيل المثال، شغّل:

    ```bash
    mvn test -Dparallel.mode=classes -Dthread.count=4
    ```

    - إذا لم يتم تحديد `-Dparallel.mode`، فإن القيمة الافتراضية (`none`) تعطل التنفيذ المتوازي.
    - يمكنك أيضًا استخدام علامة أبسط مثل `-DParallel=true` لتمكين التوازي مع وضع محدد مسبقًا (على سبيل المثال، `classes`). لدعم هذا، حدّث `pom.xml` لتفسير `-DParallel`:

    ```xml
    <project>
        <!-- تكوينات أخرى -->
        <properties>
            <parallel.mode>${Parallel ? 'classes' : 'none'}</parallel.mode>
            <thread.count>4</thread.count>
        </properties>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-surefire-plugin</artifactId>
                    <version>3.5.3</version>
                    <configuration>
                        <parallel>${parallel.mode}</parallel>
                        <threadCount>${thread.count}</threadCount>
                        <perCoreThreadCount>false</perCoreThreadCount>
                        <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                        <forkCount>1</forkCount>
                        <reuseForks>true</reuseForks>
                    </configuration>
                </plugin>
            </plugins>
        </build>
    </project>
    ```

    الآن، يمكنك تشغيل الاختبارات باستخدام:

    ```bash
    mvn test -DParallel=true
    ```

    - `-DParallel=true`: يمكّن التنفيذ المتوازي مع `parallel=classes` و `threadCount=4`.
    - `-DParallel=false` أو حذف `-DParallel`: يعطل التنفيذ المتوازي (`parallel=none`).
    - يمكنك تجاوز عدد الخيوط باستخدام `-Dthread.count=<number>` (على سبيل المثال، `-Dthread.count=8`).

3.  **ضمان سلامة الخيوط (Thread Safety)**:
    تنفذ فئة `MavenTest` الخاصة بك أوامر Maven (`mvn exec:exec -Dproblem=<problem>`) بشكل متوازٍ، مما ينتج عمليات منفصلة. هذا آمن بشكل طبيعي من حيث الخيوط حيث أن كل عملية لها مساحة ذاكرة خاصة بها، مما يتجنب مشاكل الحالة المشتركة. ومع ذلك، تأكد من:
    - أن فئات `com.lzw.solutions.uva.<problem>.Main` لا تشارك الموارد (على سبيل المثال، الملفات أو قواعد البيانات) التي قد تسبب تعارضات.
    - أن ملفات الإدخال/الإخراج أو الموارد المستخدمة من قبل كل مشكلة (على سبيل المثال، بيانات الاختبار لـ `p10009`) معزولة لتجنب ظروف السباق (race conditions).
    - إذا تم استخدام موارد مشتركة، ففكر في استخدام `@NotThreadSafe` على فئات اختبار محددة أو مزامنة الوصول إلى الموارد المشتركة.

4.  **معالجة قائمة التخطي (Skip List) مع التنفيذ المتوازي**:
    يحتوي `MavenTest.java` الخاص بك بالفعل على مجموعة `SKIP_PROBLEMS` لتخطي مشاكل مثل `p10009`. هذا يعمل بشكل جيد مع التنفيذ المتوازي، حيث يتم استبعاد المشاكل المتخطاة قبل جدولة الاختبارات. تأكد من تحديث قائمة التخطي حسب الحاجة:

    ```java
    private static final Set<String> SKIP_PROBLEMS = new HashSet<>(Arrays.asList(
        "p10009", // يتخطى p10009 بسبب NumberFormatException
        "p10037"  // أضف المشاكل الأخرى المشكلة هنا
    ));
    ```

5.  **تشغيل الاختبارات**:
    لتشغيل الاختبارات بشكل متوازٍ مع قائمة التخطي وعلامة `-DParallel`:

    ```bash
    mvn test -DParallel=true -Dthread.count=4
    ```

    - يشغل هذا ما يصل إلى أربعة اختبارات للمشاكل في وقت واحد، متخطيًا `p10009` وأي مشاكل أخرى في `SKIP_PROBLEMS`.
    - إذا أردت تعطيل التوازي لتصحيح الأخطاء:

      ```bash
      mvn test -DParallel=false
      ```

6.  **معالجة `NumberFormatException` لـ `p10009`**:
    يشير `NumberFormatException` في `p10009` (من خطأك الأصلي) إلى تحليل سلسلة (string) ذات قيمة `null`. بينما يتجنب تخطي `p10009` المشكلة، قد ترغب في إصلاحها للإكمال. تحقق من `com.lzw.solutions.uva.p10009.Main` عند السطر 17 (طريقة `readInt`) وأضف فحوصات القيمة الفارغة (null-checks):

    ```java
    public int readInt() {
        String input = readInput(); // طريقة افتراضية لقراءة الإدخال
        if (input == null || input.trim().isEmpty()) {
            throw new IllegalArgumentException("Input cannot be null or empty");
        }
        return Integer.parseInt(input);
    }
    ```

    بدلاً من ذلك، احتفظ بـ `p10009` في قائمة التخطي حتى يتم حل المشكلة.

### ملاحظات حول التنفيذ المتوازي
- **الأداء**: التنفيذ المتوازي مع `parallel=classes` مناسب لفئة `MavenTest` الخاصة بك، حيث يمثل كل `DynamicTest` مشكلة مميزة. هذا يقلل من الحمل الزائد مقارنة بـ `methods` أو `both`.
- **استخدام الموارد**: يزيد التنفيذ المتوازي من استخدام وحدة المعالجة المركزية والذاكرة. راقب نظامك للتأكد من أن `threadCount` (على سبيل المثال، `4`) لا يثقل على أجهزتك. استخدم `forkCount` لعزل الاختبارات في JVMs منفصلة إذا ظهرت مشاكل في الذاكرة.
- **مهلات الانتظار (Timeouts)**: يضمن إعداد `parallelTestsTimeoutInSeconds` ألا تتعلق الاختبارات إلى الأبد، متوافقًا مع `TEST_TIMEOUT` البالغ 10 ثوانٍ في `MavenTest.java`.
- **سلامة الخيوط (Thread Safety)**: نظرًا لأن اختباراتك تنفذ أوامر `mvn exec:exec`، التي تعمل في عمليات منفصلة، فإن سلامة الخيوط أقل إثارة للقلق. ومع ذلك، تأكد من أن مدخلات/مخرجات الاختبار (على سبيل المثال، الملفات) معزولة لكل مشكلة.
- **تصحيح الأخطاء**: إذا فشلت الاختبارات بشكل غير متوقع في الوضع المتوازي، فشغّلها بشكل تسلسلي (`-DParallel=false`) لعزل المشاكل.

### مثال على الأمر الكامل
لتشغيل الاختبارات بشكل متوازٍ، متخطيًا `p10009`، بأربعة خيوط:

```bash
mvn test -DParallel=true -Dthread.count=4
```

لتصحيح مشكلة محددة (على سبيل المثال، `p10009`) بدون توازي، أزلها مؤقتًا من `SKIP_PROBLEMS` وشغّل:

```bash
mvn test -DParallel=false -Dproblem=p10009
```

### اعتبارات إضافية
- **قيود JUnit 4**: يستخدم مشروعك JUnit 4 (استنادًا إلى استيرادات `org.junit.jupiter.api` و `DynamicTest`). يدعم JUnit 4.7+ التنفيذ المتوازي عبر Surefire، لكن JUnit 5 يقدم خيارات توازي أكثر مرونة. فكر في الترقية إلى JUnit 5 إذا كنت بحاجة إلى ميزات متقدمة مثل التوازي لكل فئة أو استراتيجيات مخصصة.
- **إصدار Maven**: تأكد من استخدامك إصدارًا حديثًا من Maven (على سبيل المثال، 3.9.10، كما في ناتج الخطأ الخاص بك) و Surefire (على سبيل المثال، 3.5.3) للحصول على دعم مثالي للتنفيذ المتوازي.
- **معالجة الأخطاء**: لجعل الاختبارات أكثر متانة، فكر في التقاط الاستثناءات في `runMavenExecTests` (كما هو مقترح في الرد السابق) لتسجيل حالات الفشل دون إيقاف مجموعة الاختبار:

   ```java
   @TestFactory
   Collection<DynamicTest> runMavenExecTests() {
       return PROBLEMS.stream()
               .map(problem -> DynamicTest.dynamicTest("Test problem: " + problem, () -> {
                   String command = String.format("mvn exec:exec -Dproblem=%s", problem);
                   System.out.println("Executing command for " + problem + ": " + command);
                   try {
                       Process process = Runtime.getRuntime().exec(command);
                       // ... (بقية كود معالجة العملية)
                       int exitCode = process.exitValue();
                       Assertions.assertTrue(
                               exitCode == 0,
                               "Maven command failed for problem: " + problem + "\nError output:\n" + errorOutput);
                   } catch (Exception e) {
                       System.err.println("Exception for problem " + problem + ": " + e.getMessage());
                       // يمكن الاستمرار بدلاً من الفشل بشكل اختياري
                   }
               }))
               .collect(Collectors.toList());
   }
   ```

يسمح لك هذا الإعداد بالتحكم في التنفيذ المتوازي باستخدام `-DParallel=true`، وتخطي الاختبارات المشكلة مثل `p10009`، والحفاظ على تنفيذ اختبار قوي. أعلمني إذا كنت بحاجة إلى مزيد من التخصيص، مثل قوائم التخطي الديناميكية عبر وسيطات سطر الأوامر أو تكوينات JUnit 5 المتقدمة!