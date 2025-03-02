---
audio: false
generated: true
lang: ar
layout: post
title: Spring Boot Maven Plugin
translated: true
---

لاستخدام `spring-boot-maven-plugin` في مشروع Spring Boot مبني على Maven، اتبع هذه الخطوات لتكوين واستخدام الإضافة لبناء، تشغيل، وإدارة تطبيقك. أدناه دليل شامل:

---

### **1. تأكد من أن مشروعك هو مشروع Spring Boot**
قبل استخدام `spring-boot-maven-plugin`، تأكد من أن مشروعك مهيأ كمشروع Spring Boot. هذا يتضمن عادةً:

- **الاستمرار من `spring-boot-starter-parent` (الموصى به)**:
  - في ملف `pom.xml` الخاص بك، قم بإعداد `spring-boot-starter-parent` كوالد لإدارة اعتمادات Spring Boot وإصدارات الإضافة.
  - مثال:
    ```xml
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.4</version> <!-- استبدل بإصدار Spring Boot الخاص بك -->
        <relativePath/> <!-- البحث عن الوالد من المستودع -->
    </parent>
    ```

- **بديلاً، استخدام `spring-boot-dependencies` BOM (Bill of Materials)**:
  - إذا لم تستطع استخدام `spring-boot-starter-parent`، قم بإستيراد `spring-boot-dependencies` BOM في قسم `dependencyManagement`.
  - مثال:
    ```xml
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.5.4</version> <!-- استبدل بإصدار Spring Boot الخاص بك -->
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    ```

استخدام `spring-boot-starter-parent` هو الموصى به من أجل السهولة، حيث يدير الإصدارات تلقائياً.

---

### **2. أضف `spring-boot-maven-plugin` إلى ملف `pom.xml` الخاص بك**
لاستخدام الإضافة، عليك إعلانها في قسم `<build><plugins>` من ملف `pom.xml` الخاص بك.

- **إذا كنت تستخدم `spring-boot-starter-parent`**:
  - أضف الإضافة دون تحديد الإصدار، حيث يديره الوالد.
  - مثال:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
    ```

- **إذا لم تكن تستخدم `spring-boot-starter-parent`**:
  - قم بتحديد الإصدار بشكل صريح، متطابق مع إصدار Spring Boot المستخدم.
  - مثال:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.5.4</version> <!-- استبدل بإصدار Spring Boot الخاص بك -->
            </plugin>
        </plugins>
    </build>
    ```

---

### **3. استخدم أهداف الإضافة**
توفر `spring-boot-maven-plugin` عدة أهداف لمساعدتك في بناء، تشغيل، وإدارة تطبيق Spring Boot الخاص بك. أدناه الأكثر استخداماً من هذه الأهداف:

- **`spring-boot:run`**
  - يجرى تطبيق Spring Boot الخاص بك مباشرة من Maven باستخدام خادم ويب مدمج (مثل Tomcat).
  - مفيد للتنمية والتجربة.
  - الأمر:
    ```
    mvn spring-boot:run
    ```

- **`spring-boot:repackage`**
  - يعيد تعبئة ملف JAR أو WAR الذي يولد بواسطة `mvn package` إلى "fat JAR" أو WAR قابل للتنفيذ يتضمن جميع الاعتمادات.
  - هذه الهدف يتم تنفيذه تلقائياً خلال مرحلة `package` إذا كانت الإضافة مهيأة.
  - الأمر:
    ```
    mvn package
    ```
  - بعد التنفيذ، يمكنك تشغيل التطبيق باستخدام:
    ```
    java -jar target/myapp.jar
    ```

- **`spring-boot:start` و `spring-boot:stop`**
  - يستخدم لاختبارات التكامل لبدء وإيقاف التطبيق خلال مراحل `pre-integration-test` و `post-integration-test` على التوالي.
  - مثال:
    ```
    mvn spring-boot:start
    mvn spring-boot:stop
    ```

