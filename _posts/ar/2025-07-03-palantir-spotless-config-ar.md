---
audio: false
generated: true
lang: ar
layout: post
title: تهيئة بالانتير جافا فورمات مع سبوتليس
translated: true
type: note
---

لتكوين **Palantir Java Format** مع **Spotless Maven Plugin** في ملف `pom.xml`، تحتاج إلى إعداد الإضافة لاستخدام `palantirJavaFormat` وتحديد خيارات التنسيق مثل مسافة الجدولة، والمسافة البادئة، وترتيب الاستيراد، والإعدادات الأخرى. فيما يلي دليل مفصل حول كيفية تكوين هذه الإعدادات والخيارات المتاحة بناءً على إضافة Spotless وPalantir Java Format.

### إضافة Spotless Maven Plugin مع Palantir Java Format

قم بتضمين Spotless Maven Plugin في ملف `pom.xml` وقم بتكوينه لاستخدام `palantirJavaFormat`. إليك الإعداد الأساسي مع التكوينات الشائعة لمسافة الجدولة، والمسافة البادئة، وترتيب الاستيراد، والخيارات الأخرى:

```xml
<plugin>
    <groupId>com.diffplug.spotless</groupId>
    <artifactId>spotless-maven-plugin</artifactId>
    <version>2.43.0</version> <!-- استخدم أحدث إصدار -->
    <configuration>
        <java>
            <!-- حدد الملفات المراد تنسيقها (اختياري، الافتراضي هو جميع ملفات .java) -->
            <includes>
                <include>src/main/java/**/*.java</include>
                <include>src/test/java/**/*.java</include>
            </includes>
            <!-- Palantir Java Format -->
            <palantirJavaFormat>
                <version>2.53.0</version> <!-- حدد الإصدار المطلوب -->
                <style>GOOGLE</style> <!-- الخيارات: GOOGLE, AOSP, أو PALANTIR -->
                <formatJavadoc>true</formatJavadoc> <!-- اختياري: تنسيق Javadoc -->
            </palantirJavaFormat>
            <!-- إعدادات المسافة البادئة -->
            <indent>
                <tabs>true</tabs> <!-- استخدم الجداول بدلاً من المسافات -->
                <spacesPerTab>4</spacesPerTab> <!-- عدد المسافات لكل جدولة -->
            </indent>
            <!-- تكوين ترتيب الاستيراد -->
            <importOrder>
                <order>java,javax,org,com,\\#</order> <!-- ترتيب استيراد مخصص -->
            </importOrder>
            <!-- إزالة الواردات غير المستخدمة -->
            <removeUnusedImports/>
            <!-- إعدادات اختيارية أخرى -->
            <trimTrailingWhitespace/>
            <endWithNewline/>
            <toggleOffOn/> <!-- تمكين علامات spotless:off و spotless:on -->
        </java>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>apply</goal> <!-- تنسيق الكود تلقائياً -->
            </goals>
            <phase>validate</phase> <!-- التشغيل خلال مرحلة التحقق -->
        </execution>
    </executions>
</plugin>
```

### شرح خيارات التكوين

إليك تفصيل الخيارات الرئيسية لتكوين قسم `java` في Spotless مع `palantirJavaFormat`، مع التركيز على مسافة الجدولة، والمسافة البادئة، وترتيب الاستيراد، والإعدادات الأخرى ذات الصلة:

#### 1. **Palantir Java Format (`<palantirJavaFormat>`)**

