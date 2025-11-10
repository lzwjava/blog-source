---
audio: false
generated: true
lang: ar
layout: post
title: سبوتليس ضد تشيك ستايل في جافا
translated: true
type: note
---

يمكنك استخدام **Spotless Maven Plugin** و **Checkstyle Maven Plugin** معًا في مشروع جافا، حيث أنهما يخدمان أغراضًا متكاملة. ومع ذلك، فإن ما إذا كنت *تحتاج* إلى كليهما يعتمد على متطلبات مشروعك. أدناه، سأشرح كيف يمكنهما العمل معًا، والاختلافات بينهما، ومتى قد تختار أحدهما على الآخر.

### الاختلافات الرئيسية بين Spotless و Checkstyle

| **الوجه**            | **Spotless**                                                                 | **Checkstyle**                                                              |
|-----------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **الغرض**           | يقوم بتنسيق الكود تلقائيًا لفرض نمط متسق وإصلاح المشكلات.   | يحلل الكود بشكل ثابت لفرض معايير البرمجة واكتشاف المخالفات.  |
| **الإجراء**            | يعدل الكود (مثل إصلاح المسافات البادئة، ترتيب الاستيراد، إزالة الاستيرادات غير المستخدمة). | يبلغ عن المخالفات دون تعديل الكود؛ يفشل عملية البناء إذا فشلت الفحوصات.      |
| **التكوين**     | يقوم بتكوين أدوات التنسيق مثل `palantir-java-format`، `google-java-format`، إلخ. | يستخدم مجموعة قواعد (مثل Google أو Sun checks) لتحديد معايير البرمجة.      |
| **المخرجات**            | ملفات المصدر المنسقة (مع `mvn spotless:apply`).                          | تقارير (XML، HTML، أو console) تسرد مخالفات النمط.                   |
| **حالة الاستخدام**          | يضمن أن الكود منسق بشكل متسق قبل العمليات commit أو build.             | يفرض معايير البرمجة ويمسك بقضايا مثل التعقيد أو الممارسات السيئة. |

### استخدام Spotless و Checkstyle معًا

يمكنك الجمع بين Spotless و Checkstyle لتحقيق كل من **التنسيق التلقائي** و **فرض النمط**. إليك كيف يكمل كل منهما الآخر:

1.  **Spotless للتنسيق**:
    *   يطبق Spotless قواعد التنسيق (مثل المسافات البادئة، ترتيب الاستيراد) باستخدام أدوات مثل `palantir-java-format`.
    *   يضمن أن الكود منسق بشكل متسق، مما يقلل الجهد اليدوي.
    *   مثال: يصلح المسافات البادئة 2 مسافة مقابل 4 مسافات، يرتب الاستيرادات، ويزيل الاستيرادات غير المستخدمة.

2.  **Checkstyle للتحقق**:
    *   يفرض Checkstyle معايير البرمجة التي تتجاوز التنسيق، مثل طول الدالة، تسمية المتغيرات، أو التعقيد.
    *   يمسك بالقضايا التي قد لا تعالجها أدوات التنسيق، مثل Javadoc المفقود أو الدوال المعقدة للغاية.
    *   مثال: يشير إلى دالة بها عدد كبير جدًا من المعلمات أو يفرض وجود Javadoc على الدوال العامة.

3.  **سير العمل**:
    *   قم بتشغيل Spotless أولاً (`mvn spotless:apply`) لتنسيق الكود.
    *   ثم قم بتشغيل Checkstyle (`mvn checkstyle:check`) للتحقق من الامتثال للقواعد الإضافية.
    *   هذا يضمن أن الكود منسق ويتبع أيضًا إرشادات النمط الأوسع.

### مثال على التكوين في `pom.xml`

إليك كيفية تكوين كلا الإضافتين في ملف `pom.xml` الخاص بك:

