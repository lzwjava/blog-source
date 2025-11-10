---
audio: false
generated: true
lang: ar
layout: post
title: تشغيل فئات جافا باستخدام Maven Exec
translated: true
type: note
---

هدف `exec:java` في إضافة Maven Exec هو طريقة قوية لتشغيل صنف جافا يحتوي على دالة `main` مباشرة من عملية بناء Mافن. ينفذ هذا الهدف صنف الجافا المحدد **داخل نفس JVM** التي تعمل فيها عملية بناء مافن، مستخدمًا تبعيات المشروع كمسار للفئات (classpath).

إليك كيفية استخدامه، مع سيناريوهات وأمثلة شائعة:

## 1. الاستخدام الأساسي من سطر الأوامر

أبسط طريقة لاستخدام `exec:java` هي مباشرة من سطر الأوامر، خاصة للاختبارات السريعة أو لتشغيل صنف أداة معين.

**الأمر:**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass"
```

**الشرح:**

  * `mvn exec:java`: يستدعي الهدف `java` الخاص بالإضافة `exec-maven-plugin`.
  * `-Dexec.mainClass="com.yourcompany.YourMainClass"`: تحدد خاصية النظام هذه الاسم المؤهل بالكامل لصنف الجافا الذي يحتوي على دالة `public static void main(String[] args)` التي تريد تنفيذها.

**مثال:**

لنفترض أن لديك الصنف `com.example.myapp.HelloWorld` بدالة `main`:

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
    }
}
```

يمكنك تشغيله باستخدام:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld"
```

**ملاحظة:** من الممارسات الجيدة تشغيل `mvn compile` أولاً لضمان ترجمة أصنافك قبل أن تحاول `exec:java` تشغيلها.

## 2. تمرير وسائط إلى برنامج الجافا الخاص بك

يمكنك تمرير وسائط إلى دالة `main` في برنامج الجافا الخاص بك باستخدام خاصية النظام `exec.args`:

**الأمر:**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass" -Dexec.args="arg1 arg2 \"arg with spaces\""
```

**مثال:**

إذا كان صنف `HelloWorld` الخاص بك كالتالي:

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
        if (args.length > 0) {
            System.out.println("Arguments received: ");
            for (String arg : args) {
                System.out.println("- " + arg);
            }
        }
    }
}
```

يمكنك تشغيله كالتالي:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="FirstArgument SecondArgument"
```

للوسائط التي تحتوي على مسافات، ضعها بين علامتي اقتباس:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="\"Hello World\" AnotherArg"
```

## 3. تهيئة `exec:java` في ملف `pom.xml`

للتهيئات الأكثر ديمومة أو الافتراضية، يمكنك إضافة `exec-maven-plugin` إلى ملف `pom.xml` الخاص بك. هذا يسمح لك بتعيين `mainClass` افتراضي ومعاملات أخرى، حتى لا تضطر إلى تحديدها في سطر الأوامر في كل مرة.

**تهيئة `pom.xml`:**

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.yourcompany</groupId>
    <artifactId>my-maven-app</artifactId>
    <version>1.0-SNAPSHOT</modelVersion>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.2.0</version> <executions>
                    <execution>
                        <goals>
                            <goal>java</goal>
                        </goals>
                    </execution>
                </executions>
                <configuration>
                    <mainClass>com.example.myapp.HelloWorld</mainClass>
                    <arguments>
                        <argument>defaultArg1</argument>
                        <argument>defaultArg2</argument>
                    </arguments>
                    <systemProperties>
                        <systemProperty>
                            <key>my.custom.property</key>
                            <value>someValue</value>
                        </systemProperty>
                    </systemProperties>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

</project>
```

**شرح خيارات التهيئة:**

  * `<groupId>org.codehaus.mojo</groupId>` و `<artifactId>exec-maven-plugin</artifactId>`: إحداثيات قياسية للإضافة.
  * `<version>3.2.0</version>`: حدد دائمًا إصدارًا حديثًا من الإضافة.
  * `<goals><goal>java</goal></goals>`: يربط هذا الهدف `java`. إذا لم تربطه بمرحلة محددة، سيتم تنفيذه عندما تستدعي `mvn exec:java` صراحةً.
  * `<mainClass>com.example.myapp.HelloWorld</mainClass>`: يحدد صنف main الافتراضي للتشغيل. إذا قمت بتشغيل `mvn exec:java` بدون `-Dexec.mainClass` في سطر الأوامر، سيتم استخدام هذا الصنف.
  * `<arguments>`: قائمة بالوسائط لتمريرها إلى دالة `main`. هذه وسائط افتراضية يمكن تجاوزها بواسطة `exec.args` في سطر الأوامر.
  * `<systemProperties>`: يسمح لك بتعريف خصائص نظام (`-Dkey=value`) ستكون متاحة لتطبيق الجافا الخاص بك عند تشغيل `exec:java`.