- **`<version>`**: يحدد إصدار `palantir-java-format` المستخدم. تحقق من أحدث إصدار على [Maven Repository](https://mvnrepository.com/artifact/com.palantir.java-format/palantir-java-format) أو [GitHub](https://github.com/palantir/palantir-java-format/releases). مثال: `<version>2.53.0</version>`.
- **`<style>`**: يحدد نمط التنسيق. الخيارات هي:
  - `GOOGLE`: يستخدم Google Java Style (مسافة بادئة بمقدار 2 مسافة، حد سطر 100 حرف).
  - `AOSP`: يستخدم نمط مشروع Android Open Source (مسافة بادئة بمقدار 4 مسافات، حد سطر 100 حرف).
  - `PALANTIR`: يستخدم نمط Palantir (مسافة بادئة بمقدار 4 مسافات، حد سطر 120 حرف، تنسيق متوافق مع lambda).[](https://github.com/palantir/palantir-java-format)
- **`<formatJavadoc>`**: قيمة منطقية لتمكين/تعطيل تنسيق Javadoc (يتطلب إصدار Palantir Java Format ≥ 2.39.0). مثال: `<formatJavadoc>true</formatJavadoc>`.[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
- **Custom Group Artifact**: نادرًا ما يكون مطلوبًا، ولكن يمكنك تحديد مجموعة ومُعرِّف مخصص للمنسق. مثال: `<groupArtifact>com.palantir.java-format:palantir-java-format</groupArtifact>`.

#### 2. **المسافة البادئة (`<indent>`)**

- **`<tabs>`**: قيمة منطقية لاستخدام الجداول (`true`) أو المسافات (`false`) للمسافة البادئة. مثال: `<tabs>true</tabs>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<spacesPerTab>`**: عدد المسافات لكل جدولة (يستخدم عندما يكون `<tabs>` هو `false` أو للمسافة البادئة المختلطة). القيم الشائعة هي `2` أو `4`. مثال: `<spacesPerTab>4</spacesPerTab>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
  - **ملاحظة**: قد يؤثر نمط Palantir Java Format (مثل `GOOGLE`, `AOSP`, `PALANTIR`) على سلوك المسافة البادئة. على سبيل المثال، `GOOGLE` يستخدم افتراضيًا مسافتين، بينما `AOSP` و `PALANTIR` يستخدمان 4 مسافات. يمكن لإعدادات `<indent>` في Spotless تجاوز هذه الإعدادات الافتراضية أو استكمالها، ولكن تأكد من الاتساق لتجنب التعارضات.[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)

#### 3. **ترتيب الاستيراد (`<importOrder>`)**

- **`<order>`**: يحدد ترتيب مجموعات الاستيراد، مفصولة بفواصل. استخدم `\\#` للواردات الثابتة وسلسلة فارغة (`""`) للواردات غير المحددة. مثال: `<order>java,javax,org,com,\\#</order>` يرتب الواردات التي تبدأ بـ `java`، ثم `javax`، إلخ، مع الواردات الثابتة في النهاية.[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
- **`<file>`**: بدلاً من ذلك، حدد ملفًا يحتوي على ترتيب الاستيراد. مثال: `<file>${project.basedir}/eclipse.importorder</file>`. تنسيق الملف يطابق تكوين ترتيب استيراد Eclipse (مثال: `java|javax|org|com|\\#`).[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)
  - مثال محتوى الملف:
    ```
    #sort
    java
    javax
    org
    com
    \#
    ```

#### 4. **إعدادات مفيدة أخرى**

- **`<removeUnusedImports>`**: يزيل الواردات غير المستخدمة. اختياريًا، حدد المحرك:
  - الافتراضي: يستخدم `google-java-format` للإزالة.
  - البديل: `<engine>cleanthat-javaparser-unnecessaryimport</engine>` للتتوافق مع JDK8+ وميزات Java الجديدة (مثل Java 17).[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)
- **`<trimTrailingWhitespace>`**: يزيل المسافات الزائدة في نهاية الأسطر. مثال: `<trimTrailingWhitespace/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<endWithNewline>`**: يضمن أن تنتهي الملفات بأسطر جديدة. مثال: `<endWithNewline/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<toggleOffOn>`**: يمكّن التعليقات `// spotless:off` و `// spotless:on` لاستبعاد أقسام من الكود من التنسيق. مثال: `<toggleOffOn/>`.[](https://dev.to/ankityadav33/standardize-code-formatting-with-spotless-2bdh)
- **`<licenseHeader>`**: يضيف رأس ترخيص إلى الملفات. مثال:
  ```xml
  <licenseHeader>
      <content>/* (C) $YEAR */</content>
  </licenseHeader>
  ```
  يمكنك أيضًا استخدام ملف: `<file>${project.basedir}/license.txt</file>`.[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<formatAnnotations>`**: يضمن أن تكون شروح النوع على نفس السطر مثل الحقول التي تصفها. مثال: `<formatAnnotations/>`.[](https://www.baeldung.com/java-maven-spotless-plugin)
- **`<ratchetFrom>`**: يحد التنسيق للملفات التي تم تغييرها بالنسبة لفرع Git (مثال: `origin/main`). مثال: `<ratchetFrom>origin/main</ratchetFrom>`.[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)

#### 5. **تنسيق POM المحدد (`<pom>`)**

لتنسيق ملف `pom.xml` نفسه، استخدم قسم `<pom>` مع `sortPom`:
```xml
<pom>
    <sortPom>
        <nrOfIndentSpace>2</nrOfIndentSpace> <!-- المسافة البادئة لـ POM -->
        <predefinedSortOrder>recommended_2008_06</predefinedSortOrder> <!-- ترتيب POM القياسي -->
        <sortDependencies>groupId,artifactId</sortDependencies> <!-- ترتيب التبعيات -->
        <sortPlugins>groupId,artifactId</sortPlugins> <!-- ترتيب الإضافات -->
        <endWithNewline>true</endWithNewline>
    </sortPom>
</pom>
```
- **خيارات `sortPom`**:
  - `<nrOfIndentSpace>`: عدد المسافات للمسافة البادئة (مثال: `2` أو `4`).
  - `<predefinedSortOrder>`: خيارات مثل `recommended_2008_06` أو `custom_1` لترتيب العناصر.[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)
  - `<sortDependencies>`: الترتيب حسب `groupId`, `artifactId`، أو معايير أخرى.
  - `<sortPlugins>`: ترتيب الإضافات بشكل مشابه.
  - `<endWithNewline>`: التأكد من انتهاء POM بأسطر جديدة.
  - `<expandEmptyElements>`: توسيع علامات XML الفارغة (مثال: `<tag></tag>` مقابل `<tag/>`).[](https://github.com/diffplug/spotless/blob/main/plugin-gradle/README.md)

### تشغيل Spotless

- **التحقق من التنسيق**: `mvn spotless:check` – يتحقق من الكود مقابل القواعد المكونة، مما يؤدي إلى فشل البناء إذا تم العثور على مخالفات.
- **تطبيق التنسيق**: `mvn spotless:apply` – يقوم بتنسيق الكود تلقائيًا للامتثال للقواعد.

### ملاحظات وأفضل الممارسات

- **الاتساق مع بيئة التطوير**: لمحاذاة IntelliJ أو Eclipse مع Spotless، قم بتثبيت إضافة IntelliJ `palantir-java-format` أو استخدم ملف XML لمنسق Eclipse. بالنسبة لـ IntelliJ، قم باستيراد ملف نمط متوافق (مثال: `intellij-java-google-style.xml` لنمط Google) أو قم بالتكوين يدويًا لمطابقة إعدادات Palantir.[](https://plugins.jetbrains.com/plugin/13180-palantir-java-format)
- **توافق الإصدار**: تأكد من أن إصدار `palantir-java-format` يدعم إصدار Java الخاص بك. بالنسبة لـ Java 17+، استخدم إصدارًا حديثًا (مثال: 2.53.0). بعض الميزات مثل pattern matching قد يكون لها دعم محدود.[](https://www.reddit.com/r/java/comments/1g8zu8c/codestyle_and_formatters/)
- **التنسيق المخصص**: للتخصيص المتقدم، استخدم ملف XML لمنسق Eclipse مع `<eclipse>` بدلاً من `<palantirJavaFormat>`:
  ```xml
  <eclipse>
      <file>${project.basedir}/custom-style.xml</file>
  </eclipse>
  ```
  مثال `custom-style.xml`:
  ```xml
  <?xml version="1.0" encoding="utf-8"?>
  <profiles version="21">
      <profile kind="CodeFormatterProfile" name="custom" version="21">
          <setting id="org.eclipse.jdt.core.formatter.tabulation.char" value="space"/>
          <setting id="org.eclipse.jdt.core.formatter.indentation.size" value="4"/>
          <setting id="org.eclipse.jdt.core.formatter.tabulation.size" value="4"/>
      </profile>
  </profiles>
  ```
  [](https://www.baeldung.com/java-maven-spotless-plugin)
- **القيود**: Palantir Java Format أقل قابلية للتكوين من منسق Eclipse ولكنه مصمم للاتساق وميزات Java الحديثة (مثل lambdas). قد لا يتعامل مع جميع الحالات المتطرفة (مثل lambdas المتداخلة بعمق).[](https://www.reddit.com/r/java/comments/18z151f/strict_code_formatter/)

### ملخص الخيارات المتاحة

| **الخيار**                  | **الوصف**                                                                 | **قيم المثال**                              |
|-----------------------------|---------------------------------------------------------------------------------|------------------------------------------------|
| `<palantirJavaFormat>`      | يكوّن Palantir Java Format.                                                | `<version>2.53.0</version>`, `<style>PALANTIR</style>` |
| `<indent>`                  | يضبط نمط المسافة البادئة (جداول أو مسافات) والحجم.                               | `<tabs>true</tabs>`, `<spacesPerTab>4</spacesPerTab>` |
| `<importOrder>`             | يحدد ترتيب مجموعة الاستيراد أو يستخدم ملفًا.                                      | `<order>java,javax,org,com,\\#</order>`        |
| `<removeUnusedImports>`     | يزيل الواردات غير المستخدمة، مع محرك اختياري.                                   | `<engine>cleanthat-javaparser-unnecessaryimport</engine>` |
| `<trimTrailingWhitespace>`  | يزيل المسافات الزائدة في النهاية.                                                   | `<trimTrailingWhitespace/>`                    |
| `<endWithNewline>`         | يضمن انتهاء الملفات بأسطر جديدة.                                              | `<endWithNewline/>`                           |
| `<toggleOffOn>`            | يمكّن علامات `spotless:off`/`spotless:on`.                                     | `<toggleOffOn/>`                              |
| `<licenseHeader>`          | يضيف رأس ترخيص.                                                         | `<content>/* (C) $YEAR */</content>`           |
| `<formatAnnotations>`       | ينسق الشروح لتكون على نفس السطر مثل الحقول.                          | `<formatAnnotations/>`                         |
| `<sortPom>`                | ينسق `pom.xml` مع الترتيب والمسافة البادئة.                                | `<nrOfIndentSpace>2</nrOfIndentSpace>`        |

### المصادر

- وثائق Spotless Maven Plugin: [GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)[](https://github.com/diffplug/spotless/blob/main/plugin-maven/README.md)
- Palantir Java Format: [GitHub](https://github.com/palantir/palantir-java-format)[](https://github.com/palantir/palantir-java-format)
- أمثلة من Stack Overflow والمجتمع لتكوين Spotless[](https://stackoverflow.com/questions/50027892/override-google-java-format-with-spotless-maven-plugin)[](https://stackoverflow.com/questions/71339562/spotless-java-google-format-vs-intellij-import-file)[](https://stackoverflow.com/questions/77126927/spotless-eclipse-formatter-java-17-error-on-string-literals-removing-unu)

يضمن هذا التكوين تنسيق كود متسق مع Palantir Java Format، مخصص لتفضيلاتك فيما يتعلق بمسافة الجدولة، والمسافة البادئة، وترتيب الاستيراد. دعني أعرف إذا كنت بحاجة إلى مزيد من التوضيح أو خيارات إضافية!