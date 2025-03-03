---
audio: false
generated: true
lang: ar
layout: post
title: مُبَادِرَةُ مَجِن
translated: true
---

ال`builder-helper-maven-plugin`، المعروف الآن باسم **Build Helper Maven Plugin**، هو أداة متعددة الاستخدامات مصممة لمساعدتك في مختلف المهام في دورة حياة بناء Maven. كان مستضيفًا سابقًا تحت Codehaus، والآن يتم صيانته بواسطة MojoHaus، على الرغم من أن إحداثيات Maven الخاصة به لا تزال تستخدم معرف المجموعة `org.codehaus.mojo`. يوفر هذا الوصف مجموعة من الأهداف لمساعدتك في العمليات مثل إضافة مجلدات مصدر إضافية، ملحق ملفات إضافية، تحليل معلومات الإصدار، وغيرها. أدناه، سأرشدك في كيفية استخدام هذا الوصف في مشروع Maven الخاص بك.

### ما هو Maven؟
قبل الغوص في الوصف، دعونا نضع السياق. Maven هو أداة لتوظيف بناء شائعة الاستخدام بشكل أساسي لمشاريع Java. يسهّل ويوحيد عملية البناء من خلال إدارة الاعتماديات، وتجميع الكود، وتعبئة التطبيقات، وغيرها، جميعها يتم تهيئتها من خلال ملف مركزي يسمى `pom.xml`.

### الخطوة 1: تضمين الوصف في ملف `pom.xml` الخاص بك
لاستخدام Build Helper Maven Plugin، عليك إضافة إلى ملف `pom.xml` لمشروع Maven الخاص بك ضمن القسم `<build><plugins>`. إليك كيفية القيام بذلك:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <!-- سيتم إضافة تنفيذات للأهداف المحددة هنا -->
        </plugin>
    </plugins>
</build>
```

- **Group ID**: `org.codehaus.mojo` (يعكس أصولها، على الرغم من أنها الآن تحت MojoHaus).
- **Artifact ID**: `build-helper-maven-plugin`.
- **Version**: اعتبارًا من آخر تحديث لي، `3.6.0` هو أحدث إصدار، ولكن يجب عليك التحقق من [Maven Central](https://mvnrepository.com/artifact/org.codehaus.mojo/build-helper-maven-plugin) للحصول على الإصدار الأحدث.

تجعل هذه الإعلان الوصف متاحًا في مشروعك، ولكن لن يفعل شيئًا حتى تتهيأ أهداف محددة.

### الخطوة 2: تهيئة تنفيذات للأهداف المحددة
يوفر Build Helper Maven Plugin أهدافًا متعددة، كل منها مصمم لمهمة معينة. تتهيئ هذه الأهداف من خلال إضافة كتلة `<executions>` داخل إعلان الوصف، وتحديد متى يجب أن تجري (من خلال مرحلة دورة حياة Maven) وكيف يجب أن تتصرف.

هنا بعض الأهداف الشائعة المستخدمة وأغراضها:

- **`add-source`**: يضيف مجلدات مصدر إضافية لمشروعك.
- **`add-test-source`**: يضيف مجلدات مصدر اختبار إضافية.
- **`add-resource`**: يضيف مجلدات موارد إضافية.
- **`attach-artifact`**: يلحق ملفات إضافية (مثل الملفات) لمشروعك للاستخدام والتوزيع.
- **`parse-version`**: يحلل إصدار المشروع ويضع الخصائص (مثل الإصدارات الرئيسية، الثانوية، المتزايدة).

تطلب كل هدف تهيئة خاصة، وتحددها داخل كتلة `<execution>`.

### الخطوة 3: مثال – إضافة مجلد مصدر إضافي
من الحالات الشائعة لهذا الوصف هو إضافة مجلد مصدر إضافي، حيث يدعم Maven عادةً مجلدًا واحدًا فقط بشكل افتراضي (`src/main/java`). إليك كيفية تهيئة هدف `add-source` لإضافة مجلد مصدر إضافي:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>build-helper-maven-plugin</artifactId>
            <version>3.6.0</version>
            <executions>
                <execution>
                    <id>add-source</id>
                    <phase>generate-sources</phase>
                    <goals>
                        <goal>add-source</goal>
                    </goals>
                    <configuration>
                        <sources>
                            <source>path/to/your/extra/source/directory</source>
                        </sources>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`<id>`**: معرف فريد لهذا التنفيذ (مثل `add-source`).
- **`<phase>`**: مرحلة دورة حياة Maven التي يجري فيها الهدف (مثل `generate-sources` يضمن أن يتم إضافة المجلد مبكرًا في البناء).
- **`<goals>`**: يحدد الهدف الذي سيتم تنفيذه (`add-source` في هذا المثال).
- **`<configuration>`**: يحدد مجلد المصدر الإضافي (قم بإعادة `path/to/your/extra/source/directory` بمسارك الفعلي، مثل `src/main/generated`).

عندما تجرى أمر Maven مثل `mvn compile`، سيشمل Maven هذا المجلد الإضافي كملف مصدر.

### ملاحظات إضافية
- **التوافق مع الإصدار**: منذ الإصدار 3.0.0، يتطلب الوصف Maven 3 أو أعلى. إذا كنت تستخدم إصدارًا أقدم من Maven، فسيكون عليك استخدام إصدار الوصف 1.12 أو أقدم.
- **أهداف متعددة**: يمكنك تعريف عدة كتلة `<execution>` داخل الوصف نفسه لتنفيذ أهداف مختلفة. على سبيل المثال، يمكنك إضافة مجلدات المصدر والاختبار من خلال تضمين تنفيذات لأهداف `add-source` و `add-test-source`.
- **تنفيد الوصف**: بعد التهيئة، ستنفذ أهداف الوصف أثناء المراحل المحددة عند تشغيل أمر Maven (مثل `mvn clean install`).

### موارد إضافية
للحصول على مزيد من التفاصيل والمثالات لأهداف أخرى، راجع الصفحة الرسمية [usage page](https://www.mojohaus.org/build-helper-maven-plugin/usage.html). توفر هذه الصفحة توثيقًا شاملًا ومثالات تهيئة لجميع الأهداف المتاحة.

### الملاحظات النهائية
Build Helper Maven Plugin هو إضافة قوية إلى أدوات Maven الخاصة بك، خاصة لمشاريع تتطلب تهيئات بناء غير قياسية. من خلال تضمينه في `pom.xml` وتهيئة الأهداف المناسبة، يمكنك تعديل عملية البناء الخاصة بك لتتوافق مع احتياجاتك الخاصة. على الرغم من أن أصله كان تحت Codehaus، فإن منزله الحالي هو MojoHaus، ويبقى خيارًا موثوقًا لتحسين عمليات بناء Maven.