**التشغيل مع تهيئة `pom.xml`:**

بمجرد التهيئة في `pom.xml`:

  * للتشغيل بصنف main الافتراضي والوسائط:
    ```bash
    mvn compile exec:java
    ```
  * لتجاوز صنف main من سطر الأوامر:
    ```bash
    mvn compile exec:java -Dexec.mainClass="com.example.myapp.AnotherMainClass"
    ```
  * لتجاوز/إضافة وسائط من سطر الأوامر:
    ```bash
    mvn compile exec:java -Dexec.args="commandLineArg1 commandLineArg2"
    ```
    (ملاحظة: عادةً ما *يستبدل* `exec.args` الوسائط `arguments` المعرفة في `pom.xml` إذا تم توفيره في سطر الأوامر.)

## 4. الاختلافات الرئيسية عن `exec:exec`

من المهم فهم الفرق بين `exec:java` و `exec:exec`:

  * **`exec:java`**: يشغل برنامج الجافا **في نفس JVM** الخاصة بـ Maven. هذا بشكل عام أسرع لأنه يتجنب إنشاء عملية جديدة. يقوم تلقائيًا بإعداد تبعيات المشروع في مسار الفئات (classpath).
  * **`exec:exec`**: يشغل برنامجًا خارجيًا عشوائيًا (بما في ذلك `java` نفسه) **في عملية منفصلة**. هذا مفيد عندما تحتاج إلى تحديد ملف تنفيذي مختلف لجافا، أو تمرير وسائط JVM (مثل `-Xmx`)، أو تشغيل ملفات تنفيذية غير جافا. إذا استخدمت `exec:exec` لتشغيل برنامج جافا، فعادةً ما يتعين عليك بناء مسار الفئات يدويًا باستخدام `%classpath` في الوسائط.

لمعظم حالات تنفيذ تطبيقات الجافا القياسية ضمن عملية بناء Maven، يعتبر `exec:java` هو الخيار الأكثر ملاءمة.

## 5. اعتبارات مهمة

  * **مسار الفئات (Classpath):** يضمن `exec:java` تلقائيًا تضمين الأصناف المترجمة لمشروعك وتبعياته في مسار الفئات.
  * **وسائط JVM:** لأن `exec:java` يعمل في *نفس* JVM الخاصة بـ Maven، لا يمكنك تمرير وسائط JVM (مثل `-Xmx`، `-XX:MaxPermSize`) مباشرة إلى `exec:java` من خلال تهيئته أو `exec.args`. يجب تمرير هذه الوسائط إلى JVM الخاصة بـ Maven نفسها، عادةً عبر متغير البيئة `MAVEN_OPTS`:
    ```bash
    export MAVEN_OPTS="-Xmx1024m -Dsome.jvm.property=value"
    mvn exec:java ...
    ```
  * **System.exit():** إذا استدعى برنامج الجافا الخاص بك `System.exit()`، فسيؤدي ذلك إلى إنهاء عملية بناء Maven بأكملها، وليس برنامجك فقط. كن mindful لهذا عند استخدام `exec:java`. تحتوي الإضافة على خيار `blockSystemExit` (منذ الإصدار 3.2.0) يحاول منع هذا، ولكن من الأفضل تصميم دالة main الخاصة بك لتكتمل بشكل طبيعي دون استدعاء `System.exit()`.
  * **التبعيات:** يعتمد `exec:java` على تبعيات المشروع. إذا كنت بحاجة لتشغيل صنف من تبعية ليست جزءًا من بناء مشروعك، قد تحتاج إلى تعديل تهيئة الإضافة أو التفكير في استخدام `exec:exec` مع تعريف صريح لمسار الفئات.
  * **إصدار الإضافة:** استخدم دائمًا إصدارًا حديثًا من `exec-maven-plugin` للحصول على أحدث الميزات وإصلاحات الأخطاء. تحقق من موقع MojoHaus للحصول على أحدث المعلومات.