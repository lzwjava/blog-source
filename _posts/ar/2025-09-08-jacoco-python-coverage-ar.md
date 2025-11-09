---
audio: false
date: 2025-09-08
generated: true
image: false
lang: ar
layout: post
title: استراتيجية تغطية جاكوكو لاختبارات بايثون
translated: true
type: note
---

# تحليل واستراتيجية تغطية JaCoCo مع اختبارات تكامل Python

## تحليل الوضع الحالي

لقد قمت بإعداد مشروع Maven متعدد الوحدات مع:
- POM الأصلي (`PlaygroundLib`)
- وحدة `PlaygroundUtils` (JAR يحتوي على فئات الأدوات المساعدة)
- وحدة `PlaygroundWeb` (WAR يحتوي على وحدات تحكم Spring MVC)

هدفك هو استخدام `unittest` الخاص بـ Python لاختبار نقاط نهاية API وإنشاء تقارير تغطية للكود Java. التحدي هو أن اختبارات Python موجودة خارج مشروع Java، وتحتاج إلى تشغيل Jetty لتقديم التطبيق أثناء الاختبار.

## مشاكل النهج الحالي

1. **مشكلة التشغيل المتعدد**: تقوم بتشغيل `PlaygroundWeb` عدة مرات لإنشاء تقارير تغطية منفصلة للوحدات المختلفة، وهو أمر غير فعال.

2. **مشكلة قابلية التوسع**: هذا النهج لن يعمل بشكل جيد مع المزيد من الوحدات. لمشروع به 10 وحدات، ستحتاج إلى 10 عمليات تشغيل منفصلة.

3. **تجزئة التغطية**: التقارير لكل وحدة تجعل من الصعب الحصول على رؤية شاملة للتغطية عبر التطبيق بأكمله.

## الاستراتيجية الموصى بها

### 1. نهج جمع التغطية الموحد

بدلاً من تشغيل التطبيق عدة مرات، أوصي بما يلي:

1. **تشغيل تطبيق الويب مرة واحدة** مع إرفاق وكيل JaCoCo
2. **تنفيذ جميع اختبارات تكامل Python** ضد هذه النسخة المفردة
3. **إنشاء تقرير تغطية موحد** يشمل جميع الوحدات

هذا النهج أكثر كفاءة ويوفر رؤية موحدة للتغطية عبر تطبيقك بأكمله.

### 2. خطوات التنفيذ

#### تعديلات POM الأصلي (`PlaygroundLib`)

أضف ملف تعريف لاختبار التكامل مع JaCoCo:

```xml
<profiles>
    <profile>
        <id>integration-test</id>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.jacoco</groupId>
                    <artifactId>jacoco-maven-plugin</artifactId>
                    <executions>
                        <execution>
                            <id>merge</id>
                            <phase>post-integration-test</phase>
                            <goals>
                                <goal>merge</goal>
                            </goals>
                            <configuration>
                                <fileSets>
                                    <fileSet>
                                        <directory>${project.basedir}</directory>
                                        <includes>
                                            <include>*/target/jacoco-it.exec</include>
                                        </includes>
                                    </fileSet>
                                </fileSets>
                                <destFile>${project.build.directory}/jacoco-merged.exec</destFile>
                            </configuration>
                        </execution>
                        <execution>
                            <id>report-merged</id>
                            <phase>verify</phase>
                            <goals>
                                <goal>report</goal>
                            </goals>
                            <configuration>
                                <dataFile>${project.build.directory}/jacoco-merged.exec</dataFile>
                                <outputDirectory>${project.reporting.outputDirectory}/jacoco-merged</outputDirectory>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
```

#### تعديلات PlaygroundWeb POM

عدل تكوين وكيل JaCoCo ليشمل جميع الوحدات:

```xml
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
                    -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.build.directory}/jacoco-it.exec,includes=org.lzw.*
                </jvmArgs>
                <!-- باقي التكوين يبقى كما هو -->
            </configuration>
        </execution>
        <!-- باقي عمليات التنفيذ تبقى كما هي -->
    </executions>
</plugin>
```

لاحظ إضافة `includes=org.lzw.*` في تكوين وكيل JaCoCo. هذا يضمن تضمين جميع الفئات في حزمة `org.lzw` (عبر جميع الوحدات) في تقرير التغطية.

### 3. تدفق التنفيذ

سيكون تدفق التنفيذ الموصى به كما يلي:

```bash
# بناء جميع الوحدات
mvn clean install

# تشغيل اختبارات التكامل مع التغطية
mvn verify -Pintegration-test
```

هذا سوف:
1. يترجم جميع الوحدات
2. يبدأ Jetty مع إرفاق وكيل JaCoCo
3. يشغل اختبارات تكامل Python
4. يوقف Jetty
5. ينشئ تقرير تغطية مدمج لجميع الوحدات

### 4. التوسع للمشاريع الأكبر

لمشروع أكبر بعشر وحدات:

1. **الوحدات الويب** (مثل `PlaygroundWeb`) سيتم تكوينها لتشغيل التطبيق مع إرفاق وكيل JaCoCo.
2. **وحدات الأدوات المساعدة** (مثل `PlaygroundUtils`) لن تحتاج إلى تكوين خاص.
3. سيتعامل POM الأصلي مع دمج بيانات التغطية من جميع الوحدات.

إذا كان لديك وحدات ويب متعددة تحتاج إلى اختبارها بشكل مستقل، يمكنك إنشاء ملفات تعريف Maven منفصلة لكل وحدة ويب وتشغيل اختبارات التكامل لكل منها بشكل منفصل، ثم دمج جميع بيانات التغطية على مستوى الأصل.

### 5. معالجة تعقيد JaCoCo

لإدارة تعقيد JaCoCo:

1. **احصر التكوين** في ملفات تعريف Maven للحفاظ على نظافة POM الرئيسي
2. **وثق العملية** بوضوح حتى يفهم أعضاء الفريق كيفية تشغيل الاختبارات وإنشاء التقارير
3. **فكر في أتمتة CI/CD** لتقليل التعقيد اليدوي للمطورين

## الملخص

يجمع النهج الموصى به جمع التغطية عن طريق تشغيل تطبيق الويب مرة واحدة مع إرفاق وكيل JaCoCo، وتنفيذ جميع اختبارات تكامل Python ضد هذه النسخة، وإنشاء تقرير تغطية موحد. هذا النهج أكثر كفاءة وقابلية للتوسع ويوفر رؤية موحدة للتغطية عبر تطبيقك بأكمله.

يجب أن تحل هذه الاستراتيجية تحدياتك الحالية وتتوسع بشكل جيد مع نمو مشروعك، مع تبسيط إدارة تعقيد JaCoCo.