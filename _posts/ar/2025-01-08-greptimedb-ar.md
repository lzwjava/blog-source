---
audio: false
generated: false
image: false
lang: ar
layout: post
title: الشركات يجب أن تقدم سياق الذكاء الاصطناعي لتسهيل التكامل
translated: true
---

لدي صديق يعمل في Greptime DB، وقد كنت أفكر في كيفية دمج منتجهم بسرعة في الأنظمة الموجودة.

## السياق

من الممكن أن يكون أحد الطرق هو تقديم المزيد من السياق الذكائي. يمكن لـ Greptime DB تنظيم وثائقه بطريقة متوافق مع أدوات الذكاء الاصطناعي مثل ChatGPT، مما يسهل عملية الدمج.

تقدم Greptime DB الوثائق على [https://greptime.com](https://greptime.com)، لكنني أتساءل ما إذا كان أدوات مثل ChatGPT أو DeepSeek قادرة على معالجة جميع الصفحات في الوثائق الخاصة بهم بكفاءة. بالإضافة إلى ذلك، هناك كم هائل من المعلومات منتشر عبر مستودعات GitHub، والمشاكل، والوثائق الداخلية، والوثائق العامة، وقطع من المعرفة المخفية التي لا تُوثق بشكل صريح.

لحل هذه المشكلة، قد تحتاج Greptime DB إلى إنشاء عدة GPTs متخصصة. على سبيل المثال، يمكنهم إنشاء تعليقات مثل هذه:

```

### وثائق Greptime:
الوثائق الرسمية متاحة على: [https://docs.greptime.com](https://docs.greptime.com)

* [دليل البدء السريع](https://docs.greptime.com/getting-started/quick-start)
* [دليل المستخدم](https://docs.greptime.com/user-guide/overview)
* [النماذج التجريبية](https://github.com/GreptimeTeam/demo-scene)
* [الأسئلة الشائعة](https://docs.greptime.com/faq-and-others/faq)

### روابط المستودعات:
هنا بعض المجلدات والمجلدات الرئيسية من جذر مستودع GreptimeDB:

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)

الملفات الرئيسية الإضافية:

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)

يرجى البحث في هذه الموارد قبل الإجابة على أي استفسارات من المستخدمين.

```

هذا سيتيح للمستخدمين التفاعل مع روبوت محادثة قائم على GPT الذي يجيب على الأسئلة بناءً على الوثائق، مما يضمن إجابات أكثر دقة.

دعونا ننشئ هذا GPT: [https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

لم أستطع الإجابة على هذا السؤال:

```
ما هو `greptimedb/src/query/src/query_engine/context.rs` عن؟
```

## الوكيل

أتصور أداة تسمى `greptimedb-agent` لتسهيل عملية الدمج.

تخيل تشغيل أمر بسيط مثل:

```bash
pip install greptimedb-agent
greptimedb-agent
```

سيجمع `greptimedb-agent` بشكل ذكي المعلومات عن النظام الحالي، مثل تفاصيل الآلة والرمم الموجودة، من أجل فهم السياق وقرار أفضل طريقة لدمج Greptime DB.

سيحدث هذا الأمر تلقائيًا تحديثات لكودك لدمج Greptime DB، واستبدال قاعدة بياناتك الحالية بـ Greptime DB في خطوات قليلة.