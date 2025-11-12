---
audio: false
generated: true
lang: ar
layout: post
title: إضافة مافن لجاكوكو
translated: true
type: note
---

إليك دليلًا خطوة بخطوة حول **كيفية استخدام إضافة JaCoCo Maven** لقياس تغطية الكود في مشروع Java قائم على Maven. JaCoCo (تغطية كود Java) هي أداة تندمج مع Maven لتتبع مقدار الكود الذي يتم تغطيته بواسطة الاختبارات، عادةً اختبارات الوحدة. من خلال إضافة وتكوين إضافة JaCoCo Maven في مشروعك، يمكنك إنشاء تقارير تغطية مفصلة أثناء عملية البناء.

---

### **خطوات استخدام إضافة JaCoCo Maven**

#### **1. إضافة إضافة JaCoCo Maven إلى ملف `pom.xml` الخاص بك**
لاستخدام إضافة JaCoCo Maven، تحتاج إلى تضمينها في قسم `<build><plugins>` في ملف `pom.xml` لمشروعك. فيما يلي تكوين أساسي لإعداد الإضافة:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- استخدم أحدث إصدار متاح -->
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

- **`groupId`, `artifactId`, و `version`**: هذه تحدد إضافة JaCoCo Maven. استبدل `0.8.12` بأحدث إصدار متاح على [Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin).
- **`<executions>`**: يكوّن هذا القسم متى وكيف تعمل الإضافة خلال دورة حياة بناء Maven:
  - **`<goal>prepare-agent</goal>`**: يُجهز وكيل JaCoCo لجمع بيانات التغطية أثناء تنفيذ الاختبارات. بشكل افتراضي، يرتبط بمرحلة مبكرة (مثل `initialize`) ولا يتطلب مرحلة صريحة ما لم يتم تخصيصه.
  - **`<goal>report</goal>`**: يولد تقرير التغطية بعد تشغيل الاختبارات. وهو مرتبط بمرحلة `verify` هنا، والتي تحدث بعد مرحلة `test`، مما يضمن توفر جميع بيانات الاختبار.

#### **2. التأكد من تكوين الاختبارات**
تعمل إضافة JaCoCo من خلال تحليل تنفيذ الاختبارات، عادةً اختبارات الوحدة التي يتم تشغيلها بواسطة Maven Surefire Plugin. في معظم مشاريع Maven، يتم تضمين Surefire افتراضيًا ويقوم بتشغيل الاختبارات الموجودة في `src/test/java`. لا حاجة لتكوين إضافي ما لم تكن اختباراتك غير قياسية. تحقق من:
- أن لديك اختبارات وحدة مكتوبة (باستخدام JUnit أو TestNG مثلاً).
- أن إضافة Surefire موجودة (يتم توريثها من الـ POM الأب الافتراضي لـ Maven في معظم الحالات).

إذا كنت بحاجة إلى تكوين Surefire صراحةً، فقد يبدو كالتالي:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- استخدم أحدث إصدار -->
</plugin>
```

يقوم هدف `prepare-agent` بإعداد وكيل JaCoCo عن طريق تعديل الخاصية `argLine`، والتي يستخدمها Surefire لتشغيل الاختبارات مع تمكين تتبع التغطية.

#### **3. تشغيل بناء Maven**
لتوليد تقرير التغطية، نفّذ الأمر التالي في دليل مشروعك:

```bash
mvn verify
```

- **`mvn verify`**: يشغل هذا جميع المراحل حتى `verify`، بما في ذلك `compile` و `test` و `verify`. ستقوم إضافة JaCoCo بما يلي:
  1. تجهيز الوكيل قبل تشغيل الاختبارات.
  2. جمع بيانات التغطية خلال مرحلة `test` (عندما ينفذ Surefire الاختبارات).
  3. توليد التقرير خلال مرحلة `verify`.

بدلاً من ذلك، إذا أردت تشغيل الاختبارات فقط دون المتابعة إلى `verify`، استخدم:

```bash
mvn test
```

ومع ذلك، نظرًا لأن هدف `report` مرتبط بمرحلة `verify` في هذا التكوين، ستحتاج إلى تشغيل `mvn verify` لرؤية التقرير. إذا كنت تفضل أن يتم توليد التقرير أثناء `mvn test`، يمكنك تغيير `<phase>` لتنفيذ `report` إلى `test`، على الرغم من أن `verify` هو الاتفاق الشائع.

#### **4. عرض تقرير التغطية**
بعد تشغيل `mvn verify`، يقوم JaCoCo بتوليد تقرير HTML افتراضيًا. يمكنك العثور عليه في:

```
target/site/jacoco/index.html
```

- افتح هذا الملف في متصفح الويب لعرض تحليل مفصل لتغطية الكود، بما في ذلك النسب المئوية للحزم والفئات والطرق والأسطر.
- يتضمن التقرير أيضًا تنسيقات XML و CSV في نفس الدليل (`jacoco.xml` و `jacoco.csv`)، وهي مفيدة للدمج مع أدوات مثل أنظمة CI.

---

### **تخصيصات اختيارية**
لحالات الاستخدام الأكثر تقدمًا، يمكنك تعديل تكوين الإضافة:

- **استبعاد فئات أو حزم**:
  لاستبعاد كود معين من تحليل التغطية (مثل الكود المُولَّد)، أضف قسم `<configuration>`:

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  ضع هذا داخل وسم `<plugin>`، فوق `<executions>`.

- **فرض حدود دنيا للتغطية**:
  لفشل البناء في حال انخفاض التغطية عن حد معين، أضف هدف `check`:

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
                          <minimum>0.80</minimum> <!-- 80% تغطية للأسطر -->
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
لاستخدام إضافة JaCoCo Maven:
1. أضف الإضافة إلى `pom.xml` الخاص بك مع أهداف `prepare-agent` و `report`.
2. تأكد من أن مشروعك يحتوي على اختبارات مُكونة (عادةً عبر Surefire).
3. شغّل `mvn verify` لتوليد تقرير التغطية.
4. افحص التقرير في `target/site/jacoco/index.html`.

يوفر هذا الإعداد طريقة مباشرة لدمج تغطية الكود في عملية بناء Maven الخاصة بك، مما يساعدك على تقييم فعالية اختباراتك. للحصول على أحدث إصدار من الإضافة أو التكوينات المتقدمة، راجع [توثيق JaCoCo الرسمي](https://www.jacoco.org/jacoco/trunk/doc/maven.html).