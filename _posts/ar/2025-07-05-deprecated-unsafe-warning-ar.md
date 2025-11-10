---
audio: false
generated: true
lang: ar
layout: post
title: ترقية Guice لإصلاح تحذير الأمان
translated: true
type: note
---

التحذير الذي تراه:

```
WARNING: A terminally deprecated method in sun.misc.Unsafe has been called
WARNING: sun.misc.Unsafe::staticFieldBase has been called by com.google.inject.internal.aop.HiddenClassDefiner (file:/opt/homebrew/Cellar/maven/3.9.10/libexec/lib/guice-5.1.0-classes.jar)
WARNING: Please consider reporting this to the maintainers of class com.google.inject.internal.aop.HiddenClassDefiner
WARNING: sun.misc.Unsafe::staticFieldBase will be removed in a future release
```

هذا **تحذير من آلة جافا الافتراضية (JVM)**، وليس من الكود الخاص بك مباشرة. هذا يعني أن مكتبة تستخدمها (في هذه الحالة، Guice، وتحديدًا `guice-5.1.0-classes.jar`) تستدعي داخليًا دالة (`staticFieldBase`) من `sun.misc.Unsafe`.

`sun.misc.Unsafe` هو واجهة برمجة تطبيقات (API) داخلية في جافا، مخصصة للعمليات منخفضة المستوى داخل JDK نفسه. إنها ليست جزءًا من واجهة برمجة تطبيقات جافا القياسية ولا يُشجع على استخدامها لأنها يمكن أن تؤدي إلى سلوك غير مستقر أو غير محدد وهي عرضة للتغيير أو الإزالة في الإصدارات المستقبلية من جافا. تخبرك آلة جافا الافتراضية أن هذه الدالة بالذات "مهملة بشكل نهائي" وستتم إزالتها، مما يعني أنها ستؤدي في النهاية إلى توقف تطبيقك عن العمل إذا استمرت المكتبة في استخدامها دون بديل.

**كيف "تزيل" هذا التحذير:**

لا يمكنك "إزالته" مباشرة عن طريق تغيير الكود الخاص بك، لأن الاستخدام موجود داخل مكتبة طرف ثالث (Guice). إليك ما يمكنك فعله، مُرتب حسب الأفضلية:

1.  **ترقية Guice (موصى به بشدة):**
    الحل الأفضل والأكثر استدامة هو الترقية إلى إصدار أحدث من Guice لا يستخدم `sun.misc.Unsafe` أو انتقل إلى واجهات برمجة تطبيقات جافا القياسية مثل `VarHandle` (المقدمة في JDK 9) أو Foreign Function & Memory API (JEP 454، القياسي في JDK 22).

    بالنظر إلى الإصدار `guice-5.1.0-classes.jar`، يبدو أنك تستخدم Guice 5.1.0. تحقق من إصدارات Guice الرسمية ووثائقها للحصول على تحديات تعالج استخدام `sun.misc.Unsafe` على إصدارات جافا الأحدث. غالبًا ما يكون حافظو المكتبات على علم بهذه الإهمالات ويوفرون إصدارات محدثة.

      * **الإجراء:** قم بتعديل ملف `pom.xml` الخاص بك لاستخدام إصدار أحدث من Guice. ستحتاج إلى العثور على أحدث إصدار مستقر من Guice متوافق مع إصدار جافا الخاص بك (JDK 21 في حالتك).

    ```xml
    <dependency>
        <groupId>com.google.inject</groupId>
        <artifactId>guice</artifactId>
        <version>LATEST_GUICE_VERSION</version> </dependency>
    ```

    قد تحتاج إلى تضمين `guice-assistedinject` أو وحدات Guice أخرى إذا كان مشروعك يستخدمها.

2.  **كتم التحذير (حل مؤقت - غير موصى به على المدى الطويل):**
    بينما لا يجب أن تعتمد على هذا الحل على المدى الطويل، يمكنك كتم التحذير أثناء وقت التشغيل إذا كان تجميليًا بحتًا ولا يعيق وظيفة تطبيقك *في الوقت الحالي*. يتم ذلك عبر وسائط سطر أوامر JVM.

    بالنسبة لـ JDK 24 (الهدف الحالي لديك هو 21، ولكن من الجيد معرفة ذلك مع تقدم جافا)، الإعداد الافتراضي هو `warn`. لكتمه، يمكنك تعيينه صراحةً إلى `allow`:

    يمكنك إضافة هذا إلى إعدادات `exec-maven-plugin`:

    ```xml
    <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.0</version>
        <configuration>
            <executable>bash</executable>
            <arguments>
                <argument>-c</argument>
                <argument>java --add-opens java.base/sun.misc=ALL-UNNAMED --sun-misc-unsafe-memory-access=allow -cp ${project.build.directory}/classes com.lzw.solutions.uva.${problem}.Main &lt; src/main/resources/uva/${problem}/1.in</argument>
            </arguments>
        </configuration>
    </plugin>
    ```

    *تصحيح ذاتي:* التحذير الأساسي هو حول `sun.misc.Unsafe::staticFieldBase` الذي تم "إهماله نهائيًا"، وليس حول الوصول العاكس غير القانوني. لذلك، `--add-opens java.base/sun.misc=ALL-UNNAMED` قد لا يكون ضروريًا هنا ما لم تكن تحصل أيضًا على تحذيرات "Illegal reflective access". العلم الأكثر مباشرة للتحذير "المهمل نهائيًا" هو `--sun-misc-unsafe-memory-access=allow`.

    **ومع ذلك، هذا إصلاح مؤقت.** هذا العلم يخبر JVM ببساطة بالسماح باستخدام دوال `sun.misc.Unsafe` دون طباعة التحذير. إنه *لا يحل* المشكلة الأساسية المتمثلة في أن `sun.misc.Unsafe` سيتم إزالته في النهاية، وقد يتوقف تطبيقك عن العمل في إصدارات JDK المستقبلية.

3.  **الإبلاغ إلى حافظي Guice (مقترح مسبقًا من قبل التحذير):**
    يقترح التحذير نفسه "يرجى التفكير في الإبلاغ عن هذا إلى حافظي الصنف `com.google.inject.internal.aop.HiddenClassDefiner`." بينما تستخدم إصدارًا محددًا، إذا تمكنت من تأكيد أن هذه المشكلة مستمرة في أحدث إصدارات Guice (والذي من المفترض ألا تكون، لأنهم عادة ما يعالجون هذه المشكلات)، فإن الإبلاغ عنها سيكون مفيدًا للمجتمع.

**باختصار، أفضل مسار للعمل هو ترقية تبعية Guice الخاصة بك.** واجهة برمجة تطبيقات `sun.misc.Unsafe` هي هدف متحرك، والمكتبات تحتاج إلى التكيف مع واجهات برمجة التطبيقات الأحدث والأكثر أمانًا والمدعومة رسميًا من قبل جافا.