---
audio: false
generated: true
lang: ar
layout: post
title: JaCoCo Maven Plugin
translated: true
---

هنا دليل خطوة بخطوة على كيفية استخدام **مُفَضِّل JaCoCo Maven** لقياس تغطية الكود في مشروع Java مبني على Maven. JaCoCo (تغطية كود Java) هو أداة تتكامل مع Maven لتتبع كم من كودك يتم تمرينه بواسطة الاختبارات، عادةً الاختبارات الوحدوية. من خلال إضافة وتهيئة مُفَضِّل JaCoCo Maven في مشروعك، يمكنك إنشاء تقارير تغطية مفصلة خلال عملية البناء.

---

### **خطوات لاستخدام مُفَضِّل JaCoCo Maven**

#### **1. إضافة مُفَضِّل JaCoCo Maven إلى ملف `pom.xml` الخاص بك**
لاستخدام مُفَضِّل JaCoCo Maven، يجب عليك تضمينه في قسم `<build><plugins>` من ملف `pom.xml` الخاص بمشروعك. أدناه هو تكوين أساسي يهيئ المُفَضِّل:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- استخدم أحدث الإصدار المتاح -->
            <executions>
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>verify</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`groupId`, `artifactId`, و `version`**: هذه تعرّف مُفَضِّل JaCoCo Maven. استبدل `0.8.12` بأحدث الإصدار المتاح في [مستودع Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin).
- **`<executions>`**: هذا القسم يهيئ متى وكيف يعمل المُفَضِّل خلال دورة حياة بناء Maven:
  - **`<goal>prepare-agent</goal>`**: يهيئ وكيل JaCoCo لجمع بيانات التغطية أثناء تنفيذ الاختبارات. بشكل افتراضي، يربط إلى مرحلة مبكرة (مثل `initialize`) ولا يتطلب مرحلة صريحة إلا إذا تم تخصيصها.
  - **`<goal>report</goal>`**: يخلق التقرير التغطية بعد انتهاء الاختبارات. يربط إلى المرحلة `verify` هنا، والتي تحدث بعد المرحلة `test`، مما يضمن توفر جميع بيانات الاختبار.

#### **2. التأكد من تهيئة الاختبارات**
يعمل مُفَضِّل JaCoCo من خلال تحليل تنفيذ الاختبارات، عادةً الاختبارات الوحدوية التي تنفذها مُفَضِّل Maven Surefire. في معظم مشاريع Maven، Surefire مدمج بشكل افتراضي وينفذ الاختبارات الموجودة في `src/test/java`. لا تحتاج إلى تهيئة إضافية إلا إذا كانت اختباراتك غير معتادة. تأكد من:
- أن لديك اختبارات وحدوية مكتوبة (مثلًا باستخدام JUnit أو TestNG).
- أن مُفَضِّل Surefire موجود (يورث من POM الأب الافتراضي لمaven في معظم الحالات).

إذا كنت بحاجة إلى تهيئة Surefire بشكل صريح، قد يبدو ذلك على النحو التالي:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- استخدم أحدث الإصدار -->
</plugin>
```

يهيئ هدف `prepare-agent` وكيل JaCoCo من خلال تعديل خاصية `argLine` التي يستخدمها Surefire لنفذ الاختبارات مع تتبع التغطية مفعّل.

#### **3. تنفيذ بناء Maven**
لإنشاء التقرير التغطية، نفذ الأمر التالي في مجلد مشروعك:

```bash
mvn verify
```

- **`mvn verify`**: هذا ينفذ جميع المراحل حتى `verify`، بما في ذلك `compile`, `test`, و `verify`. سيقوم مُفَضِّل JaCoCo:
  1. بإعداد الوكيل قبل تنفيذ الاختبارات.
  2. جمع بيانات التغطية خلال المرحلة `test` (عندما ينفذ Surefire الاختبارات).
  3. إنشاء التقرير خلال المرحلة `verify`.

بدلاً من ذلك، إذا كنت تريد فقط تنفيذ الاختبارات دون الانتقال إلى `verify`, استخدم:

```bash
mvn test
```

لكن نظرًا لأن هدف `report` مرتبط بـ `verify` في هذا التهيئة، عليك تنفيذ `mvn verify` لرؤية التقرير. إذا كنت تفضل إنشاء التقرير أثناء `mvn test`, يمكنك تغيير `<phase>` لهدف `report` إلى `test`, ولكن `verify` هو عادات شائعة.

#### **4. عرض التقرير التغطية**
بعد تنفيذ `mvn verify`, يخلق JaCoCo تقريرًا HTML بشكل افتراضي. يمكنك العثور عليه في:

```
target/site/jacoco/index.html
```

- افتح هذا الملف في متصفح ويب لرؤية تحليل تفصيلي لتغطية الكود، بما في ذلك النسبة المئوية للحزم، الفئات، الأطوار، والخطوط.
- يتضمن التقرير أيضًا صيغ XML و CSV في نفس الدليل (`jacoco.xml` و `jacoco.csv`), مفيد للتكامل مع أدوات مثل أنظمة CI.

---

### **تخصيصات اختيارية**
لحالات استخدام متقدمة، يمكنك تعديل تهيئة المُفَضِّل:

- **استبعاد الفئات أو الحزم**:
  لاستبعاد بعض الكود من تحليل التغطية (مثل الكود المولّد)، أضف قسم `<configuration>`:

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  ضع هذا داخل علامة `<plugin>`, فوق `<executions>`.

- **تطبيق حدود التغطية**:
  لفعل بناء إذا كانت التغطية أقل من حد معين، أضف هدف `check`:

  ```xml
  <execution>
      <id>check</id>
      <phase>verify</phase>
      <goals>
          <goal>check</goal>
      </goals>
      <configuration>
          <rules>
              <rule>
                  <element>BUNDLE</element>
                  <limits>
                      <limit>
                          <counter>LINE</counter>
                          <value>COVEREDRATIO</value>
                          <minimum>0.80</minimum> <!-- 80% تغطية الخط -->
                      </limit>
                  </limits>
              </rule>
          </rules>
      </configuration>
  </execution>
  ```

- **تغيير دليل إخراج التقرير**:
  لتخصيص موقع التقرير، أضف:

  ```xml
  <configuration>
      <destFile>${project.build.directory}/custom-jacoco.exec</destFile>
      <dataFile>${project.build.directory}/custom-jacoco.exec</dataFile>
      <outputDirectory>${project.build.directory}/custom-reports</outputDirectory>
  </configuration>
  ```

---

### **ملخص**
لاستخدام مُفَضِّل JaCoCo Maven:
1. أضف المُفَضِّل إلى ملف `pom.xml` مع أهداف `prepare-agent` و `report`.
2. تأكد من أن مشروعك له اختبارات مهيئة (عادةً عبر Surefire).
3. نفذ `mvn verify` لإنشاء التقرير التغطية.
4. تحقق من التقرير في `target/site/jacoco/index.html`.

توفر هذه التهيئة طريقة بسيطة لتكامل تغطية الكود في عملية بناء Maven، مما يساعدك في تقييم فعالية اختباراتك. للحصول على أحدث إصدار للمُفَضِّل أو تهيئات متقدمة، راجع [التوثيق الرسمي لـ JaCoCo](https://www.jacoco.org/jacoco/trunk/doc/maven.html).