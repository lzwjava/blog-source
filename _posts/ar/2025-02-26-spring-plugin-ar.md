---
audio: false
generated: true
lang: ar
layout: post
title: إضافة Maven لـ Spring Boot
translated: true
type: note
---

لاستخدام `spring-boot-maven-plugin` في مشروع Spring Boot يعتمد على Maven، اتبع هذه الخطوات لتكوين واستخدام البرنامج المساعد لبناء وتشغيل وإدارة تطبيقك. فيما يلي دليل شامل:

---

### **1. تأكد من أن مشروعك هو مشروع Spring Boot**
قبل استخدام `spring-boot-maven-plugin`، تأكد من إعداد مشروعك كمشروع Spring Boot. يتضمن هذا عادةً:

- **الوراثة من `spring-boot-starter-parent` (مُوصى به)**:
  - في ملف `pom.xml` الخاص بك، عيّن `spring-boot-starter-parent` كأصل لإدارة تبعيات وإصدارات برامج Spring Boot المساعدة.
  - مثال:
    ```xml
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.4</version> <!-- استبدل بإصدار Spring Boot الخاص بك -->
        <relativePath/> <!-- ابحث عن الأصل من المستودع -->
    </parent>
    ```

- **بديلاً لذلك، استخدام BOM `spring-boot-dependencies` (قائمة المواد)**:
  - إذا لم تتمكن من استخدام `spring-boot-starter-parent`، فاستورد BOM `spring-boot-dependencies` في قسم `dependencyManagement`.
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

يُوصى باستخدام `spring-boot-starter-parent` للبساطة، حيث يدير إصدارات البرامج المساعدة تلقائيًا.

---

### **2. أضف `spring-boot-maven-plugin` إلى ملف `pom.xml` الخاص بك**
لاستخدام البرنامج المساعد، تحتاج إلى التصريح عنه في قسم `<build><plugins>` في ملف `pom.xml` الخاص بك.

- **إذا كنت تستخدم `spring-boot-starter-parent`**:
  - أضف البرنامج المساعد دون تحديد الإصدار، حيث تتم إدارته بواسطة الأصل.
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
  - حدد الإصدار صراحةً، ليطابق إصدار Spring Boot المستخدم.
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

### **3. استخدم أهداف البرنامج المساعد**
يوفر `spring-boot-maven-plugin` عدة أهداف لمساعدة في بناء وتشغيل وإدارة تطبيق Spring Boot الخاص بك. فيما يلي أكثر الأهداف استخدامًا:

- **`spring-boot:run`**
  - يشغّل تطبيق Spring Boot الخاص بك مباشرة من Maven باستخدام خادم ويب مضمّن (مثل Tomcat).
  - مفيد للتطوير والاختبار.
  - الأمر:
    ```
    mvn spring-boot:run
    ```

- **`spring-boot:repackage`**
  - يعيد تغليف ملف JAR أو WAR الذي تم إنشاؤه بواسطة `mvn package` إلى "JAR سمين" أو WAR قابل للتنفيذ يتضمن جميع التبعيات.
  - يتم تنفيذ هذا الهدف تلقائيًا خلال مرحلة `package` إذا تم تكوين البرنامج المساعد.
  - الأمر:
    ```
    mvn package
    ```
  - بعد التشغيل، يمكنك بدء التطبيق باستخدام:
    ```
    java -jar target/myapp.jar
    ```

- **`spring-boot:start` و `spring-boot:stop`**
  - تُستخدم لاختبارات التكامل لبدء وإيقاف التطبيق خلال مراحل `pre-integration-test` و `post-integration-test` على التوالي.
  - مثال:
    ```
    mvn spring-boot:start
    mvn spring-boot:stop
    ```

- **`spring-boot:build-info`**
  - يولد ملف `build-info.properties` يحتوي على معلومات البناء (مثل وقت البناء، الإصدار).
  - يمكن الوصول إلى هذه المعلومات في تطبيقك باستخدام bean `BuildProperties` الخاص بـ Spring Boot أو تعريفات `@Value`.
  - الأمر:
    ```
    mvn spring-boot:build-info
    ```

---

### **4. خصّص تكوين البرنامج المساعد (اختياري)**
يمكنك تخصيص سلوك `spring-boot-maven-plugin` عن طريق إضافة خيارات التكوين في `pom.xml`. فيما يلي بعض عمليات التخصيص الشائعة:

- **تحديد الفئة الرئيسية**:
  - إذا لم يتمكن البرنامج المساعد من اكتشاف الفئة الرئيسية تلقائيًا، فحددها يدويًا.
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

- **استبعاد التبعيات من JAR السمين**:
  - استبعد التبعيات التي يوفرها بيئة وقت التشغيل (مثل حاوية servlet خارجية).
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

- **تعيين وسيطات التطبيق**:
  - قم بتكوين وسيطات لتمريرها إلى التطبيق عند التشغيل باستخدام `spring-boot:run`.
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
  - بديلاً لذلك، يمكن تمرير الوسيطات عبر سطر الأوامر:
    ```
    mvn spring-boot:run -Dspring-boot.run.arguments=--server.port=8081
    ```

- **بناء ملفات WAR**:
  - إذا كنت تبني ملف WAR للنشر على حاوية servlet خارجية، فتأكد من تعيين تغليف مشروعك على `war` في `pom.xml`:
    ```xml
    <packaging>war</packaging>
    ```
  - قد تحتاج أيضًا إلى استبعاد حاويات servlet المضمنة (مثل Tomcat) إذا كانت مرفقة بالبيئة. أضف التبعية التالية كـ `provided`:
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
  - عند تشغيل `mvn package`، يعيد البرنامج المساعد تغليف JAR/WAR تلقائيًا خلال مرحلة `package` لجعله قابلاً للتنفيذ.
  - القطعة المعاد تغليفها هي القطعة الرئيسية، بينما يتم إرفاق JAR/WAR الأصلي بمعرّف تصنيف (مثل `original`).

- **سير عمل التطوير**:
  - استخدم `mvn spring-boot:run` للتطوير والاختبار السريع.
  - استخدم `mvn package` لبناء JAR أو WAR قابل للتنفيذ وقابل للنشر.

- **اختبارات التكامل**:
  - استخدم `spring-boot:start` و `spring-boot:stop` لإدارة دورة حياة التطبيق أثناء اختبار التكامل.

---

### **الخلاصة**
لاستخدام `spring-boot-maven-plugin`:
1. تأكد من أن مشروعك هو مشروع Spring Boot، عادةً عن طريق الوراثة من `spring-boot-starter-parent` أو استخدام BOM `spring-boot-dependencies`.
2. أضف البرنامج المساعد إلى قسم `<build><plugins>` في ملف `pom.xml` الخاص بك.
3. استخدم أوامر Maven مثل:
   - `mvn spring-boot:run` لتشغيل التطبيق.
   - `mvn package` لبناء JAR/WAR قابل للتنفيذ.
   - الأهداف الأخرى مثل `spring-boot:start`، `spring-boot:stop`، و `spring-boot:build-info` حسب الحاجة.
4. قم بتخصيص تكوين البرنامج المساعد في `pom.xml` لحالات الاستخدام المتقدمة بشكل اختياري.

يمكّنك هذا الإعداد من بناء وتشغيل وإدارة تطبيقات Spring Boot بكفاءة باستخدام Maven.