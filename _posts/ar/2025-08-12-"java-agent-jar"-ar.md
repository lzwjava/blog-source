---
audio: false
generated: true
image: false
lang: ar
layout: post
title: كيفية العثور على أو إنشاء وكيل جافا في صيغة JAR
translated: true
type: note
---

`/path/to/java-agent.jar` في الكود الخاص بك هو مجرد عنصر نائب — لا يوجد "وكيل جافا" رسمي وعالمي يمكنك تنزيله يحتوي على `com.example.Agent`.

مكان الحصول على الملف الفعلي يعتمد كليًا على **أي وكيل جافا تريد الاتصال به**:

---

**1. إذا كان هذا وكيل الجافا الخاص بك**

* تحتاج إلى **كتابته وبناءه** بلغة جافا.
* أنشئ مشروع جافا مع الحزمة `com.example` وفئة `Agent` تنفذ الدوال `getJVMInfo()`، و`getMemoryUsage()`، و`getThreadInfo()`.
* قم بتجميعه وتعبئته في ملف JAR باستخدام أداة مثل Maven أو Gradle.
* مثال على أمر Maven:

  ```bash
  mvn clean package
  ```

  بعد البناء، ستجد `java-agent.jar` في الدليل `target/`.

---

**2. إذا كان جزءًا من أداة مراقبة/تحليل أداء محددة**

* أدوات مثل **VisualVM**، أو **Java Mission Control**، أو **YourKit**، أو **New Relic** لديها ملفات الوكيل JAR الخاصة بها.
* ستحتاج إلى تنزيل حزمة تلك الأداة من موقعها الإلكتروني والبحث عن ملف الوكيل JAR داخل مجلد `lib` أو `agent` الخاص بها.
* على سبيل المثال، وكيل YourKit غالبًا ما يُسمى بشيء مثل `yjpagent.jar`.

---

**3. إذا كان من مشروع على GitHub أو مشروع مفتوح المصدر**

* ابحث عن مستودع المشروع الذي يعرّف `com.example.Agent`.
* انسخ المستودع وقم ببنائه في ملف JAR.
* مثال:

  ```bash
  git clone https://github.com/username/java-agent.git
  cd java-agent
  mvn package
  ```

---

**4. إذا كنت تريد فقط اختبار اتصال Python–Java JPype الخاص بك**

* يمكنك إنشاء فئة وكيل جافا صغيرة بنفسك وتجميعها:

  ```java
  package com.example;

  public class Agent {
      public String getJVMInfo() {
          return System.getProperty("java.version");
      }
      public String getMemoryUsage() {
          return Runtime.getRuntime().freeMemory() + " free / " +
                 Runtime.getRuntime().totalMemory() + " total";
      }
      public String getThreadInfo() {
          return Thread.activeCount() + " active threads";
      }
  }
  ```

  ثم قم بتجميعه وتعبيئه في JAR:

  ```bash
  javac com/example/Agent.java
  jar cf java-agent.jar com/example/Agent.class
  ```

---

إذا كنت تريد، يمكنني **كتابة كود مصدر لوكيل جافا يعمل** بشكل مطابق تمامًا للواجهة التي كتبتها في Python، بحيث يمكنك تجميعه في `java-agent.jar` وتشغيل السكريبت الخاص بك فورًا. هل تريد مني تحضير ذلك؟