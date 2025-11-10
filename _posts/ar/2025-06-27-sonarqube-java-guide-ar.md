---
audio: false
generated: true
lang: ar
layout: post
title: إتقان استخدام سونار كيوب لمشاريع جافا وسبرينغ
translated: true
type: note
---

# الدليل الشامل لاستخدام SonarQube مع مشاريع Java و Spring

## المقدمة
SonarQube هو منصة مفتوحة المصدر للتفتيش المستمر على جودة الكود. يقوم بإجراء تحليل ثابت للكود لاكتشاف الأخطاء ورائح الكود ونقاط الضعف وحساب تغطية الكود. يقدم هذا الدليل نظرة شاملة لإعداد واستخدام SonarQube في مشروع Java Spring، بما في ذلك التثبيت، التهيئة، التكامل، وأفضل الممارسات.

## جدول المحتويات
1. [ما هو SonarQube؟](#ما-هو-sonarqube)
2. [المتطلبات الأساسية](#المتطلبات-الأساسية)
3. [تثبيت SonarQube](#تثبيت-sonarqube)
4. [إعداد مشروع Java Spring](#إعداد-مشروع-java-spring)
5. [تهيئة SonarQube للمشروع](#تهيئة-sonarqube-للمشروع)
6. [تشغيل تحليل SonarQube](#تشغيل-تحليل-sonarqube)
7. [تفسير نتائج SonarQube](#تفسير-نتائج-sonarqube)
8. [أفضل الممارسات](#أفضل-الممارسات)
9. [استكشاف الأخطاء وإصلاحها الشائعة](#استكشاف-الأخطاء-وإصلاحها-الشائعة)
10. [الخلاصة](#الخلاصة)

## ما هو SonarQube؟
SonarQube هو أداة توفر تفتيشًا مستمرًا لجودة الكود من خلال تحليل الكود المصدري للبحث عن:
- **الأخطاء**: أخطاء محتملة في الكود.
- **رائح الكود**: مشاكل في قابلية الصيانة قد تؤدي إلى دين تقني.
- **نقاط الضعف**: مشاكل أمنية قد يتم استغلالها.
- **تغطية الكود**: النسبة المئوية للكود المغطى بواسطة اختبارات الوحدة.
- **التكرارات**: كتل كود مكررة يمكن إعادة هيكلتها.

يدعم SonarQube لغات متعددة، بما في ذلك Java، ويمكن دمجه بسلاسة مع أدوات البناء مثل Maven و Gradle، بالإضافة إلى خطوط أنابيب CI/CD.

## المتطلبات الأساسية
قبل إعداد SonarQube، تأكد من توفر:
- **Java Development Kit (JDK)**: الإصدار 11 أو أحدث (يتطلب SonarQube Java 11 أو 17).
- **Maven أو Gradle**: أداة البناء لمشروع Java Spring.
- **خادم SonarQube**: الإصدار 9.9 LTS أو أحدث (النسخة Community كافية لمعظم حالات الاستخدام).
- **SonarScanner**: أداة CLI لتشغيل التحليل.
- **قاعدة البيانات**: يتطلب SonarQube قاعدة بيانات (مثل PostgreSQL أو MySQL أو H2 المضمنة للاختبار).
- **مشروع Spring**: مشروع Spring Boot أو Spring Framework يعمل.
- **بيئة التطوير المتكاملة**: IntelliJ IDEA أو Eclipse أو VS Code للتطوير.

## تثبيت SonarQube

### الخطوة 1: تنزيل وتثبيت SonarQube
1. **تنزيل SonarQube**:
   - قم بزيارة [صفحة تنزيل SonarQube](https://www.sonarqube.org/downloads/).
   - اختر النسخة Community (مجانية) أو نسخة أخرى بناءً على احتياجاتك.
   - قم بتنزيل ملف ZIP (مثل `sonarqube-9.9.0.zip`).

2. **استخراج ملف ZIP**:
   - قم بفك ضغط الملف الذي تم تنزيله إلى دليل، مثل `/opt/sonarqube` أو `C:\sonarqube`.

3. **تهيئة قاعدة البيانات**:
   - يتطلب SonarQube قاعدة بيانات. للإنتاج، استخدم PostgreSQL أو MySQL. للاختبار، قاعدة البيانات المضمنة H2 كافية.
   - مثال لـ PostgreSQL:
     - قم بتثبيت PostgreSQL وأنشئ قاعدة بيانات (مثل `sonarqube`).
     - قم بتحديث ملف تهيئة SonarQube (`conf/sonar.properties`):
       ```properties
       sonar.jdbc.url=jdbc:postgresql://localhost:5432/sonarqube
       sonar.jdbc.username=sonarqube_user
       sonar.jdbc.password=sonarqube_pass
       ```

4. **بدء تشغيل SonarQube**:
   - انتقل إلى دليل SonarQube (`bin/<platform>`).
   - قم بتشغيل سكريبت البدء:
     - على Linux/Mac: `./sonar.sh start`
     - على Windows: `StartSonar.bat`
   - قم بالوصول إلى SonarQube على `http://localhost:9000` (المنفذ الافتراضي).

5. **تسجيل الدخول**:
   - بيانات الاعتماد الافتراضية: `admin/admin`.
   - قم بتغيير كلمة المرور بعد أول تسجيل دخول.

### الخطوة 2: تثبيت SonarScanner
1. **تنزيل SonarScanner**:
   - قم بالتنزيل من [صفحة SonarQube Scanner](https://docs.sonarqube.org/latest/analyzing-source-code/scanners/sonarscanner/).
   - قم باستخراجه إلى دليل، مثل `/opt/sonar-scanner`.

2. **تهيئة متغيرات البيئة**:
   - أضف SonarScanner إلى PATH الخاص بك:
     - على Linux/Mac: `export PATH=$PATH:/opt/sonar-scanner/bin`
     - على Windows: أضف `C:\sonar-scanner\bin` إلى نظام PATH.

3. **التحقق من التثبيت**:
   - قم بتشغيل `sonar-scanner --version` للتأكيد على التثبيت.

## إعداد مشروع Java Spring
في هذا الدليل، سنستخدم مشروع Spring Boot مع Maven. الخطوات مشابهة لمشاريع Gradle أو Spring غير Boot.

1. **إنشاء مشروع Spring Boot**:
   - استخدم [Spring Initializer](https://start.spring.io/) لإنشاء مشروع مع:
     - التبعيات: Spring Web، Spring Data JPA، H2 Database، Spring Boot Starter Test.
     - أداة البناء: Maven.
   - قم بتنزيل المشروع واستخراجه.

2. **إضافة اختبارات الوحدة**:
   - تأكد من أن مشروعك يحتوي على اختبارات وحدة لقياس تغطية الكود.
   - مثال لفئة اختبار:
     ```java
     import org.junit.jupiter.api.Test;
     import org.springframework.boot.test.context.SpringBootTest;

     @SpringBootTest
     public class ApplicationTests {
         @Test
         void contextLoads() {
         }
     }
     ```

3. **إضافة Jacoco لتغطية الكود**:
   - أضف إضافة JaCoCo Maven إلى `pom.xml` لتوليد تقارير تغطية الكود:
     ```xml
     <plugin>
         <groupId>org.jacoco</groupId>
         <artifactId>jacoco-maven-plugin</artifactId>
         <version>0.8.8</version>
         <executions>
             <execution>
                 <goals>
                     <goal>prepare-agent</goal>
                 </goals>
             </execution>
             <execution>
                 <id>report</id>
                 <phase>test</phase>
                 <goals>
                     <goal>report</goal>
                 </goals>
             </execution>
         </executions>
     </plugin>
     ```

## تهيئة SonarQube للمشروع

1. **إنشاء مشروع SonarQube**:
   - سجل الدخول إلى SonarQube (`http://localhost:9000`).
   - انقر على **Create Project** > **Manually**.
   - قم بتوفير **مفتاح المشروع** (مثل `my-spring-project`) و **اسم العرض**.
   - قم بتوليد رمز للمصادقة (مثل `my-token`).

2. **تهيئة `sonar-project.properties`**:
   - في جذر مشروع Spring الخاص بك، أنشئ ملف `sonar-project.properties`:
     ```properties
     sonar.projectKey=my-spring-project
     sonar.projectName=My Spring Project
     sonar.host.url=http://localhost:9000
     sonar.token=my-token
     sonar.java.binaries=target/classes
     sonar.sources=src/main/java
     sonar.tests=src/test/java
     sonar.junit.reportPaths=target/surefire-reports
     sonar.jacoco.reportPaths=target/jacoco.exec
     sonar.sourceEncoding=UTF-8
     ```

3. **دمج Maven (بديل)**:
   - بدلاً من `sonar-project.properties`، يمكنك تهيئة SonarQube في `pom.xml`:
     ```xml
     <properties>
         <sonar.host.url>http://localhost:9000</sonar.host.url>
         <sonar.token>my-token</sonar.token>
         <sonar.projectKey>my-spring-project</sonar.projectKey>
         <sonar.projectName>My Spring Project</sonar.projectName>
     </properties>
     <build>
         <plugins>
             <plugin>
                 <groupId>org.sonarsource.scanner.maven</groupId>
                 <artifactId>sonar-maven-plugin</artifactId>
                 <version>3.9.1.2184</version>
             </plugin>
         </plugins>
     </build>
     ```

## تشغيل تحليل SonarQube

1. **باستخدام SonarScanner**:
   - انتقل إلى جذر المشروع.
   - قم بتشغيل:
     ```bash
     sonar-scanner
     ```
   - تأكد من تنفيذ الاختبارات قبل التحليل (`mvn test` لمشاريع Maven).

2. **باستخدام Maven**:
   - قم بتشغيل:
     ```bash
     mvn clean verify sonar:sonar
     ```
   - يقوم هذا الأمر بترجمة الكود، وتشغيل الاختبارات، وتوليد تقارير التغطية، وإرسال النتائج إلى SonarQube.

3. **التحقق من النتائج**:
   - افتح SonarQube (`http://localhost:9000`) وانتقل إلى مشروعك.
   - تحقق من لوحة التحكم لرؤية نتائج التحليل.

## تفسير نتائج SonarQube
توفر لوحة تحكم SonarQube:
- **نظرة عامة**: ملخص للمشاكل، التغطية، والتكرارات.
- **المشاكل**: قائمة بالأخطاء، نقاط الضعف، ورائح الكود مع مستوى الخطورة (Blocker، Critical، Major، إلخ).
- **تغطية الكود**: النسبة المئوية للكود المغطى بالاختبارات (عبر JaCoCo).
- **التكرارات**: كتل كود مكررة.
- **بوابة الجودة**: حالة النجاح/الفشل بناءً على عتبات محددة مسبقًا (مثل تغطية > 80%).

### أمثلة على الإجراءات:
- **إصلاح الأخطاء**: معالجة المشاكل الحرجة مثل عمليات الإشارة إلى null.
- **إعادة هيكلة رائح الكود**: تبسيط الطرق المعقدة أو إزالة الكود غير المستخدم.
- **تحسين التغطية**: كتابة اختبارات وحدة إضافية للكود غير المغطى.

## أفضل الممارسات
1. **التكامل مع CI/CD**:
   - أضف تحليل SonarQube إلى خط أنابيب CI/CD الخاص بك (مثل Jenkins، GitHub Actions).
   - مثال لسير عمل GitHub Actions:
     ```yaml
     name: CI with SonarQube
     on: [push]
     jobs:
       build:
         runs-on: ubuntu-latest
         steps:
           - uses: actions/checkout@v3
           - name: Set up JDK 11
             uses: actions/setup-java@v3
             with:
               java-version: '11'
           - name: Build and Analyze
             run: mvn clean verify sonar:sonar -Dsonar.host.url=http://localhost:9000 -Dsonar.token=${{ secrets.SONAR_TOKEN }}
     ```

2. **تحديد بوابات الجودة**:
   - حدد عتبات لتغطية الكود، الأخطاء، ونقاط الضعف في SonarQube.
   - مثال: فشل البناء إذا كانت التغطية < 80% أو إذا وجدت مشاكل حرجة.

3. **استخدام SonarLint**:
   - قم بتثبيت إضافة SonarLint في بيئة التطوير المتكاملة الخاصة بك (مثل IntelliJ IDEA) لاكتشاف المشاكل أثناء التطوير.

4. **التحليل المنتظم**:
   - قم بتشغيل تحليل SonarQube في كل commit أو يوميًا لاكتشاف المشاكل مبكرًا.

5. **تخصيص القواعد**:
   - خصص قواعد SonarQube لتناسب احتياجات مشروعك (مثل تعطيل القواعد غير ذات الصلة أو إضافة قواعد مخصصة).

## استكشاف الأخطاء وإصلاحها الشائعة
1. **فشل تحميل التحليل**:
   - تحقق من `sonar.host.url` و `sonar.token` في التهيئة.
   - تأكد من أن خادم SonarQube يعمل (`http://localhost:9000`).

2. **لا توجد تغطية للكود**:
   - تحقق من أن إضافة JaCoCo مهيئة بشكل صحيح في `pom.xml`.
   - قم بتشغيل `mvn test` قبل التحليل لتوليد `jacoco.exec`.

3. **أخطاء اتصال قاعدة البيانات**:
   - تأكد من بيانات اعتماد قاعدة البيانات في `sonar.properties`.
   - تأكد من أن خادم قاعدة البيانات يعمل.

4. **نفاد الذاكرة**:
   - زد ذاكرة JVM في `sonar.properties`:
     ```properties
     sonar.web.javaOpts=-Xmx2g -Xms1g
     ```

## الخلاصة
SonarQube هو أداة قوية للحفاظ على جودة الكود في مشاريع Java Spring. من خلال دمجه في سير عمل التطوير الخاص بك، يمكنك اكتشاف المشاكل مبكرًا، وتحسين قابلية صيانة الكود، وضمان أمن قوي. التحليل المنتظم، مقترنًا بأفضل الممارسات مثل التكامل مع CI/CD و SonarLint، سيساعدك في الحفاظ على قاعدة كود عالية الجودة.