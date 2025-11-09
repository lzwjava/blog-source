---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ar
layout: post
model: mistralai/mistral-medium-3.1
title: استبعاد حزم com.ibm في JaCoCo
translated: true
type: note
---

لاستبعاد حزم **`com.ibm`** (أو أي حزم أخرى) من تغطية JaCoCo في بيئة **WebSphere Liberty Profile**، يمكنك تكوين الاستثناءات في ملف **`pom.xml`** الخاص بك. يتم ذلك عادةً في تكوين **إضافة Maven الخاصة بـ JaCoCo**.

---

### **كيفية استبعاد حزم `com.ibm` في `pom.xml`**

يمكنك استخدام علامة `<excludes>` في تكوين إضافة JaCoCo لتحديد الفئات أو الحزم التي يجب استبعادها من تقارير التغطية.

#### **مثال على التكوين:**

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.11</version> <!-- استخدم أحدث إصدار -->
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
                    <configuration>
                        <outputDirectory>${project.reporting.outputDirectory}/jacoco</outputDirectory>
                        <excludes>
                            <!-- استبعاد جميع حزم com.ibm -->
                            <exclude>com/ibm/**</exclude>
                        </excludes>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

---

### **الشرح:**
- **`<excludes>`**: يحدد هذا القسم الفئات أو الحزم التي يجب استبعادها من تقارير التغطية.
- **`<exclude>com/ibm/**</exclude>`**: يستبعد هذا جميع الفئات الموجودة تحت حزمة `com.ibm` والحزم الفرعية التابعة لها.

---

### **ملاحظات إضافية:**
- إذا كنت تريد استبعاد حزم متعددة، أضف المزيد من إدخالات `<exclude>`:
  ```xml
  <excludes>
      <exclude>com/ibm/**</exclude>
      <exclude>org/apache/**</exclude>
  </excludes>
  ```
- إذا كنت تستخدم **JaCoCo مع WebSphere Liberty**، فتأكد من تكوين وكيل JaCoCo بشكل صحيح في ملف `server.env` أو `jvm.options` الخاص بك، وأن الاستثناءات في ملف `pom.xml` تتماشى مع متطلباتك.

---

### **أفضل الممارسات:**
- تحقق دائمًا من عمليات الاستبعاد عن طريق تشغيل تقرير تغطية والتحقق من عدم تضمين الحزم المستبعدة في النتائج.
- إذا كنت بحاجة إلى استبعاد حزم أثناء وقت التشغيل (على سبيل المثال، في وسيطات وكيل JaCoCo)، يمكنك استخدام المعامل `excludes` في وسيطات الوكيل:
  ```plaintext
  -javaagent:/path/to/jacocoagent.jar=destfile=/path/to/jacoco.exec,excludes=com.ibm.*
  ```