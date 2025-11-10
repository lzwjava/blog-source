---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: نظرة عامة على إزالة التسلسل متعدد الأشياء لجاكسون
translated: true
type: note
---

### نظرة عامة على إزالة التسلسل متعدد الأشكال في Jackson

Jackson هي مكتبة جافا لتسلسل وإزالة تسلسل JSON. تسمح إزالة التسلسل متعددة الأشكال لـ Jackson بإنشاء الفئة الفرعية الصحيحة لفئة أساس تلقائيًا أثناء إزالة التسلسل، بناءً على معلومات النوع المضمنة في JSON. هذا مفيد عند التعامل مع تسلسلات الوراثة، مما يضمن إنشاء نوع الكائن الصحيح من بيانات JSON.

المكونات الرئيسية:
- **@JsonTypeInfo**: تعريفات تتحكم في مكان وكيفية تخزين معلومات النوع في JSON.
- **@JsonSubTypes**: تعريفات تسرد الفئات الفرعية (الأنواع الفرعية) ومعرفاتها.
- يتعامل قرار النوع الفرعي في Jackson مع التعيين.

بدون هذه، ستقوم Jackson افتراضيًا بإزالة تسلسل جميع الكائنات كالفئة الأساسية، مما قد يؤدي إلى فقدان البيانات المحددة للفئة الفرعية.

### كيف تعمل خطوة بخطوة

1. **التعريفات على الفئة الأساسية**:
   - استخدم `@JsonTypeInfo` لتحديد مكان تضمين معلومات النوع (مثل خاصية في كائن JSON).
   - مثال:
     ```java
     @JsonTypeInfo(use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY, property = "@type")
     @JsonSubTypes({
         @JsonSubType(value = Cat.class, name = "cat"),
         @JsonSubType(value = Dog.class, name = "dog")
     })
     public abstract class Animal {
         public String name;
     }
     ```
     - `use = JsonTypeInfo.Id.NAME`: يستخدم اسم (معرف سلسلة) للنوع.
     - `include = JsonTypeInfo.As.PROPERTY`: يضيف معلومات النوع كخاصية ("@type") في كائن JSON.
     - `@JsonSubTypes`: يعين أسماء الفئات الفرعية إلى فئات جافا الخاصة بها (مثل "cat" → Cat.class).

2. **عملية التسلسل**:
   - عند تسلسل كائن Cat أو Dog، تضيف Jackson معرف النوع إلى JSON.
   - مثال الناتج: `{"@type": "cat", "name": "Whiskers", "purr": true}` (إذا كان لدى Cat حقل "purr").

3. **عملية إزالة التسلسل**:
   - تقرأ Jackson ملف JSON وتتحقق من معلومات النوع (مثل الخاصية "@type").
   - تعين المعرف ("cat") مرة أخرى إلى الفئة الفرعية المسجلة (Cat.class) باستخدام `@JsonSubTypes`.
   - تقوم بإنشاء الفئة الفرعية الصحيحة وتملأ حقولها.
   - إذا لم يكن هناك تطابق أو كانت معلومات النوع مفقودة، فإنها ترجع إلى الفئة الأساسية أو تطرح استثناءات (قابلة للتكوين عبر `defaultImpl`).

4. **تنسيقات معلومات النوع المدعومة**:
   - `@JsonTypeInfo.As.PROPERTY`: النوع كحقل (مثل `{"@type": "cat", ...}`).
   - `@JsonTypeInfo.As.WRAPPER_OBJECT`: يلف الكائن في غلاف مع النوع كمفتاح (مثل `{"cat": {...}}`).
   - `@JsonTypeInfo.As.WRAPPER_ARRAY`: يستخدم تنسيق المصفوفة.
   - `@JsonTypeInfo.As.EXTERNAL_PROPERTY`: معلومات النوع في حقل منفصل (متقدم، لهياكل شبيهة بـ XML).

### التكوين المتقدم والحالات الطرفية

- **معينات الأسماء المخصصة**: استخدم `@JsonTypeInfo(use = JsonTypeInfo.Id.CLASS)` لتضمين اسم الفئة المؤهل بالكامل مباشرة في JSON (مثل `{"@class": "com.example.Cat", ...}`)، والذي يمكن أن يكون هشًا عبر إعادة الهيكلة.
- **التنفيذ الافتراضي**: أضف `defaultImpl = Animal.class` للتراجع إذا كانت معلومات النوع مفقودة.
- **الرؤية و Mix-Ins**: طبق التعريفات عبر فئات mix-in إذا لم تتمكن من تعديل الفئات المصدر.
- **معالجة الأخطاء**: إذا لم تتطابق معلومات النوع مع نوع فرعي مسجل، تطرح Jackson `JsonMappingException`. يمكن التعامل مع هذا باستخدام مزيلات التسلسل المخصصة.
- **الأداء**: الحد الأدنى من النفقات العامة أثناء إزالة التسلسل بسبب عمليات البحث الفعالة، لكن تضمين معلومات النوع يزيد من حجم حمولة JSON.

للحصول على الوثائق الكاملة، انظر الدليل الرسمي لـ Jackson: [Polymorphic Type Handling](https://github.com/FasterXML/jackson-docs/wiki/JacksonPolymorphicDeserialization). كانت هذه الميزة مستقرة منذ Jackson 2.x، مع مفاهيم مماثلة في مكتبات JSON أخرى مثل Gson. إذا كنت تقوم بالتخصيص أكثر، فقم بتوسيع `PolymorphicTypeValidator` للأمان في المدخلات غير الموثوقة.