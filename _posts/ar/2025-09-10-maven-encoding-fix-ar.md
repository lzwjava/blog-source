---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: إصلاح تحذيرات ترميز منصة Maven
translated: true
type: note
---

تحذير Maven هذا يعني أن عملية بناء مشروعك تعتمد على **ترميز المنصة الافتراضي** (مثل GBK على نظام Windows الصيني). إذا استخدم مطورون آخرون أو خوادم CI ترميزًا مختلفًا (مثل UTF-8 على Linux)، فقد يتم قراءة ملفات النص (مثل ملفات Java المصدر، وخصائص properties، وXML، إلخ) أو تجميعها بشكل خاطئ.

إليك كيفية إصلاح ذلك:

---

### 1. تعيين ترميز المصدر في ملف `pom.xml`

في قسم `<properties>` لمشروعك، عيّن الترميز بشكل صريح:

```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <maven.compiler.encoding>UTF-8</maven.compiler.encoding>
</properties>
```

هذا يضمن أن Maven يقوم بتجميع المصادر وإنشاء التقارير بشكل متسق باستخدام UTF-8، بغض النظر عن الترميز الافتراضي لنظام التشغيل.

---

### 2. تكوين إضافة المترجم (إذا لم تكن مضبوطة مسبقًا)

تتطلب بعض إعدادات Maven القديمة تعيين الترميز ضمن إضافة المترجم:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
                <encoding>UTF-8</encoding>
            </configuration>
        </plugin>
    </plugins>
</build>
```

---

### 3. التحقق من ترميز الملفات

* تأكد من أن ملفاتك مثل `.java` و`.properties` و`.yml` إلخ، محفوظة بترميز UTF-8 وليس GBK.
* في IntelliJ IDEA أو VS Code، عيّن **File Encoding = UTF-8** في إعدادات المشروع.
* بالنسبة لـ Git، يمكنك فرض ترميز متسق باستخدام ملف `.gitattributes` إذا لزم الأمر.

---

### 4. تشغيل Maven مع ترميز صريح (اختياري)

يمكنك أيضًا تجاوز الترميز عند تشغيل Maven:

```bash
mvn clean install -Dfile.encoding=UTF-8
```

لكن أفضل ممارسة هي إصلاح المشكلة داخل ملف `pom.xml`، لضمان الاتساق للجميع.

---

✅ بعد هذه التغييرات، يجب أن يختفي تحذير "الترميز المعتمد على المنصة GBK"، وسيصبح مشروع Spring + Maven الخاص بك آمنًا من مشاكل الترميز عبر مختلف الأجهزة.

هل تريد مني أيضًا أن أوضح لك كيفية **تحويل ملفات المصدر الحالية من ترميز GBK إلى UTF-8** بشكل آمن (بحيث يصبح مستودعك نظيفًا ومتسقًا)؟