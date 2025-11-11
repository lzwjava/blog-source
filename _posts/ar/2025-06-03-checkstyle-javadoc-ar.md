---
audio: false
generated: true
lang: ar
layout: post
title: تعطيل فحوصات جافادوك في تشيك ستايل
translated: true
type: note
---

لتكوين Checkstyle لتجاهل جميع الفحوصات المتعلقة بـ Javadoc ومعاملتها على أنها غير مخالفة، تحتاج إلى تعديل ملف تكوين Checkstyle الخاص بك (عادةً `checkstyle.xml`) إما لتعطيل أو كبح وحدات Javadoc ذات الصلة. إليك كيف يمكنك القيام بذلك:

### الخيار 1: تعطيل فحوصات Javadoc ذات الصلة
يحتوي Checkstyle على عدة وحدات متعلقة بـ Javadoc، مثل `JavadocMethod`، و`JavadocType`، و`JavadocVariable`، و`JavadocStyle`، و`JavadocPackage`. لتعطيلها، تأكد من إزالة هذه الوحدات أو تعليقها في ملف التكوين. على سبيل المثال:

```xml
<module name="Checker">
    <!-- وحدات أخرى -->
    <!-- علّق أو أزل فحوصات Javadoc ذات الصلة -->
    <!--
    <module name="JavadocMethod"/>
    <module name="JavadocType"/>
    <module name="JavadocVariable"/>
    <module name="JavadocStyle"/>
    <module name="JavadocPackage"/>
    -->
</module>
```

إذا لم تكن هذه الوحدات موجودة في تكوينك، فلن يفرض Checkstyle فحوصات Javadoc.

### الخيار 2: كبح فحوصات Javadoc باستخدام عوامل التصفية للكبح
يمكنك استخدام `SuppressionFilter` الخاص بـ Checkstyle لكبح جميع فحوصات Javadoc ذات الصلة عبر قاعدة التعليمات البرمجية الخاصة بك. أضف قاعدة كبح إلى ملف كبح منفصل (مثل `suppressions.xml`) وأشر إليه في تكوين Checkstyle الخاص بك.

1. **قم بإنشاء ملف كبح** (مثل `suppressions.xml`):
   ```xml
   <!DOCTYPE suppressions PUBLIC
       "-//Checkstyle//DTD Suppression DTD 1.0//EN"
       "https://checkstyle.org/dtds/suppressions_1_0.dtd">
   <suppressions>
       <!-- كبح جميع فحوصات Javadoc ذات الصلة -->
       <suppress checks="Javadoc.*" files=".*"/>
   </suppressions>
   ```

   النمط `checks="Javadoc.*"` يطابق جميع الفحوصات التي تبدأ بـ "Javadoc" (مثل `JavadocMethod`، `JavadocType`، إلخ)، و `files=".*"` يطبق الكبح على جميع الملفات.

2. **أشر إلى ملف الكبح في تكوين Checkstyle الخاص بك**:
   ```xml
   <module name="Checker">
       <module name="SuppressionFilter">
           <property name="file" value="suppressions.xml"/>
       </module>
       <!-- وحدات أخرى -->
   </module>
   ```

### الخيار 3: استخدام شرح `@SuppressWarnings`
إذا كنت تريد كبح فحوصات Javadoc لفئات أو طرق محددة، يمكنك استخدام شرح `@SuppressWarnings("checkstyle:javadoc")` في كود Java الخاص بك. على سبيل المثال:

```java
@SuppressWarnings("checkstyle:javadoc")
public class MyClass {
    // الكود بدون Javadoc لن يتسبب في ظهور مخالفات
}
```

هذا الأسلوب مفيد للكبح المستهدف ولكنه يتطلب إضافة شروح إلى الكود، مما قد لا يكون مثاليًا لتعطيل فحوصات Javadoc بشكل عام.

### ملاحظات
- **تحقق من تكوينك**: بعد تعديل التكوين، قم بتشغيل Checkstyle للتأكد من عدم الإبلاغ عن مخالفات Javadoc ذات الصلة. على سبيل المثال، استخدم الأمر:
  ```bash
  java -jar checkstyle.jar -c checkstyle.xml YourSourceFiles
  ```
- **وحدات Javadoc الشائعة**: تأكد من معالجة جميع الوحدات ذات الصلة، بما في ذلك `JavadocMethod`، و`JavadocType`، و`JavadocVariable`، و`JavadocStyle`، و`JavadocPackage`، و`MissingJavadocMethod`، و`MissingJavadocType`، و`InvalidJavadocPosition`.
- **إصدار Checkstyle**: قد تختلف أسماء الوحدات النمطية وبناء جملة الكبح قليلاً اعتمادًا على إصدار Checkstyle الخاص بك. الأمثلة أعلاه متوافقة مع Checkstyle 8.x والإصدارات الأحدث.
- **كبح عام**: يُعد أسلوب `SuppressionFilter` (الخيار 2) عادةً أنظف طريقة لتعطيل جميع فحوصات Javadoc دون تعديل التكوين الأساسي بشكل مكثف.

إذا كنت تستخدم أداة بناء محددة مثل Maven أو Gradle، فأخبرني، ويمكنني تقديم إرشادات إضافية حول دمج تكوين Checkstyle المحدث!