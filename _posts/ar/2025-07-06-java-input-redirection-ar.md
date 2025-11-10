---
audio: false
generated: true
lang: ar
layout: post
title: إعادة توجيه الإدخال في برامج جافا باستخدام مافن
translated: true
type: note
---

قد يكون توجيه الإدخال لبرامج `exec:java` صعبًا بعض الشيء لأن `exec:java` يشغل عملية Java داخل *نفس JVM* الخاصة بـ Maven. هذا يعني أنك لا يمكنك استخدام مشغلي إعادة التوجيه القياسية في Shell (`<`, `>`) بنفس الطريقة التي تستخدمها لعملية منفصلة.

ومع ذلك، لا يزال لديك بعض الخيارات لتوفير الإدخال لبرنامج `exec:java` الخاص بك:

## 1. الإدخال البرمجي (`System.in` القياسي)

الطريقة الأكثر مباشرة هي تصميم برنامج Java الخاص بك ليقرأ من `System.in` كالمعتاد. عند تشغيل `mvn exec:java`، أي شيء تكتبه في وحدة التحكم (console) سيتم توجيهه إلى `System.in` لبرنامج Java الخاص بك.

**برنامج Java مثال (`MyInputProgram.java`):**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.println("You are " + age + " years old.");

        scanner.close();
    }
}
```

**التشغيل من سطر الأوامر:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyInputProgram"
```

عند تشغيل هذا، ستبدأ Maven، ثم سيطالبك برنامجك بالإدخال. يمكنك الكتابة مباشرة في وحدة التحكم.

## 2. استخدام خاصية `exec.args` للإدخال (للحالات البسيطة)

إذا كان برنامجك يتوقع إدخالًا بسيطًا وغير تفاعلي، *قد* تتمكن من تمريره كوسيطة (argument)، ثم يقرأ برنامجك تلك الوسيطة بدلاً من `System.in`. هذا ليس توجيه إدخال قياسي حقيقي، لكنه يخدم غرضًا مشابهًا للبيانات البسيطة.

**برنامج Java مثال (`MyArgProgram.java`):**

```java
package com.example.app;

public class MyArgProgram {
    public static void main(String[] args) {
        if (args.length > 0) {
            String inputData = args[0];
            System.out.println("Received input from argument: " + inputData);
        } else {
            System.out.println("No input argument provided.");
        }
    }
}
```

**التشغيل من سطر الأوامر:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="MyCustomInputString"
```

أو مع المسافات:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="\"Input with spaces\""
```

هذا النهج مناسب فقط إذا كان يمكن تعديل برنامجك لقبول "مدخلاته" كوسائط سطر أوامر.

## 3. إعادة توجيه الإدخال باستخدام إعادة توجيه Shell (مع `exec:exec`)

إذا كنت بحاجة مطلقة إلى إعادة توجيه الإدخال من ملف أو pipe، **يجب** استخدام هدف `exec:exec` بدلاً من `exec:java`. يقوم هدف `exec:exec` بإنشاء عملية منفصلة، مما يسمح لـ Shell بالتعامل مع إعادة توجيه الإدخال/الإخراج القياسي.

**تكوين `pom.xml` لـ `exec:exec`:**

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.yourcompany</groupId>
    <artifactId>my-maven-app</artifactId>
    <version>1.0-SNAPSHOT</version>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.2.0</version> <executions>
                    <execution>
                        <id>run-my-java-app</id>
                        <phase>package</phase> <goals>
                            <goal>exec</goal>
                        </goals>
                        <configuration>
                            <executable>java</executable>
                            <arguments>
                                <argument>-classpath</argument>
                                <classpath/> <argument>com.example.app.MyInputProgram</argument>
                                </arguments>
                            <workingDirectory>${project.build.directory}/classes</workingDirectory>
                            </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

</project>
```

**برنامج Java مثال (نفس `MyInputProgram.java` كما ورد أعلاه):**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        // بافتراض أنك تريد قراءة سطر آخر للعمر بعد الاسم
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.println("You are " + age + " years old.");

        scanner.close();
    }
}
```

**ملف الإدخال (`input.txt`):**

```
Alice
30
```

**التشغيل باستخدام `exec:exec` وإعادة توجيه الإدخال:**

أولاً، قم بترجمة (compile) مشروعك:

```bash
mvn compile
```

ثم، شغل هدف `exec:exec` وقم بإعادة توجيه الإدخال باستخدام Shell الخاص بك:

```bash
mvn exec:exec@run-my-java-app < input.txt
```

**الشرح:**

  * `mvn exec:exec@run-my-java-app`: ينفذ هدف `exec` لـ `exec-maven-plugin` بالـ `id` "run-my-java-app".
  * `< input.txt`: هذا مشغل إعادة توجيه قياسي في Shell. يخبر Shell الخاص بك بأخذ محتوى `input.txt` وتغذيته كإدخال قياسي للأمر الذي يتم تنفيذه (`java com.example.app.MyInputProgram`).

**ملاحظات مهمة لـ `exec:exec`:**

  * **`executable`:** تحدد `java` صراحةً كأمر قابل للتنفيذ.
  * **`arguments`:** تحتاج إلى بناء وسائط أمر `java` يدويًا، بما في ذلك `-classpath` و `mainClass`. علامة `<classpath/>` هي قيمة خاصة يستبدلها `exec-maven-plugin` بـ classpath الفعلي المحسوب لمشروعك.
  * **`workingDirectory`:** من المفيد غالبًا تعيين `workingDirectory` إلى `${project.build.directory}/classes` حتى يتمكن Java من العثور على ملفات `.class` المترجمة الخاصة بك.
  * **`outputFile` (اختياري):** يوفر `exec-maven-plugin` لـ `exec:exec` خيار تكوين `<outputFile>` لإعادة توجيه الإخراج القياسي والخطأ للبرنامج إلى ملف مباشرةً داخل تكوين الـ plugin، بدلاً من الاعتماد على إعادة التوجيه في Shell. يمكن أن يكون هذا مفيدًا للتسجيل (logging).

**باختصار:**

  * للإدخال التفاعلي حيث يقوم المستخدم بالكتابة مباشرة، يعمل `exec:java` و `System.in` بشكل جيد.
  * لتوفير الإدخال من ملف أو pipe، ستحتاج إلى التبديل إلى `exec:exec` والاستفادة من قدرات إعادة توجيه الإدخال في Shell الخاص بك (`<`).