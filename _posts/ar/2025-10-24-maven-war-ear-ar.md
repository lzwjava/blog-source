---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: إعداد وحدات Maven من نوع WAR وEAR
translated: true
type: note
---

### إعداد مشروع Maven متعدد الوحدات لتحويل WAR إلى EAR

في Maven، لجعل وحدة واحدة تنتج ملف WAR (على سبيل المثال، تطبيق ويب) وتقوم وحدة أخرى بتجميعه في ملف EAR (أرشيف المؤسسة)، استخدم هيكل مشروع متعدد الوحدات. تعتمد وحدة EAR على وحدة WAR عبر `maven-ear-plugin`. هذا يضمن تضمين WAR في EAR أثناء عملية البناء.

#### الخطوة 1: إنشاء Parent POM
يحدد Parent POM الوحدات ويدير التكوينات المشتركة. اضبط تعبئته على `pom`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>parent</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>web-module</module>  <!-- Build this first -->
        <module>ear-module</module>
    </modules>

    <!-- Optional: Shared dependencies and plugin versions -->
    <dependencyManagement>
        <dependencies>
            <!-- Define versions for child modules here -->
        </dependencies>
    </dependencyManagement>

    <build>
        <pluginManagement>
            <plugins>
                <!-- Manage plugin versions -->
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-ear-plugin</artifactId>
                    <version>3.3.0</version>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
</project>
```

#### الخطوة 2: تكوين وحدة WAR
تبني هذه الوحدة تطبيق الويب كملف WAR. اضبط تعبئتها على `war`. لا حاجة لتكوين خاص بـ EAR هنا—كل ما تحتاجه هو أن تُبنى أولاً.

هيكل الدليل: `web-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>web-module</artifactId>
    <packaging>war</packaging>

    <dependencies>
        <!-- Add your web dependencies, e.g., servlet-api -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

#### الخطوة 3: تكوين وحدة EAR
تقوم هذه الوحدة بتجميع ملف EAR. اضبط تعبئتها على `ear` واستخدم `maven-ear-plugin` للإشارة إلى وحدة WAR. سيقوم البرنامج المساعد بسحب قطعة أثرية WAR وتضمينها في EAR.

هيكل الدليل: `ear-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>ear-module</artifactId>
    <packaging>ear</packaging>

    <dependencies>
        <!-- Depend on the WAR module to include it in the build -->
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>web-module</artifactId>
            <version>${project.version}</version>
            <type>war</type>
        </dependency>
        <!-- Optional: Add EJB or other modules if needed -->
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- EAR version (e.g., for Java EE) -->
                    <version>8</version>
                    
                    <!-- Directory for libraries in EAR -->
                    <defaultLibBundleDir>lib</defaultLibBundleDir>
                    
                    <!-- Skinny WARs (exclude dependencies already in EAR libs) -->
                    <skinnyWars>true</skinnyWars>
                    
                    <!-- Define modules to include -->
                    <modules>
                        <webModule>
                            <groupId>com.example</groupId>
                            <artifactId>web-module</artifactId>
                            <bundleDir>/</bundleDir>  <!-- Root of EAR -->
                            <contextRoot>/mywebapp</contextRoot>  <!-- Deployment context -->
                        </webModule>
                        <!-- Add more <ejbModule> or <jarModule> if needed -->
                    </modules>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### الخطوة 4: بناء المشروع
- شغّل من **الدليل الرئيسي للمشروع**: `mvn clean install`
  - هذا يبني الوحدات بالترتيب (WAR أولاً، ثم EAR).
- سيكون ملف EAR في `ear-module/target/ear-module-1.0-SNAPSHOT.ear`.
- لبناء EAR فقط (بافتراض أن WAR مبنية مسبقاً): `cd ear-module && mvn clean package`.

#### ملاحظات رئيسية
- **ترتيب البناء**: اذكر وحدة WAR قبل وحدة EAR في `<modules>` الخاصة بالـ Parent لضمان أن Maven يبني WAR أولاً.
- **التبعيات**: تبعية `<dependency>` لوحدة EAR على وحدة WAR تضمن حلها أثناء التعبئة.
- **التخصيص**: اضبط `<contextRoot>` لمسار URL لتطبيق الويب. أضف المزيد من الوحدات (مثل EJB JARs) في `<modules>`.
- **استكشاف الأخطاء وإصلاحها**: إذا لم يتم تضمين WAR، تحقق من تطابق إحداثيات القطعة الأثرية تماماً. استخدم `mvn dependency:tree` في وحدة EAR للتحقق.

لمزيد من التفاصيل، راجع وثائق برنامج Maven EAR Plugin المساعد الرسمي.

[Apache Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/)  
[Maven Multi-Module Projects](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#Multi-module_Projects)