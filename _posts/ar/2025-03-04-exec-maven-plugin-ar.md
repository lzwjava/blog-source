---
audio: false
generated: true
lang: ar
layout: post
title: أداة Exec Maven
translated: true
---

لاستخدام الإضافة `org.codehaus.mojo` Exec Maven في مشروع Maven الخاص بك، عليك تهيئتها في ملف `pom.xml` الخاص بك وتحديد كيفية تنفيذ البرامج - إما الأوامر الخارجية أو البرامج Java - خلال عملية البناء. تقدم الإضافة هدفين رئيسيين: `exec:exec` لتشغيل البرامج الخارجية و `exec:java` لتشغيل فئات Java. أدناه، سأرشدك عبر الخطوات لتهيئتها واستخدامها بشكل فعال.

### الخطوة 1: إضافة الإضافة إلى ملف `pom.xml`
أولاً، أضف الإضافة Exec Maven إلى القسم `<build><plugins>` من ملف `pom.xml`. حدد `groupId` و `artifactId` و إصدار (الأحدث حاليًا هو `3.1.0`):

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

هذا يضيف الإضافة إلى مشروعك، ولكن لن يفعل شيئًا حتى تتهيئ له أو تنفذ أهدافه يدويًا.

### الخطوة 2: اختيار الهدف
تقدم الإضافة هدفين رئيسيين:
- **`exec:exec`**: ينفذ أي برنامج خارجي (مثل scripts أو binaries أو حتى الأمر `java`).
- **`exec:java`**: ينفذ فئة Java مع طريقة `main` من مشروعك في نفس JVM Maven.

يمكنك استخدام هذه الأهداف إما من خلال تنفيذه يدويًا من سطر الأوامر (مثل `mvn exec:exec`) أو من خلال ربطها بفترة معينة في دورة حياة بناء Maven.

### الخيار 1: تشغيل برنامج Java باستخدام `exec:java`
إذا كنت تريد تنفيذ فئة Java من مشروعك، استخدم هدف `exec:java`. هذا مناسب لتشغيل طريقة `main` في فئة جزء من مشروعك، واستخدام مسار تشغيل المشروع (بما في ذلك الاعتماديات) تلقائيًا.

#### التنفيذ اليدوي
أضف تهيئة لتحديد فئة `main`:

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

ثم، تنفذها من سطر الأوامر:

```bash
mvn exec:java
```

هذا ينفذ `com.example.Main` في نفس JVM Maven، وراثة إعدادات JVM Maven.

#### التنفيذ التلقائي أثناء البناء
لتنفيذه تلقائيًا أثناء فترة بناء (مثل `test`), استخدم القسم `<executions>`:

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

الآن، عندما تنفذ `mvn test`, ستنفذ فئة `com.example.Main` خلال فترة `test`.

#### تمرير المعلمات أو خواص النظام
يمكنك تمرير المعلمات إلى طريقة `main` أو تعيين خواص النظام:

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

لاحظ أن `exec:java` ينفذ في نفس JVM Maven، لذلك يتم وراثة خيارات JVM (مثل `-Xmx`) من كيفية تنفيذه Maven (مثل `mvn -Xmx512m exec:java`).

### الخيار 2: تشغيل برنامج خارجي باستخدام `exec:exec`
لنفذ البرامج الخارجية مثل scripts أو الأوامر، استخدم هدف `exec:exec`.

#### التنفيذ اليدوي
تهيئ الإضافة لتنفيذ script:

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

تنفذها باستخدام:

```bash
mvn exec:exec
```

هذا ينفذ `myScript.sh` مع المعلمات المحددة في الدليل العمل المحدد.

#### التنفيذ التلقائي أثناء البناء
ربطه بفترة مثل بدء وإيقاف خادم للاختبارات المتكاملة:

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

تنفيذ `mvn integration-test` سيبدأ الخادم قبل الاختبارات ويوقفها بعدها.

#### تشغيل Java مع خيارات JVM مخصصة
إذا كنت تحتاج إلى JVM منفصلة مع خيارات محددة (خلاف `exec:java`), استخدم `exec:exec` مع الأمر `java`. ستحتاج إلى إدارة مسار التصنيف يدويًا. voici un exemple:

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

لشمل الاعتماديات في مسار التصنيف، يمكنك استخدام الإضافة `maven-dependency-plugin` لتوليدها:

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

قم بتعديل فاصل مسار التصنيف (`:` لـ Unix، `;` لـ Windows) حسب الحاجة.

### خيارات التهيئة الإضافية
- **المتغيرات البيئية** (ل `exec:exec`):
  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```
- **دليل العمل**: استخدم `<workingDirectory>` لتحديد أين يتم تنفيذ الأمر.

### ملخص
الإضافة Exec Maven متعددة الاستخدامات:
- استخدم `exec:java` لتشغيل فئات Java من مشروعك بسهولة، واستخدام مسار تصنيف المشروع، ولكن ينفذ في JVM Maven.
- استخدم `exec:exec` للبرامج الخارجية أو Java مع خيارات JVM مخصصة، يتطلب إدارة مسار التصنيف يدويًا إذا لزم الأمر.
- تهيئها في `pom.xml` وتنفذها يدويًا (`mvn exec:java` أو `mvn exec:exec`) أو ربطها بفترات البناء مع `<executions>`.

هذه التهيئة تسمح لك بتكامل تنفيذات مخصصة بشكل سلس في عملية بناء Maven!