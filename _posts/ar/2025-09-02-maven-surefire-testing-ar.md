---
audio: false
generated: true
image: false
lang: ar
layout: post
title: دليل اختبار الوحدة لإضافة مافن شورفاير
translated: true
type: note
---

**إضافة Maven Surefire** هي الإضافة التي تُشغِّل اختبارات الوحدة الخاصة بك خلال مرحلة **الاختبار (test)** من دورة حياة بناء Maven. إنها واحدة من أكثر إضافات Maven استخدامًا لأن كل مشروع تقريبًا يحتاج إلى دمج الاختبارات الآلية في عملية البناء الخاصة به.

---

## ما هي

*   **الاسم**: `maven-surefire-plugin`
*   **الغرض**: تنفيذ الاختبارات المكتوبة باستخدام أطر عمل مثل JUnit (3, 4, 5)، TestNG، إلخ.
*   **المرحلة**: مرتبطة بمرحلة `test` من دورة الحياة الافتراضية لـ Maven.
*   **المخرجات**: يُنشئ تقارير الاختبارات (افتراضيًا في `target/surefire-reports`).

---

## كيف تعمل

1.  عندما تُشغِّل `mvn test` أو `mvn package`، يستدعي Maven إضافة Surefire.
2.  تفحص دليل `src/test/java` الخاص بك للعثور على فئات الاختبار.
3.  افتراضيًا، تبحث عن الملفات التي تطابق الاصطلاحات التسمية مثل:
    *   `*Test.java`
    *   `Test*.java`
    *   `*Tests.java`
    *   `*TestCase.java`
4.  تُنفذها في عازل فئات (isolated classloader).
5.  تكتب النتائج في `target/surefire-reports` (نص عادي، XML، وأحيانًا HTML عبر إضافات التقارير).

---

## الاستخدام الأساسي

يمكنك تكوينها في ملف `pom.xml` الخاص بك:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>3.2.5</version> <!-- استخدم الأحدث المستقر -->
    </plugin>
  </plugins>
</build>
```

بعد ذلك، قم فقط بتشغيل:

```bash
mvn test
```

---

## التكوينات الشائعة

*   **أنماط التضمين/الاستبعاد**:

```xml
<configuration>
  <includes>
    <include>**/*MyTest.java</include>
  </includes>
  <excludes>
    <exclude>**/IntegrationTest.java</exclude>
  </excludes>
</configuration>
```

*   **خصائص النظام**:

```xml
<configuration>
  <systemPropertyVariables>
    <env>dev</env>
  </systemPropertyVariables>
</configuration>
```

*   **تنفيذ الاختبارات بالتوازي**:

```xml
<configuration>
  <forkCount>2</forkCount>
  <reuseForks>true</reuseForks>
  <parallel>classes</parallel>
</configuration>
```

هذا يُشغِّل الاختبارات في عمليات JVM متعددة أو خيوط تنفيذ.

---

## متى تستخدمها

*   في أي وقت تريد دمج **اختبارات الوحدة** في دورة حياة Maven الخاصة بك.
*   لفصل **اختبارات الوحدة (Surefire)** عن **اختبارات التكامل (إضافة Failsafe)**:
    *   Surefire → اختبارات الوحدة (`mvn test`)
    *   Failsafe → اختبارات التكامل (`mvn verify`)

---

✅ **باختصار**: `maven-surefire-plugin` هي الإضافة الأساسية التي تلجأ إليها لتنفيذ اختبارات الوحدة في مشاريع Maven. تقوم بتكوينها في `pom.xml`، وتشغلها بـ `mvn test`، وتراجع التقارير في `target/surefire-reports`.

---

هل تريد مني أيضًا شرح **الفرق بين Surefire و Failsafe** (نظرًا لأنهما غالبًا ما يُخلط بينهما)؟