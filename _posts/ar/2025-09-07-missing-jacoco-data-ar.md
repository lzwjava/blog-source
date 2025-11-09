---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ar
layout: post
title: حل ملف بيانات تنفيذ JaCoCo المفقود
translated: true
type: note
---

لتوليد ملف بيانات تنفيذ JaCoCo، الذي يُشار إليه غالبًا باسم **ملف '.exec'**، تحتاج إلى تشغيل اختباراتك مع وكيل JaCoCo مرفق. تشير رسالة السجل "Skipping JaCoCo execution due to missing execution data file" إلى أن هدف `report` تم تنفيذه دون أن يكون الهدف `prepare-agent` قد تم تشغيله بنجاح أولاً.

-----

### الخطوة 1: تكوين إضافة Maven الخاصة بـ JaCoCo

أولاً، تأكد من أن ملف `pom.xml` الخاص بك يحتوي على إضافة Maven الخاصة بـ JaCoCo مُكونة بشكل صحيح. يجب أن يبدو كالتالي:

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.12</version>
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
        </execution>
    </executions>
</plugin>
```

إن الهدف **`prepare-agent`** حاسم لأنه يُنشئ وكيل وقت التشغيل لـ JaCoCo. يقوم هذا الوكيل بتجهيز الكود الخاص بك أثناء تشغيل الاختبارات لجمع بيانات التغطية.

-----

### الخطوة 2: تشغيل الاختبارات

بعد تكوين الإضافة، قم بتشغيل بناء Maven الخاص بك. الأمر النموذجي لتشغيل الاختبارات وتوليد التقرير هو:

`mvn clean install`

عند تشغيل هذا الأمر، ينفذ Maven هدف `prepare-agent` أولاً، والذي يرفق وكيل JaCoCo بـ JVM. ثم، عندما تعمل مرحلة `test`، يسجل الوكيل بيانات تغطية الكود ويحفظها في ملف، عادةً ما يكون موجودًا في **`target/jacoco.exec`**. بعد ذلك، يتم تنفيذ هدف `report`، الذي يقرأ ملف `.exec` هذا ويولد التقارير النهائية بصيغة HTML أو XML.

إذا كنت لا تزال تواجه مشاكل، تحقق من التالي:

  * **هيكل المشروع**: تأكد من أن اختباراتك موجودة في دليل Maven القياسي `src/test/java`.
  * **فشل الاختبارات**: إذا كانت اختباراتك تفشل، فقد يتوقف البناء قبل أن يتم إنشاء ملف `.exec`. قم بحل أي فشل في الاختبارات أولاً.
  * **عدم تطابق الإصدارات**: تأكد من أن إصدار إضافة JaCoCo متوافق مع إصدارات Maven و Java الخاصة بك.