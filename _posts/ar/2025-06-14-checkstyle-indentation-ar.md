---
audio: false
generated: true
lang: ar
layout: post
title: كشف المسافات البادئة في تشيك ستايل
translated: true
type: note
---

أفهم أنك تتساءل عن سبب عدم اكتشاف Checkstyle لعدم المسافة البادئة قبل عبارة `System.out.println` في طريقة `logAfter` الخاصة بك. دعنا نحلل هذا خطوة بخطوة لتحديد المشكلة وإصلاحها.

### لماذا لا يكتشف Checkstyle مشكلة المسافة البادئة؟
يستخدم Checkstyle وحدات محددة لفرض معايير الترميز، وبالنسبة للمسافة البادئة، فإنه يعتمد على وحدة `Indentation`. إذا لم يتم تكوين هذه الوحدة بشكل صحيح أو تضمينها في إعداد Checkstyle الخاص بك، فلن تكتشف أخطاء المسافة البادئة مثل الموجودة في الكود الخاص بك.

إليك الكود الحالي الخاص بك:

```java
package org.lzwjava;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
    System.out.println("Method executed: " + joinPoint.getSignature());  // No indentation
    }
}
```

في اتفاقيات Java القياسية، يجب أن تكون العبارات داخل طريقة (مثل `System.out.println`) ذات مسافة بادئة نسبية لتعريف الطريقة. في الكود الخاص بك، سطر `System.out.println` ليس له مسافة بادئة، وهو ما يجب على Checkstyle الإشارة إليه كخطأ إذا تم تكوينه بشكل صحيح. إليك الأسباب الأكثر احتمالاً لعدم اكتشافه:

1. **وحدة `Indentation` غير مضمنة** في ملف تكوين Checkstyle الخاص بك (مثل `checks.xml`).
2. **الوحدة مضمنة ولكنها غير مكونة بشكل صحيح**، لذا لا تطبق قواعد المسافة البادئة المتوقعة.
3. **تكوينك يستثني ملفات أو حزم معينة**، مما يمنع الفحص من التشغيل على هذا الكود.
4. **هناك مشكلة في كيفية تشغيل Checkstyle** (عبر Maven أو بيئة التطوير المتكاملة IDE)، تتجاوز السلوك المتوقع.

دعنا نتعامل مع هذه الاحتمالات ونصلحها.

---

### الخطوة 1: التحقق من وحدة `Indentation` في التكوين الخاص بك
أولاً، تحقق من ملف تكوين Checkstyle الخاص بك (على الأرجح `checks.xml`) لمعرفة ما إذا كانت وحدة `Indentation` مضمنة. إليك الطريقة:

1. **حدد موقع ملف `checks.xml` الخاص بك**. يكون عادةً في دليل المشروع الخاص بك (مثل `/home/lzw/Projects/blog-server/checks.xml` إذا كنت تستخدم إعدادًا مشابهًا).
2. **ابحث عن وحدة `Indentation`** داخل قسم `TreeWalker`. يجب أن تبدو هكذا:

   ```xml
   <module name="TreeWalker">
       <!-- Other checks -->
       <module name="Indentation">
           <property name="basicOffset" value="4"/>  <!-- 4 spaces per indentation level -->
           <property name="lineWrappingIndentation" value="4"/>  <!-- Optional: for wrapped lines -->
       </module>
       <!-- Other checks -->
   </module>
   ```

   - **إذا لم تر هذه الوحدة**، فهذه هي المشكلة—Checkstyle لا يتحقق من المسافة البادئة على الإطلاق.
   - **إذا كانت موجودة**، تحقق من أن `basicOffset` مضبوط على قيمة معقولة (مثل 4 مسافات، وهو المعيار في Java).

---

### الخطوة 2: إضافة أو إصلاح وحدة `Indentation`
إذا كانت الوحدة مفقودة أو غير مضبوطة بشكل صحيح، إليك كيفية إصلاحها:

#### إذا كانت مفقودة: أضف وحدة `Indentation`
أضف ما يلي داخل قسم `TreeWalker` في ملف `checks.xml` الخاص بك:

