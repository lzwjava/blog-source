---
audio: false
date: 2025-09-08
generated: true
image: false
lang: ar
layout: post
title: استراتيجية جاكوكو للإبلاغ عن التغطية متعددة الوحدات
translated: true
type: note
---

بالتأكيد. تحليلك دقيق، خاصة فيما يتعلق بتعقيدات JaCoCo مع اختبارات التكامل الخارجية. تشغيل البناء مرتين ليس مثالياً بالتأكيد.

الإستراتيجية التي تبحث عنها تتضمن تنفيذ الاختبارات بشكل مركزي ثم تجميع النتائج. أنت قريب جداً، وهدف `aggregate` هو بالفعل الأداة المناسبة، لكن يجب تطبيقه بطريقة محددة لهذا السيناريو.

هذه هي الإستراتيجية الموصى بها: **قم بإنشاء ملف تغطية واحد (`.exec`) في وحدة تطبيق الويب الخاصة بك، ثم استخدم وحدة تقارير منفصلة ومخصصة لإنشاء تقرير واحد ومجمع لجميع الوحدات النمطية ذات الصلة.**

هذا النهج نظيف، قابل للتطوير، ويتجنب عمليات البناء المكررة.

-----

## المفهوم الأساسي

عندما يعمل تطبيق `PlaygroundWeb` الخاص بك على Jetty مع وكيل JaCoCo، فإن الوكيل يقوم بتجهيز **جميع الفئات التي يتم تحميلها بواسطة محمل فئات التطبيق**. وهذا يشمل الفئات من `PlaygroundWeb` نفسها *وجميع* تبعياتها، مثل `PlaygroundUtils.jar`.

لذلك، فإن ملف `jacoco-it.exec` الواحد الذي تم إنشاؤه أثناء بناء `PlaygroundWeb` يحتوي بالفعل على بيانات التغطية **لكلا الوحدتين**. التحدي ببساطة هو توجيه أداة تقارير JaCoCo إلى الكود المصدري لجميع الوحدات النمطية التي تحتاجها لبناء التقرير النهائي بتنسيق HTML.

-----

## إستراتيجية قابلة للتطوير في 4 خطوات

إليك دليل خطوة بخطوة لإعادة هيكلة مشروعك للحصول على تقارير تغطية مجمعة ونظيفة.

### الخطوة 1: إنشاء وحدة تقارير مخصصة

أولاً، قم بإنشاء وحدة نمطية جديدة مخصصة حصريًا للتجميع. هذه ممارسة مثلى في Maven تحافظ على فصل المهام.

1.  في ملف `pom.xml` الرئيسي الخاص بك (`PlaygroundLib`)، أضف الوحدة النمطية الجديدة:
    ```xml
    <modules>
        <module>PlaygroundUtils</module>
        <module>PlaygroundWeb</module>
        <module>PlaygroundReports</module> </modules>
    ```
2.  قم بإنشاء دليل جديد `PlaygroundReports` في المجلد الرئيسي مع ملف `pom.xml` الخاص به.

سيبدو هيكل المشروع الجديد الخاص بك هكذا:

```
.
├── PlaygroundReports
│   └── pom.xml
├── PlaygroundUtils
│   └── pom.xml
├── PlaygroundWeb
│   └── pom.xml
└── pom.xml
```

### الخطوة 2: تكوين ملف `pom.xml` لوحدة التقارير

ملف `pom.xml` الجديد هذا هو حيث تحدث السحر. سيعتمد على جميع الوحدات النمطية التي تريد تضمينها في التقرير وسيقوم بتنفيذ هدف `report-aggregate`.

**`PlaygroundReports/pom.xml`:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.lzw</groupId>
        <artifactId>PlaygroundLib</artifactId>
        <version>1.0</version>
    </parent>
    <artifactId>PlaygroundReports</artifactId>
    <packaging>pom</packaging>
    <name>PlaygroundReports</name>

    <dependencies>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundWeb</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundUtils</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <executions>
                    <execution>
                        <id>aggregate-report</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>report-aggregate</goal>
                        </goals>
                        <configuration>
                            <dataFiles>
                                <dataFile>${project.basedir}/../PlaygroundWeb/target/jacoco-it.exec</dataFile>
                            </dataFiles>
                            <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### الخطوة 3: تبسيط وحدة `PlaygroundWeb`

وحدة `PlaygroundWeb` الخاصة بك أصبحت مسؤولة الآن فقط عن **إنشاء بيانات التغطية**، وليس عن إنشاء التقرير عنها. يمكنك إزالة تنفيذ `jacoco:report` من ملف `pom.xml` الخاص بها.

**`PlaygroundWeb/pom.xml` (التغييرات فقط):**

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
            <configuration>
                <propertyName>jacoco.it.agent</propertyName>
                <destFile>${project.build.directory}/jacoco-it.exec</destFile>
            </configuration>
        </execution>
        </executions>
</plugin>

<plugin>
    <groupId>org.eclipse.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>start-jetty</id>
            <phase>pre-integration-test</phase>
            <goals>
                <goal>start</goal>
            </goals>
            <configuration>
                <daemon>true</daemon>
                <jvmArgs>
                    ${jacoco.it.agent}
                </jvmArgs>
                </configuration>
        </execution>
        </executions>
</plugin>
```

*ملاحظة*: لقد قمت بتعديل تكوين `prepare-agent` قليلاً لاستخدام خاصية (`jacoco.it.agent`) ثم الإشارة إلى تلك الخاصية في `jetty-maven-plugin`. هذه طريقة قوية لتمرير سلسلة الوكيل. التكوين السابق في ملف `pom.xml` الخاص بك كان جيداً أيضاً، لكن هذا يجعل القصد أكثر وضوحاً.

### الخطوة 4: تنظيف وحدة `PlaygroundUtils`

لا تحتاج وحدة `PlaygroundUtils` إلى أي تكوين لبرنامج JaCoCo plugin لاختبارات التكامل. يتم تغطية كودها عبر `PlaygroundWeb`، ويتم التعامل مع التقارير بواسطة `PlaygroundReports`. يمكنك إزالة أي خصائص أو إضافات متعلقة بـ JaCoCo من ملف `pom.xml` الخاص بها.

-----

## كيف يحل هذا المشكلة

1.  **بناء واحد:** تقوم بتشغيل `mvn clean verify` من الدليل الرئيسي مرة واحدة فقط.
2.  **دورة حياة صحيحة:**
      * يقوم Maven ببناء `PlaygroundUtils`.
      * يقوم Maven ببناء `PlaygroundWeb`، ويشغل Jetty مع وكيل JaCoCo، وينفذ اختبارات Python الخاصة بك (والتي تصل إلى الكود في كلا الوحدتين)، ويوقف Jetty، وينتج ملف `PlaygroundWeb/target/jacoco-it.exec`.
      * يقوم Maven ببناء `PlaygroundReports`. في مرحلة `verify`، يتم تشغيل هدف `report-aggregate`. يجد ملف `.exec` من `PlaygroundWeb`، وبسبب التبعيات، يعرف مكان العثور على الكود المصدري لكل من `PlaygroundWeb` و `PlaygroundUtils`.
      * يولد **تقرير HTML موحد واحد** مع تغطية لكلتا الوحدتين.
3.  **القدرة على التطوير:** إذا أضفت عشر وحدات مكتبية أخرى، فما عليك سوى إضافتها كتبعيات لملف `PlaygroundReports/pom.xml`. المنطق الأساسي لا يتغير. هذا هو الحل النظيف والقابل للتطوير الذي كنت تبحث عنه.