- **`spring-boot:build-info`**
  - يولد ملف `build-info.properties` يحتوي على معلومات البناء (مثل وقت البناء، الإصدار).
  - يمكن الوصول إلى هذه المعلومات في تطبيقك باستخدام Bean `BuildProperties` من Spring Boot أو تعليقات `@Value`.
  - الأمر:
    ```
    mvn spring-boot:build-info
    ```

---

### **4. تخصيص تكوين الإضافة (اختياري)**
يمكنك تخصيص سلوك `spring-boot-maven-plugin` بإضافة خيارات التكوين في `pom.xml`. أدناه بعض التخصيصات الشائعة:

- **تحديد الفئة الرئيسية**:
  - إذا لم يتمكن الإضافة من اكتشاف الفئة الرئيسية تلقائياً، قم بتحديدها يدوياً.
  - مثال:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <mainClass>com.example.MyApplication</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **استبعاد الاعتمادات من "fat JAR"**:
  - استبعد الاعتمادات التي يوفرها بيئة التشغيل (مثل خادم Servlet خارجي).
  - مثال:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>com.example</groupId>
                            <artifactId>some-dependency</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **تعيين حجج التطبيق**:
  - قم بتكوين حجج لتسليمها إلى التطبيق عند تشغيله باستخدام `spring-boot:run`.
  - مثال في `pom.xml`:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <arguments>
                        <argument>--server.port=8081</argument>
                    </arguments>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```
  - بديلاً، قم بتسليم الحجج عبر سطر الأوامر:
    ```
    mvn spring-boot:run -Dspring-boot.run.arguments=--server.port=8081
    ```

- **بناء ملفات WAR**:
  - إذا كنت تبني ملف WAR للإنشاء في خادم Servlet خارجي، تأكد من أن نوع التعبئة الخاص بك هو `war` في `pom.xml`:
    ```xml
    <packaging>war</packaging>
    ```
  - قد تحتاج أيضاً إلى استبعاد خادمات Servlet المدمجة (مثل Tomcat) إذا تم توفيرها من البيئة. أضف الاعتماد التالي ك `provided`:
    ```xml
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
            <scope>provided</scope>
        </dependency>
    </dependencies>
    ```

---

### **5. ملاحظات رئيسية**
- **السلوك الافتراضي**:
  - عندما تجرى `mvn package`، تقوم الإضافة بإعادة تعبئة JAR/WAR تلقائياً خلال مرحلة `package` لجعله قابل للتنفيذ.
  - يتم تجميع المنتج النهائي، ويضاف المنتج الأصلي مع تصنيف (مثل `original`).

- **عملية التنمية**:
  - استخدم `mvn spring-boot:run` للتنمية والتجربة السريعة.
  - استخدم `mvn package` لبناء JAR أو WAR قابل للتنفيذ.

- **اختبارات التكامل**:
  - استخدم `spring-boot:start` و `spring-boot:stop` لإدارة دورة حياة التطبيق أثناء اختبارات التكامل.

---

### **ملخص**
لاستخدام `spring-boot-maven-plugin`:
1. تأكد من أن مشروعك هو مشروع Spring Boot، عادةً من خلال الاستمرار من `spring-boot-starter-parent` أو استخدام `spring-boot-dependencies` BOM.
2. أضف الإضافة إلى قسم `<build><plugins>` من ملف `pom.xml` الخاص بك.
3. استخدم أوامر Maven مثل:
   - `mvn spring-boot:run` لتشغيل التطبيق.
   - `mvn package` لبناء JAR/WAR قابل للتنفيذ.
   - أهداف أخرى مثل `spring-boot:start`، `spring-boot:stop`، و `spring-boot:build-info` حسب الحاجة.
4. اختيارياً، قم بتخصيص تكوين الإضافة في `pom.xml` لمواقف الاستخدام المتقدمة.

هذه الإعدادات تتيح لك بناء، تشغيل، وإدارة تطبيقات Spring Boot بشكل فعال باستخدام Maven.