---
audio: false
generated: true
lang: ar
layout: post
title: إضافة إمافن التنفيذية
translated: true
type: note
---

لاستخدام إضافة `org.codehaus.mojo` Exec Maven Plugin في مشروع Maven الخاص بك، تحتاج إلى تكوينها في ملف `pom.xml` الخاص بك وتقرر كيف تريد تنفيذ البرامج—إما أوامر خارجية أو برامج Java—خلال عملية البناء. توفر الإضافة هدفين رئيسيين: `exec:exec` لتشغيل البرامج الخارجية و `exec:java` لتنفيذ فئات Java. أدناه، سأرشدك خلال الخطوات لإعدادها واستخدامها بفعالية.

### الخطوة 1: إضافة الإضافة إلى ملف `pom.xml` الخاص بك
أولاً، قم بتضمين Exec Maven Plugin في قسم `<build><plugins>` في ملف `pom.xml` الخاص بك. حدد `groupId`، و `artifactId`، وإصدار (أحدث إصدار حالياً هو `3.1.0`):

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
        </plugin>
    </plugins>
</build>
```

هذا يضيف الإضافة إلى مشروعك، لكنها لن تفعل أي شيء بعد حتى تقوم بتكوينها أو تشغيل أهدافها يدوياً.

### الخطوة 2: اختر هدفك
تقدم الإضافة هدفين أساسيين:
- **`exec:exec`**: ينفذ أي برنامج خارجي (مثل نصوص shell، أو الملفات الثنائية، أو حتى أمر `java`).
- **`exec:java`**: يشغل فئة Java تحتوي على دالة `main` من مشروعك في نفس JVM الذي يعمل فيه Maven.

يمكنك استخدام هذه الأهداف إما بتشغيلها يدوياً من سطر الأوامر (مثل `mvn exec:exec`) أو بربطها بمرحلة محددة في دورة حياة بناء Maven.

### الخيار 1: تشغيل برنامج Java باستخدام `exec:java`
إذا كنت تريد تنفيذ فئة Java من مشروعك، استخدم هدف `exec:java`. هذا مثالي لتشغيل دالة `main` في فئة هي جزء من مشروعك، مستفيداً تلقائياً من classpath وقت التشغيل للمشروع (بما في ذلك التبعيات).

#### التنفيذ اليدوي
أضف تكويناً لتحديد الفئة الرئيسية:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <mainClass>com.example.Main</mainClass>
            </configuration>
        </plugin>
    </plugins>
</build>
```

ثم، شغله من سطر الأوامر:

```bash
mvn exec:java
```

هذا ينفذ `com.example.Main` في نفس JVM الذي يعمل فيه Maven، وراثاً إعدادات JVM الخاصة بـ Maven.

#### التنفيذ التلقائي أثناء البناء
لتشغيله تلقائياً خلال مرحلة بناء (مثل `test`)، استخدم قسم `<executions>`:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-my-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>java</goal>
                    </goals>
                    <configuration>
                        <mainClass>com.example.Main</mainClass>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

الآن، عندما تشغل `mvn test`، سيتم تنفيذ فئة `com.example.Main` خلال مرحلة `test`.

#### تمرير وسيطات أو خصائص النظام
يمكنك تمرير وسيطات إلى دالة `main` أو تعيين خصائص النظام:

```xml
<configuration>
    <mainClass>com.example.Main</mainClass>
    <arguments>
        <argument>arg1</argument>
        <argument>arg2</argument>
    </arguments>
    <systemProperties>
        <systemProperty>
            <key>propertyName</key>
            <value>propertyValue</value>
        </systemProperty>
    </systemProperties>
</configuration>
```

لاحظ أن `exec:java` يعمل في نفس JVM الذي يعمل فيه Maven، لذا فإن خيارات JVM (مثل `-Xmx`) يتم وراثتها من كيفية استدعاء Maven (مثل `mvn -Xmx512m exec:java`).

### الخيار 2: تشغيل برنامج خارجي باستخدام `exec:exec`
لتنفيذ برامج خارجية مثل نصوص shell أو أوامر، استخدم هدف `exec:exec`.

#### التنفيذ اليدوي
قم بتكوين الإضافة لتشغيل نص برمجي:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>myScript.sh</executable>
                <workingDirectory>/path/to/dir</workingDirectory>
                <arguments>
                    <argument>param1</argument>
                    <argument>param2</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

شغله باستخدام:

```bash
mvn exec:exec
```

هذا ينفذ `myScript.sh` بالوسيطات المحددة في دليل العمل المعطى.

#### التنفيذ التلقائي أثناء البناء
اربطه بمرحلة، مثل بدء وإيقاف خادم لاختبارات التكامل:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>start-server</id>
                    <phase>pre-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>startServer.sh</executable>
                    </configuration>
                </execution>
                <execution>
                    <id>stop-server</id>
                    <phase>post-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>stopServer.sh</executable>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

سيؤدي تشغيل `mvn integration-test` إلى بدء الخادم قبل الاختبارات وإيقافه بعد ذلك.

#### تشغيل Java بخيارات JVM مخصصة
إذا كنت تحتاج إلى JVM منفصل بخيارات محددة (على عكس `exec:java`)، استخدم `exec:exec` مع الأداة القابلة للتنفيذ `java`. ستحتاج إلى إدارة classpath يدوياً. إليك مثال:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>java</executable>
                <arguments>
                    <argument>-Xmx512m</argument>
                    <argument>-classpath</argument>
                    <argument>${project.build.outputDirectory}</argument>
                    <argument>com.example.Main</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

لتضمين التبعيات في classpath، يمكنك استخدام `maven-dependency-plugin` لتوليده:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
            <executions>
                <execution>
                    <id>build-classpath</id>
                    <phase>generate-resources</phase>
                    <goals>
                        <goal>build-classpath</goal>
                    </goals>
                    <configuration>
                        <outputProperty>project.classpath</outputProperty>
                    </configuration>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>java</executable>
                        <arguments>
                            <argument>-Xmx512m</argument>
                            <argument>-classpath</argument>
                            <argument>${project.classpath}:${project.build.outputDirectory}</argument>
                            <argument>com.example.Main</argument>
                        </arguments>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

اضبط فاصل classpath (`:` لنظام Unix، `;` لنظام Windows) حسب الحاجة.

### خيارات التكوين الإضافية
- **متغيرات البيئة** (لـ `exec:exec`):
  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```
- **دليل العمل**: استخدم `<workingDirectory>` لتعيين المكان الذي يعمل فيه الأمر.

### الملخص
إضافة Exec Maven Plugin متعددة الاستخدامات:
- استخدم `exec:java` لتشغيل فئات Java من مشروعك بسهولة، مستفيداً من classpath المشروع، لكنها تعمل في JVM الخاص بـ Maven.
- استخدم `exec:exec` للبرامج الخارجية أو Java بخيارات JVM مخصصة، مما يتطلب إدارة classpath يدوياً إذا لزم الأمر.
- قم بتكوينها في `pom.xml` وشغلها إما يدوياً (`mvn exec:java` أو `mvn exec:exec`) أو اربطها بمراحل البناء باستخدام `<executions>`.

هذا الإعداد يسمح لك بدمج عمليات التنفيذ المخصصة بسلاسة في عملية بناء Maven الخاصة بك