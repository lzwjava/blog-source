---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4.1-fast
title: ملفات تعريف Maven لتكوين بيئة WAS
translated: true
type: note
---

لـ IBM WebSphere Application Server (النسخة التقليدية WAS، وليس Liberty)، فإن التغليف القياسي هو ملف **EAR** (حتى للتطبيقات البسيطة، حيث يفضل WAS ملفات EAR بدلاً من WAR المنفردة). أفضل ممارسة للتعامل مع البيئات المختلفة — مثل التطوير المحلي (مستخدم تسجيل دخول ثابت/مشفّر للاختبار) مقابل الخادم/الإنتاج (SSO أو مجال أمان مناسب) — هي استخدام **ملفات تعريف Maven** في ملف `pom.xml` واحد. هذا يتجنب الحفاظ على ملفات POM منفصلة متعددة (مثل `pom.xml` و `build_pom.xml`)، وهو أمر عرضة للأخطاء ولا يعتبر أسلوبًا قياسيًا في Maven.

### لماذا ملفات التعريف بدلاً من ملفات POM متعددة؟
- مصدر واحد للحقيقة (ملف POM واحد).
- تفعيل سهل: `mvn package -Plocal` أو `mvn package -Pserver`.
- يمكن لملفات التعريف تصفية الموارد، تجاوز الملفات، تغيير تكوين الإضافات، أو ضبط الربط (مثل `ibm-web-bnd.xml`، `ibm-application-ext.xml` للمصادقة الخاصة بـ WAS).
- شائع الاستخدام للاختلافات بين التطوير/الاختبار/الإنتاج، بما في ذلك إعدادات المصادقة.

### الهيكل الموصى به
استخدم Maven Resources Plugin مع التصفية + أدلة موارد خاصة بملف التعريف لتبديل ملفات التكوين (مثل `web.xml`، ملفات `properties`، تكوين أمان Spring، أو روابط WAS).

مثال على تخطيط الدليل:
```
src/
├── main/
│   ├── resources/          (التكوينات المشتركة)
│   ├── webapp/
│   │   ├── WEB-INF/
│   │   │   ├── web.xml      (نسخة أساسية أو مشتركة)
│   │   │   └── ibm-web-bnd.xml (اختياري، لربط JNDI/المصادقة)
│   └── ...
├── local/                   (موارد خاصة بملف التعريف، تُنسخ/تُصفى فقط للمحلي)
│   └── webapp/
│       └── WEB-INF/
│           ├── web.xml      (نسخة محلية مع تسجيل دخول بالنموذج + مستخدم/دور مشفر أو بدون أمان)
│           └── ...
└── server/                  (خاص بملف التعريف للإنتاج/SSO)
    └── webapp/
        └── WEB-INF/
            ├── web.xml      (نسخة الخادم مع <login-config><auth-method>CLIENT-CERT</auth-method> أو SPNEGO لـ SSO)
            └── ...
```

### مثال مقتطف من pom.xml
```xml
<project ...>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-was-app</artifactId>
    <version>1.0.0</version>
    <packaging>ear</packaging>   <!-- أو war إذا قمت بالنشر كـ WAR، لكن EAR مفضل لـ WAS -->

    <properties>
        <maven.compiler.source>11</maven.compiler.source> <!-- أو إصدار جافا الخاص بك -->
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- تبعيات تطبيقك -->
        <!-- لـ APIs وقت الترجمة الخاصة بـ WAS (نطاق provided) -->
        <dependency>
            <groupId>com.ibm.tools.target</groupId>
            <artifactId>was</artifactId>
            <version>9.0</version> <!-- طابق إصدار WAS الخاص بك، مثلاً 8.5.5 أو 9.0 -->
            <type>pom</type>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- بناء EAR (اضبط لـ WAR إذا لزم الأمر) -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- تكوين EAR الخاص بك، الوحدات، إلخ. -->
                </configuration>
            </plugin>

            <!-- تصفية الموارد & تجاوزات خاصة بملف التعريف -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-resources-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <useDefaultDelimiters>true</useDefaultDelimiters>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- ملفات التعريف -->
    <profiles>
        <!-- ملف تعريف محلي/تطوير: مستخدم ثابت، تسجيل دخول بالنموذج أو بدون أمان -->
        <profile>
            <id>local</id>
            <activation>
                <activeByDefault>true</activeByDefault> <!-- افتراضي للبناءات المحلية -->
            </activation>
            <build>
                <resources>
                    <!-- الموارد المشتركة -->
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <!-- تجاوز بملفات خاصة بالمحلي -->
                    <resource>
                        <directory>src/local/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- مثال على خصائص مصفاة لمستخدم مشفر محلي -->
                <app.login.user>devuser</app.login.user>
                <app.login.password>devpass</app.login.password>
            </properties>
        </profile>

        <!-- ملف تعريف خادم/إنتاج: SSO حقيقي (مثل SPNEGO، LTPA، أو OpenIDConnect) -->
        <profile>
            <id>server</id>
            <build>
                <resources>
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <resource>
                        <directory>src/server/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- خصائص الإنتاج، مثلاً تمكين أعلام SSO -->
                <app.auth.method>SSO</app.auth.method>
            </properties>
        </profile>
    </profiles>
</project>
```

### النقاط الرئيسية لاختلافات المصادقة
- **المحلي**: استخدم تسجيل دخول بالنموذج مع مستخدمين/أدوار بسيطة في `web.xml` أو ملف properties، أو عطّل الأمان تمامًا (إزالة `<security-constraint>`).
- **الخادم**: قم بتكوين SSO الخاص بـ WAS في `web.xml` (مثل `<auth-method>FORM</auth-method>` مع SPNEGO، أو استخدم ميزة OpenID Connect بأسلوب Liberty، لكن بالنسبة لـ WAS التقليدي غالبًا ما يكون LTPA + مجال أمان عام). يمكن أيضًا تجاوز روابط WAS (`ibm-web-bnd.xml`) لكل ملف تعيين لتعيينات المستخدم/الدور.
- إذا كنت تستخدم Spring Security أو ما شابه، فقم بتبديل `applicationContext-security.xml` أو properties بنفس الطريقة.
- للمستخدم المحلي المشفر: تجنب بيانات الاعتماد المشفرة الحقيقية؛ استخدم مستخدم اختبار معين في ملف `users.properties` محلي أو عطّل فحوصات المصادقة عبر علامة.

### أوامر البناء
- محلي (افتراضي): `mvn clean package`
- خادم/إنتاج: `mvn clean package -Pserver`

ينتج هذا ملفات EAR مختلفة مصممة خصيصًا لكل بيئة من **نفس قاعدة الكود**. إذا كنت تحتاج حقًا إلى أسماء artifacts منفصلة (مثل `myapp-local.ear` مقابل `myapp.ear`)، أضف `<finalName>${project.artifactId}-${profile}</finalName>` في أقسام `<build>` الخاصة بملف التعريف.

[Maven Profiles Guide](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)  
[Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/)  
[IBM WAS Maven Integration](https://www.ibm.com/docs/en/wasdtfe/9.7.0?topic=suye-configuring-dependency-pom-files-that-emulate-classpath-specific-websphere-runtime-environments)