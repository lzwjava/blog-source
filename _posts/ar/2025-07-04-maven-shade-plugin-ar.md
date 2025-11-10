---
audio: false
generated: true
lang: ar
layout: post
title: 'إضافة Maven للتظليل: إنشاء حزم JAR الشاملة'
translated: true
type: note
---

`maven-shade-plugin` هو إضافة (plugin) لـ Maven تُستخدم لإنشاء "JAR شامل" (ملف JAR واحد مكتفٍ ذاتيًا) من خلال دمج الكود المترجم للمشروع مع تبعياته. يشيع استخدامه في مشاريع Java لتعبئة التطبيق وجميع المكتبات المطلوبة في ملف JAR قابل للتنفيذ، مما يبسط عملية التوزيع والنشر.

### التفاصيل الرئيسية:
- **معرف المجموعة (Group ID)**: `org.apache.maven.plugins` (يشير إلى أنها إضافة رسمية من Apache Maven).
- **معرف القطعة (Artifact ID)**: `maven-shade-plugin` (اسم الإضافة المحدد).
- **الغرض**:
  - **التظليل (Shading)**: يعيد توجيه (إعادة تسمية) حزم التبعيات لتجنب تعارضات الفئات (على سبيل المثال، عندما تستخدم عدة مكتبات إصدارات مختلفة من نفس الفئة).
  - **التعبئة (Packaging)**: يحزم التبعيات في ملف JAR النهائي، مما يجعله مكتفيًا ذاتيًا.
  - **تحويل الموارد (Resource Transformation)**: يمكنه تعديل الموارد (على سبيل المثال، دمج ملفات التكوين مثل `MANIFEST.MF`).
- **حالات الاستخدام الشائعة**:
  - إنشاء ملفات JAR قابلة للتنفيذ لتطبيقات سطر الأوامر.
  - حل تعارضات مسار الفئة (classpath) في المشاريع التي تحتوي على تبعيات متعددة.
  - تبسيط النشر لتطبيقات مثل وظائف Spark أو Hadoop.
- **كيف يعمل**:
  - يتم تكوينه في ملف `pom.xml` ضمن قسم `<plugins>`.
  - أثناء عملية البناء (عادة في مرحلة `package`)، يجمع الفئات والموارد، ويعيد توجيه الحزم بشكل اختياري، وينتج ملف JAR النهائي.
- **مثال للتكوين** في `pom.xml`:
  ```xml
  <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-shade-plugin</artifactId>
      <version>3.5.0</version> <!-- استخدم أحدث إصدار -->
      <executions>
          <execution>
              <phase>package</phase>
              <goals>
                  <goal>shade</goal>
              </goals>
              <configuration>
                  <transformers>
                      <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                          <mainClass>com.example.Main</mainClass>
                      </transformer>
                  </transformers>
              </configuration>
          </execution>
      </executions>
  </plugin>
  ```
  يحدد هذا المثال الفئة الرئيسية (main class) لملف JAR قابل للتنفيذ ويشغّل الإضافة خلال مرحلة `package`.

- **الميزات الرئيسية**:
  - **إدراج التبعيات**: تضمين التبعيات في ملف JAR.
  - **إعادة توجيه الحزم**: إعادة تسمية الحزم لتجنب التعارضات (على سبيل المثال، `com.google.common` إلى `shaded.com.google.common`).
  - **تصفية الموارد**: دمج أو تحويل ملفات الموارد.
  - **JAR قابل للتنفيذ**: إضافة إدخالات إلى البيان (manifest) لجعل ملف JAR قابلاً للتنفيذ باستخدام `java -jar`.

### متى تستخدمه:
- عندما تحتاج إلى ملف JAR واحد لتسهيل التوزيع.
- عند التعامل مع تعارضات التبعيات (على سبيل المثال، إصدارات مختلفة من نفس المكتبة).
- لنشر التطبيقات في بيئات يصعب فيها إدارة التبعيات الخارجية.

إذا كان لديك سؤال محدد حول تكوينه أو حالة استخدامه، دعني أعلم!