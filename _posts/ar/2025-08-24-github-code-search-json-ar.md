---
audio: false
generated: true
image: false
lang: ar
layout: post
title: نصائح البحث في كود GitHub بصيغة JSON
translated: true
type: note
---

يمكنك كتابة استعلام بحث GitHub للشفرة بهذا الشكل:

```
"deepseek/deepseek-chat-v3.1" language:JSON
```

### ملاحظات:

* تضمن علامات الاقتباس أن يبحث GitHub عن السلسلة النصية الدقيقة `deepseek/deepseek-chat-v3.1`.
* `language:JSON` (أو `lang:json`، كلاهما يعمل) يقتصر النتائج على ملفات JSON.
* إذا كنت تريد تضمين ملفات إعدادات تشبه JSON ولكنها ليست في ملفات `.json` (مثل `.ipynb` أو `.eslintrc`)، يمكنك إزالة عامل التصفية `lang:`.

أمثلة:

* البحث فقط في ملفات JSON:

  ```
  "deepseek/deepseek-chat-v3.1" lang:json
  ```

* البحث في جميع أنواع الملفات مع إبراز نتائج JSON:

  ```
  "deepseek/deepseek-chat-v3.1"
  ```

هل تريد أيضًا أن أوضح لك كيفية تحسين هذا البحث أكثر - على سبيل المثال، البحث فقط داخل المستودعات أو المشكلات أو الشفرة؟