```xml
<module name="Indentation">
    <property name="basicOffset" value="4"/>  <!-- 4 spaces is typical -->
    <property name="lineWrappingIndentation" value="4"/>
</module>
```

#### إذا كانت موجودة: تحقق من الإعدادات
تأكد من:
- أن `basicOffset` مضبوط على عدد المسافات الذي تتوقعه للمسافة البادئة (مثل 4).
- عدم وجود خصائص تعطل أو تتجاوز الفحص بطريقة تتخطى الكود الخاص بك.

احفظ الملف بعد إجراء التغييرات.

---

### الخطوة 3: التحقق من الاستثناءات
في بعض الأحيان، تستثني تكوينات Checkstyle ملفات أو حزم معينة. في ملف `checks.xml` الخاص بك، ابحث عن:
- `SuppressionFilter` أو `SuppressionCommentFilter` قد يتخطى حزمة `org.lzwjava` أو هذا الملف المحدد.
- أي أنماط تستثني ملفات `.java` أو أدلة محددة.

إذا وجدت مثل هذا الاستثناء يؤثر على الكود الخاص بك، فقم بإزالته أو تعديله بحيث يتم فحص `DebugAspect.java`.

---

### الخطوة 4: اختبار الإصلاح
بعد تحديث التكوين الخاص بك، قم بتشغيل Checkstyle مرة أخرى. إذا كنت تستخدم Maven، على سبيل المثال:

```bash
mvn clean checkstyle:check
```

تحقق من الناتج. يجب أن ترى خطأً مثل:

```
[ERROR] DebugAspect.java:13: 'System.out.println' should be indented +4 spaces relative to its enclosing block.
```

هذا يشير إلى أن Checkstyle يكتشف الآن عدم وجود مسافة بادئة. للرجوع، إليك كيف يجب أن يبدو الكود الخاص بك *بالمسافة البادئة الصحيحة*:

```java
@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
        System.out.println("Method executed: " + joinPoint.getSignature());  // 4 spaces indent
    }
}
```

---

### الخطوة 5: استكشاف الأخطاء وإصلاحها إذا لم تنجح العملية
إذا كان Checkstyle لا يزال لا يكتشف المشكلة:
- **التشغيل مع ناتج التصحيح**: استخدم أمرًا مفصلًا لترى ما يفعله Checkstyle:
  ```bash
  mvn -X checkstyle:check
  ```
  ابحث عن رسائل حول وحدة `Indentation` أو الملفات التي تم تخطيها.
- **الاختبار بتكوين أدنى**: أنشئ `checks.xml` مؤقتًا يحتوي فقط على فحص `Indentation`:
  ```xml
  <?xml version="1.0"?>
  <!DOCTYPE module PUBLIC
      "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
      "https://checkstyle.org/dtds/configuration_1_3.dtd">
  <module name="Checker">
      <module name="TreeWalker">
          <module name="Indentation">
              <property name="basicOffset" value="4"/>
          </module>
      </module>
  </module>
  ```
  وجّه Checkstyle إلى هذا الملف واختبر مرة أخرى لعزل المشكلة.
- **تحقق من إعدادك**: إذا كنت تشغل Checkstyle عبر بيئة تطوير متكاملة (مثل IntelliJ أو Eclipse)، فتأكد من أن بيئة التطوير المتكاملة تستخدم `checks.xml` المحدث وليس تكوينًا قديمًا أو منفصلاً.

---

### الخلاصة
Checkstyle لا يكتشف عدم المسافة البادئة لأن وحدة `Indentation` على الأرجح مفقودة أو غير مكونة بشكل صحيح في ملف `checks.xml` الخاص بك. من خلال إضافة أو تصحيح هذه الوحدة والتأكد من عدم تطبيق أي استثناءات، يجب على Checkstyle الإشارة إلى عدم وجود مسافة بادئة قبل `System.out.println`. قم بتحديث التكوين كما هو موضح، وأعد تشغيل Checkstyle، ويجب أن ترى الخطأ مُبلغًا عنه كما هو متوقع. دعني أعرف إذا كنت بحاجة إلى مساعدة في الخطوات التالية!