```xml
<build>
    <plugins>
        <!-- Spotless Plugin for Formatting -->
        <plugin>
            <groupId>com.diffplug.spotless</groupId>
            <artifactId>spotless-maven-plugin</artifactId>
            <version>2.43.0</version>
            <configuration>
                <java>
                    <includes>
                        <include>src/main/java/**/*.java</include>
                        <include>src/test/java/**/*.java</include>
                    </includes>
                    <palantirJavaFormat>
                        <version>2.53.0</version>
                        <style>GOOGLE</style> <!-- Use Google style -->
                    </palantirJavaFormat>
                    <indent>
                        <spacesPerTab>2</spacesPerTab> <!-- 2-space indentation -->
                    </indent>
                    <importOrder>
                        <order>java,javax,org,com,\\#</order>
                    </importOrder>
                    <removeUnusedImports/>
                    <trimTrailingWhitespace/>
                    <endWithNewline/>
                </java>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>apply</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
        </plugin>

        <!-- Checkstyle Plugin for Validation -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.4.0</version>
            <configuration>
                <configLocation>google_checks.xml</configLocation> <!-- Use Google style or custom XML -->
                <includeTestSourceDirectory>true</includeTestSourceDirectory>
                <failOnViolation>true</failOnViolation> <!-- Fail build on violations -->
                <consoleOutput>true</consoleOutput> <!-- Output violations to console -->
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>check</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
            <dependencies>
                <!-- Specify Checkstyle version -->
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version>
                </dependency>
            </dependencies>
        </plugin>
    </plugins>
</build>
```

### ملاحظات تكوين رئيسية

1.  **قواعد النمط المشتركة**:
    *   لتجنب التعارضات، قم بمحاذاة تكوينات Spotless و Checkstyle. على سبيل المثال، استخدم `palantirJavaFormat` مع `style>GOOGLE` في Spotless و `google_checks.xml` في Checkstyle.
    *   قم بتنزيل `google_checks.xml` من [Checkstyle’s GitHub](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml) أو أنشئ مجموعة قواعد مخصصة.

2.  **ترتيب التنفيذ**:
    *   قم بتشغيل Spotless قبل Checkstyle في مرحلة `validate` لضمان تنسيق الكود قبل التحقق منه.
    *   مثال: `mvn spotless:apply checkstyle:check`.

3.  **قواعد Checkstyle مخصصة**:
    *   قم بتخصيص `google_checks.xml` أو أنشئ ملفك الخاص (مثل `my_checks.xml`) لفرض قواعد محددة، مثل:
        ```xml
        <module name="Indentation">
            <property name="basicOffset" value="2"/>
            <property name="lineWrappingIndentation" value="4"/>
        </module>
        <module name="ImportOrder">
            <property name="groups" value="java,javax,org,com"/>
            <property name="ordered" value="true"/>
            <property name="separated" value="true"/>
        </module>
        ```

4.  **تجنب التكرار**:
    *   إذا كان Spotless يتعامل مع التنسيق (مثل المسافات البادئة، ترتيب الاستيراد)، قم بتعطيل قواعد Checkstyle المتداخلة لتجنب الفحوصات المكررة. على سبيل المثال، عطل وحدة `Indentation` في Checkstyle إذا كان Spotless يفرض المسافات البادئة:
        ```xml
        <module name="Indentation">
            <property name="severity" value="ignore"/>
        </module>
        ```

### متى تستخدم أحدهما مقابل كلاهما

*   **استخدم Spotless بمفرده**:
    *   إذا كنت تحتاج فقط إلى تنسيق كود متسق (مثل المسافات البادئة، ترتيب الاستيراد، المسافات البيضاء).
    *   مثالي للفرق التي تريد تنسيقًا آليًا دون فرض صارم للنمط.
    *   مثال: المشاريع الصغيرة أو الفرق التي تستخدم التنسيق المعتمد على IDE.

