---
audio: false
generated: true
lang: ar
layout: post
title: مشكلة تبعية مافن
translated: true
type: note
---

### نظرة عامة على المشكلة

يواجه المستخدم فشل في بناء التطبيق عند تشغيل تطبيق Spring Boot باستخدام Maven. تشير رسالة الخطأ إلى وجود `IllegalArgumentException` ناتج عن `NoClassDefFoundError: org/springframework/beans/factory/aot/BeanRegistrationExcludeFilter`. يشير هذا إلى وجود مشكلة عدم توافق في الإصدارات بين تبعيات المشروع، مما يمنع التطبيق من البدء بشكل صحيح. ملف `pom.xml` المُقدم ونتيجة تنفيذ Maven يقدمان لنا السياق اللازم لتشخيص المشكلة وحلها.

### السبب الجذري

يحدث الخطأ لأن تطبيق Spring Boot غير قادر على إنشاء مثيل للفئة `SharedMetadataReaderFactoryContextInitializer`، وهي فئة تشارك في عملية الضبط التلقائي (auto-configuration) في Spring Boot. السبب الأساسي هو فقدان الفئة `BeanRegistrationExcludeFilter`، والتي هي جزء من Spring Framework 6.0 والإصدارات الأحدث. يستخدم المشروع Spring Boot 3.4.2، الذي يعتمد على Spring Framework 6.1.14. ومع ذلك، فإن ملف `pom.xml` يحدد إصدارات قديمة وغير متوافقة من تبعيات Spring Framework، مما يؤدي إلى تعارض في classpath.

إليك المشاكل الرئيسية التي تم تحديدها في ملف `pom.xml`:

1.  **إصدار غير متوافق من إضافة Maven لـ Spring Boot:**
    *   تم تعيين `spring-boot-maven-plugin` إلى الإصدار `2.7.0`، والذي صُمم ليعمل مع Spring Boot 2.x، وليس Spring Boot 3.4.2 (إصدار 3.x). يمكن أن يتسبب هذا التباين في حدوث مشاكل أثناء مراحل البناء والتشغيل.

2.  **تبعيات Spring Framework الصريحة غير المتوافقة:**
    *   يعلن ملف `pom.xml` صراحةً عن `spring-aop` و `spring-aspects` مع الإصدار `5.3.23` (Spring Framework 5.x)، بينما يتطلب Spring Boot 3.4.2 الإصدار Spring Framework 6.1.14. تعطي Maven الأولوية لهذه الإصدارات المعلن عنها صراحةً على الإصدارات التي تديرها Spring Boot، مما يؤدي إلى وجود مزيج من Spring Framework 5.x و 6.x في classpath. يتسبب هذا المزيج في حدوث `NoClassDefFoundError` لأن `BeanRegistrationExcludeFilter` (من Spring Framework 6.x) غير متاح عند تحميل ملفات JAR القديمة الخاصة بالإصدار 5.x.

### الحل

لحل هذه المشكلة، نحتاج إلى التأكد من أن جميع مكونات المشروع متوافقة مع Spring Boot 3.4.2 وأن Spring Boot يدير إصدارات تبعياته لتجنب التعارضات. يجب إجراء التغييرات التالية على ملف `pom.xml`:

1.  **تحديث إصدار إضافة Maven لـ Spring Boot:**
    *   قم بتغيير إصدار `spring-boot-maven-plugin` من `2.7.0` إلى `3.4.2` ليتوافق مع إصدار Spring Boot المستخدم في المشروع.

2.  **إزالة تبعيات Spring Framework الصريحة:**
    *   قم بإزالة التصريحات الصريحة لـ `spring-aop` و `spring-aspects` مع الإصدار `5.3.23`. يدير Spring Boot 3.4.2 هذه التبعيات من خلال الـ starters الخاصة به (على سبيل المثال، `spring-boot-starter-web` يتضمن `spring-aop` مع الإصدار الصحيح، 6.1.14). من خلال إزالة هذه التبعيات، نمنع Maven من تجاوز إدارة تبعيات Spring Boot.

### ملف `pom.xml` المُحدَّث

إليك ملف `pom.xml` المصحح مع تطبيق التغييرات اللازمة:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.lzwjava</groupId>
    <artifactId>blog-server</artifactId>
    <version>1.0</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>3.4.2</version>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>5.3.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <version>3.4.2</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjrt</artifactId>
            <version>1.9.22</version>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjweaver</artifactId>
            <version>1.9.22</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>3.4.2</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M8</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-checkstyle-plugin</artifactId>
                <version>3.1.1</version>
                <configuration>
                    <configLocation>google_checks.xml</configLocation>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### شرح التغييرات

*   **تحديث إضافة Maven لـ Spring Boot:**
    *   تم تغيير `<version>2.7.0</version>` إلى `<version>3.4.2</version>` في إعدادات `spring-boot-maven-plugin`. يضمن هذا أن الإضافة متوافقة مع Spring Boot 3.4.2، مما يدعم الميزات والإعدادات المحددة للسلسلة 3.x.

*   **إزالة `spring-aop` و `spring-aspects`:**
    *   تمت إزالة التبعيات التالية:
        ```xml
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aop</artifactId>
            <version>5.3.23</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aspects</artifactId>
            <version>5.3.23</version>
        </dependency>
        ```
    *   `spring-aop` مدرجة بالفعل في `spring-boot-starter-web` (عبر `spring-web`)، ويدير Spring Boot إصدارها إلى 6.1.14، وهو متوافق مع 3.4.2.
    *   `spring-aspects` ليست تبعية قياسية في starters Spring Boot. إذا كان المشروع يحتاجها صراحةً (على سبيل المثال، للـ aspects المخصصة)، فيمكن إضافتها مرة أخرى بدون تحديد إصدار (السماح لإدارة تبعيات Spring Boot بالتعامل معها) أو تعيينها إلى `6.1.14`. ومع ذلك، نظرًا لأن الخطأ يحدث أثناء بدء التشغيل ويتعلق بالضبط التلقائي وليس بفقدان aspects، فمن المرجح أنها غير ضرورية هنا ويمكن إزالتها بأمان.

### ملاحظات إضافية

*   **تبعيات AspectJ:**
    *   تبقى تبعيات `aspectjrt` و `aspectjweaver` (الإصدار 1.9.22) في ملف `pom.xml` لأنها متوافقة مع Spring Framework 6.1.14 وقد تكون مطلوبة إذا كان المشروع يستخدم ميزات AspectJ. هذه لا تتعارض مع Spring Boot 3.4.2.

*   **أفضل الممارسات:**
    *   لمشاريع Spring Boot، يُوصى باستخدام `spring-boot-starter-parent` كـ POM parent أو استيراد BOM `spring-boot-dependencies` لإدارة إصدارات التبعيات تلقائيًا. ملف `pom.xml` الحالي لا يفعل أيًا من هذين، لكن الحل يعمل دون الحاجة إلى هذا التغيير طالما أن `spring-boot-starter-web` والـ starters الأخرى لا تزال تفرض تناسق الإصدارات عند إزالة التجاوزات الصريحة.

*   **التحقق:**
    *   بعد تطبيق هذه التغييرات، قم بتشغيل `mvn clean spring-boot:run` للتحقق من أن التطبيق يبدأ بدون أخطاء. إذا كان المشروع يعتمد على `spring-aspects` (على سبيل المثال، لوظيفة AOP محددة)، وتسبب إزالتها في حدوث مشاكل، فأعد إضافتها مع `<version>6.1.14</version>` أو احذف تحديد الإصدار وتأكد من إدارة التبعية بشكل صحيح.

### الخلاصة

من خلال تحديث `spring-boot-maven-plugin` إلى الإصدار 3.4.2 وإزالة التبعيات الصريحة `spring-aop` و `spring-aspects`، سوف يستخدم المشروع إصدارات متسقة من Spring Boot (3.4.2) و Spring Framework (6.1.14). يحل هذا التعارض في classpath الذي تسبب في `NoClassDefFoundError` ويسمح للتطبيق بالبدء بنجاح.