*   **استخدم Checkstyle بمفرده**:
    *   إذا كنت تحتاج إلى فرض معايير البرمجة (مثل تسمية المتغيرات، Javadoc، تعقيد الدالة) دون تعديل الكود.
    *   مناسب للمشاريع حيث يقوم المطورون بتنسيق الكود يدويًا ولكنهم بحاجة إلى التحقق منه.

*   **استخدم كلاهما**:
    *   لجودة كود قوية: يقوم Spotless بتنسيق الكود تلقائيًا، ويمسك Checkstyle بمشكلات إضافية (مثل Javadoc المفقود، الدوال المعقدة).
    *   شائع في الفرق الكبيرة أو المشاريع ذات معايير البرمجة الصارمة.
    *   مثال: المشاريع enterprise أو المستودعات مفتوحة المصدر التي تتطلب نمطًا متسقًا وفحوصات جودة.

### اعتبارات عملية

*   **الأداء**: تشغيل كلا الإضافتين يزيد من وقت البناء. استخدم `spotless:check` (بدلاً من `apply`) و `checkstyle:check` في خطوط أنابيب CI للتحقق دون تعديل الكود.
*   **دمج IDE**:
    *   Spotless: استخدم مهام Spotless Gradle/Maven أو إضافات IDE (مثل `palantir-java-format` لـ IntelliJ).
    *   Checkstyle: استخدم إضافة Checkstyle-IDEA لـ IntelliJ أو إضافة Eclipse Checkstyle، مع تكوينها بنفس `google_checks.xml`.
*   **CI/CD**: قم بتكوين كلا الإضافتين في خط أنابيب CI الخاص بك (مثل Jenkins، GitHub Actions) لفرض التنسيق وفحوصات النمط على طلبات السحب.
    ```yaml
    # Example GitHub Actions workflow
    name: CI
    on: [pull_request]
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3
          - name: Set up JDK 17
            uses: actions/setup-java@v3
            with: { java-version: '17' }
          - name: Run Spotless and Checkstyle
            run: mvn spotless:check checkstyle:check
    ```

### تعارضات محتملة وحلول

*   **قواعد متداخلة**: إذا قام Spotless بتنسيق الكود بشكل مختلف عن قواعد Checkstyle (مثل مسافات بادئة 2 مقابل 4 مسافات)، قد تفشل عمليات البناء. الحل: محاذاة التكوينات (مثل استخدام نمط `GOOGLE` لكليهما).
*   **فشل البناء**: `failOnViolation` في Checkstyle يمكن أن يعطل عمليات البناء إذا لم يعمل Spotless أولاً. الحل: تأكد من تشغيل Spotless أولاً أو استخدم `spotless:check` للتحقق من التنسيق.
*   **تبني الفريق**: قد يقاوم المطورون التنسيق التلقائي. الحل: استخدم `spotless:check` في CI وقم بتوعية الفريق حول دمج IDE.

### المصادر

*   Spotless Documentation: [GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)
*   Checkstyle Maven Plugin: [Maven Site](https://maven.apache.org/plugins/maven-checkstyle-plugin/)
*   مناقشات المجتمع على Stack Overflow وقضايا GitHub

### خاتمة

يعد استخدام Spotless و Checkstyle معًا مزيجًا قويًا للحفاظ على جودة الكود: يضمن Spotless تنسيقًا متسقًا، بينما يفرض Checkstyle معايير برمجة أوسع. قم بتكوينهما ليتوافقا (مثل نفس قواعد المسافات البادئة وترتيب الاستيراد) وقم بتشغيلهما بالتسلسل في عملية البناء الخاصة بك. إذا كان مشروعك يحتاج فقط إلى التنسيق، فقد يفي Spotless بمفرده؛ إذا كنت تحتاج إلى تحقق صارم، ففكر في إضافة Checkstyle. دعني أعرف إذا كنت بحاجة إلى مساعدة في تكوينات محددة أو ملف `google_checks.xml` نموذجي!